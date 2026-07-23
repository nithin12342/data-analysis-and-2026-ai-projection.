import duckdb
import pandas as pd
import json
import glob
from pathlib import Path

DATA_DIR = Path("DATA")
DB_FILE = DATA_DIR / "tesm_54_tables.duckdb"

def parse_sec_file(filepath, max_rows=1000):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    header = lines[0].strip().split('\t')
    data = []
    for line in lines[1:max_rows+1]:
        parts = line.strip().split('\t')
        if len(parts) >= len(header):
            data.append(parts[:len(header)])
        elif parts:
            padded = parts + [''] * (len(header) - len(parts))
            data.append(padded)
    return pd.DataFrame(data, columns=header)

con = duckdb.connect(str(DB_FILE))

print("=" * 70)
print("  INTEGRATING NOT-PREPROCESSED DATA INTO DUCKDB")
print("=" * 70)

# 1. USGS Water Data (Table 50)
print("\n[1] USGS Water Data (Table 50)...")
water_file = DATA_DIR / "not preprocessed" / "usco2015v2.0.csv"
if water_file.exists():
    df = pd.read_csv(water_file, skiprows=1, nrows=5000)
    df.columns = df.columns.str.strip()
    con.execute("DROP TABLE IF EXISTS usgs_water_complete")
    con.execute("CREATE TABLE usgs_water_complete AS SELECT * FROM df")
    print(f"    Loaded: {len(df)} rows, {len(df.columns)} columns")

# 2. SEC EDGAR Data - latest 2 quarters
print("\n[2] SEC EDGAR Data...")
sec_dirs = sorted(glob.glob(str(DATA_DIR / "[0-9][0-9][0-9][0-9]q[1-4]")))
for sec_dir in sec_dirs[-2:]:
    quarter = Path(sec_dir).name
    sub_file = Path(sec_dir) / "sub.txt"
    if sub_file.exists():
        try:
            df = parse_sec_file(sub_file, max_rows=1000)
            table_name = f"sec_sub_{quarter}"
            con.execute(f"DROP TABLE IF EXISTS {table_name}")
            con.execute(f"CREATE TABLE {table_name} AS SELECT * FROM df")
            print(f"    {table_name}: {len(df)} rows")
        except Exception as e:
            print(f"    Error {quarter}: {e}")

# 3. SEC Tag Data - latest quarter
print("\n[3] SEC Tag Data...")
for sec_dir in sec_dirs[-1:]:
    quarter = Path(sec_dir).name
    tag_file = Path(sec_dir) / "tag.txt"
    if tag_file.exists():
        try:
            df = parse_sec_file(tag_file, max_rows=500)
            table_name = f"sec_tag_{quarter}"
            con.execute(f"DROP TABLE IF EXISTS {table_name}")
            con.execute(f"CREATE TABLE {table_name} AS SELECT * FROM df")
            print(f"    {table_name}: {len(df)} rows")
        except Exception as e:
            print(f"    Error {quarter}: {e}")

# 4. SEC Num Data - latest quarter
print("\n[4] SEC Numeric Data...")
for sec_dir in sec_dirs[-1:]:
    quarter = Path(sec_dir).name
    num_file = Path(sec_dir) / "num.txt"
    if num_file.exists():
        try:
            df = parse_sec_file(num_file, max_rows=500)
            table_name = f"sec_num_{quarter}"
            con.execute(f"DROP TABLE IF EXISTS {table_name}")
            con.execute(f"CREATE TABLE {table_name} AS SELECT * FROM df")
            print(f"    {table_name}: {len(df)} rows")
        except Exception as e:
            print(f"    Error {quarter}: {e}")

# 5. Grid Services Revenue Data
print("\n[5] Grid Services Revenue Data...")
grid_file = DATA_DIR / "grid_services_revenue.csv"
if grid_file.exists():
    df = pd.read_csv(grid_file)
    con.execute("DROP TABLE IF EXISTS grid_services_revenue")
    con.execute("CREATE TABLE grid_services_revenue AS SELECT * FROM df")
    print(f"    Loaded: {len(df)} rows")

# 6. LBNL Queue Data
print("\n[6] LBNL Queue Data...")
lbnl_file = DATA_DIR / "not preprocessed" / "LBNL_Ix_Queue_Data_File_thru2025.xlsx"
if lbnl_file.exists():
    df = pd.read_excel(lbnl_file, sheet_name=0, nrows=100)
    con.execute("DROP TABLE IF EXISTS lbdl_queue_data")
    con.execute("CREATE TABLE lbdl_queue_data AS SELECT * FROM df")
    print(f"    Loaded: {len(df)} rows")

# 7. EIA 860 Generator Data - 2024
print("\n[7] EIA 860 Generator Data...")
eia_dir = DATA_DIR / "not preprocessed" / "eia8602024"
gen_file = eia_dir / "EIA-860 Form.xlsx"
if gen_file.exists():
    df = pd.read_excel(gen_file, sheet_name="GENERATORS", nrows=2000)
    if len(df) > 0:
        con.execute("DROP TABLE IF EXISTS eia860_generators_2024")
        con.execute("CREATE TABLE eia860_generators_2024 AS SELECT * FROM df")
        print(f"    eia860_generators_2024: {len(df)} rows")

con.close()

print("\n" + "=" * 70)
print("  DUCKDB DATABASE UPDATED")
print("=" * 70)

con = duckdb.connect(str(DB_FILE))
tables = con.execute("SHOW TABLES").fetchall()
print(f"\n  Total tables: {len(tables)}")
for t in tables:
    count = con.execute(f"SELECT COUNT(*) FROM {t[0]}").fetchone()[0]
    cols = len(con.execute(f"DESCRIBE SELECT * FROM {t[0]} LIMIT 1").fetchall())
    print(f"    {t[0]}: {count} rows, {cols} columns")
con.close()