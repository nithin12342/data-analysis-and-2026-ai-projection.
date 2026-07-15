# Comprehensive Data Sources & Lineage Registry

**Project:** Comprehensive Financial Modeling: Dot-com Bubble vs. Today's AI Economy  
**Generated:** 2026-07-15  
**Repository:** `C:\Users\NITHING\Desktop\projections\`

---

## Table of Contents

1. [Core Financial & Market Data Sources](#1-core-financial--market-data-sources)
2. [Data Center Infrastructure Data](#2-data-center-infrastructure-data)
3. [Grid & Power Infrastructure Data](#3-grid--power-infrastructure-data)
4. [Semiconductor Supply Chain Data](#4-semiconductor-supply-chain-data)
5. [AI Adoption & Productivity Research](#5-ai-adoption--productivity-research)
6. [Chinese AI Ecosystem Data](#6-chinese-ai-ecosystem-data)
7. [Macroeconomic & Financial Market Data](#7-macroeconomic--financial-market-data)
8. [Regulatory & Policy Data](#8-regulatory--policy-data)
9. [Black Swan & Stress Scenario Parameters](#9-black-swan--stress-scenario-parameters)
10. [Onsite Power Generation Data](#10-onsite-power-generation-data)
11. [Model Calibration & Validation Data](#11-model-calibration--validation-data)
12. [Derived/Computed Datasets](#12-derivedcomputed-datasets)
13. [Source Code Files](#13-source-code-files)

---

## 1. Core Financial & Market Data Sources

### 1.1 SEC EDGAR / DERA Financial Statements
| **Module** | **Priority** | **Description** | **Access Method** |
|------------|--------------|-----------------|-------------------|
| §1, §2, §3, §13, §15, §25, §33 | P0 | 100+ tickers × 20+ quarters (1995-2002 dot-com + 2020-present AI) | SEC DERA bulk download + API |

**Key Data Tags Extracted:**
- `RevenueFromContractWithCustomerExcludingAssessedTax` — Total revenue
- `ResearchAndDevelopmentExpense` — R&D intensity
- `PaymentsToAcquirePropertyPlantAndEquipment` — CapEx
- `ContractWithCustomerLiabilityCurrent/Noncurrent` — RPO/Deferred Revenue
- `RevenueRemainingPerformanceObligation` — Backlog
- `ShareBasedCompensation` — SBC (critical for AI companies)
- `SegmentRevenue` + `SegmentProfit` — Where disclosed

**URL:** https://www.sec.gov/files/dera/data/financial-statement-data-sets/  
**Bulk Download Pattern:** `https://www.sec.gov/files/dera/data/financial-statement-data-sets/{YYYY}q{Q}/`

**Coverage:** 6 hyperscalers × 13 quarters (2023q1–2026q1) currently processed; expansion to 100+ tickers planned

---

### 1.2 Equity Market Data (CRSP / Refinitiv / Bloomberg)
| **Module** | **Priority** | **Data Elements** | **History** |
|------------|--------------|-------------------|-------------|
| §1, §3, §13, §15, §24, §33.1 | P0 | Daily OHLCV, splits, dividends, shares outstanding, institutional holdings (13F), analyst estimates (IBES), short interest, options flow, ETF flows | 1995-present |

**Sources:**
- CRSP / Refinitiv (subscription required)
- WhaleWisdom / SEC 13F filings (free)
- FINRA / S3 Partners (short interest)
- CBOE / SpotGamma (options)
- ETF.com / Bloomberg (ETF flows)

---

### 1.3 Private Market Data (AI Pure-Plays)
| **Module** | **Priority** | **Companies** | **Sources** |
|------------|--------------|---------------|-------------|
| §2, §3, §15 | P1 | OpenAI, Anthropic, Mistral, Cohere, xAI, Scale AI, Databricks, Hugging Face, CoreWeave, Lambda Labs, RunPod, Together AI, Perplexity, Character.ai, Adept, Inflection | PitchBook, Forge, Caplight, Prime Unicorn Index, The Information, Bloomberg, Reuters, Crunchbase Pro, LinkedIn Insights, Revelio Labs |

**Data Elements:** Valuation history, revenue estimates, cap tables, secondary market prices, employee counts, hiring velocity

---

### 1.4 IPO Prospectus Database (S-1 / F-1 Filings)
| **Module** | **Priority** | **Scope** | **Parsing Method** |
|------------|--------------|-----------|-------------------|
| §3, §33.2 | P1 | All AI/ML/cloud IPOs 2019-present + Dot-com IPOs 1995-2000 | `sec-edgar-downloader` + `BeautifulSoup` + `pdfplumber` |

**Extraction Targets:** Pre-IPO financials (3-5 yrs), use of proceeds, lockup terms, underwriter syndicate, risk factors (NLP), customer concentration, unit economics (CAC, LTV, churn)

---

## 2. Data Center Infrastructure Data

### 2.1 Master Global Data Centers Dataset (Compiled)
| **File** | **Records** | **Description** | **Sources Combined** |
|----------|-------------|-----------------|---------------------|
| `data_centers/master_global_datacenters.csv` | 19,694 facilities | Global facility-level data | 4 sources (see below) |
| `data_centers/README_MASTER_DATASET.md` | — | Documentation & summary | — |

**Component Sources:**

| Source | Records | Coverage | License | URL |
|--------|---------|----------|---------|-----|
| **GitHub Global-Data-Center-Map** | 18,089 | 116 countries, 4,181 operators (ATLAS dataset) | OpenStreetMap ODbL | https://github.com/.../Global-Data-Center-Map |
| **FracTracker US Tracker** | 1,579 | US facilities with pipeline status | Creative Commons | https://www.fractracker.org/... |
| **DCMap.us Pipeline** | 11 | Major US hyperscale pipeline (250,993 MW total) | Public tracker | https://dcmap.us/ |
| **DataCenterMap.info** | 15 | Country-level aggregates (11,873 facilities, 179 countries) | CC-BY-4.0 | https://datacentermap.info/ |

**Key Fields:** `source`, `facility_name`, `operator`, `city`, `state_province`, `country`, `address`, `status` (Operating/Planned/Under Construction/Cancelled/Suspended/Expanding/Reference), `capacity_mw`, `capacity_category`, `facility_size_sqft`, `property_size_acres`, `project_cost_usd`, `expected_online_date`, `latitude`, `longitude`, `cooling_type`, `power_source`, `tenant`, `purpose`, `community_pushback`, `notes`, `source_url`, `date_added`, `last_updated`

---

### 2.2 Enriched Hyperscale Facility Dataset (Phase 1-4)
| **File** | **Records** | **Description** |
|----------|-------------|-----------------|
| `data_centers/master_facility_list_v3_enriched.json` | 52 | Curated hyperscale facilities with compute estimates |
| `data_centers/master_facility_list_v3_enriched.csv` | 52 | CSV version with 60+ computed fields |
| `data_centers/FACILITY_FINANCIALS.csv` | 41 | Financial model outputs per facility |

**Data Pipeline (Phase 1-4):**
1. `phase1_master_list.py` → `master_facility_list.csv` (seed list from DCMap.us, news, filings)
2. `phase1_enhance.py` → `master_facility_list_v2.json` (add utility, PPA, GPU gen, cluster size)
3. `phase2_harvest.py` / `phase2_enrich.py` → `master_facility_list_v3_enriched.json` (deep enrichment)
4. `phase4_deliverables.py` → **Computed fields:** GPU estimates (H100/B200/MI300/GB200), training/inference PFLOPS, token throughput, training runs/year, power economics (annual MWh, cost, revenue potential), CapEx estimates ($/kW, $/GPU)

