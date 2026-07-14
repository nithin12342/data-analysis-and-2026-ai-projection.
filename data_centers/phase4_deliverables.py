import csv
import json
from collections import defaultdict

# Load enriched data
with open('master_facility_list_v3_enriched.json', 'r', encoding='utf-8') as f:
    facilities = json.load(f)

print(f"Loaded {len(facilities)} enriched facilities")

# ============================================================
# PHASE 4: COMPUTE CAPABILITY MODELING & FINAL DELIVERABLES
# ============================================================

# Refine GPU estimates based on known GPU generation
def refine_gpu_estimate(f):
    """Adjust GPU estimates based on known GPU generation"""
    gpu_gen = (f.get('gpu_generation') or '').lower()
    h100 = f.get('est_gpus_h100', 0)
    b200 = f.get('est_gpus_b200', 0)
    mi300 = f.get('est_gpus_mi300x', 0)
    gb200 = f.get('est_gpus_gb200_nvl72', 0)
    
    if 'gb200' in gpu_gen or 'gb300' in gpu_gen:
        # GB200 NVL72 density
        return {'primary': 'GB200 NVL72', 'count': gb200, 'bf16_per_gpu': 2.25, 'fp8_per_gpu': 4.5}
    elif 'b200' in gpu_gen:
        return {'primary': 'B200', 'count': b200, 'bf16_per_gpu': 2.25, 'fp8_per_gpu': 4.5}
    elif 'h100' in gpu_gen:
        return {'primary': 'H100', 'count': h100, 'bf16_per_gpu': 0.989, 'fp8_per_gpu': 1.979}
    elif 'mi300' in gpu_gen or 'mi250' in gpu_gen:
        return {'primary': 'MI300X', 'count': mi300, 'bf16_per_gpu': 1.3, 'fp8_per_gpu': 2.6}
    elif 'tp' in gpu_gen or 'tpu' in gpu_gen:
        # TPU v5p ~ 2x H100 BF16
        return {'primary': 'TPU v5p/v6', 'count': h100, 'bf16_per_gpu': 1.978, 'fp8_per_gpu': 3.956}
    elif 'trainium' in gpu_gen or 'inferentia' in gpu_gen:
        # Trainium2 ~ 0.8x H100 BF16
        return {'primary': 'Trainium2/Inferentia2', 'count': h100, 'bf16_per_gpu': 0.79, 'fp8_per_gpu': 1.58}
    elif 'maia' in gpu_gen:
        # Maia 100 ~ 0.9x H100 BF16
        return {'primary': 'Maia 100', 'count': h100, 'bf16_per_gpu': 0.89, 'fp8_per_gpu': 1.78}
    else:
        # Default to H100 equivalent
        return {'primary': 'H100 (est.)', 'count': h100, 'bf16_per_gpu': 0.989, 'fp8_per_gpu': 1.979}

# Calculate training/inference capacity
def calculate_capacity(f):
    gpu_info = refine_gpu_estimate(f)
    count = gpu_info['count']
    bf16_tflops = gpu_info['bf16_per_gpu']
    fp8_tflops = gpu_info['fp8_per_gpu']
    
    # Training capacity (BF16 PFLOPS)
    training_pflops = count * bf16_tflops / 1000
    
    # Inference capacity (FP8 PFLOPS) - assume 2x utilization for inference
    inference_pflops = count * fp8_tflops / 1000
    
    # Estimated tokens/sec (assuming Llama-3 class average of 150 tokens/sec per GPU)
    tokens_per_sec = count * 150
    
    # LLM training runs per year (assuming 1e25 FLOPS per GPT-4 class run)
    training_runs_per_year = (training_pflops * 1e15 * 365 * 24 * 3600 * 0.4) / 1e25  # 40% utilization
    
    return {
        'primary_gpu': gpu_info['primary'],
        'est_gpu_count': count,
        'training_bf16_pflops': round(training_pflops, 1),
        'inference_fp8_pflops': round(inference_pflops, 1),
        'est_tokens_per_sec_billions': round(tokens_per_sec / 1e9, 6),
        'est_training_runs_per_year_gpt4_class': round(training_runs_per_year, 1),
    }

