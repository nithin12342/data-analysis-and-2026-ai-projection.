import duckdb
con = duckdb.connect('databases/deduplicated_tesm_database.duckdb')

# Check for revenue tags
tags = con.execute("SELECT DISTINCT tag FROM sec_company_facts_complete WHERE tag LIKE '%evenu%' OR tag LIKE '%Revenue%' LIMIT 20").fetchall()
print('Revenue-related tags:', [t[0] for t in tags])

# Check for NetIncomeLoss
tags2 = con.execute("SELECT DISTINCT tag FROM sec_company_facts_complete WHERE tag LIKE '%NetIncome%' OR tag LIKE '%Operating%' LIMIT 20").fetchall()
print('Income-related tags:', [t[0] for t in tags2])

# Check for TotalAssets
tags3 = con.execute("SELECT DISTINCT tag FROM sec_company_facts_complete WHERE tag LIKE '%Asset%' OR tag LIKE '%Liabilit%' LIMIT 20").fetchall()
print('Asset/Liability tags:', [t[0] for t in tags3])

# Check for Cash
tags4 = con.execute("SELECT DISTINCT tag FROM sec_company_facts_complete WHERE tag LIKE '%Cash%' LIMIT 20").fetchall()
print('Cash tags:', [t[0] for t in tags4])

con.close()