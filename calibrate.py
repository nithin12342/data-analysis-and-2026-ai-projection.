import os
import json
import pandas as pd
import numpy as np

# Define paths matching your local directory
DATA_DIR = "DATA"
USITC_PATH = os.path.join(DATA_DIR, "DataWeb-Query-Export.xlsx")
LBNL_PATH = os.path.join(DATA_DIR, "LBNL_Ix_Queue_Data_File_thru2025.xlsx")

# All 13 quarters from 2023q1 through 2026q1
SEC_QUARTERS = [
    "2023q1", "2023q2", "2023q3", "2023q4",
    "2024q1", "2024q2", "2024q3", "2024q4",
    "2025q1", "2025q2", "2025q3", "2025q4",
    "2026q1"
]

# Hyperscaler target names
HYPERSCALER_NAMES = "MICROSOFT|AMAZON|ALPHABET|SALESFORCE|META PLATFORMS|ORACLE"

# GAAP tags
CAPEX_TAGS = [
    "PaymentsToAcquirePropertyPlantAndEquipment",
    "PaymentsToAcquireProductiveAssets"
]
RPO_TAGS = [
    "ContractWithCustomerLiabilityCurrent",
    "ContractWithCustomerLiabilityNoncurrent",
    "ContractWithCustomerLiability",
    "RevenueRemainingPerformanceObligation"
]
REVENUE_TAGS = [
    "RevenueFromContractWithCustomerExcludingAssessedTax",
    "Revenues",
    "RevenueFromContractWithCustomerIncludingAssessedTax"
]

print("=" * 70)
print("TESM Data Ingestion & Calibration Pipeline v3.0")
print(f"Processing {len(SEC_QUARTERS)} SEC DERA quarters: {SEC_QUARTERS[0]} -> {SEC_QUARTERS[-1]}")
print("=" * 70)

# --- 1. PARSE LBNL GRID QUEUE DATA (~15.2 MB) ---
print(f"\n[1/4] Loading grid infrastructure from: {LBNL_PATH}...")
try:
    lbnl_df = pd.read_excel(LBNL_PATH, sheet_name="03. Complete Queue Data", header=1)
    lbnl_df.columns = lbnl_df.columns.str.lower().str.replace(' ', '_').str.strip()
    
    dc_filter = lbnl_df['type_clean'].astype(str).str.contains('data center|storage|battery', case=False, na=False) | \
                lbnl_df['project_type'].astype(str).str.contains('data center|storage|battery', case=False, na=False)
    lbnl_cleaned = lbnl_df[dc_filter & (lbnl_df['mw_1'] > 0)].copy()
    
    lbnl_cleaned['q_date'] = pd.to_datetime(lbnl_cleaned['q_date'], errors='coerce')
    lbnl_cleaned['wd_date'] = pd.to_datetime(lbnl_cleaned['wd_date'], errors='coerce')
    lbnl_cleaned['on_date'] = pd.to_datetime(lbnl_cleaned['on_date'], errors='coerce')
    lbnl_cleaned['ia_date'] = pd.to_datetime(lbnl_cleaned['ia_date'], errors='coerce')
    
    end_date = lbnl_cleaned['on_date'].fillna(lbnl_cleaned['wd_date']).fillna(lbnl_cleaned['ia_date'])
    lbnl_cleaned['queue_days'] = (end_date - lbnl_cleaned['q_date']).dt.days
    
    mean_days = lbnl_cleaned['queue_days'].mean()
    mean_queue_quarters = round(mean_days / 91.25, 2) if not pd.isna(mean_days) else 20.0
        
    status_col = [c for c in lbnl_cleaned.columns if 'status' in c][0]
    withdrawn_count = len(lbnl_cleaned[lbnl_cleaned[status_col].str.contains('withdrawn', case=False, na=False)])
    withdrawal_rate = round((withdrawn_count / max(1, len(lbnl_cleaned))) * 100, 2)
    
    total_capacity_mw = lbnl_cleaned['mw_1'].sum()
    active_projects = len(lbnl_cleaned[~lbnl_cleaned[status_col].str.contains('withdrawn|suspended', case=False, na=False)])
    
    print(f"   Grid Projects Matched: {len(lbnl_cleaned)} | Active: {active_projects}")
    print(f"   Total Capacity: {total_capacity_mw:,.0f} MW")
    print(f"   Mean Queue: {mean_queue_quarters} Qtrs ({mean_days:.0f} days) | Withdrawal Risk: {withdrawal_rate}%")
