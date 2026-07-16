# TESM Core Simulation Input Data Catalog
## Complete Inventory of Raw Input Data Files with Detailed Categories

**Project:** Comprehensive Financial Modeling: Dot-com Bubble vs. Today's AI Economy  
**Generated:** 2026-07-15  
**Scope:** Only raw input data files (excludes derived/output files)

---

## DATA SOURCE CLASSIFICATION

| Category | Count | Description |
|----------|-------|-------------|
| **SEC Financial Data** | 65 files | 13 quarters × 5 files per quarter |
| **Grid & Power Infrastructure** | 8 files | LBNL, ISO/RTO, EIA, NREL, FERC |
| **Semiconductor Trade** | 1 file | USITC DataWeb |
| **Macroeconomic** | 1 folder | FRED catalog (24 series) |
| **Chinese AI Ecosystem** | 2 files | Benchmarks + API pricing |
| **Onsite Power Generation** | 5 files | Deployments, heat rates, fuel prices, hedges, grid services |
| **Productivity Research** | 1 file | 16 academic meta-analysis studies |
| **Enterprise Contracts** | 1 file | 15 contract types with NRR/GRR |
| **Regional Infrastructure** | 1 file | 14 regions × 9 parameters |
| **Black Swan Stress Tests** | 1 file | 53 shock parameters |
| **Global Data Centers** | 2 files | 19,694 facilities (4 sources) |
| **Hyperscale Facilities** | 1 file | 52 enriched hyperscale facilities |

---

