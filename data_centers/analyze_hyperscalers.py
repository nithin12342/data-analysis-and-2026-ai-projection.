import csv
import json
from collections import defaultdict

# Load the key hyperscale projects
projects = []
with open('key_hyperscale_projects.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        projects.append(row)

# Group by operator/tenant
by_operator = defaultdict(list)
for p in projects:
    op = p.get('operator', '').strip()
    tenant = p.get('tenant', '').strip()
    if op:
        by_operator[op].append(p)
    if tenant and tenant != op:
        by_operator[tenant].append(p)

# Print summary
print("=== HYPERSCALER / AI COMPUTE PROVIDERS ===\n")
for op, projs in sorted(by_operator.items(), key=lambda x: -len(x[1])):
    total_mw = 0
    statuses = defaultdict(int)
    states = set()
    for p in projs:
        statuses[p.get('status', 'Unknown')] += 1
        if p.get('state_province'):
            states.add(p['state_province'])
        mw = p.get('capacity_mw', '')
        if mw and mw.replace('-', '').replace(',', '').isdigit():
            total_mw += int(mw.replace(',', '').split('-')[0])
    print(f"{op}")
    print(f"  Projects: {len(projs)} | Est. MW: {total_mw:,} | States: {len(states)}")
    for s, c in sorted(statuses.items(), key=lambda x: -x[1]):
        print(f"  {s}: {c}")
    print()

# Now create a focused hyperscaler CSV
hyperscalers = {
    'AWS': ['Amazon', 'AWS', 'Amazon Web Services'],
    'Microsoft': ['Microsoft', 'Azure'],
    'Google': ['Google', 'GCP', 'Google Cloud'],
    'Meta': ['Meta', 'Facebook'],
    'Oracle': ['Oracle'],
    'Apple': ['Apple'],
    'CoreWeave': ['CoreWeave'],
    'Lambda Labs': ['Lambda Labs', 'Lambda'],
    'Crusoe': ['Crusoe'],
    'Applied Digital': ['Applied Digital'],
    'Stargate': ['Stargate', 'OpenAI', 'SoftBank', 'MGX'],
    'Equinix': ['Equinix'],
    'Digital Realty': ['Digital Realty'],
    'Vantage': ['Vantage'],
    'QTS': ['QTS'],
    'CyrusOne': ['CyrusOne'],
    'Stream Data Centers': ['Stream Data Centers'],
    'Aligned': ['Aligned'],
    'Prime Data Centers': ['Prime Data Centers'],
    'NTT': ['NTT'],
    'EdgeCore': ['EdgeCore', 'Edgecore'],
    'Cerebras': ['Cerebras'],
    'xAI': ['xAI'],
    'Nebius': ['Nebius'],
}

# Categorize projects
categorized = defaultdict(list)
for p in projects:
    op = p.get('operator', '').strip().lower()
    tenant = p.get('tenant', '').strip().lower()
    facility = p.get('facility_name', '').strip().lower()
    
    assigned = False
    for hyper, keywords in hyperscalers.items():
        for kw in keywords:
            if kw.lower() in op or kw.lower() in tenant or kw.lower() in facility:
                categorized[hyper].append(p)
                assigned = True
                break
        if assigned:
            break
    if not assigned:
        categorized['Other/Unclassified'].append(p)

# Write focused hyperscaler CSV
output_fields = [
    'hyperscaler_category', 'facility_name', 'operator', 'tenant', 
    'city', 'state_province', 'country', 'status', 'capacity_mw', 
    'capacity_category', 'expected_online_date', 'project_cost_usd',
    'cooling_type', 'power_source', 'purpose', 'source_url'
]

with open('hyperscaler_focused_projects.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=output_fields)
    writer.writeheader()
    for hyper, projs in categorized.items():
        for p in projs:
            row = {
                'hyperscaler_category': hyper,
                'facility_name': p.get('facility_name', ''),
                'operator': p.get('operator', ''),
                'tenant': p.get('tenant', ''),
                'city': p.get('city', ''),
                'state_province': p.get('state_province', ''),
                'country': p.get('country', ''),
                'status': p.get('status', ''),
                'capacity_mw': p.get('capacity_mw', ''),
                'capacity_category': p.get('capacity_category', ''),
                'expected_online_date': p.get('expected_online_date', ''),
                'project_cost_usd': p.get('project_cost_usd', ''),
                'cooling_type': p.get('cooling_type', ''),
                'power_source': p.get('power_source', ''),
                'purpose': p.get('purpose', ''),
                'source_url': p.get('source_url', ''),
            }
            writer.writerow(row)

print(f"\nWritten hyperscaler_focused_projects.csv with {len(projects)} total rows")

# Summary by hyperscaler
print("\n=== HYPERSCALER SUMMARY ===")
for hyper, projs in sorted(categorized.items(), key=lambda x: -len(x[1])):
    if hyper == 'Other/Unclassified':
        continue
    total_mw = 0
    statuses = defaultdict(int)
    for p in projs:
        statuses[p.get('status', 'Unknown')] += 1
        mw = p.get('capacity_mw', '')
        if mw and mw.replace('-', '').replace(',', '').isdigit():
            total_mw += int(mw.replace(',', '').split('-')[0])
    print(f"{hyper}: {len(projs)} projects, ~{total_mw:,} MW")
    for s, c in sorted(statuses.items(), key=lambda x: -x[1]):
        print(f"  {s}: {c}")