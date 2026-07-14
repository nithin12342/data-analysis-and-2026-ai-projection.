#!/usr/bin/env python3
"""
Create comprehensive master CSV of global data centers from multiple sources:
1. GitHub Global-Data-Center-Map (18,110 facilities, 116 countries)
2. FracTracker US Data Centers Tracker (1,400+ US sites with pipeline status)
3. DCMap.us US Pipeline (1,063 facilities, 250,993 MW)
4. DataCenterMap.info stats (11,873 facilities, 179 countries)
"""

import csv
import json
from datetime import datetime
from collections import defaultdict

def load_github_global(filepath):
    """Load GitHub global data centers CSV"""
    records = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append({
                'source': 'GitHub_GlobalMap',
                'facility_name': row.get('name', '').strip(),
                'operator': row.get('company', '').strip(),
                'city': row.get('city', '').strip(),
                'state_province': row.get('state', '').strip(),
                'country': row.get('country', '').strip(),
                'address': row.get('address', '').strip(),
                'status': 'Operating',  # GitHub data appears to be operating facilities
                'capacity_mw': '',
                'capacity_category': '',
                'facility_size_sqft': '',
                'property_size_acres': '',
                'project_cost_usd': '',
                'expected_online_date': '',
                'latitude': '',
                'longitude': '',
                'cooling_type': '',
                'power_source': '',
                'tenant': '',
                'purpose': '',
                'community_pushback': '',
                'notes': '',
                'source_url': '',
                'date_added': '',
                'last_updated': ''
            })
    return records

def load_fractracker_us(filepath):
    """Load FracTracker US data centers CSV"""
    records = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Parse status
            status = row.get('status', '').strip()
            status_map = {
                'Operating': 'Operating',
                'Proposed': 'Planned',
                'Approved/Permitted/Under construction': 'Under Construction',
                'Approved': 'Under Construction',
                'Under construction': 'Under Construction',
                'Expanding': 'Expanding',
                'Suspended': 'Suspended',
                'Cancelled': 'Cancelled'
            }
            mapped_status = status_map.get(status, status)
            
            # Parse MW
            mw_str = row.get('mw', '').strip()
            capacity_mw = mw_str if mw_str else ''
            
            # Parse size rank
            size_rank = row.get('sizerank', '').strip()
            
            records.append({
                'source': 'FracTracker_US',
                'facility_name': row.get('facility_name', '').strip(),
                'operator': row.get('operator_name', '').strip(),
                'city': row.get('city', '').strip(),
                'state_province': row.get('state', '').strip(),
                'country': 'United States',
                'address': row.get('address', '').strip(),
                'status': mapped_status,
                'capacity_mw': capacity_mw,
                'capacity_category': size_rank,
                'facility_size_sqft': row.get('facility_size_sqft', '').strip(),
                'property_size_acres': row.get('property_size_acres', '').strip(),
                'project_cost_usd': row.get('project_cost', '').strip(),
                'expected_online_date': row.get('expected_date_online', '').strip(),
                'latitude': row.get('lat', '').strip(),
                'longitude': row.get('long', '').strip(),
                'cooling_type': row.get('cooling_type', '').strip(),
                'power_source': row.get('power_source', '').strip(),
                'tenant': row.get('tenant', '').strip(),
                'purpose': row.get('purpose', '').strip(),
                'community_pushback': row.get('community_pushback', '').strip(),
                'notes': row.get('other_info', '').strip(),
                'source_url': row.get('info_source_1', '').strip(),
                'date_added': row.get('date_created', '').strip(),
                'last_updated': row.get('date_updated', '').strip()
            })
    return records