**Primary Sources for Enrichment:**
- Company earnings calls (Meta Q4'24, Microsoft, Alphabet, Amazon, Oracle)
- Utility IRPs (Entergy, Georgia Power, PacifiCorp, PG&E, Oncor/ERCOT)
- PSC/LPSC dockets (Louisiana, Georgia, Arizona, California)
- Vendor case studies (Vertiv, Bloom Energy, NVIDIA reference architectures)
- Building permits, county GIS, FERC filings, SEC 10-K/10-Q
- News: Data Center Dynamics, CRN, SemiAnalysis, The Information

**Output Files:**
- `FACILITY_CAPABILITY_CARDS.md` — 52 detailed 1-page facility cards
- `MASTER_CAPABILITY_MATRIX.csv` — 40+ column capability matrix
- `HYPERSCALER_AGGREGATE_REPORT.md` — Operator-level rollups
- `DATA_LINEAGE_LOG.csv` — Source attribution per field (A/B/C confidence)
- `GAP_UNCERTAINTY_REGISTER.csv` — Missing data tracking with suggested sources

---

## 3. Grid & Power Infrastructure Data

### 3.1 LBNL Interconnection Queue Database
| **File** | **Source** | **Coverage** | **Key Metrics** |
|----------|------------|--------------|-----------------|
| `DATA/LBNL_Ix_Queue_Data_File_thru2025.xlsx` | Lawrence Berkeley National Laboratory | All US ISO/RTO queues (CAISO, PJM, ERCOT, MISO, NYISO, ISO-NE, SPP) | Project-level: MW capacity, queue date, IA date, commercial online date, withdrawal date, status, technology type, location |

**Processed Metrics (calibrate.py):**
- Mean queue duration: **20 quarters** (median ~18)
- Withdrawal rate: **~75%** for data center/storage/battery projects
- Active pipeline capacity: **sum of MW_1** for non-withdrawn projects

**URL:** https://emp.lbl.gov/utility-scale-solar/ (LBNL queue data portal)  
**Direct Download:** https://emp.lbl.gov/sites/default/files/queuedata_2025.xlsx

---

### 3.2 ISO/RTO Queue Data (Direct)
| ISO/RTO | Data Portal | Key Tables |
|---------|-------------|------------|
| **PJM** | https://www.pjm.com/planning/services-requests/interconnection-queues.aspx | Queue Dashboard, Project Status |
| **ERCOT** | https://www.ercot.com/gridinfo/resource | GINR, Project Tracking |
| **CAISO** | http://www.caiso.com/planning/Pages/GeneratorInterconnection/Default.aspx | Queue Cluster Results |
| **MISO** | https://www.misoenergy.org/planning/generator-interconnection/ | DPP Results, Queue |
| **NYISO** | https://www.nyiso.com/interconnection-process | Queue Status |
| **ISO-NE** | https://www.iso-ne.com/ws/document | IR Queue |
| **SPP** | https://spp.org/engineering/generator-interconnection/ | GI Queue |

---

### 3.3 FERC Form 715 (Transmission Planning)
| **Source** | **Coverage** | **Access** |
|------------|--------------|------------|
| FERC eLibrary | All US transmission owners | https://elibrary.ferc.gov/ |

**Key Variables:** Line ratings, loading, planned upgrades, thermal limits

---

### 3.4 EIA Forms (Generation & Capacity)
| Form | Coverage | Key Variables | URL |
|------|----------|---------------|-----|
| **EIA-860** | All US generators | Capacity, fuel, emissions, retirement plans, technology | https://www.eia.gov/electricity/data/eia860/ |
| **EIA-923** | All US generators | Generation, fuel consumption, heat rates, costs | https://www.eia.gov/electricity/data/eia923/ |

---

### 3.5 NREL Models
| Model | Description | URL |
|-------|-------------|-----|
| **ReEDS** | Least-cost capacity expansion model | https://www.nrel.gov/analysis/reeds/ |
| **GridPath** | Open-source power system model | https://www.gridpath.io/ |

---

## 4. Semiconductor Supply Chain Data

### 4.1 Public Filings & Earnings
| Company | Data Elements | Frequency |
|---------|---------------|-----------|
| **TSMC** | Wafer starts by node, CoWoS capacity, revenue by platform | Quarterly |
| **Samsung Foundry** | Wafer capacity, advanced node yields | Quarterly |
| **Intel Foundry** | 18A/14A capacity, external customer ramps | Quarterly |
| **NVIDIA** | Data Center revenue, GPU shipments by architecture (H100/B200/GB200) | Quarterly |
| **AMD** | MI300/MI325/MI350 shipments, Data Center GPU revenue | Quarterly |
| **SK Hynix / Samsung / Micron** | HBM production, allocation, DRAM/NAND bit growth | Quarterly |

**Sources:** Earnings transcripts (Seeking Alpha, FactSet), 10-Q/10-K, investor presentations

---

### 4.2 Subscription Research (Required for Production)
| Provider | Data Product | Est. Cost | Key Data |
|----------|--------------|-----------|----------|
| **Omdia** | Semiconductor Manufacturing Tracker | $20K+/yr | Wafer starts by node, fab utilization, equipment spend |
| **TrendForce / DRAMeXchange** | HBM/DRAM/NAND pricing & supply | $15K+/yr | HBM production by vendor, spot/contract pricing |
| **Jon Peddie Research** | GPU shipments by SKU | $10K+/yr | Discrete GPU shipments, attach rates |
| **SemiAnalysis** | Semi supply chain deep dives | Subscription | CoWoS capacity, lead times, packaging bottlenecks |
| **DC Byte / Structure Research / Synergy Research** | Data center build tracker | $30K+/yr | Facility-level construction, MW by region, operator |

---

### 4.3 USITC Trade Data (Semiconductor Imports)
| **File** | **Source** | **HTS Codes** | **Frequency** |
|----------|------------|---------------|---------------|
| `DataWeb-Query-Export.xlsx` | USITC DataWeb | 8542 (Integrated circuits), 8473.30 (Parts for ADP machines) | Monthly |

**URL:** https://dataweb.usitc.gov/  
**Processed:** Quarterly aggregation of semiconductor import value/volume by country

---

## 5. AI Adoption & Productivity Research

### 5.1 Academic Meta-Analysis Corpus (50+ Studies)
| **Category** | **Key Papers** | **Effect Sizes** |
|--------------|----------------|------------------|
| **Coding Assistants** | Peng et al. 2023 (Copilot, 55% faster), Tabachnyk & Nikolov 2022, Moradi et al. 2023 | % task time reduction, acceptance rate |
| **Writing/Content** | Noy & Zhang 2023 (Science), Dell'Acqua et al. 2023 (BCG) | Words/hour, quality scores |
| **Customer Support** | Brynjolfsson et al. 2023 (NBER), Cui et al. 2024 (QJE) | Tickets/hour, resolution rate, CSAT |
| **Professional Services** | Kanazawa et al. 2023 (legal), Agrawal et al. 2023 (consulting) | Billable hours, output quality |
| **R&D / Science** | Wang et al. 2023 (materials), Liu et al. 2024 (drug discovery) | Experiment throughput, hit rate |
| **General Knowledge Work** | Eloundou et al. 2023 (OpenAI), Felten et al. 2021/2023 | Occupation-level exposure scores |

**Search Databases:** PubMed, SSRN, ArXiv, EconLit, Google Scholar  
**Protocol:** PRISMA systematic review  
**Meta-Analysis:** Random-effects (DerSimonian-Laird), meta-regression by industry/task/model quality, publication bias tests (Egger's, trim-and-fill)

**Output:** JSON with study-level effects + pooled posterior (mean, SD, 95% CI) by category → used as Bayesian priors

---

### 5.2 Labor Market Data
| **Dataset** | **Source** | **Variables** | **Frequency** |
|-------------|------------|---------------|---------------|
| **O*NET 28.0** | O*NET Center | 1,000+ occupations × 200+ descriptors (tasks, skills, knowledge) | Annual |
| **AI Exposure Scores** | Felten/Raj/Seamans replication | Occupation-level exposure to LM, image gen, etc. | Static (update with new models) |
| **CPS Displaced Worker Supplement** | BLS | Displacement rates, reemployment, wage changes | Biennial |
| **JOLTS** | BLS | Job openings, hires, quits by industry | Monthly |
| **QCEW** | BLS | Employment, wages by county/industry | Quarterly |
| **ACS / CPS Microdata** | Census / IPUMS | Individual-level demographics, occupation, wages | Annual/Monthly |
| **Lightcast / Burning Glass** | Private | Real-time job postings, skill requirements | Monthly |

**Integration:** Map O*NET tasks → AI automation probability → occupation displacement risk → industry employment forecast

---

### 5.3 Third-Party Adoption Estimates
| **Provider** | **Coverage** | **Access** | **Cost** |
|--------------|--------------|------------|----------|
| **Gartner** | Enterprise AI adoption curves, Magic Quadrants, Hype Cycles | Subscription | $50K+/yr |
| **IDC** | Worldwide AI Spending Guide, MarketScape, Tracker data | Subscription | $40K+/yr |
| **Morgan Stanley CIO Survey** | Quarterly IT budget intent, AI prioritization | Free (published) | Free |
| **Piper Sandler / KeyBanc / JMP** | Software surveys, seat count estimates | Research access | Varies |
| **Flexera State of Cloud** | Multi-cloud adoption, reserved vs on-demand mix | Free annual report | Free |
| **Omdia / Synergy Research** | Cloud market share, DC capacity | Subscription | Varies |

---

### 5.4 Vendor-Reported Usage Metrics
| **Vendor** | **Metrics Tracked** | **Extraction Method** |
|------------|---------------------|----------------------|
| **OpenAI** | ChatGPT MAU/DAU, Plus/Pro/Team/Enterprise seats, API token volume, GPT-4/4o/o1 usage split | MSFT earnings calls, investor presentations, API pricing page changes |
| **Anthropic** | Claude users, API token volume, Enterprise seats, Opus/Sonnet/Haiku mix | Investor decks, blog posts, API headers |
| **Google** | Gemini users, Vertex AI API calls, TPU utilization, Cloud AI revenue | Alphabet earnings calls, Cloud revenue breakdown |
| **Microsoft** | Copilot seats (M365, GitHub, Security, Azure), Azure OpenAI consumption | Earnings calls, partner announcements |
| **AWS** | Bedrock model invocations, Trainium/Inferentia adoption, SageMaker jobs | re:Invent keynotes, earnings calls |
| **Meta** | Llama downloads (HF), internal GPU fleet, AI ad revenue | Llama release blogs, earnings calls |

**Schema:** `{vendor, date, metric, value, source, confidence}`

---

### 5.5 Alternative Data (Usage Proxies)
| **Data Type** | **Provider** | **Use Case** |
|---------------|--------------|--------------|
| Web traffic / app usage | SimilarWeb, Sensor Tower, Data.ai | Consumer adoption trends |
| GitHub stars / clones / forks | GitHub Archive, GH Archive | Open-source model adoption |
| Hugging Face downloads / likes | HF Hub API | Model popularity, fine-tuning activity |
| ArXiv submission rates | ArXiv API | Research velocity by topic |
| Job postings (AI roles) | Lightcast, Revelio Labs, LinkedIn | Enterprise hiring intent |
| Credit card transactions | Second Measure, Earnest | Consumer subscription retention |
| App Store / Play Store rankings | Sensor Tower, AppMagic | Mobile AI app adoption |

---

## 6. Chinese AI Ecosystem Data

### 6.1 Model Benchmarks & Performance
| **Benchmark** | **Models Covered** | **Access** | **Frequency** |
|---------------|--------------------|------------|---------------|
| **LMSYS Chatbot Arena** | All major open/closed models | HF dataset / API | Weekly |
| **OpenCompass** (Shanghai AI Lab) | Chinese + global models | GitHub / website | Monthly |
| **C-Eval** | Chinese language understanding | GitHub | Per release |
| **CMMLU** | Chinese MMLU | GitHub | Per release |
| **SuperCLUE** | Chinese LLM evaluation | Website / API | Monthly |
| **FlagEval** (BAAI) | Multimodal, code, reasoning | GitHub | Quarterly |
| **Hugging Face Open LLM Leaderboard** | Open-weight models | HF Hub / API | Continuous |

**Schema:** `{model, organization, benchmark, elo, ci, date, category, language}`

---

### 6.2 Chinese API Pricing & Market Data
| **Provider** | **Models** | **Pricing Source** | **Update** |
|--------------|------------|-------------------|------------|
| **Zhipu AI** | GLM-4, GLM-4V, GLM-4-Air | pricing.zhipu.ai | Monthly scrape |
| **Baichuan** | Baichuan2, Baichuan3, Baichuan4 | api.baichuan-ai.com | Monthly |
| **01.ai** | Yi series | platform.01.ai | Monthly |
| **Moonshot** | Kimi (Moonshot-v1) | platform.moonshot.cn | Monthly |
| **MiniMax** | abab 6.5, abab 7 | api.minimax.chat | Monthly |
| **Alibaba** | Qwen series | dashscope.aliyuncs.com | Monthly |
| **Tencent** | Hunyuan | cloud.tencent.com | Monthly |
| **ByteDance** | Doubao | volcengine.com | Monthly |

**PPP Adjustment:** CNY → USD at market rate **AND** PPP rate (World Bank ICP 2021: 1 USD = 3.8 CNY PPP vs 7.2 market)

---

### 6.3 Chinese Infrastructure Costs
| **Cost Category** | **Source** | **Granularity** |
|-------------------|------------|-----------------|
| Data Center Land | JLL China, CBRE China, Colliers | City-level (Tier 1/2/3), $/mu |
| Construction Cost | Turner & Townsend China, Linesight, RLB | $/MW, by tier level |
| Electricity (Industrial) | NEAC, provincial grids, China Electricity Council | Province-level, ¥/kWh |
| Water / Cooling | Local water bureaus, environmental reports | City-level |
| Engineering Salaries | Levels.fyi China, 51job, Zhaopin, Liepin | Role × experience × city |
| GPU Pricing (Domestic) | Huawei Ascend, Cambricon, Biren, Moore Threads | Vendor quotes, distributor channels |
| PPP Factors | World Bank ICP 2021, Penn World Tables 10.0 | Expenditure category breakdown |

---

## 7. Macroeconomic & Financial Market Data

### 7.1 Core Macro Time Series (FRED / OECD / BIS / IMF)
| **Series** | **FRED Code** | **Frequency** | **History** | **Use Case** |
|------------|---------------|---------------|-------------|--------------|
| US Real GDP | GDPC1 | Quarterly | 1947+ | Output gap, potential growth |
| US CPI / Core PCE | CPIAUCSL / PCEPILFE | Monthly | 1959+ | Inflation expectations |
| Fed Funds Rate | FEDFUNDS / DFEDTARU | Daily | 1954+ | Monetary policy stance |
| 10Y Treasury | GS10 / DGS10 | Daily | 1962+ | Discount rate, term premium |
| 2Y-10Y Spread | T10Y2Y | Daily | 1976+ | Recession predictor |
| IG/HY Spreads | BAMLC0A0CMEY / BAMLH0A0HYM2 | Daily | 1996+ | Credit conditions |
| DXY / Major FX | DTWEXBGS / EXCHUS | Daily | 1973+ | Currency effects |
| WTI / Brent / Henry Hub | DCOILWTICO / DCOILBRENTEU / DHHNGSP | Daily | 1986+ | Energy costs for DCs |
| Copper / Lithium / Cobalt | PCOPPUSDM / PLITUSDM / PCOBUSDM | Monthly | 2000+ | Hardware BOM costs |
| Global PMI | S&P Global | Monthly | 1998+ | Leading indicator |
| Capital Flows (TIC) | Treasury | Monthly | 1970+ | Foreign demand for US assets |
| Geopolitical Risk (GPR) | Caldara/Iacoviello | Monthly | 1985+ | Tail risk scenarios |

**Access:** FRED API (free, 800k+ series) + OECD SDMX + BIS Statistics + IMF IFS

---

### 7.2 Financial Market Microstructure
| **Data** | **Source** | **Frequency** |
|----------|------------|---------------|
| Factor Returns (MKT, SMB, HML, RMW, CMA, UMD) | Ken French Library | Daily/Monthly |
| Sector ETF Flows | ETF.com, Bloomberg | Daily |
| Institutional 13F Holdings | WhaleWisdom, SEC | Quarterly |
| Short Interest / Borrow Rates | FINRA, S3 Partners, IHS Markit | Bi-weekly |
| Options Greeks / Gamma Exposure | CBOE, SpotGamma, Dealer's Eye | Daily |
| Analyst Revisions | IBES (Refinitiv), FactSet | Daily |
| Credit Default Swaps | Markit, Bloomberg | Daily |

---

## 8. Regulatory & Policy Data

### 8.1 Jurisdiction × Rule Matrix
| **Jurisdiction** | **Regulation** | **Status** | **Key Requirements** | **Compliance Cost Source** |
|------------------|----------------|------------|----------------------|----------------------------|
| US Federal | EO 14110 (AI Safety) | Active | Red-teaming, watermarking, CFIUS | NIST AI RMF assessments |
| US Federal | NIST AI RMF 1.0 | Voluntary | Governance, mapping, measurement | Big 4 consulting quotes |
| US Federal | SEC AI Disclosure Guidance | Active | 10-K risk factors, materiality | Law firm memos |
| US Federal | Copyright (NYT v OpenAI) | Litigation | Training data licensing | Settlement tracking |
| US State (CA) | SB 1047 (vetoed) / new bills | Legislative | Model registration, safety tests | Legislative analysis |
| EU | AI Act (Reg 2024/1689) | Phased 2025-2027 | Tiered risk, conformity assessment | EU Commission impact assessment |
| EU | GDPR Art. 22 | Active | Automated decision rights | DPA guidance, fines |
| EU | DSA / DMA | Active | VLOP obligations, interoperability | EC enforcement decisions |
| China | Interim Measures for GenAI | Active (Aug 2023) | Filing, security assessment, content control | CAC filings, law firm analyses |
| China | Data Security Law / PIPL | Active | Cross-border transfer, classification | Cyberspace Administration |
| UK | AI Regulation White Paper | Principles-based | Sectoral regulators, sandboxes | DSIT consultations |
| India | DPDP Act 2023 | Rules pending | Data localization, consent | MeitY draft rules |
| UAE | AI Strategy 2031 / DIFC AI Law | Active | Licensing, data sovereignty | DIFC Authority |
| KSA | NCA AI Ethics / SDAIA | Active | Registration, classification | SDAIA guidelines |

**Schema:** `{jurisdiction, regulation, tier, requirements[], compliance_cost{low,median,high}, cost_unit, source, effective_date, enforcement_probability}`

**Update Mechanism:** Regulatory tracking feeds (LexisNexis, Thomson Reuters, GlobalRegulation.com) + government gazette monitoring

---

### 8.2 Export Controls & Entity Lists
| **List** | **Authority** | **Frequency** | **Key Fields** |
|----------|---------------|---------------|----------------|
| Entity List | BIS (US) | Weekly | Entity name, address, license requirement, ECCN |
| Military End User (MEU) | BIS | Monthly | Entity, country, license policy |
| Unverified List | BIS | Quarterly | Entity, country, last verification |
| SDN / Non-SDN | OFAC | Daily | Entity, program, sanctions type |
| China Export Control List | MOFCOM | Irregular | Dual-use items, restricted entities |
| Wassenaar Arrangement | Secretariat | Annual | Dual-use controls, munitions list |

**Integration:** Map ECCN codes to AI hardware (3A090, 4A090, 5A002, 5D002) → model supply chain disruption probability

---

## 9. Black Swan & Stress Scenario Library

**File:** `data_centers/module_31_black_swan_stress_test.csv` (53 rows)

| **Shock Category** | **Parameterization** | **Annual Probability** | **Correlation** |
|--------------------|----------------------|------------------------|-----------------|
| Global Recession | GDP -3 to -5%, unemployment +3-5pp, credit spreads 2-3x | 15% | Correlated across regions (copula) |
| Energy Crisis | Oil +100-200%, gas +300-500%, electricity +50-100% | 5% | Regional (EU/Asia/US different) |
| Semiconductor Supply Disruption | Foundry output -30-50%, lead time 2-4x, spot price +200% | 3% | TSMC/Taiwan concentration |
| Taiwan Strait Conflict | TSMC offline, shipping lanes closed, sanctions cascade | 1-2% | Extreme tail, correlated with semi + geopolitical |
| Major Cyber Incident | Cloud outage 1-4 weeks, data breach costs $1-10B | 2% | Cloud provider concentration |
| AI Safety Event | Model capability surprise, regulatory crackdown, usage restrictions | 1% | Novel, expert elicitation only |
| Financial Crisis | Equity -30-50%, credit freeze, bank failures, liquidity crunch | 3% | Correlated with recession |
| Regulatory Shock | EU AI Act enforcement + fines, US EO expansion, China crackdown | 5% | Jurisdiction-specific |
| Algorithmic Breakthrough | Compute efficiency 5-10x, new paradigm | 2% | Innovation process model |
| Hardware Breakthrough | New memory (MRAM), interconnect (optical), packaging (3D) | 3% | IRDS/ITRS roadmap |
| Quantum Crypto Break | RSA/ECC broken, PQC transition cost $100B+ | 0.5% | NIST PQC timeline |
| Fusion Commercialization | Net energy gain, pilot plant, electricity <$20/MWh | 0.5% | ITER/DOE milestones |
| Sustained Deflationary AI Cost Reductions | 50%+ annual cost declines persist | 30% | Expert elicitation |

**Expert Elicitation Protocol (Delphi Method):**
1. Recruit 15-20 domain experts per shock category
2. Round 1: Independent probability + magnitude estimates
3. Round 2: Share anonymized distribution → revise
4. Round 3: Final calibrated distributions
5. Fit parametric distributions (Generalized Pareto for tails)
6. Estimate correlation matrix via expert judgment + historical co-occurrence

**Key Sources Cited in File:**
- IMF 2026, OECD 2026 (recession)
- IEA 2026 (energy)
- SIA 2025, CSIS 2025 (semiconductors)
- WEF Global Risks 2026 (cyber)
- Anthropic 2026, CAIS 2026 (AI safety)
- BIS 2026, Reinhart/Rogoff (financial crisis)
- CFR 2026, IISS 2026 (geopolitical)
- Epoch AI 2025, METR 2025 (algorithmic breakthrough)
- McKinsey Quantum 2025, DARPA 2025 (quantum)
- DOE 2025, ITER 2025, CFS/Helion 2025 (fusion)
- ArXiv 2606.01575, Zhang & Zhang 2026 (deflationary AI)

---

## 10. Onsite Power Generation Data (§34)

### 10.1 Technology Taxonomy & Deployment Status
| **Technology** | **Typical Capacity** | **CapEx ($/kW)** | **O&M ($/MWh)** | **Heat Rate (Btu/kWh)** | **Fuel Types** | **Stage** | **Key Vendors** |
|----------------|---------------------|------------------|-----------------|-------------------------|----------------|-----------|-----------------|
| Aeroderivative Gas Turbine | 25-100 MW | 1,200-1,800 | 8-15 | 9,000-11,000 | Gas, H2-blend | Commercial | GE Vernova, Siemens, Mitsubishi |
| Reciprocating Engine (RICE) | 2-20 MW | 1,000-1,500 | 10-20 | 8,000-9,500 | Gas, Diesel, H2 | Commercial | Wärtsilä, MAN, Caterpillar, Rolls-Royce |
| Solid Oxide Fuel Cell (SOFC) | 0.2-4 MW | 4,000-7,000 | 5-10 | 6,500-8,000 | Gas, Biogas, H2 | Early Commercial | Bloom Energy, FuelCell Energy, Ceres |
| PEM Fuel Cell | 0.1-2 MW | 3,000-5,000 | 3-8 | 5,500-7,000 | H2 | Pilot/Demo | Plug Power, Ballard, Toyota |
| Small Modular Reactor (SMR) | 50-300 MW | 5,000-8,000 | 15-25 | N/A | Uranium | Licensing/FOAK | NuScale, TerraPower, X-energy, GE Hitachi |
| Solar PV + Battery | 10-500 MW | 1,000-1,800 | 5-15 | N/A | Sunlight | Commercial | NextEra, Fluence, Tesla |
| Hydrogen Turbine | 50-100 MW | 1,500-2,500 | 10-20 | 9,500-12,000 | H2 (green/blue) | Demo | GE, Siemens, Mitsubishi |

---

### 10.2 Empirical Deployment Data (param_overrides.json → powerMetrics.capacity)
**508 records** of hyperscaler onsite generation deployments (2021-2026)

| **Company** | **Technology** | **Capacity (MW)** | **COD Years** | **Source** |
|-------------|----------------|-------------------|---------------|------------|
| **Microsoft** | Bloom SOFC | 20×3 (2024-2026) | 2024, 2025, 2026 | Bloom Energy / AWS PPA |
| **Microsoft** | Hydrogen FC | 3 (2022), 1.5 (2021) | 2021, 2022 | Plug Power 2022, Ballard/Caterpillar 2021 |
| **Microsoft** | Gas Turbine | 198 (3×66MW) | 2008 | Chicago 3×66MW |
| **Google** | Bloom SOFC | 50×3 (2024-2026) | 2024, 2025, 2026 | Bloom Energy / Intel PPA |
| **Google** | Gas Turbine | 300 | 2025 | Grid connection queue |
| **AWS** | Bloom SOFC | 24.3×3 (Oregon), 20×3 (Silicon Valley) | 2024, 2025, 2026 | Bloom Energy Oregon/CA PPAs |
| **Oracle** | Bloom SOFC | 1,200 (2024), 1,600×2 (2025-2026) | 2024, 2025, 2026 | Bloom Energy Oracle 1.2GW/1.6GW |
| **Intel** | Bloom SOFC | 50 (2014), 100 (2024) | 2014, 2024 | Bloom Energy Intel 2014/2024 |
| **CoreWeave** | Bloom SOFC | 100 | 2026 | Bloom Energy CoreWeave 2026 |
| **Equinix** | Bloom SOFC | 50 | 2024 | Bloom Energy Equinix 2024 |
| **Digital Realty** | Bloom SOFC | 30 | 2024 | Bloom Energy DLR 2024 |
| **CyrusOne** | Bloom SOFC | 25 | 2024 | Bloom Energy CONEX 2024 |

**Total Tracked:** ~5,600 MW across US hyperscalers (2024)

---

### 10.3 Heat Rate Degradation Curves (param_overrides.json → powerMetrics.heat_rates)
| **Unit** | **Technology** | **Fuel** | **Heat Rate (Btu/kWh)** | **Degradation (%/yr)** | **Source** |
|----------|----------------|----------|-------------------------|------------------------|------------|
| Bloom ES-5 | SOFC | Natural Gas | 6,800 → 7,000 (2024-2028) | 0.5% | Bloom Energy whitepaper |
| GE 7HA | Gas Turbine | Natural Gas | 9,200 → 9,400 | 0.7% | GE specs |
| Siemens HL | Gas Turbine | Natural Gas | 9,000 → 9,100 | 0.6% | Siemens specs |
| Mitsubishi M501 | Gas Turbine | Natural Gas | 9,500 → 9,600 | 0.7% | Mitsubishi specs |
| Wärtsilä 18V50 | RICE | Natural Gas | 8,200 → 8,300 | 0.5% | Wärtsilä specs |
| Plug Power Gen | Solid Oxide | Hydrogen | 5,500 → 5,550 | 0.3% | Plug Power specs |
| Ballard FC | Hydrogen | Hydrogen | 5,500 | 0.3% | Ballard specs |

---

### 10.4 Fuel Price Time Series (param_overrides.json → powerMetrics.fuel_prices)
| **Hub** | **Period** | **Frequency** | **Source** |
|---------|------------|---------------|------------|
| **Henry Hub** | 2023-01 → 2026-12 | Monthly | EIA |
| **TTF (Europe)** | 2023-01 → 2026-12 | Monthly | ICE |
| **JKM (NE Asia)** | 2023-01 → 2026-12 | Monthly | ICE |

**Data Points:** 1,808 monthly observations across 3 hubs  
**Fields:** `hub`, `date`, `price_usd_mmbtu`, `basis_diff_usd_mmbtu`, `volatility_pct`, `source`

---

### 10.5 Hedge Ratios (param_overrides.json → powerMetrics.hedge_ratios)
| **Company** | **Commodity** | **Hedge Ratio** | **Tenor (yr)** | **Instruments** | **Date** | **Source** |
|-------------|---------------|-----------------|----------------|-----------------|----------|------------|
| Microsoft | Natural Gas | 0.65 → 0.75 | 2-3 | Swaps, Collars | 2024-2026 | Microsoft 10-K |
| Google | Natural Gas | 0.60 → 0.70 | 2-3 | Swaps, Collars | 2024-2026 | Alphabet 10-K |
| AWS | Natural Gas | 0.70 → 0.80 | 2-3 | Swaps, Collars, Physical | 2024-2026 | Amazon 10-K |
| Meta | Natural Gas | 0.55 → 0.65 | 2-3 | Swaps | 2024-2026 | Meta 10-K |
| Oracle | Natural Gas | 0.50 → 0.55 | 2-3 | Swaps | 2024-2025 | Oracle 10-K |
| Intel | Natural Gas | 0.60 → 0.65 | 2-3 | Swaps | 2024-2025 | Intel 10-K |

**Count:** 18 records across 6 companies

---

### 10.6 Grid Services Revenue (param_overrides.json → powerMetrics.grid_services)
| **ISO** | **Service** | **Price ($/MW-yr)** | **Volume (MW)** | **Date** | **Source** |
|---------|-------------|---------------------|-----------------|----------|------------|
| CAISO | Regulation Up | 45,000 | 1,200 | 2024-01 | CAISO Market Report |
| CAISO | Regulation Down | 38,000 | 1,100 | 2024-01 | CAISO Market Report |
| CAISO | Spinning Reserve | 25,000 | 800 | 2024-01 | CAISO Market Report |
| CAISO | Non-Spinning Reserve | 18,000 | 600 | 2024-01 | CAISO Market Report |

**Weighted Average:** ~$25,000-40,000/MW-yr depending on service mix

---

### 10.7 Grid Connection Delays (Regional)
| **Region** | **Mean Queue (quarters)** | **Withdrawal Rate** | **Source** |
|------------|---------------------------|---------------------|------------|
| **US (LBNL aggregate)** | 20 | 75% | LBNL Queue Data 2025 |
| **China** | 3 | ~10% | Centralized planning |
| **India** | 4 | ~20% | CEA / POSOCO |
| **Gulf (UAE/KSA)** | 2 | ~5% | Centralized planning |
| **EU** | 11 | ~40% | ENTSO-E / national TSOs |

---

### 10.8 Transformer Shortage Data
| **Metric** | **Value** | **Source** |
|------------|-----------|------------|
| **Lead time (large power transformers)** | 52-104 weeks | DOE 2024, EEI 2024 |
| **Global manufacturing capacity** | ~$20B/yr | Wood Mackenzie 2024 |
| **US import dependence** | >80% | DOE 2023 |
| **Price increase 2020-2024** | 60-100% | IEA 2024 |

---

### 10.9 Carbon Prices
| **Jurisdiction** | **Price ($/ton CO2)** | **Source** |
|------------------|----------------------|------------|
| EU ETS | ~€80-90 | Ember 2024 |
| UK ETS | ~£40-45 | UK ETS Registry |
| California Cap-and-Trade | ~$35-40 | CARB 2024 |
| RGGI (NE US) | ~$13-15 | RGGI Inc. 2024 |
| China National ETS | ~¥60-80 | MEE 2024 |

---

## 11. Model Calibration & Validation Data

### 11.1 Historical Crisis Trails (engine.js → REAL_HISTORICAL_TRAILS)
| **Episode** | **Period** | **Index Data Points** | **Auxiliary Data** |
|-------------|------------|----------------------|-------------------|
| **Dot-com Bubble** | 1995-2002 | 24 quarterly index values (100 → 520 → 78) | Historical CapEx series (24 quarters) |
| **Japan Asset Bubble** | 1985-1995 | 24 quarterly index values (100 → 27) | Historical policy rates (24 quarters) |
| **Railway Mania** | 1843-1850 | 29 quarterly index values (100 → 72) | — |

**Calibration Targets:**
- RMSE < 25.0 (index points)
- Directional Accuracy > 70%

**Optimization Parameters:** elasticityCoefficient, priceCompression, capitalReflexivity

---

### 11.2 SEC Hyperscaler Audit (13 Quarters)
**File:** `data_centers/HYPERSCALER_CAPEX_AUDIT_2020_2026.md`

| **Company** | **Quarters** | **Tags Verified** |
|-------------|--------------|-------------------|
| Microsoft | 2023q1–2026q1 | CapEx, RPO, Revenue, R&D, SBC |
| Amazon (AWS) | 2023q1–2026q1 | CapEx, RPO, Revenue, R&D, SBC |
| Alphabet (Google) | 2023q1–2026q1 | CapEx, RPO, Revenue, R&D, SBC |
| Meta | 2023q1–2026q1 | CapEx, RPO, Revenue, R&D, SBC |
| Oracle | 2023q1–2026q1 | CapEx, RPO, Revenue, R&D, SBC |
| Salesforce | 2023q1–2026q1 | CapEx, RPO, Revenue, R&D, SBC |

**Scripts:** `verify_hyperscaler_capex.py`, `generate_capex_audit.py`

---

### 11.3 Onsite Power Regulatory Audit
**File:** `data_centers/ONSITE_POWER_REGULATORY_AUDIT.md`

| **Permit Type** | **Timeline** | **Key Agency** | **Status** |
|-----------------|--------------|----------------|------------|
| Air Permitting (NSR/Title V) | 12-36 months | EPA / State DEQ | Varies by state |
| Interconnection Agreement | 6-24 months | FERC / ISO-RTO | Order 2023 reforms |
| Net Metering / Export Rules | Varies | State PUC | State-specific |
| Hydrogen Regulations (45V/IPC) | Evolving | IRS / DOE / EU | Guidance pending |
| Nuclear Licensing (SMR) | 5-10+ years | NRC (US) / ONR (UK) / NRA (JP) | Design certification phase |

**Scripts:** `verify_onsite_permits.py`, `generate_audit_markdown.py`

---

## 12. Derived/Computed Datasets

| **File** | **Description** | **Generated By** | **Key Columns** |
|----------|-----------------|------------------|-----------------|
| `data_centers/module_1_historical_comparison.csv` | Dot-com vs AI financial comparison | Phase 1-2 | Valuation, revenue, profitability, FCF, multiples, concentration, CapEx, sentiment, IPO quality, VC, debt, rates |
| `data_centers/module_3_ipo_quality.csv` | IPO quality scoring | Phase 2 | Revenue, profitability, cash burn, margins, retention, revenue quality, multiples, fundamentals |
| `data_centers/module_4_ai_adoption.csv` | AI adoption metrics | Phase 3 | Free/paid users, enterprise adoption, usage growth, revenue conversion, retention, token usage, inference/training demand |
| `data_centers/module_5_capex_model.csv` | CapEx projections | Phase 3 | AI chips, data centers, networking, power, cooling, cloud expansion |
| `data_centers/module_6_efficiency_model.csv` | AI efficiency improvements | Phase 3 | Inference cost reduction, architecture improvements, quantization, MoE, utilization |
| `data_centers/module_7_productivity_gains.csv` | Productivity gains from AI | Phase 3 | Labor savings, time savings, operational efficiency, output increase, cost reduction, ROI |
| `data_centers/module_8_chinese_competition.csv` | Chinese AI competitive pressure | Phase 3 | Model quality convergence, pricing pressure, open-source competition, inference cost reduction, market share shifts |
| `data_centers/module_9_ppp.csv` | PPP adjustments for China | Phase 3 | Labor costs, electricity, DC construction, hardware, OpEx, engineering salaries |
| `data_centers/module_10_demand_shocks.csv` | Demand scenario modeling | Phase 3 | Exponential/moderate/slowing/flat/declining scenarios |
| `data_centers/module_11_enterprise_agents.csv` | Enterprise AI agent deployments | Phase 3 | Google 1,302 agents, Salesforce 20,000 agents, productivity, cost savings, revenue, ROI |
| `data_centers/module_12_workflow_integration.csv` | Workflow integration metrics | Phase 3 | Automation rates, task completion, process optimization, human-AI collaboration, stickiness, switching costs |
| `data_centers/module_13_financial_modeling.csv` | DCF, scenarios, Monte Carlo | Phase 4 | DCF valuations, sensitivity, unit economics, cash flows, CapEx vs revenue, saturation |
| `data_centers/module_14_detailed_calculations.csv` | Transparent calculations | Phase 4 | Assumptions, inputs, equations, intermediate, outputs, sensitivity tables |
| `data_centers/module_15_final_assessment.csv` | Final conclusions | Phase 4 | Bubble assessment, severity, overvalued sectors, justified sectors, resilient models, vulnerable companies, crash probability, stagnation probability, 5-10yr outlook |
| `data_centers/module_16_global_infra_deployment.csv` | Regional infrastructure speed | Phase 4 | Construction timelines, grid expansion, power deployment, HV transmission, fab facilities, water, cooling, fiber, land, environmental, regulatory |
| `data_centers/module_17_contract_lag.csv` | Enterprise contract lag model | Phase 4 | 3yr/5yr contracts, reserved capacity, GPU reservations, licensing, pre-purchases, budgeting cycles |
| `data_centers/module_18_agentic_liability.csv` | Agentic AI liability costs | Phase 4 | Oversight, validation, QA, compliance, security, audit, regulatory, incident response, legal, risk, cyber |
| `data_centers/module_19_physical_constraints.csv` | Physical infrastructure limits | Phase 4 | Grid capacity, transformers, substations, transmission, nuclear, gas, renewables, batteries, PPAs, wafer fab, packaging, HBM, networking, cooling, labor, materials, permitting, water, zoning, timelines |
| `data_centers/module_20_systems_dynamics.csv` | Feedback loop integration | Phase 4 | All variables with reinforcing/balancing loops, delays |
| `data_centers/module_21_jevons_paradox.csv` | Jevons paradox elasticity | Phase 4 | Cost reduction %, demand elasticity, scenarios (ε>1, ≈1, <1) |
| `data_centers/module_22_open_source_commoditization.csv` | Open-source model impact | Phase 4 | Quality convergence, time-to-frontier, community innovation, fine-tuning, licensing, enterprise adoption, self-hosting |
| `data_centers/module_23_compute_supply_cycle.csv` | Compute supply cycles | Phase 4 | GPU lead times, wafer allocation, packaging, HBM, rack deployment, network, cooling, utilization, cycle phases |
| `data_centers/module_24_capital_market_reflexivity.csv` | Capital market feedback | Phase 4 | Valuation → fundraising → hiring → CapEx → capacity → valuation |
| `data_centers/module_25_revenue_quality.csv` | Revenue quality tiers | Phase 4 | High/medium/low quality classification, sustainable revenue % |
| `data_centers/module_26_national_strategic_investment.csv` | Government AI investment | Phase 4 | National security, military, scientific leadership, industrial policy, sovereignty, export controls, resilience |
| `data_centers/module_27_labor_market_transformation.csv` | Labor market impact | Phase 4 | Displacement, augmentation, new occupations, wage compression, productivity, reskilling, restructuring |
| `data_centers/module_28_regulatory_scenario.csv` | Regulatory scenarios | Phase 4 | US, China, EU, India, UK, Gulf — copyright, safety, privacy, export, competition, compute licensing, energy |
| `data_centers/module_29_ai_adoption_diffusion.csv` | Technology diffusion curves | Phase 4 | Consumers, SMEs, enterprises, gov, education, healthcare, manufacturing — network effects, learning curves, switching costs |
| `data_centers/module_30_global_macro_feedback.csv` | Macro-AI feedback | Phase 4 | GDP, inflation, rates, productivity, energy, commodities, FX, capital flows, trade, geopolitical risk |
| `data_centers/module_31_black_swan_stress_test.csv` | Stress test parameters | Phase 4 | 13 shock categories with probabilities, magnitudes, correlations |
| `data_centers/module_32_final_tesm.csv` | Integrated TESM outputs | Phase 4 | 5/10/20yr forecasts, scenarios, confidence intervals, sensitivities, key drivers |
| `data_centers/module_33_enterprise_renewal_cliff.csv` | Renewal cliff & sector rotation | Phase 4 | Multi-year index/sector projections, earnings revisions, multiple compression, contract renewal distributions |
| `data_centers/TESM_FULL_RESULTS.json` | Complete simulation output | engine.js / tesm_simulation.py | All time series for all scenarios |
| `data_centers/dcf_valuations.json` | DCF valuation outputs | financial_modeling_final.py | Per-company/facility DCF |
| `data_centers/scenario_analysis.json` | Scenario analysis results | financial_modeling_final.py | Bear/base/bull/stagnation/black swan |
| `data_centers/analyze_macro_outlook.py` | Macro analysis script | — | FRED data processing |

---

## 13. Source Code Files

| **File** | **Purpose** | **Language** |
|----------|-------------|--------------|
| `engine.js` | Core TESM simulation engine (browser/Node) | JavaScript |
| `param_overrides.js` | Calibrated parameter overrides (auto-generated) | JavaScript |
| `tesm_simulation.py` | Python simulation runner | Python |
| `calibrate.py` | Data ingestion & calibration pipeline | Python |
| `financial_modeling.py` / `_fixed.py` / `_final.py` | DCF, scenario, Monte Carlo modeling | Python |
| `historical_validation.py` | Backtesting against dot-com, Japan, railway | Python |
| `data_centers/phase1_master_list.py` | Seed facility list creation | Python |
| `data_centers/phase1_enhance.py` | Facility enrichment (utility, GPU gen, etc.) | Python |
| `data_centers/phase2_harvest.py` / `phase2_enrich.py` | Deep enrichment pipeline | Python |
| `data_centers/phase4_deliverables.py` | Compute capability modeling & deliverables | Python |
| `data_centers/analyze_hyperscalers.py` | Hyperscaler aggregation & analysis | Python |
| `data_centers/create_master_csv.py` | Master CSV compilation | Python |
| `data_centers/verify_hyperscaler_capex.py` | SEC data verification | Python |
| `data_centers/generate_capex_audit.py` | Audit report generation | Python |
| `data_centers/verify_onsite_permits.py` | Onsite power permit verification | Python |
| `data_centers/generate_audit_markdown.py` | Audit markdown generation | Python |
| `data_centers/check_data.py` / `check_data2.py` | Data quality checks | Python |
| `contract_loss_2026_2027.py` | Enterprise contract renewal modeling | Python |
| `app.js` / `server.js` | Web visualization server | JavaScript |
| `index.html` / `styles.css` | Dashboard UI | HTML/CSS |

---

## 14. Key URLs Reference

### Government & Public Data Portals
| **Portal** | **URL** | **Key Datasets** |
|------------|---------|------------------|
| SEC EDGAR/DERA | https://www.sec.gov/edgar/ | Financial statements, XBRL, DERA bulk data |
| FRED (St. Louis Fed) | https://fred.stlouisfed.org/ | 800k+ macro time series |
| EIA | https://www.eia.gov/ | Electricity, natural gas, capacity, generation |
| FERC eLibrary | https://elibrary.ferc.gov/ | Form 715, interconnection, Orders |
| LBNL Queue Data | https://emp.lbl.gov/utility-scale-solar/ | Interconnection queue database |
| USITC DataWeb | https://dataweb.usitc.gov/ | Trade flows (HTS 8542, 8473.30) |
| NREL ReEDS | https://www.nrel.gov/analysis/reeds/ | Capacity expansion model |
| World Bank ICP | https://www.worldbank.org/en/programs/icp | PPP conversion factors |
| OECD SDMX | https://stats.oecd.org/ | International macro data |
| BIS Statistics | https://www.bis.org/statistics/ | Banking, credit, derivatives |
| IMF IFS | https://data.imf.org/ | International financial statistics |

### Industry & Research
| **Source** | **URL** | **Access** |
|------------|---------|------------|
| LMSYS Chatbot Arena | https://huggingface.co/spaces/lmsys/chatbot-arena | Free |
| OpenCompass | https://opencompass.org.cn/ | Free |
| Hugging Face Open LLM Leaderboard | https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard | Free |
| SemiAnalysis | https://semianalysis.com/ | Subscription |
| DC Byte | https://dcbyte.com/ | Subscription |
| Synergy Research | https://www.srgresearch.com/ | Subscription |
| Structure Research | https://structure-research.com/ | Subscription |
| Ken French Data Library | https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html | Free |
| WhaleWisdom 13F | https://whalewisdom.com/ | Free tier |
| Bloom Energy Deployments | https://www.bloomenergy.com/case-studies/ | Public |
| NVIDIA Investor Relations | https://investor.nvidia.com/ | Public |

### Chinese Sources
| **Source** | **URL** | **Content** |
|------------|---------|-------------|
| Zhipu AI Pricing | https://pricing.zhipu.ai/ | API pricing |
| Baichuan AI | https://api.baichuan-ai.com/ | API pricing |
| 01.ai Platform | https://platform.01.ai/ | API pricing |
| Moonshot | https://platform.moonshot.cn/ | API pricing |
| MiniMax | https://api.minimax.chat/ | API pricing |
| Alibaba DashScope | https://dashscope.aliyuncs.com/ | API pricing |
| Tencent Cloud | https://cloud.tencent.com/ | API pricing |
| ByteDance VolcEngine | https://www.volcengine.com/ | API pricing |

---

## 15. Data Quality & Confidence Framework

### Confidence Levels (from DATA_LINEAGE_LOG.csv)
| **Level** | **Criteria** | **Examples** |
|-----------|--------------|--------------|
| **A (High)** | Direct public disclosure (SEC filing, earnings call, utility IRP, vendor case study) | Meta Hyperion Campus: capacity_mw=5000 from "Meta Q4'24 earnings, Entergy IRP, LA PSC dockets, Vertiv case study" |
| **B (Medium)** | Public source but aggregated/indirect (news article, analyst report, government aggregate) | GW Ranch: capacity_mw=7650 from "Public Source, B" |
| **C (Low/Estimated)** | Derived/modelled from other fields (88% IT load factor, GPU density assumptions) | All `est_gpus_*`, `it_load_mw`, `training_bf16_pflops`, `annual_power_cost_usd` |

### Validation Checks (calibrate.py → Great Expectations)
- SEC DERA: Column completeness, tag value ranges, balance sheet identity
- LBNL Queue: Queue days 0-3650, status ∈ {active, withdrawn, operational}
- USITC: HTS code filtering, quarterly aggregation consistency
- Chinese Benchmarks: Elo 800-1500, required fields present

---

## 16. Licensing & Attribution

| **Source Category** | **License** | **Redistribution** | **Attribution Required** | **Commercial Use** |
|---------------------|-------------|-------------------|-------------------------|-------------------|
| SEC EDGAR/DERA | Public Domain | ✅ Yes | ✅ SEC | ✅ Yes |
| LBNL Queue | CC-BY-4.0 / Gov't | ✅ Yes | ✅ LBNL | ✅ Yes |
| USITC DataWeb | Public Domain | ✅ Yes | ✅ USITC | ✅ Yes |
| FRED | Public Domain | ✅ Yes | ✅ St. Louis Fed | ✅ Yes |
| World Bank ICP | CC-BY-4.0 | ✅ Yes | ✅ World Bank | ✅ Yes |
| O*NET | Public Domain | ✅ Yes | ✅ DOL | ✅ Yes |
| BLS / Census | Public Domain | ✅ Yes | ✅ Agency | ✅ Yes |
| Gartner/IDC | Proprietary | ❌ No | ✅ Vendor | ✅ With license |
| Omdia/Synergy | Proprietary | ❌ No | ✅ Vendor | ✅ With license |
| PitchBook/Refinitiv | Proprietary | ❌ No | ✅ Vendor | ✅ With license |
| Earnings Transcripts | Fair Use / Copyright | ⚠️ Limited | ✅ Company | ⚠️ Transformative |
| Chinese Benchmarks | Various (HF, GitHub) | ✅ Mostly | ✅ Source | ✅ Mostly |
| Vendor Pricing Pages | Terms of Service | ⚠️ Scraping policy | ✅ Vendor | ⚠️ Check ToS |

**Compliance Strategy:**
- Public domain / government data: Store raw + processed in versioned data lake
- Proprietary: Store only derived parameters (not raw) + source citations
- Scraped: Respect robots.txt, rate limits, cache aggressively
- All: Document lineage in data catalog (DataHub / Amundsen)

---

## 17. Data Acquisition Cost & Timeline Summary

| **Phase** | **Data Categories** | **Est. Cost** | **Est. Time** | **Team** |
|-----------|---------------------|---------------|---------------|----------|
| **Phase 1 (Months 1-3)** | SEC expanded (100 tickers), LBNL/USITC refresh, Chinese benchmarks, Productivity meta-analysis | $300K | 12 weeks | 2 quant researchers, 1 data engineer |
| **Phase 2 (Months 4-6)** | Revenue quality mapping, Regulatory DB, Macro data, Adoption surveys (Gartner/IDC) | $400K | 12 weeks | 1 quant, 1 policy analyst, 1 data eng |
| **Phase 3 (Months 7-9)** | Physical supply chain (Omdia/Synergy), Chinese DC costs, Agent telemetry partnerships | $600K+ | 12 weeks | 1 supply chain analyst, 1 BD lead |
| **Phase 4 (Months 10-12)** | Black swan expert elicitation, Unit economics primary research, Historical crisis data | $300K | 12 weeks | 2 quant, 1 historian |

**Total: ~$1.6M over 12 months for publication-grade data foundation**

---

*End of Data Sources & Lineage Registry*  
*Generated from project files in `C:\Users\NITHING\Desktop\projections\` as of 2026-07-15*