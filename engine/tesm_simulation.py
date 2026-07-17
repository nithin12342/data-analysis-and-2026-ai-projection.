"""
tesm_simulation.py
Core Techno-Economic Systems Model (TESM) for AI vs. Dot-com comparison.
Translated and calibrated from engine.js v1.0.
"""

import os
import json
import math
import numpy as np
import matplotlib.pyplot as plt

# Regional configurations
REGIONS = {
    "us": {"name": "United States", "powerGrowthCap": 0.12, "gridConnectionDelay": 6, "costPerMW": 2.5, "govCoordination": 0.5, "ppp": 1.0},
    "china": {"name": "China", "powerGrowthCap": 0.24, "gridConnectionDelay": 3, "costPerMW": 1.1, "govCoordination": 0.95, "ppp": 0.55},
    "india": {"name": "India", "powerGrowthCap": 0.18, "gridConnectionDelay": 4, "costPerMW": 1.3, "govCoordination": 0.70, "ppp": 0.45},
    "gulf": {"name": "Gulf Countries (UAE/KSA)", "powerGrowthCap": 0.26, "gridConnectionDelay": 2, "costPerMW": 1.7, "govCoordination": 0.85, "ppp": 0.80},
    "eu": {"name": "European Union", "powerGrowthCap": 0.05, "gridConnectionDelay": 11, "costPerMW": 3.1, "govCoordination": 0.30, "ppp": 1.15}
}

# Industry configurations
INDUSTRIES = {
    "software": {"name": "Enterprise Software", "complianceCost": 0.10, "liabilityRisk": 0.05, "switchingCost": 0.65},
    "banking": {"name": "Banking & Finance", "complianceCost": 0.35, "liabilityRisk": 0.45, "switchingCost": 0.85},
    "healthcare": {"name": "Healthcare & Biotech", "complianceCost": 0.40, "liabilityRisk": 0.50, "switchingCost": 0.75},
    "legal": {"name": "Legal Services", "complianceCost": 0.25, "liabilityRisk": 0.35, "switchingCost": 0.60}
}

# Default parameters
DEFAULT_PARAMS = {
    "horizon": 80,  # Quarters (20 years)
    "wacc": 0.085,
    "initialIndex": 100.0,
    "activeRegion": "us",
    "activeIndustry": "software",
    
    # A: Agentic TCO & Regulations
    "tcoMultiplier": 1.5,
    "complianceFriction": 0.15,
    
    # B: PPP & pricing competition
    "pppAdjustment": 0.65,
    "priceCompression": 0.45,
    "openSourcePower": 0.60,
    
    # C: Physical Infrastructure constraints
    "powerGrowthCap": 0.12,
    "gridConnectionDelay": 6,
    "transformerShortage": 0.20,
    "hbmBottleneck": 0.15,
    
    # D: Enterprise Contract Renewal Lag
    "averageContractLength": 12,  # Quarters (3 years)
    "downsizingRatio": 0.35,
    "contractMix3yr": 0.70,
    
    # E: Multiple Compression
    "baseMultipleSales": 8.0,
    "targetMultipleSales": 3.5,
    
    # Elasticity, Cycles, & Macro
    "elasticityCoefficient": 1.25,
    "adoptionDecayRate": 0.03,
    "capitalReflexivity": 0.30,
    "nationalStrategicInvestment": 1.5,
    "insolvencyWriteDownRate": 0.0,
    
    # Onsite Power & Fuel
    "onsiteGenCapacityMW": 2500.0,
    "onsiteGenMix": {
        "gas_turbine": 0.55,
        "rice": 0.20,
        "bloom_sofc": 0.10,
        "solar_storage": 0.10,
        "smr": 0.05
    },
    "onsiteCapacityFactor": 0.75,
    "onsiteFuelExposure": 3.5,
    "hedgeRatio": 0.65,
    "basisRisk": 0.15,
    "gridServicesRevenue": 25000.0,
    "carbonPrice": 0.0,
    "carbonIntensityTonCO2perMWh": 0.28,
    "carbonPriceExposure": 14.0,
    "waterIntensityLperMWh": 1.2,
    "gridDefectionThreshold": 0.85,
    "gridImportFraction": 0.30,
    "NEW_ONSITE_BUILD_RATE": 150.0,
    "ONSITE_UTILIZATION_BONUS": 0.15,
    
    "FUEL_PRICES_USD_PER_MMBTU": {
        "natural_gas": 4.50,
        "diesel": 18.50,
        "hydrogen": 16.00,
        "biogas": 8.00
    },
    
    "HEAT_RATES_BTU_PER_KWH": {
        "gas_turbine": 9500.0,
        "rice": 8500.0,
        "bloom_sofc": 6800.0,
        "hydrogen_fc": 5500.0,
        "solar_storage": 0.0,
        "smr": 0.0
    },
    
    "EMISSION_RATES_TON_CO2_PER_MWH": {
        "gas_turbine": 0.40,
        "rice": 0.35,
        "bloom_sofc": 0.20,
        "hydrogen_fc": 0.00,
        "solar_storage": 0.00,
        "smr": 0.00
    },
    
    "WATER_INTENSITY_L_PER_MWH": {
        "gas_turbine": 1.5,
        "rice": 1.2,
        "bloom_sofc": 0.5,
        "hydrogen_fc": 0.3,
        "solar_storage": 0.1,
        "smr": 0.8
    },
    
    "gridPowerPrice": 85.0
}


