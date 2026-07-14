import json
with open('C:/Users/NITHING/Desktop/projections/data_centers/master_facility_list_v3_enriched.json', 'r') as f:
    data = json.load(f)

# Check all keys in first record
print("All keys in first record:")
for k in sorted(data[0].keys()):
    print(f"  {k}")

print("\n\nSample values for Meta Hyperion:")
for d in data:
    if 'Meta Hyperion' in d.get('facility_name', ''):
        for k, v in d.items():
            if v and str(v).strip():
                print(f"  {k}: {v}")
        break