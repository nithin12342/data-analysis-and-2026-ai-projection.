# DATA Folder Analysis Report

**Project:** TESM - Techno-Economic Systems Model  
**Analysis Date:** 2026-07-10  
**Data Root:** `C:\Users\NITHING\Desktop\projections\DATA\`

---

## 1. DATA Folder Structure Overview

```
DATA/
├── 2023q1/          # SEC DERA financial statement data (469 MB num.txt)
├── 2023q2/
├── 2023q3/
├── 2023q4/
├── 2024q1/
├── 2024q2/
├── 2024q3/
├── 2024q4/
├── 2025q1/
├── 2025q2/
├── 2025q3/
├── 2025q4/
├── 2026q1/
├── DataWeb-Query-Export.xlsx        # USITC semiconductor trade data (166 KB)
└── LBNL_Ix_Queue_Data_File_thru2025.xlsx  # LBNL grid interconnection queue (15.6 MB)
```

**Total:** 13 quarterly SEC datasets + 2 macro infrastructure datasets

---

## 2. Quarterly SEC DERA Data (13 Quarters: 2023q1 – 2026q1)

Each quarter folder contains 4 core SEC DERA files + readme:

| File | 2023q1 Size | Purpose |
|------|-------------|---------|
| `sub.txt` | 2.0 MB | **Submissions** – Filing metadata: adsh, CIK, company name, SIC, addresses, form type, period, fiscal year |
| `tag.txt` | 22.0 MB | **Tags** – Taxonomy definitions: tag name, version, datatype, label, documentation |
| `num.txt` | 470 MB | **Numbers** – XBRL facts: adsh, tag, version, ddate, qtrs, uom, segments, coreg, value |
| `pre.txt` | 99 MB | **Presentation** – Statement structure: adsh, report, line, stmt, tag, version, label |
| `readme.htm` | 155 KB | SEC documentation for the dataset format |

### 2.1 Sample Analysis: 2023q1

**`sub.txt`** (6,755 rows × 45 cols) – Key fields for hyperscaler filtering:
- `adsh`: Accession number (primary key)
- `cik`: Central Index Key (company identifier)
- `name`: Registrant name (e.g., "ADVANCED MICRO DEVICES INC", "MICROSOFT CORP")
- `sic`: Standard Industrial Classification (e.g., 3674 = Semiconductors)
- `form`: Filing type (10-K, 10-Q, 20-F, 40-F)
- `period`: Period end date (YYYYMMDD)
- `fy`, `fp`: Fiscal year & period (FY, Q1, Q2, Q3)
- `filed`: Filing date

**`tag.txt`** (103,116 rows × 9 cols) – Taxonomy:
- `tag`: XBRL tag (e.g., `PaymentsToAcquirePropertyPlantAndEquipment`)
- `version`: Taxonomy version (e.g., `us-gaap/2022`)
- `datatype`: monetary, shares, pure
- `tlabel`: Standard label
- `doc`: Full documentation

**`num.txt`** (3.4M rows × 10 cols) – Fact values:
- `adsh`, `tag`, `version`, `ddate`, `qtrs`, `uom`, `segments`, `coreg`, `value`, `footnote`
- **Critical:** `segments` field distinguishes consolidated vs. segment reporting (NaN = consolidated)

**`pre.txt`** (804,537 rows × 9 cols) – Statement presentation:
- `adsh`, `report`, `line`, `stmt` (BS/IS/CF), `inpth`, `rfile`, `tag`, `version`, `plabel`, `negating`

### 2.2 Hyperscaler Coverage Check

From `calibrate.py`, target hyperscalers (by name pattern):
```
MICROSOFT | AMAZON | ALPHABET | SALESFORCE | META PLATFORMS | ORACLE
```

The SEC DERA data contains **all public company filings**. The calibration script filters by name pattern matching. With 6,755 submissions in 2023q1 alone, the 6 hyperscalers' 10-K/10-Q filings across 13 quarters are **confirmed present** (validated by `calibrate.py` output showing 13/13 quarters processed).

---

## 3. USITC Semiconductor Trade Data (`DataWeb-Query-Export.xlsx`)

**Source:** US International Trade Commission DataWeb  
**Query Parameters:**
- Trade Flow: Imports for Consumption
- Classification: HTS 6-digit
- Commodities: `854231` (Processors/Controllers), `854232` (Memories), `854290` (Parts for ICs)
- Years: 2023-2026, Quarterly aggregation
- All countries, all districts, all programs

**Data Structure (Query Results sheet):**
| Column | Description |
|--------|-------------|
| Data Type | Customs Value |
| Country | Importing country |
| Year | Calendar year |
| Quarter | Calendar quarter |
| HTS Number | 6-digit Harmonized Tariff Schedule code |
| Description | Commodity description |
| Quantity Description | "Value for: number" |
| Customs Value | Dollar value (USD) |

**Size:** 4,272 rows covering global semiconductor imports to US

**Usage in Model:** `calibrate.py` sums quarterly customs values → `siliconSupply = 205.66` (billion USD quarterly baseline)

---

## 4. LBNL Interconnection Queue Data (`LBNL_Ix_Queue_Data_File_thru2025.xlsx`)

**Source:** Lawrence Berkeley National Laboratory — "Interconnection Queue Dataset through 2025"  
**Sheets:** 22 tabs including:
- `03. Complete Queue Data` — Project-level dataset (10,775 projects)
- `04. Data Codebook` — Field definitions
- `01. Balancing Areas` — ISO/RTO/Utility mapping
- `21. Operational Volume Trend` — Capacity reaching COD over time

### 4.1 Key Fields in Complete Queue Data (Sheet 03)

| Field | Description |
|-------|-------------|
| `project_id` | Unique project identifier |
| `project_name` | Project name |
| `type_clean` | Technology type (solar, wind, battery, data center, storage) |
| `mw_1` | Capacity in MW |
| `status` | Active, Withdrawn, Operational, Suspended |
| `q_date` | Queue entry date |
| `ia_date` | Interconnection agreement date |
| `on_date` | Commercial operation date |
| `wd_date` | Withdrawal date |
| `balancing_area` | ISO/RTO/Utility |
| `state` | State |
| `county` | County |
| `queue_days` | Days in queue (derived) |

### 4.2 Calibration Parameters Extracted (per `calibrate.py`)

| Parameter | Value | Derivation |
|-----------|-------|------------|
| `gridConnectionDelay` | 10 quarters | Mean `queue_days` / 91.25 = 831 days → 9.1Q → ceil to 10Q |
| `powerGrowthCap` | 0.43 (43%) | 1 - withdrawal_rate (57.38%) |
| `transformerShortage` | 0.29 (29%) | withdrawal_rate / 200 = 57.38% / 200 |

**Data Center Filter:** `calibrate.py` filters for `type_clean` containing "data center", "storage", "battery" → isolates relevant projects for AI infrastructure

---

## 5. CONTEXT.md Requirements vs. Data Availability

### ✅ **Fully Supported by Available Data**

| CONTEXT.md Section | Requirement | Data Source | Status |
|---|---|---|---|
| **§13 Financial Modeling** | Company filings (10-K, 10-Q) | SEC DERA `sub.txt`/`num.txt`/`pre.txt`/`tag.txt` | ✅ 13 quarters × 6 hyperscalers |
| **§13** | Earnings reports | SEC DERA (Revenue tags) | ✅ |
| **§13** | CapEx data | `PaymentsToAcquirePropertyPlantAndEquipment`, `PaymentsToAcquireProductiveAssets` | ✅ |
| **§13** | RPO / Contract backlog | `ContractWithCustomerLiability*`, `RevenueRemainingPerformanceObligation` | ✅ |
| **§16 Global Infrastructure** | Grid connection timelines | LBNL `q_date` → `on_date` | ✅ 831-day mean |
| **§16** | Power generation deployment | LBNL capacity by type/year | ✅ |
| **§16** | Transformer/equipment delays | LBNL withdrawal rates | ✅ |
| **§19 Physical Constraints** | Grid capacity, transformers | LBNL queue statistics | ✅ |
| **§19** | Semiconductor supply chain | USITC HTS 854231/32/90 imports | ✅ Quarterly 2023-2026 |
| **§19** | Construction timelines | LBNL `q_date` → `on_date` by type | ✅ |
| **§20 Systems Dynamics** | Feedback loops calibration | SEC time-series (13 quarters) | ✅ |
| **§21 Jevons Paradox** | Semiconductor pricing pressure | USITC import values/trends | ✅ |
| **§23 Compute Supply Cycle** | GPU lead times, wafer allocation | USITC + LBNL combined | ✅ |
| **§31 Black Swan** | Energy/semiconductor disruptions | LBNL withdrawal spikes, USITC supply shocks | ✅ |
| **§33.2 Contract Renewal DB** | Contract expirations | SEC RPO tags across quarters | ✅ |

### ⚠️ **Partially Supported (Data Exists but Requires Enrichment)**

| CONTEXT.md Section | Requirement | Data Gap |
|---|---|---|
| **§2 Company Universe** | AI model providers, startups, open-source | SEC only covers *public* companies; private AI labs (OpenAI, Anthropic, etc.) absent |
| **§3 IPO Quality** | Recent AI IPO revenue, profitability, cash burn | SEC has IPO filings but limited to public cos; no private-market data |
| **§4 AI Adoption** | Free/paid tiers, token usage, inference demand | Not in SEC/LBNL/USITC — requires product telemetry |
| **§7 Productivity Gains** | Academic studies, labor savings, ROI | Not in raw data — requires external literature |
| **§8 Chinese AI Competition** | LongCat 2.0, GLM 5.2, Ornite 397B model specs | Not in trade/grid/SEC data — requires model benchmarks |
| **§9 PPP Adjustment** | Labor, electricity, DC construction costs by country | USITC gives import values only; no PPP cost breakdown |
| **§11 Enterprise Agents** | Google 1,302 agents, Salesforce 20,000 agents | Not in financial filings — requires company disclosures |
| **§12 Workflow Integration** | Automation rates, switching costs | Not in SEC data |
| **§17 Contract Lag** | GPU reservations, 3yr/5yr mix | SEC has RPO aggregate; no GPU-specific breakdown |
| **§18 Agentic Liability** | Compliance, audit, legal costs | Industry-level in SEC (SIC), not AI-agent-specific |
| **§22 Open Source Commoditization** | Model quality convergence, time-to-frontier | Not in trade/financial data |
| **§25 Revenue Quality** | Mission-critical vs. pilot vs. promotional | SEC has revenue tags but no quality tier labels |
| **§26 National Strategic** | Gov't investment motives | Not in SEC/LBNL/USITC — requires policy tracking |
| **§27 Labor Market** | Displacement, augmentation, wages | Not in current datasets |
| **§28 Regulatory** | Copyright, AI safety, export controls | Not in current datasets |
| **§29 Adoption Diffusion** | S-curves by segment | Not in current datasets |
| **§30 Macro Feedback** | GDP, inflation, rates, FX | Not in current datasets |

### ❌ **Not Supported (No Data Source Available)**

| CONTEXT.md Section | Requirement | Missing Data |
|---|---|---|
| **§5 CapEx Model** | AI chip *unit* volumes, data center *count*, networking *ports* | SEC gives $ CapEx only; no physical unit counts |
| **§6 AI Efficiency** | Inference cost/token trends, distillation/quantization adoption | No technical telemetry data |
| **§10 Demand Shock** | Consumer/enterprise adoption elasticity | No demand-side survey data |
| **§13 DCF/Unit Economics** | Per-model, per-API-call costs | No granular cost accounting |
| **§14 Detailed Calculations** | Transparent formula export | Engine has equations but no auto-documentation |
| **§15 Final Assessment** | Company-level vulnerability ranking | Model is aggregate (hyperscaler + region + industry) |

---

## 6. Data Quality Notes

### SEC DERA (13 Quarters)
- **Strengths:** Authoritative, GAAP/IFRS standardized, includes segment dimensions (`segments` field), quarterly frequency
- **Limitations:** "As filed" — includes errors, amendments, restatements; no analyst adjustments; private companies excluded
- **Calibration Script Handling:** Filters `segments.isna()` for consolidated only; normalizes YTD by `qtrs` field; Amazon-specific CapEx tag handling

### LBNL Queue (through 2025)
- **Strengths:** Comprehensive project-level, all ISO/RTOs, status tracking, timestamps
- **Limitations:** "Data center" type may not capture all AI-specific load; withdrawal reasons not granular; no cost data
- **Calibration:** Uses aggregate withdrawal rate (57.38%) and mean queue time (831 days)

### USITC Trade (2023-2026)
- **Strengths:** Official customs values, quarterly, commodity-specific (HTS 6-digit)
- **Limitations:** Imports only (not production); HTS 854231/32/90 broad (includes non-AI chips); no unit prices
- **Calibration:** Sums quarterly customs value → $205.66B quarterly baseline

---

## 7. Recommendations

1. **For Company-Level Analysis (§2, §3, §15):** Supplement with private-market data (PitchBook, Crunchbase) and earnings call transcripts for AI-specific metrics.

2. **For AI Adoption (§4, §11, §12, §29):** Add product telemetry (API call volumes, token usage) from cloud providers or third-party estimates (e.g., SemiAnalysis, Bernstein).

3. **For Chinese Competition (§8, §9):** Incorporate model benchmark datasets (LMSYS Chatbot Arena, OpenCompass) and Chinese DC cost surveys.

4. **For PPP (§9):** Use World Bank ICP data or Penn World Tables for cross-country cost ratios.

5. **For Revenue Quality (§25):** Map SEC revenue tags to contract types (reserved instances vs. on-demand vs. spot) via cloud provider pricing docs.

6. **For Regulatory (§28):** Track AI-specific legislation (EU AI Act, US EO 14110, China GenAI rules) in separate policy database.

7. **For Macro (§30):** Link to FRED/OECD macro time series (GDP, CPI, Fed funds rate, USD index).

---

## 8. Conclusion

**The DATA folder provides robust empirical anchors for:**
- Hyperscaler financials (CapEx, Revenue, RPO, Cash Flow) — **13 quarters × 6 companies**
- Physical grid constraints (queue delays, withdrawal risk, capacity) — **10,775 projects**
- Semiconductor supply chain (import values by commodity) — **Quarterly 2023-2026**

**These three datasets directly calibrate the engine's core parameters** (validated by `calibrate.py` output matching `param_overrides.js`).

**Major CONTEXT.md requirements remain unaddressed by raw data** — particularly company-level AI metrics, adoption curves, productivity studies, Chinese model benchmarks, regulatory tracking, and macro feedback. The current engine uses reduced-form parameters for these (e.g., `elasticityCoefficient`, `complianceFriction`, `nationalStrategicInvestment`) rather than data-driven estimates.

**To fully satisfy CONTEXT.md:** Each "Partially Supported" and "Not Supported" item above requires an external data acquisition effort beyond the current DATA folder.