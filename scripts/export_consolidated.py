import duckdb
import pandas as pd
from pathlib import Path

conn = duckdb.connect("databases/consolidated_data.duckdb")

# Get all tables
tables = conn.execute("SHOW TABLES").fetchall()
tables = [t[0] for t in tables]

print(f"Exporting {len(tables)} tables to CSV and Excel...")

# Create output directories
csv_dir = Path("consolidated_csv")
xlsx_dir = Path("consolidated_xlsx")
csv_dir.mkdir(exist_ok=True)
xlsx_dir.mkdir(exist_ok=True)

# Export each table to CSV
for table in tables:
    try:
        df = conn.execute(f"SELECT * FROM {table}").df()
        csv_path = csv_dir / f"{table}.csv"
        df.to_csv(csv_path, index=False)
        print(f"[OK] {table}: {len(df)} rows -> {csv_path}")
    except Exception as e:
        print(f"[FAIL] {table}: {e}")

# Create master Excel file with all tables as sheets
excel_path = xlsx_dir / "consolidated_all_tables.xlsx"
with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    for table in tables:
        try:
            df = conn.execute(f"SELECT * FROM {table}").df()
            # Excel sheet names max 31 chars
            sheet_name = table[:31]
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"[OK] {table} -> sheet '{sheet_name}'")
        except Exception as e:
            print(f"[FAIL] {table}: {e}")

print(f"\nMaster Excel: {excel_path}")

# Create a summary catalog
catalog = []
for table in tables:
    try:
        df = conn.execute(f"SELECT * FROM {table}").df()
        catalog.append({
            "table_name": table,
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": ", ".join(df.columns[:10]) + ("..." if len(df.columns) > 10 else "")
        })
    except Exception as e:
        catalog.append({
            "table_name": table,
            "rows": "ERROR",
            "columns": "ERROR",
            "column_names": str(e)
        })

catalog_df = pd.DataFrame(catalog)
catalog_df.to_csv("consolidated_csv/_CATALOG.csv", index=False)
catalog_df.to_excel("consolidated_xlsx/_CATALOG.xlsx", index=False)
print("\nCatalog saved to _CATALOG.csv and _CATALOG.xlsx")

conn.close()
print("\nDone!")