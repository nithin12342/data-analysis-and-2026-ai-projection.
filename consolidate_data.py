import duckdb
import pandas as pd
import os
from pathlib import Path

data_dir = Path(r"C:\Users\NITHING\Desktop\projections")
csv_files = list(data_dir.rglob("*.csv"))

print(f"Found {len(csv_files)} CSV files:")
for f in csv_files:
    print(f"  {f.relative_to(data_dir)}")

conn = duckdb.connect("databases/consolidated_data.duckdb")

for csv_file in csv_files:
    table_name = csv_file.stem.lower().replace("-", "_").replace(" ", "_")
    try:
        conn.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM read_csv_auto('{csv_file}')")
        count = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
        cols = conn.execute(f"DESCRIBE {table_name}").fetchall()
        print(f"[OK] Loaded {table_name}: {count} rows, {len(cols)} columns")
    except Exception as e:
        print(f"[FAIL] Failed to load {table_name}: {e}")

print("\n--- Database Tables ---")
tables = conn.execute("SHOW TABLES").fetchall()
for t in tables:
    print(f"  {t[0]}")

conn.close()
print("\nDuckDB database created: databases/consolidated_data.duckdb")