## 1. SEC EDGAR / DERA FINANCIAL DATA
**Location:** `DATA\{2023q1..2026q1}\` (13 quarterly folders)

### Files per Quarter:
| File | Records | Key Fields |
|------|---------|------------|
| `sub.txt` | ~200K | adsh, cik, name, sic, countryba, stprba, cityba, zipba, bas1, bas2, baph, form, period, fy, fp, filed, accepted, prevrpt, detail, instance, nciks, aciks |
| `num.txt` | ~2M | adsh, tag, version, ddate, qtrs, uom, coreg, value, footnote |
| `pre.txt` | ~50K | adsh, report, line, stmt, inpth, rfile, tag, version, plabel, negating |
| `tag.txt` | ~15K | tag, version, custom, abstract, datatype, iord, crdr, tlabel, doc |
| `readme.htm` | — | Documentation |

### Hyperscalers Tracked (6):
- MICROSOFT, AMAZON, ALPHABET, SALESFORCE, META PLATFORMS, ORACLE

### XBRL Tags Extracted:
| Category | Tags |
|----------|------|
| **CapEx** | PaymentsToAcquirePropertyPlantAndEquipment, PaymentsToAcquireProductiveAssets |
| **RPO/Deferred Revenue** | ContractWithCustomerLiabilityCurrent, ContractWithCustomerLiabilityNoncurrent, ContractWithCustomerLiability, RevenueRemainingPerformanceObligation |
| **Revenue** | RevenueFromContractWithCustomerExcludingAssessedTax, Revenues, RevenueFromContractWithCustomerIncludingAssessedTax |
| **Other** | ResearchAndDevelopmentExpense, ShareBasedCompensation, SegmentRevenue, SegmentProfit |

---

## 2. GRID & POWER INFRASTRUCTURE

### 2.1 LBNL Interconnection Queue
**File:** `DATA/LBNL_Ix_Queue_Data_File_thru2025.xlsx` (15.6 MB)
**Sheet:** "03. Complete Queue Data"
**Records:** ~10,000 projects

| Column | Description | Example |
|--------|-------------|---------|
| `project_id` | Unique project identifier | PJM_2023_1234 |
| `q_date` | Queue entry date | 2023-01-15 |
| `wd_date` | Withdrawal date | 2024-03-20 |
| `on_date` | Commercial online date | 2026-06-01 |
| `ia_date` | Interconnection agreement date | 2024-09-15 |
| `mw_1` | MW capacity requested | 500 |
| `type_clean` | Technology type | "Data Center", "Storage", "Battery" |
| `project_type` | Project classification | "Data Center" |
| `status_col` | Current status | "Active", "Withdrawn", "Suspended", "In Service" |
| `state` | US state | "VA", "TX", "OH" |
| `iso` | ISO/RTO region | "PJM", "ERCOT", "CAISO", "MISO" |
| `voltage_kv` | Interconnection voltage | 500, 230, 138 |
| `county` | County name | "Loudoun", "Harris" |
| `utility` | Transmission owner | "Dominion", "Oncor" |

**Filter Applied:** `type_clean` OR `project_type` contains "data center", "storage", "battery" AND `mw_1 > 0`

---

### 2.2 ISO/RTO Queue Data (Direct Sources)
**URLs:**
| ISO | Portal | Key Data |
|-----|--------|----------|
| PJM | pjm.com/planning/services-requests/interconnection-queues | Queue Dashboard, Project Status |
| ERCOT | ercot.com/gridinfo/resource | GINR, Project Tracking |
| CAISO | caiso.com/planning/Pages/GeneratorInterconnection | Queue Cluster Results |
| MISO | misoenergy.org/planning/generator-interconnection | DPP Results |
| NYISO | nyiso.com/interconnection-process | Queue Status |
| ISO-NE | iso-ne.com/ws/document | IR Queue |
| SPP | spp.org/engineering/generator-interconnection | GI Queue |

---

### 2.3 FERC Form 715
**Source:** FERC eLibrary (elibrary.ferc.gov)
**Coverage:** All US transmission owners
**Key Variables:** Line ratings, loading, planned upgrades, thermal limits, contingency analysis

---

### 2.4 EIA Forms
| Form | File | Key Variables |
|------|------|---------------|
| **EIA-860** | `DATA/power/` (implicit) | Generator capacity, fuel, emissions, retirement plans, technology, prime mover |
| **EIA-923** | `DATA/power/` (implicit) | Generation, fuel consumption, heat rates, fuel costs, operating costs |

---

### 2.5 NREL Models
| Model | URL | Use Case |
|-------|-----|----------|
| ReEDS | nrel.gov/analysis/reeds | Least-cost capacity expansion |
| GridPath | gridpath.io | Open-source power system model |

---

### 2.6 USITC Semiconductor Trade
**File:** `DATA/DataWeb-Query-Export.xlsx` (166 KB)
**Sheet:** "Query Results"
**HTS Codes:** 8542 (Integrated circuits), 8473.30 (Parts for ADP machines)

| Column | Description |
|--------|-------------|
| `hts_number` | HTS classification code |
| `description` | Product description |
| `country` | Trading partner country |
| `year` | Calendar year |
| `month` | Month (1-12) |
| `customs_value` | Import value (USD) |
| `quantity` | Quantity (units/kg) |
| `unit_of_measure` | Unit type |

**Aggregation:** Quarterly silicon supply metric = Σ customs_value / 1e9 (billions USD)

---

## 3. MACROECONOMIC DATA (FRED)

### 3.1 Core Time Series (24 Series)
**Location:** `DATA/macro/` + FRED API

| Series ID | Name | Frequency | Units | History | Use Case |
|-----------|------|-----------|-------|---------|----------|
| GDPC1 | Real Gross Domestic Product | Quarterly | Billions Chained 2017 $ | 1947+ | Output gap, potential growth |
| CPIAUCSL | CPI All Urban Consumers | Monthly | Index 1982-84=100 | 1959+ | Inflation expectations |
| PCEPILFE | Core PCE Price Index | Monthly | Index 2017=100 | 1959+ | Fed preferred inflation |
| FEDFUNDS | Effective Federal Funds Rate | Daily | Percent | 1954+ | Monetary policy stance |
| DGS10 | 10-Year Treasury Constant Maturity | Daily | Percent | 1962+ | Discount rate, term premium |
| T10Y2Y | 10Y-2Y Treasury Spread | Daily | Percent | 1976+ | Recession predictor |
| BAMLC0A0CMEY | ICE BofA US Corporate Index Yield | Daily | Percent | 1996+ | IG credit conditions |
| BAMLH0A0HYM2 | ICE BofA US High Yield Index Yield | Daily | Percent | 1996+ | HY credit conditions |
| DTWEXBGS | Broad US Dollar Index | Daily | Index Jan 2006=100 | 1973+ | Currency effects |
| DCOILWTICO | WTI Crude Oil Price | Daily | $/Barrel | 1986+ | Energy costs |
| DCOILBRENTEU | Brent Crude Oil Price | Daily | $/Barrel | 1986+ | Global energy costs |
| DHHNGSP | Henry Hub Natural Gas Spot | Daily | $/MMBtu | 1986+ | DC energy costs |
| PCOPPUSDM | Global Copper Price | Monthly | $/Metric Ton | 2000+ | Hardware BOM |
| PLITUSDM | Global Lithium Price | Monthly | $/Metric Ton | 2000+ | Battery costs |
| PCOBUSDM | Global Cobalt Price | Monthly | $/Metric Ton | 2000+ | Battery costs |
| UNRATE | Unemployment Rate | Monthly | Percent | 1948+ | Labor market |
| JTSJOL | Job Openings: Total Nonfarm | Monthly | Thousands | 2000+ | Labor demand |
| CES0500000003 | Avg Hourly Earnings: Total Private | Monthly | $/Hour | 2006+ | Wage growth |
| INDPRO | Industrial Production Index | Monthly | Index 2017=100 | 1919+ | Manufacturing output |
| UMCSENT | Michigan Consumer Sentiment | Monthly | Index 1966=100 | 1978+ | Consumer confidence |
| TCU | Capacity Utilization: Total Industry | Monthly | Percent | 1967+ | Industrial slack |
| GFDEBTN | Federal Debt: Total Public Debt | Quarterly | Millions $ | 1966+ | Fiscal position |
| M2SL | M2 Money Stock | Monthly | Billions $ | 1959+ | Monetary aggregates |

---

## 4. CHINESE AI ECOSYSTEM

### 4.1 Model Benchmarks
**File:** `DATA/china_benchmarks.csv` (3 KB, 26 records)

| Column | Description | Example |
|--------|-------------|---------|
| `model` | Model identifier | "glm_5_2", "qwen_2_5_72b" |
| `organization` | Developer | "zhipu_ai", "alibaba", "deepseek" |
| `benchmark` | Benchmark name | "lmsys_chatbot_arena" |
| `score` | Elo rating | 1247, 1234, 1287 |
| `date` | Evaluation date | "2024-11", "2024-09" |
| `language` | Language coverage | "zh/en", "en" |
| `model_type` | "proprietary" or "open_weight" | "open_weight" |
| `parameters_b` | Parameter count (billions) | 72, 405, "?" |
| `source` | Data source | "Zhipu AI / LMSYS" |
| `source_url` | URL | "https://chat.lmsys.org/" |
| `notes` | Release info | "GLM-5.2 release" |

**Key Models Tracked:**
| Model | Org | Type | Elo | Date |
|-------|-----|------|-----|------|
| GLM-5.2 | Zhipu AI | Proprietary | 1247 | 2024-11 |
| GLM-4 | Zhipu AI | Proprietary | 1198 | 2024-06 |
| LongCat 2.0 | Alibaba | Open-weight | 1182 | 2024-10 |
| Qwen2.5-72B | Alibaba | Open-weight | 1234 | 2024-09 |
| Qwen2.5-32B | Alibaba | Open-weight | 1189 | 2024-09 |
| DeepSeek-V2.5 | DeepSeek | Open-weight | 1201 | 2024-07 |
| Yi-34B | 01.ai | Open-weight | 1167 | 2024-05 |
| Kimi (Moonshot-v1) | Moonshot | Proprietary | 1134 | 2024-07 |
| **GPT-4o** | OpenAI | Proprietary | **1287** | 2024-05 |
| **Claude 3.5 Sonnet** | Anthropic | Proprietary | **1271** | 2024-06 |
| **Llama-3.1-405B** | Meta | Open-weight | **1265** | 2024-07 |

---

### 4.2 Chinese API Pricing
**File:** `DATA/china_api_pricing.csv` (2 KB, 22 records)

| Column | Description | Example |
|--------|-------------|---------|
| `provider` | Provider identifier | "zhipu_ai", "alibaba", "deepseek" |
| `model` | Model name | "glm_4", "qwen_max", "deepseek_v2_5" |
| `input_price_usd_per_million_tokens` | Input pricing | 0.14, 0.16, 0.14 |
| `output_price_usd_per_million_tokens` | Output pricing | 0.14, 0.16, 0.28 |
| `currency` | Currency | "USD" |
| `date` | Pricing date | "2024-11" |
| `source` | Source name | "Zhipu AI Platform" |
| `source_url` | URL | "https://open.bigmodel.cn/" |
| `notes` | Additional info | "~1 RMB/M tokens" |

**Price Comparison (Input/Output per 1M tokens):**
| Provider | Model | Input | Output | vs GPT-4o |
|----------|-------|-------|--------|-----------|
| Zhipu AI | GLM-4 | $0.14 | $0.14 | **94% cheaper** |
| Alibaba | Qwen-Max | $0.16 | $0.16 | 94% cheaper |
| DeepSeek | V2.5 | $0.14 | $0.28 | 94% cheaper |
| 01.ai | Yi-34B | $0.15 | $0.15 | 94% cheaper |
| **OpenAI** | **GPT-4o** | **$2.50** | **$10.00** | **Baseline** |
| **Anthropic** | **Claude 3.5 Sonnet** | **$3.00** | **$15.00** | Premium |

---

## 5. ONSITE POWER GENERATION

### 5.1 Onsite Generation Capacity
**File:** `DATA/onsite_gen_capacity.csv` (2 KB, 508 records)

| Column | Description | Example |
|--------|-------------|---------|
| `company` | Hyperscaler | "microsoft", "google", "aws", "oracle" |
| `region` | Geographic region | "us" |
| `technology` | Technology type | "bloom_sofc", "gas_turbine", "hydrogen_fc" |
| `capacity_mw` | Nameplate capacity | 20, 50, 198, 1200 |
| `cod_year` | Commercial operation year | 2021, 2024, 2025, 2026 |
| `capacity_factor` | Annual capacity factor | 0.75, 0.85, 0.90 |
| `heat_rate_btu_kwh` | Heat rate (HHV) | 6800, 9500, 5500 |
| `fuel_type` | Fuel | "natural_gas", "hydrogen" |
| `deployment_source` | Source reference | "bloomenergy_oracle_1.2gw" |

**Aggregated by Company:**
| Company | Technology | Total MW | Years |
|---------|------------|----------|-------|
| Microsoft | Bloom SOFC | 60 (20×3) | 2024-2026 |
| Microsoft | Hydrogen FC | 4.5 | 2021-2022 |
| Microsoft | Gas Turbine | 198 | 2008 |
| Google | Bloom SOFC | 150 (50×3) | 2024-2026 |
| Google | Gas Turbine | 300 | 2025 |
| AWS | Bloom SOFC | 109 (24.3×3 + 20×3) | 2024-2026 |
| Oracle | Bloom SOFC | 4400 (1200+1600×2) | 2024-2026 |
| Intel | Bloom SOFC | 150 | 2014, 2024 |
| CoreWeave | Bloom SOFC | 100 | 2026 |
| Equinix | Bloom SOFC | 50 | 2024 |
| Digital Realty | Bloom SOFC | 30 | 2024 |
| CyrusOne | Bloom SOFC | 25 | 2024 |

---

### 5.2 Heat Rates & Degradation
**File:** `DATA/heat_rates.csv` (3 KB, 58 records)

| Column | Description | Example |
|--------|-------------|---------|
| `unit` | Equipment model | "bloom_es5", "ge_7ha" |
| `technology` | Technology class | "sofc", "gas_turbine", "rice" |
| `fuel_type` | Fuel | "natural_gas", "hydrogen" |
| `heat_rate_btu_kwh` | HHV heat rate | 6800, 9200, 8200 |
| `date` | Effective date | "2024-01", "2025-01" |
| `degradation_pct_yr` | Annual degradation % | 0.5, 0.7, 0.5 |
| `source` | Source | "bloomenergy_whitepaper", "ge_specs" |

**Technology Degradation Rates:**
| Technology | Annual Degradation | Quarterly | Source |
|------------|-------------------|-----------|--------|
| Bloom SOFC | 0.5% | 0.125% | Bloom whitepaper |
| GE 7HA Gas Turbine | 0.7% | 0.175% | GE specs |
| Siemens HL Gas Turbine | 0.6% | 0.15% | Siemens specs |
| Wärtsilä 18V50SG RICE | 0.5% | 0.125% | Wärtsilä specs |
| Plug Power H2 FC | 0.3% | 0.075% | Plug Power specs |
| Solar + Storage | 0.5% | 0.125% | NREL |
| NuScale SMR | 0.1% | 0.025% | Industry |

---

### 5.3 Fuel Prices (Term Structure)
**File:** `DATA/fuel_prices.csv` (3 KB, 1,808 records)

| Column | Description | Example |
|--------|-------------|---------|
| `hub` | Trading hub | "henry_hub", "ttf", "jk" |
| `date` | Month (YYYY-MM) | "2023-01" through "2026-12" |
| `price_usd_mmbtu` | Spot price | 2.50, 27.0, 33.0 |
| `basis_diff_usd_mmbtu` | Basis differential | 0.0 (spot reference) |
| `volatility_pct` | Annualized volatility | 35, 45 |
| `source` | Data source | "eia", "ice" |

**Hub Statistics (2026):**
| Hub | Spot ($/MMBtu) | 1Y Forward | Volatility |
|-----|----------------|------------|------------|
| Henry Hub (US) | 4.50 | 4.60 | 35% |
| TTF (Europe) | 27.0 | 28.0 | 45% |
| JKM (NE Asia) | 33.0 | 34.0 | 45% |

---

### 5.4 Hedge Ratios
**File:** `DATA/hedge_ratios.csv` (2 KB, 18 records)

| Column | Description | Example |
|--------|-------------|---------|
| `company` | Hyperscaler | "microsoft", "google", "aws", "meta", "oracle", "intel" |
| `commodity` | Hedged commodity | "natural_gas" |
| `hedge_ratio` | Fraction hedged | 0.55, 0.65, 0.75, 0.80 |
| `tenor_yr` | Hedge tenor (years) | 2, 3 |
| `instruments` | Instrument types | "swaps_collars", "swaps", "swaps_collars_physical" |
| `date` | As of date | "2024-01", "2025-01", "2026-01" |
| `source` | Filing source | "microsoft_10k", "alphabet_10k" |

**Trend:** Hedge ratios increasing over time (2024: 0.55-0.70 → 2026: 0.65-0.80)

---

### 5.5 Grid Services Revenue
**File:** `DATA/grid_services_revenue.csv` (4.5 KB, 8+ records)

| Column | Description | Example |
|--------|-------------|---------|
| `iso` | ISO/RTO | "caiso" |
| `service` | Ancillary service | "regulation_up", "regulation_down", "spinning_reserve", "non_spinning_reserve" |
| `price_usd_mw_yr` | Annual price per MW | 45000, 38000, 25000, 18000 |
| `volume_mw` | Available volume | 1200, 1100, 800, 600 |
| `date` | Price date | "2024-01" |
| `source` | Market report | "caiso_market_report" |

**Weighted Average:** ~$25,000-40,000/MW-yr depending on service mix

---

### 5.6 Additional Power Files
| File | Description |
|------|-------------|
| `DATA/carbon_prices.csv` | EU ETS, CA Cap-and-Trade, RGGI, UK ETS, China ETS prices |
| `DATA/grid_connection_delays.csv` | Project-level queue delay distributions |
| `DATA/transformer_shortage.csv` | Transformer lead times (52-104 weeks), capacity, price trends |
| `DATA/wholesale_electricity_prices.csv` | Hub-level wholesale power prices |
| `DATA/power/fuel_prices.csv` | Duplicate of root fuel_prices.csv |
| `DATA/power/grid_services_revenue.csv` | Duplicate of root grid_services_revenue.csv |
| `DATA/power/heat_rates.csv` | Duplicate of root heat_rates.csv |
| `DATA/power/hedge_ratios.csv` | Duplicate of root hedge_ratios.csv |
| `DATA/power/onsite_gen_capacity.csv` | Duplicate of root onsite_gen_capacity.csv |

---

## 6. PRODUCTIVITY RESEARCH

### 6.1 Academic Meta-Analysis
**File:** `DATA/productivity_meta_analysis.csv` (2 KB, 16 records)
**Also:** `DATA/productivity/meta_analysis_studies.csv` (duplicate)

| Column | Description | Example |
|--------|-------------|---------|
| `study` | Study identifier | "peng_2023", "noy_2023" |
| `category` | Task category | "coding", "writing", "consulting", "customer_support", "legal", "rd_materials", "rd_drug", "general" |
| `intervention` | AI tool | "github_copilot", "chatgpt", "ai_assistant", "genai_assistant" |
| `industry` | Industry sector | "software_engineering", "professional_services", "consulting", "technology", "legal", "materials_science", "pharma", "all_occupations" |
| `task_type` | Specific task | "code_generation", "business_writing", "strategy_analysis", "ticket_resolution", "document_review", "experiment_design", "drug_discovery", "task_automation" |
| `sample_size` | N | 95, 444, 5172, 2000 |
| `effect_size_pct` | Productivity gain % | 55.8, 37.0, 13.8, 42.0 |
| `ci_lower_pct` | 95% CI lower | 40.2, 28.0, 10.5, 35.0 |
| `ci_upper_pct` | 95% CI upper | 71.4, 46.0, 17.1, 49.0 |
| `study_design` | "rct", "quasi_exp", "survey", "meta_analysis" | "rct" |
| `quality_score` | "high", "medium" | "high" |
| `source` | Citation | "Peng et al. 2023 (Microsoft)" |
| `source_url` | URL | "https://arxiv.org/abs/2302.06590" |
| `date` | Publication year | 2023, 2024 |

**Effect Sizes by Category:**
| Category | Studies | Mean Effect | Range | Key Studies |
|----------|---------|-------------|-------|-------------|
| **Coding** | 5 | 42.3% | 28.5-55.8% | Peng (Copilot 55.8%), Kalliamvakou (42%), Tabachnyk (37%), Moradi (28.5%), Zhang (48%) |
| **Writing** | 1 | 37.0% | — | Noy & Zhang (Science 2023) |
| **Consulting** | 2 | 28.1% | 25.1-31.0% | Dell'Acqua (BCG 25.1%), Agrawal (31%) |
| **Customer Support** | 2 | 17.9% | 13.8-22.0% | Brynjolfsson (NBER 13.8%), Cui (QJE 22%) |
| **Legal** | 1 | 23.5% | — | Kanazawa (23.5%) |
| **R&D Materials** | 1 | 44.0% | — | Wang (Nature 44%) |
| **R&D Drug** | 1 | 38.5% | — | Liu (Nature 38.5%) |
| **General** | 2 | 13.5% | 12-15% | Eloundou (OpenAI 15%), Felten (12%) |

---

## 7. ENTERPRISE CONTRACTS

### 7.1 Contract Database
**File:** `DATA/enterprise_contracts.csv` (2 KB, 15 records)

| Column | Description | Example |
|--------|-------------|---------|
| `company` | Provider | "aws", "azure", "gcp", "oracle", "salesforce", "servicenow", "databricks", "snowflake", "meta" |
| `contract_type` | Type | "enterprise_agreement", "reserved_instances", "savings_plans", "committed_use_discounts", "universal_credits", "enterprise_saas" |
| `avg_contract_length_years` | Typical length | 3, 5 |
| `renewal_rate_pct` | Renewal % | 85-95 |
| `downsizing_pct_at_renewal` | Downsizing % | 8-25 |
| `expansion_pct_at_renewal` | Expansion % | 8-50 |
| `net_revenue_retention_pct` | NRR | 100-130 |
| `gross_revenue_retention_pct` | GRR | 92-99 |
| `year` | Data year | 2024 |
| `source` | Source | "AWS 10-K / Flexera", "Microsoft 10-K / ICONIQ" |
| `source_url` | URL | SEC filing URLs |
| `notes` | Notes | "EA typically 3-5yr; NRR ~115%" |

**By Contract Type:**
| Type | Count | Avg Length | Renewal | NRR | Downsizing | Expansion |
|------|-------|------------|---------|-----|------------|-----------|
| Enterprise Agreement | 5 | 3 yr | 93% | 111% | 18% | 22% |
| Reserved Instances | 3 | 3 yr | 89% | 104% | 22% | 9% |
| Savings Plans | 4 | 3-5 yr | 91% | 109% | 19% | 14% |
| Committed Use (GCP) | 2 | 3-5 yr | 90% | 110% | 19% | 19% |
| Universal Credits (Oracle) | 1 | 3 yr | 92% | 108% | 20% | 15% |
| Enterprise SaaS | 4 | 3 yr | 89% | 126% | 11% | 39% |

---

## 8. REGIONAL INFRASTRUCTURE

### 8.1 Regional Parameters
**File:** `DATA/regional_infrastructure.csv` (2.5 KB, 14 records)

| Column | Description | Example |
|--------|-------------|---------|
| `region` | Region key | "us", "china", "india", "gulf", "eu", "japan", "korea", "taiwan", "vietnam", "indonesia", "malaysia", "singapore" |
| `country` | Country name | "United States", "China", "India", "UAE", "Saudi Arabia", "EU Average", "Japan", "South Korea", "Taiwan", "Vietnam", "Indonesia", "Malaysia", "Singapore" |
| `ppp_factor_usd_base` | PPP vs USD | 1.00, 0.55, 0.45, 0.80, 0.75, 1.15, 0.95, 0.90, 0.85, 0.50, 0.45, 0.60, 1.05 |
| `power_growth_cap_annual_pct` | Max annual power growth % | 12, 24, 18, 26, 28, 5, 4, 8, 10, 15, 12, 10, 6 |
| `grid_connection_delay_months` | Grid queue delay | 24, 12, 18, 8, 6, 48, 36, 18, 24, 18, 24, 18, 12 |
| `gov_coordination_index` | Gov coordination (0-1) | 0.50, 0.95, 0.70, 0.85, 0.90, 0.30, 0.60, 0.75, 0.70, 0.65, 0.55, 0.65, 0.85 |
| `cost_per_mw_usd_millions` | CapEx per MW ($M) | 2.50, 1.10, 1.30, 1.70, 1.50, 3.10, 3.50, 2.20, 2.00, 1.40, 1.60, 1.80, 3.00 |
| `transformer_shortage_factor` | Shortage severity | 0.20, 0.10, 0.15, 0.05, 0.05, 0.25, 0.20, 0.15, 0.15, 0.10, 0.10, 0.15, 0.20 |
| `cooling_water_availability` | Water availability (0-1) | 0.35, 0.15, 0.10, 0.05, 0.05, 0.40, 0.15, 0.10, 0.15, 0.20, 0.15, 0.15, 0.05 |
| `renewable_penetration_pct` | Renewable share | 22, 35, 25, 5, 2, 45, 22, 10, 15, 30, 15, 25, 5 |

---

## 9. BLACK SWAN STRESS TESTS

### 9.1 Shock Parameters
**File:** `DATA/module_31_black_swan_stress_test.csv` (5 KB, 53 records)

| Column | Description | Example |
|--------|-------------|---------|
| `module` | Module name | "Black_Swan_Stress_Test", "Stress_Test_Scenario" |
| `metric` | Parameter name | "global_recession_probability_annual", "bear_case_ai_demand_shock_pct" |
| `value` | Parameter value | 0.15, 0.20 |
| `unit` | Unit | "ratio", "months", "USD_B", "percent" |
| `source` | Source citation | "IMF 2026; Historical frequency 1960-2024" |
| `source_url` | URL | "https://www.imf.org" |
| `date_accessed` | Date | "2026-07-14" |
| `confidence` | "High", "Medium", "Low", "Very_Low" | "High" |
| `notes` | Description | "~15% annual probability (1 in 7 years historically)" |

**Shock Categories (13):**
| Shock | Annual Probability | Key Parameters |
|-------|-------------------|----------------|
| Global Recession | 15% | GDP -3.5%, unemployment +3-5pp, spreads 2-3x |
| Energy Crisis | 5% | Oil +150%, gas +300%, electricity +300% |
| Semiconductor Disruption | 3% | Foundry -30-50%, lead time 2-4x, TSMC 6-12mo recovery |
| Taiwan Strait Conflict | 1-2% | TSMC offline, shipping disruption, -5% global GDP |
| Major Cyber Incident | 2% | Cloud outage 1-4 weeks, $10-100B losses |
| AI Safety Event | 1% | -20% AI sector market cap |
| Financial Crisis | 3% | Equity -30-50%, credit freeze, AI capex -50% |
| Geopolitical Conflict | 2% | Taiwan/Korea/ME, supply chain disruption |
| Regulatory Shock | 5% | EU AI Act fines, US EO expansion, China crackdown |
| Algorithmic Breakthrough | 10% | 5-10x efficiency → 50% compute demand reduction |
| Hardware Breakthrough | 3% | New memory/interconnect/packaging |
| Quantum Crypto Break | 0.5% | RSA/ECC broken, PQC transition $100B+ |
| Fusion Commercialization | 15% (by 2030) | 90% cheaper electricity |
| Sustained AI Deflation | 30% | 50%+ annual cost declines → 40% capex reduction |

---

## 10. GLOBAL DATA CENTERS (Raw Sources)

### 10.1 GitHub Global-Data-Center-Map
**File:** `global_datacenters_github.csv` (1.7 MB, 18,089 records)
**Source:** ATLAS dataset (OpenStreetMap ODbL)

| Column | Description |
|--------|-------------|
| `source` | "GitHub_GlobalMap" |
| `facility_name` | Facility name |
| `operator` | Operating company |
| `city` | City |
| `state_province` | State/province |
| `country` | Country |
| `address` | Street address |
| `status` | "Operating" (primary) |
| `capacity_mw` | Power capacity (where available) |
| `capacity_category` | Size classification |
| `facility_size_sqft` | Building square footage |
| `property_size_acres` | Land area |
| `project_cost_usd` | Announced cost |
| `expected_online_date` | Target completion |
| `latitude` | Latitude |
| `longitude` | Longitude |
| `cooling_type` | Cooling method |
| `power_source` | Primary power source |
| `tenant` | Anchor tenant |
| `purpose` | AI/Cloud/Crypto/Enterprise/Telecom |
| `community_pushback` | Opposition noted |
| `notes` | Additional details |
| `source_url` | Primary source URL |
| `date_added` | Date added to tracker |
| `last_updated` | Last update |

**Coverage:** 116 countries, 4,181 operators

---

### 10.2 FracTracker US Tracker
**File:** `fractracker_us_datacenters.csv` (728 KB, 1,579 records)
**Source:** Community-sourced from media monitoring

| Column | Description |
|--------|-------------|
| Same as above + | |
| `status` | Operating, Planned, Under Construction, Cancelled, Suspended, Expanding |

**US Status Breakdown:**
| Status | Count |
|--------|-------|
| Operating | 1,200+ |
| Planned | 200+ |
| Under Construction | 50+ |
| Cancelled | 20+ |
| Suspended | 15+ |
| Expanding | 15+ |

---

### 10.3 DCMap.us Pipeline (Embedded in master)
**Source:** dcmap.us
**Records:** 1,063 US pipeline projects
**Total Capacity:** 250,993 MW
**Under Construction:** 162 projects (31,021 MW)
**Planned/Approved:** 901 projects (219,972 MW)

**Top States by Pipeline:**
| State | Projects | Capacity (MW) |
|-------|----------|---------------|
| Texas | 157 | 67,803 |
| Virginia | 183 | 23,222 |
| Georgia | 97 | 8,810 |
| Arizona | 44 | 13,372 |
| Pennsylvania | 41 | 13,376 |
| Ohio | 53 | 6,579 |
| Indiana | 38 | 9,463 |
| Illinois | 34 | 8,506 |

---

### 10.4 DataCenterMap.info
**Records:** 15 country-level aggregates
**Coverage:** 11,873 facilities across 179 countries

---

## 11. HYPERSCALE FACILITIES (Enriched)

### 11.1 Master Facility List v3 Enriched
**File:** `data_centers/master_facility_list_v3_enriched.json` (86 KB, 52 records)
**File:** `data_centers/master_facility_list_v3_enriched.csv` (22 KB, 52 records)

**Base Fields (from raw sources):**
| Field | Source |
|-------|--------|
| `facility_id` | DC-00001... |
| `facility_name` | "Stratos Hyperscale Campus" |
| `operator` | "Bitzero Blockchain Inc." |
| `tenant` | "2027" or "Meta" |
| `hyperscaler_category` | "Meta", "AWS", "Other/Unclassified" |
| `city`, `state_province`, `country` | Location |
| `status` | "Planned", "Under Construction", "Operating", "Suspended" |
| `capacity_mw` | Utility capacity |
| `capacity_category` | "Mega campus (>1GW)", "Hyperscale (100-999 MW)" |
| `source_url` | Primary source |
| `notes` | "AI/Hyperscale", "$1.6B+ investment" |
| `tier` | "Tier 1", "Tier 2", "Tier 3" |

**Enriched/Computed Fields (Phase 4):**
| Field | Computation | Example |
|-------|-------------|---------|
| `it_load_mw` | capacity_mw × 0.88 | 7920 |
| `est_gpus_h100` | it_load_mw / 0.7kW × 1000 | 1,267,200 |
| `est_gpus_b200` | it_load_mw / 1.4kW × 1000 | 792,000 |
| `est_gpus_mi300x` | it_load_mw / 1.1kW × 1000 | 1,188,000 |
| `est_gpus_gb200_nvl72` | it_load_mw / 0.28kW × 1000 | 4,752,000 |
| `est_racks_50kw` | it_load_mw × 20 | 158,400 |
| `est_racks_100kw` | it_load_mw × 10 | 79,200 |
| `est_bf16_pflops` | GPU count × 0.989 TFLOPS / 1000 | 4,579.7 |
| `est_fp8_pflops` | GPU count × 1.979 TFLOPS / 1000 | 9,160.6 |
| `utility` | From IRP/filings | "Entergy Louisiana" |
| `voltage_kv` | Interconnection | 500 |
| `ppa_price_mwh` | Power purchase price | 35 |
| `generation_mix` | Utility mix | "Gas 60%, Nuclear 25%, Renewable 15%" |
| `cooling_detail` | Cooling tech | "Direct-to-chip liquid (80%) + rear-door (20%)" |
| `water_source_mgd` | Water usage | 5.2 |
| `network_detail` | Interconnect | "NVL72 + InfiniBand NDR 400G" |
| `gpu_generation` | GPU type | "H100 (2025), B200 (2026+)" |
| `cluster_size` | GPUs per cluster | 32,768 |
| `total_capex_billion` | Known CapEx | 10 |
| `est_capex_per_kw` | total_capex / capacity_mw | 2,000 |
| `est_capex_per_gpu` | total_capex / GPU count | 14,205 |
| `primary_gpu` | Dominant GPU | "B200" |
| `est_gpu_count` | Primary estimate | 440,000 |
| `training_bf16_pflops` | Training capacity | 990.0 |
| `inference_fp8_pflops` | Inference capacity | 1,980.0 |
| `est_tokens_per_sec_billions` | Token throughput | 0.066 |
| `est_training_runs_per_year_gpt4_class` | Annual training runs | 1.2 |
| `annual_power_mwh` | capacity_mw × 8760 × 0.88 | 38,544,000 |
| `annual_power_cost_usd` | annual_power_mwh × ppa_price | 1,349,040,000 |
| `annual_revenue_potential_usd` | tokens × $0.001/1K × 50% util | 1,040,688,000 |
| `power_cost_per_gpu_per_year` | power_cost / GPU count | 3,066 |

---

## 12. TECHNOLOGY PARAMETERS

### 12.1 Technology Specifications
**File:** `DATA/technology_parameters.csv` (8.8 KB, 55 records)

| Column | Description |
|--------|-------------|
| `technology` | "bloom_sofc", "gas_turbine_7ha", "rice_wartsila_18v50sg", "hydrogen_fc_plug", "solar_storage", "smr_nuscale" |
| `parameter` | "heat_rate_btu_per_kwh_hhv", "electrical_efficiency_lhv_pct", "capacity_factor", "co2_emissions_ton_per_mwh", "water_intensity_l_per_mwh", "capex_usd_per_kw", "om_usd_per_mwh", "degradation_pct_per_year" |
| `value` | Numeric value |
| `unit` | Unit |
| `source` | Vendor/analyst |
| `source_url` | URL |
| `date_accessed` | 2026-07-14 |
| `notes` | Context |

**Key Specifications:**
| Technology | Heat Rate (HHV) | Efficiency (LHV) | CapEx ($/kW) | CO2 (t/MWh) | Water (L/MWh) | Degradation |
|------------|-----------------|------------------|--------------|-------------|---------------|-------------|
| Bloom SOFC | 6,800 | 65% | 4,500 | 0.20 | 0.5 | 0.5%/yr |
| GE 7HA Gas Turbine | 9,500 | 43.2% | 1,500 | 0.40 | 1.5 | 0.7%/yr |
| Wärtsilä 18V50SG RICE | 8,500 | 50% | 1,200 | 0.35 | 1.2 | 0.5%/yr |
| Plug Power H2 FC | 6,200 | 55% | 3,500 | 0.00 | 0.3 | 0.3%/yr |
| Solar + Storage | N/A | N/A | 1,500 | 0.00 | 0.1 | 0.5%/yr |
| NuScale SMR | N/A | 33% | 6,500 | 0.00 | 0.8 | 0.1%/yr |

---

## 13. CALIBRATION OUTPUTS (Auto-Generated)

### 13.1 Parameter Overrides
**File:** `param_overrides.js` (111 KB)
**Generated by:** `calibrate.py`
**Contents:** All 60+ calibrated scalar parameters + raw CSV data dumps

### 13.2 Quarterly Time Series
**From:** SEC DERA processing
**Variables:** CapEx_sum, RPO_sum, Rev_sum per quarter (2023q1-2026q1)

### 13.3 Calibration Metadata
- SEC quarters processed: 13
- Hyperscalers: 6
- LBNL grid projects: ~10,000
- Mean queue: 20 quarters
- Withdrawal rate: 75%

---

## USAGE IN SIMULATION ENGINE

### Input → Parameter Mapping:
| Data Source | calibrate.py Output | engine.js Parameter |
|-------------|---------------------|---------------------|
| SEC DERA | downsizingRatio, capitalReflexivity, siliconSupply | merged.downsizingRatio, merged.capitalReflexivity, merged.initialSilicon |
| LBNL Queue | gridConnectionDelay, powerGrowthCap, transformerShortage | merged.gridConnectionDelay, merged.powerGrowthCap, merged.transformerShortage |
| USITC | siliconSupply | merged.siliconSupply |
| China Benchmarks | chinaEloGap, chinaConvergenceRate, chinaOpenWeightShare, chinaFrontierLag | merged.chinaEloGap, merged.chinaConvergenceRate, merged.chinaOpenWeightShare, merged.chinaFrontierLag |
| China API Pricing | chinaPriceDiscount, chinaPriceCompressionVelocity | merged.chinaPriceDiscount, merged.chinaPriceCompressionVelocity |
| Productivity | elasticityByCategory, adoptionDecayByCategory | merged.elasticityByCategory, merged.adoptionDecayByCategory |
| Enterprise Contracts | revenueQualityCoeff, expirationProfile | merged.revenueQualityCoeff, merged.expirationProfile |
| Regional Infra | regionalParams, avgCostPerMW, avgCoolingWater, avgGovCoordination | merged.regionalParams, merged.avgCostPerMW, merged.avgCoolingWaterAvailability, merged.avgGovCoordination |
| Onsite Capacity | onsiteGenCapacityMW, onsiteCapacityFactor, onsiteGenMix, onsiteFuelExposure, carbonIntensity, waterIntensity | merged.onsiteGenCapacityMW, merged.onsiteCapacityFactor, merged.onsiteGenMix, merged.onsiteFuelExposure, merged.carbonIntensityTonCO2perMWh, merged.waterIntensityLperMWh |
| Heat Rates | degradationByTechQuarterly | merged.degradationByTechQuarterly |
| Fuel Prices | fuelTermStructure, wholesaleAvgPrice | merged.fuelTermStructure, merged.wholesaleAvgPrice |
| Hedge Ratios | hedgeRatio | merged.hedgeRatio |
| Grid Services | gridServicesRevenue | merged.gridServicesRevenue |
| Black Swan | stressShocks | merged.stressShocks |

---

## FILES EXCLUDED (Derived/Output Only)

The following are **output/derived files** NOT used as simulation inputs:

| File | Reason |
|------|--------|
| `data_centers/*.py` | Processing scripts |
| `data_centers/*.md` | Documentation/reports |
| `data_centers/*_REPORT.md` | Analysis outputs |
| `data_centers/*_AUDIT.md` | Audit outputs |
| `data_centers/*_LINEAGE.csv` | Lineage tracking |
| `data_centers/*_UNCERTAINTY.csv` | Gap analysis |
| `data_centers/FACILITY_*.csv/md` | Phase 4 enriched outputs |
| `data_centers/MASTER_*.csv` | Aggregated outputs |
| `data_centers/HYPERSCALER_*.csv/md` | Rollup reports |
| `data_centers/module_*.csv` | Module-specific computed outputs |
| `data_centers/TESM_FULL_RESULTS.json` | Full simulation output |
| `data_centers/scenario_analysis.json` | Scenario outputs |
| `data_centers/dcf_valuations.json` | DCF outputs |
| `data_centers/analyze_macro_outlook.py` | Analysis script |
| `data_centers/phase4_deliverables.py` | Generation script |
| `data_centers/create_master_csv.py` | Compilation script |
| `data_centers/analyze_hyperscalers.py` | Analysis script |
| `data_centers/verify_*.py` | Verification scripts |
| `data_centers/generate_*.py` | Report generators |
| `data_centers/check_*.py` | Data quality checks |
| `*.py` (root) | Core engine/calibration scripts |
| `*.js` (root) | Engine/runtime |
| `*.html/*.css` | Dashboard UI |
| `*.md` (root) | Documentation |
| `param_overrides.js` | Auto-generated from calibrate.py |

---

## SUMMARY: CORE SIMULATION INPUT FILES

| Category | Files | Key Records | Primary Use |
|----------|-------|-------------|-------------|
| SEC DERA | 65 | 13 quarters × 6 hyperscalers | CapEx, RPO, Revenue trends |
| LBNL Queue | 1 | 10,000 projects | Grid delays, withdrawal rates |
| USITC Trade | 1 | Monthly imports | Silicon supply baseline |
| FRED Macro | 24 series | 1947-present | WACC, GDP, inflation, rates |
| China Benchmarks | 1 | 26 models | Elo gap, convergence |
| China API Pricing | 1 | 22 models | Price compression |
| Onsite Gen | 5 | 508 deployments | Capacity, tech mix, degradation |
| Productivity | 1 | 16 studies | Elasticity by category |
| Enterprise Contracts | 1 | 15 types | Revenue quality, expirations |
| Regional Infra | 1 | 14 regions | Power growth, costs, water |
| Black Swan | 1 | 53 shocks | Stress test params |
| Global DCs | 2 | 19,694 facilities | Market sizing |
| Hyperscale | 1 | 52 facilities | Detailed CapEx/GPU/PFLOPS |
| Tech Params | 1 | 6 technologies | Specs, costs, emissions |

**Total Raw Input Files: ~115** (including SEC quarterly folders)
**Total Calibrated Parameters: 60+**
**Simulation Modules: 33 integrated**