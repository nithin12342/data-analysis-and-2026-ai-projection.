import json
import os

enriched_path = "C:/Users/NITHING/Desktop/projections/data_centers/master_facility_list_v3_enriched.json"

if not os.path.exists(enriched_path):
    print(f"Error: {enriched_path} does not exist.")
    exit(1)

with open(enriched_path, "r", encoding="utf-8") as f:
    facilities = json.load(f)

planned_or_constructing = [f for f in facilities if f.get("status", "").lower() in ["planned", "under construction", "constructing"]]

table_rows = []
for f in planned_or_constructing:
    name = f.get("facility_name", "Unknown")
    operator = f.get("operator", "Unknown")
    status = f.get("status", "Unknown")
    power_src = f.get("power_source", "").strip()
    gen_mix = f.get("generation_mix", "").strip()
    notes = f.get("notes", "").strip()
    source_notes = f.get("source_notes", "").strip()
    
    text = (power_src + " " + gen_mix + " " + notes + " " + source_notes).lower()
    
    # Determine onsite planning
    has_onsite = any(kw in text for kw in ["onsite", "solar", "nuclear", "gas", "turbine", "generator", "smr", "wind", "geothermal", "bess"])
    
    # Determine regulatory approval / active filings
    approval_status = "No data"
    approval_details = []
    
    if "permit" in text:
        approval_status = "Approved / Permitted"
        approval_details.append("Air/building permits cited")
    if any(kw in text for kw in ["psc", "dockets", "filings"]):
        approval_status = "Regulatory Filings / PSC Review"
        approval_details.append("State Utility Commission dockets")
    if any(kw in text for kw in ["caiso", "ercot", "interconnection", "queue"]):
        approval_status = "Grid Connection Active / Interconnected"
        approval_details.append("ISO Queue / Grid Agreement")
    if "contract" in text:
        approval_status = "Utility Contract Executed"
        approval_details.append("Power Supply Agreement")
    
    details_str = ", ".join(approval_details) if approval_details else "Public announcement / pending filings"
    
    if has_onsite or gen_mix or power_src:
        table_rows.append({
            "id": f.get("facility_id", "N/A"),
            "name": name,
            "operator": operator,
            "status": status,
            "onsite_tech": gen_mix if gen_mix else "Onsite generation planned",
            "regulatory": approval_status if approval_details else "Pending Review",
            "details": details_str
        })

print("| Facility ID | Name | Operator | Status | Onsite Tech / Mix | Regulatory Status | Approval / Filing Details |")
print("|---|---|---|---|---|---|---|")
for row in table_rows:
    print(f"| {row['id']} | {row['name']} | {row['operator']} | {row['status']} | {row['onsite_tech']} | {row['regulatory']} | {row['details']} |")