def load_dcmap_pipeline():
    """Add DCMap.us pipeline summary data as reference"""
    # Major pipeline projects from DCMap.us
    pipeline_projects = [
        {'facility_name': 'Stratos Hyperscale Campus', 'operator': 'Bitzero Blockchain Inc.', 'state_province': 'Utah', 'country': 'United States', 'capacity_mw': '9000', 'status': 'Planned', 'source': 'DCMap_Pipeline'},
        {'facility_name': 'Monarch Compute Campus', 'operator': 'Nscale Ltd.', 'state_province': 'West Virginia', 'country': 'United States', 'capacity_mw': '8000', 'status': 'Planned', 'target_year': '2027', 'source': 'DCMap_Pipeline'},
        {'facility_name': 'GW Ranch', 'operator': 'Pacifico Energy', 'state_province': 'Texas', 'country': 'United States', 'capacity_mw': '7650', 'status': 'Planned', 'target_year': '2027', 'source': 'DCMap_Pipeline'},
        {'facility_name': 'New Era Lea Data Center', 'operator': 'New Era Energy & Digital', 'state_province': 'New Mexico', 'country': 'United States', 'capacity_mw': '7000', 'status': 'Planned', 'target_year': '2028', 'source': 'DCMap_Pipeline'},
        {'facility_name': 'Meta Hyperion Campus', 'operator': 'Meta', 'state_province': 'Louisiana', 'country': 'United States', 'capacity_mw': '5000', 'status': 'Under Construction', 'target_year': '2026', 'source': 'DCMap_Pipeline'},
        {'facility_name': 'Data City Texas', 'operator': 'Energy Abundance', 'state_province': 'Texas', 'country': 'United States', 'capacity_mw': '5000', 'status': 'Planned', 'target_year': '2026', 'source': 'DCMap_Pipeline'},
        {'facility_name': 'Sailfish Comanche Circle', 'operator': 'Sailfish Digital Ventures', 'state_province': 'Texas', 'country': 'United States', 'capacity_mw': '5000', 'status': 'Planned', 'target_year': '2028', 'source': 'DCMap_Pipeline'},
        {'facility_name': 'GridFree AI South Dallas One', 'operator': 'GridFree AI', 'state_province': 'Texas', 'country': 'United States', 'capacity_mw': '5000', 'status': 'Planned', 'target_year': '2026', 'source': 'DCMap_Pipeline'},
        {'facility_name': 'Fermi Phase 3 (SMR/Expansion)', 'operator': 'Fermi America', 'state_province': 'Texas', 'country': 'United States', 'capacity_mw': '4600', 'status': 'Planned', 'target_year': '2036', 'source': 'DCMap_Pipeline'},
        {'facility_name': 'Homer City Energy Campus', 'operator': 'Homer City Redevelopment', 'state_province': 'Pennsylvania', 'country': 'United States', 'capacity_mw': '4500', 'status': 'Planned', 'target_year': '2027', 'source': 'DCMap_Pipeline'},
        {'facility_name': 'Fermi Phase 2 (Nuclear)', 'operator': 'Fermi America', 'state_province': 'Texas', 'country': 'United States', 'capacity_mw': '4400', 'status': 'Planned', 'target_year': '2032', 'source': 'DCMap_Pipeline'},
        {'facility_name': 'High Performance Compute Campus', 'operator': 'Joule Capital Partners', 'state_province': 'Utah', 'country': 'United States', 'capacity_mw': '4000', 'status': 'Planned', 'target_year': '2026', 'source': 'DCMap_Pipeline'},
        {'facility_name': 'STAK Energy North Slopes', 'operator': 'STAK Energy', 'state_province': 'Alaska', 'country': 'United States', 'capacity_mw': '3000', 'status': 'Planned', 'source': 'DCMap_Pipeline'},
        {'facility_name': 'Vermaland La Osa Campus', 'operator': 'Vermaland', 'state_province': 'Arizona', 'country': 'United States', 'capacity_mw': '3000', 'status': 'Planned', 'source': 'DCMap_Pipeline'},
        {'facility_name': 'North Creek Tech Campus', 'operator': 'Amazon', 'state_province': 'Virginia', 'country': 'United States', 'capacity_mw': '2700', 'status': 'Planned', 'source': 'DCMap_Pipeline'},
    ]
    
    records = []
    for p in pipeline_projects:
        records.append({
            'source': p['source'],
            'facility_name': p['facility_name'],
            'operator': p['operator'],
            'city': '',
            'state_province': p['state_province'],
            'country': p['country'],
            'address': '',
            'status': p['status'],
            'capacity_mw': p['capacity_mw'],
            'capacity_category': 'Mega campus (>1,000 MW)' if int(p['capacity_mw']) > 1000 else 'Hyperscale (100-999 MW)',
            'facility_size_sqft': '',
            'property_size_acres': '',
            'project_cost_usd': '',
            'expected_online_date': p.get('target_year', ''),
            'latitude': '',
            'longitude': '',
            'cooling_type': '',
            'power_source': '',
            'tenant': '',
            'purpose': 'AI/Hyperscale',
            'community_pushback': '',
            'notes': f"DCMap.us pipeline project, target: {p.get('target_year', 'TBD')}",
            'source_url': 'https://dcmap.us/insights/pipeline/',
            'date_added': '',
            'last_updated': '2026-07-14'
        })
    return records

