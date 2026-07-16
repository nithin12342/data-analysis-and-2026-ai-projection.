"""
SEC DERA Data Loader - DuckDB Implementation
Loads 13 quarters of SEC financial statement data for AI ecosystem companies.
"""

import duckdb
import os
import pandas as pd
from pathlib import Path

# Configuration
DATA_ROOT = Path(r"C:\Users\NITHING\Desktop\projections\DATA")
DB_PATH = Path(r"C:\Users\NITHING\Desktop\projections\databases\sec_dera.duckdb")

# 13 quarters available
QUARTERS = [
    "2023q1", "2023q2", "2023q3", "2023q4",
    "2024q1", "2024q2", "2024q3", "2024q4",
    "2025q1", "2025q2", "2025q3", "2025q4",
    "2026q1"
]

# Target CIKs for AI ecosystem companies (P0/P1 priority)
TARGET_CIKS = {
    # Hyperscalers
    789019: "MICROSOFT",
    1018724: "AMAZON",
    1652044: "ALPHABET",
    1326801: "META_PLATFORMS",
    1341439: "ORACLE",
    1108524: "SALESFORCE",
    
    # Semiconductors
    1045810: "NVIDIA",
    2488: "AMD",
    50863: "INTEL",
    1730168: "BROADCOM",
    1835632: "MARVELL",
    804328: "QUALCOMM",
    723125: "MICRON",
    6951: "APPLIED_MATERIALS",
    707549: "LAM_RESEARCH",
    319201: "KLA",
    883241: "SYNOPSYS",
    813672: "CADENCE",
    937966: "ASML",
    
    # DC REITs / Infrastructure
    1101239: "EQUINIX",
    1297996: "DIGITAL_REALTY",
    
    # Server/Hardware
    1571996: "DELL",
    1645590: "HPE",
}

# Key XBRL tags to extract (high-value for financial modeling)
TARGET_TAGS = [
    # Revenue
    "RevenueFromContractWithCustomerExcludingAssessedTax",
    "Revenues",
    "RevenueFromContractWithCustomerIncludingAssessedTax",
    
    # Segment Revenue (for cloud/DC breakdowns)
    "SegmentRevenue",
    "SegmentProfit",
    
    # Expenses
    "ResearchAndDevelopmentExpense",
    "SalesAndMarketingExpense",
    "GeneralAndAdministrativeExpense",
    "ShareBasedCompensation",
    "OperatingIncomeLoss",
    "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
    "NetIncomeLoss",
    
    # Cash Flow
    "NetCashProvidedByUsedInOperatingActivities",
    "PaymentsToAcquirePropertyPlantAndEquipment",
    "PaymentsToAcquireProductiveAssets",
    "PaymentsForAcquisitionOfBusinesses",
    "ProceedsFromIssuanceOfLongTermDebt",
    "RepaymentsOfLongTermDebt",
    "PaymentsForRepurchaseOfCommonStock",
    "PaymentsOfDividends",
    
    # Balance Sheet
    "CashAndCashEquivalentsAtCarryingValue",
    "ShortTermInvestments",
    "AccountsReceivableNetCurrent",
    "InventoryNet",
    "PropertyPlantAndEquipmentNet",
    "OperatingLeaseRightOfUseAsset",
    "IntangibleAssetsNetExcludingGoodwill",
    "Goodwill",
    "Assets",
    "AccountsPayableCurrent",
    "ContractWithCustomerLiabilityCurrent",
    "ContractWithCustomerLiabilityNoncurrent",
    "RevenueRemainingPerformanceObligation",
    "LongTermDebtCurrent",
    "LongTermDebtNoncurrent",
    "OperatingLeaseLiabilityCurrent",
    "OperatingLeaseLiabilityNoncurrent",
    "Liabilities",
    "StockholdersEquity",
]

