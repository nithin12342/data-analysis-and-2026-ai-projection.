import csv
from collections import defaultdict

# Load the master list
facilities = []
with open('master_facility_list.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        facilities.append(row)

print(f"Loaded {len(facilities)} facilities")

# Deduplicate by facility name + operator
def make_dedup_key(f):
    return (f['facility_name'].strip().lower(), f['operator'].strip().lower())

unique = {}
for f in facilities:
    k = make_dedup_key(f)
    if k not in unique:
        unique[k] = f
    else:
        # Merge non-empty fields
        existing = unique[k]
        for key, val in f.items():
            if val and val.strip() and (not existing.get(key) or not existing[key].strip()):
                existing[key] = val

print(f"After dedup: {len(unique)} unique facilities")

# Enhanced hyperscaler classification
def classify_hyperscaler(f):
    name = f['facility_name'].strip().lower()
    operator = f['operator'].strip().lower()
    tenant = f['tenant'].strip().lower()
    purpose = f['purpose'].strip().lower()
    
    # Known AI/Hyperscale developers and their likely customers
    ai_developers = {
        'Meta': ['meta', 'facebook'],
        'AWS': ['amazon', 'aws'],
        'Google': ['google', 'gcp', 'google cloud', 'groot'],
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
        'Stream Data Centers': ['stream data centers', 'stream dc', 'stream data'],
        'Aligned': ['aligned'],
        'Prime Data Centers': ['prime data centers', 'prime data'],
        'NTT': ['ntt'],
        'EdgeCore': ['edgecore', 'edge core'],
        'Cerebras': ['cerebras'],
        'xAI': ['xai'],
        'Nebius': ['nebius'],
        # AI-focused developers/operators
        'Nscale': ['nscale'],
        'Bitzero': ['bitzero'],
        'Pacifico Energy': ['pacifico energy'],
        'New Era Energy': ['new era energy', 'new era digital'],
        'Energy Abundance': ['energy abundance'],
        'Sailfish Digital': ['sailfish digital', 'sailfish'],
        'GridFree AI': ['gridfree ai', 'gridfree'],
        'Fermi America': ['fermi america', 'fermi'],
        'Homer City Redevelopment': ['homer city'],
        'Joule Capital': ['joule capital'],
        'STAK Energy': ['stak energy'],
        'Vermaland': ['vermaland'],
        'Tract': ['tract data centers', 'tract'],
        'Beale Infrastructure': ['beale infrastructure'],
        'Compass Data Centers': ['compass data centers', 'compass'],
        'AVAIO Digital': ['avaio digital', 'avaio'],
        'Serverfarm': ['serverfarm'],
        'Northpoint Development': ['northpoint development'],
        'Fortescue': ['fortescue'],
        'Menlo Digital': ['menlo digital', 'menlo equities'],
        'H5 Data Centers': ['h5 data centers'],
        'Expedient': ['expedient'],
        'Sabey': ['sabey'],
        'Cyxtera': ['cyxtera'],
        'CoreSite': ['coresite'],
        'EdgeConneX': ['edgeconnex', 'edge connex'],
        'Colovore': ['colovore'],
        'IREN': ['iren'],
        'Riot Platforms': ['riot platforms', 'riot'],
        'Hut 8': ['hut 8'],
        'Core Scientific': ['core scientific'],
        'TeraWulf': ['terawulf'],
        'Greenidge': ['greenidge'],
        'Clean Cloud Energy': ['clean cloud energy'],
        'Logistic Land Investments': ['logistic land investments'],
        'Beacon': ['beacon data centers', 'beacon'],
        'ForgeLight Ventures': ['forgelight ventures', 'forgelight'],
        'DigitalBridge': ['digitalbridge', 'digital bridge'],
        'KKR': ['kkr'],
        'Blackstone': ['blackstone'],
        'Brookfield': ['brookfield'],
        'Macquarie': ['macquarie'],
    }
    
    # Also check for known hyperscaler tenants in purpose/notes
    all_text = f"{name} {operator} {tenant} {purpose}".lower()
    
    for cat, keywords in ai_developers.items():
        for kw in keywords:
            if kw in all_text:
                return cat
    
    return 'Other/Unclassified'

# Re-classify and assign tiers based on capacity
for f in unique.values():
    f['hyperscaler_category'] = classify_hyperscaler(f)
    cap = f['capacity_mw']
    if cap:
        try:
            cap_int = int(cap)
            if cap_int >= 500:
                f['tier'] = 'Tier 1'
            elif cap_int >= 100:
                f['tier'] = 'Tier 2'
            else:
                f['tier'] = 'Tier 3'
        except:
            f['tier'] = 'Tier 3'
    else:
        f['tier'] = 'Tier 3'

# Also add latitude/longitude from FracTracker data if available
# Let's load FracTracker for lat/long
fractracker = {}
with open('fractracker_us_datacenters.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row.get('facility_name', '').strip().lower()
        lat = row.get('lat', '').strip()
        lon = row.get('long', '').strip()
        if name and lat and lon:
            fractracker[name] = (lat, lon)

matched = 0
for f in unique.values():
    name = f['facility_name'].strip().lower()
    if name in fractracker:
        f['latitude'], f['longitude'] = fractracker[name]
        matched += 1

print(f"Matched {matched} facilities with FracTracker coordinates")

# Write enhanced master list
output_fields = [
    'facility_id', 'facility_name', 'operator', 'tenant', 'hyperscaler_category',
    'city', 'state_province', 'country', 'latitude', 'longitude',
    'status', 'capacity_mw', 'capacity_category', 'expected_online_date',
    'project_cost_usd', 'cooling_type', 'power_source', 'purpose',
    'source_url', 'notes', 'tier'
]

# Re-sort and re-ID
facilities_list = list(unique.values())
facilities_list.sort(key=lambda x: (x['tier'] != 'Tier 1', x['tier'] != 'Tier 2', -(int(x['capacity_mw']) if x['capacity_mw'] and str(x['capacity_mw']).isdigit() else 0)))

for i, f in enumerate(facilities_list, 1):
    f['facility_id'] = f"DC-{i:05d}"

with open('master_facility_list_v2.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=output_fields)
    writer.writeheader()
    writer.writerows(facilities_list)

print(f"\nWritten {len(facilities_list)} facilities to master_facility_list_v2.csv")

# Summary
for tier in ['Tier 1', 'Tier 2', 'Tier 3']:
    tier_facilities = [f for f in facilities_list if f['tier'] == tier]
    count = len(tier_facilities)
    total_mw = sum(int(f['capacity_mw']) for f in tier_facilities if f['capacity_mw'] and str(f['capacity_mw']).isdigit())
    print(f"  {tier}: {count} facilities, {total_mw:,} MW")

print("\nBy Hyperscaler Category:")
cats = defaultdict(lambda: {'count': 0, 'mw': 0})
for f in facilities_list:
    cats[f['hyperscaler_category']]['count'] += 1
    if f['capacity_mw'] and str(f['capacity_mw']).isdigit():
        cats[f['hyperscaler_category']]['mw'] += int(f['capacity_mw'])

for cat, data in sorted(cats.items(), key=lambda x: -x[1]['mw']):
    print(f"  {cat}: {data['count']} facilities, {data['mw']:,} MW")

print("\nBy Status:")
status_counts = defaultdict(int)
for f in facilities_list:
    status_counts[f['status']] += 1
for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
    print(f"  {status}: {count}")

print("\nBy Country:")
country_counts = defaultdict(int)
for f in facilities_list:
    country_counts[f['country']] += 1
for country, count in sorted(country_counts.items(), key=lambda x: -x[1]):
    print(f"  {country}: {count}")

# Check for facilities with coordinates
with_coords = sum(1 for f in facilities_list if f.get('latitude') and f.get('longitude'))
print(f"\nFacilities with coordinates: {with_coords}/{len(facilities_list)}")

# Save as JSON too for easy programmatic access
import json
with open('master_facility_list_v2.json', 'w', encoding='utf-8') as f:
    json.dump(facilities_list, f, indent=2, ensure_ascii=False)

print("\nAlso saved as JSON: master_facility_list_v2.json")