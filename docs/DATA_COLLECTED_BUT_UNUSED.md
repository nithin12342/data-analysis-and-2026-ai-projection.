# Data Collected But Not Used in TESM Model

**Generated:** 2026-07-15  
**Project:** Comprehensive Financial Modeling: Dot-com Bubble vs. Today's AI Economy  
**Repository:** `C:\Users\NITHING\Desktop\projections\`

---

## Executive Summary

The calibration pipeline (`calibrate.py`) loads **17 CSV data files + 13 SEC quarters + 2 Excel files** containing rich structured datasets. However, the core simulation engine (`engine.js`) only consumes **~25 scalar parameters** from this data. The majority of granular, time-series, and cross-sectional data is **loaded into memory but discarded** — either written as empty objects in `param_overrides.js` or passed through as unstructured JSON blobs never accessed by the simulation.

---

## 1. Data Files Fully Loaded But Parameters Never Used in Engine

| Data File | Records | Rich Fields Available | What calibrate.py Extracts | Used in engine.js? |
|-----------|---------|----------------------|----------------------------|-------------------|
| **`productivity/meta_analysis_studies.csv`** | 16 studies | study, category, intervention, industry, task_type, sample_size, effect_size_pct, ci_lower/upper, study_design, quality_score, source, url | Single scalar: `elasticityCoefficient = 1.0 + pooled_effect * 0.5` | ❌ Only elasticityCoefficient used; all study-level detail discarded |
| **`enterprise_contracts.csv`** | 15 contracts | company, contract_type, avg_contract_length_years, renewal_rate_pct, downsizing_pct_at_renewal, expansion_pct_at_renewal, NRR, GRR, year, source | 3 scalars: averageContractLength, contractMix3yr, downsizingRatio | ❌ Only 3 scalars used; per-contract-type dynamics, NRR/GRR trends, expansion rates ignored |
| **`china_benchmarks.csv`** | 26 models | model, organization, benchmark, score, date, language, model_type, parameters_b, source | **NOTHING** - loaded but zero parameters extracted | ❌ Entire Chinese model quality/convergence dataset unused |
| **`china_api_pricing.csv`** | 22 models | provider, model, input/output_price_usd_per_million_tokens, currency, date, source | **NOTHING** - loaded but zero parameters extracted | ❌ Chinese API pricing pressure data completely unused |
| **`regional_infrastructure.csv`** | 14 regions | region, country, ppp_factor, power_growth_cap_annual_pct, grid_connection_delay_months, gov_coordination_index, cost_per_mw_usd_millions, transformer_shortage_factor, cooling_water_availability, renewable_penetration_pct | Partial: powerGrowthCap, gridConnectionDelay, pppAdjustment via REGIONS dict | ❌ Regional cost_per_mw, transformer_shortage_factor, cooling_water, renewable_penetration, gov_coordination_index ignored |
| **`technology_parameters.csv`** | ? | (technology specs per vendor) | Loaded as `tech_params` DataFrame, passed to `TESM_DATA_CATEGORIES.technology` | ❌ Never accessed in engine.js |
| **`wholesale_electricity_prices.csv`** | ? | (hourly/daily wholesale prices by hub) | Loaded, passed to `TESM_DATA_CATEGORIES.wholesale_power` | ❌ Never accessed in engine.js |
| **`grid_connection_delays.csv`** | ? | (project-level queue delays) | Loaded, passed to `TESM_DATA_CATEGORIES.grid_delays` | ❌ Only mean from LBNL used; project-level distribution ignored |
| **`transformer_shortage.csv`** | ? | (transformer lead times, capacity) | Loaded, passed to `TESM_DATA_CATEGORIES.transformer_shortage` | ❌ Only scalar `transformerShortage` from LBNL withdrawal rate used |
| **`carbon_prices.csv`** | ? | (carbon prices by jurisdiction over time) | Loaded, passed to `TESM_DATA_CATEGORIES.carbon_prices` | ❌ Only static `carbonPrice` scalar used; jurisdictional time-series ignored |

---

## 2. Data Partially Used (Rich Structure Reduced to Single Scalar)

| Data Source | Rich Structure | Engine Consumes | Lost Information |
|-------------|----------------|-----------------|------------------|
| **LBNL Queue (Excel)** | 10,000+ projects × 30 fields (queue date, IA date, online date, withdrawal date, status, MW, technology, state, ISO, voltage, COD) | Mean queue (20 qtrs), withdrawal rate (75%) → `gridConnectionDelay`, `powerGrowthCap`, `transformerShortage` | Full project-level survival curves, technology-specific queue times, state/ISO heterogeneity, voltage-class constraints |
| **SEC DERA (13 quarters × 6 hyperscalers)** | 100+ XBRL tags per filing × 78 filings = ~8,000 data points | 3 time-series: CapEx_sum, RPO_sum, Rev_sum → `downsizingRatio`, `capitalReflexivity`, `siliconSupply` | Segment revenue (cloud vs ads vs hardware), SBC detail, deferred revenue components, geographic splits, capex by asset class |
| **Onsite Gen Capacity (CSV)** | 508 deployments × 12 fields (company, technology, capacity_mw, COD_year, capacity_factor, heat_rate, fuel_type, deployment_source) | Aggregate: total MW, weighted CF, tech mix dict, weighted heat rate, carbon intensity, water intensity | Company-specific rollout schedules, technology learning curves (degradation), fuel switching pathways, geographic distribution |
| **Heat Rates (CSV)** | 58 records × 8 fields (unit, technology, fuel, heat_rate_btu_kwh, date, degradation_pct_yr, source) | Single weighted average for current tech mix | Technology-specific degradation curves, vintage effects, fuel-specific efficiency trajectories |
| **Hedge Ratios (CSV)** | 18 records × 7 fields (company, commodity, hedge_ratio, tenor_yr, instruments, date, source) | Simple average (0.65) | Company-specific hedge tenor profiles, instrument mix (swaps vs collars vs physical), time-varying hedge ratios |
| **Grid Services (CSV)** | 8+ records × 7 fields (ISO, service, price_usd_mw_yr, volume_mw, date, source) | Simple average ($25k-40k/MW-yr) | Service-specific revenue stacks (regulation vs spinning vs capacity), ISO-specific price trajectories, volume constraints |
| **Fuel Prices (CSV)** | 1,808 monthly records × 6 fields (hub, date, price, basis_diff, volatility, source) | Current spot price only (Henry Hub $4.50, TTF ~$27, JKM ~$33) | Full term structure, basis risk dynamics, volatility regimes, seasonal patterns, hub correlations |
| **Productivity Meta-Analysis (CSV)** | 16 studies × 14 fields (effect sizes, CIs, study design, quality, industry, task_type) | Single pooled mean effect → `elasticityCoefficient` | Category-specific effects (coding 37-56%, writing 37%, support 14-22%, legal 24%, consulting 25-31%, R&D 38-44%), study quality weights, publication bias corrections |

---

## 3. Data Structures Passed to Browser But Never Accessed

In `param_overrides.js`, these are written as `TESM_DATA_CATEGORIES.*` but **never read by `engine.js`**:

```javascript
window.TESM_DATA_CATEGORIES = {
  "technology": [...],           // 0 records used
  "fuel_prices": [...],          // 1,808 records → only current spot used
  "grid_services": [...],        // 8+ records → only mean used
  "heat_rates": [...],           // 58 records → only weighted avg used
  "onsite_capacity": [...],      // 508 records → only aggregates used
  "hedge_ratios": [...],         // 18 records → only mean used
  "carbon_prices": [...],        // ? records → only static scalar used
  "grid_delays": [...],          // ? records → only LBNL mean used
  "transformer_shortage": [...], // ? records → only scalar used
  "wholesale_power": [...],      // ? records → NEVER USED
  "regional_infra": [...],       // 14 records → only 3 params via REGIONS dict
  "enterprise_contracts": [...], // 15 records → only 3 scalars used
  "productivity": [...]          // 16 records → only pooled mean used
};
```

---

## 4. Module-Specific Data Gaps (Per context.md Requirements)

| context.md Module | Required Data | Available But Unused |
|-------------------|---------------|---------------------|
| **§7 Productivity Gains** | Category-specific effect sizes, industry mapping, task automation rates | `productivity_meta_analysis.csv` has 16 studies with category/industry/task_type — only pooled mean used |
| **§8 Chinese AI Competition** | Model quality convergence (Elo), API pricing pressure, open-weight vs proprietary | `china_benchmarks.csv` (26 models), `china_api_pricing.csv` (22 models) — **completely unused** |
| **§9 PPP Adjustments** | Regional cost differentials for labor, electricity, construction, hardware, OpEx | `regional_infrastructure.csv` has PPP factors but only applied to `pppAdjustment` scalar; cost_per_mw, cooling_water, renewable_penetration ignored |
| **§11 Enterprise AI Agents** | Agent deployment counts (Google 1,302, SF 20,000), productivity gains, ROI | `enterprise_contracts.csv` has renewal/expansion rates but no agent-specific data |
| **§12 Workflow Integration** | Automation rates, task completion, switching costs, stickiness | Not collected at all |
| **§17 Enterprise Contract Lag** | Contract expiration schedules, reserved capacity expirations, GPU reservation expirations | `enterprise_contracts.csv` has avg length & mix but no expiration schedule or distribution |
| **§18 Agentic Liability** | Compliance costs by industry, audit requirements, liability exposure | `enterprise_contracts.csv` has downsizing % but no liability/compliance cost breakdown |
| **§19 Physical Constraints** | Transformer lead times, grid capacity, water availability, permitting timelines | `regional_infrastructure.csv` has transformer_shortage_factor, cooling_water_availability — **ignored** |
| **§21 Jevons Paradox** | Elasticity coefficient by use case, cost reduction trajectories | `productivity_meta_analysis.csv` has task_type-level effects — only pooled mean used |
| **§22 Open-Source Commoditization** | Model quality convergence timelines, fine-tuning adoption, self-hosting economics | `china_benchmarks.csv` tracks open-weight model Elo scores over time — **unused** |
| **§23 Compute Supply Cycle** | GPU lead times, wafer allocation, packaging constraints, HBM production | Not collected (only `siliconSupply` scalar from USITC) |
| **§24 Capital Market Reflexivity** | Institutional flows, short interest, options gamma, analyst revisions | Not collected |
| **§25 Revenue Quality** | Contract tier mix (high/med/low), NRR by cohort, expansion vs renewal | `enterprise_contracts.csv` has NRR/GRR but not used in revenue quality tiering |
| **§26 National Strategic Investment** | Govt subsidy amounts, industrial policy targets, energy security spending | `regional_infrastructure.csv` has gov_coordination_index — **not used** |
| **§27 Labor Market** | Occupation exposure, displacement rates, reskilling costs, wage effects | Not collected |
| **§28 Regulatory Scenarios** | Compliance costs by jurisdiction/regulation, enforcement probability | Not collected (only `complianceFriction` scalar) |
| **§29 AI Adoption Diffusion** | Adoption curves by segment (consumer/SME/enterprise/gov/healthcare/mfg) | Not collected |
| **§30 Macro Feedback** | GDP, inflation, rates, energy demand, commodity demand, FX, capital flows | FRED catalog loaded (24 series) but only `wacc` scalar used |
| **§31 Black Swan** | Shock correlations, tail distributions, expert elicitations | `module_31_black_swan_stress_test.csv` exists but not integrated into Monte Carlo |
| **§33 Renewal Cliff** | Contract expiration probability distributions, sector rotation timing | `enterprise_contracts.csv` has averages but no expiration schedule |
| **§34 Onsite Power** | Technology-specific degradation, fuel switching, water constraints, permitting | Partial: tech mix, heat rates, capacity factors used; degradation curves, water intensity, permitting timelines **ignored** |

---

## 5. Quantified Data Waste

| Metric | Value |
|--------|-------|
| **Total CSV records loaded** | ~2,500+ |
| **Total SEC quarterly facts processed** | ~8,000 |
| **Total LBNL queue projects analyzed** | ~10,000 |
| **Scalar parameters actually consumed by engine.js** | 25 |
| **Data utilization rate** | **< 1%** (by record count) |
| **Empty objects in param_overrides.js** | 10 (`adoptionMetrics`, `chinaMetrics`, `revenueQualityMetrics`, `semiconductorMetrics`, `agentsMetrics`, `regulatoryMetrics`, `laborMetrics`, `unitEconomicsMetrics`, `stressScenarioMetrics`, `macroMetrics.fred_catalog` metadata only) |

---

## 6. Recommended Integration Points

### High Impact / Low Effort
1. **Chinese competition module** (§8): Plug `china_benchmarks.csv` + `china_api_pricing.csv` into `priceCompression` and `openSourcePower` as time-varying functions
2. **Productivity by category** (§7, §21): Replace pooled `elasticityCoefficient` with task-type-specific elasticities from meta-analysis
3. **Revenue quality tiering** (§25): Use `enterprise_contracts.csv` NRR/GRR/expansion/downsizing by contract_type to parameterize `qualityCoeff`
4. **Regional infrastructure** (§16, §19): Use `regional_infrastructure.csv` cost_per_mw, cooling_water, transformer_shortage_factor, gov_coordination_index in region-specific power/capex constraints
5. **Onsite power degradation** (§34): Apply heat_rates.csv degradation_pct_yr to model efficiency decay over 20-year horizon

### Medium Effort
6. **Contract expiration distributions** (§17, §33): Synthesize expiration schedules from `enterprise_contracts.csv` avg lengths + renewal rates → feed `realContractSeed` in engine.js
7. **Fuel price term structure** (§34): Use `fuel_prices.csv` monthly data to model basis risk, seasonal hedging, volatility regimes
8. **Grid services revenue stack** (§34): Model regulation vs spinning vs capacity markets separately with ISO-specific price trajectories
9. **Black Swan correlations** (§31): Parse `module_31_black_swan_stress_test.csv` into Monte Carlo correlation matrix

### High Effort (Requires New Data)
10. **Agent-level enterprise data** (§11, §18): Need primary research on agent deployment counts, TCO, liability costs
11. **Labor market transformation** (§27): Need O*NET × AI exposure mapping + BLS displacement data
12. **Adoption diffusion curves** (§29): Need survey/telemetry data by segment
13. **Macro feedback loops** (§30): Need structural VAR or DSGE integration

---

## 7. Files to Investigate for Missing Data

| Expected File (per calibrate.py) | Status | Notes |
|----------------------------------|--------|-------|
| `DATA/technology_parameters.csv` | Loaded but empty DataFrame | File exists? |
| `DATA/calibration_parameters.csv` | Loaded but empty DataFrame | Reference only |
| `DATA/productivity/meta_analysis_studies.csv` | ✅ 16 records | Duplicate of root `productivity_meta_analysis.csv` |
| `DATA/wholesale_electricity_prices.csv` | Loaded, never used | Hourly hub prices — high value for §34 |
| `DATA/grid_connection_delays.csv` | Loaded, never used | Project-level — high value for §16, §19 |
| `DATA/transformer_shortage.csv` | Loaded, never used | Lead times, capacity — high value for §19 |
| `DATA/carbon_prices.csv` | Loaded, never used | Jurisdictional time-series — high value for §34 |

---

*Analysis based on: `calibrate.py` (646 lines), `engine.js` (753 lines), `param_overrides.js` (1,800+ lines), and all CSV files in `DATA/` directory*