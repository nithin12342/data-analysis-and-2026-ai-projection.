/**
 * app.js
 * Main Controller for TESM Dashboard
 * Ties sliders, region/industry dropdowns, matrices, charts, and formula views together.
 */

document.addEventListener("DOMContentLoaded", () => {
  const engine = window.TESMEngine;
  if (!engine) {
    console.error("TESM simulation engine not loaded!");
    return;
  }

  // Active state
  let currentParams = { ...engine.DEFAULT_PARAMS };
  let currentTab = "dynamics"; // dynamics, montecarlo, historical
  let selectedScenario = "baseline";
  let activeFormulaId = "roic";
  let mainChart = null;

  // Cache DOM elements
  const sliders = document.querySelectorAll(".sidebar input[type='range']");
  const tabButtons = document.querySelectorAll(".tab-btn");
  const matrixContainer = document.querySelector(".matrix-grid");
  const explorerList = document.querySelector(".explorer-list");
  const explorerDetail = document.querySelector(".explorer-detail");
  const activeRegionSelect = document.getElementById("activeRegion");
  const activeIndustrySelect = document.getElementById("activeIndustry");

  // Formula documentation presets for Explorer
  const formulas = {
    compute: {
      title: "Compute Stranding & Power Alignment",
      equation: "Stranded = Max(0, ComputeSupply - (ActivePower * 1.15))",
      description: "Compute hardware capacity scales with CapEx and sentiment, while data-center grid power expansion is delayed by local regulatory and construction lead times. If compute exceeds what the active power infrastructure supports, it is 'stranded' (idle) and triggers a 12% impairment rate.",
      getInputs: (p, sim) => [
        { name: "Total Compute Supply Q80", value: sim.computeSupply[79].toFixed(2) },
        { name: "Active Power Grid Q80", value: `${sim.activePower[79].toFixed(2)} MW` },
        { name: "Transformer & Permitting Lag", value: `${(p.transformerShortage * 100).toFixed(0)}%` }
      ],
      getOutputs: (p, sim) => [
        { name: "Stranded Compute Q80", value: sim.strandedCapacity[79].toFixed(2) },
        { name: "Power Capacity Deficit Q80", value: Math.max(0, (sim.computeSupply[79] / 1.15) - sim.activePower[79]).toFixed(2) }
      ]
    },
    pricing: {
      title: "Jevons Paradox & Price Elasticity",
      equation: "DemandVolume = Compute * (1 / TokenPrice) ^ (Elasticity - 1)",
      description: "As open-source models converge and hardware efficiency lowers token costs, API prices compress. If elasticity coefficient (ε) is greater than 1.0, cost savings trigger explosive volume demand, generating net positive revenues. If ε < 1.0, deflation compresses top-line returns.",
      getInputs: (p, sim) => [
        { name: "Demand Elasticity (ε)", value: p.elasticityCoefficient.toFixed(2) },
        { name: "Annual Token Compression", value: `${(p.priceCompression * 100).toFixed(0)}%` },
        { name: "Open Source Competitiveness", value: `${(p.openSourcePower * 100).toFixed(0)}%` }
      ],
      getOutputs: (p, sim) => {
        const costRate = 0.38;
        const totalDrop = costRate + p.priceCompression * p.openSourcePower;
        const finalTokenPrice = Math.max(0.005, Math.pow(1 - totalDrop * 0.25, 79));
        return [
          { name: "Token Cost Q80 (Base = 1.0)", value: finalTokenPrice.toFixed(4) },
          { name: "Volume Expansion Factor", value: Math.pow(1 / finalTokenPrice, p.elasticityCoefficient - 1).toFixed(1) }
        ];
      }
    },
    adoption: {
      title: "Compliance Drag & Net Labor Savings",
      equation: "NetSavings = GrossSavings - DemandVolume * TCOMultiplier * ComplianceFactor",
      description: "Autonomous agent deployment benefits are partially offsets by compliance monitoring, validation gates, security audits, and liability coverage. Regulated industries (Banking, Healthcare) suffer heavier agentic friction, slowing technology diffusion.",
      getInputs: (p, sim) => [
        { name: "Agent TCO Multiplier", value: `${p.tcoMultiplier.toFixed(1)}x` },
        { name: "Industry Regulator Costs", value: p.activeIndustry },
        { name: "Compliance Drag", value: `${(p.complianceFriction * 100).toFixed(0)}%` }
      ],
      getOutputs: (p, sim) => {
        const complianceCost = p.activeIndustry === 'software' ? 0.10 : p.activeIndustry === 'banking' ? 0.25 : p.activeIndustry === 'healthcare' ? 0.20 : 0.15;
        const complianceDelay = 1 + (p.complianceFriction + complianceCost) * 3;
        return [
          { name: "Compliance Delay Factor", value: complianceDelay.toFixed(2) },
          { name: "Enterprise Net ROI Q80", value: `${(sim.netEnterpriseROI[79] * 100).toFixed(1)}%` }
        ];
      }
    },
    cliff: {
      title: "Contract Renewal & Multi-Year Cliffs",
      equation: "RenewalRate = ROI < WACC ? (1 - DownsizingRatio) : 0.96",
      description: "Hyperscalers lock enterprise software firms into 3-year (70%) and 5-year (30%) capacity leases. If software products underperform relative to WACC, clients scale back committed GPU/Cloud spending upon renewal, creating a delayed revenue cliff.",
      getInputs: (p, sim) => [
        { name: "Contract Mix (3yr / 5yr)", value: `${(p.contractMix3yr * 100).toFixed(0)}% / ${(100 - p.contractMix3yr * 100).toFixed(0)}%` },
        { name: "Downsizing Ratio", value: `${(p.downsizingRatio * 100).toFixed(0)}%` },
        { name: "WACC Cost of Capital", value: `${(p.wacc * 100).toFixed(1)}%` }
      ],
      getOutputs: (p, sim) => {
        const roi = sim.netEnterpriseROI[79];
        return [
          { name: "Software ROI Q80", value: `${(roi * 100).toFixed(1)}%` },
          { name: "Effective Renewal Rate Q80", value: `${((roi < p.wacc ? (1 - p.downsizingRatio) : 0.96) * 100).toFixed(0)}%` }
        ];
      }
    },
    roic: {
      title: "Return on Invested Capital (ROIC)",
      equation: "ROIC = (CloudEbitda - Amortization - StrandedImpairment) / InvestedCapital",
      description: "Net operating profit matches cloud EBITDA minus hardware depreciation and write-downs of stranded infrastructure. ROIC determines if hyperscalers generate returns above WACC, which recursively drives capital markets valuations and CapEx cycles.",
      getInputs: (p, sim) => [
        { name: "Cloud EBITDA Margin", value: "44%" },
        { name: "Amortization Rate (Qtr)", value: "6.25%" },
        { name: "Stranded Impairment Rate", value: "12% / Year" }
      ],
      getOutputs: (p, sim) => [
        { name: "ROIC Q80", value: `${(sim.roic[79] * 100).toFixed(1)}%` },
        { name: "Sentiment Multiplier Q80", value: `${sim.multipleSales[79].toFixed(1)}x` }
      ]
    },
    quality: {
      title: "Revenue Quality Tiering Model",
      equation: "HighQuality = CloudRevenue * SwitchingCost * NetROI",
      description: "Differentiates stable, sticky, mission-critical enterprise software subscriptions (High Quality) from temporary pilots, experimental credits, and price-sensitive API tokens (Low Quality).",
      getInputs: (p, sim) => [
        { name: "Active Industry", value: p.activeIndustry },
        { name: "Net ROI Q80", value: `${(sim.netEnterpriseROI[79] * 100).toFixed(1)}%` }
      ],
      getOutputs: (p, sim) => [
        { name: "High Quality Revenue Q80", value: `$${sim.revenueQualityHigh[79].toFixed(1)}B` },
        { name: "Low Quality Revenue Q80", value: `$${sim.revenueQualityLow[79].toFixed(1)}B` }
      ]
    },
    gdp: {
      title: "Global Macroeconomic Feedback Model",
      equation: "GDPBoost = SoftwareRevenues * 0.5% * PPPDiscount",
      description: "Models second-order macro productivity boosts resulting from operational cost reductions. Adjusted for Purchasing Power Parity (PPP) metrics to reflect strategic regional cost structures.",
      getInputs: (p, sim) => [
        { name: "Selected Region", value: p.activeRegion },
        { name: "PPP Adjustment Multiplier", value: pppAdjustmentLabel(p.activeRegion) }
      ],
      getOutputs: (p, sim) => [
        { name: "Peak Productivity GDP Boost", value: `${Math.max(...sim.gdpBoost).toFixed(2)}%` },
        { name: "Q80 Productivity GDP Boost", value: `${sim.gdpBoost[79].toFixed(2)}%` }
      ]
    },
    onsite: {
      title: "Onsite Generation & Grid Defection Economics",
      equation: "EffectivePowerPrice = GridPrice * ImportFraction + (OnsiteNetCost / Dispatch) * (1 - ImportFraction)",
      description: "Models onsite generation (Bloom SOFC, gas turbines, hydrogen fuel cells) to bypass transmission constraints. If net onsite costs drop below the grid defection threshold, hyperscalers build more onsite MW, bringing blended electricity costs down from $85/MWh.",
      getInputs: (p, sim) => [
        { name: "Onsite Capacity Q80", value: `${sim.onsiteGenCapacityMW[79].toFixed(0)} MW` },
        { name: "Capacity Factor", value: `${(p.onsiteCapacityFactor * 100).toFixed(1)}%` },
        { name: "Defection Threshold", value: `${(p.gridDefectionThreshold * 100).toFixed(0)}%` }
      ],
      getOutputs: (p, sim) => [
        { name: "Onsite Dispatch Q80", value: `${sim.onsiteDispatch[79].toFixed(0)} MW` },
        { name: "Blended Power Price Q80", value: `$${sim.effectiveGridPrice[79].toFixed(2)}/MWh` },
        { name: "Fuel & Carbon Cost Q80", value: `$${((sim.onsiteFuelCost[79] + sim.carbonCost[79]) / 1e6).toFixed(2)}M/qtr` }
      ]
    }
  };

  function pppAdjustmentLabel(region) {
    if (region === "us") return "1.00 (Base)";
    if (region === "china") return "0.55 (PPP Discount)";
    if (region === "india") return "0.45 (PPP Discount)";
    if (region === "gulf") return "0.80 (PPP Discount)";
    if (region === "eu") return "1.15 (PPP Cost Premium)";
    return "1.00";
  }

  // Initialize UI controls
  function initControls() {
    // Synchronize sliders and select dropdowns with overrides on page load
    sliders.forEach(slider => {
      const id = slider.id;
      if (currentParams[id] !== undefined) {
        // Expand range dynamically if calibrated value exceeds default HTML slider limit
        if (id === 'powerGrowthCap' && currentParams[id] > parseFloat(slider.max)) {
          slider.max = currentParams[id];
        }
        slider.value = currentParams[id];
        
        const label = document.querySelector(`[data-for='${id}']`);
        if (label) {
          const val = currentParams[id];
          if (id === 'tcoMultiplier') label.textContent = `${val.toFixed(1)}x`;
          else if (id === 'wacc' || id === 'priceCompression' || id === 'powerGrowthCap' || id === 'downsizingRatio') {
            label.textContent = `${(val * 100).toFixed(0)}%`;
          } else if (id === 'averageContractLength') {
            label.textContent = `${val} Qtrs`;
          } else {
            label.textContent = val.toFixed(2);
          }
        }
      }

      slider.addEventListener("input", (e) => {
        const id = e.target.id;
        const val = parseFloat(e.target.value);
        currentParams[id] = val;
        
        const label = document.querySelector(`[data-for='${id}']`);
        if (label) {
          if (id === 'tcoMultiplier') label.textContent = `${val.toFixed(1)}x`;
          else if (id === 'wacc' || id === 'priceCompression' || id === 'powerGrowthCap' || id === 'downsizingRatio') {
            label.textContent = `${(val * 100).toFixed(0)}%`;
          } else if (id === 'averageContractLength') {
            label.textContent = `${val} Qtrs`;
          } else {
            label.textContent = val.toFixed(2);
          }
        }
        
        document.querySelectorAll(".matrix-cell").forEach(c => c.classList.remove("active"));
        updateDashboard();
      });
    });

    if (currentParams.activeRegion) activeRegionSelect.value = currentParams.activeRegion;
    if (currentParams.activeIndustry) activeIndustrySelect.value = currentParams.activeIndustry;

    // Dropdown selectors
    activeRegionSelect.addEventListener("change", (e) => {
      currentParams.activeRegion = e.target.value;
      updateDashboard();
    });

    activeIndustrySelect.addEventListener("change", (e) => {
      currentParams.activeIndustry = e.target.value;
      updateDashboard();
    });

    // Tab buttons
    tabButtons.forEach(btn => {
      btn.addEventListener("click", () => {
        tabButtons.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        currentTab = btn.dataset.tab;
        renderCharts();
      });
    });
  }

  // Generate and update the 31 Scenario Matrix Grid
  function updateScenarioMatrix() {
    matrixContainer.innerHTML = "";
    const matrix = engine.generateScenarioMatrix(currentParams);
    
    Object.keys(matrix).forEach(name => {
      const sim = matrix[name];
      const finalIndex = sim.indexVal[sim.indexVal.length - 1];
      const finalROIC = sim.roic[sim.roic.length - 1];
      
      let statusClass = "status-green";
      let statusText = "Stable Growth";
      
      const overallCAGR = Math.pow(finalIndex / 100, 1 / 20) - 1;
      
      if (finalIndex < 50) {
        statusClass = "status-red";
        statusText = "Severe Crash";
      } else if (finalIndex < 100) {
        statusClass = "status-yellow";
        statusText = "Deflationary";
      } else if (overallCAGR < 0.04 || finalROIC < currentParams.wacc) {
        statusClass = "status-purple";
        statusText = "Stagnant / Flat";
      }
      
      const cell = document.createElement("div");
      cell.className = `matrix-cell ${name === selectedScenario ? 'active' : ''}`;
      cell.innerHTML = `
        <div class="matrix-cell-title">${name}</div>
        <div class="matrix-cell-status ${statusClass}">${statusText}</div>
        <div style="font-family: monospace; font-size: 0.75rem; color: var(--text-muted);">Idx: ${finalIndex.toFixed(0)}</div>
      `;
      
      cell.addEventListener("click", () => {
        selectedScenario = name;
        document.querySelectorAll(".matrix-cell").forEach(c => c.classList.remove("active"));
        cell.classList.add("active");
        
        applyPresetScenario(name);
      });
      
      matrixContainer.appendChild(cell);
    });
  }

  // Pre-configured adjustments for Scenarios A-E
  function applyPresetScenario(name) {
    const scenarioDefs = {
      baseline: {},
      A: { tcoMultiplier: 3.0, complianceFriction: 0.60 },
      B: { pppAdjustment: 0.40, priceCompression: 0.85, openSourcePower: 0.90 },
      C: { powerGrowthCap: 0.04, gridConnectionDelay: 12, transformerShortage: 0.50, hbmBottleneck: 0.45 },
      D: { averageContractLength: 16, downsizingRatio: 0.65, contractMix3yr: 0.40 },
      E: { baseMultipleSales: 12.0, targetMultipleSales: 2.0 }
    };
    
    const elements = name.split('+');
    const merged = {};
    
    elements.forEach(el => {
      if (scenarioDefs[el]) {
        Object.assign(merged, scenarioDefs[el]);
      }
    });
    
    // Reset inputs
    Object.keys(engine.DEFAULT_PARAMS).forEach(key => {
      currentParams[key] = merged[key] !== undefined ? merged[key] : engine.DEFAULT_PARAMS[key];
      
      // Update UI Slider and Value
      const slider = document.getElementById(key);
      if (slider) {
        slider.value = currentParams[key];
        const label = document.querySelector(`[data-for='${key}']`);
        if (label) {
          const val = currentParams[key];
          if (key === 'tcoMultiplier') label.textContent = `${val.toFixed(1)}x`;
          else if (key === 'wacc' || key === 'priceCompression' || key === 'powerGrowthCap' || key === 'downsizingRatio') {
            label.textContent = `${(val * 100).toFixed(0)}%`;
          } else {
            label.textContent = val.toFixed(2);
          }
        }
      }
      
      // Update UI Dropdowns
      const select = document.getElementById(key);
      if (select && select.tagName === "SELECT") {
        select.value = currentParams[key];
      }
    });
    
    updateDashboard();
  }

  // Update Stats Cards
  function updateStatsCards(sim) {
    const finalIdx = sim.indexVal[sim.indexVal.length - 1];
    const maxMultiple = Math.max(...sim.multipleSales);
    const maxStranded = Math.max(...sim.strandedCapacity) / (Math.max(...sim.computeSupply) + 0.1) * 100;
    const finalROI = sim.netEnterpriseROI[sim.netEnterpriseROI.length - 1] * 100;
    
    document.getElementById("stat-index").textContent = finalIdx.toFixed(0);
    document.getElementById("stat-multiple").textContent = `${maxMultiple.toFixed(1)}x`;
    document.getElementById("stat-stranded").textContent = `${maxStranded.toFixed(0)}%`;
    document.getElementById("stat-roi").textContent = `${finalROI.toFixed(0)}%`;
    
    const indexTrend = document.getElementById("trend-index");
    if (finalIdx >= 100) {
      indexTrend.className = "card-trend trend-up";
      indexTrend.innerHTML = "▲ Expansionary";
    } else if (finalIdx >= 50) {
      indexTrend.className = "card-trend trend-down";
      indexTrend.innerHTML = "▼ Stagnation / Deflation";
    } else {
      indexTrend.className = "card-trend trend-down";
      indexTrend.innerHTML = "▼ Bubble Burst / Crash";
    }
    
    const roiTrend = document.getElementById("trend-roi");
    if (finalROI >= currentParams.wacc * 100) {
      roiTrend.className = "card-trend trend-up";
      roiTrend.innerHTML = `▲ Net Positive (GDP +${sim.gdpBoost[79].toFixed(1)}%)`;
    } else {
      roiTrend.className = "card-trend trend-down";
      roiTrend.innerHTML = `▼ Destructive (GDP +${sim.gdpBoost[79].toFixed(1)}%)`;
    }
  }

  // Setup formula explorer list
  function setupFormulaExplorer() {
    explorerList.innerHTML = "";
    Object.keys(formulas).forEach(id => {
      const item = document.createElement("button");
      item.className = `explorer-item ${id === activeFormulaId ? 'active' : ''}`;
      item.textContent = formulas[id].title;
      item.addEventListener("click", () => {
        activeFormulaId = id;
        document.querySelectorAll(".explorer-item").forEach(i => i.classList.remove("active"));
        item.classList.add("active");
        renderFormulaDetail();
      });
      explorerList.appendChild(item);
    });
    renderFormulaDetail();
  }

  // Render detail in explorer
  function renderFormulaDetail() {
    const formula = formulas[activeFormulaId];
    if (!formula) return;
    const sim = engine.runSimulation(currentParams);
    
    let tableRows = "";
    
    formula.getInputs(currentParams, sim).forEach(row => {
      tableRows += `<tr><td>${row.name} (Input)</td><td>${row.value}</td></tr>`;
    });
    
    formula.getOutputs(currentParams, sim).forEach(row => {
      tableRows += `<tr><td><strong>${row.name} (Output)</strong></td><td><strong>${row.value}</strong></td></tr>`;
    });

    explorerDetail.innerHTML = `
      <h3 style="font-size: 1.1rem; color: var(--text-primary); font-family: var(--font-sans);">${formula.title}</h3>
      <p style="font-size: 0.85rem; color: var(--text-secondary);">${formula.description}</p>
      <div class="math-eq">${formula.equation}</div>
      <table class="detail-table">
        <thead>
          <tr>
            <th>Variable</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          ${tableRows}
        </tbody>
      </table>
    `;
  }

  // Render Main Chart
  function renderCharts() {
    if (mainChart) {
      mainChart.destroy();
    }
    
    const calPanel = document.getElementById("calibration-metrics-panel");
    if (calPanel) {
      calPanel.style.display = (currentTab === "historical") ? "flex" : "none";
    }
    
    const ctx = document.getElementById("main-chart-canvas").getContext("2d");
    const sim = engine.runSimulation(currentParams);
    let labels = sim.quarters.map(q => `Q${q}`);
    
    let dataSets = [];
    let options = {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: {
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          ticks: { color: '#a0aec0', font: { family: 'Space Grotesk' } }
        },
        y: {
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          ticks: { color: '#a0aec0', font: { family: 'Space Grotesk' } }
        }
      },
      plugins: {
        legend: { labels: { color: '#f5f6fa', font: { family: 'Outfit' } } }
      }
    };

    if (currentTab === "dynamics") {
      dataSets = [
        {
          label: "Cloud Hyperscaler Revenue ($B)",
          data: sim.cloudRevenue,
          borderColor: '#4facfe',
          backgroundColor: 'rgba(79, 172, 254, 0.08)',
          fill: true,
          tension: 0.2
        },
        {
          label: "High Quality Enterprise Rev ($B)",
          data: sim.revenueQualityHigh,
          borderColor: '#00e676',
          backgroundColor: 'transparent',
          borderDash: [2, 2],
          tension: 0.2
        },
        {
          label: "Enterprise AI Software Revenue ($B)",
          data: sim.softwareRevenues,
          borderColor: '#00f2fe',
          backgroundColor: 'rgba(0, 242, 254, 0.04)',
          fill: true,
          tension: 0.2
        },
        {
          label: "Stranded Compute Capacity",
          data: sim.strandedCapacity,
          borderColor: '#ff3366',
          backgroundColor: 'transparent',
          borderDash: [5, 5],
          tension: 0.2
        }
      ];
    } else if (currentTab === "montecarlo") {
      const mc = engine.runMonteCarlo(currentParams, 200);
      dataSets = [
        {
          label: "Index Value (90th Percentile)",
          data: mc.indexVal.p90,
          borderColor: 'rgba(0, 242, 254, 0.3)',
          backgroundColor: 'transparent',
          borderDash: [2, 2],
          tension: 0.1
        },
        {
          label: "Index Value (50th Percentile - Expected)",
          data: mc.indexVal.p50,
          borderColor: '#4facfe',
          backgroundColor: 'rgba(79, 172, 254, 0.15)',
          fill: true,
          tension: 0.2
        },
        {
          label: "Index Value (10th Percentile - Stress)",
          data: mc.indexVal.p10,
          borderColor: 'rgba(255, 51, 102, 0.5)',
          backgroundColor: 'transparent',
          borderDash: [2, 2],
          tension: 0.1
        }
      ];
    } else if (currentTab === "historical") {
      // Run the backtest engine verification
      const dotcomVerify = engine.verifyHistoricalCase("dotcom");
      const japanVerify = engine.verifyHistoricalCase("japan");
      
      // Select active data set based on the user's dropdown region config
      const activeVerify = (currentParams.activeRegion === "china" || currentParams.activeRegion === "eu") ? japanVerify : dotcomVerify;

      // Override labels to fit the calibration horizon (24 quarters)
      labels = activeVerify.simulatedTrail.map((_, i) => `Q${i}`);

      // Update chart to display actual historical numbers side-by-side with simulation outputs
      dataSets = [
        {
          label: `TESM Simulated Index Path (${activeVerify.crisis.toUpperCase()})`,
          data: activeVerify.simulatedTrail,
          borderColor: '#00f2fe',
          borderWidth: 3,
          tension: 0.2
        },
        {
          label: `Actual Real-World Market Path (${activeVerify.crisis.toUpperCase()})`,
          data: activeVerify.actualTrail,
          borderColor: '#ffb300',
          backgroundColor: 'transparent',
          borderDash: [4, 4],
          tension: 0.1
        }
      ];
      
      // Update the browser console with transparent mathematical verification logs
      console.log(`--- TESM HISTORICAL CALIBRATION LOG [${activeVerify.crisis.toUpperCase()}] ---`);
      console.log(`Calculated Root Mean Squared Error (RMSE): ${activeVerify.rmse.toFixed(3)}`);
      console.log(`Realized Directional Predictive Accuracy: ${activeVerify.directionalAccuracyPct.toFixed(1)}%`);
      console.log(`Validation Audit Passed: ${activeVerify.calibrationPassed}`);

      // Update the UI panel with metrics
      if (calPanel) {
        document.getElementById("cal-rmse").textContent = activeVerify.rmse.toFixed(3);
        document.getElementById("cal-da").textContent = `${activeVerify.directionalAccuracyPct.toFixed(1)}%`;
        const statusEl = document.getElementById("cal-status");
        if (activeVerify.calibrationPassed) {
          statusEl.textContent = "PASSED";
          statusEl.className = "metric-badge badge-passed";
        } else {
          statusEl.textContent = "FAILED";
          statusEl.className = "metric-badge badge-failed";
        }
      }
    }

    mainChart = new Chart(ctx, {
      type: 'line',
      data: { labels, datasets: dataSets },
      options
    });
  }

  // Update All Components
  function updateDashboard() {
    const sim = engine.runSimulation(currentParams);
    updateStatsCards(sim);
    renderCharts();
    renderFormulaDetail();
    updateScenarioMatrix();
  }

  // Initial load
  initControls();
  setupFormulaExplorer();
  updateDashboard();
});
