# TESM Complete Numerical Results Report

**Generated**: July 9, 2026  
**Engine**: [engine.js](file:///c:/Users/NITHING/Desktop/projections/engine.js) | **Calibration**: [calibrate.py v3.0](file:///c:/Users/NITHING/Desktop/projections/calibrate.py) | **Overrides**: [param_overrides.js](file:///c:/Users/NITHING/Desktop/projections/param_overrides.js)  
**Data Sources**: 13 SEC DERA Quarters (2023q1-2026q1) · LBNL Interconnection Queue · USITC Semiconductor Trade Matrix  
**Hyperscalers Tracked**: Microsoft, Amazon, Alphabet, Salesforce, Meta Platforms, Oracle  
**Verification**: [97/97 tests passed](file:///C:/Users/NITHING/.gemini/antigravity/brain/d160859e-b61b-4e5d-b3e0-5d69f3cb8085/scratch/verify_engine.js)

---

## Input: Calculations Performed

### Data Ingestion
| # | Input Source | File | Records / Size |
|:--|:---|:---|:---|
| 1 | LBNL Grid Interconnection Queue | `DATA/LBNL_Ix_Queue_Data_File_thru2025.xlsx` | 10,775 grid projects, 15.2 MB |
| 2 | USITC Semiconductor Trade Matrix | `DATA/DataWeb-Query-Export.xlsx` | Customs import values, 162 KB |
| 3 | SEC DERA Quarters (13 directories) | `DATA/2023q1` to `2026q1` | `sub.txt` & `num.txt` per quarter |

### Calculations Executed
| # | Calculation | Script | Method / Description |
|:--|:---|:---|:---|
| 1 | **LBNL Grid Queue Extraction** | `calibrate.py` | Filters data centers, storage, and battery projects; calculates days from queue entry (`q_date`) to final status (`on_date`/`wd_date`/`ia_date`); calculates withdrawal rate. |
| 2 | **USITC Wafer Import Metric** | `calibrate.py` | Ingests and cleans Customs Value strings (removing commas/formatting errors) to establish quarterly silicon inflow baseline. |
| 3 | **SEC DERA Consolidated Fact Filtering** | `calibrate.py` | Identifies filers, matches reporting period (`ddate == period`), and **critically filters out dimensional segments (`segments.isna()`)** to extract pure consolidated balances. |
| 4 | **CapEx Flow Normalization** | `calibrate.py` | Extracts `PaymentsToAcquirePropertyPlantAndEquipment` (or `PaymentsToAcquireProductiveAssets` for Amazon) and **normalizes YTD cash flows to quarterly averages by dividing by `qtrs`**. |
| 5 | **RPO & Revenue Normalization** | `calibrate.py` | Sums current/noncurrent contract liabilities (instant facts, `qtrs=0`); normalizes revenues to quarterly flows using `qtrs` division. |
| 6 | **Downsizing Ratio Derivation** | `calibrate.py` | Evaluates overinvestment risk by scaling average CapEx to RPO ratio: `min(0.90, max(0.25, (meanCapEx / meanRPO) * 1.0))`. |
| 7 | **Capital Reflexivity Derivation** | `calibrate.py` | Evaluates sentiment feedback strength from average CapEx to Revenue ratio: `min(0.80, max(0.10, (meanCapEx / meanRevenue) * 1.5))`. |
| 8 | **Systems Dynamics Simulation** | `engine.js` | Runs Euler integration ODE solver over 80 quarterly steps for baseline and permutations. |
| 9 | **Scenario Matrix & Monte Carlo** | `engine.js` | Computes 32 scenario permutations and runs 100 perturbed trials to map out confidence intervals. |
| 10 | **Backtesting Optimization** | `engine.js` | Runs a grid-search parameter sweep on elasticity/compression/reflexivity, fitting against historical Dot-com and Japan index curves with OLS scale regression alignment. |

---

## 1. Calibrated Parameters (Empirically Derived)

| Parameter | Value | Description & Heuristic Formula |
|:---|:---:|:---|
| Grid Connection Delay | **10 Quarters** | LBNL Queue - 10,775 projects, 831 mean days |
| Power Growth Cap | **0.43** | LBNL - 57.38% withdrawal rate |
| Transformer Shortage | **0.29** | LBNL - withdrawal rate / 200 |
| Downsizing Ratio | **0.60** | SEC - CapEx/RPO overinvestment: `min(0.90, max(0.25, (CapEx/RPO) * 1.0))` |
| Capital Reflexivity | **0.26** | SEC - CapEx/Revenue sentiment feedback: `min(0.80, max(0.10, (CapEx/Rev) * 1.5))` |
| Silicon Supply | **$205.66B** | USITC - wafer customs trade value |
| WACC | **8.5%** | Institutional cost of capital benchmark |
| Contract Mix | **70% 3-yr / 30% 5-yr** | Industry baseline |

---

## 2. Baseline Simulation (20-Year Projection)

| Metric | Value |
|:---|:---:|
| **Final Market Index** | **117.04** |
| Peak Index | 117.04 |
| Min Index (Trough) | 49.14 |
| **Final Cloud Revenue** | **$25.47B** |
| **Final Enterprise ROI** | **33.3%** |
| Peak Enterprise ROI | 49.2% |
| **Final ROIC** | **13.8%** |
| **Peak Valuation Multiple (EV/Sales)** | **9.34x** |
| Final Valuation Multiple | 3.50x |
| **Peak Stranded Compute Fraction** | **58.6%** |
| Peak Stranded Capacity | 27.03 units |
| Final Compute Supply | 46.13 units |
| Final Active Power | 16.61 units |
| **Peak GDP Boost** | **2.73%** |

---

## 3. Milestone Trajectory

| Period | Index | Cloud Rev | ROI | ROIC | Stranded % | Multiple | GDP Boost |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Year 1 Q1** | 100.00 | $8.16B | 49.2% | 9.6% | 43.6% | 9.34x | 1.29% |
| **Year 1 Q4** | 87.95 | $8.62B | 46.0% | 9.8% | 46.3% | 7.77x | 1.28% |
| **Year 3 Q4** | 66.24 | $9.83B | 39.8% | 10.1% | 52.6% | 5.13x | 1.27% |
| **Year 5 Q4** | 50.93 | $11.08B | 36.1% | 10.5% | 52.7% | 3.50x | 1.29% |
| **Year 10 Q4** | 67.53 | $14.69B | 34.6% | 12.0% | 54.1% | 3.50x | 1.64% |
| **Year 15 Q4** | 89.18 | $19.40B | 34.0% | 13.0% | 56.7% | 3.50x | 2.13% |
| **Year 20 Q4** | 117.04 | $25.47B | 33.3% | 13.8% | 58.6% | 3.50x | 2.73% |

---

## 4. Scenario Matrix (32 Permutations)

### Distribution
*   **Stable Growth Scenarios (Index >= 100)**: **10** (31.2%)
*   **Deflationary Scenarios (50 <= Index < 100)**: **14** (43.8%)
*   **Severe Crash Scenarios (Index < 50)**: **8** (25.0%)

### Individual Scenario Perspectives (Final Year 20 Values)

| Scenario | Final Index | Cloud Rev | ROI | Peak Stranded |
|:---|:---:|:---:|:---:|:---:|
| **A** (Compliance Drag) | 52.65 | $11.45B | -0.9% | 21.30 |
| **B** (Price Compression) | 121.73 | $26.49B | 33.3% | 27.57 |
| **C** (Infrastructure Crunch) | 110.90 | $24.13B | 29.8% | 31.29 |
| **D** (Contract Downsizing) | 117.07 | $25.48B | 33.3% | 27.04 |
| **E** (Multiple Compression) | 98.82 | $25.47B | 33.3% | 27.03 |
| A+B | 50.50 | $10.98B | -1.0% | 20.91 |
| A+C | 53.32 | $11.60B | -0.6% | 23.84 |
| A+D | 52.48 | $11.42B | -0.9% | 21.29 |
| A+E | 42.06 | $11.45B | -0.9% | 21.30 |
| B+C | 115.03 | $25.03B | 29.9% | 31.99 |
| B+D | 121.75 | $26.50B | 33.3% | 27.58 |
| B+E | 102.78 | $26.49B | 33.3% | 27.57 |
| C+D | 110.90 | $24.14B | 29.8% | 31.30 |
| C+E | 93.12 | $24.13B | 29.8% | 31.29 |
| D+E | 98.84 | $25.48B | 33.3% | 27.04 |
| A+B+C | 50.75 | $11.04B | -0.8% | 23.23 |
| A+B+D | 50.29 | $10.94B | -1.1% | 20.90 |
| A+B+E | 40.33 | $10.98B | -1.0% | 20.91 |
| A+C+D | 53.16 | $11.57B | -0.6% | 23.84 |
| A+C+E | 42.62 | $11.60B | -0.6% | 23.84 |
| A+D+E | 41.93 | $11.42B | -0.9% | 21.29 |
| B+C+D | 115.04 | $25.04B | 29.9% | 32.01 |
| B+C+E | 96.60 | $25.03B | 29.9% | 31.99 |
| B+D+E | 102.81 | $26.50B | 33.3% | 27.58 |
| C+D+E | 93.13 | $24.14B | 29.8% | 31.30 |
| A+B+C+D | 50.55 | $11.00B | -0.8% | 23.22 |
| A+B+C+E | 40.55 | $11.04B | -0.8% | 23.23 |
| A+B+D+E | 40.17 | $10.94B | -1.1% | 20.90 |
| A+C+D+E | 42.49 | $11.57B | -0.6% | 23.84 |
| B+C+D+E | 96.61 | $25.04B | 29.9% | 32.01 |
| **Baseline** | 117.04 | $25.47B | 33.3% | 27.03 |
| A+B+C+D+E | 40.39 | $11.00B | -0.8% | 23.22 |

---

## 5. Regional Comparisons

| Region | Final Index | Cloud Rev | ROI | Peak Stranded % | GDP Boost |
|:---|:---:|:---:|:---:|:---:|:---:|
| **United States** | 117.04 | $25.47B | 33.3% | 58.6% | 2.73% |
| **China** | 116.78 | $25.41B | 33.3% | 58.0% | 1.50% |
| **India** | 116.89 | $25.43B | 33.3% | 58.2% | 1.23% |
| **Gulf Countries (UAE/KSA)** | 116.69 | $25.39B | 33.3% | 57.7% | 2.18% |
| **European Union** | 117.42 | $25.55B | 33.3% | 59.3% | 3.15% |

---

## 6. Industry Comparisons

| Industry | Final Index | Final ROI | Avg ROI (20yr) | Cloud Rev |
|:---|:---:|:---:|:---:|:---:|
| **Enterprise Software** | 117.04 | 33.3% | 36.1% | $25.47B |
| **Banking & Finance** | 39.92 | -11.4% | 3.1% | $8.68B |
| **Healthcare & Biotech** | 38.22 | -14.4% | 1.8% | $8.31B |
| **Legal Services** | 43.31 | -6.0% | 5.6% | $9.42B |

---

## 7. Monte Carlo Probability Distribution (100 Trials)

| Percentile | Final Index | Cloud Rev | ROIC |
|:---|:---:|:---:|:---:|
| **P10** (Downside) | 88.43 | $19.24B | 10.9% |
| **P50** (Median) | 111.37 | $24.23B | 13.3% |
| **P90** (Upside) | 577.15 | $72.39B | 21.7% |

> [!NOTE]
> **Monte Carlo Distribution Modeling Disclosure**: The upside skew (P90 = 577.15) is a direct consequence of the positive feedback loop in capital reflexivity (uncapped upside) combined with the structural valuation and sentiment floors on the downside. In real public markets, upside growth is bounded by physical supply chains, human capital shortages, and capital rationing, which are modeled here as a theoretical maximum.

---

## 8. Historical Bubble Calibration Fit (In-Sample Calibration)

> [!NOTE]
> The calibration metrics below represent **in-sample calibration fit** (optimization parameters derived via grid search to fit the model to historical curves), rather than out-of-sample prediction.

| Backtest | RMSE | Target | DA | Target | Status |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Dot-com Bubble** (NASDAQ 1997-2002) | 24.503 | < 25.0 | 87.0% | > 70% | **PASSED** |
| **Japan Asset Bubble** (Nikkei 1989-1995) | 6.277 | < 25.0 | 87.0% | > 70% | **PASSED** |

---

## 9. SEC Hyperscaler Time-Series (13 Quarters)

| Quarter | CapEx (Sum) | RPO/Deferred Rev | Revenue (Sum) |
|:---|:---:|:---:|:---:|
| 2023q1 | $40.38B | $83.33B | $301.34B |
| 2023q2 | $37.88B | $82.30B | $299.38B |
| 2023q3 | $36.33B | $98.21B | $315.02B |
| 2023q4 | $38.60B | $90.21B | $332.10B |
| 2024q1 | $39.43B | $94.24B | $338.28B |
| 2024q2 | $46.17B | $91.03B | $344.54B |
| 2024q3 | $51.08B | $108.10B | $355.70B |
| 2024q4 | $72.37B | $160.99B | $438.10B |
| 2025q1 | $63.21B | $100.95B | $381.36B |
| 2025q2 | $77.38B | $100.17B | $382.46B |
| 2025q3 | $91.54B | $122.55B | $407.24B |
| 2025q4 | $102.21B | $113.12B | $437.75B |
| 2026q1 | $116.32B | $115.40B | $439.03B |

| Trend Metric | Value |
|:---|:---:|
| **CapEx CAGR** (annualized) | **42.3%** |
| **RPO CAGR** (annualized) | **11.5%** |
| **CapEx/RPO Growth Gap** | **3.68x** |

> [!NOTE]
> **Accounting Disclosure on CapEx**: The quarterly CapEx sums parsed here are extracted from the Cash Flow Statement tag `PaymentsToAcquirePropertyPlantAndEquipment` (or `PaymentsToAcquireProductiveAssets` for Amazon). This cash-flow item represents cash outlays and excludes capital and finance-leased equipment. Since companies like Microsoft, Amazon, and Meta deploy significant server assets via finance leases, this cash metric runs below headline "CapEx guidance." Additionally, the data parser accounts for MSFT and ORCL non-calendar fiscal quarter ends by mapping individual filings dynamically to their respective balance sheet date.

---

## 10. Contract Expiration & Downsizing Loss (2026-2027)

### Contracts Expiring
| Year | 3-Year Contracts | 5-Year Contracts | **Total Expiring** |
|:---|:---:|:---:|:---:|
| **2026** | $247.8B | $63.7B | **$311.6B** |
| **2027** | $318.1B | $79.7B | **$397.7B** |
| **Combined** | $565.9B | $143.4B | **$709.3B** |

### Revenue Loss by Scenario
| Scenario | 2026 Loss | 2027 Loss | **Combined** |
|:---|:---:|:---:|:---:|
| Normal (4% churn) | $12.5B | $15.9B | **$28.4B** |
| Full Stress (60% downsize) | $186.9B | $238.6B | **$425.6B** |

---

## Output: Key Findings & Conclusions

### Finding 1: The $709.3 Billion Contract Cliff
Approximately **$709.3 Billion** in hyperscaler cloud contracts come up for renewal across 2026–2027. Under stress conditions (60% downsizing ratio derived from the CapEx/RPO overinvestment gap), the maximum revenue lost is **$425.6 Billion** over those 8 quarters.

### Finding 2: The 58.6% Stranded Compute Crisis
Due to the **10-quarter (2.5-year) grid connection delays** extracted from LBNL data and the 29% transformer shortage risk, **58.6%** of all built-out compute capacity will sit dark in data centers waiting for power at peak. This triggers massive write-downs on unamortized CapEx.

### Finding 3: The CapEx/RPO Divergence
Across 13 quarters of SEC data, hyperscaler CapEx is growing at **42.3% CAGR** while contract backlogs (RPO) grow at only **11.5%**. This **3.68x gap** is the quantitative signature of capital reflexivity - investor sentiment driving physical investment far ahead of committed revenue backlog.

### Finding 4: Industry Winners and Losers
Only Enterprise Software maintains positive 20-year ROI (**33.3%**). Banking (**-11.4%**), Healthcare (**-14.4%**), and Legal Services (**-6.0%**) all experience negative final ROIs due to high compliance friction and liability risk.

### Finding 5: Valuation Crashes under Stacked Scenarios
Across the 32 scenario permutations, **8 combinations (25.0%)** land in the "Severe Crash" zone below Index 50 (specifically, those stacking Scenario A compliance drag with Scenario E valuation multiple compression). The remaining **14 scenarios (43.8%)** result in deflationary compression (Index 50-100), and only **10 scenarios (31.2%)** maintain stable growth (Index >= 100). The worst-case combined scenario (A+B+C+D+E) ends at **Index 40.39**.

### Finding 6: Distinct Scenario Dynamics (D vs. E Resolved)
The actual engine results show distinct dynamics after resolving the markdown duplication issue:
*   **Scenario D (Contract Downsizing)**: Ends at **Index 117.07** (multiple floor of 3.5 is reached, but contract renewal patterns maintain recurring backlog).
*   **Scenario E (Multiple Compression)**: Ends at **Index 98.82** (reflecting a lower multiple floor of 2.0x EV/Sales, reducing final valuation).

### Finding 7: Monte Carlo Asymmetry
The Monte Carlo confidence intervals show strong upside skew (P10 = 88.43, P50 = 111.37, P90 = 577.15). This asymmetry is a direct consequence of the positive feedback loop in capital reflexivity (uncapped upside) combined with the structural valuation and sentiment floors on the downside.

---
*Report generated by TESM Engine v2.0 | Calibration Pipeline v3.0 | 97/97 verification tests passed*
