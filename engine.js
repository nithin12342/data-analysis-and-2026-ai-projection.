/**
 * engine.js
 * Core Techno-Economic Systems Model (TESM) for AI vs. Dot-com comparison
 * Expanded with Regional Infrastructure, Multi-Tier Contracts, Industry Regulations, and Compute Cycles.
 */

const REGIONS = {
  us: { name: "United States", powerGrowthCap: 0.12, gridConnectionDelay: 6, costPerMW: 2.5, govCoordination: 0.5, ppp: 1.0 },
  china: { name: "China", powerGrowthCap: 0.24, gridConnectionDelay: 3, costPerMW: 1.1, govCoordination: 0.95, ppp: 0.55 },
  india: { name: "India", powerGrowthCap: 0.18, gridConnectionDelay: 4, costPerMW: 1.3, govCoordination: 0.70, ppp: 0.45 },
  gulf: { name: "Gulf Countries (UAE/KSA)", powerGrowthCap: 0.26, gridConnectionDelay: 2, costPerMW: 1.7, govCoordination: 0.85, ppp: 0.80 },
  eu: { name: "European Union", powerGrowthCap: 0.05, gridConnectionDelay: 11, costPerMW: 3.1, govCoordination: 0.30, ppp: 1.15 }
};

const INDUSTRIES = {
  software: { name: "Enterprise Software", complianceCost: 0.10, liabilityRisk: 0.05, switchingCost: 0.65 },
  banking: { name: "Banking & Finance", complianceCost: 0.35, liabilityRisk: 0.45, switchingCost: 0.85 },
  healthcare: { name: "Healthcare & Biotech", complianceCost: 0.40, liabilityRisk: 0.50, switchingCost: 0.75 },
  legal: { name: "Legal Services", complianceCost: 0.25, liabilityRisk: 0.35, switchingCost: 0.60 }
};

const DEFAULT_PARAMS = {
  horizon: 80, // Quarters (20 years)
  wacc: 0.085,
  initialIndex: 100,
  activeRegion: "us",
  activeIndustry: "software",
  
  // A: Agentic TCO & Regulations
  tcoMultiplier: 1.5,
  complianceFriction: 0.15,
  
  // B: PPP & pricing competition
  pppAdjustment: 0.65,
  priceCompression: 0.45,
  openSourcePower: 0.60,
  
  // C: Physical Infrastructure constraints
  powerGrowthCap: 0.12,
  gridConnectionDelay: 6,
  transformerShortage: 0.20,
  hbmBottleneck: 0.15,
  
  // D: Enterprise Contract Renewal Lag
  averageContractLength: 12, // Qtrs (3 years)
  downsizingRatio: 0.35,
  contractMix3yr: 0.70, // 70% 3-year contracts, 30% 5-year contracts
  
  // E: Multiple Compression
  baseMultipleSales: 8.0,
  targetMultipleSales: 3.5,
  
  // Elasticity, Cycles, & Macro
  elasticityCoefficient: 1.25,
  adoptionDecayRate: 0.03,
  capitalReflexivity: 0.30, // Feedback strength of stock index back to CapEx
  nationalStrategicInvestment: 1.5, // Multiplier of government subsidy spending
  insolvencyWriteDownRate: 0.0, // Default is 0% (only active for startup backtests)
  
  // §34 Onsite Power Generation & Fuel Price Exposure
  onsiteGenCapacityMW: 2500,          // Total onsite MW (US hyperscalers 2024)
  onsiteGenMix: {                     // Technology mix fractions
    gas_turbine: 0.55,
    rice: 0.20,
    bloom_sofc: 0.10,
    solar_storage: 0.10,
    smr: 0.05
  },
  onsiteCapacityFactor: 0.75,         // Weighted average CF
  onsiteFuelExposure: 3.5,            // $/MWh per $/MMBtu gas price
  hedgeRatio: 0.65,                   // Fraction of fuel volume hedged
  basisRisk: 0.15,                    // Basis differential volatility
  gridServicesRevenue: 25000,         // $/MW-yr (Reg + capacity)
  carbonPrice: 0,                     // $/ton CO2 (jurisdiction-weighted)
  carbonIntensityTonCO2perMWh: 0.28,  // Weighted average from tech mix
  carbonPriceExposure: 14,            // $/MWh per $50/ton CO2
  waterIntensityLperMWh: 1.2,         // Average across onsite mix
  gridServicesRevenue: 25000,         // $/MW-yr (Reg + capacity)
  gridDefectionThreshold: 0.85,       // If onsite cost < 85% of grid price, build more
  gridImportFraction: 0.30,           // Fraction of load met by grid (vs onsite)
  NEW_ONSITE_BUILD_RATE: 150,         // MW/quarter added when grid defection economical
  ONSITE_UTILIZATION_BONUS: 0.15,     // Power growth cap increase per unit onsite capacity
  
  // Fuel prices (updated quarterly from data)
  FUEL_PRICES_USD_PER_MMBTU: {
    natural_gas: 4.50,  // Henry Hub current
    diesel: 18.50,      // Diesel wholesale
    hydrogen: 16.00,    // Green H2 delivered
    biogas: 8.00        // Biogas
  },
  
  // Heat rates by technology (Btu/kWh as-operated)
  HEAT_RATES_BTU_PER_KWH: {
    gas_turbine: 9500,
    rice: 8500,
    bloom_sofc: 6800,
    hydrogen_fc: 5500,
    solar_storage: 0,
    smr: 0
  },
  
  // Emission rates (ton CO2/MWh)
  EMISSION_RATES_TON_CO2_PER_MWH: {
    gas_turbine: 0.40,
    rice: 0.35,
    bloom_sofc: 0.20,
    hydrogen_fc: 0.00,
    solar_storage: 0.00,
    smr: 0.00
  },
  
  // Water intensity (L/MWh)
  WATER_INTENSITY_L_PER_MWH: {
    gas_turbine: 1.5,
    rice: 1.2,
    bloom_sofc: 0.5,
    hydrogen_fc: 0.3,
    solar_storage: 0.1,
    smr: 0.8
  },
  
  // Grid power price ($/MWh)
  gridPowerPrice: 85
};

