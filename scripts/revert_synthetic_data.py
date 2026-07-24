import duckdb
import os
from pathlib import Path

DB_FILE = Path("databases/deduplicated_tesm_database.duckdb")
con = duckdb.connect(str(DB_FILE))

print("=" * 70)
print("  REVERTING SYNTHETIC DATA TO PRESERVE REAL DATA INTEGRITY")
print("=" * 70)

# Tables that were synthetically generated and need to be dropped
synthetic_tables = [
    'private_ai_company_financials_estimated',
    'private_ai_valuation_rounds',
    'vendor_token_usage_proxy',
    'dotcom_ipo_database',
    'dotcom_company_financials_proxy',
    'dotcom_drawdown_summary',
    'equity_prices_daily_expanded',
    'ai_ipo_database',
    'historical_backtest',
    'model_validation_metrics'
]

print("\nDropping synthetic tables...")
for t in synthetic_tables:
    try:
        con.execute(f"DROP TABLE IF EXISTS {t}")
        print(f"  Dropped: {t}")
    except Exception as e:
        print(f"  Error dropping {t}: {e}")

# Check what we have in the original database
print("\n\nChecking original database (DATA/tesm_54_tables.duckdb)...")
orig_con = duckdb.connect('DATA/tesm_54_tables.duckdb')
orig_tables = orig_con.execute('SHOW TABLES').fetchall()
print(f"Original database has {len(orig_tables)} tables:")
for t in orig_tables:
    count = orig_con.execute(f'SELECT COUNT(*) FROM {t[0]}').fetchone()[0]
    print(f"  {t[0]}: {count:,} rows")
orig_con.close()

# Check current database
print("\n\nChecking current database...")
tables = con.execute('SHOW TABLES').fetchall()
print(f"Current database has {len(tables)} tables")
for t in tables[:30]:
    count = con.execute(f'SELECT COUNT(*) FROM {t[0]}').fetchone()[0]
    print(f"  {t[0]}: {count:,} rows")

con.close()

print("\n" + "=" * 70)
print("  REVERT COMPLETE")
print("=" * 70)