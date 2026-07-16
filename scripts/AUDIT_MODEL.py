import json

# Load and audit the model outputs
with open('C:/Users/NITHING/Desktop/projections/data_centers/TESM_FULL_RESULTS.json', 'r') as f:
    results = json.load(f)

print("=" * 70)
print("COMMON SENSE AUDIT OF TESM MODEL OUTPUTS")
print("=" * 70)

# 1. Revenue Reality Check
print("\n1. REVENUE REALITY CHECK")
print("-" * 50)
scenarios = results['scenario_analysis']['scenarios']
for key, res in scenarios.items():
    final = res['yearly'][-1]['aggregate']
    rev_t = final['revenue'] / 1e12
    ebitda_t = final['ebitda'] / 1e12
    margin = ebitda_t / rev_t * 100
    print(f"  {res['scenario']}: Rev=${rev_t:.1f}T, EBITDA=${ebitda_t:.1f}T, Margin={margin:.0f}%")

print("\n  REALITY CHECK:")
print("  - Global Cloud Market (2024): ~$600B")
print("  - Global Semiconductor Market (2024): ~$630B") 
print("  - Global GDP: ~$105T")
print("  - Model Base Case Rev: $4.6T = 7.6x Cloud Market = 7.3x Semi Market")
print("  - VERDICT: IMPOSSIBLE - revenue 5-10x total addressable market")

# 2. EBITDA Margin
print("\n2. EBITDA MARGIN CHECK")
print("-" * 50)
print("  Model margins: 96-99%")
print("  Real Cloud Gross Margins: 60-70%")
print("  Real Cloud EBITDA Margins: 25-35% (AWS ~30%, Azure ~35%, GCP ~10-15%)")
print("  Model missing: R&D (15-20%), S&M (10-15%), G&A (5-10%), Depreciation (10-15%)")
print("  VERDICT: Model assumes zero operating costs")

# 3. ROIC Check
print("\n3. ROIC CHECK")
print("-" * 50)
for key, res in scenarios.items():
    roic = res['yearly'][-1]['aggregate']['avg_roic'] * 100
    print(f"  {res['scenario']}: {roic:.0f}%")
print("  Real hyperscaler ROIC: 15-25%")
print("  Model: 186% - 896%")
print("  VERDICT: Revenue massively overstated relative to capital")

# 4. Pre-revenue companies
print("\n4. PRE-REVENUE COMPANIES REVENUE")
print("-" * 50)
hyperscaler_agg = results['hyperscaler_aggregate']
for name, data in hyperscaler_agg.items():
    rev = data['revenue_billion']
    capex = data['capex_billion']
    if name in ['Bitzero', 'Nscale', 'Pacifico Energy', 'New Era Energy', 'Energy Abundance',
                'Sailfish Digital', 'GridFree AI', 'Fermi America', 'Homer City', 'Joule Capital',
                'STAK Energy', 'Vermaland', 'Tract', 'Northpoint Development', 'Beale Infrastructure']:
        print(f"  {name}: Rev=${rev:.0f}B, CapEx=${capex:.1f}B, Rev/CapEx={rev/capex:.1f}x")

# 5. Revenue per PFLOPS calibration
print("\n5. REVENUE PER PFLOPS CALIBRATION")
print("-" * 50)
print("  Model assumption: $50M per PFLOPS FP8/year at 100% utilization")
print()
print("  REAL WORLD CALIBRATION:")
print("  H100 cost: ~$30K")
print("  H100 FP8: ~4 TFLOPS (marketing) / ~2 TFLOPS real")
print("  1 PFLOPS FP8 = 1,000 TFLOPS = 250-500 H100s")
print("  Cloud H100 rental: $2-4/hour")
print("  250 H100s at $3/hr = $750/hr = $6.6M/year at 100% utilization")
print("  >>> Model $50M is 7.5x REALITY")
print()
print("  ALSO: Model DOUBLE COUNTS revenue:")
print("  - Compute rental revenue: PFLOPS * $50M * utilization")
print("  - Token API revenue: tokens/sec * $1K/B * utilization")
print("  But token API IS compute rental - same revenue stream!")
print("  >>> Double counting adds ~30-50% extra revenue")

# 6. Facility status ignored
print("\n6. FACILITY STATUS IGNORED")
print("-" * 50)
# Load facility data
with open('C:/Users/NITHING/Desktop/projections/data_centers/master_facility_list_v3_enriched.json', 'r') as f:
    facilities = json.load(f)

