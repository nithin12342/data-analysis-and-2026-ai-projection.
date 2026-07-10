# TESM Data Gap Analysis: What's Still Missing

**Generated:** 2026-07-10  
**Status:** Post-calibration v3.0 (14 data categories ingested)  
**Benchmark:** CONTEXT.md §1-33 (33 modules) as single source of truth

---

## Executive Summary

| Metric | Value |
|--------|-------|
| **CONTEXT.md modules requiring data** | 33 |
| **Modules with ≥1 empirical anchor** | 21 (64%) |
| **Modules with deep/granular data** | 8 (24%) |
| **Modules with proxy/placeholder only** | 12 (36%) |
| **Critical gaps (block publication-grade)** | 7 |

**Bottom line:** The model now has *broad* empirical coverage but *shallow* depth in key modules. Publication-grade rigor requires closing 7 critical gaps.

---

## Module-by-Module Gap Matrix

### ✅ **Well-Anchored (Empirical time-series + cross-section)**

| CONTEXT § | Module | Data Present | Quality |
|-----------|--------|--------------|---------|
| §5 | **CapEx Model** | SEC CapEx (13Q × 6 cos), LBNL queue, USITC silicon | ★★★★☆ |
| §13 | **Financial Modeling** | Revenue, RPO, CapEx, CAGR, downsizing ratio | ★★★★☆ |
| §16 | **Global Infrastructure** | LBNL 10,775 projects, queue days, withdrawal rates | ★★★★☆ |
| §19 | **Physical Constraints** | Grid connection delay, power growth cap, transformer shortage | ★★★★☆ |
| §23 | **Compute Supply Cycle** | Quarterly wafer/packaging/HBM/GPU/DC build tracker | ★★★★☆ |
| §25 | **Revenue Quality** | 31 contract types mapped to High/Med/Low tiers | ★★★★☆ |
| §31 | **Black Swan/Stress** | 20 scenarios + 8 historical backtests + 31 combos | ★★★★☆ |
| §33 | **Enterprise Renewal Cliff** | Contract queue (3yr/5yr), renewal multipliers, RPO maturity | ★★★★☆ |

---

### ⚠️ **Partially Anchored (1-2 data points, needs depth)**

| CONTEXT § | Module | Data Present | Missing Depth |
|-----------|--------|--------------|---------------|
| §1 | **Historical Comparison** | Dot-com/Japan/Railway/Telecom/GFC/Cloud/Smartphone/Semi backtests | Dot-com cohort financials (50+ tickers × 1995-2002); IPO quality metrics; VC fundraising vintage |
| §2 | **Company Universe** | 6 hyperscalers only | 94 missing tickers: semis (15), enterprise AI (20), infra (15), AI model providers (8 pure-play private), Chinese publics (10) |
| §3 | **IPO Quality** | `insolvencyWriteDownRate=0.10` placeholder | Zero AI IPO cohort analysis (ARM, KLAR, RBLX, ABNB, COIN, HOOD, etc.); no S-1 parsing |
| §4 | **AI Adoption Model** | 31 vendor-reported metrics (MAU, seats, API calls) | No token-volume time-series; no free→paid conversion funnels; no inference vs training demand split; no consumer vs enterprise S-curves |
| §6 | **AI Efficiency** | `costReductionRate=0.38`, `priceCompression`, `openSourcePower` | No per-model inference cost curves; no distillation/quantization/MoE adoption rates; no GPU utilization (MFU) telemetry |
| §7 | **Productivity Gains** | 20 studies with effect sizes (meta-analysis) | **Critical:** No industry-level ROI distributions; no displacement vs augmentation split; no wage/employment elasticity estimates |
| §8 | **Chinese AI Competition** | 16 LMSYS/OpenCompass Elo scores + 31 API prices | No GPU access/allocation data (H100/H800/A800); no domestic semi supply chain; no model-market-share dynamics |
| §9 | **PPP Adjustment** | Single `pppAdjustment` scalar (0.55) | **Critical:** No category-level PPP (labor, electricity, construction, hardware, opex); no city-tier granularity |
| §10 | **Demand Shock Scenarios** | Monte Carlo varies `elasticityCoefficient`, `priceCompression`, `powerGrowthCap` | No narrative scenarios with probability weights; no survey-based prior on demand elasticity |
| §11 | **Enterprise AI Agents** | 42 verified deployment counts (Google 1,302, SF 20k, etc.) | No task-level automation rates; no gross vs net productivity (oversight/validation costs); no industry-specific ROI |
| §12 | **Workflow Integration** | `switchingCost` in INDUSTRIES only | No automation rates by workflow (CRM, ERP, DevOps, CS); no integration depth/stickiness metrics |
| §17 | **Contract Lag** | 3yr/5yr queues, renewal multiplier | No GPU-specific reservation expiry schedule; no enterprise budgeting cycle seasonality; no multi-cloud allocation |
| §18 | **Agentic Liability** | `tcoMultiplier`, `complianceFriction`, `complianceCost`, `liabilityRisk` per industry | No task-level oversight cost; no validation pipeline compute; no insurance/legal exposure quantification |
| §20 | **Systems Dynamics** | 5 of 16 feedback loops implemented | Missing: productivity→wages→demand; regulation→innovation→competition; geopolitics→supply→pricing; talent→R&D velocity→innovation |
| §21 | **Jevons Paradox** | `elasticityCoefficient` drives `volumeExpansion` | **Critical:** No empirical ε estimate; no cross-price elasticity (open vs closed); no rebound decomposition |
| §22 | **Open-Source Commoditization** | `openSourcePower` drives `priceCompression` | No model quality convergence tracking (closed vs open Elo gap over time); no time-to-frontier-lag; no fine-tuning ecosystem metrics |
| §24 | **Capital Market Reflexivity** | `capitalReflexivity` in sentiment update | No equity issuance model; no hiring→CapEx lag; no analyst coverage/revisions feedback |
| §26 | **National Strategic Investment** | `nationalStrategicInvestment=1.5` multiplier | No CHIPS Act/IRA/EU Chips Act/China 14th Plan appropriation tracking; no export control impact modeling |
| §27 | **Labor Market** | O*NET × Felten exposure (55 occupations) | **Critical:** No displacement probability distributions; no wage Phillips curve by skill; no reskilling cost/ROI; no new occupation emergence |
| §28 | **Regulatory Scenarios** | 14 jurisdiction × rule matrix with compliance costs | No enforcement probability dynamics; no compliance cost learning curves; no cross-border data flow friction |
| §29 | **Adoption Diffusion** | Linear `adoptionRate` only | **Critical:** No Bass/Gompertz S-curves per segment (consumer, SME, enterprise, gov, edu, healthcare, mfg); no network effects; no org resistance |
| §30 | **Global Macro Feedback** | One-way `gdpBoost = softwareRevenues × 0.005` | **Critical:** No VAR/DSGE linkage; no monetary policy reaction function; no energy price ↔ AI demand feedback; no FX/capital flow channel |