def create_database():
    """Create DuckDB database and load all SEC data."""
    con = duckdb.connect(str(DB_PATH))
    
    print("=" * 70)
    print("SEC DERA Data Loader - Building DuckDB Database")
    print(f"Database: {DB_PATH}")
    print(f"Quarters: {len(QUARTERS)} ({QUARTERS[0]} to {QUARTERS[-1]})")
    print(f"Target Companies: {len(TARGET_CIKS)}")
    print(f"Target Tags: {len(TARGET_TAGS)}")
    print("=" * 70)
    
    # Create schema
    con.execute("CREATE SCHEMA IF NOT EXISTS sec")
    con.execute("CREATE SCHEMA IF NOT EXISTS model")
    
    # 1. Load submissions metadata for all quarters
    print("\n[1/4] Loading submissions metadata (sub.txt)...")
    for i, q in enumerate(QUARTERS):
        sub_path = DATA_ROOT / q / "sub.txt"
        if sub_path.exists():
            con.execute(f"""
                CREATE TABLE IF NOT EXISTS sec.submissions_{q} AS
                SELECT * FROM read_csv_auto(
                    '{sub_path}', 
                    delim='\t', header=true, nullstr='', 
                    sample_size=10000,
                    columns={{
                        adsh: 'VARCHAR', cik: 'VARCHAR', name: 'VARCHAR', 
                        sic: 'VARCHAR', countryba: 'VARCHAR', stprba: 'VARCHAR',
                        cityba: 'VARCHAR', zipba: 'VARCHAR', bas1: 'VARCHAR', bas2: 'VARCHAR',
                        baph: 'VARCHAR', countryma: 'VARCHAR', stprma: 'VARCHAR',
                        cityma: 'VARCHAR', zipma: 'VARCHAR', mas1: 'VARCHAR', mas2: 'VARCHAR',
                        countryinc: 'VARCHAR', stprinc: 'VARCHAR', ein: 'VARCHAR',
                        former: 'VARCHAR', changed: 'VARCHAR', afs: 'VARCHAR',
                        wksi: 'VARCHAR', fye: 'VARCHAR', form: 'VARCHAR',
                        period: 'VARCHAR', fy: 'VARCHAR', fp: 'VARCHAR',
                        filed: 'VARCHAR', accepted: 'VARCHAR', prevrpt: 'VARCHAR',
                        detail: 'VARCHAR', instance: 'VARCHAR', nciks: 'VARCHAR',
                        aciks: 'VARCHAR'
                    }}
                )
            """)
            count = con.execute(f"SELECT COUNT(*) FROM sec.submissions_{q} WHERE cik IN ({','.join(str(c) for c in TARGET_CIKS.keys())})").fetchone()[0]
            print(f"  {q}: {count} target company filings")
        else:
            print(f"  {q}: FILE NOT FOUND")
    
    # 2. Load tags taxonomy (once, from first quarter)
    print("\n[2/4] Loading XBRL tags taxonomy (tag.txt)...")
    tag_path = DATA_ROOT / QUARTERS[0] / "tag.txt"
    if tag_path.exists():
        con.execute(f"""
            CREATE TABLE IF NOT EXISTS sec.tags AS
            SELECT * FROM read_csv_auto(
                '{tag_path}',
                delim='\t', header=true, nullstr='',
                columns={{tag: 'VARCHAR', version: 'VARCHAR', custom: 'VARCHAR',
                         abstract: 'VARCHAR', datatype: 'VARCHAR', iord: 'VARCHAR',
                         crdr: 'VARCHAR', tlabel: 'VARCHAR', doc: 'VARCHAR'}}
            )
        """)
        tag_count = con.execute("SELECT COUNT(*) FROM sec.tags").fetchone()[0]
        print(f"  Loaded {tag_count:,} tags")
    
    # 3. Load numeric facts (filtered for target companies and tags)
    print("\n[3/4] Loading numeric facts (num.txt) - filtered...")
    cik_list = "','".join(str(c) for c in TARGET_CIKS.keys())
    tag_list = "','".join(TARGET_TAGS)
    
    total_facts = 0
    for i, q in enumerate(QUARTERS):
        num_path = DATA_ROOT / q / "num.txt"
        if num_path.exists():
            # Create temp table for this quarter's filtered facts
            con.execute(f"""
                CREATE TABLE IF NOT EXISTS sec.facts_{q} AS
                SELECT 
                    n.adsh, n.tag, n.version, n.ddate, n.qtrs, n.uom,
                    n.segments, n.coreg, n.value, n.footnote,
                    s.cik, s.name, s.form, s.period, s.fy, s.fp, s.filed
                FROM read_csv_auto(
                    '{num_path}',
                    delim='\t', header=true, nullstr='',
                    columns={{
                        adsh: 'VARCHAR', tag: 'VARCHAR', version: 'VARCHAR',
                        ddate: 'VARCHAR', qtrs: 'INTEGER', uom: 'VARCHAR',
                        segments: 'VARCHAR', coreg: 'VARCHAR', value: 'DOUBLE',
                        footnote: 'VARCHAR'
                    }}
                ) n
                INNER JOIN sec.submissions_{q} s ON n.adsh = s.adsh
                WHERE s.cik IN ('{cik_list}')
                  AND n.tag IN ('{tag_list}')
            """)
            count = con.execute(f"SELECT COUNT(*) FROM sec.facts_{q}").fetchone()[0]
            total_facts += count
            print(f"  {q}: {count:,} facts")
        else:
            print(f"  {q}: FILE NOT FOUND")
    
    print(f"\n  Total facts loaded: {total_facts:,}")
    
    # 4. Create unified quarterly financials view
    print("\n[4/4] Creating unified quarterly financials table...")
    
    # Union all quarters
    union_queries = []
    for q in QUARTERS:
        union_queries.append(f"SELECT * FROM sec.facts_{q}")
    
    union_sql = " UNION ALL ".join(union_queries)
    
    con.execute(f"""
        CREATE TABLE IF NOT EXISTS sec.quarterly_financials AS
        {union_sql}
    """)
    
    total_rows = con.execute("SELECT COUNT(*) FROM sec.quarterly_financials").fetchone()[0]
    print(f"  Unified table: {total_rows:,} rows")
    
    # Create pivoted view (company x quarter x metric)
    print("\n[5/5] Creating pivoted metrics table...")
    con.execute("""
        CREATE TABLE IF NOT EXISTS model.company_quarterly_metrics AS
        SELECT 
            cik,
            name,
            form,
            period,
            fy,
            fp,
            filed,
            -- Revenue
            MAX(CASE WHEN tag = 'RevenueFromContractWithCustomerExcludingAssessedTax' THEN value END) AS revenue,
            MAX(CASE WHEN tag = 'Revenues' THEN value END) AS revenues_alt,
            MAX(CASE WHEN tag = 'RevenueFromContractWithCustomerIncludingAssessedTax' THEN value END) AS revenue_incl_tax,
            -- R&D
            MAX(CASE WHEN tag = 'ResearchAndDevelopmentExpense' THEN value END) AS rd_expense,
            -- S&M
            MAX(CASE WHEN tag = 'SalesAndMarketingExpense' THEN value END) AS sm_expense,
            -- G&A
            MAX(CASE WHEN tag = 'GeneralAndAdministrativeExpense' THEN value END) AS ga_expense,
            -- SBC
            MAX(CASE WHEN tag = 'ShareBasedCompensation' THEN value END) AS sbc,
            -- Operating Income
            MAX(CASE WHEN tag = 'OperatingIncomeLoss' THEN value END) AS operating_income,
            -- Pre-tax Income
            MAX(CASE WHEN tag = 'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest' THEN value END) AS pretax_income,
            -- Net Income
            MAX(CASE WHEN tag = 'NetIncomeLoss' THEN value END) AS net_income,
            -- Operating Cash Flow
            MAX(CASE WHEN tag = 'NetCashProvidedByUsedInOperatingActivities' THEN value END) AS ocf,
            -- CapEx
            MAX(CASE WHEN tag = 'PaymentsToAcquirePropertyPlantAndEquipment' THEN value END) AS capex,
            MAX(CASE WHEN tag = 'PaymentsToAcquireProductiveAssets' THEN value END) AS capex_alt,
            -- Acquisitions
            MAX(CASE WHEN tag = 'PaymentsForAcquisitionOfBusinesses' THEN value END) AS acquisitions,
            -- Debt
            MAX(CASE WHEN tag = 'ProceedsFromIssuanceOfLongTermDebt' THEN value END) AS debt_issuance,
            MAX(CASE WHEN tag = 'RepaymentsOfLongTermDebt' THEN value END) AS debt_repayment,
            -- Share Repurchases
            MAX(CASE WHEN tag = 'PaymentsForRepurchaseOfCommonStock' THEN value END) AS share_repurchases,
            -- Dividends
            MAX(CASE WHEN tag = 'PaymentsOfDividends' THEN value END) AS dividends,
            -- Balance Sheet
            MAX(CASE WHEN tag = 'CashAndCashEquivalentsAtCarryingValue' THEN value END) AS cash,
            MAX(CASE WHEN tag = 'ShortTermInvestments' THEN value END) AS short_term_investments,
            MAX(CASE WHEN tag = 'AccountsReceivableNetCurrent' THEN value END) AS receivables,
            MAX(CASE WHEN tag = 'InventoryNet' THEN value END) AS inventory,
            MAX(CASE WHEN tag = 'PropertyPlantAndEquipmentNet' THEN value END) AS ppe_net,
            MAX(CASE WHEN tag = 'OperatingLeaseRightOfUseAsset' THEN value END) AS lease_rou_asset,
            MAX(CASE WHEN tag = 'IntangibleAssetsNetExcludingGoodwill' THEN value END) AS intangibles,
            MAX(CASE WHEN tag = 'Goodwill' THEN value END) AS goodwill,
            MAX(CASE WHEN tag = 'Assets' THEN value END) AS total_assets,
            MAX(CASE WHEN tag = 'AccountsPayableCurrent' THEN value END) AS payables,
            MAX(CASE WHEN tag = 'ContractWithCustomerLiabilityCurrent' THEN value END) AS deferred_rev_current,
            MAX(CASE WHEN tag = 'ContractWithCustomerLiabilityNoncurrent' THEN value END) AS deferred_rev_noncurrent,
            MAX(CASE WHEN tag = 'RevenueRemainingPerformanceObligation' THEN value END) AS rpo,
            MAX(CASE WHEN tag = 'LongTermDebtCurrent' THEN value END) AS debt_current,
            MAX(CASE WHEN tag = 'LongTermDebtNoncurrent' THEN value END) AS debt_noncurrent,
            MAX(CASE WHEN tag = 'OperatingLeaseLiabilityCurrent' THEN value END) AS lease_liab_current,
            MAX(CASE WHEN tag = 'OperatingLeaseLiabilityNoncurrent' THEN value END) AS lease_liab_noncurrent,
            MAX(CASE WHEN tag = 'Liabilities' THEN value END) AS total_liabilities,
            MAX(CASE WHEN tag = 'StockholdersEquity' THEN value END) AS equity,
            -- Segment Revenue (where available)
            MAX(CASE WHEN tag = 'SegmentRevenue' THEN value END) AS segment_revenue,
            MAX(CASE WHEN tag = 'SegmentProfit' THEN value END) AS segment_profit
        FROM sec.quarterly_financials
        GROUP BY cik, name, form, period, fy, fp, filed
        ORDER BY cik, period
    """)
    
    metric_count = con.execute("SELECT COUNT(*) FROM model.company_quarterly_metrics").fetchone()[0]
    print(f"  Company-quarter metrics: {metric_count} rows")
    
    # Compute derived metrics
    print("\n[6/6] Computing derived metrics...")
    con.execute("""
        CREATE TABLE IF NOT EXISTS model.company_quarterly_derived AS
        SELECT 
            cik,
            name,
            period,
            fy,
            fp,
            form,
            -- Base metrics
            revenue,
            rd_expense,
            sm_expense,
            ga_expense,
            sbc,
            operating_income,
            net_income,
            ocf,
            COALESCE(capex, capex_alt) AS capex,
            acquisitions,
            cash,
            short_term_investments,
            total_assets,
            total_liabilities,
            equity,
            deferred_rev_current,
            deferred_rev_noncurrent,
            rpo,
            debt_current,
            debt_noncurrent,
            lease_liab_current,
            lease_liab_noncurrent,
            -- Derived metrics
            CASE WHEN revenue > 0 THEN capex / revenue END AS capex_intensity,
            CASE WHEN revenue > 0 THEN rd_expense / revenue END AS rd_intensity,
            CASE WHEN revenue > 0 THEN sbc / revenue END AS sbc_pct_revenue,
            CASE WHEN revenue > 0 THEN operating_income / revenue END AS operating_margin,
            CASE WHEN revenue > 0 THEN net_income / revenue END AS net_margin,
            CASE WHEN capex > 0 THEN ocf / capex END AS ocf_to_capex,
            CASE WHEN total_assets > 0 THEN (debt_current + debt_noncurrent) / total_assets END AS debt_to_assets,
            CASE WHEN equity > 0 THEN (debt_current + debt_noncurrent) / equity END AS debt_to_equity,
            COALESCE(deferred_rev_current, 0) + COALESCE(deferred_rev_noncurrent, 0) AS total_deferred_revenue,
            CASE WHEN total_deferred_revenue > 0 AND rpo > 0 THEN rpo / total_deferred_revenue END AS rpo_to_deferred_ratio,
            CASE WHEN revenue > 0 THEN (ocf - capex) / revenue END AS fcf_margin,
            COALESCE(debt_current, 0) + COALESCE(debt_noncurrent, 0) AS total_debt,
            COALESCE(cash, 0) + COALESCE(short_term_investments, 0) AS cash_and_investments,
            CASE WHEN (COALESCE(debt_current, 0) + COALESCE(debt_noncurrent, 0)) > 0 
                 THEN (COALESCE(cash, 0) + COALESCE(short_term_investments, 0)) / (COALESCE(debt_current, 0) + COALESCE(debt_noncurrent, 0))
            END AS cash_to_debt
        FROM model.company_quarterly_metrics
    """)
    
    derived_count = con.execute("SELECT COUNT(*) FROM model.company_quarterly_derived").fetchone()[0]
    print(f"  Derived metrics table: {derived_count} rows")
    
    # Summary stats
    print("\n" + "=" * 70)
    print("LOAD COMPLETE - SUMMARY")
    print("=" * 70)
    
    # Companies loaded
    companies = con.execute("""
        SELECT cik, name, COUNT(*) as quarters, MIN(period) as first_q, MAX(period) as last_q
        FROM model.company_quarterly_derived
        GROUP BY cik, name
        ORDER BY name
    """).fetchall()
    
    print(f"\nCompanies with data ({len(companies)}):")
    for cik, name, qtrs, first, last in companies:
        print(f"  {name} (CIK:{cik}): {qtrs} quarters ({first} to {last})")
    
    # Key metrics coverage
    print("\nKey metric coverage (non-null %):")
    for metric in ['revenue', 'capex', 'rd_expense', 'sbc', 'ocf', 'rpo', 'total_debt', 'cash_and_investments']:
        cov = con.execute(f"""
            SELECT 
                COUNT(CASE WHEN {metric} IS NOT NULL THEN 1 END) * 100.0 / COUNT(*) as pct
            FROM model.company_quarterly_derived
        """).fetchone()[0]
        print(f"  {metric}: {cov:.1f}%")
    
    con.close()
    print(f"\nDatabase saved to: {DB_PATH}")
    return DB_PATH


