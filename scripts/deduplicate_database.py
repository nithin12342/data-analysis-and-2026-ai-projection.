import duckdb
import os
from pathlib import Path
from collections import defaultdict
import re

OUTPUT_DB = Path("databases/deduplicated_tesm_database.duckdb")
if OUTPUT_DB.exists():
    os.remove(OUTPUT_DB)

con = duckdb.connect(str(OUTPUT_DB))

print("=" * 70)
print("  DEDUPLICATING DUCKDB DATABASE (COMPLETE)")
print("=" * 70)

# Attach the database to deduplicate
con.execute("ATTACH 'databases/final_tesm_database.duckdb' AS source")

# Get all tables
tables = con.execute("SHOW TABLES FROM source").fetchall()
print(f"\nOriginal tables: {len(tables)}")

# Function to extract clean base name
def get_base_name(table_name):
    name = table_name
    
    # Remove database prefixes (in order of specificity)
    prefixes_to_remove = [
        "all_consolidated_consolidated_data_duckdb_",
        "all_consolidated_master_consolidated_duckdb_",
        "consolidated_data_duckdb_",
        "master_consolidated_duckdb_",
        "all_consolidated_",
        "consolidated_data_",
        "enriched_data_",
        "master_consolidated_",
        "sec_dera_",
        "tesm_54_"
    ]
    
    for prefix in prefixes_to_remove:
        if name.startswith(prefix):
            name = name[len(prefix):]
            break
    
    # Remove common suffixes
    name = re.sub(r'^duckdb_', '', name)
    name = re.sub(r'_complete$', '', name)
    name = re.sub(r'_sample$', '', name)
    
    return name

# Group tables by their base name
table_groups = defaultdict(list)
for t in tables:
    table_name = t[0]
    base_name = get_base_name(table_name)
    table_groups[base_name].append(table_name)

print(f"Unique base tables: {len(table_groups)}")
duplicate_count = sum(1 for g in table_groups.values() if len(g) > 1)
print(f"Duplicate groups: {duplicate_count}")

# Show duplicate groups
if duplicate_count > 0:
    print("\nDuplicate groups found:")
    for base_name, table_names in table_groups.items():
        if len(table_names) > 1:
            print(f"  {base_name}:")
            for t in table_names:
                print(f"    - {t}")

# Deduplicate
duplicates_removed = 0
tables_added = 0

print("\nProcessing tables...")
for base_name, table_names in table_groups.items():
    # Pick the best table (prefer tables with more data)
    best_table = None
    best_count = -1
    
    for tname in table_names:
        try:
            count = con.execute(f"SELECT COUNT(*) FROM source.{tname}").fetchone()[0]
            if count > best_count:
                best_count = count
                best_table = tname
        except Exception as e:
            pass
    
    if best_table:
        con.execute(f"CREATE TABLE {base_name} AS SELECT * FROM source.{best_table}")
        tables_added += 1
        
        if len(table_names) > 1:
            duplicates_removed += len(table_names) - 1

con.execute("DETACH source")

con.close()

print(f"\n{'=' * 70}")
print(f"  DEDUPLICATION COMPLETE")
print(f"  Output: {OUTPUT_DB}")
print(f"  Tables kept: {tables_added}")
print(f"  Duplicates removed: {duplicates_removed}")
print("=" * 70)

# Verify
con = duckdb.connect(str(OUTPUT_DB))
tables = con.execute("SHOW TABLES").fetchall()

print(f"\n  Total tables in final database: {len(tables)}")

# Show key tables with row counts
print("\n  Key tables:")
key_tables = [
    'usgs_water',
    'sec_sub_2025q4',
    'sec_num_2025q4',
    'sec_tag_2025q4',
    'grid_services_revenue',
    'global_datacenters_github',
    'sec_quarterly_financials',
    'company_security_master',
    'equity_prices_daily',
    'hyperscaler_capex'
]

for t in key_tables:
    try:
        count = con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        print(f"    {t}: {count} rows")
    except Exception as e:
        print(f"    {t}: NOT FOUND")

con.close()