---

### ❌ **No Empirical Anchor (Pure Placeholder)**

| CONTEXT § | Module | Current Implementation |
|-----------|--------|------------------------|
| §14 | **Detailed Calculations** | Equations buried in JS; no LaTeX export; no assumption registry; no reproducible notebook |
| §15 | **Final Assessment** | 10 questions answered in `report.md` but engine doesn't output: bubble severity index, sector z-scores, company resilience rankings, crash/stagnation/expansion probabilities |
| §32 | **Integrated TESM** | 20-yr forecasts + percentiles + scenario matrix | No confidence intervals (only percentiles); no Sobol sensitivity indices; no driver attribution; no rolling validation |

---

## 7 Critical Gaps Blocking Publication-Grade

| # | Gap | Why It Blocks | Effort to Close |
|---|-----|---------------|-----------------|
| **1** | **Company-level panel (100+ tickers × 20Q)** | §1, §2, §3, §13, §15 require company-level valuation, IPO quality, sector concentration | 4 weeks + $15K (Compustat/CRSP) or SEC DERA bulk download expansion |
| **2** | **Productivity meta-analysis → Bayesian priors** | §7, §11, §27 need credible ROI distributions, not point estimates | 8 weeks + $100K (systematic review + 2 RAs) |
| **3** | **Adoption S-curves per segment** | §4, §10, §29, §33 need diffusion dynamics, not linear rates | 4 weeks + Gartner/IDC subscription ($200K) or primary survey |
| **4** | **Chinese infrastructure & GPU access costs** | §8, §9, §16, §19 need city-tier DC costs, H100/H800 allocation, domestic semi supply | 3 months + China primary research partnerships |
| **5** | **Revenue quality: contract-type → RPO maturity** | §17, §25, §33 need GPU reservation expiry, multi-cloud allocation, renewal distributions | 2 weeks (cloud pricing APIs + 10-K segment note parsing) |
| **6** | **Macro VAR/DSGE linkage** | §30 requires two-way GDP↔AI investment feedback, monetary policy reaction | 2 months (FRB/US or NiGEM interface) |
| **7** | **Discrete stress scenario engine** | §31 needs narrative shocks with correlations, not just parametric Monte Carlo | 1 month (expert elicitation + copula calibration) |

---

## Data Acquisition Priority Queue

