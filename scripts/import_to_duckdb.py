import duckdb
import pandas as pd
import os
from pathlib import Path

DATA_DIR = Path("DATA")
DB_FILE = DATA_DIR / "tesm_54_tables.duckdb"

# Connect to DuckDB (creates new file if doesn't exist)
con = duckdb.connect(str(DB_FILE))

print("=" * 70)
print("  DUCKDB TABLE IMPORT FROM CSV FILES")
print("=" * 70)

# List of CSV files to import
csv_files = [
    ("company_security_master", "Table 1"),
    ("company_quarterly_clean", "Tables 1-6, 13-14"),
    ("vendor_reported_metrics", "Tables 9, 35-40"),
    ("gpu_economics", "Tables 38-40"),
    ("api_pricing", "Tables 35-40"),
    ("training_costs", "Table 38"),
    ("model_benchmarks", "Tables 38-40"),
    ("rpo_deferred_revenue", "Table 13"),
    ("market_cap_quarterly", "Table 4"),
    ("token_usage_proxy", "Tables 9, 35-40"),
    ("usgs_water_sample", "Table 50"),
    ("lbnl_queue_sample", "Tables 46-49, 51"),
    ("eia_generators_sample", "Tables 52-53"),
    ("agentic_tco_sample", "Tables 41-45"),
    ("private_ai_financials_sample", "Tables 11-14"),
    ("company_segments_sample", "Table 23"),
]

for csv_name, table_desc in csv_files:
    csv_path = DATA_DIR / f"{csv_name}.csv"
    if csv_path.exists():
        try:
            df = pd.read_csv(csv_path)
            # Drop if exists
            con.execute(f"DROP TABLE IF EXISTS {csv_name}")
            # Register and create table
            con.register(csv_name, df)
            con.execute(f"CREATE TABLE {csv_name} AS SELECT * FROM {csv_name}")
            row_count = len(df)
            col_count = len(df.columns)
            print(f"  [OK] {csv_name}: {row_count} rows, {col_count} columns ({table_desc})")
        except Exception as e:
            print(f"  [ERROR] {csv_name}: {e}")
    else:
        print(f"  [SKIP] {csv_name}: file not found")

# Close connection
con.close()

print("\n" + "=" * 70)
print(f"  DUCKDB DATABASE CREATED: {DB_FILE}")
print("=" * 70)

# Verify by querying
con = duckdb.connect(str(DB_FILE))
tables = con.execute("SHOW TABLES").fetchall()
print(f"\n  Total tables: {len(tables)}")
print("\n  Tables in database:")
for t in tables:
    count = con.execute(f"SELECT COUNT(*) FROM {t[0]}").fetchone()[0]
    print(f"    {t[0]}: {count} rows")
con.close()
print("=" * 70)