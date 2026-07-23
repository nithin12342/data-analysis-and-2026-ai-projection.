import duckdb
import os
from pathlib import Path

OUTPUT_DB = Path("databases/final_tesm_database.duckdb")
if OUTPUT_DB.exists():
    os.remove(OUTPUT_DB)

con = duckdb.connect(str(OUTPUT_DB))

print("=" * 70)
print("  CREATING FINAL TESM DATABASE")
print("=" * 70)

# Attach all source databases
databases = [
    ("databases/all_databases_consolidated.duckdb", "all_consolidated"),
    ("DATA/tesm_54_tables.duckdb", "tesm_54")
]

total_tables = 0
for db_path, alias in databases:
    if Path(db_path).exists():
        print(f"\nProcessing {db_path}...")
        con.execute(f"ATTACH '{db_path}' AS {alias}")
        
        tables = con.execute(f"SHOW TABLES FROM {alias}").fetchall()
        
        for table in tables:
            table_name = table[0]
            new_name = f"{alias}_{table_name}"
            
            try:
                count = con.execute(f"SELECT COUNT(*) FROM {alias}.{table_name}").fetchone()[0]
                if count > 0:
                    con.execute(f"CREATE TABLE {new_name} AS SELECT * FROM {alias}.{table_name}")
                    total_tables += 1
            except Exception as e:
                pass
        
        con.execute(f"DETACH {alias}")

con.close()

print(f"\n{'=' * 70}")
print(f"  FINAL DATABASE CREATED")
print(f"  Output: {OUTPUT_DB}")
print(f"  Total tables: {total_tables}")
print("=" * 70)

# Verify
con = duckdb.connect(str(OUTPUT_DB))
tables = con.execute("SHOW TABLES").fetchall()
print(f"\n  Top 20 tables by row count:")
for t in con.execute("SELECT table_name, COUNT(*) as rows FROM information_schema.tables GROUP BY table_name ORDER BY rows DESC LIMIT 20").fetchall():
    print(f"    {t[0]}: {t[1]} rows")