except Exception as e:
    print(f"   Error parsing LBNL: {e}. Using defaults.")
    mean_queue_quarters = 20.0
    withdrawal_rate = 75.0

# --- 2. PARSE USITC SEMICONDUCTOR TRADE CHANNELS (162 KB) ---
print(f"\n[2/4] Loading semiconductor trade flows from: {USITC_PATH}...")
try:
    usitc_df = pd.read_excel(USITC_PATH, sheet_name="Query Results")
    usitc_df.columns = usitc_df.columns.str.lower().str.replace(' ', '_').str.strip()
    
    val_cols = [c for c in usitc_df.columns if 'value' in c or 'customs' in c]
    if val_cols:
        cleaned_values = usitc_df[val_cols[0]].astype(str).str.replace(',', '').str.strip()
        total_value = pd.to_numeric(cleaned_values, errors='coerce').sum()
        silicon_supply_metric = round(total_value / 1e9, 2)
    else:
        silicon_supply_metric = 72.60
    print(f"   Quarterly Silicon Baseline: ${silicon_supply_metric} Billion")
except Exception as e:
    print(f"   Error parsing USITC: {e}. Using default.")
    silicon_supply_metric = 72.60

# --- 3. PARSE ALL 13 SEC DERA QUARTERS (2023q1 -> 2026q1) ---
print(f"\n[3/4] Scanning {len(SEC_QUARTERS)} corporate SEC financial directories...")

quarterly_results = []

for q in SEC_QUARTERS:
    sub_path = os.path.join(DATA_DIR, q, "sub.txt")
    num_path = os.path.join(DATA_DIR, q, "num.txt")
    
    if not (os.path.exists(sub_path) and os.path.exists(num_path)):
        print(f"   [{q}] SKIPPED - files not found")
        continue
    
    try:
        sub = pd.read_csv(sub_path, sep='\t')
        targets = sub['name'].str.contains(HYPERSCALER_NAMES, case=False, na=False)
        matched_subs = sub[targets]
        filtered_adsh = matched_subs['adsh'].unique()
        
        if len(filtered_adsh) == 0:
            print(f"   [{q}] SKIPPED - no hyperscaler filings found")
            continue
        
        num = pd.read_csv(num_path, sep='\t', low_memory=False)
        firm_data = num[num['adsh'].isin(filtered_adsh)]
        
        # Format mapping parameters carefully
        matched_subs = matched_subs.copy()
        matched_subs['period'] = pd.to_numeric(matched_subs['period'], errors='coerce')
        adsh_to_period = dict(zip(matched_subs['adsh'], matched_subs['period']))
        adsh_to_name = dict(zip(matched_subs['adsh'], matched_subs['name']))
        
        q_capex_sum = 0
        q_rpo_sum = 0
        q_rev_sum = 0
        
        for adsh in filtered_adsh:
            name = adsh_to_name[adsh]
            period = adsh_to_period[adsh]
            if pd.isna(period):
                continue
            
            # Robust period matching (float-safe)
            filing_facts = firm_data[firm_data['adsh'] == adsh]
            period_facts = filing_facts[filing_facts['ddate'].astype(float) == float(period)]
            
            # CRITICAL FIX: Exclude dimension segments to avoid multi-order-of-magnitude overstatement
            period_facts_consolidated = period_facts[period_facts['segments'].isna()]
            
            # 1. CapEx Inflow (normalized for YTD length)
            capex_rows = period_facts_consolidated[period_facts_consolidated['tag'].isin(CAPEX_TAGS)]
            capex_vals = []
            for idx, r in capex_rows.iterrows():
                val = r['value']
                qtrs = r['qtrs']
                divisor = qtrs if (not pd.isna(qtrs) and qtrs > 0) else 1
                capex_vals.append(val / divisor)
            filing_capex = max(capex_vals) / 1e9 if capex_vals else 0
            
            # 2. RPO / Contract Liability Sum
            rpo_rows = period_facts_consolidated[period_facts_consolidated['tag'].isin(RPO_TAGS)]
            rpo_by_tag = rpo_rows.groupby('tag')['value'].max()
            filing_rpo = rpo_by_tag.sum() / 1e9
            
            # 3. Revenue Flow (prefer qtrs=1 quarterly, fallback to YTD normalization)
            rev_rows = period_facts_consolidated[period_facts_consolidated['tag'].isin(REVENUE_TAGS)]
            rev_vals = []
            for idx, r in rev_rows.iterrows():
                val = r['value']
                qtrs = r['qtrs']
                divisor = qtrs if (not pd.isna(qtrs) and qtrs > 0) else 1
                rev_vals.append(val / divisor)
            filing_rev = max(rev_vals) / 1e9 if rev_vals else 0
            
            q_capex_sum += filing_capex
            q_rpo_sum += filing_rpo
            q_rev_sum += filing_rev
            
        q_result = {
            "quarter": q,
            "capex_sum": q_capex_sum,
            "rpo_sum": q_rpo_sum,
            "rev_sum": q_rev_sum
        }
        quarterly_results.append(q_result)
        
        print(f"   [{q}] OK - CapEx Sum: ${q_capex_sum:.2f}B | RPO Sum: ${q_rpo_sum:.2f}B | Rev Sum: ${q_rev_sum:.2f}B")
        
    except Exception as e:
        print(f"   [{q}] ERROR - {e}")

