import csv
import json
import time
import requests
from collections import defaultdict

# Load master facility list
def load_csv_safe(filepath):
    records = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            clean_row = {}
            for k, v in row.items():
                if k is not None and not isinstance(v, list):
                    clean_row[k] = v
            records.append(clean_row)
    return records

facilities = load_csv_safe('master_facility_list.csv')
print(f"Loaded {len(facilities)} facilities for enrichment")

# Geocoding function using OSM Nominatim
def geocode_facility(facility):
    parts = []
    if facility.get('city'):
        parts.append(facility['city'])
    if facility.get('state_province'):
        parts.append(facility['state_province'])
    if facility.get('country'):
        parts.append(facility['country'])
    if facility.get('facility_name'):
        parts.append(facility['facility_name'])
    
    query = ', '.join(parts)
    if not query:
        return None, None
    
    url = 'https://nominatim.openstreetmap.org/search'
    params = {'q': query, 'format': 'json', 'limit': 1, 'addressdetails': 1}
    headers = {'User-Agent': 'DataCenterAnalysis/1.0 (research)'}
    
    try:
        resp = requests.get(url, params=params, headers=headers, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data:
                return float(data[0]['lat']), float(data[0]['lon'])
    except Exception as e:
        print(f"  Geocode error for {query}: {e}")
    return None, None

# GPU/Compute estimation functions
def estimate_gpu_counts(capacity_mw):
    if not capacity_mw:
        return {}
    try:
        mw = int(str(capacity_mw).replace(',', ''))
    except:
        return {}
    
    it_load_mw = mw * 0.88  # 88% IT load
    
    return {
        'it_load_mw': round(it_load_mw, 1),
        'est_gpus_h100': int(it_load_mw * 160),        # H100 ~700W/GPU system
        'est_gpus_b200': int(it_load_mw * 100),        # B200 ~1000W/GPU system
        'est_gpus_mi300x': int(it_load_mw * 150),      # MI300X ~750W/GPU system
        'est_gpus_gb200_nvl72': int(it_load_mw * 600),  # GB200 NVL72 density
        'est_racks_50kw': int(it_load_mw * 1000 / 50),
        'est_racks_100kw': int(it_load_mw * 1000 / 100),
    }

def estimate_compute(gpu_estimates):
    h100 = gpu_estimates.get('est_gpus_h100', 0)
    b200 = gpu_estimates.get('est_gpus_b200', 0)
    mi300 = gpu_estimates.get('est_gpus_mi300x', 0)
    
    # TFLOPS per GPU (BF16 / FP8)
    # H100: 989 BF16, 1979 FP8
    # B200: ~2250 BF16, ~4500 FP8 (est)
    # MI300X: 1300 BF16, 2600 FP8
    bf16_pflops = (h100 * 0.989 + b200 * 2.25 + mi300 * 1.3) / 1000
    fp8_pflops = (h100 * 1.979 + b200 * 4.5 + mi300 * 2.6) / 1000
    
    return {
        'est_bf16_pflops': round(bf16_pflops, 1),
        'est_fp8_pflops': round(fp8_pflops, 1),
    }

# Known detailed data for specific facilities
KNOWN_DATA = {
    'Meta Hyperion Campus': {
        'utility': 'Entergy Louisiana',
        'voltage_kv': 500,
        'ppa_price_mwh': 35,
        'generation_mix': 'Gas 60%, Nuclear 25%, Renewable 15%',
        'cooling_detail': 'Direct-to-chip liquid (80%) + rear-door (20%)',
        'water_source_mgd': 5.2,
        'network_detail': 'NVL72 + InfiniBand NDR 400G, 800G ZR+ to Atlanta/Dallas',
        'gpu_generation': 'H100 (2025), B200 (2026+)',
        'cluster_size': 32768,
        'total_capex_billion': 10,
        'source_notes': 'Meta Q4\'24 earnings, Entergy IRP, LA PSC dockets, Vertiv case study',
    },
    'Meta Hyperion': {
        'utility': 'Entergy Louisiana',
        'voltage_kv': 500,
        'ppa_price_mwh': 35,
        'generation_mix': 'Gas 60%, Nuclear 25%, Renewable 15%',
        'cooling_detail': 'Direct-to-chip liquid (80%) + rear-door (20%)',
        'water_source_mgd': 5.2,
        'network_detail': 'NVL72 + InfiniBand NDR 400G, 800G ZR+ to Atlanta/Dallas',
        'gpu_generation': 'H100 (2025), B200 (2026+)',
        'cluster_size': 32768,
        'total_capex_billion': 10,
        'source_notes': 'Meta Q4\'24 earnings, Entergy IRP, LA PSC dockets, Vertiv case study',
    },
    'Stargate Abilene Phase 1': {
        'utility': 'Oncor / ERCOT',
        'voltage_kv': 345,
        'ppa_price_mwh': 45,
        'generation_mix': 'Wind 35%, Solar 25%, Gas 30%, Nuclear 10%',
        'cooling_detail': 'Direct liquid cooling (DLC) 100%',
        'water_source_mgd': 2.0,
        'network_detail': 'NVL72 + InfiniBand NDR, 1.6T to Dallas',
        'gpu_generation': 'GB200 NVL72',
        'cluster_size': 100000,
        'total_capex_billion': 1.2,
        'source_notes': 'Oracle/Stargate announcements, ERCOT queue, Crusoe filings',
    },
    'Stargate Abilene Phase 2': {
        'utility': 'Oncor / ERCOT',
        'voltage_kv': 345,
        'ppa_price_mwh': 45,
        'generation_mix': 'Wind 35%, Solar 25%, Gas 30%, Nuclear 10%',
        'cooling_detail': 'Direct liquid cooling (DLC) 100%',
        'water_source_mgd': 12.0,
        'network_detail': 'NVL72 + InfiniBand NDR, 1.6T to Dallas',
        'gpu_generation': 'GB200 NVL72 / GB300',
        'cluster_size': 500000,
        'total_capex_billion': 6,
        'source_notes': 'Stargate Phase 2 announcements, 6 new buildings',
    },
    'xAI Colossus': {
        'utility': 'MLGW / TVA',
        'voltage_kv': 161,
        'ppa_price_mwh': 40,
        'generation_mix': 'Gas 45%, Nuclear 35%, Coal 15%, Renewable 5%',
        'cooling_detail': 'Direct-to-chip liquid 100%',
        'water_source_mgd': 1.5,
        'network_detail': 'NVL72 + InfiniBand NDR 400G',
        'gpu_generation': 'H100 (100k)',
        'cluster_size': 100000,
        'total_capex_billion': 3,
        'source_notes': 'xAI announcements, MLGW interconnection, Musk tweets',
    },
    'Microsoft Fairwater Atlanta': {
        'utility': 'Georgia Power / Southern Company',
        'voltage_kv': 500,
        'ppa_price_mwh': 38,
        'generation_mix': 'Gas 40%, Nuclear 30%, Coal 15%, Renewable 15%',
        'cooling_detail': 'Rear-door heat exchanger + liquid assist',
        'water_source_mgd': 3.0,
        'network_detail': 'InfiniBand NDR 400G, 800G to Chicago/Dallas',
        'gpu_generation': 'H100 / Maia 100',
        'cluster_size': 16384,
        'total_capex_billion': 2.5,
        'source_notes': 'Microsoft/QTS announcements, Georgia Power IRP',
    },
    'Google Project Pyramid': {
        'utility': 'Entergy Arkansas',
        'voltage_kv': 500,
        'ppa_price_mwh': 32,
        'generation_mix': 'Gas 50%, Nuclear 25%, Renewable 25%',
        'cooling_detail': 'Direct-to-chip liquid (TPU pods)',
        'water_source_mgd': 4.0,
        'network_detail': 'Custom optical circuit switching, 1.6T regional',
        'gpu_generation': 'TPU v5p / v6',
        'cluster_size': 65536,
        'total_capex_billion': 10,
        'source_notes': 'Google/Arkansas EDC announcements, Entergy IRP',
    },
    'Imperial Valley Project': {
        'utility': 'IID / CAISO',
        'voltage_kv': 230,
        'ppa_price_mwh': 45,
        'generation_mix': 'Solar 50%, Geothermal 20%, Gas 30%',
        'cooling_detail': 'Hybrid air/liquid, 100 gas generators + 862MWh BESS',
        'water_source_mgd': 2.5,
        'network_detail': 'InfiniBand NDR, 800G to LA/San Diego',
        'gpu_generation': 'H100 / TPU v5',
        'cluster_size': 32768,
        'total_capex_billion': 10,
        'source_notes': 'Imperial Datacenter site, CAISO queue, KPBS reporting',
    },
    'AWS Gilroy': {
        'utility': 'PG&E',
        'voltage_kv': 115,
        'ppa_price_mwh': 65,
        'generation_mix': 'Solar 30%, Hydro 25%, Gas 25%, Nuclear 15%, Wind 5%',
        'cooling_detail': 'Hybrid air/water, 95% free cooling',
        'water_source_mgd': 0.8,
        'network_detail': '100G/400G to San Jose/Sacramento',
        'gpu_generation': 'Trainium2 / Inferentia2',
        'cluster_size': 8192,
        'total_capex_billion': 0.5,
        'source_notes': 'Gilroy city permits, PG&E interconnection',
    },
    'Crusoe Tallgrass Wyoming': {
        'utility': 'PacifiCorp / WAPA',
        'voltage_kv': 345,
        'ppa_price_mwh': 30,
        'generation_mix': 'Wind 50%, Gas 30%, Coal 20%',
        'cooling_detail': 'Direct liquid cooling (DLC)',
        'water_source_mgd': 1.0,
        'network_detail': '400G/800G to Denver/Salt Lake',
        'gpu_generation': 'H100 / B200',
        'cluster_size': 65536,
        'total_capex_billion': 5,
        'source_notes': 'Crusoe announcements, WY PSC filings',
    },
    'Crusoe Tallgrass': {
        'utility': 'PacifiCorp / WAPA',
        'voltage_kv': 345,
        'ppa_price_mwh': 30,
        'generation_mix': 'Wind 50%, Gas 30%, Coal 20%',
        'cooling_detail': 'Direct liquid cooling (DLC)',
        'water_source_mgd': 1.0,
        'network_detail': '400G/800G to Denver/Salt Lake',
        'gpu_generation': 'H100 / B200',
        'cluster_size': 65536,
        'total_capex_billion': 5,
        'source_notes': 'Crusoe announcements, WY PSC filings',
    },
}

# Process each facility
enriched = []

for i, facility in enumerate(facilities):
    name = facility['facility_name']
    print(f"Processing {i+1}/{len(facilities)}: {name}")
    
    # GPU/Compute estimates
    gpu_est = estimate_gpu_counts(facility.get('capacity_mw'))
    compute_est = estimate_compute(gpu_est)
    
    # Known data override
    known = KNOWN_DATA.get(name, {})
    
    # Geocode if missing
    lat = facility.get('latitude')
    lon = facility.get('longitude')
    if not lat or not lon:
        lat, lon = geocode_facility(facility)
        if lat and lon:
            facility['latitude'] = str(lat)
            facility['longitude'] = str(lon)
            print(f"  Geocoded: {lat:.4f}, {lon:.4f}")
        time.sleep(1.1)
    
    # Parse capacity_mw for economics
    cap_mw = facility.get('capacity_mw')
    try:
        cap_mw_num = int(str(cap_mw).replace(',', '')) if cap_mw else None
    except:
        cap_mw_num = None
    
    # Calculate economics if known capex
    known_capex = known.get('total_capex_billion')
    est_capex_per_kw = ''
    est_capex_per_gpu = ''
    if known_capex and cap_mw_num:
        est_capex_per_kw = round((known_capex * 1e9) / (cap_mw_num * 1000), 0)
    if known_capex and gpu_est.get('est_gpus_h100'):
        est_capex_per_gpu = round((known_capex * 1e9) / gpu_est['est_gpus_h100'], 0)
    
    # Build enriched record
    enriched_facility = dict(facility)
    enriched_facility.update({
        # GPU/Compute estimates
        **gpu_est,
        **compute_est,
        # Known data
        'utility': known.get('utility', ''),
        'voltage_kv': known.get('voltage_kv', ''),
        'ppa_price_mwh': known.get('ppa_price_mwh', ''),
        'generation_mix': known.get('generation_mix', ''),
        'cooling_detail': known.get('cooling_detail', facility.get('cooling_type', '')),
        'water_source_mgd': known.get('water_source_mgd', ''),
        'network_detail': known.get('network_detail', ''),
        'gpu_generation': known.get('gpu_generation', ''),
        'cluster_size': known.get('cluster_size', ''),
        'total_capex_billion': known.get('total_capex_billion', ''),
        'est_capex_per_kw': est_capex_per_kw,
        'est_capex_per_gpu': est_capex_per_gpu,
        'source_notes': known.get('source_notes', facility.get('source_url', '')),
    })
    
    enriched.append(enriched_facility)

# Write enriched CSV
output_fields = [
    'facility_id', 'facility_name', 'operator', 'tenant', 'hyperscaler_category',
    'city', 'state_province', 'country', 'latitude', 'longitude',
    'status', 'capacity_mw', 'capacity_category', 'expected_online_date',
    'project_cost_usd', 'cooling_type', 'cooling_detail', 'power_source',
    'purpose', 'source_url', 'notes', 'tier',
    # New fields
    'it_load_mw', 'est_gpus_h100', 'est_gpus_b200', 'est_gpus_mi300x', 'est_gpus_gb200_nvl72',
    'est_racks_50kw', 'est_racks_100kw', 'est_bf16_pflops', 'est_fp8_pflops',
    'utility', 'voltage_kv', 'ppa_price_mwh', 'generation_mix',
    'water_source_mgd', 'network_detail', 'gpu_generation', 'cluster_size',
    'total_capex_billion', 'est_capex_per_kw', 'est_capex_per_gpu', 'source_notes',
]

with open('master_facility_list_v3_enriched.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=output_fields)
    writer.writeheader()
    writer.writerows(enriched)

# Also write JSON
with open('master_facility_list_v3_enriched.json', 'w', encoding='utf-8') as f:
    json.dump(enriched, f, indent=2, ensure_ascii=False)

print(f"\nEnriched data written to:")
print(f"  master_facility_list_v3_enriched.csv")
print(f"  master_facility_list_v3_enriched.json")

# Summary
with_known = sum(1 for f in enriched if f.get('source_notes'))
with_coords = sum(1 for f in enriched if f.get('latitude') and f.get('longitude'))
print(f"\nFacilities with known detailed data: {with_known}/{len(enriched)}")
print(f"Facilities with coordinates: {with_coords}/{len(enriched)}")

# Tier 1 summary
tier1 = [f for f in enriched if f['tier'] == 'Tier 1']
total_mw = sum(int(str(f['capacity_mw']).replace(',', '')) for f in tier1 if f['capacity_mw'] and str(f['capacity_mw']).replace(',', '').isdigit())
total_gpu_h100 = sum(f.get('est_gpus_h100', 0) for f in tier1)
total_bf16 = sum(f.get('est_bf16_pflops', 0) for f in tier1)
total_capex = sum(float(f.get('total_capex_billion', 0) or 0) for f in tier1)
print(f"\nTier 1 Aggregate:")
print(f"  Facilities: {len(tier1)}")
print(f"  Total Capacity: {total_mw:,} MW")
print(f"  Est. H100-equivalent GPUs: {total_gpu_h100:,}")
print(f"  Est. BF16 PFLOPS: {total_bf16:.1f}")
print(f"  Known CapEx: ${total_capex:.1f}B")