def export_key_tables():
    """Export key tables to CSV for model integration."""
    con = duckdb.connect(str(DB_PATH))
    
    output_dir = DATA_ROOT / "sec_exports"
    output_dir.mkdir(exist_ok=True)
    
    print("\nExporting key tables to CSV...")
    
    # 1. Company quarterly metrics (full)
    con.execute(f"""
        COPY model.company_quarterly_derived 
        TO '{output_dir}/company_quarterly_metrics.csv' 
        (HEADER, DELIMITER ',')
    """)
    print(f"  Exported: company_quarterly_metrics.csv")
    
    # 2. Hyperscaler CapEx trajectory
    con.execute(f"""
        COPY (
            SELECT name, period, fy, fp, revenue, capex, capex_intensity, ocf, ocf_to_capex
            FROM model.company_quarterly_derived
            WHERE name IN ('MICROSOFT', 'AMAZON', 'ALPHABET', 'META_PLATFORMS', 'ORACLE', 'SALESFORCE')
            ORDER BY name, period
        ) TO '{output_dir}/hyperscaler_capex.csv' (HEADER, DELIMITER ',')
    """)
    print(f"  Exported: hyperscaler_capex.csv")
    
    # 3. Semiconductor Data Center revenue
    con.execute(f"""
        COPY (
            SELECT name, period, fy, fp, revenue, rd_expense, rd_intensity, capex, capex_intensity
            FROM model.company_quarterly_derived
            WHERE name IN ('NVIDIA', 'AMD', 'INTEL', 'BROADCOM', 'MARVELL', 'QUALCOMM', 'MICRON')
            ORDER BY name, period
        ) TO '{output_dir}/semiconductor_metrics.csv' (HEADER, DELIMITER ',')
    """)
    print(f"  Exported: semiconductor_metrics.csv")
    
    # 4. RPO / Deferred Revenue for contract lag modeling
    con.execute(f"""
        COPY (
            SELECT name, period, fy, fp, revenue, rpo, total_deferred_revenue, 
                   deferred_rev_current, deferred_rev_noncurrent,
                   rpo_to_deferred_ratio
            FROM model.company_quarterly_derived
            WHERE rpo IS NOT NULL OR total_deferred_revenue > 0
            ORDER BY name, period
        ) TO '{output_dir}/rpo_deferred_revenue.csv' (HEADER, DELIMITER ',')
    """)
    print(f"  Exported: rpo_deferred_revenue.csv")
    
    # 5. SBC burden for IPO quality / financial modeling
    con.execute(f"""
        COPY (
            SELECT name, period, fy, fp, revenue, sbc, sbc_pct_revenue, net_income
            FROM model.company_quarterly_derived
            WHERE sbc IS NOT NULL
            ORDER BY name, period
        ) TO '{output_dir}/sbc_burden.csv' (HEADER, DELIMITER ',')
    """)
    print(f"  Exported: sbc_burden.csv")
    
    # 6. DC REIT metrics
    con.execute(f"""
        COPY (
            SELECT name, period, fy, fp, revenue, capex, capex_intensity, 
                   total_debt, cash_and_investments, debt_to_equity
            FROM model.company_quarterly_derived
            WHERE name IN ('EQUINIX', 'DIGITAL_REALTY')
            ORDER BY name, period
        ) TO '{output_dir}/dc_reit_metrics.csv' (HEADER, DELIMITER ',')
    """)
    print(f"  Exported: dc_reit_metrics.csv")
    
    con.close()
    print(f"\nAll exports saved to: {output_dir}")


if __name__ == "__main__":
    # Step 1: Build database
    db_path = create_database()
    
    # Step 2: Export CSVs for model integration
    export_key_tables()
    
    print("\n✅ SEC DERA data pipeline complete!")
    print(f"   Database: {db_path}")
    print(f"   Exports: {DATA_ROOT / 'sec_exports'}")