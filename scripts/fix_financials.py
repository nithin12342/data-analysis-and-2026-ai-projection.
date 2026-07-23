import duckdb
con = duckdb.connect('databases/deduplicated_tesm_database.duckdb')

print("=" * 70)
print("  RECREATING SEC COMPANY FINANCIALS FROM FACTS")
print("=" * 70)

# Drop and recreate
con.execute("DROP TABLE IF EXISTS sec_company_financials_derived")

# Use the correct tag names
con.execute("""
    CREATE TABLE sec_company_financials_derived AS
    SELECT 
        cik,
        entity_name,
        MAX(CASE WHEN tag = 'RevenueFromContractWithCustomerExcludingAssessedTax' THEN value END) as revenue,
        MAX(CASE WHEN tag = 'NetIncomeLoss' THEN value END) as net_income,
        MAX(CASE WHEN tag = 'OperatingIncomeLoss' THEN value END) as operating_income,
        MAX(CASE WHEN tag = 'ResearchAndDevelopmentExpense' THEN value END) as rd_expense,
        MAX(CASE WHEN tag = 'CashAndCashEquivalentsAtCarryingValue' THEN value END) as cash,
        MAX(CASE WHEN tag = 'TotalAssets' THEN value END) as total_assets,
        MAX(CASE WHEN tag = 'TotalLiabilities' THEN value END) as total_liabilities,
        MAX(CASE WHEN tag = 'CommonStockSharesOutstanding' THEN value END) as shares_outstanding,
        MAX(CASE WHEN tag = 'EntityCommonStockSharesOutstanding' THEN value END) as shares_outstanding_alt,
        MAX(CASE WHEN tag = 'ContractWithCustomerLiabilityCurrent' THEN value END) as rpo_current,
        MAX(CASE WHEN tag = 'ContractWithCustomerLiabilityNoncurrent' THEN value END) as rpo_noncurrent,
        MAX(CASE WHEN tag = 'RevenueRemainingPerformanceObligation' THEN value END) as rpo_total
    FROM sec_company_facts_complete
    GROUP BY cik, entity_name
""")

count = con.execute("SELECT COUNT(*) FROM sec_company_financials_derived").fetchone()[0]
print(f"Created: {count} companies")

companies_with_revenue = con.execute("""
    SELECT COUNT(*) FROM sec_company_financials_derived WHERE revenue IS NOT NULL
""").fetchone()[0]
print(f"Companies with revenue: {companies_with_revenue}")

companies_with_net_income = con.execute("""
    SELECT COUNT(*) FROM sec_company_financials_derived WHERE net_income IS NOT NULL
""").fetchone()[0]
print(f"Companies with net_income: {companies_with_net_income}")

companies_with_assets = con.execute("""
    SELECT COUNT(*) FROM sec_company_financials_derived WHERE total_assets IS NOT NULL
""").fetchone()[0]
print(f"Companies with total_assets: {companies_with_assets}")

# Show sample
sample = con.execute("""
    SELECT cik, entity_name, revenue, net_income, total_assets 
    FROM sec_company_financials_derived 
    WHERE revenue IS NOT NULL
    LIMIT 5
""").fetchall()
print(f"\nSample companies with revenue:")
for s in sample:
    print(f"  {s}")

# Update final_company_panel_quarterly
print("\nUpdating final_company_panel_quarterly...")
con.execute("DROP TABLE IF EXISTS sec_company_financials_new")
con.execute("""
    CREATE TABLE sec_company_financials_new AS
    SELECT 
        cik,
        entity_name as company_name,
        '2025Q4' as period,
        NULL as fy,
        NULL as fp,
        NULL as form,
        revenue,
        net_income,
        operating_income,
        NULL as ocf,
        NULL as capex,
        cash,
        total_assets,
        total_liabilities,
        NULL as equity,
        (COALESCE(rpo_current, 0) + COALESCE(rpo_noncurrent, 0)) as rpo,
        NULL as total_deferred_revenue,
        NULL as debt_current,
        NULL as debt_noncurrent,
        NULL as sbc,
        rd_expense,
        NULL as capex_intensity,
        NULL as rd_intensity,
        NULL as sbc_pct_revenue,
        NULL as operating_margin,
        NULL as net_margin,
        NULL as ocf_to_capex,
        NULL as debt_to_assets,
        NULL as debt_to_equity,
        NULL as fcf_margin,
        NULL as cash_to_debt
    FROM sec_company_financials_derived
    WHERE revenue IS NOT NULL
""")

new_count = con.execute("SELECT COUNT(*) FROM sec_company_financials_new").fetchone()[0]
print(f"New companies to add: {new_count}")

# Append to final_company_panel
con.execute("""
    INSERT INTO final_company_panel_quarterly
    SELECT * FROM sec_company_financials_new
""")
count = con.execute("SELECT COUNT(*) FROM final_company_panel_quarterly").fetchone()[0]
print(f"Updated final_company_panel: {count} rows")

con.close()

print("\n" + "=" * 70)
print("  COMPLETE")
print("=" * 70)