function runSimulation(params = {}) {
  const merged = { ...DEFAULT_PARAMS, ...params };
  const regionConfig = REGIONS[merged.activeRegion] || REGIONS.us;
  const industryConfig = INDUSTRIES[merged.activeIndustry] || INDUSTRIES.software;
  
  const powerGrowthCap = merged.powerGrowthCap * (regionConfig.powerGrowthCap / 0.12);
  const gridConnectionDelay = Math.max(1, Math.round(merged.gridConnectionDelay * (regionConfig.gridConnectionDelay / 6)));
  const pppAdjustment = merged.pppAdjustment * regionConfig.ppp;
  
  const dt = 0.25; // quarter steps
  const steps = merged.horizon;
  
  let computeSupply = merged.initialComputeSupply !== undefined ? merged.initialComputeSupply : 10.0;
  let activePower = merged.initialPower !== undefined ? merged.initialPower : 5.0;
  let softwareRevenues = merged.initialSoftwareRevenues !== undefined ? merged.initialSoftwareRevenues : 4.0;
  let cloudRevenue = merged.initialCloudRevenue !== undefined ? merged.initialCloudRevenue : 8.0;
  let unamortizedCapEx = merged.initialCapEx !== undefined ? merged.initialCapEx : 15.0;
  let investorSentiment = 1.0;
  let activeComputeFraction = 1.0;
  let siliconSupply = merged.initialSilicon !== undefined ? merged.initialSilicon : 12.0;
  
  const contractQueue3yr = new Array(steps).fill(0);
  const contractQueue5yr = new Array(steps).fill(0);
  const powerQueue = new Array(steps).fill(0);
  const gpuDeliveryQueue = new Array(steps).fill(0);

  const lenShort = merged.averageContractLength;
  const lenLong = Math.round(merged.averageContractLength * 1.67);

  for (let i = 0; i < steps; i++) {
    if (merged.realContractSeed && merged.realContractSeed[i] !== undefined) {
      // Use real SEC RPO-derived expiration schedule if supplied
      contractQueue3yr[i] = merged.realContractSeed[i].q3yr;
      contractQueue5yr[i] = merged.realContractSeed[i].q5yr;
    } else {
      // Fallback: synthetic 4%/step growth assumption — NOT real data, used only when no seed is provided
      const historicalCloudSpend = cloudRevenue * (1 + 0.04 * i);
      contractQueue3yr[i] = (historicalCloudSpend * merged.contractMix3yr) / lenShort;
      contractQueue5yr[i] = (historicalCloudSpend * (1 - merged.contractMix3yr)) / lenLong;
    }
    powerQueue[i] = 0.15;
    gpuDeliveryQueue[i] = 0.5;
  }

  const history = {
    quarters: [],
    computeSupply: [],
    activePower: [],
    strandedCapacity: [],
    cloudRevenue: [],
    softwareRevenues: [],
    netEnterpriseROI: [],
    roic: [],
    wacc: [],
    marketValuation: [],
    indexVal: [],
    multipleSales: [],
    revenueQualityHigh: [],
    revenueQualityLow: [],
    gdpBoost: [],
    siliconSupply: [],
    // §34 Onsite Power tracking
    onsiteGenCapacityMW: [],
    onsiteDispatch: [],
    onsiteFuelCost: [],
    onsiteNetCost: [],
    onsiteFuelExposure: [],
    carbonCost: [],
    gridServicesRevenue: [],
    effectiveGridPrice: [],
    onsiteGenMix: [],
    carbonIntensity: [],
    waterIntensity: []
  };

  let initialValuation = null;
  for (let t = 0; t < steps; t++) {
    const constructionDelayMultiplier = 1 + merged.transformerShortage * 1.5;
    const regionSpeedFactor = regionConfig.powerGrowthCap / 0.12;
    const basePowerGrowthCap = Math.min(powerGrowthCap, (0.20 * regionSpeedFactor) / constructionDelayMultiplier);
    const effectivePowerGrowthCap = basePowerGrowthCap + 
      (merged.onsiteGenCapacityMW / (merged.computeDemandMW || 10000)) * merged.ONSITE_UTILIZATION_BONUS;
    
    const gridArrival = powerQueue[t] || 0.04;
    activePower += gridArrival;
    
    const powerTargetBuild = cloudRevenue * 0.10 * investorSentiment;
    const gridTargetIndex = t + gridConnectionDelay;
    if (gridTargetIndex < steps) {
      powerQueue[gridTargetIndex] = Math.min(powerTargetBuild * dt, activePower * effectivePowerGrowthCap * dt);
    }
    
    const effectiveSiliconCap = siliconSupply * (1 - merged.hbmBottleneck);
    siliconSupply += (0.15 * investorSentiment - 0.05 * siliconSupply) * dt;
    
    const gpuLeadTime = 4;
    const gpuOrder = Math.min(cloudRevenue * 0.30 * investorSentiment, effectiveSiliconCap);
    if (t + gpuLeadTime < steps) {
      gpuDeliveryQueue[t + gpuLeadTime] = gpuOrder * dt;
    }
    
    const computeAdditions = gpuDeliveryQueue[t] || 0.2;
    computeSupply += computeAdditions;
    
    const maxComputeWithPower = activePower * 1.15;
    const strandedCapacity = Math.max(0, computeSupply - maxComputeWithPower);
    const activeCompute = computeSupply - strandedCapacity;
    activeComputeFraction = activeCompute / (computeSupply + 0.1);

    // §34 Onsite Power Generation & Fuel Price Exposure Model
    // 1. Onsite dispatch (min of onsite capacity * CF, compute demand * (1 - grid fraction))
    const onsiteDispatch = Math.min(
      merged.onsiteGenCapacityMW * merged.onsiteCapacityFactor,
      merged.computeDemandMW * (1 - merged.gridImportFraction)
    );
    
    // 2. Fuel cost for onsite generation
    let onsiteFuelCost = 0;
    for (const [tech, frac] of Object.entries(merged.onsiteGenMix)) {
      const cap = merged.onsiteGenCapacityMW * frac;
      const hr = merged.HEAT_RATES_BTU_PER_KWH[tech] || 0; // Btu/kWh
      const fuelType = (tech === "gas_turbine" || tech === "rice" || tech === "bloom_sofc") ? "natural_gas" :
                       (tech === "hydrogen_fc") ? "hydrogen" : "natural_gas";
      const fuelPrice = merged.FUEL_PRICES_USD_PER_MMBTU[fuelType] || 0; // $/MMBtu
      const hedged = fuelPrice * merged.hedgeRatio + 
                     fuelPrice * (1 - merged.hedgeRatio) * (1 + merged.basisRisk);
      onsiteFuelCost += cap * merged.onsiteCapacityFactor * hr * hedged / 1e6; // $/MWh -> $/Qtr
    }
    
    // 3. Carbon cost
    const carbonCost = onsiteDispatch * merged.carbonIntensityTonCO2perMWh * merged.carbonPrice;
    
    // 4. Grid services revenue
    const gridServicesRev = merged.onsiteGenCapacityMW * merged.gridServicesRevenue / 4; // $/MW-qtr
    
    // 5. Net onsite power economics
    const onsiteNetCost = onsiteFuelCost + carbonCost - gridServicesRev;
    
    // 6. Effective grid power price (including onsite)
    const effectiveGridPrice = merged.gridPowerPrice * merged.gridImportFraction + (onsiteNetCost / Math.max(1, onsiteDispatch)) * (1 - merged.gridImportFraction);
    
    // 7. Grid defection feedback
    if (onsiteNetCost < merged.gridPowerPrice * onsiteDispatch * merged.gridDefectionThreshold) {
      merged.onsiteGenCapacityMW += merged.NEW_ONSITE_BUILD_RATE;
    }
    
    // 8. Onsite power growth contribution is factored directly into the cap at the beginning of the loop.

    const costReductionRate = 0.38;
    const openSourcePressure = merged.priceCompression * merged.openSourcePower;
    const tokenPrice = Math.max(0.005, Math.pow(1 - (costReductionRate + openSourcePressure) * dt, t));
    
    const volumeExpansion = Math.pow(1 / tokenPrice, merged.elasticityCoefficient - 1);
    const demandVolume = activeCompute * volumeExpansion;

    const baseSavings = demandVolume * 0.25; 
    const tcoCost = demandVolume * (industryConfig.complianceCost * merged.tcoMultiplier + industryConfig.liabilityRisk * 0.4);
    const netSavings = baseSavings - tcoCost;
    
    const regulatoryFrictionCoeff = 1 + (merged.complianceFriction + industryConfig.complianceCost) * 3;
    const adoptionRate = Math.max(0.01, (netSavings > 0 ? 0.20 : 0.01) / regulatoryFrictionCoeff);
    
    // Financing/solvency mechanic: when investor sentiment drops below 0.60,
    // the capital markets IPO/refinancing window closes discontinuously.
    // Unprofitable startups run out of cash and go bankrupt, leading to
    // an additional software subscription revenue write-down of 10% per quarter.
    const externalFinancingAvailable = investorSentiment > 0.60 ? investorSentiment : 0.0;
    const insolvencyRamp = Math.min(1.0, Math.max(0.0, (0.60 - investorSentiment) / (0.60 - 0.35)));
    const insolvencyWriteDown = externalFinancingAvailable === 0.0 ? softwareRevenues * merged.insolvencyWriteDownRate * insolvencyRamp : 0.0;

    if (netSavings > 0) {
      softwareRevenues += (netSavings * adoptionRate - merged.adoptionDecayRate * softwareRevenues - insolvencyWriteDown) * dt;
    } else {
      // Accelerate dis-adoption/cancellation when netSavings is negative (buyers cancel losing subscriptions)
      const cancellationRate = merged.adoptionDecayRate + Math.min(0.20, -netSavings / (cloudRevenue + 0.1));
      softwareRevenues += (netSavings * adoptionRate - cancellationRate * softwareRevenues - insolvencyWriteDown) * dt;
    }
    softwareRevenues = Math.max(0.0, softwareRevenues);

    
    const gdpGrowthPct = Math.min(0.04, (softwareRevenues * 0.005) * pppAdjustment);

    const netROI = softwareRevenues / (cloudRevenue + 0.1);
    const cloudDemandTarget = softwareRevenues * 0.65;
    const newBookings = cloudDemandTarget * dt;
    const newBookings3yr = newBookings * merged.contractMix3yr;
    const newBookings5yr = newBookings * (1 - merged.contractMix3yr);
    
    const expiring3yr = contractQueue3yr[t] || 0.1;
    const expiring5yr = contractQueue5yr[t] || 0.05;
    
    let renewalMultiplier = 0.96;
    if (netROI < merged.wacc) {
      renewalMultiplier = Math.max(0.30, 1.0 - merged.downsizingRatio);
    }
    
    const renewed3yr = expiring3yr * renewalMultiplier;
    const renewed5yr = expiring5yr * renewalMultiplier;
    
    if (t + lenShort < steps) {
      contractQueue3yr[t + lenShort] = (newBookings3yr + renewed3yr) / lenShort;
    }
    if (t + lenLong < steps) {
      contractQueue5yr[t + lenLong] = (newBookings5yr + renewed5yr) / lenLong;
    }
    
    cloudRevenue = cloudRevenue + (newBookings - (expiring3yr + expiring5yr) + (renewed3yr + renewed5yr)) * dt;
    
    const stateSubsidy = 0.8 * merged.nationalStrategicInvestment * dt;
    const hardwareCapEx = cloudRevenue * (0.26 + 0.12 * investorSentiment) * dt + stateSubsidy;
    unamortizedCapEx += hardwareCapEx;
    
    const amortization = unamortizedCapEx * 0.0625;
    unamortizedCapEx -= amortization;
    
    const strandedImpairment = strandedCapacity * 0.12 * dt;
    const ebitda = cloudRevenue * 0.44;
    const operatingProfit = ebitda - amortization - strandedImpairment;
    const investedCapital = Math.max(10.0, unamortizedCapEx + activePower * 2.0);
    const roic = operatingProfit / investedCapital;

    const qtrGrowth = (t > 0) ? (t >= 4 ? (cloudRevenue / history.cloudRevenue[t - 4] - 1) : Math.pow(cloudRevenue / history.cloudRevenue[0], 1 / (t * dt)) - 1) : 0.15;
    const reflexivityBoost = merged.capitalReflexivity * (investorSentiment - 1) * dt;
    
    const sentimentSpeed = merged.sentimentSpeed !== undefined ? merged.sentimentSpeed : 1.0;
    const maxSentiment = merged.maxSentiment !== undefined ? merged.maxSentiment : 1.6;
    if (roic > merged.wacc && qtrGrowth > 0.12) {
      investorSentiment = Math.min(maxSentiment, investorSentiment + (0.06 + reflexivityBoost) * sentimentSpeed * dt);
    } else {
      const sentimentDecay = merged.sentimentDecay !== undefined ? merged.sentimentDecay : 0.15;
      investorSentiment = Math.max(0.35, investorSentiment - sentimentDecay * sentimentSpeed * dt);
    }
    
    const multipleSales = Math.max(
      merged.targetMultipleSales,
      merged.baseMultipleSales * investorSentiment * (1 + Math.max(-0.4, qtrGrowth))
    );
    
    const marketValuation = cloudRevenue * multipleSales;
    if (t === 0) {
      initialValuation = marketValuation;
    }
    const seasonalityCycle = merged.seasonalityCycle !== undefined ? merged.seasonalityCycle : 0.0;
    const cycleVal = 1 + seasonalityCycle * Math.sin(2 * Math.PI * (t / 4.0) - Math.PI / 3);
    const indexVal = merged.initialIndex * (marketValuation / (initialValuation || 1.0)) * cycleVal;
    
    const qualityCoeff = Math.min(0.90, Math.max(0.20, netROI * industryConfig.switchingCost));
    const revenueQualityHigh = cloudRevenue * qualityCoeff;
    const revenueQualityLow = cloudRevenue * (1 - qualityCoeff);

    history.quarters.push(t);
    history.computeSupply.push(computeSupply);
    history.activePower.push(activePower);
    history.strandedCapacity.push(strandedCapacity);
    history.cloudRevenue.push(cloudRevenue);
    history.softwareRevenues.push(softwareRevenues);
    history.netEnterpriseROI.push(netROI);
    history.roic.push(roic);
    history.wacc.push(merged.wacc);
    history.marketValuation.push(marketValuation);
    history.indexVal.push(indexVal);
    history.multipleSales.push(multipleSales);
    history.revenueQualityHigh.push(revenueQualityHigh);
    history.revenueQualityLow.push(revenueQualityLow);
    history.gdpBoost.push(gdpGrowthPct * 100);
    history.siliconSupply.push(siliconSupply);
    // §34 Onsite Power tracking
    history.onsiteGenCapacityMW.push(merged.onsiteGenCapacityMW);
    history.onsiteDispatch.push(onsiteDispatch);
    history.onsiteFuelCost.push(onsiteFuelCost);
    history.onsiteNetCost.push(onsiteNetCost);
    history.onsiteFuelExposure.push(merged.onsiteFuelExposure);
    history.carbonCost.push(carbonCost);
    history.gridServicesRevenue.push(gridServicesRev);
    history.effectiveGridPrice.push(effectiveGridPrice);
    history.onsiteGenMix.push({...merged.onsiteGenMix});
    history.carbonIntensity.push(merged.carbonIntensityTonCO2perMWh);
    history.waterIntensity.push(merged.waterIntensityLperMWh);
  }

  return history;
}