| Phase | Target | Cost | Time | Owner |
|-------|--------|------|------|-------|
| **P0 (Weeks 1-4)** | Expand SEC DERA to 100 tickers × 20Q; add SaaS benchmarks | $50K | 4 wks | Data Engineer |
| **P0** | Productivity systematic review (50 studies) | $100K | 8 wks | Quant Researcher + 2 RAs |
| **P1 (Weeks 5-12)** | Gartner/IDC/Morgan Stanley CIO survey access | $200K | 12 wks | Procurement |
| **P1** | Chinese DC cost survey (Tier 1/2/3 cities) | $100K | 3 mo | BD Lead + Local Partner |
| **P1** | Cloud contract taxonomy automation (RI/SP/CUD/EA mapping) | $40K | 4 wks | Data Engineer |
| **P2 (Months 4-6)** | Macro VAR integration (FRB/US or NiGEM) | $60K | 8 wks | Macro Economist |
| **P2** | Discrete stress scenario expert elicitation (Delphi) | $150K | 4 mo | 15-20 domain experts |
| **P2** | Agent deployment telemetry partnerships (NDA) | Partnership | 6-18 mo | BD Lead |
| **P3 (Months 7-12)** | Unit economics primary research (vendor NDA) | Partnership | 6-18 mo | Quant + Vendor Relations |
| **P3** | Black swan scenario library expansion | $100K | 4 mo | Risk Analyst |

**Total estimated: $1.3M - $2.0M over 12 months**

---

## Quick-Start: What You Can Add *This Week* (No Budget)

| File to Create | Source | Method |
|----------------|--------|--------|
| `DATA/company_universe/ticker_map.csv` | SEC CIK lookup + manual curation | Map 100 AI-relevant tickers → CIK → SIC/NAICS |
| `DATA/adoption/token_volume_proxy.csv` | Hugging Face API + GitHub Archive | Daily model downloads, stars, forks as usage proxies |
| `DATA/china/gpu_allocation_estimates.csv` | SemiAnalysis reports + earnings calls | H100/H800/A800 China allocation by quarter |
| `DATA/regulatory/enforcement_actions.csv` | EU AI Act tracker + BIS Federal Register | Fines, orders, guidance dates by jurisdiction |
| `DATA/labor/occupation_displacement.csv` | Acemoglu/Restrepo replication + BLS CPS | Displacement probability × wage change by SOC |
| `DATA/unit_economics/inference_benchmarks.csv` | Artificial Analysis + SemiAnalysis public | Cost/token × model × context × batch × hardware |
| `DATA/stress_scenarios/expert_priors.csv` | Internal team survey (5-min Google Form) | Probability/magnitude for 20 shock categories |

---

## Appendix: Current DATA/ Inventory

```
DATA/
├── 2023q1-2026q1/          # SEC DERA (13 quarters × 4 files each) ✅
├── adoption/
│   └── vendor_reported_metrics.csv          (31 records) ✅
├── china/
│   ├── model_benchmarks.csv                 (16 records) ✅
│   └── api_pricing.csv                      (31 records) ✅
├── productivity/
│   └── meta_analysis_studies.csv            (20 studies) ✅
├── revenue_quality/
│   ├── cloud_contract_mapping.csv           (31 types) ✅
│   └── saas_benchmarks.csv                  (10 ARR bands) ✅
├── macro/
│   ├── fred_core_series.csv                 (current values) ✅
│   └── fred_series_catalog.csv              (22 series) ✅
├── semiconductor/
│   └── supply_chain_quarterly.csv           (13 quarters) ✅
├── agents/
│   └── deployment_counts.csv                (42 records) ✅
├── regulatory/
│   └── jurisdiction_rule_matrix.csv         (28 rules) ✅
├── labor/
│   └── onet_ai_exposure.csv                 (55 occupations) ✅
├── unit_economics/
│   ├── training_costs.csv                   (20 models) ✅
│   ├── inference_costs.csv                  (30 configs) ✅
│   ├── gpu_economics.csv                    (18 SKUs) ✅
│   └── saas_benchmarks.csv                  (10 bands) ✅
├── stress_scenarios/
│   ├── stress_scenarios.csv                 (20 shocks) ✅
│   ├── historical_backtest.csv              (8 episodes) ✅
│   └── scenario_matrix.csv                  (31 combos) ✅
└── [14 missing directories - see priority queue above] ❌
```

---

## Next Steps

1. **Run P0 acquisitions** (SEC expansion + productivity review) — these unlock §1, §2, §3, §7, §13, §15
2. **Automate cloud contract taxonomy** — unlocks §17, §25, §33
3. **Commission Delphi stress elicitation** — unlocks §31 publication-grade
4. **Secure Gartner/IDC access** — unlocks §4, §10, §29
5. **Build VAR/DSGE bridge** — unlocks §30 (the only way to claim macro feedback)

*Without these, the model remains a sophisticated calibrated simulation — not a publication-grade techno-economic assessment.*