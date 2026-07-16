#!/usr/bin/env python3
"""
Python script to find all CSV and non-CSV data files in the workspace,
analyze their data structures (columns, row counts, categorical fields),
and document them per-file in a markdown catalog.
"""

import os
import csv
import json
import re
import math
from pathlib import Path
from datetime import datetime

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False

try:
    import openpyxl
    OPENPYXL_AVAILABLE = True
except ImportError:
    OPENPYXL_AVAILABLE = False


def count_lines(filepath: Path) -> int:
    """Efficiently count lines in a large text file using chunk reading."""
    count = 0
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b''):
                count += chunk.count(b'\n')
    except Exception:
        # Fallback if any error occurs
        return 0
    return count


def classify_column_values(values, total_count) -> str:
    """Classify a list of values as numeric, date, category, or text."""
    if not values:
        return 'text'

    # Filter out empty/None values
    valid_values = [v for v in values if v is not None and str(v).strip() != '']
    if not valid_values:
        return 'text'

    # Check if mostly numeric
    numeric_count = 0
    for v in valid_values:
        try:
            float(v)
            numeric_count += 1
        except ValueError:
            pass

    if len(valid_values) > 0 and numeric_count / len(valid_values) > 0.8:
        return 'numeric'

    # Check if mostly dates
    date_count = 0
    date_patterns = [
        r'^\d{4}-\d{2}-\d{2}$',
        r'^\d{2}/\d{2}/\d{4}$',
        r'^\d{4}\d{2}\d{2}$',  # YYYYMMDD
    ]
    for v in valid_values:
        v_str = str(v).strip()
        if any(re.match(pat, v_str) for pat in date_patterns):
            date_count += 1

    if len(valid_values) > 0 and date_count / len(valid_values) > 0.8:
        return 'date'

    # Determine cardinality
    unique_vals = set(valid_values)
    unique_count = len(unique_vals)
    unique_ratio = unique_count / total_count if total_count > 0 else 1.0

    # Categorical classification: low cardinality or explicitly small distinct set
    if unique_count <= 15 or (unique_count <= 100 and unique_ratio < 0.20):
        return 'category'

    return 'text'