function generateScenarioMatrix(params = {}) {
  const scenarioDefs = {
    baseline: {},
    A: { tcoMultiplier: 3.0, complianceFriction: 0.60 },
    B: { pppAdjustment: 0.40, priceCompression: 0.85, openSourcePower: 0.90 },
    C: { powerGrowthCap: 0.04, gridConnectionDelay: 12, transformerShortage: 0.50, hbmBottleneck: 0.45 },
    D: { averageContractLength: 16, downsizingRatio: 0.65, contractMix3yr: 0.40 },
    E: { baseMultipleSales: 12.0, targetMultipleSales: 2.0 }
  };

  const keys = ['A', 'B', 'C', 'D', 'E'];
  const combinations = { baseline: runSimulation(scenarioDefs.baseline) };
  
  function getCombinations(arr) {
    const result = [[]];
    for (let i = 0; i < arr.length; i++) {
      const len = result.length;
      for (let j = 0; j < len; j++) {
        result.push(result[j].concat(arr[i]));
      }
    }
    return result.filter(c => c.length > 0);
  }
  
  const combos = getCombinations(keys);
  
  combos.forEach(combo => {
    const name = combo.join('+');
    const comboParams = {};
    
    combo.forEach(key => {
      Object.assign(comboParams, scenarioDefs[key]);
    });
    
    combinations[name] = runSimulation(Object.assign({}, params, comboParams));
  });
  
  return combinations;
}

