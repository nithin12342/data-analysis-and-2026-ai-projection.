import numpy as np
import pandas as pd
import json

print("=" * 70)
print("CONTRACT DOWNSIZING REVENUE LOSS CALCULATOR (v3.0)")
print("Reconciled with SEC DERA Hyperscaler Filings (2023q1 - 2026q1)")
print("=" * 70)

# --- CORRECTED SEC DATA (from calibrate.py v3.0 output) ---
quarterly_data = [
    {"quarter": "2023q1", "capexB": 40.38, "rpoB": 83.33, "revB": 301.34},
    {"quarter": "2023q2", "capexB": 37.88, "rpoB": 82.30, "revB": 299.38},
    {"quarter": "2023q3", "capexB": 36.33, "rpoB": 98.21, "revB": 315.02},
    {"quarter": "2023q4", "capexB": 38.60, "rpoB": 90.21, "revB": 332.10},
    {"quarter": "2024q1", "capexB": 39.43, "rpoB": 94.24, "revB": 338.28},
    {"quarter": "2024q2", "capexB": 46.17, "rpoB": 91.03, "revB": 344.54},
    {"quarter": "2024q3", "capexB": 51.08, "rpoB": 108.10, "revB": 355.70},
    {"quarter": "2024q4", "capexB": 72.37, "rpoB": 160.99, "revB": 438.10},
    {"quarter": "2025q1", "capexB": 63.21, "rpoB": 100.95, "revB": 381.36},
    {"quarter": "2025q2", "capexB": 77.38, "rpoB": 100.17, "revB": 382.46},
    {"quarter": "2025q3", "capexB": 91.54, "rpoB": 122.55, "revB": 407.24},
    {"quarter": "2025q4", "capexB": 102.21, "rpoB": 113.12, "revB": 437.75},
    {"quarter": "2026q1", "capexB": 116.32, "rpoB": 115.40, "revB": 439.03},
]

df = pd.DataFrame(quarterly_data)

# Reconciled parameters (from calibrate.py v3.0)
DOWNSIZING_RATIO = 0.60       # 60% of contract value lost on stressed renewal
CONTRACT_MIX_3YR = 0.70       # 70% are 3-year contracts
CONTRACT_MIX_5YR = 0.30       # 30% are 5-year contracts
NORMAL_CHURN = 0.04           # 4% natural non-renewal even in good times
WACC = 0.085                  # Cost of capital threshold

print("\n--- STEP 1: MAPPING CONTRACT ORIGINATION TO EXPIRATION ---")
print("3-year contracts signed in 2023 -> expire in 2026")
print("3-year contracts signed in 2024 -> expire in 2027")
print("5-year contracts signed in 2021 -> expire in 2026 (estimated)")
print("5-year contracts signed in 2022 -> expire in 2027 (estimated)")

# 3-YEAR CONTRACTS EXPIRING IN 2026 = contracts signed throughout 2023
rpo_2023 = df[df['quarter'].str.startswith('2023')]['rpoB'].values
total_rpo_2023 = rpo_2023.sum()
contracts_3yr_expiring_2026 = total_rpo_2023 * CONTRACT_MIX_3YR

# 3-YEAR CONTRACTS EXPIRING IN 2027 = contracts signed throughout 2024
rpo_2024 = df[df['quarter'].str.startswith('2024')]['rpoB'].values
total_rpo_2024 = rpo_2024.sum()
contracts_3yr_expiring_2027 = total_rpo_2024 * CONTRACT_MIX_3YR

# 5-YEAR CONTRACTS EXPIRING IN 2026 = contracts signed in 2021 (estimated at 60% of 2023 levels)
estimated_rpo_2021_annual = total_rpo_2023 * 0.60
contracts_5yr_expiring_2026 = estimated_rpo_2021_annual * CONTRACT_MIX_5YR

# 5-YEAR CONTRACTS EXPIRING IN 2027 = contracts signed in 2022 (estimated at 75% of 2023 levels)
estimated_rpo_2022_annual = total_rpo_2023 * 0.75
contracts_5yr_expiring_2027 = estimated_rpo_2022_annual * CONTRACT_MIX_5YR

print(f"\n--- STEP 2: TOTAL CONTRACTS EXPIRING ---")
print(f"\n2026 EXPIRATIONS:")
print(f"  3-year contracts (signed 2023):  ${contracts_3yr_expiring_2026:,.1f}B")
print(f"  5-year contracts (signed 2021):  ${contracts_5yr_expiring_2026:,.1f}B")
total_expiring_2026 = contracts_3yr_expiring_2026 + contracts_5yr_expiring_2026
print(f"  TOTAL EXPIRING IN 2026:          ${total_expiring_2026:,.1f}B")

print(f"\n2027 EXPIRATIONS:")
print(f"  3-year contracts (signed 2024):  ${contracts_3yr_expiring_2027:,.1f}B")
print(f"  5-year contracts (signed 2022):  ${contracts_5yr_expiring_2027:,.1f}B")
total_expiring_2027 = contracts_3yr_expiring_2027 + contracts_5yr_expiring_2027
print(f"  TOTAL EXPIRING IN 2027:          ${total_expiring_2027:,.1f}B")

total_combined_exp = total_expiring_2026 + total_expiring_2027
print(f"  COMBINED TOTAL EXPIRING:         ${total_combined_exp:,.1f}B")