def extract_numeric_stats(values):
    """Compute basic statistics for a list of numeric-like values."""
    nums = []
    for v in values:
        if v is not None and str(v).strip() != '':
            try:
                nums.append(float(v))
            except ValueError:
                pass
    if not nums:
        return {}
    
    nums.sort()
    n = len(nums)
    mean = sum(nums) / n
    median = nums[n // 2] if n % 2 != 0 else (nums[n // 2 - 1] + nums[n // 2]) / 2
    
    return {
        'min': nums[0],
        'max': nums[-1],
        'mean': mean,
        'median': median
    }


class DataCataloger:
    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir)
        self.csv_files = []
        self.excel_files = []
        self.json_files = []
        self.tsv_files = []  # large text/tsv data files
        
        self.csv_catalog = {}
        self.excel_catalog = {}
        self.json_catalog = {}
        self.tsv_catalog = {}

    def scan_workspace(self):
        """Scan workspace recursively for data files, ignoring code-related paths."""
        exclude_dirs = {'.git', '__pycache__', 'node_modules', '.gemini', '.agents', 'scratch'}
        
        for dirpath, dirnames, filenames in os.walk(self.root_dir):
            # Prune excluded directories in place
            dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
            
            for f in filenames:
                file_path = Path(dirpath) / f
                ext = file_path.suffix.lower()
                
                # Check for CSV
                if ext == '.csv':
                    self.csv_files.append(file_path)
                # Check for Excel
                elif ext in ['.xlsx', '.xls']:
                    self.excel_files.append(file_path)
                # Check for JSON
                elif ext == '.json':
                    # Ignore package.json, tsconfig.json, project config etc.
                    if f not in ['package.json', 'package-lock.json', 'tsconfig.json']:
                        self.json_files.append(file_path)
                # Check for large text data files (e.g. SEC DERA TSV data files)
                elif ext == '.txt' and ('2023q' in str(file_path) or '2024q' in str(file_path) or '2025q' in str(file_path) or '2026q' in str(file_path)):
                    if f in ['num.txt', 'pre.txt', 'sub.txt', 'tag.txt']:
                        self.tsv_files.append(file_path)

    def analyze_csv_files(self):
        """Analyze all found CSV files."""
        print(f"Analyzing {len(self.csv_files)} CSV files...")
        for path in sorted(self.csv_files):
            rel_path = path.relative_to(self.root_dir).as_posix()
            try:
                self.csv_catalog[rel_path] = self._analyze_csv_file(path)
            except Exception as e:
                self.csv_catalog[rel_path] = {'error': str(e), 'file_size': path.stat().st_size}

    def _analyze_csv_file(self, path: Path) -> dict:
        info = {
            'file_size_bytes': path.stat().st_size,
            'row_count': 0,
            'columns': [],
            'column_types': {},
            'category_columns': {},
            'numeric_stats': {},
            'sample_rows': []
        }

        # Try using pandas first, fallback to csv module if needed
        if PANDAS_AVAILABLE:
            df = pd.read_csv(path, low_memory=False)
            df.columns = [str(c) for c in df.columns]
            info['row_count'] = len(df)
            info['columns'] = list(df.columns)
            
            # Analyze each column
            for col in df.columns:
                series = df[col]
                non_null_vals = series.dropna().tolist()
                
                # Classify type
                col_type = classify_column_values(non_null_vals, len(df))
                info['column_types'][col] = col_type
                
                if col_type == 'category':
                    unique_vals = sorted(list(set(non_null_vals)), key=str)
                    info['category_columns'][col] = {
                        'unique_count': len(unique_vals),
                        'null_count': int(series.isnull().sum()),
                        'samples': [str(v) for v in unique_vals[:15]]
                    }
                elif col_type == 'numeric':
                    info['numeric_stats'][col] = extract_numeric_stats(non_null_vals)

            # Sample rows
            info['sample_rows'] = df.head(3).to_dict(orient='records')
        else:
            # Fallback to csv module
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                reader = csv.reader(f)
                header = next(reader, None)
                if not header:
                    return info
                header = [str(c) for c in header]
                info['columns'] = header
                rows = list(reader)
                info['row_count'] = len(rows)

                # Process columns
                for idx, col in enumerate(header):
                    col_vals = [r[idx] for r in rows if idx < len(r)]
                    col_type = classify_column_values(col_vals, len(rows))
                    info['column_types'][col] = col_type

                    if col_type == 'category':
                        non_null = [v for v in col_vals if v.strip() != '']
                        unique_vals = sorted(list(set(non_null)), key=str)
                        info['category_columns'][col] = {
                            'unique_count': len(unique_vals),
                            'null_count': len(rows) - len(non_null),
                            'samples': [str(v) for v in unique_vals[:15]]
                        }
                    elif col_type == 'numeric':
                        info['numeric_stats'][col] = extract_numeric_stats(col_vals)

                # Sample rows
                for r in rows[:3]:
                    row_dict = {}
                    for idx, col in enumerate(header):
                        if idx < len(r):
                            row_dict[col] = r[idx]
                    info['sample_rows'].append(row_dict)

        return info

    def analyze_excel_files(self):
        """Analyze all found Excel files."""
        print(f"Analyzing {len(self.excel_files)} Excel files...")
        for path in sorted(self.excel_files):
            rel_path = path.relative_to(self.root_dir).as_posix()
            try:
                self.excel_catalog[rel_path] = self._analyze_excel_file(path)
            except Exception as e:
                self.excel_catalog[rel_path] = {'error': str(e), 'file_size': path.stat().st_size}

    def _analyze_excel_file(self, path: Path) -> dict:
        info = {
            'file_size_bytes': path.stat().st_size,
            'sheets': {}
        }

        if not PANDAS_AVAILABLE:
            raise ImportError("Pandas is required to parse Excel files in this script.")

        # Read sheet names
        xl = pd.ExcelFile(path)
        for sheet_name in xl.sheet_names:
            # Load sheet
            df = xl.parse(sheet_name)
            df.columns = [str(c) for c in df.columns]
            
            sheet_info = {
                'row_count': len(df),
                'columns': list(df.columns),
                'column_types': {},
                'category_columns': {},
                'numeric_stats': {},
                'sample_rows': []
            }

            for col in df.columns:
                series = df[col]
                non_null_vals = series.dropna().tolist()
                
                # Classify type
                col_type = classify_column_values(non_null_vals, len(df))
                sheet_info['column_types'][col] = col_type
                
                if col_type == 'category':
                    unique_vals = sorted(list(set(non_null_vals)), key=str)
                    sheet_info['category_columns'][col] = {
                        'unique_count': len(unique_vals),
                        'null_count': int(series.isnull().sum()),
                        'samples': [str(v) for v in unique_vals[:15]]
                    }
                elif col_type == 'numeric':
                    sheet_info['numeric_stats'][col] = extract_numeric_stats(non_null_vals)

            # Sample rows
            sheet_info['sample_rows'] = df.head(3).to_dict(orient='records')
            info['sheets'][sheet_name] = sheet_info

        return info

    def analyze_json_files(self):
        """Analyze all found JSON files."""
        print(f"Analyzing {len(self.json_files)} JSON files...")
        for path in sorted(self.json_files):
            rel_path = path.relative_to(self.root_dir).as_posix()
            try:
                self.json_catalog[rel_path] = self._analyze_json_file(path)
            except Exception as e:
                self.json_catalog[rel_path] = {'error': str(e), 'file_size': path.stat().st_size}

    def _analyze_json_file(self, path: Path) -> dict:
        info = {
            'file_size_bytes': path.stat().st_size,
            'is_tabular': False,
            'row_count': 0,
            'columns': [],
            'column_types': {},
            'category_columns': {},
            'structure_summary': {},
            'sample_rows': []
        }

        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            data = json.load(f)

        # Check if it is a list of dictionaries (tabular format)
        if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            info['is_tabular'] = True
            info['row_count'] = len(data)
            
            # Find all unique keys across records
            all_keys = set()
            for record in data[:100]:  # inspect first 100 records for keys
                all_keys.update(record.keys())
            columns = sorted(list(all_keys))
            info['columns'] = columns

            # Classify columns
            for col in columns:
                col_vals = [r.get(col) for r in data if r.get(col) is not None]
                col_type = classify_column_values(col_vals, len(data))
                info['column_types'][col] = col_type

                if col_type == 'category':
                    unique_vals = sorted(list(set(col_vals)), key=str)
                    info['category_columns'][col] = {
                        'unique_count': len(unique_vals),
                        'null_count': len(data) - len(col_vals),
                        'samples': [str(v) for v in unique_vals[:15]]
                    }

            # Sample rows
            info['sample_rows'] = data[:3]
        else:
            # General nested JSON structure analysis
            info['is_tabular'] = False
            info['structure_summary'] = self._summarize_dict_structure(data)

        return info

    def _summarize_dict_structure(self, data, depth=0, max_depth=3) -> dict:
        """Recursively summarize dictionary structures for nested JSON files."""
        if depth > max_depth:
            return {'type': type(data).__name__, 'truncated': True}

        if isinstance(data, dict):
            summary = {'type': 'object', 'keys': {}}
            for k, v in data.items():
                if isinstance(v, (dict, list)):
                    summary['keys'][k] = self._summarize_dict_structure(v, depth + 1, max_depth)
                else:
                    summary['keys'][k] = {'type': type(v).__name__, 'value_sample': str(v)[:50]}
            return summary
        elif isinstance(data, list):
            summary = {'type': 'array', 'length': len(data)}
            if len(data) > 0:
                summary['element_type'] = type(data[0]).__name__
                if isinstance(data[0], (dict, list)):
                    summary['element_structure'] = self._summarize_dict_structure(data[0], depth + 1, max_depth)
            return summary
        else:
            return {'type': type(data).__name__, 'value_sample': str(data)[:50]}

    def analyze_tsv_files(self):
        """Analyze all SEC DERA text files recursively, reading efficiently."""
        print(f"Analyzing {len(self.tsv_files)} SEC DERA text files...")
        for path in sorted(self.tsv_files):
            rel_path = path.relative_to(self.root_dir).as_posix()
            try:
                self.tsv_catalog[rel_path] = self._analyze_tsv_file(path)
            except Exception as e:
                self.tsv_catalog[rel_path] = {'error': str(e), 'file_size': path.stat().st_size}

    def _analyze_tsv_file(self, path: Path) -> dict:
        info = {
            'file_size_bytes': path.stat().st_size,
            'row_count': 0,
            'columns': [],
            'column_types': {},
            'category_columns': {},
            'sample_rows': []
        }

        # Count total lines efficiently (rows = total_lines - 1)
        total_lines = count_lines(path)
        info['row_count'] = max(0, total_lines - 1)

        # Read the first 100 rows to extract schema & classify columns
        rows = []
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            reader = csv.DictReader(f, delimiter='\t')
            info['columns'] = reader.fieldnames or []
            
            # Read first 100 rows
            for i, row in enumerate(reader):
                if i >= 100:
                    break
                rows.append(row)

        if not rows:
            return info

        # Classify columns based on first 100 records
        for col in info['columns']:
            col_vals = [r[col] for r in rows if r[col] is not None]
            col_type = classify_column_values(col_vals, len(rows))
            info['column_types'][col] = col_type

            if col_type == 'category':
                unique_vals = sorted(list(set(col_vals)), key=str)
                null_in_sample = sum(1 for r in rows if r[col] is None or str(r[col]).strip() == '')
                est_nulls = int((null_in_sample / len(rows)) * info['row_count']) if rows else 0
                info['category_columns'][col] = {
                    'unique_count': len(unique_vals),
                    'estimated_null_count': est_nulls,
                    'samples': [str(v) for v in unique_vals[:15]]
                }

        # Sample rows
        info['sample_rows'] = rows[:3]
        return info

    def generate_report(self) -> str:
        """Construct the markdown report from gathered catalogs."""
        md = []
        md.append("# Workspace Data Catalog and Structure Report")
        md.append("")
        md.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        md.append(f"**Root Workspace Directory:** `{self.root_dir.as_posix()}`")
        md.append("")
        
        # Table of Contents
        md.append("## Table of Contents")
        md.append("")
        md.append("1. [Executive Summary](#1-executive-summary)")
        md.append("2. [CSV Files Analysis](#2-csv-files-analysis)")
        md.append("3. [Excel Files Analysis (Advanced Methodology)](#3-excel-files-analysis-advanced-methodology)")
        md.append("4. [JSON Datasets Analysis (Advanced Methodology)](#4-json-datasets-analysis-advanced-methodology)")
        md.append("5. [SEC DERA Text/TSV Datasets (Advanced Methodology)](#5-sec-dera-texttsv-datasets-advanced-methodology)")
        md.append("")
        
        # 1. Executive Summary
        md.append("## 1. Executive Summary")
        md.append("")
        md.append(f"- **Total CSV Files:** {len(self.csv_files)}")
        md.append(f"- **Total Excel Files:** {len(self.excel_files)}")
        md.append(f"- **Total JSON Files:** {len(self.json_files)}")
        md.append(f"- **Total SEC DERA Text Files:** {len(self.tsv_files)}")
        
        total_size_bytes = (
            sum(p.stat().st_size for p in self.csv_files) +
            sum(p.stat().st_size for p in self.excel_files) +
            sum(p.stat().st_size for p in self.json_files) +
            sum(p.stat().st_size for p in self.tsv_files)
        )
        md.append(f"- **Total Data Catalog Size:** {total_size_bytes / (1024 * 1024):.2f} MB")
        md.append("")
        md.append("---")
        md.append("")

        # Helper for printing category details
        def format_categories(cat_dict):
            cat_lines = []
            cat_lines.append("| Category Column | Unique Values Count | Samples / Categories |")
            cat_lines.append("|---|---|---|")
            for col, cat_info in cat_dict.items():
                samples_str = ", ".join(f"`{s}`" for s in cat_info['samples'])
                if cat_info['unique_count'] > len(cat_info['samples']):
                    samples_str += " ... (and more)"
                cat_lines.append(f"| **{col}** | {cat_info['unique_count']} | {samples_str} |")
            return "\n".join(cat_lines)

        # Helper for sample rows table
        def format_sample_table(columns, sample_rows):
            if not sample_rows:
                return "*No sample data available*"
            
            # Select first 7 columns to avoid extremely wide tables in MD
            display_cols = columns[:7]
            has_more_cols = len(columns) > 7

            header_line = "| " + " | ".join(display_cols) + (" | ... |" if has_more_cols else " |")
            sep_line = "| " + " | ".join(["---"] * len(display_cols)) + (" | --- |" if has_more_cols else " |")
            
            table_lines = [header_line, sep_line]
            for row in sample_rows:
                vals = []
                for c in display_cols:
                    val = row.get(c, '')
                    val_str = str(val).replace('\n', ' ').replace('|', '\\|')
                    if len(val_str) > 40:
                        val_str = val_str[:37] + "..."
                    vals.append(val_str)
                row_line = "| " + " | ".join(vals) + (" | ... |" if has_more_cols else " |")
                table_lines.append(row_line)
            return "\n".join(table_lines)

        # Helper for nested json
        def format_nested_json(summary, indent=0):
            lines = []
            prefix = "  " * indent
            if summary.get('type') == 'object':
                lines.append(f"{prefix}- **Object** containing keys:")
                for k, v in sorted(summary.get('keys', {}).items()):
                    if v.get('type') in ['object', 'array']:
                        lines.append(f"{prefix}  - **{k}**: {v.get('type')}")
                        lines.extend(format_nested_json(v, indent + 2))
                    else:
                        lines.append(f"{prefix}  - **{k}** ({v.get('type')}): sample = `{v.get('value_sample')}`")
            elif summary.get('type') == 'array':
                lines.append(f"{prefix}- **Array** of length {summary.get('length')} containing `{summary.get('element_type')}` items.")
                if 'element_structure' in summary:
                    lines.extend(format_nested_json(summary['element_structure'], indent + 1))
            return lines

        # 2. CSV Files Analysis
        md.append("## 2. CSV Files Analysis")
        md.append("")
        for file_path, info in sorted(self.csv_catalog.items()):
            md.append(f"### File: `{file_path}`")
            md.append("")
            if 'error' in info:
                md.append(f"> [!WARNING]")
                md.append(f"> Failed to analyze CSV file. Error: {info['error']}")
                md.append("")
                continue
            
            md.append(f"- **Size:** {info['file_size_bytes'] / 1024:.2f} KB")
            md.append(f"- **Total Rows:** {info['row_count']:,}")
            md.append(f"- **Total Columns:** {len(info['columns'])}")
            
            col_by_type = {'category': [], 'numeric': [], 'date': [], 'text': []}
            for col, t in info['column_types'].items():
                col_by_type[t].append(str(col))
                
            md.append(f"- **Category Columns:** {', '.join(col_by_type['category']) if col_by_type['category'] else '*None*'}")
            md.append(f"- **Numeric Columns:** {', '.join(col_by_type['numeric']) if col_by_type['numeric'] else '*None*'}")
            md.append(f"- **Date Columns:** {', '.join(col_by_type['date']) if col_by_type['date'] else '*None*'}")
            md.append(f"- **Text Columns:** {', '.join(col_by_type['text']) if col_by_type['text'] else '*None*'}")
            md.append("")

            # Category details
            if info['category_columns']:
                md.append("#### Categorical Variable Details")
                md.append("")
                md.append(format_categories(info['category_columns']))
                md.append("")

            # Sample rows
            md.append("#### Sample Data (First 3 rows)")
            md.append("")
            md.append(format_sample_table(info['columns'], info['sample_rows']))
            md.append("")
            md.append("---")
            md.append("")

        # 3. Excel Files Analysis
        md.append("## 3. Excel Files Analysis (Advanced Methodology)")
        md.append("")
        for file_path, info in sorted(self.excel_catalog.items()):
            md.append(f"### File: `{file_path}`")
            md.append("")
            if 'error' in info:
                md.append(f"> [!WARNING]")
                md.append(f"> Failed to analyze Excel file. Error: {info['error']}")
                md.append("")
                continue

            md.append(f"- **Size:** {info['file_size_bytes'] / (1024 * 1024):.2f} MB")
            md.append(f"- **Sheets in Workbook:** {len(info['sheets'])}")
            md.append("")
            
            for sheet_name, sheet_info in info['sheets'].items():
                md.append(f"#### Sheet: `{sheet_name}`")
                md.append("")
                md.append(f"- **Rows:** {sheet_info['row_count']:,}")
                md.append(f"- **Total Columns:** {len(sheet_info['columns'])}")
                
                col_by_type = {'category': [], 'numeric': [], 'date': [], 'text': []}
                for col, t in sheet_info['column_types'].items():
                    col_by_type[t].append(str(col))

                md.append(f"- **Category Columns:** {', '.join(col_by_type['category']) if col_by_type['category'] else '*None*'}")
                md.append(f"- **Numeric Columns:** {', '.join(col_by_type['numeric']) if col_by_type['numeric'] else '*None*'}")
                md.append(f"- **Date/Time Columns:** {', '.join(col_by_type['date']) if col_by_type['date'] else '*None*'}")
                md.append(f"- **Text Columns:** {', '.join(col_by_type['text']) if col_by_type['text'] else '*None*'}")
                md.append("")

                if sheet_info['category_columns']:
                    md.append("##### Categorical Variable Details")
                    md.append("")
                    md.append(format_categories(sheet_info['category_columns']))
                    md.append("")

                md.append("##### Sample Data")
                md.append("")
                md.append(format_sample_table(sheet_info['columns'], sheet_info['sample_rows']))
                md.append("")
            
            md.append("---")
            md.append("")

        # 4. JSON Datasets Analysis
        md.append("## 4. JSON Datasets Analysis (Advanced Methodology)")
        md.append("")
        for file_path, info in sorted(self.json_catalog.items()):
            md.append(f"### File: `{file_path}`")
            md.append("")
            if 'error' in info:
                md.append(f"> [!WARNING]")
                md.append(f"> Failed to analyze JSON file. Error: {info['error']}")
                md.append("")
                continue

            md.append(f"- **Size:** {info['file_size_bytes'] / 1024:.2f} KB")
            
            if info['is_tabular']:
                md.append("- **Format:** Tabular JSON (List of records)")
                md.append(f"- **Total Records:** {info['row_count']:,}")
                md.append(f"- **Total Columns/Keys:** {len(info['columns'])}")
                
                col_by_type = {'category': [], 'numeric': [], 'date': [], 'text': []}
                for col, t in info['column_types'].items():
                    col_by_type[t].append(str(col))

                md.append(f"- **Category Fields:** {', '.join(col_by_type['category']) if col_by_type['category'] else '*None*'}")
                md.append(f"- **Numeric Fields:** {', '.join(col_by_type['numeric']) if col_by_type['numeric'] else '*None*'}")
                md.append(f"- **Text Fields:** {', '.join(col_by_type['text']) if col_by_type['text'] else '*None*'}")
                md.append("")

                if info['category_columns']:
                    md.append("#### Categorical Field Details")
                    md.append("")
                    md.append(format_categories(info['category_columns']))
                    md.append("")

                md.append("#### Sample Records")
                md.append("")
                md.append(format_sample_table(info['columns'], info['sample_rows']))
                md.append("")
            else:
                md.append("- **Format:** Hierarchical/Nested JSON Document")
                md.append("#### JSON Structure Summary")
                md.append("")
                nested_lines = format_nested_json(info['structure_summary'])
                md.extend(nested_lines)
                md.append("")
            
            md.append("---")
            md.append("")

        # 5. SEC DERA Text/TSV Datasets
        md.append("## 5. SEC DERA Text/TSV Datasets (Advanced Methodology)")
        md.append("")
        md.append("> [!NOTE]")
        md.append("> These are large tab-separated text files containing XBRL financial statement dataset chunks.")
        md.append("> The scanner reads these files using a streaming generator to map headers and estimate categories without exhausting system memory.")
        md.append("")
        
        quarters_grouped = {}
        for file_path, info in sorted(self.tsv_catalog.items()):
            match = re.search(r'DATA/(20\d{2}q\d)', file_path)
            if match:
                q = match.group(1)
                if q not in quarters_grouped:
                    quarters_grouped[q] = []
                quarters_grouped[q].append((file_path, info))

        for q, file_list in sorted(quarters_grouped.items()):
            md.append(f"### Quarter: `{q}`")
            md.append("")
            
            for file_path, info in file_list:
                md.append(f"#### File: `{file_path}`")
                md.append("")
                if 'error' in info:
                    md.append(f"**Error analyzing file:** {info['error']}")
                    md.append("")
                    continue
                
                md.append(f"- **Size:** {info['file_size_bytes'] / (1024 * 1024):.2f} MB")
                md.append(f"- **Total Rows:** {info['row_count']:,}")
                md.append(f"- **Total Columns:** {len(info['columns'])}")
                
                col_by_type = {'category': [], 'numeric': [], 'date': [], 'text': []}
                for col, t in info['column_types'].items():
                    col_by_type[t].append(str(col))

                md.append(f"- **Category Columns:** {', '.join(col_by_type['category']) if col_by_type['category'] else '*None*'}")
                md.append(f"- **Numeric Columns:** {', '.join(col_by_type['numeric']) if col_by_type['numeric'] else '*None*'}")
                md.append(f"- **Text Columns:** {', '.join(col_by_type['text']) if col_by_type['text'] else '*None*'}")
                md.append("")

                if info['category_columns']:
                    md.append("##### Sample Categorical Details (First 100 rows sample)")
                    md.append("")
                    md.append(format_categories(info['category_columns']))
                    md.append("")

                md.append("##### Sample Records")
                md.append("")
                md.append(format_sample_table(info['columns'], info['sample_rows']))
                md.append("")
            
            md.append("---")
            md.append("")

        return "\n".join(md)


def main():
    root_dir = "C:/Users/NITHING/Desktop/projections"
    output_md_path = Path(root_dir) / "DATA_CATALOG_SUMMARY.md"

    print("Initializing Data Cataloger...")
    cataloger = DataCataloger(root_dir)

    print("Scanning workspace...")
    cataloger.scan_workspace()
    print(f"Discovered: {len(cataloger.csv_files)} CSVs, "
          f"{len(cataloger.excel_files)} Excels, "
          f"{len(cataloger.json_files)} JSONs, "
          f"{len(cataloger.tsv_files)} SEC TSVs.")

    cataloger.analyze_csv_files()
    cataloger.analyze_excel_files()
    cataloger.analyze_json_files()
    cataloger.analyze_tsv_files()

    print("Building report...")
    report_content = cataloger.generate_report()

    print(f"Writing report to: {output_md_path}")
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(report_content)

    print("Process successfully finished!")


if __name__ == "__main__":
    main()
