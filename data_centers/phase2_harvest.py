#!/usr/bin/env python3
"""
Phase 2: Automated Data Harvesting from Public Sources

Sources:
1. SEC EDGAR - Company filings (10-K, 10-Q, 8-K) for CapEx, power contracts, lease commitments
2. ISO/RTO Interconnection Queues - PJM, ERCOT, CAISO, MISO, NYISO, ISO-NE, SPP
3. EPA ECHO - Air/water permits for generators, cooling water
5. Sustainability Reports - PUE, WUE, carbon intensity, renewable %
6. Vendor Case Studies - Vertiv, Schneider, NVIDIA reference architectures
"""

import csv
import json
import re
import time
import requests
from datetime import datetime
from collections import defaultdict

# Load master facility list
facilities = []
with open('master_facility_list_v2.json', 'r', encoding='utf-8') as f:
    facilities = json.load(f)

print(f"Loaded {len(facilities)} facilities for data harvesting")

# ============================================================
# 1. SEC EDGAR FILINGS HARVESTING
# ============================================================
# Major public operators with CIK codes
CIK_MAP = {
    'Meta': '0001326801',
    'AWS': '0001018724',  # Amazon.com
    'Google': '0001652044',  # Alphabet
    'Microsoft': '0000789019',
    'Oracle': '0001341439',
    'Apple': '0000320193',
    'Equinix': '0001101239',
    'Digital Realty': '0001252874',
    'CyrusOne': '0001641994',  # Now private, historical
    'QTS': '0001454786',  # Now private (Blackstone)
    'Vantage': None,  # Private
    'NTT': '0001446813',  # NTT Data
    'CoreWeave': None,  # Private
    'Crusoe': None,  # Private
    'xAI': None,  # Private
}

# SEC EDGAR API base
SEC_BASE = "https://data.sec.gov"
HEADERS = {
    'User-Agent': 'DataCenterResearch/1.0 (research@example.com)',
    'Accept': 'application/json'
}

def fetch_sec_company_facts(cik):
    """Fetch company facts (XBRL data) from SEC"""
    url = f"{SEC_BASE}/api/xbrl/companyfacts/CIK{cik.zfill(10)}.json"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f"  SEC fetch failed for CIK {cik}: {resp.status_code}")
    except Exception as e:
        print(f"  SEC fetch error for CIK {cik}: {e}")
    return None

def extract_capex_power_leases(facts_json):
    """Extract relevant data points from company facts"""
    if not facts_json or 'facts' not in facts_json:
        return {}
    
    facts = facts_json['facts']
    us_gaap = facts.get('us-gaap', {})
    
    results = {}
    
    # Key tags to extract
    tags = {
        'capex': ['PaymentsToAcquirePropertyPlantAndEquipment', 'CapitalExpendituresIncurred'],
        'cash': ['CashAndCashEquivalentsAtCarryingValue'],
        'debt': ['LongTermDebt', 'LongTermDebtNoncurrent'],
        'lease_liability': ['OperatingLeaseLiabilityNoncurrent', 'FinanceLeaseLiabilityNoncurrent'],
        'property_plant_equipment': ['PropertyPlantEquipmentNet'],
        'construction_in_progress': ['ConstructionInProgress'],
    }
    
    for category, tag_list in tags.items():
        for tag in tag_list:
            if tag in us_gaap:
                data = us_gaap[tag]
                if 'units' in data:
                    for unit, values in data['units'].items():
                        if values:
                            # Get latest annual value
                            latest = max(values, key=lambda x: x.get('end', ''))
                            results[f'{category}_{tag}'] = {
                                'value': latest.get('val'),
                                'unit': unit,
                                'end_date': latest.get('end'),
                                'filed': latest.get('filed')
                            }
                            break
                break  # Use first matching tag
    
    return results

# Harvest SEC data for public companies
print("\n=== SEC EDGAR HARVESTING ===")
sec_data = {}
for company, cik in CIK_MAP.items():
    if cik:
        print(f"Fetching {company} (CIK: {cik})...")
        facts = fetch_sec_company_facts(cik)
        if facts:
            extracted = extract_capex_power_leases(facts)
            sec_data[company] = extracted
            print(f"  Extracted {len(extracted)} data points")
        time.sleep(0.1)  # Rate limit

