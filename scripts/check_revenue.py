import duckdb
con = duckdb.connect('databases/deduplicated_tesm_database.duckdb')

# Check if RevenueFromContractWithCustomerExcludingAssessedTax has values
count = con.execute("""
    SELECT COUNT(*) FROM sec_company_facts_complete 
    WHERE tag = 'RevenueFromContractWithCustomerExcludingAssessedTax' AND value IS NOT NULL
""").fetchone()[0]
print(f"RevenueFromContractWithCustomerExcludingAssessedTax with values: {count}")

# Check what the financials table looks like
sample = con.execute("""
    SELECT cik, entity_name, revenue, net_income, total_assets 
    FROM sec_company_financials_derived 
    WHERE revenue IS NOT NULL
    LIMIT 5
""").fetchall()
print(f"\nCompanies with revenue: {len(sample)}")
for s in sample:
    print(f"  {s}")

# Check if the issue is with the GROUP BY
all_companies = con.execute("""
    SELECT COUNT(DISTINCT cik) FROM sec_company_facts_complete 
    WHERE tag = 'RevenueFromContractWithCustomerExcludingAssessedTax' AND value IS NOT NULL
""").fetchone()[0]
print(f"\nCompanies with revenue tag: {all_companies}")

con.close()