status_count = {}
status_mw = {}
for f in facilities:
    s = f.get('status', 'Unknown')
    cap = f.get('capacity_mw', 0)
    if cap and str(cap).isdigit():
        cap = int(cap)
    else:
        cap = 0
    status_count[s] = status_count.get(s, 0) + 1
    status_mw[s] = status_mw.get(s, 0) + cap

total_mw = sum(status_mw.values())
for s, cnt in sorted(status_count.items()):
    mw = status_mw.get(s, 0)
    pct = mw / total_mw * 100 if total_mw > 0 else 0
    print(f"  {s}: {cnt} facilities, {mw:,} MW ({pct:.1f}%)")

print("\n  >>> Model applies SAME revenue formula to ALL statuses")
print("  >>> 86% of capacity is PLANNED (may never be built) but generates revenue!")

# 7. GPU estimation check
print("\n7. GPU ESTIMATION CHECK")
print("-" * 50)
print("  Model: GPUs = capacity_mw * 1000 / 0.7")
print()
for f in facilities:
    cap = f.get('capacity_mw', 0)
    if cap and str(cap).isdigit() and int(cap) > 5000:
        gpus = int(cap) * 1000 / 0.7
        print(f"  {f['facility_name']}: {cap} MW -> {gpus:,.0f} GPUs")

print()
print("  NVIDIA 2024 H100 shipments: ~2M units")
print("  >>> Single facility (Bitzero 9GW) = 12.8M GPUs = 6.4x NVIDIA ANNUAL OUTPUT")
print()
print("  Also ignores:")
print("  - PUE 1.15: only 87% of power to IT")
print("  - GPU power share: ~60-70% of IT load (rest CPU, networking, storage)")
print("  - Real GPU density: ~800-1000 GPUs/MW (not 1400)")

# 8. Google valuation
print("\n8. GOOGLE VALUATION CHECK")
print("-" * 50)
for name, data in hyperscaler_agg.items():
    if name in ['Google', 'AWS', 'Microsoft', 'Meta', 'Oracle']:
        ev = data.get('ev_trillion', 0) if 'ev_trillion' in data else 'N/A'
        capex = data.get('capex_billion', 0)
        rev = data.get('revenue_billion', 0)
        ebitda = data.get('ebitda_billion', 0)
        print(f"  {name}: Rev=${rev:.1f}B, EBITDA=${ebitda:.1f}B, CapEx=${capex:.1f}B")

print()
print("  Reality: Google Market Cap ~$2.2T, Cloud AI Revenue ~$9B/yr")
print("  Model: Google EV=$0.04T, Rev=$12.6B (ok), but EV=$40B vs $2.2T actual = 55x OFF")

# 9. Root cause summary
print("\n" + "=" * 70)
print("ROOT CAUSES OF NONSENSICAL OUTPUTS")
print("=" * 70)
root_causes = [
    ("Revenue/PFLOPS assumption", "$50M is 7.5x too high (real: ~$6.6M)"),
    ("Double counting", "Compute rental + Token API = same revenue stream"),
    ("Facility status ignored", "86% capacity is Planned but generates full revenue"),
    ("GPU estimation", "capacity/0.7kW ignores PUE, non-GPU power, real density"),
    ("Pre-revenue companies", "No anchor revenue but PFLOPS formula gives $190-343B"),
    ("Anchor blending", "50/50 anchor + PFLOPS = double revenue for hyperscalers"),
    ("Zero operating costs", "No R&D, S&M, G&A, Depreciation = 98% EBITDA margin"),
    ("Google anchor wrong", "$9B revenue anchor but $10B capex -> 3.7x EV/CapEx vs 55x actual"),
]
for i, (cause, detail) in enumerate(root_causes, 1):
    print(f"  {i}. {cause}: {detail}")

print("\n" + "=" * 70)
print("REQUIRED FIXES BEFORE MODEL IS USABLE")
print("=" * 70)
fixes = [
    "Revenue/PFLOPS: $50M -> $6.6M (calibrate to H100 cloud pricing)",
    "Remove double counting: Keep only compute rental OR token API, not both",
    "Facility status filter: Only Operating (100%) + Under Construction (50%) generate revenue",
    "GPU estimation: capacity_mw * 1000 * 0.87 (PUE) * 0.65 (GPU share) / 0.7 = ~800 GPUs/MW",
    "Pre-revenue companies: Zero revenue until anchor tenant + operating",
    "Anchor only: Use anchor revenue for hyperscalers, PFLOPS only for neoclouds",
    "Add operating costs: R&D 18%, S&M 12%, G&A 8%, D&A 12% of revenue",
    "Recalibrate Google anchor: Use actual market cap or realistic EV/Revenue multiple",
]
for i, fix in enumerate(fixes, 1):
    print(f"  {i}. {fix}")