import os
import pandas as pd
import numpy as np

DATA_DIR = "C:/Users/NITHING/Desktop/projections/DATA"
SEC_QUARTERS = [
    "2023q1", "2023q2", "2023q3", "2023q4",
    "2024q1", "2024q2", "2024q3", "2024q4",
    "2025q1", "2025q2", "2025q3", "2025q4",
    "2026q1"
]

# Tickers to CIK mappings for the six hyperscalers
HYPERSCALERS = {
    "MICROSOFT CORP": "MSFT",
    "AMAZON COM INC": "AMZN",
    "ALPHABET INC": "GOOG",
    "META PLATFORMS, INC.": "META",
    "ORACLE CORP": "ORCL",
    "SALESFORCE, INC.": "CRM"
}

CAPEX_TAGS = [
    "PaymentsToAcquirePropertyPlantAndEquipment",
    "PaymentsToAcquireProductiveAssets"
]

results = []

print("Scanning quarters...")
for q in SEC_QUARTERS:
    sub_path = os.path.join(DATA_DIR, q, "sub.txt")
    num_path = os.path.join(DATA_DIR, q, "num.txt")
    
    if not (os.path.exists(sub_path) and os.path.exists(num_path)):
        continue
        
    try:
        sub = pd.read_csv(sub_path, sep='\t')
        # Filter for our six hyperscalers
        matched_subs = sub[sub['name'].str.contains("MICROSOFT|AMAZON|ALPHABET|SALESFORCE|META PLATFORMS|ORACLE", case=False, na=False)]
        filtered_adsh = matched_subs['adsh'].unique()
        
        if len(filtered_adsh) == 0:
            continue
            
        num = pd.read_csv(num_path, sep='\t', low_memory=False)
        firm_data = num[num['adsh'].isin(filtered_adsh)]
        
        matched_subs = matched_subs.copy()
        matched_subs['period'] = pd.to_numeric(matched_subs['period'], errors='coerce')
        adsh_to_period = dict(zip(matched_subs['adsh'], matched_subs['period']))
        adsh_to_name = dict(zip(matched_subs['adsh'], matched_subs['name']))
        
        for adsh in filtered_adsh:
            name = adsh_to_name[adsh]
            period = adsh_to_period[adsh]
            if pd.isna(period):
                continue
                
            filing_facts = firm_data[firm_data['adsh'] == adsh]
            period_facts = filing_facts[filing_facts['ddate'].astype(float) == float(period)]
            period_facts_consolidated = period_facts[period_facts['segments'].isna()]
            
            capex_rows = period_facts_consolidated[period_facts_consolidated['tag'].isin(CAPEX_TAGS)]
            capex_vals = []
            for idx, r in capex_rows.iterrows():
                val = r['value']
                qtrs = r['qtrs']
                divisor = qtrs if (not pd.isna(qtrs) and qtrs > 0) else 1
                # Convert YTD/quarterly value to single quarter rate
                capex_vals.append(val / divisor)
                
            if capex_vals:
                quarterly_capex = max(capex_vals) / 1e9  # In Billions
                
                # Standardize company name
                std_name = "Unknown"
                for k in HYPERSCALERS:
                    if k.split()[0].lower() in name.lower():
                        std_name = HYPERSCALERS[k]
                        break
                        
                results.append({
                    "quarter": q,
                    "company": std_name,
                    "capex_b": quarterly_capex
                })
    except Exception as e:
        print(f"Error processing {q}: {e}")

df = pd.DataFrame(results)
if not df.empty:
    print("\nSummary of Extracted Quarterly CapEx ($B):")
    pivot = df.pivot_table(index="quarter", columns="company", values="capex_b", aggfunc="sum")
    print(pivot)
    print("\nTotal Quarterly CapEx across all 6 companies ($B):")
    total_q = pivot.sum(axis=1)
    print(total_q)
    print(f"\nAverage Quarterly Total: ${total_q.mean():.2f}B")
    print(f"Implied Annual Total (Quarterly * 4): ${total_q.mean() * 4:.2f}B")
else:
    print("No data extracted.")