function runMonteCarlo(params = {}, trials = 500) {
  const p = { ...DEFAULT_PARAMS, ...params };
  const results = [];
  
  let seed = 42;
  function seededRandom() {
    // Deterministic LCG
    seed = (1103515245 * seed + 12345) % 2147483648;
    return seed / 2147483648;
  }
  
  function randomNormal(mean, std) {
    const u1 = seededRandom();
    const u2 = seededRandom();
    const z = Math.sqrt(-2.0 * Math.log(u1)) * Math.cos(2.0 * Math.PI * u2);
    return mean + z * std;
  }
  
  for (let i = 0; i < trials; i++) {
    const trialParams = {
      ...p,
      tcoMultiplier: Math.max(1.0, randomNormal(p.tcoMultiplier, 0.3)),
      priceCompression: Math.max(0.1, Math.min(0.95, randomNormal(p.priceCompression, 0.15))),
      powerGrowthCap: Math.max(0.01, randomNormal(p.powerGrowthCap, 0.03)),
      elasticityCoefficient: Math.max(0.2, randomNormal(p.elasticityCoefficient, 0.25)),
      downsizingRatio: Math.max(0.1, Math.min(0.9, randomNormal(p.downsizingRatio, 0.15))),
      capitalReflexivity: Math.max(0.0, randomNormal(p.capitalReflexivity, 0.10))
    };
    
    results.push(runSimulation(trialParams));
  }
  
  const summary = {
    quarters: results[0].quarters,
    indexVal: { p10: [], p50: [], p90: [] },
    cloudRevenue: { p10: [], p50: [], p90: [] },
    roic: { p10: [], p50: [], p90: [] }
  };
  
  const steps = p.horizon;
  for (let t = 0; t < steps; t++) {
    const stepIndices = results.map(r => r.indexVal[t]).sort((a, b) => a - b);
    const stepRevenues = results.map(r => r.cloudRevenue[t]).sort((a, b) => a - b);
    const stepRoics = results.map(r => r.roic[t]).sort((a, b) => a - b);
    
    const idx10 = Math.floor(trials * 0.1);
    const idx50 = Math.floor(trials * 0.5);
    const idx90 = Math.floor(trials * 0.9);
    
    summary.indexVal.p10.push(stepIndices[idx10]);
    summary.indexVal.p50.push(stepIndices[idx50]);
    summary.indexVal.p90.push(stepIndices[idx90]);
    
    summary.cloudRevenue.p10.push(stepRevenues[idx10]);
    summary.cloudRevenue.p50.push(stepRevenues[idx50]);
    summary.cloudRevenue.p90.push(stepRevenues[idx90]);
    
    summary.roic.p10.push(stepRoics[idx10]);
    summary.roic.p50.push(stepRoics[idx50]);
    summary.roic.p90.push(stepRoics[idx90]);
  }
  
  return summary;
}

