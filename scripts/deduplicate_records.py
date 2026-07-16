#!/usr/bin/env python3
"""
Python script to recursively find and remove duplicate rows (in-place)
from CSV and Excel (spreadsheet) files in the workspace.
"""

import os
import pandas as pd
from pathlib import Path

def deduplicate_csv(filepath: Path) -> int:
    try:
        # Load the CSV
        df = pd.read_csv(filepath, low_memory=False)
        dup_count = df.duplicated().sum()
        
        if dup_count > 0:
            # Drop duplicates in-place
            df_clean = df.drop_duplicates()
            df_clean.to_csv(filepath, index=False)
            return dup_count
    except Exception as e:
        print(f"Error deduplicating CSV {filepath.name}: {e}")
    return 0


def deduplicate_excel(filepath: Path) -> int:
    try:
        xl = pd.ExcelFile(filepath)
        cleaned_sheets = {}
        total_removed = 0
        any_changes = False
        
        for sheet_name in xl.sheet_names:
            df = xl.parse(sheet_name)
            dup_count = df.duplicated().sum()
            
            if dup_count > 0:
                df = df.drop_duplicates()
                total_removed += dup_count
                any_changes = True
            cleaned_sheets[sheet_name] = df
            
        if any_changes:
            with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                for sheet_name, df in cleaned_sheets.items():
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
            return total_removed
    except Exception as e:
        print(f"Error deduplicating Excel {filepath.name}: {e}")
    return 0


def main():
    workspace = Path(r"C:\Users\NITHING\Desktop\projections")
    exclude_dirs = {'.git', '.gemini', '.agents', 'scratch'}
    
    csv_count = 0
    excel_count = 0
    total_csv_removed = 0
    total_excel_removed = 0
    
    print("Scanning workspace for data files...")
    
    for root, dirs, files in os.walk(workspace):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for f in files:
            filepath = Path(root) / f
            ext = filepath.suffix.lower()
            
            if ext == '.csv':
                removed = deduplicate_csv(filepath)
                if removed > 0:
                    print(f"[CLEANED] CSV: {filepath.relative_to(workspace)} -> Removed {removed} duplicate rows.")
                    total_csv_removed += removed
                    csv_count += 1
            elif ext in ['.xlsx', '.xls']:
                removed = deduplicate_excel(filepath)
                if removed > 0:
                    print(f"[CLEANED] Excel: {filepath.relative_to(workspace)} -> Removed {removed} duplicate rows across sheets.")
                    total_excel_removed += removed
                    excel_count += 1
                    
    print("\n=== Deduplication Summary ===")
    print(f"Deduplicated {csv_count} CSV files (removed {total_csv_removed} rows).")
    print(f"Deduplicated {excel_count} Excel files (removed {total_excel_removed} rows).")


if __name__ == "__main__":
    main()
