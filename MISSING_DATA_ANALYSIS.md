# Missing Data Analysis: DATA Folder vs CONTEXT.md Requirements

**Generated:** 2026-07-10  
**Standard:** CONTEXT.md as single source of truth  
**Scope:** Every data requirement in CONTEXT.md → mapped to DATA/ availability

---

## Summary

| Category | CONTEXT.md Requirements | DATA/ Coverage | Missing Data Items |
|----------|------------------------|----------------|-------------------|
| **Company Financials** | §1, §2, §3, §13, §15 | ✅ SEC DERA (13 quarters, 6 hyperscalers) | Private AI cos, semis, enterprise AI, IPO prospectuses |
| **Grid/Infrastructure** | §5, §16, §19, §23 | ✅ LBNL Queue (10,775 projects) | Transmission topology, water/cooling, labor, permitting distributions |
| **Semiconductor Supply** | §5, §19, §23 | ✅ USITC HTS 854231/32/90 (quarterly 2023-26) | Wafer-level capacity, packaging allocation, HBM spot prices, lead times |
| **AI Adoption/Usage** | §4, §10, §11, §12, §29 | ❌ **ZERO** | Token volumes, API call counts, free/paid tiers, enterprise seat counts, agent deployments |
| **Productivity Evidence** | §7, §11 | ❌ **ZERO** | Academic studies, labor displacement measurements, ROI case studies |
| **Chinese AI Competition** | §8, §9 | ❌ **ZERO** | Model benchmarks (LongCat, GLM, Ornite), API pricing, DC costs, PPP breakdowns |
| **Revenue Quality** | §25 | ❌ **ZERO** | Contract-type mapping (reserved/on-demand/spot/pro-services), churn/expansion |
| **Regulatory Scenarios** | §28 | ❌ **ZERO** | Jurisdiction×rule matrix, compliance costs, enforcement probabilities |
| **Macro Feedback** | §30 | ❌ **ZERO** | GDP/inflation/rates/FX time series, energy prices, commodity indices |
| **Black Swan/Stress** | §31 | ❌ **ZERO** | Historical crisis chronologies, shock magnitudes, correlation matrices |
| **Labor Market** | §27 | ❌ **ZERO** | O*NET task-AI exposure, displacement surveys, wage Phillips curves |
| **Unit Economics** | §13, §14 | ❌ **ZERO** | Per-model training cost, per-API inference cost, per-GPU economics |

**Total Missing Data Categories: 11/16 (69%)**

---

## Detailed Missing Data by CONTEXT.md Section

---

### §1 Historical Comparison (16 Dimensions)

| Dimension | Required Data | DATA/ Status | Missing |
|-----------|---------------|--------------|---------|
| Company valuations | Market cap, EV, P/E, P/S for dot-com (1995-2002) & AI (2023+) cohorts | ❌ | CRSP/Compustat historical; current: FactSet/Refinitiv/API |
| Revenue growth | Quarterly revenue by company | ⚠️ SEC DERA (hyperscalers only) | Non-hyperscaler AI cos; dot-com cohort |
| Profitability | Net income, EBITDA, FCF margins | ⚠️ SEC DERA (hyperscalers only) | Same as above |
| Free cash flow | Operating CF - CapEx | ⚠️ SEC DERA (hyperscalers only) | Same |
| Earnings multiples | Forward/Trailing P/E | ❌ | IBES estimates; current market data |
| Price-to-sales | EV/Sales, P/S | ❌ | Market data + revenue |
| Market concentration | HHI, CR4, CR8 by sector | ❌ | Revenue breakdown by company |
| CapEx | Quarterly CapEx by company | ⚠️ SEC DERA (hyperscalers only) | Non-hyperscalers; dot-com era |
| Investor sentiment | Surveys, flows, VIX, put/call | ❌ | AAII, ICI, EPFR, CBOE data |
| IPO quality | S-1 financials, lockups, underwriters | ❌ | EDGAR S-1 parsing; Renaissance Capital IPO data |
| VC investment | Deal count, $ volume, stage, sector | ❌ | PitchBook, Crunchbase, NVCA |
| Public market financing | SEO, convertible, ATM volume | ❌ | SDC Platinum, Dealogic |
| Retail speculation | Robinhood/Reddit activity, margin debt | ❌ | FINRA margin stats; alternative data |
| Institutional investment | 13F holdings, flows | ❌ | WhaleWisdom, 13F filings |
| Debt levels | Total debt, net debt, maturity profile | ⚠️ SEC DERA (hyperscalers only) | Non-hyperscalers; dot-com |
| Interest rate environment | Fed funds, 10Y, yield curve, credit spreads | ❌ | FRED, Treasury, ICE BofA indices |

**Missing: 14/16 dimensions for full company universe**

---

### §2 Company Universe (5 Categories × Sub-types)