# Save SEC data
with open('sec_harvested_data.json', 'w') as f:
    json.dump(sec_data, f, indent=2)

print("SEC data saved to sec_harvested_data.json")

# ============================================================
# 2. ISO/RTO INTERCONNECTION QUEUE HARVESTING
# ============================================================
# Note: Most ISO queues require registration or have specific APIs
# We'll document the access methods and fetch what's publicly available

ISO_SOURCES = {
    'PJM': {
        'queue_url': 'https://dataminer2.pjm.com/feed/gen_interconnection_queue',
        'requires_auth': True,
        'public_reports': 'https://www.pjm.com/planning/services-requests/interconnection-queues'
    },
    'ERCOT': {
        'queue_url': 'https://www.ercot.com/gridinfo/geninterconnect',
        'requires_auth': False,
        'public_reports': 'https://www.ercot.com/gridinfo/geninterconnect'
    },
    'CAISO': {
        'queue_url': 'https://www.caiso.com/planning/Pages/GeneratorInterconnection/Default.aspx',
        'requires_auth': True,
        'public_reports': 'https://www.caiso.com/planning/Pages/GeneratorInterconnection/Default.aspx'
    },
    'MISO': {
        'queue_url': 'https://www.misoenergy.org/planning/generator-interconnection/',
        'requires_auth': True,
        'public_reports': 'https://www.misoenergy.org/planning/generator-interconnection/'
    },
    'NYISO': {
        'queue_url': 'https://www.nyiso.com/interconnection',
        'requires_auth': True,
        'public_reports': 'https://www.nyiso.com/interconnection'
    },
    'ISO-NE': {
        'queue_url': 'https://www.iso-ne.com/system-planning/system-plans-studies/interconnection',
        'requires_auth': True,
        'public_reports': 'https://www.iso-ne.com/system-planning/system-plans-studies/interconnection'
    },
    'SPP': {
        'queue_url': 'https://www.spp.org/engineering/generation-interconnection/',
        'requires_auth': True,
        'public_reports': 'https://www.spp.org/engineering/generation-interconnection/'
    }
}

# Save ISO source documentation
with open('iso_queue_sources.json', 'w') as f:
    json.dump(ISO_SOURCES, f, indent=2)

print("\n=== ISO/RTO QUEUE SOURCES DOCUMENTED ===")
for iso, info in ISO_SOURCES.items():
    print(f"  {iso}: {info['public_reports']} (Auth: {info['requires_auth']})")

# ============================================================
# 3. EPA ECHO AIR/WATER PERMITS
# ============================================================
# EPA ECHO API: https://echo.epa.gov/tools/data-downloads/echo-data-download

EPA_ECHO_BASE = "https://echo.epa.gov/api"

def search_epa_facilities(lat, lon, radius_miles=5):
    """Search EPA ECHO for facilities near coordinates"""
    # This would require the ECHO API - for now document the approach
    pass

# Document EPA approach
epa_approach = {
    'api_base': EPA_ECHO_BASE,
    'data_downloads': 'https://echo.epa.gov/tools/data-downloads/echo-data-download',
    'key_datasets': [
        'CAA_FACILITY' - Clean Air Act facilities (generators, emissions)',
        'CWA_FACILITY' - Clean Water Act facilities (cooling water intake)',
        'RCRA_FACILITY' - Hazardous waste',
        'EMISSIONS' - GHG and criteria pollutant emissions',
        'PERMITS' - Title V and NSR permits'
    ],
    'query_method': 'Facility search by lat/lon + radius, then filter by NAICS 221310 (Water Supply & Irrigation) or 518210 (Data Processing)',
    'key_fields': [
        'Facility ID', 'Facility Name', 'Latitude', 'Longitude',
        'Permit Type', 'Permit Number', 'Permit Status',
        'Emissions (tons/yr)', 'Heat Input (MMBtu/yr)',
        'Generator Capacity (MW)', 'Fuel Type',
        'Cooling Water Intake (MGD)', 'Discharge Temperature'
    ]
}

