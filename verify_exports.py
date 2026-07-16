import duckdb
con = duckdb.connect('DATA/sec_dera.duckdb')

print("=== EXPORT VERIFICATION ===")

# 1. Hyperscaler capex
df = con.execute('SELECT * FROM read_csv_auto("DATA/sec_exports/hyperscaler_capex.csv")').fetchdf()
print(f"Hyperscaler CapEx: {len(df)} rows, {df['name'].nunique()} companies")
print(f"  Periods: {df['period'].min()} to {df['period'].max()}")
print(f"  CapEx coverage: {df['capex'].notna().sum()}/{len(df)}")
print(f"  Revenue coverage: {df['revenue'].notna().sum()}/{len(df)}")

# 2. Semiconductors
df = con.execute('SELECT * FROM read_csv_auto("DATA/sec_exports/semiconductor_metrics.csv")').fetchdf()
print(f"Semiconductors: {len(df)} rows, {df['name'].nunique()} companies")
print(f"  CapEx coverage: {df['capex'].notna().sum()}/{len(df)}")
print(f"  R&D coverage: {df['rd_expense'].notna().sum()}/{len(df)}")

# 3. All company quarterly
df = con.execute('SELECT * FROM read_csv_auto("DATA/sec_exports/all_company_quarterly.csv")').fetchdf()
print(f"All Company Quarterly: {len(df)} rows, {df['name'].nunique()} companies")

# 4. SBC
df = con.execute('SELECT * FROM read_csv_auto("DATA/sec_exports/sbc_burden_full.csv")').fetchdf()
print(f"SBC Burden: {len(df)} rows, {df['name'].nunique()} companies")
print(f"  SBC coverage: {df['sbc'].notna().sum()}/{len(df)}")

# 5. DC REITs
df = con.execute('SELECT * FROM read_csv_auto("DATA/sec_exports/dc_reit_metrics.csv")').fetchdf()
print(f"DC REITs: {len(df)} rows, {df['name'].nunique()} companies")

con.close()