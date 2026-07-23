import duckdb
con = duckdb.connect('databases/deduplicated_tesm_database.duckdb')

# Check all unique tags that contain 'Revenue' or 'Sales'
tags = con.execute("""
    SELECT DISTINCT tag FROM sec_company_facts_complete 
    WHERE tag LIKE '%Revenue%' OR tag LIKE '%Sales%' OR tag LIKE '%revenue%' OR tag LIKE '%sales%'
    LIMIT 30
""").fetchall()
print('Revenue/Sales tags:', [t[0] for t in tags])

# Check for common financial tags
tags2 = con.execute("""
    SELECT DISTINCT tag FROM sec_company_facts_complete 
    WHERE tag LIKE '%NetIncome%' OR tag LIKE '%Profit%' OR tag LIKE '%Loss%'
    LIMIT 20
""").fetchall()
print('\nIncome/Loss tags:', [t[0] for t in tags2])

# Check for Asset tags
tags3 = con.execute("""
    SELECT DISTINCT tag FROM sec_company_facts_complete 
    WHERE tag LIKE '%Asset%' AND LENGTH(tag) < 50
    LIMIT 20
""").fetchall()
print('\nAsset tags:', [t[0] for t in tags3])

# Check sample data for a company with revenue
sample = con.execute("""
    SELECT DISTINCT tag, value FROM sec_company_facts_complete 
    WHERE tag LIKE '%Revenue%' OR tag LIKE '%Sales%'
    LIMIT 10
""").fetchall()
print('\nSample revenue data:', sample)

# Check if any value is not null
non_null = con.execute("""
    SELECT COUNT(*) FROM sec_company_facts_complete WHERE value IS NOT NULL
""").fetchone()[0]
print(f'\nRows with non-null values: {non_null}')

# Check sample values
sample_vals = con.execute("""
    SELECT tag, value FROM sec_company_facts_complete 
    WHERE value IS NOT NULL
    LIMIT 10
""").fetchall()
print('\nSample non-null values:', sample_vals)

con.close()