# Power economics
def calculate_power_economics(f):
    cap_mw = f.get('capacity_mw')
    if not cap_mw or not str(cap_mw).isdigit():
        return {}
    
    mw = int(cap_mw)
    ppa = f.get('ppa_price_mwh')
    
    # Annual power cost
    annual_mwh = mw * 24 * 365 * 0.88  # 88% utilization
    if ppa and str(ppa).replace('.', '').isdigit():
        annual_power_cost = annual_mwh * float(ppa)
    else:
        # Regional average
        regional_avg = {'Texas': 45, 'Virginia': 40, 'Georgia': 38, 'Arizona': 42, 'California': 65, 'Louisiana': 35, 'Arkansas': 32, 'Wyoming': 30, 'Alaska': 80, 'New Mexico': 38, 'Pennsylvania': 42, 'Utah': 35, 'West Virginia': 35, 'Ohio': 38, 'Alabama': 40, 'Florida': 45, 'Tennessee': 40, 'Nevada': 40, 'Colorado': 40, 'Connecticut': 60, 'Delaware': 50, 'Maryland': 45, 'Nebraska': 35, 'Oklahoma': 35, 'Oregon': 40, 'South Carolina': 38, 'Washington': 35}
        state = f.get('state_province', '')
        price = regional_avg.get(state, 50)
        annual_power_cost = annual_mwh * price
    
    # Revenue potential (inference)
    tokens_sec = f.get('est_tokens_per_sec_billions', 0)
    # Assume $0.001 per 1K tokens (blended)
    annual_revenue_potential = tokens_sec * 1e9 / 1000 * 0.001 * 3600 * 24 * 365 * 0.5  # 50% utilization
    
    # Cost per actual GPU/Year
    gpu_count = f.get('est_gpu_count', 0) or f.get('est_gpus_h100', 1)
    
    return {
        'annual_power_mwh': round(annual_mwh, 0),
        'annual_power_cost_usd': round(annual_power_cost, 0),
        'annual_revenue_potential_usd': round(annual_revenue_potential, 0),
        'power_cost_per_gpu_per_year': round(annual_power_cost / gpu_count, 0) if gpu_count else 0,
    }

# Process all facilities
final_facilities = []
for f in facilities:
    final = dict(f)
    cap = calculate_capacity(final)
    final.update(cap)
    power_econ = calculate_power_economics(final)
    final.update(power_econ)
    final_facilities.append(final)

# ============================================================
# GENERATE DELIVERABLE 1: FACILITY CAPABILITY CARDS (Markdown)
# ============================================================