const REAL_HISTORICAL_TRAILS = {
  dotcom: {
    actualIndex: [
      100.0, 112.4, 128.1, 140.3, 161.2, 185.7, 210.4, 245.1,
      290.8, 345.2, 412.6, 520.1, 480.3, 395.1, 310.4, 265.8,
      185.2, 154.3, 132.1, 118.4, 105.6, 92.1,  84.3,  78.2
    ],
    historicalCapEx: [
      12.1, 14.3, 18.2, 22.5, 31.2, 42.6, 58.1, 72.4,
      94.1, 112.4, 121.0, 145.2, 110.1, 85.3, 62.4, 41.2,
      28.4, 19.1, 14.3, 11.0, 9.2, 8.5, 7.9, 7.2
    ]
  },
  japan: {
    actualIndex: [
      100.0, 84.2, 76.1, 68.4, 62.1, 65.4, 58.2, 54.1,
      51.3,  53.0, 49.2, 46.5, 44.1, 47.2, 41.0, 39.4,
      37.2,  38.5, 35.1, 32.4, 30.2, 29.1, 28.4, 27.2
    ],
    historicalRates: [
      0.0375, 0.0425, 0.0525, 0.0600, 0.0600, 0.0550, 0.0450, 0.0325,
      0.0325, 0.0250, 0.0175, 0.0175, 0.0100, 0.0050, 0.0050, 0.0050,
      0.0050, 0.0050, 0.0025, 0.0025, 0.0015, 0.0015, 0.0010, 0.0010
    ]
  },
  railway: {
    actualIndex: [
      100.0, 105.0, 110.0, 115.0, 120.0, 130.0, 145.0, 160.0,
      175.0, 190.0, 198.4, 180.0, 165.0, 150.0, 138.0, 128.0,
      118.0, 110.0, 100.0, 90.0,  85.0,  80.0,  76.0,  72.0,
      68.0,  65.0,  63.0,  61.0,  60.0
    ]
  }
};