def add_datacentermap_country_stats():
    """Add DataCenterMap.info country-level statistics as reference rows"""
    stats = [
        {'country': 'United States', 'total_facilities': 4497, 'source': 'DataCenterMap'},
        {'country': 'Germany', 'total_facilities': 527, 'source': 'DataCenterMap'},
        {'country': 'United Kingdom', 'total_facilities': 561, 'source': 'DataCenterMap'},
        {'country': 'China', 'total_facilities': 369, 'source': 'DataCenterMap'},
        {'country': 'France', 'total_facilities': 393, 'source': 'DataCenterMap'},
        {'country': 'Canada', 'total_facilities': 289, 'source': 'DataCenterMap'},
        {'country': 'Australia', 'total_facilities': 286, 'source': 'DataCenterMap'},
        {'country': 'Japan', 'total_facilities': 259, 'source': 'DataCenterMap'},
        {'country': 'Italy', 'total_facilities': 260, 'source': 'DataCenterMap'},
        {'country': 'India', 'total_facilities': 298, 'source': 'DataCenterMap'},
        {'country': 'Netherlands', 'total_facilities': 186, 'source': 'DataCenterMap'},
        {'country': 'Brazil', 'total_facilities': 215, 'source': 'DataCenterMap'},
        {'country': 'Spain', 'total_facilities': 212, 'source': 'DataCenterMap'},
        {'country': 'Russia', 'total_facilities': 188, 'source': 'DataCenterMap'},
        {'country': 'Singapore', 'total_facilities': 68, 'source': 'DataCenterMap'},
    ]
    
    records = []
    for s in stats:
        records.append({
            'source': s['source'],
            'facility_name': f"[COUNTRY STAT] {s['country']}",
            'operator': '',
            'city': '',
            'state_province': '',
            'country': s['country'],
            'address': '',
            'status': 'Reference',
            'capacity_mw': '',
            'capacity_category': f"Total facilities: {s['total_facilities']}",
            'facility_size_sqft': '',
            'property_size_acres': '',
            'project_cost_usd': '',
            'expected_online_date': '',
            'latitude': '',
            'longitude': '',
            'cooling_type': '',
            'power_source': '',
            'tenant': '',
            'purpose': 'Country-level aggregate',
            'community_pushback': '',
            'notes': f"DataCenterMap.info reports {s['total_facilities']} facilities in {s['country']}",
            'source_url': 'https://www.datacentermap.com/datacenters/',
            'date_added': '',
            'last_updated': '2026-07-14'
        })
    return records

def normalize_state(state, country):
    """Normalize state/province names"""
    if not state:
        return ''
    state = state.strip()
    # US state abbreviations to full names
    us_states = {
        'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas',
        'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware',
        'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho',
        'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas',
        'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
        'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi',
        'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada',
        'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York',
        'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma',
        'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
        'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
        'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia',
        'WI': 'Wisconsin', 'WY': 'Wyoming', 'DC': 'District of Columbia'
    }
    if country == 'United States' and state.upper() in us_states:
        return us_states[state.upper()]
    return state

def deduplicate_records(records):
    """Remove duplicates based on facility name + operator + location"""
    seen = set()
    unique = []
    for r in records:
        key = (
            r['facility_name'].lower().strip(),
            r['operator'].lower().strip(),
            r['city'].lower().strip(),
            r['state_province'].lower().strip(),
            r['country'].lower().strip()
        )
        if key not in seen and r['facility_name']:
            seen.add(key)
            unique.append(r)
    return unique

def main():
    print("Loading GitHub Global Data Centers...")
    github_records = load_github_global('global_datacenters_github.csv')
    print(f"  Loaded {len(github_records)} records")
    
    print("Loading FracTracker US Data Centers...")
    fractracker_records = load_fractracker_us('fractracker_us_datacenters.csv')
    print(f"  Loaded {len(fractracker_records)} records")
    
    print("Loading DCMap.us Pipeline Projects...")
    dcmap_records = load_dcmap_pipeline()
    print(f"  Loaded {len(dcmap_records)} records")
    
    print("Adding DataCenterMap Country Stats...")
    dcmap_stats = add_datacentermap_country_stats()
    print(f"  Added {len(dcmap_stats)} country stats")
    
    # Combine all records
    all_records = github_records + fractracker_records + dcmap_records + dcmap_stats
    
    # Normalize states
    for r in all_records:
        r['state_province'] = normalize_state(r['state_province'], r['country'])
    
    # Deduplicate
    print("Deduplicating...")
    all_records = deduplicate_records(all_records)
    print(f"  {len(all_records)} unique records after deduplication")
    
    # Write master CSV
    fieldnames = [
        'source', 'facility_name', 'operator', 'city', 'state_province', 'country',
        'address', 'status', 'capacity_mw', 'capacity_category', 'facility_size_sqft',
        'property_size_acres', 'project_cost_usd', 'expected_online_date',
        'latitude', 'longitude', 'cooling_type', 'power_source', 'tenant',
        'purpose', 'community_pushback', 'notes', 'source_url',
        'date_added', 'last_updated'
    ]
    
    output_file = 'master_global_datacenters.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_records)
    
    print(f"\nMaster CSV written to: {output_file}")
    print(f"Total records: {len(all_records)}")
    
    # Print summary by source
    source_counts = defaultdict(int)
    status_counts = defaultdict(int)
    country_counts = defaultdict(int)
    
    for r in all_records:
        source_counts[r['source']] += 1
        status_counts[r['status']] += 1
        country_counts[r['country']] += 1
    
    print("\nBy Source:")
    for s, c in sorted(source_counts.items(), key=lambda x: -x[1]):
        print(f"  {s}: {c}")
    
    print("\nBy Status:")
    for s, c in sorted(status_counts.items(), key=lambda x: -x[1]):
        print(f"  {s}: {c}")
    
    print("\nTop 20 Countries:")
    for c, cnt in sorted(country_counts.items(), key=lambda x: -x[1])[:20]:
        print(f"  {c}: {cnt}")

if __name__ == '__main__':
    main()