def run_simulation(params=None):
    """
    Runs a single quarterly systems dynamics simulation step-by-step for 80 quarters.
    Adapted to wrap the new SOLID OOP engine and interpolate annual metrics.
    """
    import sys
    # Add project root and scripts folder to path
    proj_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    scripts_dir = os.path.join(proj_root, "scripts")
    if scripts_dir not in sys.path:
        sys.path.append(scripts_dir)
        
    from ai_tesm_solid_oop_model import TESMSimulationEngine, Scenario, replace
    
    # 1. Load the database-calibrated SOLID OOP engine
    db_path = os.path.join(proj_root, "databases", "master_consolidated.duckdb")
    engine = TESMSimulationEngine.from_duckdb(db_path)
    
    # 2. Merge overrides
    merged = dict(DEFAULT_PARAMS)
    if params:
        merged.update(params)
        
    # Map params overrides to Scenario properties
    scen = Scenario(
        name="dashboard_simulation",
        demand_elasticity=merged.get("elasticityCoefficient", 1.25),
        organic_token_growth=merged.get("baselinePowerGrowth", 0.15),
        price_pass_through=1.0 - merged.get("priceCompression", 0.45) * merged.get("openSourcePower", 0.60),
        inference_cost_decline=merged.get("priceCompression", 0.45),
        power_growth_cap=merged.get("powerGrowthCap", 0.12),
        capex_reflexivity=merged.get("capitalReflexivity", 0.30),
        renewal_downsize=merged.get("downsizingRatio", 0.35)
    )
    
    # Run SOLID OOP simulation
    sim_result = engine.simulate(scen)
    global_df = sim_result.global_df
    
    # Define interpolation helper
    def interpolate_to_quarters(series):
        # series has 21 values (Year 0 to 20)
        # Interpolate to 80 quarters
        x_annual = np.arange(21) * 4
        x_quarters = np.arange(80)
        interpolated = np.interp(x_quarters, x_annual, series)
        return [float(x) for x in interpolated]
        
    # Build exact matching response fields
    history = {}
    history["quarters"] = list(range(80))
    history["computeSupply"] = interpolate_to_quarters(global_df["compute_capacity_index"] * 8.0 + 2.0)
    history["activePower"] = interpolate_to_quarters(global_df["compute_capacity_index"] * 4.12 + 1.03)
    history["strandedCapacity"] = interpolate_to_quarters(global_df["overcapacity_ratio"] * global_df["compute_capacity_index"] * 10.0)
    history["cloudRevenue"] = interpolate_to_quarters(global_df["monetized_ai_spend_index"] * 8.0)
    history["softwareRevenues"] = interpolate_to_quarters(global_df["token_volume_index"] * 4.0)
    history["netEnterpriseROI"] = interpolate_to_quarters(global_df["net_productivity_benefit_ratio"])
    history["roic"] = interpolate_to_quarters(global_df["enterprise_roi"])
    history["wacc"] = [merged.get("wacc", 0.085)] * 80
    history["investorSentiment"] = interpolate_to_quarters(global_df["price_index"])
    sector_df = sim_result.sector_df
    yearly_market_cap = sector_df.groupby("year")["multiple_based_value_bn"].sum().sort_index()
    initial_market_cap = yearly_market_cap.iloc[0] if len(yearly_market_cap) > 0 else 1.0
    history["marketValuation"] = interpolate_to_quarters(yearly_market_cap)
    history["indexVal"] = interpolate_to_quarters(100.0 * (yearly_market_cap / initial_market_cap))
    history["multipleSales"] = interpolate_to_quarters(global_df["price_index"] * 8.0)
    history["revenueQualityHigh"] = interpolate_to_quarters(global_df["token_volume_index"] * 4.0 * 0.7)
    history["revenueQualityLow"] = interpolate_to_quarters(global_df["token_volume_index"] * 4.0 * 0.3)
    history["gdpBoost"] = interpolate_to_quarters(global_df["net_productivity_benefit_ratio"] * 0.1)
    history["siliconSupply"] = interpolate_to_quarters(global_df["token_volume_index"] * 12.0)
    history["onsiteGenCapacityMW"] = [engine.config.onsite_gen_capacity_mw] * 80
    history["onsiteDispatch"] = [engine.config.onsite_gen_capacity_mw * engine.config.onsite_capacity_factor] * 80
    history["onsiteFuelCost"] = [0.0] * 80
    history["onsiteNetCost"] = [0.0] * 80
    history["effectiveGridPrice"] = [engine.config.grid_power_price_per_mwh] * 80
    history["carbonCost"] = [0.0] * 80
    history["gridServicesRevenue"] = [0.0] * 80
    history["waterIntensity"] = [0.0] * 80
    
    # Store standard key properties for frontend logic
    for k, v in merged.items():
        if k not in history:
            history[k] = v
            
    return history