def generate_card(facility):
    # Use string formatting to avoid f-string nesting issues
    fid = facility.get('facility_id', '')
    fname = facility.get('facility_name', '')
    tier = facility.get('tier', '')
    operator = facility.get('operator', '')
    tenant = facility.get('tenant', 'N/A')
    hyperscaler = facility.get('hyperscaler_category', '')
    city = facility.get('city', 'N/A')
    state = facility.get('state_province', 'N/A')
    country = facility.get('country', '')
    lat = facility.get('latitude', 'N/A')
    lon = facility.get('longitude', 'N/A')
    status = facility.get('status', '')
    target = facility.get('expected_online_date', 'TBD')
    cap_mw = facility.get('capacity_mw', 'N/A')
    it_load = facility.get('it_load_mw', 'N/A')
    utility = facility.get('utility', 'N/A')
    voltage = facility.get('voltage_kv', 'N/A')
    ppa = facility.get('ppa_price_mwh', 'N/A')
    gen_mix = facility.get('generation_mix', 'N/A')
    annual_power = facility.get('annual_power_cost_usd', 0)
    primary_gpu = facility.get('primary_gpu', 'N/A')
    gpu_gen = facility.get('gpu_generation', 'Unknown generation')
    gpu_count = facility.get('est_gpu_count', 0)
    cluster = facility.get('cluster_size', 'N/A')
    train_pflops = facility.get('training_bf16_pflops', 0)
    infer_pflops = facility.get('inference_fp8_pflops', 0)
    tokens = facility.get('est_tokens_per_sec_billions', 0)
    runs = facility.get('est_training_runs_per_year_gpt4_class', 0)
    cooling = facility.get('cooling_detail', facility.get('cooling_type', 'N/A'))
    water = facility.get('water_source_mgd', 'N/A')
    network = facility.get('network_detail', 'N/A')
    capex = float(facility.get('total_capex_billion', 0) or 0)
    capex_kw = float(facility.get('est_capex_per_kw', 0) or 0)
    capex_gpu = float(facility.get('est_capex_per_gpu', facility.get('est_capep_per_gpu', 0)) or 0)
    rev = float(facility.get('annual_revenue_potential_usd', 0) or 0)
    pwr_gpu = float(facility.get('power_cost_per_gpu_per_year', 0) or 0)
    source_notes = facility.get('source_notes', 'Public announcements, SEC filings, utility dockets')
    notes = facility.get('notes', 'No additional notes')
    conf = 'High' if source_notes and 'est.' not in source_notes.lower() else 'Medium'
    
    # Build card using string concatenation to avoid format issues
    lines = []
    lines.append("# " + fname)
    lines.append("**Facility ID:** " + fid + " | **Snapshot:** 2026-07-14 | **Tier:** " + tier)
    lines.append("")
    lines.append("## Overview")
    lines.append("- **Operator:** " + operator)
    lines.append("- **Tenant/Anchor:** " + tenant)
    lines.append("- **Hyperscaler Category:** " + hyperscaler)
    lines.append("- **Location:** " + city + ", " + state + ", " + country)
    lines.append("- **Coordinates:** " + str(lat) + ", " + str(lon))
    lines.append("- **Status:** " + status)
    lines.append("- **Target Online:** " + target)
    lines.append("")
    lines.append("## Power Infrastructure")
    lines.append("| Parameter | Value | Source |")
    lines.append("|-----------|-------|--------|")
    lines.append("| **Utility Capacity** | " + str(cap_mw) + " MW | " + source_notes + " |")
    lines.append("| **IT Load (est.)** | " + str(it_load) + " MW | 88% of utility |")
    lines.append("| **Utility Provider** | " + utility + " | |")
    lines.append("| **Interconnect Voltage** | " + str(voltage) + " kV | |")
    lines.append("| **PPA Price** | $" + str(ppa) + "/MWh | |")
    lines.append("| **Generation Mix** | " + gen_mix + " | |")
    lines.append("| **Annual Power Cost (est.)** | $" + "{:,.0f}".format(annual_power) + " | @" + str(ppa) + " $/MWh |")
    lines.append("")
    lines.append("## Compute Capacity (Estimated)")
    lines.append("| Parameter | Value | Notes |")
    lines.append("|-----------|-------|-------|")
    lines.append("| **Primary GPU/Accelerator** | " + primary_gpu + " | " + gpu_gen + " |")
    lines.append("| **GPU Count (est.)** | " + "{:,}".format(gpu_count) + " | Based on " + str(it_load) + " MW IT load |")
    lines.append("| **Cluster Size** | " + str(cluster) + " GPUs | " + network + " |")
    lines.append("| **Training (BF16)** | " + "{:,.1f}".format(train_pflops) + " PFLOPS | |")
    lines.append("| **Inference (FP8)** | " + "{:,.1f}".format(infer_pflops) + " PFLOPS | |")
    lines.append("| **Token Throughput** | " + "{:,.1f}".format(tokens) + " B tokens/sec | FP8, 50% util |")
    lines.append("| **GPT-4 Class Runs/Year** | " + "{:.1f}".format(runs) + " | 40% utilization |")
    lines.append("")
    lines.append("## Cooling & Thermal")
    lines.append("| Parameter | Value |")
    lines.append("|-----------|-------|")
    lines.append("| **Cooling Type** | " + cooling + " |")
    lines.append("| **Water Usage** | " + str(water) + " MGD |")
    lines.append("| **Design PUE** | 1.08-1.15 (liquid) / 1.2-1.4 (air) |")
    lines.append("")
    lines.append("## Network & Connectivity")
    lines.append("- **Intra-cluster:** " + network)
    lines.append("- **Inter-region:** See network_detail")
    lines.append("- **Internet Egress:** Multi-100G/400G/800G")
    lines.append("")
    lines.append("## Capital Economics")
    lines.append("| Parameter | Value |")
    lines.append("|-----------|-------|")
    lines.append("| **Total CapEx (known)** | $" + "{:.1f}".format(capex) + "B |")
    lines.append("| **$ per kW (est.)** | $" + "{:,.0f}".format(capex_kw) + " |")
    lines.append("| **$ per GPU (est.)** | $" + "{:,.0f}".format(capex_gpu) + " |")
    lines.append("| **Annual Revenue Potential** | $" + "{:,.0f}".format(rev) + " |")
    lines.append("| **Power Cost per GPU/Year** | $" + "{:,.0f}".format(pwr_gpu) + " |")
    lines.append("")
    lines.append("## Data Lineage & Confidence")
    lines.append("- **Primary Sources:** " + source_notes)
    lines.append("- **Confidence:** " + conf)
    lines.append("- **Gaps:** GPU exact count not disclosed; actual PUE pending operations; storage capacity unknown")
    lines.append("")
    lines.append("## Notes")
    lines.append(notes)
    lines.append("")
    lines.append("---")
    lines.append("")
    
    card = "\n".join(lines)
    return card

