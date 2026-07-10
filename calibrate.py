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

# New data source paths
ADOPTION_DIR = os.path.join(DATA_DIR, "adoption")
CHINA_DIR = os.path.join(DATA_DIR, "china")
PRODUCTIVITY_DIR = os.path.join(DATA_DIR, "productivity")
REVENUE_QUALITY_DIR = os.path.join(DATA_DIR, "revenue_quality")
MACRO_DIR = os.path.join(DATA_DIR, "macro")
SEMICONDUCTOR_DIR = os.path.join(DATA_DIR, "semiconductor")
AGENTS_DIR = os.path.join(DATA_DIR, "agents")
REGULATORY_DIR = os.path.join(DATA_DIR, "regulatory")
LABOR_DIR = os.path.join(DATA_DIR, "labor")
UNIT_ECONOMICS_DIR = os.path.join(DATA_DIR, "unit_economics")
STRESS_DIR = os.path.join(DATA_DIR, "stress_scenarios")

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
print(f"\n[3/6] Scanning {len(SEC_QUARTERS)} corporate SEC financial directories...")

# --- 4. LOAD NEW DATA SOURCES ---
print(f"\n[4/6] Loading new data sources...")

# 4a. AI Adoption Telemetry
adoption_path = os.path.join(DATA_DIR, "adoption", "vendor_reported_metrics.csv")
if os.path.exists(adoption_path):
    adoption_df = pd.read_csv(adoption_path)
    print(f"   Adoption metrics: {len(adoption_df)} records loaded")
else:
    print(f"   Adoption metrics: NOT FOUND")

# 4b. Chinese AI Benchmarks
china_benchmarks_path = os.path.join(DATA_DIR, "china", "model_benchmarks.csv")
if os.path.exists(china_benchmarks_path):
    china_benchmarks_df = pd.read_csv(china_benchmarks_path)
    print(f"   Chinese model benchmarks: {len(china_benchmarks_df)} records loaded")
else:
    print(f"   Chinese model benchmarks: NOT FOUND")

# 4c. Chinese API Pricing
china_pricing_path = os.path.join(DATA_DIR, "china", "api_pricing.csv")
if os.path.exists(china_pricing_path):
    china_pricing_df = pd.read_csv(china_pricing_path)
    print(f"   Chinese API pricing: {len(china_pricing_df)} records loaded")
else:
    print(f"   Chinese API pricing: NOT FOUND")

# 4d. Productivity Meta-Analysis
productivity_path = os.path.join(DATA_DIR, "productivity", "meta_analysis_studies.csv")
if os.path.exists(productivity_path):
    productivity_df = pd.read_csv(productivity_path)
    print(f"   Productivity studies: {len(productivity_df)} records loaded")
else:
    print(f"   Productivity studies: NOT FOUND")

# 4e. Macro/Financial Data
macro_path = os.path.join(DATA_DIR, "macro", "fred_series_catalog.csv")
if os.path.exists(macro_path):
    macro_df = pd.read_csv(macro_path)
    print(f"   Macro series catalog: {len(macro_df)} series loaded")
else:
    print(f"   Macro series catalog: NOT FOUND")

# 4e. Semiconductor Supply Chain
semi_path = os.path.join(DATA_DIR, "semiconductor", "supply_chain_quarterly.csv")
if os.path.exists(semi_path):
    semi_df = pd.read_csv(semi_path)
    print(f"   Semi supply chain: {len(semi_df)} quarters loaded")
else:
    print(f"   Semi supply chain: NOT FOUND")

# 4f. Enterprise AI Agent Deployments
agents_path = os.path.join(DATA_DIR, "agents", "deployment_counts.csv")
if os.path.exists(agents_path):
    agents_df = pd.read_csv(agents_path)
    print(f"   Agent deployments: {len(agents_df)} records loaded")
else:
    print(f"   Agent deployments: NOT FOUND")

# 4g. Regulatory Scenario Database
regulatory_path = os.path.join(DATA_DIR, "regulatory", "jurisdiction_rule_matrix.csv")
if os.path.exists(regulatory_path):
    regulatory_df = pd.read_csv(regulatory_path)
    print(f"   Regulatory rules: {len(regulatory_df)} records loaded")
else:
    print(f"   Regulatory rules: NOT FOUND")

# 4h. Labor Market Transformation
labor_path = os.path.join(DATA_DIR, "labor", "onet_ai_exposure.csv")
if os.path.exists(labor_path):
    labor_df = pd.read_csv(labor_path)
    print(f"   Labor O*NET exposure: {len(labor_df)} occupations loaded")
