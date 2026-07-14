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
    """
    merged = dict(DEFAULT_PARAMS)
    if params:
        merged.update(params)
        
    region_config = REGIONS.get(merged["activeRegion"], REGIONS["us"])
    industry_config = INDUSTRIES.get(merged["activeIndustry"], INDUSTRIES["software"])
    
    power_growth_cap = merged["powerGrowthCap"] * (region_config["powerGrowthCap"] / 0.12)
    grid_connection_delay = max(1, int(round(merged["gridConnectionDelay"] * (region_config["gridConnectionDelay"] / 6.0))))
    ppp_adjustment = merged["pppAdjustment"] * region_config["ppp"]
    
    dt = 0.25  # quarter steps
    steps = int(merged["horizon"])
    
    compute_supply = merged.get("initialComputeSupply", 10.0)
    active_power = merged.get("initialPower", 5.0)
    software_revenues = merged.get("initialSoftwareRevenues", 4.0)
    cloud_revenue = merged.get("initialCloudRevenue", 8.0)
    unamortized_capex = merged.get("initialCapEx", 15.0)
    investor_sentiment = 1.0
    silicon_supply = merged.get("initialSilicon", 12.0)
    
    contract_queue_3yr = [0.0] * steps
    contract_queue_5yr = [0.0] * steps
    power_queue = [0.0] * steps
    gpu_delivery_queue = [0.0] * steps
    
    len_short = int(merged["averageContractLength"])
    len_long = int(round(merged["averageContractLength"] * 1.67))
    
    for i in range(steps):
        if "realContractSeed" in merged and merged["realContractSeed"] is not None and i in merged["realContractSeed"]:
            contract_queue_3yr[i] = merged["realContractSeed"][i].get("q3yr", 0.0)
            contract_queue_5yr[i] = merged["realContractSeed"][i].get("q5yr", 0.0)
        else:
            historical_cloud_spend = cloud_revenue * (1.0 + 0.04 * i)
            contract_queue_3yr[i] = (historical_cloud_spend * merged["contractMix3yr"]) / len_short
            contract_queue_5yr[i] = (historical_cloud_spend * (1.0 - merged["contractMix3yr"])) / len_long
        power_queue[i] = 0.15
        gpu_delivery_queue[i] = 0.5
        
    history = {
        "quarters": [],
        "computeSupply": [],
        "activePower": [],
        "strandedCapacity": [],
        "cloudRevenue": [],
        "softwareRevenues": [],
        "netEnterpriseROI": [],
        "roic": [],
        "wacc": [],
        "marketValuation": [],
        "indexVal": [],
        "multipleSales": [],
        "revenueQualityHigh": [],
        "revenueQualityLow": [],
        "gdpBoost": [],
        "siliconSupply": [],
        "onsiteGenCapacityMW": [],
        "onsiteDispatch": [],
        "onsiteFuelCost": [],
        "onsiteNetCost": [],
        "effectiveGridPrice": [],
        "carbonCost": [],
        "gridServicesRevenue": [],
        "waterIntensity": []
    }
    
    initial_valuation = None
    
    for t in range(steps):
        # 1. Physical Grid Capacity Constraints
        merged["computeDemandMW"] = active_power * 1000.0
        
        construction_delay_multiplier = 1.0 + merged["transformerShortage"] * 1.5
        region_speed_factor = region_config["powerGrowthCap"] / 0.12
        base_power_growth_cap = min(power_growth_cap, (0.20 * region_speed_factor) / construction_delay_multiplier)
        
        effective_power_growth_cap = base_power_growth_cap + (
            (merged["onsiteGenCapacityMW"] / (merged["computeDemandMW"] or 10000.0)) * merged["ONSITE_UTILIZATION_BONUS"]
        )
        
        grid_arrival = power_queue[t] if t < len(power_queue) else 0.04
        active_power += grid_arrival
        
        power_target_build = cloud_revenue * 0.10 * investor_sentiment
        grid_target_index = t + grid_connection_delay
        if grid_target_index < steps:
            power_queue[grid_target_index] = min(
                power_target_build * dt, 
                active_power * effective_power_growth_cap * dt
            )
            
        # 2. Semiconductor Wafer Caps & Lead times
        effective_silicon_cap = silicon_supply * (1.0 - merged["hbmBottleneck"])
        silicon_supply += (0.15 * investor_sentiment - 0.05 * silicon_supply) * dt
        
        gpu_lead_time = 4
        gpu_order = min(cloud_revenue * 0.30 * investor_sentiment, effective_silicon_cap)
        if t + gpu_lead_time < steps:
            gpu_delivery_queue[t + gpu_lead_time] = gpu_order * dt
            
        compute_additions = gpu_delivery_queue[t] if t < len(gpu_delivery_queue) else 0.2
        compute_supply += compute_additions
        
        # 3. Stranded Capacity Impairment
        max_compute_with_power = active_power * 1.15
        stranded_capacity = max(0.0, compute_supply - max_compute_with_power)
        active_compute = compute_supply - stranded_capacity
        active_compute_fraction = active_compute / (compute_supply + 0.1)
        
        # 4. Onsite Power Economics Model (§34 unit corrections)
        onsite_dispatch = min(
            merged["onsiteGenCapacityMW"] * merged["onsiteCapacityFactor"],
            merged["computeDemandMW"] * (1.0 - merged["gridImportFraction"])
        )
        
        onsite_fuel_cost = 0.0
        for tech, frac in merged["onsiteGenMix"].items():
            cap = merged["onsiteGenCapacityMW"] * frac
            hr = merged["HEAT_RATES_BTU_PER_KWH"].get(tech, 0.0)
            
            if tech in ["gas_turbine", "rice", "bloom_sofc"]:
                fuel_type = "natural_gas"
            elif tech == "hydrogen_fc":
                fuel_type = "hydrogen"
            else:
                fuel_type = "natural_gas"
                
            fuel_price = merged["FUEL_PRICES_USD_PER_MMBTU"].get(fuel_type, 0.0)
            hedged = fuel_price * merged["hedgeRatio"] + fuel_price * (1.0 - merged["hedgeRatio"]) * (1.0 + merged["basisRisk"])
            
            # cap (MW) * capacityFactor * hours/qtr * hr/1000 (MMBtu/MWh) * hedged ($/MMBtu)
            onsite_fuel_cost += cap * merged["onsiteCapacityFactor"] * 2190.0 * (hr / 1000.0) * hedged
            
        carbon_cost = onsite_dispatch * 2190.0 * merged["carbonIntensityTonCO2perMWh"] * merged["carbonPrice"]
        grid_services_rev = merged["onsiteGenCapacityMW"] * merged["gridServicesRevenue"] / 4.0
        onsite_net_cost = onsite_fuel_cost + carbon_cost - grid_services_rev
        
        effective_grid_price = merged["gridPowerPrice"] * merged["gridImportFraction"] + (
            onsite_net_cost / max(1.0, onsite_dispatch * 2190.0)
        ) * (1.0 - merged["gridImportFraction"])
        
        if onsite_net_cost < merged["gridPowerPrice"] * (onsite_dispatch * 2190.0) * merged["gridDefectionThreshold"]:
            merged["onsiteGenCapacityMW"] += merged["NEW_ONSITE_BUILD_RATE"]
            
        # 5. Jevons Paradox & Pricing Elasticity Model
        cost_reduction_rate = 0.38
        open_source_pressure = merged["priceCompression"] * merged["openSourcePower"]
        token_price = max(0.005, math.pow(1.0 - (cost_reduction_rate + open_source_pressure) * dt, t))
        
        volume_expansion = math.pow(1.0 / token_price, merged["elasticityCoefficient"] - 1.0)
        demand_volume = active_compute * volume_expansion
        
        # 6. Compliance friction, TCO Multiplier & Adoptions
        base_savings = demand_volume * 0.25
        tco_cost = demand_volume * (
            industry_config["complianceCost"] * merged["tcoMultiplier"] + 
            industry_config["liabilityRisk"] * 0.4
        )
        net_savings = base_savings - tco_cost
        
        regulatory_friction_coeff = 1.0 + (merged["complianceFriction"] + industry_config["complianceCost"]) * 3.0
        adoption_rate = max(0.01, (0.20 if net_savings > 0 else 0.01) / regulatory_friction_coeff)
        
        external_financing_available = investor_sentiment if investor_sentiment > 0.60 else 0.0
        insolvency_ramp = min(1.0, max(0.0, (0.60 - investor_sentiment) / 0.25))
        insolvency_writedown = (
            software_revenues * merged["insolvencyWriteDownRate"] * insolvency_ramp 
            if external_financing_available == 0.0 else 0.0
        )
        
        if net_savings > 0:
            software_revenues += (net_savings * adoption_rate - merged["adoptionDecayRate"] * software_revenues - insolvency_writedown) * dt
        else:
            cancellation_rate = merged["adoptionDecayRate"] + min(0.20, -net_savings / (cloud_revenue + 0.1))
            software_revenues += (-cancellation_rate * software_revenues - insolvency_writedown) * dt
            
        software_revenues = max(0.0, software_revenues)
        gdp_growth_pct = min(0.04, (software_revenues * 0.005) * ppp_adjustment)
        
        # 7. Multi-Tier Contract renewals & cloud bookings
        net_roi = software_revenues / (cloud_revenue + 0.1)
        cloud_demand_target = software_revenues * 0.65
        new_bookings = cloud_demand_target * dt
        new_bookings_3yr = new_bookings * merged["contractMix3yr"]
        new_bookings_5yr = new_bookings * (1.0 - merged["contractMix3yr"])
        
        expiring_3yr = contract_queue_3yr[t] if t < len(contract_queue_3yr) else 0.1
        expiring_5yr = contract_queue_5yr[t] if t < len(contract_queue_5yr) else 0.05
        
        renewal_multiplier = 0.96
        if net_roi < merged["wacc"]:
            renewal_multiplier = max(0.30, 1.0 - merged["downsizingRatio"])
            
        renewed_3yr = expiring_3yr * renewal_multiplier
        renewed_5yr = expiring_5yr * renewal_multiplier
        
        if t + len_short < steps:
            contract_queue_3yr[t + len_short] = (new_bookings_3yr + renewed_3yr) / len_short
        if t + len_long < steps:
            contract_queue_5yr[t + len_long] = (new_bookings_5yr + renewed_5yr) / len_long
            
        cloud_revenue += (new_bookings - (expiring_3yr + expiring_5yr) + (renewed_3yr + renewed_5yr)) * dt
        cloud_revenue = max(0.0, cloud_revenue)
        
        # 8. Financial returns (ROIC)
        state_subsidy = 0.8 * merged["nationalStrategicInvestment"] * dt
        hardware_capex = cloud_revenue * (0.26 + 0.12 * investor_sentiment) * dt + state_subsidy
        unamortized_capex += hardware_capex
        
        amortization = unamortized_capex * 0.0625
        unamortized_capex -= amortization
        
        stranded_impairment = stranded_capacity * 0.12 * dt
        ebitda = cloud_revenue * 0.44
        operating_profit = ebitda - amortization - stranded_impairment
        invested_capital = max(10.0, unamortized_capex + active_power * 2.0)
        roic = operating_profit / invested_capital
        
        # 9. Capital Market Sentiment loops
        qtr_growth = (
            (cloud_revenue / history["cloudRevenue"][t - 4] - 1.0) 
            if (t >= 4 and len(history["cloudRevenue"]) >= 4 and history["cloudRevenue"][t - 4] > 0.0)
            else (math.pow(cloud_revenue / history["cloudRevenue"][0], 1.0 / (t * dt)) - 1.0 if (t > 0 and history["cloudRevenue"][0] > 0.0) else 0.15)
        )
        
        reflexivity_boost = merged["capitalReflexivity"] * (investor_sentiment - 1.0) * dt
        sentiment_speed = merged.get("sentimentSpeed", 1.0)
        max_sentiment = merged.get("maxSentiment", 1.6)
        
        if roic > merged["wacc"] and qtr_growth > 0.12:
            investor_sentiment = min(max_sentiment, investor_sentiment + (0.06 + reflexivity_boost) * sentiment_speed * dt)
        else:
            sentiment_decay = merged.get("sentimentDecay", 0.15)
            investor_sentiment = max(0.35, investor_sentiment - sentiment_decay * sentiment_speed * dt)
            
        multiple_sales = max(
            merged["targetMultipleSales"],
            merged["baseMultipleSales"] * investor_sentiment * (1.0 + max(-0.4, qtr_growth))
        )
        
        market_valuation = cloud_revenue * multiple_sales
        if t == 0:
            initial_valuation = market_valuation
            
        seasonality_cycle = merged.get("seasonalityCycle", 0.0)
        cycle_val = 1.0 + seasonality_cycle * math.sin(2.0 * math.pi * (t / 4.0) - math.pi / 3.0)
        index_val = merged["initialIndex"] * (market_valuation / (initial_valuation or 1.0)) * cycle_val
        
        # 10. Revenue Quality Tiering
        quality_coeff = min(0.90, max(0.20, net_roi * industry_config["switchingCost"]))
        rev_quality_high = cloud_revenue * quality_coeff
        rev_quality_low = cloud_revenue * (1.0 - quality_coeff)
        
        # Log to History
        history["quarters"].append(t)
        history["computeSupply"].append(compute_supply)
        history["activePower"].append(active_power)
        history["strandedCapacity"].append(stranded_capacity)
        history["cloudRevenue"].append(cloud_revenue)
        history["softwareRevenues"].append(software_revenues)
        history["netEnterpriseROI"].append(net_roi)
        history["roic"].append(roic)
        history["wacc"].append(merged["wacc"])
        history["marketValuation"].append(market_valuation)
        history["indexVal"].append(index_val)
        history["multipleSales"].append(multiple_sales)
        history["revenueQualityHigh"].append(rev_quality_high)
        history["revenueQualityLow"].append(rev_quality_low)
        history["gdpBoost"].append(gdp_growth_pct * 100.0)
        history["siliconSupply"].append(silicon_supply)
        history["onsiteGenCapacityMW"].append(merged["onsiteGenCapacityMW"])
        history["onsiteDispatch"].append(onsite_dispatch)
        history["onsiteFuelCost"].append(onsite_fuel_cost)
        history["onsiteNetCost"].append(onsite_net_cost)
        history["effectiveGridPrice"].append(effective_grid_price)
        history["carbonCost"].append(carbon_cost)
        history["gridServicesRevenue"].append(grid_services_rev)
        history["waterIntensity"].append(merged["waterIntensityLperMWh"])
        
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
    combinations = {"baseline": run_simulation(scenario_defs["baseline"])}
    
    base_params = dict(params) if params else {}
    
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
