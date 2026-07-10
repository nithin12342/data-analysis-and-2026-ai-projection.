import json
import numpy as np
import pandas as pd

# Load the reconciled parameters (v3.0)
overrides = {
    "gridConnectionDelay": 10,
    "powerGrowthCap": 0.43,
    "transformerShortage": 0.29,
    "downsizingRatio": 0.60,
    "siliconSupply": 205.66,
    "wacc": 0.085,
    "capitalReflexivity": 0.26
}

# Baseline default parameters
DEFAULT_PARAMS = {
    "horizon": 80,
    "wacc": 0.085,
    "initialIndex": 100,
    "tcoMultiplier": 1.5,
    "complianceFriction": 0.15,
    "pppAdjustment": 0.65,
    "priceCompression": 0.45,
    "openSourcePower": 0.60,
    "powerGrowthCap": 0.12,
    "gridConnectionDelay": 6,
    "transformerShortage": 0.20,
    "hbmBottleneck": 0.15,
    "averageContractLength": 12,
    "downsizingRatio": 0.35,
    "contractMix3yr": 0.70,
    "baseMultipleSales": 8.0,
    "targetMultipleSales": 3.5,
    "elasticityCoefficient": 1.25,
    "adoptionDecayRate": 0.03,
    "capitalReflexivity": 0.30,
    "nationalStrategicInvestment": 1.5,
    "siliconSupply": 12.0,
    "insolvencyWriteDownRate": 0.0
}

# Merge calibrated parameters
params = {**DEFAULT_PARAMS, **overrides}