else:
    print(f"   Labor O*NET exposure: NOT FOUND")

# 4i. Unit Economics
unit_eco_path = os.path.join(DATA_DIR, "unit_economics", "training_costs.csv")
if os.path.exists(unit_eco_path):
    unit_eco_df = pd.read_csv(unit_eco_path)
    print(f"   Unit economics (training): {len(unit_eco_df)} records loaded")
else:
    print(f"   Unit economics (training): NOT FOUND")

unit_eco_inf_path = os.path.join(DATA_DIR, "unit_economics", "inference_costs.csv")
if os.path.exists(unit_eco_inf_path):
    unit_eco_inf_df = pd.read_csv(unit_eco_inf_path)
    print(f"   Unit economics (inference): {len(unit_eco_inf_df)} records loaded")
else:
    print(f"   Unit economics (inference): NOT FOUND")

unit_eco_gpu_path = os.path.join(DATA_DIR, "unit_economics", "gpu_economics.csv")
if os.path.exists(unit_eco_gpu_path):
    unit_eco_gpu_df = pd.read_csv(unit_eco_gpu_path)
    print(f"   Unit economics (GPU): {len(unit_eco_gpu_df)} records loaded")
else:
    print(f"   Unit economics (GPU): NOT FOUND")

unit_eco_saas_path = os.path.join(DATA_DIR, "unit_economics", "saas_benchmarks.csv")
if os.path.exists(unit_eco_saas_path):
    unit_eco_saas_df = pd.read_csv(unit_eco_saas_path)
    print(f"   Unit economics (SaaS): {len(unit_eco_saas_df)} records loaded")
else:
    print(f"   Unit economics (SaaS): NOT FOUND")

# 4j. Cloud Revenue Quality Mapping
cloud_rev_path = os.path.join(DATA_DIR, "revenue_quality", "cloud_contract_mapping.csv")
if os.path.exists(cloud_rev_path):
    cloud_rev_df = pd.read_csv(cloud_rev_path)
    print(f"   Cloud revenue quality: {len(cloud_rev_df)} contract types loaded")
else:
    print(f"   Cloud revenue quality: NOT FOUND")

# 4k. SaaS Benchmarks
saas_bench_path = os.path.join(DATA_DIR, "unit_economics", "saas_benchmarks.csv")
if os.path.exists(saas_bench_path):
    saas_bench_df = pd.read_csv(saas_bench_path)
    print(f"   SaaS benchmarks: {len(saas_bench_df)} ARR bands loaded")
else:
    print(f"   SaaS benchmarks: NOT FOUND")

# 4l. Stress Scenarios
stress_path = os.path.join(DATA_DIR, "stress_scenarios", "stress_scenarios.csv")
if os.path.exists(stress_path):
    stress_df = pd.read_csv(stress_path)
    print(f"   Stress scenarios: {len(stress_df)} scenarios loaded")
else:
    print(f"   Stress scenarios: NOT FOUND")

stress_backtest_path = os.path.join(DATA_DIR, "stress_scenarios", "historical_backtest.csv")
if os.path.exists(stress_backtest_path):
    stress_backtest_df = pd.read_csv(stress_backtest_path)
    print(f"   Historical backtests: {len(stress_backtest_df)} episodes loaded")
else:
    print(f"   Historical backtests: NOT FOUND")

scenario_matrix_path = os.path.join(DATA_DIR, "stress_scenarios", "scenario_matrix.csv")
if os.path.exists(scenario_matrix_path):
    scenario_matrix_df = pd.read_csv(scenario_matrix_path)
    print(f"   Scenario matrix: {len(scenario_matrix_df)} combinations loaded")
else:
    print(f"   Scenario matrix: NOT FOUND")

# --- 5. PARSE ALL 13 SEC DERA QUARTERS (2023q1 -> 2026q1) ---
print(f"\n[5/6] Scanning {len(SEC_QUARTERS)} corporate SEC financial directories...")

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

# --- DATA INGESTION FUNCTIONS FOR NEW SOURCES ---

def ingest_adoption_data(data_dir):
    """Load AI adoption & usage telemetry from vendor reports and surveys."""
    metrics = {}
    path = os.path.join(data_dir, "vendor_reported_metrics.csv")
    if os.path.exists(path):
        df = pd.read_csv(path)
        # Aggregate key metrics by vendor/quarter
        metrics["vendor_metrics"] = df.to_dict(orient="records")
    return metrics