| Category | Required Companies | DATA/ Status | Missing Data Source |
|----------|-------------------|--------------|---------------------|
| **AI Model Providers** | OpenAI, Anthropic, Mistral, Cohere, AI21, Inflection, xAI, Adept, Character.ai, Stability, Midjourney, Runway, Hugging Face (private) | ❌ **ZERO** | Private market data (PitchBook, Forge, Caplight); earnings calls if public |
| **Frontier Model Cos** | Google (DeepMind), Meta (FAIR), Microsoft (OpenAI partnership), Amazon (Bedrock/Titan) | ⚠️ Partial (SEC) | Segment revenue attribution (not in 10-K) |
| **Mid-sized AI** | Palantir, C3.ai, DataRobot, Scale AI, Databricks, Weights & Biases | ❌ Mostly private | Private data; PLTR/CRM/DBNR public but not AI-segmented |
| **Small AI Startups** | 500+ YC/Sequoia/A16Z portfolio cos | ❌ | Crunchbase/PitchBook API |
| **Open-source AI** | Meta (Llama), Mistral, Falcon, BLOOM, Stable Diffusion, BERT variants | ❌ | GitHub stars, HF downloads, Papers with Code |
| **Semiconductors** | NVDA, AMD, AVGO, MRVL, TSM, INTC, QCOM, ARM, NXPI, ON, LRCX, KLAC, AMAT, ASML | ❌ **ZERO in DATA/** | SEC DERA available but not downloaded; need 13 quarters × 15 tickers |
| **Cloud Infrastructure** | AMZN (AWS), MSFT (Azure), GOOGL (GCP), ORCL, IBM, ALIBABA, TENCENT | ⚠️ Partial (3/7 in SEC) | Need all 7; segment cloud revenue |
| **AI Infrastructure** | ANET, ARSTA, CISCO, JNPR, VRT, VNT, ENPH, SSD, PSTG, NTAP, DELL, HPE, SMCI | ❌ **ZERO** | SEC DERA available but not downloaded |
| **Enterprise AI** | CRM, NOW, SNOW, PLTR, DATA, DDOG, SPLK, TEAM, ATLAS, MNDY, ASAN, ZS, OKTA, PANW | ❌ **ZERO** | SEC DERA available but not downloaded |

**Missing: ~100+ company financial histories (13 quarters each)**

---

### §3 IPO Quality Analysis

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| AI IPO cohort (2020-2026): ARM, KLAR, RBLX, ABNB, COIN, HOOD, etc. | ❌ | Renaissance Capital IPO database; SEC S-1 filings |
| Pre-IPO financials (S-1): revenue, burn, margins, retention | ❌ | EDGAR S-1 parsing (XBRL or HTML) |
| Post-IPO performance: 1-day, 1-month, 1-year, 3-year returns | ❌ | CRSP daily returns |
| Lockup expiration dates, insider selling | ❌ | SEC Form 4, 144 filings |
| Underwriter quality (Goldman/MS/JPM tier) | ❌ | SDC Platinum |
| VC backing pre-IPO (tier, # rounds, $ raised) | ❌ | PitchBook/Crunchbase |
| Dot-com IPO cohort (1995-2000) for comparison | ❌ | Jay Ritter IPO data; historical CRSP |

---

### §4 AI Adoption Model

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| Free-tier users: MAU/DAU by product (ChatGPT, Claude, Copilot, Gemini) | ❌ | Company disclosures; Sensor Tower; SimilarWeb |
| Paid subscriptions: $20/mo (Plus), $30/mo (Pro), enterprise seats | ❌ | Earnings calls; investor presentations |
| Enterprise adoption: seat counts, ACV, NRR by vendor | ❌ | Gartner/IDC/Forrester reports; vendor 10-K |
| Consumer adoption: household penetration, frequency | ❌ | Pew Research; Census Bureau surveys |
| Token usage: billions tokens/day by model, by tier | ❌ | **Only vendors have this** (OpenAI, Anthropic, Google) |
| Inference demand: API calls/day, latency p50/p99 | ❌ | Vendor telemetry; Datadog/CloudWatch aggregates |
| Training demand: GPU-hours, model count, parameter scale | ❌ | MLPerf; vendor disclosures; SemiAnalysis estimates |
| Revenue conversion: free→paid funnel, enterprise close rates | ❌ | Vendor investor decks; S-1s |

**Missing: 100% — No adoption telemetry in DATA/**

---

### §5 CapEx Model (Physical Units)

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| AI chip units: H100/H200/B200/MI300/TPU v5/v6 volumes by quarter | ❌ | NVDA/AMD/GOOGL earnings; SemiAnalysis; Omdia |
| Data center count: new builds, MW capacity, rack density | ❌ | DC Byte; Structure Research; Synergy Research |
| Networking: 400G/800G port shipments, InfiniBand vs Ethernet | ❌ | Dell'Oro Group; Crehan Research |
| Power infrastructure: transformer orders, substation builds, UPS | ❌ | LBNL has queue; no equipment-level data |
| Cooling: liquid cooling deployments, CDU units, chiller capacity | ❌ | Omdia; vendor data (Vertiv, Schneider, Delta) |
| Cloud expansion: new regions, AZs, capacity MW by provider | ❌ | Provider blogs; Gartner Magic Quadrant notes |

**Missing: Physical unit counts — SEC only gives $ CapEx**

---

### §6 AI Efficiency Model

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| Inference cost/token: historical trajectory by model class | ❌ | SemiAnalysis; Artificial Analysis; vendor pricing history |
| Model architecture efficiency: Chinchilla scaling law params | ❌ | Papers: Kaplan et al. 2020; Hoffmann et al. 2022 |
| Distillation gains: teacher→student compression ratios | ❌ | ArXiv distillation papers; vendor blogs |
| Quantization: INT8/INT4/FP8 vs FP16 accuracy/latency tradeoffs | ❌ | MLPerf Inference results; Hugging Face benchmarks |
| Sparse MoE: expert count, activation sparsity, FLOP reduction | ❌ | Switch Transformer; GLaM; MegaBlocks papers |
| GPU utilization: MFU/achieved FLOPS by workload, cluster size | ❌ | NVIDIA DCGM; vendor disclosures; MosaicML blogs |
| Energy consumption: kWh/token, PUE by data center generation | ❌ | IEA; Google/Microsoft/Amazon sustainability reports |

**Missing: 100% — Technical efficiency data not in financial/grid/trade data**

---

### §7 Productivity Gains (Academic Evidence)

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| **Meta-analysis dataset**: 50+ studies with effect sizes, SEs, contexts | ❌ | Systematic literature review (Google Scholar, SSRN, NBER) |
| Brynjolfsson et al. (2023) - Generative AI at work | ❌ | NBER WP 31161 |
| Noy & Zhang (2023) - Writing productivity | ❌ | Science 381(6654) |
| Dell'Acqua et al. (2023) - BCG consultant study | ❌ | HBS Working Paper |
| Peng et al. (2023) - GitHub Copilot coding | ❌ | ArXiv 2302.06590 |
| Cui et al. (2024) - Customer support agents | ❌ | Quarterly Journal of Economics |
| Industry-specific: legal (Casetext), medical (Ambience), coding (Cursor) | ❌ | Vendor case studies; peer-reviewed replications |
| Labor displacement: occupation-level exposure (Felten/Raj/Seamans) | ❌ | O*NET × AI exposure mapping |
| Wage effects: skill premium, automation elasticity | ❌ | Acemoglu & Restrepo (2018, 2020, 2022) |
| ROI measurements: $ invested → $ saved/generated | ❌ | Vendor TCO calculators; Forrester TEI studies |

**Missing: 100% — Requires systematic literature review**

---

### §8 Chinese AI Competition

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| Model benchmarks: LongCat 2.0, GLM 5.2, Ornite 397B, DeepSeek, Qwen, Yi, Baichuan | ❌ | LMSYS Chatbot Arena; OpenCompass; C-Eval; CMMLU; HF Leaderboard |
| API pricing: Zhipu, Baichuan, 01.ai, Moonshot, MiniMax vs OpenAI/Anthropic | ❌ | Vendor pricing pages; China AI pricing trackers |
| Open-weight adoption: HF downloads, GitHub stars, fine-tune count | ❌ | Hugging Face API; GitHub API |
| Chinese DC costs: land, power, construction, labor by city (Tier 1/2/3) | ❌ | China Statistical Yearbook; local gov't reports; JLL/CBRE China |
| PPP breakdown: labor, electricity, construction, hardware, opex by category | ❌ | World Bank ICP 2021; Penn World Tables 10.0 |
| GPU access: H100/H800/A800 allocation, domestic alternatives (Huawei Ascend, Cambricon, Biren) | ❌ | SemiAnalysis China reports; BIS 744 filings |
| Regulatory: Interim Measures compliance costs, filing requirements | ❌ | CAC announcements; law firm analyses (Zhong Lun, King & Wood) |

**Missing: 100% — No Chinese data in DATA/**

---

### §9 PPP Adjustment

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| PPP conversion factors by expenditure category (labor, energy, construction, equipment) | ❌ | World Bank ICP; OECD PPP; Penn World Tables |
| City-level cost indices: Beijing/Shanghai/Shenzhen vs San Francisco/Austin/Seattle | ❌ | Numbeo; Expatistan; local salary surveys |
| Electricity industrial rates by province/state | ❌ | EIA (US); NBS/NEAC (China); IEA global |
| Construction cost per MW data center by region | ❌ | DC Byte; Turner & Townsend; Linesight |
| Engineering salary bands by experience, specialty, city | ❌ | Levels.fyi; Glassdoor; Payscale; Radford (China) |

---

### §10 Demand Shock Scenarios

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| Historical demand elasticity estimates for: cloud, semiconductors, software | ❌ | NBER papers; IMF/World Bank studies; vendor analyst models |
| Survey data: enterprise AI budget intent (Gartner, IDC, Morgan Stanley CIO survey) | ❌ | Gartner/IDC subscription; MS CIO survey PDFs |
| Consumer sentiment: AI trust, adoption willingness (Pew, Edelman, KPMG) | ❌ | Pew Research; Edelman Trust Barometer |
| Scenario narratives with probability weights (expert elicitation) | ❌ | Delphi study; Superforecaster surveys; Good Judgment Project |

---

### §11 Enterprise AI Agent Deployment

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| Agent counts: Google 1,302, Salesforce 20,000 — verified, dated | ❌ | Earnings calls (exact quotes); investor days; blog posts |
| Task automation: % of tickets resolved, code committed, emails drafted | ❌ | Vendor case studies (Intercom Fin, Sierra, Ada, Decagon) |
| Labor replacement vs augmentation: FTE reduction, role transformation | ❌ | Company disclosures; academic studies (Brynjolfsson et al.) |
| ROI: $ cost/agent vs $ saved, payback period | ❌ | Vendor TCO; Forrester TEI; Nucleus Research |
| Industry deployment: banking (JPM IndexGPT), healthcare (Epic), legal (Harvey) | ❌ | Press releases; conference talks; vendor customer lists |

---

### §12 Workflow Integration

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| Automation rates by workflow: CRM (lead→opp), ERP (PO→pay), DevOps (commit→deploy), CS (ticket→resolution) | ❌ | UiPath/Automation Anywhere/Blue Prism process mining data |
| Task completion time: pre-AI vs post-AI by role | ❌ | Time-motion studies; vendor telemetry |
| Switching costs: migration effort, data gravity, retraining | ❌ | Gartner TCO models; customer reference calls |
| Integration depth: API calls/day, webhook volume, embedded vs sidecar | ❌ | Vendor partner programs; MuleSoft/Workato/Zapier data |

---

### §13 Financial Modeling — Unit Economics

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| Per-model training cost: GPT-4, Claude 3, Llama 3, Gemini 1.5 | ❌ | SemiAnalysis; Epoch AI; vendor leaks |
| Per-API-call inference cost: by model, by context length, by batch | ❌ | Artificial Analysis; vendor pricing; own benchmarking |
| Per-GPU economics: H100 80GB hourly cost (cloud vs on-prem), utilization breakeven | ❌ | Lambda Labs; RunPod; CoreWeave; AWS/Azure/GCP pricing |
| Per-seat enterprise SaaS: CAC, LTV, gross margin, churn by tier | ❌ | SaaS Capital; KeyBanc; ICONIQ benchmarks |
| Cash flow waterfall: revenue → COGS → S&M → R&D → FCF by segment | ⚠️ Partial (SEC) | Need segment P&L (not in 10-K for most) |

---

### §14 Detailed Calculations — Transparency

| Required Artifact | DATA/ Status | Missing |
|-------------------|--------------|---------|
| Assumption registry: every parameter, source, date, confidence | ❌ | Not in DATA/; `param_overrides.js` has values not sources |
| Equation LaTeX export: every formula in engine.js | ❌ | Not generated |
| Intermediate calculation trace: quarter-by-quarter for audit | ❌ | Engine returns history but not formula trace |
| Sensitivity table: every param ±10% → output delta | ❌ | Monte Carlo does distribution not one-way sensitivity |
| Reproducible notebook: input → output for every figure | ❌ | Not created |

---

### §16 Global Infrastructure Deployment

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| Permitting timelines: environmental, zoning, interconnection by country/state | ❌ | LBNL has queue dates; no permitting breakdown |
| Land availability: acres, cost, proximity to fiber/power/water | ❌ | LoopNet; Crexi; county GIS; Data center site selection firms |
| Water rights: gallons/day, cost, recycling rate by region | ❌ | USGS; state water boards; China Ministry of Water Resources |
| Workforce: electricians, fiber splicers, HVAC techs, commissioning engineers | ❌ | BLS OES; China NBS; Associated Builders & Contractors |
| Government coordination index: central planning vs market, subsidy $/MW | ❌ | IEA policy database; CHIPS Act tracking; EU Chips Act; China 14th Plan |

---

### §17 Enterprise Contract Lag

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| GPU reservation contracts: H100 reserved instances, 1yr/3yr terms, pricing | ❌ | AWS/GCP/Azure reserved instance pricing pages; CoreWeave/Lambda contracts |
| Enterprise budgeting cycles: federal (Oct-Sep), calendar (Jan-Dec), quarterly locks | ❌ | Gartner IT spending surveys; CIO interviews |
| Contract renewal probability distributions (not point estimates) | ❌ | Need parametric fit to RPO maturity schedule |
| Multi-cloud allocation: % spend per provider, portability clauses | ❌ | Flexera State of Cloud; RightScale; customer surveys |

---

### §18 Agentic Liability & Compliance Cost

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| Human oversight: FTE/agent, salary, training cost by risk tier | ❌ | BLS OES; vendor pricing (Scale AI, Surge, Labelbox) |
| Validation pipeline: compute, engineering, test cases per deployment | ❌ | MLOps vendor data (Weights & Biases, MLflow, ClearML) |
| Compliance monitoring: SOC2, HIPAA, GDPR, SOX, PCI-DSS per agent type | ❌ | Audit firm fee surveys (Big 4); Vanta/Drata pricing |
| Insurance: AI liability premiums, limits, exclusions by use case | ❌ | Marsh/Aon/Willis Towers Watson cyber/AI insurance quotes |
| Legal review: hours, rate, frequency for agent deployment | ❌ | Law firm AI practice billing data |
| Incident response: MTTR, cost/incident, reputational impact | ❌ | Verizon DBIR; Ponemon Institute; vendor post-mortems |

---

### §19 Physical Infrastructure Constraints (Beyond LBNL)

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| Transmission topology: line ratings, congestion, upgrade queue | ❌ | FERC Form 715; ISO/RTO planning studies; ENTSO-E |
| Substation transformer: 500kV/345kV/230kV lead times, inventory | ❌ | Hitachi/ABB/Siemens/GE order books; EEI surveys |
| Nuclear: SMR deployment timeline, licensing (NuScale, TerraPower, X-energy) | ❌ | NRC docket; IAEA ARIS; vendor roadmaps |
| Natural gas: pipeline capacity, Henry Hub basis, firm transport | ❌ | EIA; FERC; Platts; ICE |
| Renewable: solar/wind/battery interconnection queue by ISO (not just LBNL aggregate) | ⚠️ LBNL has this | Need ISO-specific (CAISO, PJM, ERCOT, MISO, NYISO, ISO-NE, SPP) |
| Water: cooling water availability, thermal discharge limits, drought risk | ❌ | USGS Water Use; state agencies; WRI Aqueduct |
| Skilled labor: union vs non-union, apprenticeship pipeline, prevailing wage | ❌ | BLS; North America's Building Trades Unions; China MOHRSS |

---

### §20 Systems Dynamics — 16 Feedback Loops

| Loop | Required Calibration Data | DATA/ Status |
|------|--------------------------|--------------|
| AI capability → efficiency gains → lower cost → adoption | Scaling laws; historical cost curves | ❌ |
| Adoption → revenue → CapEx → compute → capability | Semiconductor cycle; cloud CapEx | ⚠️ Partial |
| Revenue → R&D → model quality → pricing power | R&D intensity; patent citations | ❌ |
| Pricing pressure → margins → investment → capacity | Price elasticity; margin history | ❌ |
| Capacity → utilization → ROIC → sentiment → valuation | Utilization rates; ROIC decomp | ❌ |
| Valuation → equity issuance → hiring → CapEx | Equity issuance data; hiring plans | ❌ |
| Regulation → compliance cost → adoption → lobbying | Regulatory cost studies | ❌ |
| Geopolitics → export controls → supply → pricing | BIS 744; entity list changes | ❌ |
| Energy price → DC opex → cloud price → demand | PUE trends; electricity prices | ❌ |
| Productivity → wages → consumer demand → enterprise spend | Phillips curve; wage growth | ❌ |
| Talent supply → hiring cost → R&D velocity → innovation | H-1B data; grad output; LinkedIn | ❌ |
| Open-source → commoditization → API price → closed-model R&D | HF downloads; API pricing | ❌ |
| Insurance → risk mitigation → deployment speed → adoption | AI insurance market data | ❌ |
| Standards (IEEE, ISO, NIST) → interoperability → switching cost | Standards adoption tracking | ❌ |
| Education → talent pipeline → innovation → productivity | CS grads; bootcamp output | ❌ |
| Financial conditions → discount rate → NPV → investment | Fed funds; term premium; credit spreads | ❌ |

**Missing: Quantitative calibration for 14/16 loops**

---

### §21 Jevons Paradox — Elasticity

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| Historical cloud price elasticity: AWS/Azure/GCP price cuts → usage growth | ❌ | Cloud provider earnings; Gartner; Synergy Research |
| Cross-price elasticity: open-source vs closed API substitution | ❌ | HF download vs API usage correlation |
| Income elasticity: enterprise IT budget growth → AI spend share | ❌ | Gartner IT spending; CIO surveys |
| Rebound decomposition: direct (more usage) vs indirect (new apps) | ❌ | Requires microdata (not available) |

---

### §22 Open-Source Commoditization

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| Model quality convergence: closed vs open gap over time (LMSYS Elo) | ❌ | LMSYS Chatbot Arena historical snapshots |
| Time-to-frontier: days from closed SOTA to open replication | ❌ | Papers with Code; HF model cards; ArXiv dates |
| Fine-tuning ecosystem: LoRA count, dataset size, downstream tasks | ❌ | HF Hub stats; PEFT library downloads |
| Licensing distribution: Apache-2.0 vs MIT vs BSD vs proprietary | ❌ | HF model card license field; SPDX |
| Enterprise adoption: % using open-weight vs API (survey) | ❌ | Gartner/IDC; vendor win/loss data |
| Self-host TCO: GPU + eng + ops vs API cost at scale | ❌ | Lambda/RunPod/CoreWeave + eng salary |

---

### §23 Compute Supply Cycle

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| GPU lead times: H100/H200/B200/MI300 by quarter, by buyer tier | ❌ | SemiAnalysis; Omdia; vendor earnings calls |
| Wafer allocation: TSMC 4N/3nm capacity % to NVDA/AMD/GOOGL/AAPL | ❌ | TSMC earnings; SemiWiki; supply chain reports |
| Advanced packaging: CoWoS-S/CoWoS-R/L capacity, utilization | ❌ | ASE/Amkor/TSMC/SPIL earnings; TrendForce |
| HBM supply: SK Hynix/Samsung/Micron capacity, allocation | ❌ | TrendForce; DRAMeXchange; vendor earnings |
| Rack deployment: ODM (Quanta, Wiwynn, Inventec, Foxconn) build slots | ❌ | ODM earnings; Digitimes |
| Network equipment: 800G/1.6T switch ASIC (Broadcom/Marvell) capacity | ❌ | Broadcom/Marvell earnings; LightCounting |
| Cooling: CDU, manifold, chiller capacity by vendor (Vertiv, Schneider, Delta) | ❌ | Omdia; vendor earnings |
| Data center utilization: % rack occupied, power utilization, stranded | ❌ | DC Byte; Structure Research; provider disclosures |

---

### §24 Capital Market Reflexivity

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| Equity issuance: SEO, ATM, convertible by AI cos quarterly | ❌ | SDC Platinum; Dealogic; SEC 424B filings |
| Analyst coverage: initiation, upgrades, price targets, estimates | ❌ | IBES/Refinitiv; FactSet; Visible Alpha |
| Institutional flows: 13F changes, ETF flows (SMH, SOXX, IGV, BOTZ) | ❌ | WhaleWisdom; ETF.com; Bloomberg |
| Short interest: days to cover, utilization, borrow rate | ❌ | FINRA; IHS Markit; S3 Partners |
| Options flow: put/call ratio, gamma exposure, dealer positioning | ❌ | CBOE; SpotGamma; Dealer's Eye |

---

### §25 Revenue Quality Mapping

| Revenue Tier | Required Contract Mapping | DATA/ Status |
|--------------|---------------------------|--------------|
| **High Quality** | Reserved Instances (3yr All Upfront, 3yr Partial, 1yr) | ❌ |
| | Enterprise Agreements (EA/ELA): committed spend, multi-year | ❌ |
| | Professional Services: implementation, migration, support | ❌ |
| | Marketplace (ISV): recurring revenue share | ❌ |
| **Medium Quality** | Reserved Instances (No Upfront) | ❌ |
| | Savings Plans (Compute, EC2 Instance, SageMaker) | ❌ |
| | On-Demand (steady baseline) | ❌ |
| **Low Quality** | Spot/Preemptible/Interruptible | ❌ |
| | Free Tier / Always Free / Credits / Promotional | ❌ |
| | One-time: Data transfer, support incidents, training | ❌ |

**Missing: Cloud provider pricing pages + 10-K segment notes → no automated mapping**

---

### §26 National Strategic Investment

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| CHIPS Act: $52B — awarded, disbursed, by company, by project | ❌ | CHIPS Program Office; NIST; Commerce.gov |
| IRA: 48C tax credits, 45X manufacturing credits for AI hardware | ❌ | IRS guidance; Treasury; DOE LPO |
| EU Chips Act: €43B — national plans, IPCEI projects | ❌ | European Commission; national ministries |
| China 14th Five-Year Plan: AI/semiconductor funding, guidance funds | ❌ | NDRC; MIIT; local gov't guidance funds (国投, 中金资本) |
| Defense: DOD AI budget (JAIC, CDAO, Replicator), classified programs | ❌ | DOD budget justification books; CBO |
| Export controls: BIS 744.23/744.24 entity list, license denial rates | ❌ | BIS annual reports; Federal Register |
| Sovereign wealth: Temasek, GIC, Mubadala, ADIA, PIF AI investments | ❌ | SWF Institute; Preqin; SWF annual reports |

---

### §27 Labor Market Transformation

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| O*NET × AI exposure: Felten/Raj/Seamans (2021, 2023) occupation scores | ❌ | Author replication package; O*NET 28.0 |
| Displacement probability: by occupation, by automation technology | ❌ | Acemoglu/Restrepo replication; BLS CPS displaced worker supplement |
| Wage Phillips curve: unemployment → wage growth by skill group | ❌ | BLS CES; CPS; Atlanta Fed Wage Growth Tracker |
| Reskilling cost: $/worker, duration, completion rate by program | ❌ | WIOA data; Coursera/edX/Pluralsight enterprise; Guild Education |
| New occupations: prompt engineer, AI auditor, red teamer, model validator | ❌ | LinkedIn Emerging Jobs; Burning Glass; Lightcast |
| Labor share: GDP → compensation vs profits, by sector | ❌ | BEA NIPA; BLS LPC; OECD |

---

### §28 Regulatory Scenario Matrix

| Jurisdiction × Rule | Required Data | DATA/ Status |
|---------------------|---------------|--------------|
| **US** — EO 14110 | Compliance cost estimates by company size | ❌ |
| **US** — NIST AI RMF | Adoption rate, assessment cost | ❌ |
| **US** — SEC AI disclosure | 10-K AI risk factor prevalence | ❌ |
| **US** — Copyright (NYT v OpenAI) | Legal cost, licensing revenue | ❌ |
| **EU** — AI Act (Tier 1-4) | Conformity assessment cost, timeline | ❌ |
| **EU** — GDPR Art. 22 | Automated decision compliance cost | ❌ |
| **EU** — DSA/DMA | VLOP/VLOSE obligations for AI | ❌ |
| **China** — Interim Measures | Filing cost, security assessment, algorithm registry | ❌ |
| **China** — Data Security Law | Cross-border transfer assessment | ❌ |
| **UK** — AI White Paper | Regulatory sandbox, principles cost | ❌ |
| **India** — DPDP Act | Data localization, consent manager | ❌ |
| **Gulf** — UAE AI Strategy / KSA NCA | Regulatory sandbox, data sovereignty | ❌ |

**Missing: 100% — No regulatory tracking in DATA/**

---

### §29 AI Adoption Diffusion

| Segment | Required S-Curve Parameters | DATA/ Status |
|---------|----------------------------|--------------|
| Consumers | Bass p (innovation), q (imitation), saturation | ❌ |
| SMEs (<500 emp) | Adoption lag, network effects, budget constraint | ❌ |
| Large Enterprise | Pilot→production conversion, procurement cycle | ❌ |
| Government | FedRAMP/StateRAMP, acquisition reform, legacy lock-in | ❌ |
| Education | LMS integration, academic integrity, budget cycle | ❌ |
| Healthcare | HIPAA, FDA SaMD, clinical validation, liability | ❌ |
| Manufacturing | OT/IT convergence, PLC integration, safety certification | ❌ |

**Missing: 100% — No diffusion data**

---

### §30 Global Macro Feedback

| Variable | Required Time Series | DATA/ Status |
|----------|---------------------|--------------|
| Real GDP (quarterly, major economies) | 2000-present | ❌ FRED/OECD/World Bank |
| CPI/PCE/Core inflation | Monthly | ❌ FRED/BLS/Eurostat |
| Policy rates (Fed, ECB, BOJ, PBOC, BOE, RBI) | Daily/Monthly | ❌ Central bank websites |
| 10Y yields, term premium, credit spreads (IG/HY) | Daily | ❌ FRED/ICE/Bloomberg |
| USD Index (DXY), CNY, EUR, JPY, EM FX | Daily | ❌ FRED/Refinitiv |
| Oil (WTI/Brent), Gas (Henry Hub/TTF/JKM), Coal | Daily | ❌ EIA/IEA/Platts |
| Copper, Lithium, Cobalt, Rare Earths | Monthly | ❌ LME/SMM/Fastmarkets |
| Global PMI (Mfg/Services/Composite) | Monthly | ❌ S&P Global/IHS Markit |
| Capital flows (TIC, BOP, IIP) | Quarterly | ❌ Treasury/IMF/OECD |
| Geopolitical risk index (Caldara/Iacoviello, GPR) | Monthly | ❌ Author websites/FRED |

**Missing: 100% — No macro data in DATA/**

---

### §31 Black Swan & Stress Test

| Scenario | Required Calibration Data | DATA/ Status |
|----------|--------------------------|--------------|
| Global recession | Historical recession depth/duration (NBER dates) | ❌ NBER |
| Energy shortage | 1973/1979 oil crisis; 2022 Europe gas crisis | ❌ IEA; FRED |
| Semiconductor disruption | 2011 Thailand floods; 2021 Renesas fire; 2024 Taiwan quake | ❌ SemiAnalysis; insurance claims |
| Geopolitical conflict | 1990 Gulf War; 2022 Ukraine; Taiwan Strait scenarios | ❌ CSIS; RAND; DoD |
| Cybersecurity incident | NotPetya ($10B); SolarWinds; Colonial Pipeline | ❌ Verizon DBIR; Ponemon |
| AI safety failure | No precedent — expert elicitation only | ❌ |
| Financial crisis | 2008 GFC; 2020 COVID; 2023 SVB — credit spread widening | ❌ FRED; BIS |
| Regulatory intervention | GDPR (2018); China tech crackdown (2020-22) | ❌ Event studies |
| Algorithmic breakthrough | Transformer (2017); Chinchilla (2022); GPT-4 (2023) — paradigm shift magnitude | ❌ Citation analysis |
| Hardware breakthrough | EUV (2019); Chiplets (2020); 3D stacking — cost curve inflection | ❌ ITRS/IRDS; SemiWiki |
| Quantum computing | Shor's algorithm (1994); supremacy (2019) — crypto risk timeline | ❌ NIST PQC; NSA CNSA 2.0 |
| Fusion energy | NIF ignition (2022); ITER timeline — abundant energy scenario | ❌ ITER; DOE; Commonwealth Fusion |
| Sustained deflationary AI cost | Historical: Moore's Law; Dennard scaling — compute cost curves | ❌ Hennessy/Patterson; Our World in Data |

**Missing: 100% — No scenario calibration data**

---

### §32 Integrated TESM — Forecasting

| Required for 5/10/20yr Forecasts | DATA/ Status |
|----------------------------------|--------------|
| Confidence intervals (not just percentiles) | ❌ Bootstrap needed |
| Global sensitivity (Sobol indices) | ❌ SALib + 50K runs |
| Assumption-to-output attribution | ❌ Not implemented |
| Fan charts with scenario weights | ❌ Not implemented |
| Rolling validation (expanding window) | ❌ Not implemented |

---

### §33 Enterprise Renewal Cliff

| Required Data | DATA/ Status | Missing Source |
|---------------|--------------|----------------|
| Contract expiration probability distributions (Weibull/LogNormal fit to RPO) | ⚠️ `analyze_contracts.py` has point estimates | Need full RPO maturity schedule from 10-K notes |
| GPU reservation expiry schedule by provider | ❌ | Cloud provider reserved instance APIs |
| Renewal rate by cohort (vintage analysis) | ❌ | Need customer-level data (not public) |
| Sector rotation signals: factor model loadings (MKT, SMB, HML, RMW, CMA, UMD) | ❌ | Ken French library; AQR; MSCI Barra |
| Passive flow impact: index reconstitution, ETF creation/redemption | ❌ | ETF.com; BlackRock/iShares/Vanguard daily flows |

---

## Missing Data Acquisition Priority Matrix

| Priority | Category | Est. Cost | Est. Time | Source Type |
|----------|----------|-----------|-----------|-------------|
| **P0** | Company panel (100 tickers × 13Q SEC) | $50K | 4 weeks | SEC DERA (download more quarters/tickers) |
| **P0** | Semiconductor company financials (15 tickers × 13Q) | $30K | 3 weeks | SEC DERA |
| **P0** | Chinese model benchmarks (LMSYS/OpenCompass scrape) | $20K | 2 weeks | Public web scraping |
| **P0** | Productivity meta-analysis (50 studies) | $100K | 8 weeks | Literature review (RA + PI) |
| **P1** | Cloud revenue quality mapping (pricing pages + 10-K) | $40K | 4 weeks | Vendor sites + SEC |
| **P1** | Adoption diffusion surveys (Gartner/IDC access) | $200K | 12 weeks | Subscription purchase |
| **P1** | Regulatory scenario database build | $80K | 8 weeks | Legal RA + policy tracking |
| **P1** | Macro time series (FRED/OECD bulk download) | $10K | 1 week | Free API |
| **P2** | Physical unit data (GPU shipments, DC builds) | $500K+ | 6 months | Omdia/Synergy/Dell'Oro subscriptions |
| **P2** | Chinese DC cost surveys (Tier 1/2/3 cities) | $100K | 3 months | JLL/CBRE/China statistical yearbooks |
| **P2** | Agent deployment telemetry (vendor partnerships) | Partnership | 6-12 months | Vendor NDA |
| **P3** | Black swan scenario expert elicitation (Delphi) | $150K | 4 months | Superforecasters/Good Judgment |
| **P3** | Unit economics primary research (vendor NDA) | Partnership | 6-18 months | NVIDIA/Cloud vendors |

**Total Estimated Data Acquisition Budget: $1.3M - $2.0M**

---

## DATA/ Folder — What SHOULD Be Added

```
DATA/
├── sec_dera/
│   ├── hyperscalers/           # 6 cos × 13Q (EXISTS)
│   ├── semiconductors/         # 15 cos × 13Q (MISSING)
│   ├── enterprise_ai/          # 20 cos × 13Q (MISSING)
│   ├── cloud_infra/            # 7 cos × 13Q (PARTIAL)
│   ├── ai_infrastructure/      # 15 cos × 13Q (MISSING)
│   └── ipo_prospectuses/       # S-1 parsed financials (MISSING)
├── adoption/
│   ├── cloud_pricing/          # AWS/Azure/GCP pricing history (MISSING)
│   ├── vendor_telemetry/       # API calls, token volumes (MISSING - NDA)
│   ├── survey_data/            # Gartner/IDC/Morgan Stanley CIO (MISSING)
│   └── diffusion_curves/       # Bass params by segment (MISSING)
├── productivity/
│   ├── meta_analysis/          # 50 studies → effect sizes (MISSING)
│   ├── case_studies/           # Vendor TCO/ROI (MISSING)
│   └── labor_exposure/         # O*NET × AI (MISSING)
├── china/
│   ├── model_benchmarks/       # LMSYS/OpenCompass/C-Eval (MISSING)
│   ├── api_pricing/            # Zhipu/Baichuan/01.ai/Moonshot (MISSING)
│   ├── dc_costs/               # City-level land/power/labor (MISSING)
│   └── ppp_breakdown/          # World Bank ICP by category (MISSING)
├── regulatory/
│   ├── jurisdiction_rules/     # Matrix: jurisdiction × rule (MISSING)
│   ├── compliance_costs/       # Estimates by rule × company size (MISSING)
│   └── enforcement_actions/    # Fines, orders, guidance dates (MISSING)
├── macro/
│   ├── fred/                   # GDP, CPI, rates, FX, PMI (MISSING)
│   ├── commodities/            # Oil, gas, metals (MISSING)
│   └── capital_flows/          # TIC, BOP, IIP (MISSING)
├── stress_scenarios/
│   ├── historical_crises/      # Recession, energy, semi, cyber (MISSING)
│   ├── expert_elicitation/     # Delphi probabilities (MISSING)
│   └── narrative_scenarios/    # 20+ discrete shocks (MISSING)
├── contracts/
│   ├── rpo_maturity/           # Full RPO schedule from 10-K notes (MISSING)
│   ├── gpu_reservations/       # Cloud RI pricing + terms (MISSING)
│   └── renewal_distributions/  # Parametric fits (MISSING)
├── unit_economics/
│   ├── training_costs/         # Per-model (MISSING)
│   ├── inference_costs/        # Per-API-call (MISSING)
│   ├── gpu_economics/          # Per-GPU hourly (MISSING)
│   └── saas_benchmarks/        # CAC/LTV/churn (MISSING)
├── infrastructure/
│   ├── transmission/           # FERC 715; ISO planning (MISSING)
│   ├── transformer_supply/     # OEM order books (MISSING)
│   ├── nuclear/                # SMR timelines (MISSING)
│   ├── water/                  # USGS; Aqueduct (MISSING)
│   └── labor/                  # BLS OES; union data (MISSING)
└── revenue_quality/
    ├── contract_mapping/       # RI/SP/OD/Spot → tier (MISSING)
    └── churn_expansion/        # Net revenue retention by cohort (MISSING)
```

---

## Conclusion

**The DATA/ folder contains only 3 of ~30 required data categories.** It provides excellent empirical anchors for:
1. Hyperscaler financials (SEC DERA)
2. Grid interconnection constraints (LBNL)
3. Semiconductor import values (USITC)

**It completely lacks data for:**
- Company-level universe beyond 6 hyperscalers
- AI adoption/usage telemetry
- Productivity academic evidence
- Chinese AI competition benchmarks
- Revenue quality contract mapping
- Regulatory scenario parameters
- Macro feedback variables
- Black swan calibration
- Labor market transformation
- Unit economics
- Physical unit supply chain (beyond $ values)

**To reach publication/production grade:** Systematic data acquisition across 11 missing categories, estimated $1.3-2.0M and 12-18 months.