def run_simulation_python(p):
    dt = 0.25
    steps = p["horizon"]
    
    # Regional scaling
    powerGrowthCap = p["powerGrowthCap"]
    gridConnectionDelay = p["gridConnectionDelay"]
    
    # State variables
    computeSupply = 10.0
    activePower = 5.0
    softwareRevenues = 4.0
    cloudRevenue = 8.0
    unamortizedCapEx = 15.0
    investorSentiment = 1.0
    siliconSupply = p["siliconSupply"]
    
    # Dynamic contract lengths (aligned with engine.js v3.0 logic)
    lenShort = int(p["averageContractLength"])
    lenLong = int(round(p["averageContractLength"] * 1.67))
    
    # Initialize queues
    contractQueue3yr = [0.0] * steps
    contractQueue5yr = [0.0] * steps
    powerQueue = [0.0] * steps
    gpuDeliveryQueue = [0.0] * steps
    
    for i in range(steps):
        if p.get("realContractSeed") and p["realContractSeed"][i] is not None:
            # Use real SEC RPO-derived expiration schedule if supplied
            contractQueue3yr[i] = p["realContractSeed"][i]["q3yr"]
            contractQueue5yr[i] = p["realContractSeed"][i]["q5yr"]
        else:
            historicalCloudSpend = cloudRevenue * (1 + 0.04 * i)
            contractQueue3yr[i] = (historicalCloudSpend * p["contractMix3yr"]) / lenShort
            contractQueue5yr[i] = (historicalCloudSpend * (1 - p["contractMix3yr"])) / lenLong
        powerQueue[i] = 0.15
        gpuDeliveryQueue[i] = 0.5
        
    history = {
        "quarters": [],
        "cloudRevenue": [],
        "softwareRevenues": [],
        "netROI": [],
        "expiring": [],
        "downsized": [],
        "netReduction": [],
        "indexVal": []
    }
    
    initialValuation = None
    
    for t in range(steps):
        # 1. Physical Grid constraints
        constructionDelayMultiplier = 1 + p["transformerShortage"] * 1.5
        regionSpeedFactor = p["powerGrowthCap"] / 0.12
        effectivePowerGrowth = min(powerGrowthCap, (0.20 * regionSpeedFactor) / constructionDelayMultiplier)
        
        gridArrival = powerQueue[t] if t < len(powerQueue) else 0.04
        activePower += gridArrival
        
        powerTargetBuild = cloudRevenue * 0.10 * investorSentiment
        gridTargetIndex = t + gridConnectionDelay
        if gridTargetIndex < steps:
            powerQueue[gridTargetIndex] = min(powerTargetBuild * dt, activePower * effectivePowerGrowth * dt)
            
        effectiveSiliconCap = siliconSupply * (1 - p["hbmBottleneck"])
        siliconSupply += (0.15 * investorSentiment - 0.05 * siliconSupply) * dt
        
        gpuLeadTime = 4
        gpuOrder = min(cloudRevenue * 0.30 * investorSentiment, effectiveSiliconCap)
        if t + gpuLeadTime < steps:
            gpuDeliveryQueue[t + gpuLeadTime] = gpuOrder * dt
            
        computeAdditions = gpuDeliveryQueue[t] if t < len(gpuDeliveryQueue) else 0.2
        computeSupply += computeAdditions
        
        maxComputeWithPower = activePower * 1.15
        strandedCapacity = max(0.0, computeSupply - maxComputeWithPower)
        activeCompute = computeSupply - strandedCapacity
        
        # 2. Demand side Jevons pricing
        costReductionRate = 0.38
        openSourcePressure = p["priceCompression"] * p["openSourcePower"]
        tokenPrice = max(0.005, (1 - (costReductionRate + openSourcePressure) * dt) ** t)
        
        volumeExpansion = (1 / tokenPrice) ** (p["elasticityCoefficient"] - 1)
        demandVolume = activeCompute * volumeExpansion
        
        # 3. Compliance and adoption TCO
        baseSavings = demandVolume * 0.25
        tcoCost = demandVolume * (0.10 * p["tcoMultiplier"] + 0.05 * 0.4) # Software defaults
        netSavings = baseSavings - tcoCost
        
        regulatoryFrictionCoeff = 1 + (p["complianceFriction"] + 0.10) * 3
        adoptionRate = max(0.01, (0.20 if netSavings > 0 else 0.01) / regulatoryFrictionCoeff)
        
        # Financing/solvency mechanic: when investor sentiment drops below 0.60,
        # the capital markets IPO/refinancing window closes discontinuously.
        # Unprofitable startups run out of cash and go bankrupt, leading to
        # an additional software subscription revenue write-down of 10% per quarter.
        externalFinancingAvailable = investorSentiment if investorSentiment > 0.60 else 0.0
        insolvencyWriteDown = softwareRevenues * p["insolvencyWriteDownRate"] if externalFinancingAvailable == 0.0 else 0.0

        # CRITICAL FIX 3: Accelerated dis-adoption/cancellation when netSavings is negative
        if netSavings > 0:
            softwareRevenues += (netSavings * adoptionRate - p["adoptionDecayRate"] * softwareRevenues - insolvencyWriteDown) * dt
        else:
            cancellationRate = p["adoptionDecayRate"] + min(0.20, -netSavings / (cloudRevenue + 0.1))
            softwareRevenues += (netSavings * adoptionRate - cancellationRate * softwareRevenues - insolvencyWriteDown) * dt
            
        softwareRevenues = max(0.0, softwareRevenues)
        netROI = softwareRevenues / (cloudRevenue + 0.1)

        
        # 4. Contracts renewal lag
        expiring3yr = contractQueue3yr[t] if t < len(contractQueue3yr) else 0.1
        expiring5yr = contractQueue5yr[t] if t < len(contractQueue5yr) else 0.05
        total_expiring = expiring3yr + expiring5yr
        
        renewalMultiplier = 0.96
        is_downsized = False
        if netROI < p["wacc"]:
            renewalMultiplier = max(0.30, 1.0 - p["downsizingRatio"])
            is_downsized = True
            
        renewed3yr = expiring3yr * renewalMultiplier
        renewed5yr = expiring5yr * renewalMultiplier
        
        cloudDemandTarget = softwareRevenues * 0.65
        newBookings = cloudDemandTarget * dt
        newBookings3yr = newBookings * p["contractMix3yr"]
        newBookings5yr = newBookings * (1 - p["contractMix3yr"])
        
        if t + lenShort < steps:
            contractQueue3yr[t + lenShort] = (newBookings3yr + renewed3yr) / lenShort
        if t + lenLong < steps:
            contractQueue5yr[t + lenLong] = (newBookings5yr + renewed5yr) / lenLong
            
        downsizing_reduction = total_expiring * (1.0 - renewalMultiplier) * dt
        
        cloudRevenue = cloudRevenue + (newBookings - total_expiring + (renewed3yr + renewed5yr)) * dt
        
        # Update CapEx & Amortization to compute ROIC state
        stateSubsidy = 0.8 * p["nationalStrategicInvestment"] * dt
        hardwareCapEx = cloudRevenue * (0.26 + 0.12 * investorSentiment) * dt + stateSubsidy
        unamortizedCapEx += hardwareCapEx
        
        amortization = unamortizedCapEx * 0.0625
        unamortizedCapEx -= amortization
        
        ebitda = cloudRevenue * 0.44
        strandedImpairment = strandedCapacity * 0.12 * dt
        operatingProfit = ebitda - amortization - strandedImpairment
        investedCapital = max(10.0, unamortizedCapEx + activePower * 2.0)
        roic = operatingProfit / investedCapital
        
        # Sentiment feedback loop
        qtrGrowth = 0.15
        if t > 0:
            if t >= 4:
                qtrGrowth = (cloudRevenue / history["cloudRevenue"][t - 4]) - 1
            else:
                qtrGrowth = ((cloudRevenue / history["cloudRevenue"][0]) ** (1 / (t * dt))) - 1
                
        reflexivityBoost = p["capitalReflexivity"] * (investorSentiment - 1) * dt
        if roic > p["wacc"] and qtrGrowth > 0.12:
            investorSentiment = min(1.6, investorSentiment + (0.06 + reflexivityBoost) * dt)
        else:
            investorSentiment = max(0.35, investorSentiment - 0.15 * dt)
            
        # Market index logic
        multipleSales = max(p["targetMultipleSales"], p["baseMultipleSales"] * investorSentiment * (1 + max(-0.4, qtrGrowth)))
        marketValuation = cloudRevenue * multipleSales
        if t == 0:
            initialValuation = marketValuation
        indexVal = p["initialIndex"] * (marketValuation / initialValuation)
        
        # Write history
        history["quarters"].append(t)
        history["cloudRevenue"].append(cloudRevenue)
        history["softwareRevenues"].append(softwareRevenues)
        history["netROI"].append(netROI)
        history["expiring"].append(total_expiring * dt) 
        history["downsized"].append(is_downsized)
        history["netReduction"].append(downsizing_reduction)
        history["indexVal"].append(indexVal)
        
    return history