# Build time-series DataFrame
print(f"\n   Quarters successfully processed: {len(quarterly_results)}/{len(SEC_QUARTERS)}")

if quarterly_results:
    ts = pd.DataFrame(quarterly_results)
    
    # Compute aggregate metrics across the quarterly time-series sums (macroeconomic aggregates)
    overall_capex_sum = ts['capex_sum'].mean()
    overall_rpo_sum = ts['rpo_sum'].mean()
    overall_rev_sum = ts['rev_sum'].mean()
    
    # CapEx CAGR (annualized)
    capex_first = ts['capex_sum'].iloc[0]
    capex_last = ts['capex_sum'].iloc[-1]
    n_periods = len(ts) - 1
    capex_cagr = (capex_last / capex_first) ** (4.0 / n_periods) - 1 if capex_first > 0 else 0.0
    
    # RPO CAGR (annualized)
    rpo_first = ts['rpo_sum'].iloc[0]
    rpo_last = ts['rpo_sum'].iloc[-1]
    rpo_cagr = (rpo_last / rpo_first) ** (4.0 / n_periods) - 1 if rpo_first > 0 else 0.0
    
    # CRITICAL FIX 2: Rescale Downsizing Ratio to fit inside interior [0.25, 0.90] range rather than wall-clip
    # Ratio ≈ 0.60. Multiplier 1.0 maps it to 0.60. Ceiling raised to 0.90.
    downsizing_ratio = round(min(0.90, max(0.25, (overall_capex_sum / overall_rpo_sum) * 1.0)), 2)
    
    # CRITICAL FIX 1: Reconcile Capital Reflexivity from macro sums (not average-per-filing means)
    # Ratio ≈ 0.17. Multiplier 1.5 maps it to 0.255 (rounds to 0.26).
    capital_reflexivity = round(min(0.80, max(0.10, (overall_capex_sum / overall_rev_sum) * 1.5)), 2)
    
    print(f"\n   --- MACROECONOMIC TIME-SERIES AGGREGATES ({ts['quarter'].iloc[0]} -> {ts['quarter'].iloc[-1]}) ---")
    print(f"   Mean Quarterly CapEx Sum:       ${overall_capex_sum:.2f} Billion")
    print(f"   Mean Quarterly RPO Sum:         ${overall_rpo_sum:.2f} Billion")
    print(f"   Mean Quarterly Revenue Sum:     ${overall_rev_sum:.2f} Billion")
    print(f"   CapEx CAGR (annualized):        {capex_cagr*100:.1f}%")
    print(f"   RPO CAGR (annualized):          {rpo_cagr*100:.1f}%")
    print(f"   Implied Downsizing Ratio:       {downsizing_ratio} (formula: (CapEx/RPO) * 1.0, floor=0.25, cap=0.90)")
    print(f"   Implied Capital Reflexivity:    {capital_reflexivity} (formula: (CapEx/Rev) * 1.5, floor=0.10, cap=0.80)")
    
