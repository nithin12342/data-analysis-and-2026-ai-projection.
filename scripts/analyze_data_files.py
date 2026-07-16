#!/usr/bin/env python3
"""
Comprehensive Data File Analysis Tool
- Finds all CSV files and identifies category columns
- Analyzes non-CSV files using advanced methodology
- Documents all findings in a markdown report
"""

import os
import csv
import json
import re
import hashlib
import mimetypes
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter
from typing import Dict, List, Set, Any, Optional
import sys

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    print("Warning: pandas not available, using built-in csv module")

try:
    import magic
    MAGIC_AVAILABLE = True
except ImportError:
    MAGIC_AVAILABLE = False


class DataFileAnalyzer:
    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir)
        self.csv_files = []
        self.non_csv_files = []
        self.results = {
            'csv_analysis': {},
            'non_csv_analysis': {},
            'summary': {}
        }

    def find_all_files(self) -> None:
        """Discover all files in the directory tree."""
        for filepath in self.root_dir.rglob('*'):
            if filepath.is_file() and not filepath.name.startswith('.'):
                if filepath.suffix.lower() == '.csv':
                    self.csv_files.append(filepath)
                else:
                    self.non_csv_files.append(filepath)

    def analyze_csv_files(self) -> None:
        """Analyze all CSV files for structure, columns, and category detection."""
        for csv_path in self.csv_files:
            try:
                analysis = self._analyze_single_csv(csv_path)
                self.results['csv_analysis'][str(csv_path.relative_to(self.root_dir))] = analysis
            except Exception as e:
                self.results['csv_analysis'][str(csv_path.relative_to(self.root_dir))] = {
                    'error': str(e),
                    'file_size': csv_path.stat().st_size
                }

    def _analyze_single_csv(self, csv_path: Path) -> Dict[str, Any]:
        """Deep analysis of a single CSV file."""
        analysis = {
            'file_path': str(csv_path.relative_to(self.root_dir)),
            'file_size_bytes': csv_path.stat().st_size,
            'file_size_mb': round(csv_path.stat().st_size / (1024 * 1024), 2),
            'encoding': self._detect_encoding(csv_path),
            'delimiter': self._detect_delimiter(csv_path),
            'row_count': 0,
            'columns': [],
            'column_types': {},
            'category_columns': [],
            'numeric_columns': [],
            'date_columns': [],
            'text_columns': [],
            'unique_value_counts': {},
            'sample_data': [],
            'null_counts': {},
            'statistics': {}
        }

        if PANDAS_AVAILABLE:
            return self._analyze_with_pandas(csv_path, analysis)
        else:
            return self._analyze_with_csv_module(csv_path, analysis)

    def _detect_encoding(self, filepath: Path) -> str:
        """Detect file encoding."""
        encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252', 'iso-8859-1']
        for enc in encodings:
            try:
                with open(filepath, 'r', encoding=enc) as f:
                    f.read(1024)
                return enc
            except UnicodeDecodeError:
                continue
        return 'unknown'

    def _detect_delimiter(self, filepath: Path) -> str:
        """Detect CSV delimiter."""
        with open(filepath, 'r', encoding=self._detect_encoding(filepath)) as f:
            sample = f.read(8192)
        sniffer = csv.Sniffer()
        try:
            dialect = sniffer.sniff(sample, delimiters=',;\t|')
            return dialect.delimiter
        except:
            return ','

    def _analyze_with_pandas(self, csv_path: Path, analysis: Dict) -> Dict:
        """Analyze CSV using pandas for rich statistics."""
        df = pd.read_csv(csv_path, encoding=analysis['encoding'], delimiter=analysis['delimiter'], low_memory=False)

        analysis['row_count'] = len(df)
        analysis['columns'] = list(df.columns)
        analysis['column_types'] = {col: str(dtype) for col, dtype in df.dtypes.items()}

        for col in df.columns:
            unique_count = df[col].nunique()
            null_count = df[col].isnull().sum()
            analysis['unique_value_counts'][col] = int(unique_count)
            analysis['null_counts'][col] = int(null_count)

            col_type = self._classify_column(df[col], unique_count, len(df))
            if col_type == 'category':
                analysis['category_columns'].append(col)
            elif col_type == 'numeric':
                analysis['numeric_columns'].append(col)
            elif col_type == 'date':
                analysis['date_columns'].append(col)
            else:
                analysis['text_columns'].append(col)

            if col in analysis['category_columns'] and unique_count < 50:
                analysis['statistics'][col] = df[col].value_counts().head(20).to_dict()
            elif col in analysis['numeric_columns']:
                analysis['statistics'][col] = {
                    'mean': float(df[col].mean()) if not df[col].isnull().all() else None,
                    'std': float(df[col].std()) if not df[col].isnull().all() else None,
                    'min': float(df[col].min()) if not df[col].isnull().all() else None,
                    'max': float(df[col].max()) if not df[col].isnull().all() else None,
                    'median': float(df[col].median()) if not df[col].isnull().all() else None
                }

        analysis['sample_data'] = df.head(3).to_dict('records')

        return analysis

    def _analyze_with_csv_module(self, csv_path: Path, analysis: Dict) -> Dict:
        """Analyze CSV using built-in csv module."""
        with open(csv_path, 'r', encoding=analysis['encoding']) as f:
            reader = csv.DictReader(f, delimiter=analysis['delimiter'])
            analysis['columns'] = reader.fieldnames or []
            rows = list(reader)

        analysis['row_count'] = len(rows)

        if not rows:
            return analysis

        for col in analysis['columns']:
            values = [row[col] for row in rows if row[col]]
            unique_vals = set(values)
            analysis['unique_value_counts'][col] = len(unique_vals)
            analysis['null_counts'][col] = len(rows) - len(values)

            col_type = self._classify_column_values(values, unique_vals, len(rows))
            if col_type == 'category':
                analysis['category_columns'].append(col)
            elif col_type == 'numeric':
                analysis['numeric_columns'].append(col)
            elif col_type == 'date':
                analysis['date_columns'].append(col)
            else:
                analysis['text_columns'].append(col)

            if col in analysis['category_columns'] and len(unique_vals) < 50:
                counter = Counter(values)
                analysis['statistics'][col] = dict(counter.most_common(20))

        analysis['sample_data'] = rows[:3]
        return analysis

    def _classify_column(self, series, unique_count: int, total_count: int) -> str:
        """Classify column type using pandas series."""
        if pd.api.types.is_numeric_dtype(series):
            return 'numeric'
        if pd.api.types.is_datetime64_any_dtype(series):
            return 'date'

        unique_ratio = unique_count / total_count if total_count > 0 else 0
        if unique_ratio < 0.05 and unique_count < 100:
            return 'category'
        if unique_count < 20:
            return 'category'
        return 'text'

    def _classify_column_values(self, values: List, unique_vals: Set, total_count: int) -> str:
        """Classify column type using raw values."""
        if not values:
            return 'text'

        numeric_count = 0
        date_count = 0
        for v in values[:100]:
            try:
                float(v)
                numeric_count += 1
            except:
                pass
            if re.match(r'\d{4}-\d{2}-\d{2}', v) or re.match(r'\d{2}/\d{2}/\d{4}', v):
                date_count += 1

        if numeric_count / len(values) > 0.8:
            return 'numeric'
        if date_count / len(values) > 0.8:
            return 'date'

        unique_ratio = len(unique_vals) / total_count if total_count > 0 else 0
        if unique_ratio < 0.05 and len(unique_vals) < 100:
            return 'category'
        if len(unique_vals) < 20:
            return 'category'
        return 'text'

    def analyze_non_csv_files(self) -> None:
        """Advanced analysis of non-CSV files."""
        for filepath in self.non_csv_files:
            try:
                analysis = self._analyze_non_csv_file(filepath)
                self.results['non_csv_analysis'][str(filepath.relative_to(self.root_dir))] = analysis
            except Exception as e:
                self.results['non_csv_analysis'][str(filepath.relative_to(self.root_dir))] = {
                    'error': str(e),
                    'file_size': filepath.stat().st_size
                }

    def _analyze_non_csv_file(self, filepath: Path) -> Dict[str, Any]:
        """Advanced multi-method analysis of non-CSV files."""
        stat = filepath.stat()
        analysis = {
            'file_path': str(filepath.relative_to(self.root_dir)),
            'file_name': filepath.name,
            'extension': filepath.suffix.lower(),
            'file_size_bytes': stat.st_size,
            'file_size_kb': round(stat.st_size / 1024, 2),
            'file_size_mb': round(stat.st_size / (1024 * 1024), 2),
            'mime_type': mimetypes.guess_type(str(filepath))[0],
            'magic_type': self._get_magic_type(filepath) if MAGIC_AVAILABLE else None,
            'encoding': self._detect_encoding(filepath),
            'line_count': 0,
            'char_count': 0,
            'word_count': 0,
            'structure': {},
            'content_summary': {},
            'extracted_data': {},
            'code_analysis': {},
            'markdown_analysis': {},
            'json_analysis': {},
            'html_analysis': {},
            'config_analysis': {},
            'hashes': {
                'md5': self._file_hash(filepath, 'md5'),
                'sha256': self._file_hash(filepath, 'sha256')
            }
        }

        content = self._read_file_content(filepath, analysis['encoding'])
        if content is None:
            analysis['error'] = 'Could not read file content'
            return analysis

        analysis['char_count'] = len(content)
        analysis['line_count'] = content.count('\n') + 1
        analysis['word_count'] = len(content.split())

        ext = filepath.suffix.lower()

        if ext == '.py':
            analysis['code_analysis'] = self._analyze_python_code(content, filepath)
        elif ext in ['.js', '.ts', '.jsx', '.tsx']:
            analysis['code_analysis'] = self._analyze_javascript_code(content, filepath)
        elif ext == '.md':
            analysis['markdown_analysis'] = self._analyze_markdown(content, filepath)
        elif ext == '.json':
            analysis['json_analysis'] = self._analyze_json(content, filepath)
        elif ext in ['.html', '.htm']:
            analysis['html_analysis'] = self._analyze_html(content, filepath)
        elif ext in ['.css', '.scss', '.sass']:
            analysis['code_analysis'] = self._analyze_css(content, filepath)
        elif ext in ['.yml', '.yaml']:
            analysis['config_analysis'] = self._analyze_yaml(content, filepath)
        elif ext in ['.toml', '.ini', '.cfg', '.conf']:
            analysis['config_analysis'] = self._analyze_config(content, filepath)
        elif ext in ['.xml', '.svg']:
            analysis['structure'] = self._analyze_xml(content, filepath)

        analysis['content_summary'] = self._generate_content_summary(content, ext)
        analysis['extracted_data'] = self._extract_key_data(content, ext)

        return analysis

    def _get_magic_type(self, filepath: Path) -> str:
        """Get file type using python-magic."""
        try:
            return magic.from_file(str(filepath), mime=True)
        except:
            return None

    def _file_hash(self, filepath: Path, algorithm: str) -> str:
        """Compute file hash."""
        hasher = hashlib.new(algorithm)
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                hasher.update(chunk)
        return hasher.hexdigest()

    def _read_file_content(self, filepath: Path, encoding: str) -> Optional[str]:
        """Read file content with fallback encodings."""
        encodings = [encoding, 'utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
        for enc in encodings:
            try:
                with open(filepath, 'r', encoding=enc) as f:
                    return f.read()
            except UnicodeDecodeError:
                continue
        return None

    def _analyze_python_code(self, content: str, filepath: Path) -> Dict:
        """Analyze Python code structure."""
        analysis = {
            'imports': [],
            'classes': [],
            'functions': [],
            'constants': [],
            'decorators': [],
            'async_functions': [],
            'type_hints': False,
            'docstrings': [],
            'complexity_indicators': {}
        }

        import_pattern = r'^(?:from\s+(\S+)\s+)?import\s+(.+)$'
        class_pattern = r'^class\s+(\w+)(?:\([^)]*\))?:'
        func_pattern = r'^(?:async\s+)?def\s+(\w+)\s*\([^)]*\)(?:\s*->\s*[^:]+)?:'
        decorator_pattern = r'^@(\w+)'
        constant_pattern = r'^([A-Z_][A-Z0-9_]*)\s*='

        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('import ') or line.startswith('from '):
                analysis['imports'].append(line)
            match = re.match(class_pattern, line)
            if match:
                analysis['classes'].append(match.group(1))
            match = re.match(func_pattern, line)
            if match:
                if line.startswith('async '):
                    analysis['async_functions'].append(match.group(1))
                else:
                    analysis['functions'].append(match.group(1))
            match = re.match(decorator_pattern, line)
            if match:
                analysis['decorators'].append(match.group(1))
            match = re.match(constant_pattern, line)
            if match:
                analysis['constants'].append(match.group(1))
            if '->' in line and 'def ' in line:
                analysis['type_hints'] = True

        analysis['complexity_indicators'] = {
            'total_lines': len(content.split('\n')),
            'import_count': len(analysis['imports']),
            'class_count': len(analysis['classes']),
            'function_count': len(analysis['functions']),
            'async_function_count': len(analysis['async_functions'])
        }
        return analysis

    def _analyze_javascript_code(self, content: str, filepath: Path) -> Dict:
        """Analyze JavaScript/TypeScript code structure."""
        analysis = {
            'imports': [],
            'exports': [],
            'functions': [],
            'classes': [],
            'constants': [],
            'variables': [],
            'arrow_functions': 0,
            'async_functions': 0,
            'typescript': filepath.suffix in ['.ts', '.tsx'],
            'jsx': filepath.suffix in ['.jsx', '.tsx'],
            'frameworks': []
        }

        import_pattern = r'import\s+.*\s+from\s+[\'"]([^\'"]+)[\'"]'
        export_pattern = r'export\s+(?:default\s+)?(?:const|function|class|var|let)\s+(\w+)'
        func_pattern = r'(?:async\s+)?function\s+(\w+)'
        arrow_pattern = r'(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>'
        class_pattern = r'class\s+(\w+)'
        const_pattern = r'const\s+(\w+)\s*='

        analysis['imports'] = re.findall(import_pattern, content)
        analysis['exports'] = re.findall(export_pattern, content)
        analysis['functions'] = re.findall(func_pattern, content)
        analysis['classes'] = re.findall(class_pattern, content)
        analysis['constants'] = re.findall(const_pattern, content)
        analysis['arrow_functions'] = len(re.findall(arrow_pattern, content))
        analysis['async_functions'] = len(re.findall(r'async\s+function', content))

        frameworks = ['react', 'vue', 'angular', 'next', 'nuxt', 'express', 'koa', 'fastify']
        for fw in frameworks:
            if fw in content.lower():
                analysis['frameworks'].append(fw)

        return analysis

    def _analyze_markdown(self, content: str, filepath: Path) -> Dict:
        """Analyze Markdown structure."""
        analysis = {
            'headers': [],
            'header_counts': Counter(),
            'links': [],
            'images': [],
            'code_blocks': [],
            'tables': 0,
            'lists': 0,
            'word_count': len(content.split()),
            'toc': []
        }

        for line in content.split('\n'):
            header_match = re.match(r'^(#{1,6})\s+(.+)$', line)
            if header_match:
                level = len(header_match.group(1))
                text = header_match.group(2).strip()
                analysis['headers'].append({'level': level, 'text': text})
                analysis['header_counts'][level] += 1
                analysis['toc'].append({'level': level, 'text': text})

        analysis['links'] = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        analysis['images'] = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)
        analysis['code_blocks'] = re.findall(r'```(\w*)\n(.*?)\n```', content, re.DOTALL)
        analysis['tables'] = content.count('|') // 2 if '|' in content else 0
        analysis['lists'] = len(re.findall(r'^\s*[-*+]\s+', content, re.MULTILINE))

        return analysis

    def _analyze_json(self, content: str, filepath: Path) -> Dict:
        """Analyze JSON structure."""
        analysis = {
            'valid': False,
            'root_type': None,
            'key_count': 0,
            'depth': 0,
            'keys': [],
            'sample_values': {},
            'arrays': [],
            'nested_objects': 0
        }

        try:
            data = json.loads(content)
            analysis['valid'] = True
            analysis['root_type'] = type(data).__name__
            analysis = self._analyze_json_structure(data, analysis, prefix='')
        except json.JSONDecodeError as e:
            analysis['error'] = str(e)
        return analysis

    def _analyze_json_structure(self, data: Any, analysis: Dict, prefix: str = '', depth: int = 0) -> Dict:
        """Recursively analyze JSON structure."""
        analysis['depth'] = max(analysis['depth'], depth)

        if isinstance(data, dict):
            analysis['key_count'] += len(data)
            for key, value in data.items():
                full_key = f"{prefix}.{key}" if prefix else key
                analysis['keys'].append(full_key)
                if len(analysis['keys']) <= 50:
                    analysis['sample_values'][full_key] = str(value)[:100]
                if isinstance(value, (dict, list)):
                    analysis['nested_objects'] += 1
                self._analyze_json_structure(value, analysis, full_key, depth + 1)
        elif isinstance(data, list):
            analysis['arrays'].append({'path': prefix, 'length': len(data)})
            if data:
                self._analyze_json_structure(data[0], analysis, f"{prefix}[0]", depth + 1)
        return analysis

    def _analyze_html(self, content: str, filepath: Path) -> Dict:
        """Analyze HTML structure."""
        analysis = {
            'doctype': False,
            'tags': Counter(),
            'ids': [],
            'classes': [],
            'scripts': [],
            'stylesheets': [],
            'meta_tags': [],
            'forms': 0,
            'inputs': 0,
            'links': 0
        }

        analysis['doctype'] = content.strip().lower().startswith('<!doctype')

        tags = re.findall(r'<(\w+)[^>]*>', content)
        analysis['tags'] = Counter(tags)

        analysis['ids'] = re.findall(r'id=["\']([^"\']+)["\']', content)
        analysis['classes'] = re.findall(r'class=["\']([^"\']+)["\']', content)
        analysis['scripts'] = re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', content)
        analysis['stylesheets'] = re.findall(r'<link[^>]*href=["\']([^"\']+)["\']', content)
        analysis['meta_tags'] = re.findall(r'<meta[^>]*>', content)
        analysis['forms'] = content.count('<form')
        analysis['inputs'] = content.count('<input')
        analysis['links'] = content.count('<a ')

        return analysis

    def _analyze_css(self, content: str, filepath: Path) -> Dict:
        """Analyze CSS structure."""
        analysis = {
            'selectors': [],
            'properties': Counter(),
            'media_queries': [],
            'keyframes': [],
            'custom_properties': [],
            'imports': [],
            'rules_count': 0
        }

        analysis['imports'] = re.findall(r'@import\s+[\'"]([^\'"]+)[\'"]', content)
        analysis['selectors'] = re.findall(r'([^{]+)\{', content)
        analysis['media_queries'] = re.findall(r'@media[^{]+\{', content)
        analysis['keyframes'] = re.findall(r'@keyframes\s+(\w+)', content)
        analysis['custom_properties'] = re.findall(r'--[\w-]+:', content)

        props = re.findall(r'(\w+(?:-\w+)*):\s*[^;]+;', content)
        analysis['properties'] = Counter(props)
        analysis['rules_count'] = len(analysis['selectors'])

        return analysis

    def _analyze_yaml(self, content: str, filepath: Path) -> Dict:
        """Analyze YAML structure."""
        try:
            import yaml
            data = yaml.safe_load(content)
            return self._analyze_json_structure(data, {
                'valid': True,
                'root_type': type(data).__name__,
                'key_count': 0,
                'depth': 0,
                'keys': [],
                'sample_values': {},
                'arrays': [],
                'nested_objects': 0
            })
        except Exception as e:
            return {'error': str(e), 'valid': False}

    def _analyze_config(self, content: str, filepath: Path) -> Dict:
        """Analyze config file structure."""
        analysis = {
            'sections': [],
            'key_value_pairs': 0,
            'comments': 0
        }
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('[') and line.endswith(']'):
                analysis['sections'].append(line[1:-1])
            elif '=' in line and not line.startswith('#') and not line.startswith(';'):
                analysis['key_value_pairs'] += 1
            elif line.startswith('#') or line.startswith(';'):
                analysis['comments'] += 1
        return analysis

    def _analyze_xml(self, content: str, filepath: Path) -> Dict:
        """Analyze XML/SVG structure."""
        analysis = {
            'declaration': False,
            'root_element': None,
            'elements': Counter(),
            'attributes': Counter(),
            'namespaces': []
        }
        analysis['declaration'] = content.strip().startswith('<?xml')
        elements = re.findall(r'<(\w+)(?:\s+[^>]*)?>', content)
        analysis['elements'] = Counter(elements)
        if elements:
            analysis['root_element'] = elements[0]
        attrs = re.findall(r'(\w+(?::\w+)?)=["\']', content)
        analysis['attributes'] = Counter(attrs)
        namespaces = re.findall(r'xmlns(?::(\w+))?=["\']([^"\']+)["\']', content)
        analysis['namespaces'] = [{'prefix': p or 'default', 'uri': u} for p, u in namespaces]
        return analysis

    def _generate_content_summary(self, content: str, ext: str) -> Dict:
        """Generate a text summary of file content."""
        lines = content.split('\n')
        non_empty = [l for l in lines if l.strip()]

        return {
            'total_lines': len(lines),
            'non_empty_lines': len(non_empty),
            'empty_line_ratio': (len(lines) - len(non_empty)) / len(lines) if lines else 0,
            'avg_line_length': sum(len(l) for l in lines) / len(lines) if lines else 0,
            'max_line_length': max(len(l) for l in lines) if lines else 0,
            'first_5_lines': lines[:5],
            'last_5_lines': lines[-5:] if len(lines) >= 5 else lines
        }

    def _extract_key_data(self, content: str, ext: str) -> Dict:
        """Extract key data patterns from content."""
        extracted = {
            'emails': re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content),
            'urls': re.findall(r'https?://[^\s<>"{}|\\^`\[\]]+', content),
            'ips': re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', content),
            'dates_iso': re.findall(r'\b\d{4}-\d{2}-\d{2}\b', content),
            'dates_us': re.findall(r'\b\d{2}/\d{2}/\d{4}\b', content),
            'version_numbers': re.findall(r'\bv?\d+\.\d+\.\d+(?:-[\w.]+)?\b', content),
            'file_paths': re.findall(r'(?:[A-Za-z]:)?[/\\][\w\-./\\ ]+', content),
            'hex_colors': re.findall(r'#[0-9a-fA-F]{3,8}\b', content),
            'uuids': re.findall(r'\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b', content, re.IGNORECASE),
        }
        for key in extracted:
            extracted[key] = list(set(extracted[key]))[:20]
        return extracted

    def generate_summary(self) -> None:
        """Generate overall summary statistics."""
        total_csv_size = sum(f.stat().st_size for f in self.csv_files)
        total_non_csv_size = sum(f.stat().st_size for f in self.non_csv_files)

        ext_counts = Counter(f.suffix.lower() for f in self.non_csv_files)

        self.results['summary'] = {
            'analysis_timestamp': datetime.now().isoformat(),
            'root_directory': str(self.root_dir),
            'csv_files': {
                'count': len(self.csv_files),
                'total_size_mb': round(total_csv_size / (1024 * 1024), 2),
                'files': [str(f.relative_to(self.root_dir)) for f in self.csv_files]
            },
            'non_csv_files': {
                'count': len(self.non_csv_files),
                'total_size_mb': round(total_non_csv_size / (1024 * 1024), 2),
                'by_extension': dict(ext_counts.most_common())
            },
            'total_files': len(self.csv_files) + len(self.non_csv_files),
            'total_size_mb': round((total_csv_size + total_non_csv_size) / (1024 * 1024), 2)
        }

    def write_markdown_report(self, output_path: str) -> None:
        """Write comprehensive markdown report."""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(self._generate_markdown())

    def _generate_markdown(self) -> str:
        """Generate the full markdown report content."""
        lines = []

        # Header
        lines.append("# Comprehensive Data File Analysis Report")
        lines.append("")
        lines.append(f"**Generated:** {self.results['summary']['analysis_timestamp']}")
        lines.append(f"**Root Directory:** `{self.results['summary']['root_directory']}`")
        lines.append("")

        # Summary
        lines.append("## Executive Summary")
        lines.append("")
        s = self.results['summary']
        lines.append(f"- **Total Files Analyzed:** {s['total_files']}")
        lines.append(f"- **Total Size:** {s['total_size_mb']} MB")
        lines.append(f"- **CSV Files:** {s['csv_files']['count']} ({s['csv_files']['total_size_mb']} MB)")
        lines.append(f"- **Non-CSV Files:** {s['non_csv_files']['count']} ({s['non_csv_files']['total_size_mb']} MB)")
        lines.append("")

        if s['non_csv_files']['by_extension']:
            lines.append("### Non-CSV Files by Extension")
            lines.append("")
            lines.append("| Extension | Count |")
            lines.append("|-----------|-------|")
            for ext, count in s['non_csv_files']['by_extension'].items():
                lines.append(f"| {ext} | {count} |")
            lines.append("")

        # CSV Analysis
        lines.append("## CSV File Analysis")
        lines.append("")

        for rel_path, analysis in self.results['csv_analysis'].items():
            lines.append(f"### `{rel_path}`")
            lines.append("")
            if 'error' in analysis:
                lines.append(f"**Error:** {analysis['error']}")
                lines.append("")
                continue

            lines.append(f"- **Size:** {analysis['file_size_mb']} MB ({analysis['file_size_bytes']:,} bytes)")
            lines.append(f"- **Encoding:** {analysis['encoding']}")
            lines.append(f"- **Delimiter:** `{analysis['delimiter']}`")
            lines.append(f"- **Rows:** {analysis['row_count']:,}")
            lines.append(f"- **Columns:** {len(analysis['columns'])}")
            lines.append("")

            lines.append("#### Column Classification")
            lines.append("")
            lines.append("| Type | Count | Columns |")
            lines.append("|------|-------|---------|")
            lines.append(f"| Category | {len(analysis['category_columns'])} | {', '.join(analysis['category_columns']) if analysis['category_columns'] else '—'} |")
            lines.append(f"| Numeric | {len(analysis['numeric_columns'])} | {', '.join(analysis['numeric_columns']) if analysis['numeric_columns'] else '—'} |")
            lines.append(f"| Date | {len(analysis['date_columns'])} | {', '.join(analysis['date_columns']) if analysis['date_columns'] else '—'} |")
            lines.append(f"| Text | {len(analysis['text_columns'])} | {', '.join(analysis['text_columns']) if analysis['text_columns'] else '—'} |")
            lines.append("")

            if analysis['category_columns']:
                lines.append("#### Category Column Details")
                lines.append("")
                for col in analysis['category_columns']:
                    uc = analysis['unique_value_counts'].get(col, 0)
                    nc = analysis['null_counts'].get(col, 0)
                    lines.append(f"**{col}** — Unique values: {uc}, Nulls: {nc}")
                    if col in analysis['statistics']:
                        lines.append("")
                        lines.append("| Value | Count |")
                        lines.append("|-------|-------|")
                        for val, cnt in list(analysis['statistics'][col].items())[:15]:
                            lines.append(f"| {val} | {cnt} |")
                        lines.append("")

            if analysis['numeric_columns']:
                lines.append("#### Numeric Column Statistics")
                lines.append("")
                lines.append("| Column | Mean | Std | Min | Max | Median |")
                lines.append("|--------|------|-----|-----|-----|--------|")
                for col in analysis['numeric_columns']:
                    if col in analysis['statistics']:
                        stats = analysis['statistics'][col]
                        def fmt(v):
                            return f"{v:.2f}" if v is not None else 'N/A'
                        lines.append(f"| {col} | {fmt(stats.get('mean'))} | {fmt(stats.get('std'))} | {fmt(stats.get('min'))} | {fmt(stats.get('max'))} | {fmt(stats.get('median'))} |")
                lines.append("")

            lines.append("#### Sample Data (First 3 Rows)")
            lines.append("")
            if analysis['sample_data']:
                if isinstance(analysis['sample_data'][0], dict):
                    headers = list(analysis['sample_data'][0].keys())
                    lines.append("| " + " | ".join(headers) + " |")
                    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
                    for row in analysis['sample_data']:
                        lines.append("| " + " | ".join(str(row.get(h, ''))[:50] for h in headers) + " |")
                else:
                    for i, row in enumerate(analysis['sample_data']):
                        lines.append(f"**Row {i+1}:** {row}")
            lines.append("")
            lines.append("---")
            lines.append("")

        # Non-CSV Analysis
        lines.append("## Non-CSV File Analysis")
        lines.append("")

        for rel_path, analysis in self.results['non_csv_analysis'].items():
            lines.append(f"### `{rel_path}`")
            lines.append("")
            if 'error' in analysis:
                lines.append(f"**Error:** {analysis['error']}")
                lines.append("")
                continue

            lines.append(f"- **Extension:** {analysis['extension']}")
            lines.append(f"- **Size:** {analysis['file_size_kb']} KB ({analysis['file_size_bytes']:,} bytes)")
            lines.append(f"- **MIME Type:** {analysis['mime_type'] or 'unknown'}")
            if analysis['magic_type']:
                lines.append(f"- **Magic Type:** {analysis['magic_type']}")
            lines.append(f"- **Encoding:** {analysis['encoding']}")
            lines.append(f"- **Lines:** {analysis['line_count']:,}")
            lines.append(f"- **Characters:** {analysis['char_count']:,}")
            lines.append(f"- **Words:** {analysis['word_count']:,}")
            lines.append(f"- **MD5:** `{analysis['hashes']['md5']}`")
            lines.append(f"- **SHA256:** `{analysis['hashes']['sha256']}`")
            lines.append("")

            # Type-specific analysis
            if analysis.get('code_analysis'):
                ca = analysis['code_analysis']
                lines.append("#### Code Structure Analysis")
                lines.append("")
                if ca.get('imports'):
                    lines.append(f"- **Imports ({len(ca['imports'])}):** {', '.join(ca['imports'][:10])}{'...' if len(ca['imports']) > 10 else ''}")
                if ca.get('classes'):
                    lines.append(f"- **Classes ({len(ca['classes'])}):** {', '.join(ca['classes'][:10])}{'...' if len(ca['classes']) > 10 else ''}")
                if ca.get('functions'):
                    lines.append(f"- **Functions ({len(ca['functions'])}):** {', '.join(ca['functions'][:10])}{'...' if len(ca['functions']) > 10 else ''}")
                if ca.get('async_functions'):
                    if isinstance(ca['async_functions'], list):
                        lines.append(f"- **Async Functions ({len(ca['async_functions'])}):** {', '.join(ca['async_functions'][:5])}")
                    else:
                        lines.append(f"- **Async Functions:** {ca['async_functions']}")
                if ca.get('constants'):
                    lines.append(f"- **Constants ({len(ca['constants'])}):** {', '.join(ca['constants'][:10])}")
                if 'complexity_indicators' in ca:
                    ci = ca['complexity_indicators']
                    lines.append(f"- **Complexity:** {ci.get('total_lines', 0)} lines, {ci.get('import_count', 0)} imports, {ci.get('class_count', 0)} classes, {ci.get('function_count', 0)} functions")
                lines.append("")

            if analysis.get('markdown_analysis'):
                ma = analysis['markdown_analysis']
                lines.append("#### Markdown Structure")
                lines.append("")
                lines.append(f"- **Headers:** {len(ma['headers'])} (H1: {ma['header_counts'].get(1, 0)}, H2: {ma['header_counts'].get(2, 0)}, H3: {ma['header_counts'].get(3, 0)})")
                lines.append(f"- **Links:** {len(ma['links'])}")
                lines.append(f"- **Images:** {len(ma['images'])}")
                lines.append(f"- **Code Blocks:** {len(ma['code_blocks'])}")
                lines.append(f"- **Tables:** {ma['tables']}")
                lines.append(f"- **Lists:** {ma['lists']}")
                lines.append(f"- **Word Count:** {ma['word_count']:,}")
                if ma['headers']:
                    lines.append("")
                    lines.append("**Table of Contents:**")
                    for h in ma['headers'][:20]:
                        lines.append(f"{'  ' * (h['level'] - 1)}- {h['text']}")
                lines.append("")

            if analysis.get('json_analysis'):
                ja = analysis['json_analysis']
                lines.append("#### JSON Structure")
                lines.append("")
                lines.append(f"- **Valid:** {ja.get('valid', False)}")
                if ja.get('valid'):
                    lines.append(f"- **Root Type:** {ja['root_type']}")
                    lines.append(f"- **Total Keys:** {ja['key_count']}")
                    lines.append(f"- **Max Depth:** {ja['depth']}")
                    lines.append(f"- **Arrays:** {len(ja['arrays'])}")
                    lines.append(f"- **Nested Objects:** {ja['nested_objects']}")
                    if ja['keys']:
                        lines.append(f"- **Sample Keys:** {', '.join(ja['keys'][:15])}{'...' if len(ja['keys']) > 15 else ''}")
                lines.append("")

            if analysis.get('html_analysis'):
                ha = analysis['html_analysis']
                lines.append("#### HTML Structure")
                lines.append("")
                lines.append(f"- **Doctype:** {ha['doctype']}")
                lines.append(f"- **Forms:** {ha['forms']}")
                lines.append(f"- **Inputs:** {ha['inputs']}")
                lines.append(f"- **Links:** {ha['links']}")
                if ha['tags']:
                    lines.append(f"- **Top Tags:** {', '.join([f'{t}({c})' for t, c in ha['tags'].most_common(10)])}")
                if ha['scripts']:
                    lines.append(f"- **Scripts:** {', '.join(ha['scripts'][:5])}")
                if ha['stylesheets']:
                    lines.append(f"- **Stylesheets:** {', '.join(ha['stylesheets'][:5])}")
                lines.append("")

            if analysis.get('config_analysis'):
                ca = analysis['config_analysis']
                lines.append("#### Config Structure")
                lines.append("")
                lines.append(f"- **Sections:** {', '.join(ca['sections']) if ca['sections'] else '—'}")
                lines.append(f"- **Key-Value Pairs:** {ca['key_value_pairs']}")
                lines.append(f"- **Comments:** {ca['comments']}")
                lines.append("")

            if analysis.get('structure'):
                sa = analysis['structure']
                lines.append("#### XML/SVG Structure")
                lines.append("")
                lines.append(f"- **Root Element:** {sa.get('root_element', 'unknown')}")
                if sa.get('elements'):
                    lines.append(f"- **Elements:** {', '.join([f'{e}({c})' for e, c in sa['elements'].most_common(10)])}")
                if sa.get('namespaces'):
                    ns_list = [f'{n["prefix"]}: {n["uri"]}' for n in sa['namespaces']]
                    lines.append(f"- **Namespaces:** {', '.join(ns_list)}")
                lines.append("")

            # Extracted data
            if analysis.get('extracted_data'):
                ed = analysis['extracted_data']
                lines.append("#### Extracted Data Patterns")
                lines.append("")
                for key, values in ed.items():
                    if values:
                        lines.append(f"- **{key.replace('_', ' ').title()} ({len(values)}):** {', '.join(values[:10])}{'...' if len(values) > 10 else ''}")
                lines.append("")

            # Content summary
            if analysis.get('content_summary'):
                cs = analysis['content_summary']
                lines.append("#### Content Summary")
                lines.append("")
                lines.append(f"- **Total Lines:** {cs['total_lines']:,}")
                lines.append(f"- **Non-Empty Lines:** {cs['non_empty_lines']:,}")
                lines.append(f"- **Empty Line Ratio:** {cs['empty_line_ratio']:.2%}")
                lines.append(f"- **Avg Line Length:** {cs['avg_line_length']:.1f} chars")
                lines.append(f"- **Max Line Length:** {cs['max_line_length']} chars")
                lines.append("")

            lines.append("---")
            lines.append("")

        return '\n'.join(lines)


def main():
    root_dir = r"C:\Users\NITHING\Desktop\projections"
    output_file = r"C:\Users\NITHING\Desktop\projections\DATA_ANALYSIS_REPORT_GENERATED.md"

    print(f"Analyzing files in: {root_dir}")
    analyzer = DataFileAnalyzer(root_dir)

    print("Discovering files...")
    analyzer.find_all_files()
    print(f"Found {len(analyzer.csv_files)} CSV files and {len(analyzer.non_csv_files)} non-CSV files")

    print("Analyzing CSV files...")
    analyzer.analyze_csv_files()

    print("Analyzing non-CSV files...")
    analyzer.analyze_non_csv_files()

    print("Generating summary...")
    analyzer.generate_summary()

    print(f"Writing report to: {output_file}")
    analyzer.write_markdown_report(output_file)

    print("Analysis complete!")


if __name__ == "__main__":
    main()