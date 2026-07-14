import csv
from collections import defaultdict

def load_csv_safe(filepath):
    """Load CSV, handling extra columns"""
    records = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Filter out None keys and list values
            clean_row = {}
            for k, v in row.items():
                if k is not None and not isinstance(v, list):
                    clean_row[k] = v
            records.append(clean_row)
    return records

focused = load_csv_safe('hyperscaler_focused_projects.csv')
key = load_csv_safe('key_hyperscale_projects.csv')

print(f"Loaded {len(focused)} from hyperscaler_focused_projects.csv")
print(f"Loaded {len(key)} from key_hyperscale_projects.csv")

# Merge by facility_name + operator + state + country
def make_key(row):
    name = (row.get('facility_name') or '').strip().lower()
    op = (row.get('operator') or '').strip().lower()
    state = (row.get('state_province') or '').strip().lower()
    country = (row.get('country') or '').strip().lower()
    return f"{name}|{op}|{state}|{country}"

merged = {}

for row in focused + key:
    k = make_key(row)
    if k not in merged:
        merged[k] = dict(row)
    else:
        existing = merged[k]
        for field, value in row.items():
            if value and str(value).strip() and (not existing.get(field) or not str(existing.get(field)).strip()):
                existing[field] = value

print(f"After dedup: {len(merged)} unique facilities")

# Create master list with facility IDs
facilities = []
facility_id = 1

for k, row in merged.items():
    operator = str(row.get('operator') or '').strip()
    tenant = str(row.get('tenant') or '').strip()
    hyperscaler_cat = str(row.get('hyperscaler_category') or '').strip()
    
    # Auto-classify if not set
    if not hyperscaler_cat or hyperscaler_cat == 'Other/Unclassified':
        name = str(row.get('facility_name') or '').strip().lower()
        op_lower = operator.lower()
        ten_lower = tenant.lower()
        
        hyperscalers = {
            'Meta': ['meta', 'facebook'],
            'AWS': ['amazon', 'aws'],
            'Google': ['google', 'gcp', 'google cloud'],
            'Microsoft': ['microsoft', 'azure'],
            'Oracle': ['oracle'],
            'Apple': ['apple'],
            'CoreWeave': ['coreweave'],
            'Lambda Labs': ['lambda labs', 'lambda'],
            'Crusoe': ['crusoe'],
            'Applied Digital': ['applied digital'],
            'Stargate': ['stargate', 'openai', 'softbank', 'mgx'],
            'Equinix': ['equinix'],
            'Digital Realty': ['digital realty'],
            'Vantage': ['vantage'],
            'QTS': ['qts'],
            'CyrusOne': ['cyrusone'],
            'Stream Data Centers': ['stream data centers', 'stream dc'],
            'Aligned': ['aligned'],
            'Prime Data Centers': ['prime data centers'],
            'NTT': ['ntt'],
            'EdgeCore': ['edgecore', 'edge core'],
            'Cerebras': ['cerebras'],
            'xAI': ['xai'],
            'Nebius': ['nebius'],
        }
        
        for cat, keywords in hyperscalers.items():
            for kw in keywords:
                if kw in op_lower or kw in ten_lower or kw in name:
                    hyperscaler_cat = cat
                    break
            if hyperscaler_cat:
                break
    
    if not hyperscaler_cat:
        hyperscaler_cat = 'Other/Unclassified'
    
    # Status mapping
    status = str(row.get('status') or '').strip()
    status_map = {
        'Operating': 'Operating',
        'Approved/Permitted/Under construction': 'Under Construction',
        'Under Construction': 'Under Construction',
        'Planned': 'Planned',
        'Proposed': 'Planned',
        'Expanding': 'Expanding',
        'Suspended': 'Suspended',
        'Cancelled': 'Cancelled',
        'Reference': 'Reference',
        'Pre-proposal': 'Pre-proposal',
    }
    norm_status = status_map.get(status, status)
    
    # Parse capacity MW
    mw_str = str(row.get('capacity_mw') or '').strip()
    capacity_mw = None
    if mw_str:
        if '-' in mw_str:
            parts = mw_str.split('-')
            try:
                capacity_mw = (int(parts[0].replace(',','')) + int(parts[1].replace(',',''))) // 2
            except:
                capacity_mw = None
        else:
            try:
                capacity_mw = int(mw_str.replace(',',''))
            except:
                capacity_mw = None
    
    # Parse project cost
    cost_str = str(row.get('project_cost_usd') or '').strip()
    project_cost_usd = None
    if cost_str:
        cost_str = cost_str.replace('$', '').replace(',', '').strip().lower()
        if 'billion' in cost_str:
            try:
                project_cost_usd = float(cost_str.replace('billion', '').strip()) * 1e9
            except:
                pass
        elif 'million' in cost_str:
            try:
                project_cost_usd = float(cost_str.replace('million', '').strip()) * 1e6
            except:
                pass
    
    facility = {
        'facility_id': f"DC-{facility_id:05d}",
        'facility_name': str(row.get('facility_name') or '').strip(),
        'operator': operator,
        'tenant': tenant,
        'hyperscaler_category': hyperscaler_cat,
        'city': str(row.get('city') or '').strip(),
        'state_province': str(row.get('state_province') or '').strip(),
        'country': str(row.get('country') or '').strip(),
        'status': norm_status,
        'capacity_mw': capacity_mw,
        'capacity_category': str(row.get('capacity_category') or '').strip(),
        'expected_online_date': str(row.get('expected_online_date') or '').strip(),
        'project_cost_usd': project_cost_usd,
        'cooling_type': str(row.get('cooling_type') or '').strip(),
        'power_source': str(row.get('power_source') or '').strip(),
        'purpose': str(row.get('purpose') or '').strip(),
        'source_url': str(row.get('source_url') or '').strip(),
        'notes': str(row.get('notes') or '').strip(),
        'tier': 'Tier 1' if (capacity_mw and capacity_mw >= 500) else ('Tier 2' if (capacity_mw and capacity_mw >= 100) else 'Tier 3'),
    }
    facilities.append(facility)
    facility_id += 1

