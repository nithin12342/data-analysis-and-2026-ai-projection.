import duckdb
from pathlib import Path
from collections import defaultdict

DB_FILE = Path("databases/deduplicated_tesm_database.duckdb")

print("=" * 100)
print("  DUCKDB DATABASE AUDIT REPORT")
print("=" * 100)
print(f"\nDatabase: {DB_FILE}")
print(f"Size: {DB_FILE.stat().st_size / (1024*1024):.2f} MB\n")

con = duckdb.connect(str(DB_FILE))

# Get all tables
tables = con.execute("SHOW TABLES").fetchall()
print(f"Total Tables: {len(tables)}\n")

print("=" * 100)
print("  TABLE DETAILS")
print("=" * 100)

# Categorize tables by type
categories = defaultdict(list)

for t in tables:
    table_name = t[0]
    
    # Get row count
    try:
        row_count = con.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
    except:
        row_count = 0
    
    # Get column info
    try:
        cols = con.execute(f"DESCRIBE SELECT * FROM {table_name} LIMIT 1").fetchall()
        column_names = [c[0] for c in cols]
    except:
        column_names = []
    
    # Categorize
    if 'sec_' in table_name and 'sub' in table_name:
        category = 'SEC Submissions'
    elif 'sec_' in table_name and 'tag' in table_name:
        category = 'SEC Tags'
    elif 'sec_' in table_name and 'num' in table_name:
        category = 'SEC Numeric Facts'
    elif 'sec_' in table_name and 'quarterly' in table_name.lower():
        category = 'SEC Quarterly Financials'
    elif 'sec_' in table_name and 'facts' in table_name:
        category = 'SEC Facts'
    elif 'global_datacenters' in table_name:
        category = 'Datacenter Data'
    elif 'hyperscaler' in table_name:
        category = 'Hyperscaler Data'
    elif 'equity_prices' in table_name:
        category = 'Market Data'
    elif 'global_macro' in table_name:
        category = 'Macro Data'
    elif 'usgs' in table_name:
        category = 'Water/Energy Data'
    elif 'eia' in table_name:
        category = 'Energy Data'
    elif 'rpo' in table_name or 'deferred' in table_name:
        category = 'Revenue Data'
    elif 'market_cap' in table_name or 'enterprise_value' in table_name or 'valuation' in table_name:
        category = 'Valuation Data'
    elif 'gpu' in table_name or 'training' in table_name or 'model' in table_name or 'api_pricing' in table_name:
        category = 'AI/ML Data'
    elif 'grid' in table_name or 'power' in table_name or 'fuel' in table_name:
        category = 'Power/Energy Data'
    elif 'carbon' in table_name:
        category = 'Carbon Data'
    elif 'scenario' in table_name or 'stress' in table_name:
        category = 'Scenario Data'
    elif 'module' in table_name:
        category = 'Model Modules'
    elif 'benchmark' in table_name or 'analysis' in table_name:
        category = 'Benchmark/Data'
    elif 'water' in table_name:
        category = 'Water Data'
    elif 'contract' in table_name or 'capacity' in table_name:
        category = 'Infrastructure Data'
    else:
        category = 'General Data'
    
    categories[category].append({
        'name': table_name,
        'rows': row_count,
        'columns': column_names
    })

# Print by category
for category in sorted(categories.keys()):
    tables_in_cat = categories[category]
    total_rows = sum(t['rows'] for t in tables_in_cat)
    
    print(f"\n{category} ({len(tables_in_cat)} tables, {total_rows:,} total rows)")
    print("-" * 100)
    
    for t in sorted(tables_in_cat, key=lambda x: -x['rows']):
        row_str = f"{t['rows']:,}"
        col_str = ", ".join(t['columns'][:5]) + ("..." if len(t['columns']) > 5 else "")
        if not col_str:
            col_str = "N/A"
        print(f"  {t['name']:<50} {row_str:>12} rows  |  cols: {col_str[:60]}")

con.close()

print("\n" + "=" * 100)
print("  SUMMARY BY CATEGORY")
print("=" * 100)

con = duckdb.connect(str(DB_FILE))
tables = con.execute("SHOW TABLES").fetchall()

for category in sorted(categories.keys()):
    tables_in_cat = categories[category]
    total_rows = sum(t['rows'] for t in tables_in_cat)
    print(f"  {category:<35} {len(tables_in_cat):>3} tables  {total_rows:>15,} rows")

con.close()

print("\n" + "=" * 100)
print("  END OF AUDIT REPORT")
print("=" * 100)