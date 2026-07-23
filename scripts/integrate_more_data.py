import duckdb
import pandas as pd
import zipfile
import json
from pathlib import Path

DB_FILE = Path("databases/deduplicated_tesm_database.duckdb")
SEC_ZIP = Path("DATA/not preprocessed/more data/companyfacts.zip")

con = duckdb.connect(str(DB_FILE))

print("=" * 70)
print("  INTEGRATING SEC COMPANY FACTS FROM MORE DATA FOLDER")
print("=" * 70)

# 1. Check the zip file
print(f"\n[1] Checking {SEC_ZIP}...")
print(f"    Size: {SEC_ZIP.stat().st_size / (1024*1024*1024):.2f} GB")

# 2. Extract and process SEC company facts
print("\n[2] Processing SEC Company Facts...")
all_facts = []
with zipfile.ZipFile(SEC_ZIP, 'r') as zf:
    json_files = [f for f in zf.namelist() if f.endswith('.json')]
    print(f"    Found {len(json_files)} JSON files")
    
    # Process first 1000 companies for initial load
    for jf in json_files[:1000]:
        try:
            with zf.open(jf) as f:
                data = json.load(f)
                cik = data.get('cik', '')
                entity_name = data.get('entityName', '')
                
                # Structure: facts -> category -> tag -> units -> unit -> items
                for category, cat_data in data.get('facts', {}).items():
                    for tag, tag_data in cat_data.items():
                        units = tag_data.get('units', {})
                        for unit, unit_data in units.items():
                            for item in unit_data:
                                all_facts.append({
                                    'cik': cik,
                                    'entity_name': entity_name,
                                    'tag': tag,
                                    'unit': unit,
                                    'value': item.get('val'),
                                    'start': item.get('start'),
                                    'end': item.get('end'),
                                    'frame': item.get('frame')
                                })
        except Exception as e:
            pass

print(f"    Extracted {len(all_facts)} facts from 1000 companies")

# 3. Create comprehensive SEC facts table
print("\n[3] Creating comprehensive SEC facts table...")
if all_facts:
    df = pd.DataFrame(all_facts)
    con.execute("DROP TABLE IF EXISTS sec_company_facts_complete")
    con.execute("CREATE TABLE sec_company_facts_complete AS SELECT * FROM df")
    print(f"    Created: {len(df)} rows")
    
    # Show sample data
    print("\n    Sample data:")
    sample = con.execute("SELECT cik, entity_name, tag, value, frame FROM sec_company_facts_complete LIMIT 5").fetchall()
    for row in sample:
        print(f"      {row}")
    
    # Show unique tags
    tags = con.execute("SELECT DISTINCT tag FROM sec_company_facts_complete LIMIT 20").fetchall()
    print(f"\n    Unique tags: {[t[0] for t in tags]}")
    
    # Count companies
    companies = con.execute("SELECT COUNT(DISTINCT cik) FROM sec_company_facts_complete").fetchone()[0]
    print(f"    Unique companies: {companies}")