# Sort by tier, then capacity desc
facilities.sort(key=lambda x: (x['tier'] != 'Tier 1', x['tier'] != 'Tier 2', -(x['capacity_mw'] or 0)))

# Write master facility list
output_fields = [
    'facility_id', 'facility_name', 'operator', 'tenant', 'hyperscaler_category',
    'city', 'state_province', 'country', 'status', 'capacity_mw', 'capacity_category',
    'expected_online_date', 'project_cost_usd', 'cooling_type', 'power_source',
    'purpose', 'source_url', 'notes', 'tier'
]

with open('master_facility_list.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=output_fields)
    writer.writeheader()
    writer.writerows(facilities)

print(f"\nWritten {len(facilities)} facilities to master_facility_list.csv")

# Summary by tier
for tier in ['Tier 1', 'Tier 2', 'Tier 3']:
    count = sum(1 for f in facilities if f['tier'] == tier)
    total_mw = sum(f['capacity_mw'] or 0 for f in facilities if f['tier'] == tier)
    print(f"  {tier}: {count} facilities, {total_mw:,} MW")

# By hyperscaler category
print("\nBy Hyperscaler Category:")
cats = defaultdict(lambda: {'count': 0, 'mw': 0})
for f in facilities:
    cats[f['hyperscaler_category']]['count'] += 1
    cats[f['hyperscaler_category']]['mw'] += f['capacity_mw'] or 0

for cat, data in sorted(cats.items(), key=lambda x: -x[1]['mw']):
    print(f"  {cat}: {data['count']} facilities, {data['mw']:,} MW")

# By status
print("\nBy Status:")
status_counts = defaultdict(int)
for f in facilities:
    status_counts[f['status']] += 1
for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
    print(f"  {status}: {count}")

# By country
print("\nBy Country:")
country_counts = defaultdict(int)
for f in facilities:
    country_counts[f['country']] += 1
for country, count in sorted(country_counts.items(), key=lambda x: -x[1]):
    print(f"  {country}: {count}")