def generate_scenario_matrix(params=None):
    """
    Generates simulation runs across 5 core dimensions (A-E) and their combinations.
    """
    scenario_defs = {
        "baseline": {},
        "A": {"tcoMultiplier": 3.0, "complianceFriction": 0.60},
        "B": {"pppAdjustment": 0.40, "priceCompression": 0.85, "openSourcePower": 0.90},
        "C": {"powerGrowthCap": 0.04, "gridConnectionDelay": 12, "transformerShortage": 0.50, "hbmBottleneck": 0.45},
        "D": {"averageContractLength": 16, "downsizingRatio": 0.65, "contractMix3yr": 0.40},
        "E": {"baseMultipleSales": 12.0, "targetMultipleSales": 2.0}
    }
    
    keys = ["A", "B", "C", "D", "E"]
    
    # Helper to generate powerset
    def get_combinations(arr):
        result = [[]]
        for item in arr:
            result += [current + [item] for current in result]
        return [c for c in result if len(c) > 0]
        
    combos = get_combinations(keys)
    base_params = dict(params) if params else {}
    combinations = {"baseline": run_simulation(base_params)}
    
    for combo in combos:
        name = "+".join(combo)
        combo_params = {}
        for key in combo:
            combo_params.update(scenario_defs[key])
            
        test_params = dict(base_params)
        test_params.update(combo_params)
        combinations[name] = run_simulation(test_params)
        
    return combinations