def ingest_china_data(data_dir):
    """Load Chinese AI benchmarks, pricing, and infrastructure costs."""
    metrics = {}
    bench_path = os.path.join(data_dir, "model_benchmarks.csv")
    if os.path.exists(bench_path):
        df = pd.read_csv(bench_path)
        metrics["model_benchmarks"] = df.to_dict(orient="records")
    
    pricing_path = os.path.join(data_dir, "api_pricing.csv")
    if os.path.exists(pricing_path):
        df = pd.read_csv(pricing_path)
        metrics["api_pricing"] = df.to_dict(orient="records")
    return metrics

def ingest_productivity_data(data_dir):
    """Load productivity meta-analysis studies."""
    metrics = {}
    path = os.path.join(data_dir, "meta_analysis_studies.csv")
    if os.path.exists(path):
        df = pd.read_csv(path)
        metrics["studies"] = df.to_dict(orient="records")
        # Compute pooled effect sizes by category
        if "category" in df.columns and "effect_size_pct" in df.columns:
            pooled = df.groupby("category")["effect_size_pct"].mean().to_dict()
            metrics["pooled_effect_sizes"] = pooled
    return metrics

def ingest_revenue_quality(data_dir):
    """Load cloud revenue quality mapping and SaaS benchmarks."""
    metrics = {}
    mapping_path = os.path.join(data_dir, "cloud_contract_mapping.csv")
    if os.path.exists(mapping_path):
        df = pd.read_csv(mapping_path)
        metrics["contract_mapping"] = df.to_dict(orient="records")
    
    saas_path = os.path.join(os.path.dirname(os.path.dirname(data_dir)), "unit_economics", "saas_benchmarks.csv")
    if os.path.exists(saas_path):
        df = pd.read_csv(saas_path)
        metrics["saas_benchmarks"] = df.to_dict(orient="records")
    return metrics

def ingest_macro_data(data_dir):
    """Load macro/financial time series catalog."""
    metrics = {}
    path = os.path.join(data_dir, "fred_series_catalog.csv")
    if os.path.exists(path):
        df = pd.read_csv(path)
        metrics["fred_catalog"] = df.to_dict(orient="records")
    return metrics

def ingest_semiconductor_data(data_dir):
    """Load semiconductor supply chain physical data."""
    metrics = {}
    path = os.path.join(data_dir, "supply_chain_quarterly.csv")
    if os.path.exists(path):
        df = pd.read_csv(path)
        metrics["quarterly_supply_chain"] = df.to_dict(orient="records")
    return metrics

def ingest_agents_data(data_dir):
    """Load enterprise AI agent deployment data."""
    metrics = {}
    path = os.path.join(data_dir, "deployment_counts.csv")
    if os.path.exists(path):
        df = pd.read_csv(path)
        metrics["deployments"] = df.to_dict(orient="records")
    return metrics

def ingest_regulatory_data(data_dir):
    """Load regulatory scenario database."""
    metrics = {}
    path = os.path.join(data_dir, "jurisdiction_rule_matrix.csv")
    if os.path.exists(path):
        df = pd.read_csv(path)
        metrics["regulatory_rules"] = df.to_dict(orient="records")
    return metrics

def ingest_labor_data(data_dir):
    """Load labor market transformation data (O*NET AI exposure)."""
    metrics = {}
    path = os.path.join(data_dir, "onet_ai_exposure.csv")
    if os.path.exists(path):
        df = pd.read_csv(path)
        metrics["onet_exposure"] = df.to_dict(orient="records")
    return metrics

def ingest_unit_economics(data_dir):
    """Load unit economics: training, inference, GPU, SaaS benchmarks."""
    metrics = {}
    base = data_dir
    files = {
        "training_costs": "training_costs.csv",
        "inference_costs": "inference_costs.csv",
        "gpu_economics": "gpu_economics.csv",
        "saas_benchmarks": "saas_benchmarks.csv"
    }
    for key, fname in files.items():
        path = os.path.join(base, fname)
        if os.path.exists(path):
            df = pd.read_csv(path)
            metrics[key] = df.to_dict(orient="records")
    return metrics

def ingest_stress_scenarios(data_dir):
    """Load stress scenarios and historical backtests."""
    metrics = {}
    files = {
        "scenarios": "stress_scenarios.csv",
        "historical_backtest": "historical_backtest.csv",
        "scenario_matrix": "scenario_matrix.csv"
    }
    for key, fname in files.items():
        path = os.path.join(data_dir, fname)
        if os.path.exists(path):
            df = pd.read_csv(path)
            metrics[key] = df.to_dict(orient="records")
    return metrics

