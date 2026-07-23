import duckdb
con = duckdb.connect('databases/deduplicated_tesm_database.duckdb')

# Check for revenue tags with values
tags = con.execute("""
    SELECT DISTINCT tag FROM sec_company_facts_complete 
    WHERE value IS NOT NULL AND (tag LIKE '%Revenue%' OR tag LIKE '%Sales%' OR tag LIKE '%revenue%' OR tag LIKE '%sales%')
    LIMIT 30
""").fetchall()
print('Revenue/Sales tags with values:', [t[0] for t in tags])

# Check for NetIncomeLoss with values
tags2 = con.execute("""
    SELECT DISTINCT tag FROM sec_company_facts_complete 
    WHERE value IS NOT NULL AND (tag LIKE '%NetIncome%' OR tag LIKE '%Profit%' OR tag LIKE '%Loss%')
    LIMIT 20
""").fetchall()
print('Income/Loss tags with values:', [t[0] for t in tags2])

# Check for TotalAssets with values
tags3 = con.execute("""
    SELECT DISTINCT tag FROM sec_company_facts_complete 
    WHERE value IS NOT NULL AND tag LIKE '%Asset%'
    LIMIT 20
""").fetchall()
print('Asset tags with values:', [t[0] for t in tags3])

# Check for TotalLiabilities with values
tags4 = con.execute("""
    SELECT DISTINCT tag FROM sec_company_facts_complete 
    WHERE value IS NOT NULL AND tag LIKE '%Liabilit%'
    LIMIT 20
""").fetchall()
print('Liability tags with values:', [t[0] for t in tags4])

con.close()