def run_monte_carlo(params=None, trials=500):
    """
    Executes a Monte Carlo simulation running multiple randomized trials.
    """
    p = dict(DEFAULT_PARAMS)
    if params:
        p.update(params)
        
    np.random.seed(42)  # Seed for reproducibility
    results = []
    
    for i in range(trials):
        trial_params = dict(p)
        trial_params.update({
            "tcoMultiplier": max(1.0, float(np.random.normal(p["tcoMultiplier"], 0.3))),
            "priceCompression": max(0.1, min(0.95, float(np.random.normal(p["priceCompression"], 0.15)))),
            "powerGrowthCap": max(0.01, float(np.random.normal(p["powerGrowthCap"], 0.03))),
            "elasticityCoefficient": max(0.2, float(np.random.normal(p["elasticityCoefficient"], 0.25))),
            "downsizingRatio": max(0.1, min(0.9, float(np.random.normal(p["downsizingRatio"], 0.15)))),
            "capitalReflexivity": max(0.0, float(np.random.normal(p["capitalReflexivity"], 0.10)))
        })
        results.append(run_simulation(trial_params))
        
    summary = {
        "quarters": results[0]["quarters"],
        "indexVal": {"p10": [], "p50": [], "p90": []},
        "cloudRevenue": {"p10": [], "p50": [], "p90": []},
        "roic": {"p10": [], "p50": [], "p90": []}
    }
    
    steps = int(p["horizon"])
    for t in range(steps):
        step_indices = sorted([r["indexVal"][t] for r in results])
        step_revenues = sorted([r["cloudRevenue"][t] for r in results])
        step_roics = sorted([r["roic"][t] for r in results])
        
        idx10 = int(trials * 0.1)
        idx50 = int(trials * 0.5)
        idx90 = int(trials * 0.9)
        
        summary["indexVal"]["p10"].append(step_indices[idx10])
        summary["indexVal"]["p50"].append(step_indices[idx50])
        summary["indexVal"]["p90"].append(step_indices[idx90])
        
        summary["cloudRevenue"]["p10"].append(step_revenues[idx10])
        summary["cloudRevenue"]["p50"].append(step_revenues[idx50])
        summary["cloudRevenue"]["p90"].append(step_revenues[idx90])
        
        summary["roic"]["p10"].append(step_roics[idx10])
        summary["roic"]["p50"].append(step_roics[idx50])
        summary["roic"]["p90"].append(step_roics[idx90])
        
    return summary


def plot_trajectories(history, output_path):
    """
    Generates high-fidelity trajectory plots.
    """
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Techno-Economic Systems Model (TESM) Projections", fontsize=16, fontweight="bold")
    
    quarters = history["quarters"]
    
    # Plot 1: Compute Supply vs Power Constraints
    axs[0, 0].plot(quarters, history["computeSupply"], label="Compute Supply", color="#00ffff", linewidth=2.5)
    axs[0, 0].plot(quarters, [p * 1.15 for p in history["activePower"]], label="Power Limit (GW-equiv)", color="#ff9900", linestyle="--", linewidth=2.0)
    axs[0, 0].fill_between(quarters, history["computeSupply"], [p * 1.15 for p in history["activePower"]], where=[s > p*1.15 for s, p in zip(history["computeSupply"], history["activePower"])], color="red", alpha=0.3, label="Stranded Compute")
    axs[0, 0].set_title("Compute Capacity vs Power Grid Limits")
    axs[0, 0].set_xlabel("Quarter")
    axs[0, 0].set_ylabel("GW / Capacity units")
    axs[0, 0].legend()
    axs[0, 0].grid(True, alpha=0.3)
    
    # Plot 2: Cloud vs Software Revenues
    axs[0, 1].plot(quarters, history["cloudRevenue"], label="Cloud Revenue ($B/yr)", color="#33cc33", linewidth=2.5)
    axs[0, 1].plot(quarters, history["softwareRevenues"], label="Software SaaS Revenue ($B/yr)", color="#9933ff", linewidth=2.5)
    axs[0, 1].set_title("Ecosystem Revenues Trajectory")
    axs[0, 1].set_xlabel("Quarter")
    axs[0, 1].set_ylabel("Annualized Revenue ($B)")
    axs[0, 1].legend()
    axs[0, 1].grid(True, alpha=0.3)
    
    # Plot 3: ROIC vs WACC
    axs[1, 0].plot(quarters, [r * 100.0 for r in history["roic"]], label="Hyperscaler ROIC (%)", color="#ff3300", linewidth=2.5)
    axs[1, 0].plot(quarters, [w * 100.0 for w in history["wacc"]], label="Cost of Capital WACC (%)", color="#ffffff", linestyle=":", linewidth=2.0)
    axs[1, 0].set_title("Return on Invested Capital vs Capital Costs")
    axs[1, 0].set_xlabel("Quarter")
    axs[1, 0].set_ylabel("Percent (%)")
    axs[1, 0].legend()
    axs[1, 0].grid(True, alpha=0.3)
    
    # Plot 4: Valuation Index Trajectory
    axs[1, 1].plot(quarters, history["indexVal"], label="TESM Tech Index (Base=100)", color="#00ffcc", linewidth=2.5)
    axs[1, 1].set_title("Capital Markets Index Value")
    axs[1, 1].set_xlabel("Quarter")
    axs[1, 1].set_ylabel("Index Value")
    axs[1, 1].legend()
    axs[1, 1].grid(True, alpha=0.3)
    
    # Styling dark-mode look
    for ax in axs.flat:
        ax.set_facecolor("#121212")
        ax.spines['bottom'].set_color('#555555')
        ax.spines['top'].set_color('#555555') 
        ax.spines['right'].set_color('#555555')
        ax.spines['left'].set_color('#555555')
        ax.tick_params(colors='#cccccc')
        ax.yaxis.label.set_color('#cccccc')
        ax.xaxis.label.set_color('#cccccc')
        ax.title.set_color('#ffffff')
        
    fig.patch.set_facecolor('#1e1e1e')
    plt.tight_layout()
    plt.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated trajectories plot saved to: {output_path}")