# --- 10. EXPORT PARAMETER OVERRIDES FILE ---
print(f"\n[10/10] Generating parameter overrides...")

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

# --- 5. INGEST NEW DATA SOURCES ---
print(f"\n[5/9] Ingesting AI adoption & usage telemetry...")
adoption_metrics = ingest_adoption_data(ADOPTION_DIR)

print(f"\n[6/9] Ingesting Chinese AI ecosystem data...")
china_metrics = ingest_china_data(CHINA_DIR)

print(f"\n[7/9] Ingesting productivity meta-analysis...")
productivity_metrics = ingest_productivity_data(PRODUCTIVITY_DIR)

print(f"\n[8/9] Ingesting revenue quality & contract mapping...")
revenue_quality_metrics = ingest_revenue_quality(REVENUE_QUALITY_DIR)

print(f"\n[9/9] Ingesting macro/financial, semiconductor, agents, regulatory, labor, unit economics...")
macro_metrics = ingest_macro_data(MACRO_DIR)
semi_metrics = ingest_semiconductor_data(SEMICONDUCTOR_DIR)
agents_metrics = ingest_agents_data(AGENTS_DIR)
regulatory_metrics = ingest_regulatory_data(REGULATORY_DIR)
labor_metrics = ingest_labor_data(LABOR_DIR)
unit_econ_metrics = ingest_unit_economics(UNIT_ECONOMICS_DIR)
stress_metrics = ingest_stress_scenarios(STRESS_DIR)

# --- 10. EXPORT PARAMETER OVERRIDES FILE ---
print(f"\n[10/10] Generating parameter overrides...")

power_growth_cap = round(max(0.03, 1.0 - (withdrawal_rate / 100.0)), 2)

# Merge all new metrics into calibrated overrides
all_metrics = {
    **calibrated_overrides,
    "adoptionMetrics": adoption_metrics,
    "chinaMetrics": china_metrics,
    "productivityMetrics": productivity_metrics,
    "revenueQualityMetrics": revenue_quality_metrics,
    "macroMetrics": macro_metrics,
    "semiconductorMetrics": semi_metrics,
    "agentsMetrics": agents_metrics,
    "regulatoryMetrics": regulatory_metrics,
    "laborMetrics": labor_metrics,
    "unitEconomicsMetrics": unit_econ_metrics,
    "stressScenarioMetrics": stress_metrics
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
 * Ingests empirical anchors from 13 SEC quarters, LBNL grid data, USITC trade flows,
 * plus 10 new data categories (adoption, China, productivity, revenue quality, macro,
 * semiconductor, agents, regulatory, labor, unit economics, stress scenarios)
 * into the TESM Engine runtime environment.
 *
 * Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}
 */

window.TESM_CALIBRATED_OVERRIDES = {json.dumps(all_metrics, indent=2)};

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

window.TESM_DATA_CATEGORIES = {{
  "adoption": {json.dumps(adoption_metrics, indent=2)},
  "china": {json.dumps(china_metrics, indent=2)},
  "productivity": {json.dumps(productivity_metrics, indent=2)},
  "revenueQuality": {json.dumps(revenue_quality_metrics, indent=2)},
  "macro": {json.dumps(macro_metrics, indent=2)},
  "semiconductor": {json.dumps(semi_metrics, indent=2)},
  "agents": {json.dumps(agents_metrics, indent=2)},
  "regulatory": {json.dumps(regulatory_metrics, indent=2)},
  "labor": {json.dumps(labor_metrics, indent=2)},
  "unitEconomics": {json.dumps(unit_econ_metrics, indent=2)},
  "stressScenarios": {json.dumps(stress_metrics, indent=2)}
}};

// Apply values to the default parameters template block
if (window.TESMEngine) {{
  Object.assign(window.TESMEngine.DEFAULT_PARAMS, window.TESM_CALIBRATED_OVERRIDES);
  console.log("TESM Engine Calibrated with Real-World Data (" + window.TESM_CALIBRATION_META.secQuartersProcessed + " SEC quarters + 10 new categories):", window.TESM_CALIBRATED_OVERRIDES);
}}
"""

with open("param_overrides.js", "w") as f:
    f.write(overrides_js_content)

print(f"\n{'=' * 70}")
print("[SUCCESS] Calibration complete. Overrides saved to: param_overrides.js")
print(f"{'=' * 70}")
print(json.dumps(all_metrics, indent=2))