with open('epa_echo_approach.json', 'w') as f:
    json.dump(epa_approach, f, indent=2)

print("\n=== EPA ECHO APPROACH DOCUMENTED ===")

# ============================================================
# 4. SUSTAINABILITY REPORT HARVESTING
# ============================================================
# Major operators' sustainability report URLs
SUSTAINABILITY_REPORTS = {
    'Meta': 'https://sustainability.fb.com/reports/',
    'AWS': 'https://sustainability.aboutamazon.com/reporting/',
    'Google': 'https://www.gstatic.com/gumdrop/sustainability/google-environmental-report.pdf',
    'Microsoft': 'https://www.microsoft.com/en-us/corporate-responsibility/sustainability',
    'Oracle': 'https://www.oracle.com/corporate/citizenship/sustainability/',
    'Apple': 'https://www.apple.com/environment/pdf/Apple_Environmental_Progress_Report_2024.pdf',
    'Equinix': 'https://www.equinix.com/sustainability/',
    'Digital Realty': 'https://www.digitalrealty.com/sustainability/',
    'NTT': 'https://www.ntt.com/sustainability/',
    'Vantage': 'https://www.vantage-dc.com/sustainability/',
    'QTS': 'https://www.qtsdatacenters.com/sustainability/',
    'CyrusOne': 'https://cyrusone.com/sustainability/',
}

sustainability_targets = {
    'Meta': {'PUE_target': 1.08, 'renewable_pct': 100, 'water_restoration': 'net positive by 2030'},
    'AWS': {'PUE_target': 1.15, 'renewable_pct': 100, 'water_positive': 'by 2030'},
    'Google': {'PUE_target': 1.10, 'renewable_pct': 100, 'carbon_free': '24/7 by 2030'},
    'Microsoft': {'PUE_target': 1.12, 'renewable_pct': 100, 'carbon_negative': 'by 2030'},
    'Oracle': {'PUE_target': 1.20, 'renewable_pct': 100},
    'Apple': {'PUE_target': 1.10, 'renewable_pct': 100, 'carbon_neutral': 'by 2030'},
}

with open('sustainability_reports.json', 'w') as f:
    json.dump({'report_urls': SUSTAINABILITY_REPORTS, 'public_targets': sustainability_targets}, f, indent=2)

print("\n=== SUSTAINABILITY REPORTS CATALOGUED ===")

# ============================================================
# 5. VENDOR REFERENCE ARCHITECTURES
# ============================================================
VENDOR_REF_ARCHS = {
    'NVIDIA': {
        'DGX_H100': 'https://www.nvidia.com/en-us/data-center/dgx-h100/',
        'DGX_B200': 'https://www.nvidia.com/en-us/data-center/dgx-b200/',
        'GB200_NVL72': 'https://www.nvidia.com/en-us/data-center/gb200-nvl72/',
        'reference_arch': 'https://www.nvidia.com/en-us/data-center/reference-architectures/',
        'key_specs': {
            'DGX_H100': {'gpus': 8, 'power_kW': 10.2, 'rack_kW': 40, 'interconnect': 'NVLink 900 GB/s'},
            'DGX_B200': {'gpus': 8, 'power_kW': 14.3, 'rack_kW': 60, 'interconnect': 'NVLink 1.8 TB/s'},
            'GB200_NVL72': {'gpus': 72, 'power_kW': 120, 'rack_kW': 120, 'interconnect': 'NVLink-C2C 1.8 TB/s'},
        }
    },
    'Vertiv': {
        'liquid_cooling': 'https://www.vertiv.com/en-us/solutions/liquid-cooling/',
        'reference_arch': 'https://www.vertiv.com/en-us/solutions/data-center-reference-architectures/',
        'key_products': ['Liebert XDU', 'Liebert DCD', 'Vertiv SmartAisle']
    },
    'Schneider': {
        'liquid_cooling': 'https://www.se.com/us/en/work/solutions/for-business/data-center/liquid-cooling/',
        'reference_arch': 'https://www.se.com/us/en/work/solutions/for-business/data-center/reference-designs/',
        'key_products': ['Uniflair', 'Coolant Distribution Units']
    },
    'Dell': {
        'reference_arch': 'https://www.delltechnologies.com/en-us/solutions/artificial-intelligence/reference-architectures.htm',
        'key_products': ['PowerEdge XE9680', 'PowerEdge XE8640', 'IR7000 Rack']
    },
    'HPE': {
        'reference_arch': 'https://www.hpe.com/us/en/solutions/ai-reference-architectures.html',
        'key_products': ['Cray EX', 'ProLiant DL380a', 'Cray XD670']
    },
    'Supermicro': {
        'reference_arch': 'https://www.supermicro.com/en/solutions/ai-deep-learning',
        'key_products': ['SYS-821GE-TNHR', 'SYS-421GE-TNHR2', 'Liquid-cooled racks']
    }
}