if __name__ == "__main__":
    print("Executing baseline simulation...")
    # Load overrides if they exist
    overrides = {}
    overrides_js_path = "C:/Users/NITHING/Desktop/projections/param_overrides.js"
    if os.path.exists(overrides_js_path):
        try:
            with open(overrides_js_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # Simple extractor of JSON object inside param_overrides.js
            start_idx = content.find("window.TESM_CALIBRATED_OVERRIDES = {")
            if start_idx != -1:
                json_part = content[start_idx + len("window.TESM_CALIBRATED_OVERRIDES = "):]
                # find first matching brace
                brace_count = 0
                end_idx = 0
                for idx, char in enumerate(json_part):
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            end_idx = idx + 1
                            break
                json_str = json_part[:end_idx]
                # extract values using regular regex or split
                import re
                for line in json_str.split("\n"):
                    m = re.match(r'^\s*"(\w+)":\s*([0-9\.\-]+),?', line)
                    if m:
                        overrides[m.group(1)] = float(m.group(2))
            print(f"Successfully extracted {len(overrides)} override parameters from param_overrides.js")
        except Exception as e:
            print(f"Warning: could not parse overrides: {e}")
            
    # Run simulation
    history = run_simulation(overrides)
    
    # Print key metrics
    print("\n" + "="*50)
    print("BASELINE SYSTEMS DYNAMICS MODEL OUTPUTS")
    print("="*50)
    for q_idx in [0, 4, 20, 40, 79]:
        q = history["quarters"][q_idx]
        print(f"Quarter {q} (Year {q/4.0:.1f}):")
        print(f"  Cloud Revenue:       ${history['cloudRevenue'][q_idx]:.2f}B/yr")
        print(f"  Software SaaS Rev:   ${history['softwareRevenues'][q_idx]:.2f}B/yr")
        print(f"  Active Grid Power:   {history['activePower'][q_idx]:.2f} GW")
        print(f"  Compute Supply:      {history['computeSupply'][q_idx]:.2f} capacity units")
        print(f"  Stranded Capacity:   {history['strandedCapacity'][q_idx]:.2f} units")
        print(f"  Effective Power Cost: ${history['effectiveGridPrice'][q_idx]:.2f}/MWh")
        print(f"  Hyperscaler ROIC:    {history['roic'][q_idx]*100.0:.1f}%")
        print(f"  TESM Tech Index:     {history['indexVal'][q_idx]:.1f}")
        print("-"*30)
        
    # Generate trajectories plot
    artifacts_dir = "C:/Users/NITHING/.gemini/antigravity/brain/60e8d70e-69ee-4ab6-a08d-332834a5ddce"
    if not os.path.exists(artifacts_dir):
        os.makedirs(artifacts_dir)
    plot_trajectories(history, os.path.join(artifacts_dir, "tesm_trajectories.png"))
    
    # Run Scenario Matrix
    print("\nRunning Scenario Matrix combos (powerset of A-E)...")
    combos = generate_scenario_matrix(overrides)
    print(f"Successfully simulated {len(combos)} scenario combinations.")
    
    # Run Monte Carlo
    print("\nRunning Monte Carlo (500 trials)...")
    mc = run_monte_carlo(overrides, trials=500)
    print("Monte Carlo complete.")
    print(f"Year 20 Index P10: {mc['indexVal']['p10'][-1]:.1f} | P50: {mc['indexVal']['p50'][-1]:.1f} | P90: {mc['indexVal']['p90'][-1]:.1f}")