# Run model
history = run_simulation_python(params)

# Convert to DataFrame
df = pd.DataFrame(history)
df['year'] = (df['quarters'] // 4) + 1
df['quarter_of_year'] = (df['quarters'] % 4) + 1
df['date_label'] = df.apply(lambda r: f"Year {int(r['year'])} Q{int(r['quarter_of_year'])}", axis=1)

# Find period of maximum contract expiration
max_exp_idx = df['expiring'].idxmax()
max_exp_row = df.loc[max_exp_idx]

# Find period of maximum downsizing reduction hit
max_hit_idx = df['netReduction'].idxmax()
max_hit_row = df.loc[max_hit_idx]

# Calculate summary stats
total_expiring_sum = df['expiring'].sum()
total_reduction_sum = df['netReduction'].sum()

print("=== CONTRACT EXPIRATION & DOWNSIZING CLINICAL AUDIT (v3.0) ===")
print(f"Total Expiring Contracts Volume over 20-Year Horizon: ${total_expiring_sum:.2f} Billion")
print(f"Total Downsizing Contract Hit (Reduced Volume):       ${total_reduction_sum:.2f} Billion")
print(f"Net Downsizing Impact (Overall Waste Ratio):          {round((total_reduction_sum / total_expiring_sum) * 100, 1)}%")

print("\n--- MAJORITY EXPIRATION PERIOD ---")
print(f"Peak Expirations Quarter:       {max_exp_row['date_label']} (Step {int(max_exp_row['quarters'])})")
print(f"Peak Quarterly Expiring Volume: ${max_exp_row['expiring']:.2f} Billion")

print("\n--- MAXIMUM DOWNSIZING HIT PERIOD ---")
print(f"Peak Downsizing Hit Quarter:    {max_hit_row['date_label']} (Step {int(max_hit_row['quarters'])})")
print(f"Peak Quarterly Revenue Drop:    -${max_hit_row['netReduction']:.2f} Billion")
print(f"Enterprise ROI at Peak Hit:     {round(max_hit_row['netROI']*100, 1)}% (WACC: {params['wacc']*100}%)")

print("\n--- DETAILED QUARTERLY CHRONOLOGY OF THE HIT ---")
hit_df = df[df['netReduction'] > 0][['date_label', 'quarters', 'expiring', 'netReduction', 'netROI', 'cloudRevenue']]
print(hit_df.to_string(index=False, formatters={
    'expiring': lambda x: f"${x:.2f}B",
    'netReduction': lambda x: f"-${x:.2f}B",
    'netROI': lambda x: f"{x*100:.1f}%",
    'cloudRevenue': lambda x: f"${x:.2f}B"
}))