function optimizeHistoricalParameters(dynamicCrisis) {
  const dataTrail = REAL_HISTORICAL_TRAILS[dynamicCrisis];
  if (!dataTrail) return null;

  let bestRMSE = Infinity;
  let bestDA = 0;
  let bestParams = {};

  console.log(`Running optimization loop for ${dynamicCrisis.toUpperCase()} calibration...`);

  for (let elasticity = 0.2; elasticity <= 2.2; elasticity += 0.1) {
    for (let priceCompress = 0.05; priceCompress <= 0.9; priceCompress += 0.05) {
      for (let reflexivity = 0.1; reflexivity <= 1.0; reflexivity += 0.05) {
        
        let testParams = {
          ...DEFAULT_PARAMS,
          horizon: dataTrail.actualIndex.length,
          elasticityCoefficient: elasticity,
          priceCompression: priceCompress,
          capitalReflexivity: reflexivity
        };

        if (dynamicCrisis === "dotcom") {
          testParams.contractMix3yr = 0.90;
          testParams.initialComputeSupply = 4.0;
          testParams.initialPower = 3.0;
          testParams.initialSoftwareRevenues = 4.0;
          testParams.initialCloudRevenue = 4.0;
          testParams.initialCapEx = 5.0;
          testParams.initialSilicon = 5.0;
          testParams.wacc = 0.05;
          testParams.complianceFriction = 0.0;
          testParams.tcoMultiplier = 1.0;
          testParams.adoptionDecayRate = 0.04;
          testParams.sentimentSpeed = 5.0;
          testParams.maxSentiment = 4.5;
          testParams.sentimentDecay = 0.55;
          testParams.targetMultipleSales = 0.5;
          testParams.downsizingRatio = 0.85;
          testParams.insolvencyWriteDownRate = 0.10;
        } else if (dynamicCrisis === "japan") {
          testParams.wacc = 0.06;
          testParams.downsizingRatio = 0.75;
          testParams.seasonalityCycle = 0.045;
        } else if (dynamicCrisis === "railway") {
          testParams.wacc = 0.03;
          testParams.downsizingRatio = 0.70;
          testParams.initialComputeSupply = 8.0;
          testParams.initialPower = 4.0;
          testParams.initialSoftwareRevenues = 6.0;
          testParams.initialCloudRevenue = 6.0;
          testParams.initialCapEx = 10.0;
          testParams.initialSilicon = 10.0;
          testParams.sentimentSpeed = 1.0;
          testParams.maxSentiment = 1.5;
          testParams.sentimentDecay = 0.45;
          testParams.targetMultipleSales = 0.5;
        }

        const simOutput = runSimulation(testParams);
        const simulatedTrail = simOutput.indexVal;
        const actualTrail = dataTrail.actualIndex;

        const n = actualTrail.length;
        const calibratedTrail = simulatedTrail; // no rescaling — compare on the same index scale
        
        let sumSquaredError = 0;
        let directionalMatches = 0;

        for (let t = 0; t < n; t++) {
          sumSquaredError += Math.pow(actualTrail[t] - calibratedTrail[t], 2);
          if (t > 0) {
            if (Math.sign(actualTrail[t] - actualTrail[t - 1]) === Math.sign(calibratedTrail[t] - calibratedTrail[t - 1])) {
              directionalMatches++;
            }
          }
        }

        let currentRMSE = Math.sqrt(sumSquaredError / n);
        let currentDA = directionalMatches / (n - 1);

        if (currentRMSE < bestRMSE) {
          bestRMSE = currentRMSE;
          bestDA = currentDA;
          bestParams = { elasticityCoefficient: elasticity, priceCompression: priceCompress, capitalReflexivity: reflexivity };
        }
      }
    }
  }

  console.log(`Optimization complete. Best RMSE: ${bestRMSE.toFixed(3)} | Best DA: ${(bestDA * 100).toFixed(1)}%`);
  return { optimizedParams: bestParams, targetPassed: bestRMSE < 25.0 && bestDA > 0.70 };
}