with open('vendor_reference_architectures.json', 'w') as f:
    json.dump(VENDOR_REF_ARCHS, f, indent=2)

print("\n=== VENDOR REFERENCE ARCHITECTURES CATALOGUED ===")

# ============================================================
# 6. BUILDING PERMITS APPROACH
# ============================================================
BUILDING_PERMITS = {
    'approach': 'County/municipal permit portals (varies by jurisdiction)',
    'key_jurisdictions': {
        'Virginia': ['Loudoun County', 'Prince William County', 'Fairfax County'],
        'Texas': ['Collin County', 'Denton County', 'Travis County', 'Bexar County'],
        'Georgia': ['Fayette County', 'Douglas County'],
        'Arizona': ['Maricopa County', 'Pinal County'],
        'Ohio': ['Franklin County', 'Licking County'],
        'California': ['Santa Clara County', 'Alameda County', 'San Joaquin County'],
        'Nevada': ['Washoe County', 'Storey County'],
        'Oregon': ['Washington County', 'Morrow County'],
        'Washington': ['Grant County', 'Quincy'],
    },
    'search_terms': [
        'data center', 'substation', 'generator', 'electrical permit',
        'mechanical permit', 'cooling tower', 'chiller', 'transformer'
    ],
    'key_fields': [
        'Permit Number', 'Address', 'Description', 'Valuation',
        'Square Footage', 'Status', 'Issue Date', 'Contractor',
        'Electrical Service Amperage', 'Generator kW'
    ],
    'api_note': 'Most jurisdictions lack APIs; requires web scraping or manual search. Some use Accela, EnerGov, or OpenCounter platforms.'
}

with open('building_permits_approach.json', 'w') as f:
    json.dump(BUILDING_PERMITS, f, indent=2)

print("\n=== BUILDING PERMITS APPROACH DOCUMENTED ===")

# ============================================================
# 7. SUMMARY: Phase 2 Complete
# ============================================================
print("\n" + "="*60)
print("PHASE 2 COMPLETE - Data Source Catalog Created")
print("="*60)
print("\nFiles created:")
print("  - sec_harvested_data.json (SEC XBRL data for public operators)")
print("  - iso_queue_sources.json (ISO/RTO interconnection queue access)")
print("  - epa_echo_approach.json (EPA permit search methodology)")
print("  - sustainability_reports.json (Report URLs + public targets)")
print("  - vendor_reference_architectures.json (GPU/cooling specs)")
print("  - building_permits_approach.json (County permit search methodology)")

print("\nNext steps for Phase 3 (Manual Deep Dives):")
print("  1. Use SEC data to validate CapEx/MW assumptions per operator")
print("  2. Access ISO queues (requires registration) for facility-specific MW")
print("  3. Query EPA ECHO for generator/cooling permits at facility coordinates")
print("  4. Parse sustainability reports for actual PUE/WUE by region")
print("  5. Cross-reference vendor architectures for rack density assumptions")
print("  4. Search county permits for facilities in Tier 1 list")