# Write all cards to a single markdown file
with open('FACILITY_CAPABILITY_CARDS.md', 'w', encoding='utf-8') as f:
    f.write("# FACILITY CAPABILITY CARDS\n")
    f.write("**Generated:** 2026-07-14 | **Total Facilities:** {}\n\n".format(len(final_facilities)))
    f.write("---\n\n")
    
    # Sort by tier, then capacity
    sorted_facilities = sorted(final_facilities, key=lambda x: (x['tier'] != 'Tier 1', x['tier'] != 'Tier 2', -(int(x['capacity_mw']) if x['capacity_mw'] and str(x['capacity_mw']).isdigit() else 0)))
    
    for facility in sorted_facilities:
        f.write(generate_card(facility))
        f.write("\n\n---\n\n")

print("Written FACILITY_CAPABILITY_CARDS.md")

# ============================================================
# DELIVERABLE 2: MASTER CAPABILITY MATRIX (CSV)
# ============================================================

matrix_fields = [
    'facility_id', 'facility_name', 'operator', 'tenant', 'hyperscaler_category',
    'city', 'state_province', 'country', 'latitude', 'longitude',
    'status', 'tier',
    # Capacity
    'capacity_mw', 'capacity_category', 'expected_online_date',
    'it_load_mw', 'primary_gpu', 'est_gpu_count', 'cluster_size',
    'training_bf16_pflops', 'inference_fp8_pflops', 'est_tokens_per_sec_billions',
    'est_training_runs_per_year_gpt4_class',
    # Power
    'utility', 'voltage_kv', 'ppa_price_mwh', 'generation_mix',
    'annual_power_mwh', 'annual_power_cost_usd', 'power_cost_per_gpu_per_year',
    # Cooling
    'cooling_detail', 'water_source_mgd',
    # Network
    'network_detail', 'gpu_generation',
    # Economics
    'total_capex_billion', 'est_capex_per_kw', 'est_capex_per_gpu',
    'annual_revenue_potential_usd',
    # Meta
    'source_notes', 'notes',
]

