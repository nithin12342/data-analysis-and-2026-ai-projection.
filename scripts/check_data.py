import json
with open('C:/Users/NITHING/Desktop/projections/data_centers/master_facility_list_v3_enriched.json', 'r') as f:
    data = json.load(f)
for d in data[:5]:
    print(f"{d['facility_name']}:")
    print(f"  inference_fp8_pflops: {d.get('inference_fp8_pflops', 'MISSING')}")
    print(f"  est_tokens_per_sec_billions: {d.get('est_tokens_per_sec_billions', 'MISSING')}")
    print(f"  est_gpu_count: {d.get('est_gpu_count', 'MISSING')}")
    print(f"  capacity_mw: {d.get('capacity_mw', 'MISSING')}")
    print()