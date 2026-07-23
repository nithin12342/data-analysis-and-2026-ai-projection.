import duckdb
import os
from pathlib import Path

DB_DIR = Path("databases")
OUTPUT_DB = DB_DIR / "all_databases_consolidated.duckdb"

print("=" * 70)
print("  CONSOLIDATING ALL DUCKDB DATABASES")
print("=" * 70)

# Remove existing output if it exists
if OUTPUT_DB.exists():
    os.remove(OUTPUT_DB)

# Create new database
con = duckdb.connect(str(OUTPUT_DB))

# List of databases to consolidate
dbs = [
    "consolidated_data.duckdb",
    "enriched_data.duckdb", 
    "master_consolidated.duckdb",
    "sec_dera.duckdb"
]

total_tables = 0
for db_file in dbs:
    db_path = DB_DIR / db_file
    if db_path.exists():
        print(f"\nProcessing {db_file}...")
        
        # Attach the database
        alias = db_file.replace('.', '_')
        con.execute(f"ATTACH '{db_path}' AS {alias}")
        
        # Get tables
        tables = con.execute(f"SHOW TABLES FROM {alias}").fetchall()
        
        for table in tables:
            table_name = table[0]
            # Rename table to avoid duplicates
            new_name = f"{alias}_{table_name}"
            
            try:
                # Check if source table has data
                count = con.execute(f"SELECT COUNT(*) FROM {alias}.{table_name}").fetchone()[0]
                
                # Copy table
                con.execute(f"CREATE TABLE {new_name} AS SELECT * FROM {alias}.{table_name}")
                print(f"  {new_name}: {count} rows")
                total_tables += 1
            except Exception as e:
                print(f"  {table_name}: Error - {e}")
        
        # Detach
        con.execute(f"DETACH {alias}")

con.close()

print(f"\n{'=' * 70}")
print(f"  CONSOLIDATION COMPLETE")
print(f"  Output: {OUTPUT_DB}")
print(f"  Total tables: {total_tables}")
print("=" * 70)

# Verify
con = duckdb.connect(str(OUTPUT_DB))
tables = con.execute("SHOW TABLES").fetchall()
print(f"\n  Tables in consolidated database:")
for t in tables[:20]:
    count = con.execute(f"SELECT COUNT(*) FROM {t[0]}").fetchone()[0]
    print(f"    {t[0]}: {count} rows")
if len(tables) > 20:
    print(f"    ... and {len(tables) - 20} more tables")
con.close()