# --- STEP 3: CALCULATE REVENUE LOSS FROM DOWNSIZING ---
print(f"\n--- STEP 3: REVENUE LOSS FROM DOWNSIZING ---")
print(f"Downsizing Ratio: {DOWNSIZING_RATIO} (60% of contract value lost on renewal)")
print(f"Normal Churn:     {NORMAL_CHURN} (4% lost even in good times)\n")

# Scenario 1: Normal Market (ROI > WACC) - only 4% natural churn
normal_loss_2026 = total_expiring_2026 * NORMAL_CHURN
normal_loss_2027 = total_expiring_2027 * NORMAL_CHURN

# Scenario 2: Stressed Market (ROI < WACC) - full 60% downsizing
stressed_loss_2026 = total_expiring_2026 * DOWNSIZING_RATIO
stressed_loss_2027 = total_expiring_2027 * DOWNSIZING_RATIO

# Scenario 3: Partial Stress - 40% of contracts downsize, 60% renew normally
partial_downsize_fraction = 0.40
partial_loss_2026 = (total_expiring_2026 * partial_downsize_fraction * DOWNSIZING_RATIO) + \
                    (total_expiring_2026 * (1 - partial_downsize_fraction) * NORMAL_CHURN)
partial_loss_2027 = (total_expiring_2027 * partial_downsize_fraction * DOWNSIZING_RATIO) + \
                    (total_expiring_2027 * (1 - partial_downsize_fraction) * NORMAL_CHURN)

print("SCENARIO           |     2026 LOSS    |     2027 LOSS    |   COMBINED LOSS")
print("-" * 75)
print(f"Normal (4% churn)  |  ${normal_loss_2026:>10,.1f}B  |  ${normal_loss_2027:>10,.1f}B  |  ${normal_loss_2026 + normal_loss_2027:>10,.1f}B")
print(f"Partial (40% down) |  ${partial_loss_2026:>10,.1f}B  |  ${partial_loss_2027:>10,.1f}B  |  ${partial_loss_2026 + partial_loss_2027:>10,.1f}B")
print(f"Full Stress (60%)  |  ${stressed_loss_2026:>10,.1f}B  |  ${stressed_loss_2027:>10,.1f}B  |  ${stressed_loss_2026 + stressed_loss_2027:>10,.1f}B")

# --- STEP 4: QUARTERLY BREAKDOWN ---
print(f"\n--- STEP 4: QUARTERLY BREAKDOWN OF REVENUE LOSS (FULL STRESS) ---")

# Distribute expirations across 4 quarters (weighted by quarterly RPO pattern)
q_weights_2026 = np.array([0.30, 0.20, 0.25, 0.25])
q_weights_2027 = np.array([0.30, 0.20, 0.25, 0.25])

print(f"\n{'Quarter':<12} {'Expiring':>12} {'Downsized Loss':>16} {'Cumulative Loss':>16}")
print("-" * 60)

cumulative = 0
for i, q_label in enumerate(["2026 Q1", "2026 Q2", "2026 Q3", "2026 Q4"]):
    q_exp = total_expiring_2026 * q_weights_2026[i]
    q_loss = q_exp * DOWNSIZING_RATIO
    cumulative += q_loss
    print(f"{q_label:<12} ${q_exp:>10,.1f}B  ${q_loss:>14,.1f}B  ${cumulative:>14,.1f}B")

for i, q_label in enumerate(["2027 Q1", "2027 Q2", "2027 Q3", "2027 Q4"]):
    q_exp = total_expiring_2027 * q_weights_2027[i]
    q_loss = q_exp * DOWNSIZING_RATIO
    cumulative += q_loss
    print(f"{q_label:<12} ${q_exp:>10,.1f}B  ${q_loss:>14,.1f}B  ${cumulative:>14,.1f}B")

print("-" * 60)
print(f"{'TOTAL':<12} ${total_expiring_2026 + total_expiring_2027:>10,.1f}B  ${stressed_loss_2026 + stressed_loss_2027:>14,.1f}B")

# --- STEP 5: IMPACT AS % OF HYPERSCALER REVENUE ---
print(f"\n--- STEP 5: IMPACT AS % OF HYPERSCALER REVENUE ---")

# Use most recent annual revenue run-rate (mean quarterly revenue * 4)
mean_qtr_rev = df['revB'].mean()
rev_per_year = mean_qtr_rev * 4

print(f"Hyperscaler Combined Revenue (Annualized):  ${rev_per_year:,.1f}B")
print(f"2026 Stressed Loss as % of Revenue:         {(stressed_loss_2026 / rev_per_year) * 100:.1f}%")
print(f"2027 Stressed Loss as % of Revenue:         {(stressed_loss_2027 / rev_per_year) * 100:.1f}%")
print(f"Combined Loss as % of Revenue:              {((stressed_loss_2026 + stressed_loss_2027) / (rev_per_year * 2)) * 100:.1f}%")

print(f"\n{'=' * 70}")
print(f"BOTTOM LINE: If all expiring contracts downsize by 60%,")
print(f"hyperscalers lose ${stressed_loss_2026 + stressed_loss_2027:,.1f}B across 2026-2027.")
print(f"{'=' * 70}")