# 4. Create company financials from SEC facts
print("\n[4] Creating company financials from SEC facts...")
try:
    con.execute("""
        CREATE TABLE IF NOT EXISTS sec_company_financials_derived AS
        SELECT 
            cik,
            entity_name,
            MAX(CASE WHEN tag IN ('Revenue', 'Revenues', 'RevenueFromContractWithCustomerIncludingAssessedTax', 'SalesRevenueServicesNet', 'SalesRevenueGoodsNet', 'RevenueFromSaleOfGoods', 'RegulatedOperatingRevenue', 'RegulatedAndUnregulatedOperatingRevenue', 'RevenuesFromExternalCustomers', 'SegmentReportingSegmentRevenue') THEN value END) as revenue,
            MAX(CASE WHEN tag IN ('NetIncomeLoss', 'IncomeLossAttributableToParent', 'ProfitLoss') THEN value END) as net_income,
            MAX(CASE WHEN tag IN ('OperatingIncomeLoss', 'OperatingExpenses') THEN value END) as operating_income,
            MAX(CASE WHEN tag = 'ResearchAndDevelopmentExpense' THEN value END) as rd_expense,
            MAX(CASE WHEN tag IN ('CashAndCashEquivalentsAtCarryingValue', 'CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents') THEN value END) as cash,
            MAX(CASE WHEN tag IN ('TotalAssets', 'Assets', 'AssetsCurrent') THEN value END) as total_assets,
            MAX(CASE WHEN tag IN ('TotalLiabilities', 'Liabilities', 'LiabilitiesCurrent') THEN value END) as total_liabilities,
            MAX(CASE WHEN tag = 'CommonStockSharesOutstanding' THEN value END) as shares_outstanding,
            MAX(CASE WHEN tag = 'EntityCommonStockSharesOutstanding' THEN value END) as shares_outstanding_alt,
            MAX(CASE WHEN tag = 'ContractWithCustomerLiabilityCurrent' THEN value END) as rpo_current,
            MAX(CASE WHEN tag = 'ContractWithCustomerLiabilityNoncurrent' THEN value END) as rpo_noncurrent,
            MAX(CASE WHEN tag = 'RevenueRemainingPerformanceObligation' THEN value END) as rpo_total
        FROM sec_company_facts_complete
        GROUP BY cik, entity_name
    """)
    count = con.execute("SELECT COUNT(*) FROM sec_company_financials_derived").fetchone()[0]
    print(f"    Created: {count} companies")
    
    # Show companies with revenue
    companies_with_revenue = con.execute("""
        SELECT COUNT(*) FROM sec_company_financials_derived WHERE revenue IS NOT NULL
    """).fetchone()[0]
    print(f"    Companies with revenue: {companies_with_revenue}")
except Exception as e:
    print(f"    Error: {e}")

# 5. Update final_company_panel_quarterly
print("\n[5] Updating final_company_panel_quarterly...")
try:
    # Create a temporary table with new data
    con.execute("""
        CREATE TABLE IF NOT EXISTS sec_company_financials_new AS
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
    
    # Count new companies
    new_count = con.execute("SELECT COUNT(*) FROM sec_company_financials_new").fetchone()[0]
    print(f"    New companies to add: {new_count}")
    
    # Append to final_company_panel (without ON CONFLICT)
    con.execute("""
        INSERT INTO final_company_panel_quarterly
        SELECT * FROM sec_company_financials_new
    """)
    count = con.execute("SELECT COUNT(*) FROM final_company_panel_quarterly").fetchone()[0]
    print(f"    Updated final_company_panel: {count} rows")
except Exception as e:
    print(f"    Error: {e}")

# 6. Check the arxiv data
print("\n[6] Checking arXiv metadata...")
arxiv_file = Path("DATA/not preprocessed/more data/arxiv-metadata-oai-snapshot.json")
if arxiv_file.exists():
    print(f"    Size: {arxiv_file.stat().st_size / (1024*1024):.2f} MB")
    with open(arxiv_file, 'r') as f:
        for i, line in enumerate(f):
            if i < 2:
                print(f"    Line {i+1}: {line[:100]}...")
            else:
                break
else:
    print("    File not found")

# 7. Check the parquet file
print("\n[7] Checking training data parquet...")
parquet_file = Path("DATA/not preprocessed/more data/train-00000-of-00001-cced8514c7ed782a.parquet")
if parquet_file.exists():
    print(f"    Size: {parquet_file.stat().st_size / (1024*1024):.2f} MB")
    try:
        df = pd.read_parquet(parquet_file, nrows=5)
        print(f"    Columns: {df.columns.tolist()}")
        print(f"    Sample rows: {len(df)}")
    except Exception as e:
        print(f"    Error reading: {e}")
else:
    print("    File not found")

con.close()

print("\n" + "=" * 70)
print("  INTEGRATION COMPLETE")
print("=" * 70)