import duckdb
import pandas as pd
from pathlib import Path
import os

DB_FILE = Path("databases/deduplicated_tesm_database.duckdb")

con = duckdb.connect(str(DB_FILE))

print("=" * 70)
print("  DATABASE QUALITY IMPROVEMENT - PHASE 1")
print("=" * 70)

# 1. Check sec_num_2026q1 structure
print("\n[1] Checking sec_num_2026q1 structure...")
try:
    cols = [c[0] for c in con.execute("DESCRIBE sec_num_2026q1").fetchall()]
    print(f"    Columns: {cols[:10]}...")
    count = con.execute("SELECT COUNT(*) FROM sec_num_2026q1").fetchone()[0]
    print(f"    Total rows: {count:,}")
except Exception as e:
    print(f"    Error: {e}")

# 2. Check equity prices tickers
print("\n[2] Checking equity price coverage...")
try:
    ticker_count = con.execute("SELECT COUNT(DISTINCT ticker) FROM equity_prices_daily").fetchone()[0]
    date_range = con.execute("SELECT MIN(date), MAX(date) FROM equity_prices_daily").fetchone()
    print(f"    Unique tickers: {ticker_count}")
    print(f"    Date range: {date_range[0]} to {date_range[1]}")
except Exception as e:
    print(f"    Error: {e}")

# 3. Check valuation data
print("\n[3] Checking valuation data...")
try:
    val_count = con.execute("SELECT COUNT(*) FROM market_cap_quarterly").fetchone()[0]
    print(f"    Valuation rows: {val_count}")
except Exception as e:
    print(f"    Error: {e}")

# 4. Create final_company_panel_quarterly using correct columns
print("\n[4] Creating final_company_panel_quarterly...")
try:
    con.execute("DROP TABLE IF EXISTS final_company_panel_quarterly")
    con.execute("""
    CREATE TABLE final_company_panel_quarterly AS
    SELECT 
        cik,
        name as company_name,
        period,
        fy,
        fp,
        form,
        revenue,
        net_income,
        operating_income,
        ocf,
        capex,
        cash,
        total_assets,
        total_liabilities,
        equity,
        rpo,
        total_deferred_revenue,
        debt_current,
        debt_noncurrent,
        sbc,
        rd_expense,
        capex_intensity,
        rd_intensity,
        sbc_pct_revenue,
        operating_margin,
        net_margin,
        ocf_to_capex,
        debt_to_assets,
        debt_to_equity,
        fcf_margin,
        cash_to_debt
    FROM sec_company_quarterly_derived
    """)
    count = con.execute("SELECT COUNT(*) FROM final_company_panel_quarterly").fetchone()[0]
    print(f"    Created: {count} rows")
except Exception as e:
    print(f"    Error: {e}")

# 5. Create final_valuation_panel_quarterly
print("\n[5] Creating final_valuation_panel_quarterly...")
try:
    con.execute("DROP TABLE IF EXISTS final_valuation_panel_quarterly")
    con.execute("""
    CREATE TABLE final_valuation_panel_quarterly AS
    SELECT 
        c.cik,
        c.company_name,
        c.period,
        c.revenue,
        c.net_income,
        c.operating_income,
        c.cash,
        c.total_assets,
        c.total_liabilities,
        c.debt_current,
        c.debt_noncurrent,
        (COALESCE(c.debt_current, 0) + COALESCE(c.debt_noncurrent, 0)) as total_debt,
        c.rpo,
        m.market_cap,
        CASE WHEN m.market_cap IS NOT NULL AND c.revenue IS NOT NULL AND c.revenue > 0 
             THEN m.market_cap / c.revenue ELSE NULL END as price_to_sales,
        CASE WHEN m.market_cap IS NOT NULL AND c.net_income IS NOT NULL AND c.net_income <> 0 
             THEN m.market_cap / c.net_income ELSE NULL END as price_to_earnings,
        CASE WHEN (COALESCE(c.debt_current, 0) + COALESCE(c.debt_noncurrent, 0)) IS NOT NULL AND m.market_cap IS NOT NULL 
             THEN m.market_cap + (COALESCE(c.debt_current, 0) + COALESCE(c.debt_noncurrent, 0)) ELSE NULL END as enterprise_value
    FROM final_company_panel_quarterly c
    LEFT JOIN market_cap_quarterly m ON c.company_name = m.name AND c.period = m.period
    """)
    count = con.execute("SELECT COUNT(*) FROM final_valuation_panel_quarterly").fetchone()[0]
    print(f"    Created: {count} rows")
except Exception as e:
    print(f"    Error: {e}")

# 6. Create data dictionary
print("\n[6] Creating data dictionary...")
try:
    con.execute("DROP TABLE IF EXISTS data_dictionary")
    con.execute("""
    CREATE TABLE data_dictionary AS
    SELECT 
        table_name,
        column_name,
        data_type,
        'See source' as description,
        'consolidated' as source,
        CURRENT_TIMESTAMP as last_updated
    FROM information_schema.columns
    WHERE table_schema = 'main'
    """)
    count = con.execute("SELECT COUNT(*) FROM data_dictionary").fetchone()[0]
    print(f"    Created: {count} entries")
except Exception as e:
    print(f"    Error: {e}")

# 7. Summary
print("\n" + "=" * 70)
print("  SUMMARY")
print("=" * 70)
tables = con.execute("SHOW TABLES").fetchall()
print(f"  Total tables: {len(tables)}")

# Show newly created tables
for t in ['final_company_panel_quarterly', 'final_valuation_panel_quarterly', 'data_dictionary']:
    try:
        count = con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        cols = len(con.execute(f"DESCRIBE {t}").fetchall())
        print(f"  {t}: {count} rows, {cols} columns")
    except Exception as e:
        print(f"  {t}: Error - {e}")

con.close()

print("\n" + "=" * 70)
print("  PHASE 1 COMPLETE")
print("=" * 70)