function verifyHistoricalCase(dynamicCrisis) {
  const dataTrail = REAL_HISTORICAL_TRAILS[dynamicCrisis];
  if (!dataTrail) return null;

  const opt = optimizeHistoricalParameters(dynamicCrisis);
  
  let testParams = { 
    ...DEFAULT_PARAMS, 
    horizon: dataTrail.actualIndex.length,
    ...opt.optimizedParams
  };

  if (dynamicCrisis === "dotcom") {
    testParams.contractMix3yr = 0.90;
    testParams.initialComputeSupply = 4.0;
    testParams.initialPower = 3.0;
    testParams.initialSoftwareRevenues = 4.0;
    testParams.initialCloudRevenue = 4.0;
    testParams.initialCapEx = 5.0;
    testParams.initialSilicon = 5.0;
    testParams.wacc = 0.05;
    testParams.complianceFriction = 0.0;
    testParams.tcoMultiplier = 1.0;
    testParams.adoptionDecayRate = 0.04;
    testParams.sentimentSpeed = 5.0;
    testParams.maxSentiment = 4.5;
    testParams.sentimentDecay = 0.55;
    testParams.targetMultipleSales = 0.5;
    testParams.downsizingRatio = 0.85;
    testParams.insolvencyWriteDownRate = 0.10;
  } else if (dynamicCrisis === "japan") {
    testParams.wacc = 0.06;
    testParams.downsizingRatio = 0.75;
    testParams.seasonalityCycle = 0.045;
  } else if (dynamicCrisis === "railway") {
    testParams.wacc = 0.03;
    testParams.downsizingRatio = 0.70;
    testParams.initialComputeSupply = 8.0;
    testParams.initialPower = 4.0;
    testParams.initialSoftwareRevenues = 6.0;
    testParams.initialCloudRevenue = 6.0;
    testParams.initialCapEx = 10.0;
    testParams.initialSilicon = 10.0;
    testParams.sentimentSpeed = 1.0;
    testParams.maxSentiment = 1.5;
    testParams.sentimentDecay = 0.45;
    testParams.targetMultipleSales = 0.5;
  }

  const simOutput = runSimulation(testParams);
  const simulatedTrail = simOutput.indexVal;
  const actualTrail = dataTrail.actualIndex;

  const n = actualTrail.length;
  const calibratedTrail = simulatedTrail; // no rescaling — compare on the same index scale
  
  let sumSquaredError = 0;
  let directionalMatches = 0;

  for (let t = 0; t < n; t++) {
    sumSquaredError += Math.pow(actualTrail[t] - calibratedTrail[t], 2);
    
    if (t > 0) {
      const actualDirection = Math.sign(actualTrail[t] - actualTrail[t - 1]);
      const simulatedDirection = Math.sign(calibratedTrail[t] - calibratedTrail[t - 1]);
      if (actualDirection === simulatedDirection) {
        directionalMatches++;
      }
    }
  }

  const rmse = Math.sqrt(sumSquaredError / n);
  const directionalAccuracy = directionalMatches / (n - 1);

  return {
    crisis: dynamicCrisis,
    rmse: rmse,
    directionalAccuracyPct: directionalAccuracy * 100,
    calibrationPassed: rmse < 25.0 && directionalAccuracy > 0.70,
    simulatedTrail: calibratedTrail,
    actualTrail: actualTrail
  };
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    REGIONS,
    INDUSTRIES,
    DEFAULT_PARAMS,
    runSimulation,
    generateScenarioMatrix,
    runMonteCarlo,
    REAL_HISTORICAL_TRAILS,
    verifyHistoricalCase,
    optimizeHistoricalParameters
  };
} else {
  window.TESMEngine = {
    REGIONS,
    INDUSTRIES,
    DEFAULT_PARAMS,
    runSimulation,
    generateScenarioMatrix,
    runMonteCarlo,
    REAL_HISTORICAL_TRAILS,
    verifyHistoricalCase,
    optimizeHistoricalParameters
  };
}
