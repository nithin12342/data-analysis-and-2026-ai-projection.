import duckdb
con = duckdb.connect('databases/deduplicated_tesm_database.duckdb')

# Check all unique tags
all_tags = con.execute("SELECT DISTINCT tag FROM sec_company_facts_complete LIMIT 50").fetchall()
print('First 50 unique tags:')
for t in all_tags:
    print(f'  {t[0]}')

# Check for any tag containing 'Revenue' or 'Revenues'
rev_tags = con.execute("""
    SELECT DISTINCT tag FROM sec_company_facts_complete 
    WHERE tag LIKE '%evenu%' OR tag LIKE '%Revenues%' OR tag LIKE '%Revenue%'
""").fetchall()
print(f'\nAll revenue-related tags: {len(rev_tags)}')
for t in rev_tags:
    count = con.execute(f"SELECT COUNT(*) FROM sec_company_facts_complete WHERE tag = '{t[0]}' AND value IS NOT NULL").fetchone()[0]
    print(f'  {t[0]}: {count} values')

# Check what the first 100 companies look like
companies = con.execute("SELECT DISTINCT cik, entity_name FROM sec_company_facts_complete LIMIT 10").fetchall()
print('\nFirst 10 companies:')
for c in companies:
    print(f'  {c[0]}: {c[1]}')

con.close()