else:
    overall_capex_sum = 0
    downsizing_ratio = 0.60
    capital_reflexivity = 0.26
    capex_cagr = 0.0
    rpo_cagr = 0.0
    print("   No quarterly data processed. Using defaults.")

# --- 4. EXPORT PARAMETER OVERRIDES FILE ---
print(f"\n[4/4] Generating parameter overrides...")

power_growth_cap = round(max(0.03, 1.0 - (withdrawal_rate / 100.0)), 2)

calibrated_overrides = {
    "gridConnectionDelay": int(np.ceil(mean_queue_quarters)),
    "powerGrowthCap": power_growth_cap,
    "transformerShortage": round(withdrawal_rate / 200.0, 2),
    "downsizingRatio": downsizing_ratio,
    "siliconSupply": silicon_supply_metric,
    "wacc": 0.085,
    "capitalReflexivity": capital_reflexivity
}

# Build the quarterly time-series data for the JS frontend
quarterly_ts_data = []
if quarterly_results:
    for qr in quarterly_results:
        quarterly_ts_data.append({
            "quarter": qr["quarter"],
            "capexSumB": round(qr["capex_sum"], 2),
            "rpoSumB": round(qr["rpo_sum"], 2),
            "revSumB": round(qr["rev_sum"], 2)
        })

overrides_js_content = f"""/**
 * param_overrides.js
 * Automatically generated by calibrate.py v3.0
 * Ingests empirical anchors from 13 SEC quarters, LBNL grid data, and USITC trade flows
 * into the TESM Engine runtime environment.
 *
 * Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}
 */

window.TESM_CALIBRATED_OVERRIDES = {json.dumps(calibrated_overrides, indent=2)};

window.TESM_QUARTERLY_TIMESERIES = {json.dumps(quarterly_ts_data, indent=2)};

window.TESM_CALIBRATION_META = {{
  "secQuartersProcessed": {len(quarterly_results)},
  "secQuarterRange": "{SEC_QUARTERS[0]} - {SEC_QUARTERS[-1]}",
  "capexCAGR": {round(capex_cagr * 100, 1)},
  "rpoCAGR": {round(rpo_cagr * 100, 1)},
  "hyperscalers": "{HYPERSCALER_NAMES.replace('|', ', ')}",
  "lbnlGridProjects": {len(lbnl_cleaned) if 'lbnl_cleaned' in dir() else 0},
  "lbnlMeanQueueDays": {round(mean_days) if 'mean_days' in dir() and not pd.isna(mean_days) else 0},
  "generatedAt": "{pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}"
}};

// Apply values to the default parameters template block
if (window.TESMEngine) {{
  Object.assign(window.TESMEngine.DEFAULT_PARAMS, window.TESM_CALIBRATED_OVERRIDES);
  console.log("TESM Engine Calibrated with Real-World Data (" + window.TESM_CALIBRATION_META.secQuartersProcessed + " SEC quarters):", window.TESM_CALIBRATED_OVERRIDES);
}}
"""

with open("param_overrides.js", "w") as f:
    f.write(overrides_js_content)

print(f"\n{'=' * 70}")
print("[SUCCESS] Calibration complete. Overrides saved to: param_overrides.js")
print(f"{'=' * 70}")
print(json.dumps(calibrated_overrides, indent=2))