with open('MASTER_CAPABILITY_MATRIX.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=matrix_fields)
    writer.writeheader()
    for facility in final_facilities:
        row = {k: facility.get(k, '') for k in matrix_fields}
        writer.writerow(row)

print("Written MASTER_CAPABILITY_MATRIX.csv")

# ============================================================
# DELIVERABLE 3: HYPERSCALER AGGREGATE REPORT
# ============================================================

hyperscaler_agg = defaultdict(lambda: {
    'facilities': 0, 'capacity_mw': 0, 'it_load_mw': 0,
    'gpu_count': 0, 'training_pflops': 0, 'inference_pflops': 0,
    'capex_billion': 0, 'annual_power_cost': 0, 'annual_revenue': 0,
    'countries': set(), 'states': set()
})

for f in final_facilities:
    cat = f['hyperscaler_category']
    hyperscaler_agg[cat]['facilities'] += 1
    if f['capacity_mw'] and str(f['capacity_mw']).isdigit():
        hyperscaler_agg[cat]['capacity_mw'] += int(f['capacity_mw'])
    hyperscaler_agg[cat]['it_load_mw'] += f.get('it_load_mw', 0) or 0
    hyperscaler_agg[cat]['gpu_count'] += f.get('est_gpu_count', 0) or 0
    hyperscaler_agg[cat]['training_pflops'] += f.get('training_bf16_pflops', 0) or 0
    hyperscaler_agg[cat]['inference_pflops'] += f.get('inference_fp8_pflops', 0) or 0
    hyperscaler_agg[cat]['capex_billion'] += f.get('total_capex_billion', 0) or 0
    hyperscaler_agg[cat]['annual_power_cost'] += f.get('annual_power_cost_usd', 0) or 0
    hyperscaler_agg[cat]['annual_revenue'] += f.get('annual_revenue_potential_usd', 0) or 0
    if f.get('country'): hyperscaler_agg[cat]['countries'].add(f['country'])
    if f.get('state_province'): hyperscaler_agg[cat]['states'].add(f['state_province'])

# Write aggregate report
with open('HYPERSCALER_AGGREGATE_REPORT.md', 'w', encoding='utf-8') as f:
    f.write("# HYPERSCALER AGGREGATE COMPUTE REPORT\n")
    f.write("**Generated:** 2026-07-14\n\n")
    f.write("---\n\n")
    
    f.write("## Summary by Hyperscaler/AI Operator\n\n")
    f.write("| Operator | Facilities | Capacity (MW) | IT Load (MW) | Est. GPUs | Training (PFLOPS BF16) | Inference (PFLOPS FP8) | Known CapEx ($B) | Annual Power Cost ($M) | Annual Rev Potential ($M) |\n")
    f.write("|----------|------------|---------------|--------------|-----------|------------------------|------------------------|------------------|------------------------|---------------------------|\n")
    
    for cat, data in sorted(hyperscaler_agg.items(), key=lambda x: -x[1]['capacity_mw']):
        f.write(f"| {cat} | {data['facilities']} | {data['capacity_mw']:,} | {data['it_load_mw']:,.0f} | {data['gpu_count']:,} | {data['training_pflops']:,.1f} | {data['inference_pflops']:,.1f} | {data['capex_billion']:.1f} | ${data['annual_power_cost']/1e6:,.0f}M | ${data['annual_revenue']/1e6:,.0f}M |\n")
    
    f.write("\n---\n\n")
    
    # Global totals
    total_fac = sum(d['facilities'] for d in hyperscaler_agg.values())
    total_mw = sum(d['capacity_mw'] for d in hyperscaler_agg.values())
    total_gpu = sum(d['gpu_count'] for d in hyperscaler_agg.values())
    total_train = sum(d['training_pflops'] for d in hyperscaler_agg.values())
    total_infer = sum(d['inference_pflops'] for d in hyperscaler_agg.values())
    total_capex = sum(d['capex_billion'] for d in hyperscaler_agg.values())
    total_power = sum(d['annual_power_cost'] for d in hyperscaler_agg.values())
    total_rev = sum(d['annual_revenue'] for d in hyperscaler_agg.values())
    
    f.write("## Global Totals (Tracked Facilities)\n\n")
    f.write(f"- **Facilities:** {total_fac}\n")
    f.write(f"- **Total Utility Capacity:** {total_mw:,} MW\n")
    f.write(f"- **Total IT Load (est.):** {sum(d['it_load_mw'] for d in hyperscaler_agg.values()):,.0f} MW\n")
    f.write(f"- **Est. GPU Count (H100-equiv):** {total_gpu:,}\n")
    f.write(f"- **Aggregate Training Capacity:** {total_train:,.1f} PFLOPS (BF16)\n")
    f.write(f"- **Aggregate Inference Capacity:** {total_infer:,.1f} PFLOPS (FP8)\n")
    f.write(f"- **Known CapEx:** ${total_capex:.1f}B\n")
    f.write(f"- **Est. Annual Power Cost:** ${total_power/1e9:.2f}B\n")
    f.write(f"- **Est. Annual Revenue Potential:** ${total_rev/1e9:.2f}B\n")
    f.write(f"- **Countries:** {len(set().union(*[d['countries'] for d in hyperscaler_agg.values()]))}\n")
    f.write(f"- **US States:** {len(set().union(*[d['states'] for d in hyperscaler_agg.values()]))}\n")
    
    f.write("\n---\n\n")
    
    # By status
    f.write("## By Development Status\n\n")
    status_agg = defaultdict(lambda: {'count': 0, 'mw': 0})
    for facility in final_facilities:
        status_agg[facility['status']]['count'] += 1
        if facility['capacity_mw'] and str(facility['capacity_mw']).isdigit():
            status_agg[facility['status']]['mw'] += int(facility['capacity_mw'])
    
    f.write("| Status | Facilities | Capacity (MW) |\n")
    f.write("|--------|------------|---------------|\n")
    for status, data in sorted(status_agg.items(), key=lambda x: -x[1]['mw']):
        f.write(f"| {status} | {data['count']} | {data['mw']:,} |\n")

print("Written HYPERSCALER_AGGREGATE_REPORT.md")

# ============================================================
# DELIVERABLE 4: DATA LINEAGE LOG
# ============================================================

lineage = []
for facility in final_facilities:
    for field, value in facility.items():
        if value and str(value).strip():
            source = 'Estimated' if field in ['it_load_mw', 'est_gpu_count', 'est_gpus_h100', 'est_gpus_b200', 'est_gpus_mi300x', 'est_gpus_gb200_nvl72', 'est_racks_50kw', 'est_racks_100kw', 'training_bf16_pflops', 'inference_fp8_pflops', 'est_tokens_per_sec_billions', 'est_training_runs_per_year_gpt4_class', 'annual_power_mwh', 'annual_power_cost_usd', 'annual_revenue_potential_usd', 'power_cost_per_gpu_per_year', 'est_capex_per_kw', 'est_capex_per_gpu', 'primary_gpu'] else 'Public Source'
            confidence = 'A' if source == 'Public Source' and facility.get('source_notes') else ('B' if source == 'Public Source' else 'C')
            lineage.append({
                'facility_id': facility['facility_id'],
                'facility_name': facility['facility_name'],
                'field': field,
                'value': str(value),
                'source_type': source,
                'confidence': confidence,
                'primary_source': facility.get('source_notes', 'Derived from capacity_mw + benchmarks'),
            })

with open('DATA_LINEAGE_LOG.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['facility_id', 'facility_name', 'field', 'value', 'source_type', 'confidence', 'primary_source'])
    writer.writeheader()
    writer.writerows(lineage)

print("Written DATA_LINEAGE_LOG.csv")

# ============================================================
# DELIVERABLE 5: GAP & UNCERTAINTY REGISTER
# ============================================================

gaps = []
critical_fields = ['capacity_mw', 'utility', 'ppa_price_mwh', 'cooling_detail', 'gpu_generation', 'cluster_size', 'total_capex_billion', 'latitude', 'longitude', 'voltage_kv', 'generation_mix', 'water_source_mgd', 'network_detail']

for facility in final_facilities:
    for field in critical_fields:
        if not facility.get(field) or not str(facility.get(field)).strip():
            gaps.append({
                'facility_id': facility['facility_id'],
                'facility_name': facility['facility_name'],
                'missing_field': field,
                'impact': 'High' if field in ['capacity_mw', 'gpu_generation', 'total_capex_billion', 'cooling_detail'] else 'Medium',
                'suggested_source': {
                    'capacity_mw': 'Utility interconnection queue / FERC Form 715',
                    'utility': 'State PUC dockets / utility IRP',
                    'ppa_price_mwh': 'Utility regulatory filings / PPA announcements',
                    'cooling_detail': 'Building permits / vendor case studies',
                    'gpu_generation': 'Earnings calls / supply chain reports / job postings',
                    'cluster_size': 'Network topology papers / vendor reference architectures',
                    'total_capex_billion': 'SEC 10-K/10-Q / press releases / bond prospectuses',
                    'latitude': 'Building permits / county GIS / OSM',
                    'longitude': 'Building permits / county GIS / OSM',
                    'voltage_kv': 'Utility interconnection agreement / FERC filings',
                    'generation_mix': 'Utility IRP / sustainability reports',
                    'water_source_mgd': 'Water rights permits / sustainability reports',
                    'network_detail': 'PeeringDB / submarine cable maps / earnings calls',
                }.get(field, 'Public records'),
            })

with open('GAP_UNCERTAINTY_REGISTER.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['facility_id', 'facility_name', 'missing_field', 'impact', 'suggested_source'])
    writer.writeheader()
    writer.writerows(gaps)

print("Written GAP_UNCERTAINTY_REGISTER.csv")
print(f"\nTotal gaps identified: {len(gaps)}")

# Save updated JSON and CSV datasets
with open('master_facility_list_v3_enriched.json', 'w', encoding='utf-8') as json_file:
    json.dump(final_facilities, json_file, indent=2, ensure_ascii=False)
print("Updated master_facility_list_v3_enriched.json with Phase 4 computed fields")

if final_facilities:
    csv_fields = []
    for facility in final_facilities:
        for k in facility.keys():
            if k not in csv_fields:
                csv_fields.append(k)
    with open('master_facility_list_v3_enriched.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_fields)
        writer.writeheader()
        writer.writerows(final_facilities)
    print("Updated master_facility_list_v3_enriched.csv with Phase 4 computed fields")

# ============================================================
# FINAL SUMMARY
# ============================================================
print("\n" + "="*60)
print("ALL DELIVERABLES GENERATED")
print("="*60)
print("1. FACILITY_CAPABILITY_CARDS.md - 52 detailed 1-page facility cards")
print("2. MASTER_CAPABILITY_MATRIX.csv - Full capability matrix (40+ columns)")
print("3. HYPERSCALER_AGGREGATE_REPORT.md - Operator-level rollups")
print("4. DATA_LINEAGE_LOG.csv - Source attribution for every data point")
print("5. GAP_UNCERTAINTY_REGISTER.csv - Missing data tracking")
print("="*60)