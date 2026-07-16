# Workspace Data Catalog and Structure Report

**Generated:** 2026-07-15 16:56:37
**Root Workspace Directory:** `C:/Users/NITHING/Desktop/projections`

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [CSV Files Analysis](#2-csv-files-analysis)
3. [Excel Files Analysis (Advanced Methodology)](#3-excel-files-analysis-advanced-methodology)
4. [JSON Datasets Analysis (Advanced Methodology)](#4-json-datasets-analysis-advanced-methodology)
5. [SEC DERA Text/TSV Datasets (Advanced Methodology)](#5-sec-dera-texttsv-datasets-advanced-methodology)

## 1. Executive Summary

- **Total CSV Files:** 70
- **Total Excel Files:** 2
- **Total JSON Files:** 5
- **Total SEC DERA Text Files:** 52
- **Total Data Catalog Size:** 7781.46 MB

---

## 2. CSV Files Analysis

### File: `DATA/New folder/adoption/vendor_reported_metrics.csv`

- **Size:** 2.31 KB
- **Total Rows:** 31
- **Total Columns:** 6
- **Category Columns:** vendor, source
- **Numeric Columns:** value, confidence
- **Date Columns:** date
- **Text Columns:** metric

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **vendor** | 6 | `anthropic`, `aws`, `google`, `meta`, `microsoft`, `openai` |
| **source** | 13 | `AWS ML blog`, `Analytics Insight`, `Anthropic disclosure`, `Anthropic pricing`, `Google Cloud ROI study`, `Google Cloud blog`, `Llama release blogs`, `MSFT FY24 Q4 earnings`, `MSFT earnings call`, `MSFT earnings calls`, `Reuters/Sensor Tower`, `Similarweb`, `re:Invent keynotes` |

#### Sample Data (First 3 rows)

| vendor | metric | date | value | source | confidence |
| --- | --- | --- | --- | --- | --- |
| openai | chatgpt_mau | 2026-06-02 | 1000000000 | Reuters/Sensor Tower | 0.9 |
| openai | chatgpt_plus_subscribers | 2024-10-15 | 11000000 | MSFT earnings call | 0.9 |
| anthropic | claude_ai_traffic_jan2026 | 2026-01-15 | 202900000 | Similarweb | 0.85 |

---

### File: `DATA/New folder/agents/deployment_counts.csv`

- **Size:** 2.67 KB
- **Total Rows:** 32
- **Total Columns:** 9
- **Category Columns:** agent_type, source
- **Numeric Columns:** agent_count, productivity_gain_pct, cost_savings_usd, roi_multiple
- **Date Columns:** deployment_date
- **Text Columns:** company, use_case

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **agent_type** | 11 | `ada_agents`, `agentforce`, `bedrock_agents`, `claude_enterprise`, `copilot`, `copilot_m365`, `decagon_agents`, `fin`, `gemini_enterprise`, `now_assist`, `sierra_agents` |
| **source** | 13 | `ada_case_study`, `anthropic_blog`, `aws_reinvent`, `decagon_blog`, `github_blog`, `google_cloud_next_2025`, `intercom_case_study`, `microsoft_customer_story`, `microsoft_earnings_q2_2025`, `salesforce_customer_story`, `salesforce_press_release`, `servicenow_press`, `sierra_blog` |

#### Sample Data (First 3 rows)

| company | deployment_date | agent_count | agent_type | use_case | productivity_gain_pct | cost_savings_usd | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google | 2025-01-15 | 1302 | gemini_enterprise | general_enterprise | 0 | 0 | ... |
| salesforce | 2025-10-13 | 20000 | agentforce | customer_service_sales | 0 | 0 | ... |
| microsoft | 2025-01-30 | 150000 | copilot_m365 | productivity_suite | 0 | 0 | ... |

---

### File: `DATA/New folder/china/api_pricing.csv`

- **Size:** 2.17 KB
- **Total Rows:** 31
- **Total Columns:** 8
- **Category Columns:** provider, source
- **Numeric Columns:** input_price_per_mtok, output_price_per_mtok, cached_input_price_per_mtok, context_window
- **Date Columns:** date
- **Text Columns:** model

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **provider** | 7 | `01.ai`, `alibaba`, `baichuan`, `bytedance`, `moonshot`, `tencent`, `zhipu-ai` |
| **source** | 8 | `AI_COST`, `ComputeUnion`, `cloud.tencent.com`, `dashscope.aliyuncs.com`, `platform.01.ai`, `toolcenter.ai`, `volcengine.com`, `z.ai pricing` |

#### Sample Data (First 3 rows)

| provider | model | input_price_per_mtok | output_price_per_mtok | cached_input_price_per_mtok | context_window | date | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| zhipu-ai | glm-5.2 | 1.0 | 3.2 | 0.2 | 1000000 | 2026-06-13 | ... |
| zhipu-ai | glm-5-turbo | 1.2 | 4.0 | 0.24 | 1000000 | 2026-06-13 | ... |
| zhipu-ai | glm-5-code | 1.2 | 5.0 | 0.3 | 1000000 | 2026-06-13 | ... |

---

### File: `DATA/New folder/china/model_benchmarks.csv`

- **Size:** 1.26 KB
- **Total Rows:** 16
- **Total Columns:** 9
- **Category Columns:** organization, benchmark, category, language
- **Numeric Columns:** elo, ci_low, ci_high
- **Date Columns:** date
- **Text Columns:** model

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **organization** | 11 | `01.ai`, `alibaba`, `baichuan`, `baidu`, `bytedance`, `deepseek`, `moonshot`, `shanghai-ai-lab`, `stepfun`, `tencent`, `zhipu-ai` |
| **benchmark** | 3 | `lmsys_chatbot_arena`, `mmbench`, `opencompass` |
| **category** | 3 | `chat`, `multimodal`, `reasoning` |
| **language** | 1 | `zh/en` |

#### Sample Data (First 3 rows)

| model | organization | benchmark | elo | ci_low | ci_high | date | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| glm-5.2 | zhipu-ai | lmsys_chatbot_arena | 1541.0 | 1506 | 1576 | 2026-03-02 | ... |
| glm-4.7 | zhipu-ai | lmsys_chatbot_arena | 1541.0 | 1506 | 1576 | 2026-03-02 | ... |
| deepseek-v4 | deepseek | lmsys_chatbot_arena | 1445.0 | 1410 | 1480 | 2026-06-01 | ... |

---

### File: `DATA/New folder/labor/onet_ai_exposure.csv`

- **Size:** 6.16 KB
- **Total Rows:** 55
- **Total Columns:** 17
- **Category Columns:** education_level
- **Numeric Columns:** ai_exposure_felten_2021, ai_exposure_felten_2023, language_modeling_exposure, image_generation_exposure, reasoning_exposure, automation_probability, augmentation_probability, displacement_risk, wage_2023, employment_2023, task_count, routine_task_pct, abstract_task_pct, manual_task_pct
- **Date Columns:** *None*
- **Text Columns:** occupation_code, occupation_title

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **education_level** | 6 | `associate`, `bachelor`, `doctorate`, `hs_diploma`, `less_hs`, `master` |

#### Sample Data (First 3 rows)

| occupation_code | occupation_title | ai_exposure_felten_2021 | ai_exposure_felten_2023 | language_modeling_exposure | image_generation_exposure | reasoning_exposure | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11-1011 | Chief Executives | 0.12 | 0.15 | 0.1 | 0.05 | 0.2 | ... |
| 11-3021 | Computer and Information Systems Mana... | 0.45 | 0.55 | 0.4 | 0.2 | 0.5 | ... |
| 13-1111 | Management Analysts | 0.6 | 0.7 | 0.65 | 0.15 | 0.6 | ... |

---

### File: `DATA/New folder/productivity/meta_analysis_studies.csv`

- **Size:** 1.98 KB
- **Total Rows:** 20
- **Total Columns:** 11
- **Category Columns:** category, model, doi
- **Numeric Columns:** n_sample, effect_size_pct, ci_low, ci_high, quality_score, publication_year
- **Date Columns:** *None*
- **Text Columns:** study, task_type

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **category** | 8 | `coding`, `consulting`, `customersupport`, `devops`, `legal`, `materials`, `pharma`, `writing` |
| **model** | 7 | `chatgpt`, `codex`, `github_copilot`, `gpt4`, `gpt_based`, `gpt_based_assistant`, `various` |
| **doi** | 11 | `10.1126/science.adh2586`, `10.48550/arXiv.2302.06590`, `Accenture Research`, `DORA Report`, `Microsoft Research`, `NBER.w31161`, `QJE.2024`, `SSRN`, `SSRN.4573321`, `SSRN.4945566`, `Stack Overflow` |

#### Sample Data (First 3 rows)

| study | category | task_type | model | n_sample | effect_size_pct | ci_low | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| peng_2023 | coding | http_server_implementation | github_copilot | 95 | 55.8 | 21.0 | ... |
| noy_zhang_2023 | writing | professional_writing_tasks | chatgpt | 444 | 37.0 | 28.0 | ... |
| dellacqua_2023 | consulting | complex_consulting_tasks | gpt4 | 758 | 12.0 | 8.0 | ... |

---

### File: `DATA/New folder/regulatory/jurisdiction_rule_matrix.csv`

- **Size:** 3.49 KB
- **Total Rows:** 20
- **Total Columns:** 12
- **Category Columns:** jurisdiction, status, cost_unit
- **Numeric Columns:** compliance_cost_low, compliance_cost_median, compliance_cost_high, enforcement_probability
- **Date Columns:** effective_date
- **Text Columns:** regulation, tier, requirements, source

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **jurisdiction** | 7 | `china`, `eu`, `india`, `ksa`, `uae`, `uk`, `us` |
| **status** | 3 | `active`, `banned`, `suspended` |
| **cost_unit** | 14 | `aed_per_model_per_year`, `cny_per_model_per_year`, `cny_per_org_per_year`, `eur_per_model_per_year`, `eur_per_system_per_year`, `eur_per_year`, `gbp_per_model_per_year`, `inr_per_org_per_year`, `sar_per_model_per_year`, `usd_per_case`, `usd_per_filing`, `usd_per_license`, `usd_per_model_per_year`, `usd_per_org_per_year` |

#### Sample Data (First 3 rows)

| jurisdiction | regulation | tier | status | effective_date | requirements | compliance_cost_low | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| eu | ai_act | high_risk | active | 2026-08-02 | conformity_assessment,risk_management... | 50000 | ... |
| eu | ai_act | gpai_systemic | active | 2025-08-02 | technical_documentation,transparency_... | 100000 | ... |
| eu | ai_act | gpai_standard | active | 2025-08-02 | technical_documentation,transparency_... | 25000 | ... |

---

### File: `DATA/New folder/revenue_quality/cloud_contract_mapping.csv`

- **Size:** 3.61 KB
- **Total Rows:** 33
- **Total Columns:** 15
- **Category Columns:** provider, quality_tier, upfront_option, capacity_reservation, typical_customer_segment, source
- **Numeric Columns:** price_discount_pct, commitment_term_years, flexibility_score, switching_cost_score, annual_churn_pct, expansion_rate_pct, nrr_pct
- **Date Columns:** date
- **Text Columns:** contract_type

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **provider** | 3 | `aws`, `azure`, `gcp` |
| **quality_tier** | 3 | `high`, `low`, `medium` |
| **upfront_option** | 9 | `auto`, `ea`, `license`, `marketplace`, `none`, `reserved`, `savings_plan`, `services`, `spend` |
| **capacity_reservation** | 2 | `none`, `yes` |
| **typical_customer_segment** | 6 | `batch/fault_tolerant`, `enterprise`, `established`, `growing`, `startups/small`, `steady` |
| **source** | 7 | `aws_ea`, `aws_marketplace`, `aws_pricing`, `aws_services`, `azure_ea`, `azure_pricing`, `gcp_pricing` |

#### Sample Data (First 3 rows)

| provider | contract_type | quality_tier | price_discount_pct | commitment_term_years | upfront_option | capacity_reservation | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aws | on_demand | low | 0 | 0 | none | none | ... |
| aws | savings_plan_1yr_no_upfront | medium | 27 | 1 | savings_plan | none | ... |
| aws | savings_plan_1yr_partial_upfront | medium | 37 | 1 | savings_plan | none | ... |

---

### File: `DATA/New folder/revenue_quality/saas_benchmarks.csv`

- **Size:** 1.33 KB
- **Total Rows:** 11
- **Total Columns:** 20
- **Category Columns:** arr_band, source
- **Numeric Columns:** arr_min, arr_max, nrr_median, nrr_p25, nrr_p75, grr_median, grr_p25, grr_p75, logo_churn_pct, expansion_rate_pct, gross_margin_pct, sm_magic_number, cac_payback_months, ltv_cac_ratio, rule_of_40_pct, net_dollar_retention_pct, sample_size, year
- **Date Columns:** *None*
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **arr_band** | 11 | `0_1M`, `100M_250M`, `10M_25M`, `1B_plus`, `1M_3M`, `250M_500M`, `25M_50M`, `3M_5M`, `500M_1B`, `50M_100M`, `5M_10M` |
| **source** | 1 | `saas_capital` |

#### Sample Data (First 3 rows)

| arr_band | arr_min | arr_max | nrr_median | nrr_p25 | nrr_p75 | grr_median | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0_1M | 0 | 1000000 | 110 | 105 | 120 | 95 | ... |
| 1M_3M | 1000000 | 3000000 | 112 | 107 | 122 | 96 | ... |
| 3M_5M | 3000000 | 5000000 | 114 | 109 | 124 | 97 | ... |

---

### File: `DATA/New folder/semiconductor/supply_chain_quarterly.csv`

- **Size:** 1.01 KB
- **Total Rows:** 13
- **Total Columns:** 12
- **Category Columns:** quarter
- **Numeric Columns:** tsmc_3nm_monthly_wafers, tsmc_4nm_5nm_monthly_wafers, tsmc_cowos_monthly_wafers, tsmc_cowos_l_pct, tsmc_cowos_s_pct, nvidia_h100_shipments, amd_mi300_shipments, hbm3e_monthly_units, coWos_capacity_kwpm, coWos_demand_kwpm, gap_pct
- **Date Columns:** *None*
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **quarter** | 13 | `2023Q4`, `2024Q1`, `2024Q2`, `2024Q3`, `2024Q4`, `2025Q1`, `2025Q2`, `2025Q3`, `2025Q4`, `2026Q1`, `2026Q2`, `2026Q3`, `2026Q4` |

#### Sample Data (First 3 rows)

| quarter | tsmc_3nm_monthly_wafers | tsmc_4nm_5nm_monthly_wafers | tsmc_cowos_monthly_wafers | tsmc_cowos_l_pct | tsmc_cowos_s_pct | nvidia_h100_shipments | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2023Q4 | 0 | 0 | 14000 | 0.3 | 0.7 | 500000 | ... |
| 2024Q1 | 0 | 0 | 15000 | 0.3 | 0.7 | 600000 | ... |
| 2024Q2 | 0 | 0 | 25000 | 0.4 | 0.6 | 800000 | ... |

---

### File: `DATA/New folder/stress_scenarios/historical_backtest.csv`

- **Size:** 1.76 KB
- **Total Rows:** 9
- **Total Columns:** 16
- **Category Columns:** episode, trigger, key_drivers, calibration_notes
- **Numeric Columns:** pre_crisis_valuation, post_crisis_valuation, peak_to_trough_pct, duration_months, recovery_months, model_predicted_trough, model_predicted_recovery, rmse, mae, directional_accuracy
- **Date Columns:** start_date, end_date
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **episode** | 9 | `cloud`, `dotcom`, `gfc`, `japan`, `railway`, `semi_2000`, `semi_2018`, `smartphone`, `telecom` |
| **trigger** | 9 | `asset_bubble`, `dotcom_crash`, `excessive_valuation`, `fiber_overbuild`, `gradual_adoption`, `housing_crisis`, `inventory_correction`, `mania`, `product_cycle` |
| **key_drivers** | 9 | `dotcom crash, inventory correction, demand collapse`, `excessive capex, demand overestimation, debt overhang`, `excessive valuation, revenue-less IPOs, Fed tightening`, `gradual adoption, enterprise migration, network effects`, `iPhone launch, app ecosystem, saturation`, `memory oversupply, trade tension, demand normalization`, `monetary tightening, demographic shift, zombie firms`, `speculative frenzy, overbuilding, regulatory crackdown`, `subprime mortgages, leverage, securitization` |
| **calibration_notes** | 9 | `S-curve adoption well captured`, `cyclical dynamics captured`, `good fit on duration; underestimated depth`, `good fit; credit channel well captured`, `limited data quality`, `long adoption curve well modeled`, `overestimated recovery speed`, `severity underestimated`, `structural factors not fully captured` |

#### Sample Data (First 3 rows)

| episode | start_date | end_date | trigger | pre_crisis_valuation | post_crisis_valuation | peak_to_trough_pct | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dotcom | 1999-03-01 | 2002-10-01 | excessive_valuation | 5000 | 1100 | -78 | ... |
| telecom | 1999-03-01 | 2002-10-01 | fiber_overbuild | 2000 | 300 | -85 | ... |
| japan | 1989-12-01 | 2003-03-01 | asset_bubble | 39000 | 7600 | -81 | ... |

---

### File: `DATA/New folder/stress_scenarios/scenario_matrix.csv`

- **Size:** 3.19 KB
- **Total Rows:** 27
- **Total Columns:** 10
- **Category Columns:** *None*
- **Numeric Columns:** probability, pA_agentic_tco, pB_ppp_pricing, pC_phys_infra, pD_contract_cliff, pE_val_multiple, horizon_years
- **Date Columns:** *None*
- **Text Columns:** scenario_name, description, key_assumptions

#### Sample Data (First 3 rows)

| scenario_name | description | probability | pA_agentic_tco | pB_ppp_pricing | pC_phys_infra | pD_contract_cliff | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| baseline | Baseline: all perspectives at median | 0.35 | 1.0 | 1.0 | 1.0 | 1.0 | ... |
| optimistic | Optimistic: favorable on all fronts | 0.1 | 0.8 | 0.8 | 0.8 | 0.8 | ... |
| pessimistic | Pessimistic: adverse on all fronts | 0.15 | 1.5 | 1.5 | 1.5 | 1.5 | ... |

---

### File: `DATA/New folder/stress_scenarios/stress_scenarios.csv`

- **Size:** 2.29 KB
- **Total Rows:** 20
- **Total Columns:** 16
- **Category Columns:** category
- **Numeric Columns:** probability_annual, gdp_shock_pct, unemployment_delta_pct, credit_spread_mult, equity_shock_pct, energy_shock_pct, semiconductor_shock_pct, regulation_shock, cyber_shock, ai_safety_shock, duration_quarters
- **Date Columns:** *None*
- **Text Columns:** scenario_id, scenario_name, correlation_structure, source

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **category** | 10 | `combined`, `cyber`, `energy`, `financial`, `geopolitical`, `health`, `macroeconomic`, `policy`, `supply_shock`, `technology` |

#### Sample Data (First 3 rows)

| scenario_id | scenario_name | category | probability_annual | gdp_shock_pct | unemployment_delta_pct | credit_spread_mult | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s1 | Global Recession | macroeconomic | 0.15 | -4.0 | 3.5 | 2.5 | ... |
| s2 | Energy Crisis | supply_shock | 0.05 | -2.0 | 1.5 | 1.8 | ... |
| s3 | Semiconductor Supply Disruption | supply_shock | 0.03 | -1.5 | 1.0 | 1.5 | ... |

---

### File: `DATA/New folder/unit_economics/gpu_economics.csv`

- **Size:** 1.85 KB
- **Total Rows:** 17
- **Total Columns:** 13
- **Category Columns:** provider, gpu_type, form_factor, source
- **Numeric Columns:** hourly_price_usd, annual_price_usd_1yr, annual_price_usd_3yr, memory_gb, memory_bandwidth_gbps, tflops_fp16, tflops_bf16, nvlink_gbps
- **Date Columns:** date
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **provider** | 7 | `aws`, `azure`, `coreweave`, `gcp`, `lambda`, `onprem`, `runpod` |
| **gpu_type** | 14 | `8x A100 80GB`, `8x H100`, `8x H100 SXM`, `ND96amsr_A100_v4 (8x A100 80GB)`, `ND96asr_v4 (8x A100)`, `a100_80gb_pcie`, `a100_80gb_sxm`, `a2-ultragpu-8g (8x A100)`, `a3-highgpu-8g (8x H100)`, `h100_80gb_pcie`, `h100_80gb_sxm`, `p4d.24xlarge (8x A100)`, `p4de.24xlarge (8x A100 80GB)`, `p5.48xlarge (8x H100)` |
| **form_factor** | 2 | `8x GPU server`, `GPU card` |
| **source** | 7 | `AWS pricing`, `Azure pricing`, `CoreWeave`, `GCP pricing`, `Lambda Labs`, `NVIDIA list price`, `RunPod` |

#### Sample Data (First 3 rows)

| provider | gpu_type | hourly_price_usd | annual_price_usd_1yr | annual_price_usd_3yr | memory_gb | memory_bandwidth_gbps | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aws | p5.48xlarge (8x H100) | 30.6 | 268056 | 718960 | 640 | 3350 | ... |
| aws | p4d.24xlarge (8x A100) | 32.77 | 287065 | 769500 | 640 | 1555 | ... |
| aws | p4de.24xlarge (8x A100 80GB) | 40.96 | 358810 | 961920 | 640 | 1555 | ... |

---

### File: `DATA/New folder/unit_economics/inference_costs.csv`

- **Size:** 2.87 KB
- **Total Rows:** 25
- **Total Columns:** 16
- **Category Columns:** provider, hardware, source
- **Numeric Columns:** input_price_per_1m_tokens, output_price_per_1m_tokens, cached_input_price_per_1m_tokens, context_window_tokens, max_output_tokens, throughput_tokens_per_sec, avg_latency_ms, utilization_pct, hw_cost_per_hour, effective_input_per_1m, effective_output_per_1m
- **Date Columns:** date
- **Text Columns:** model

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **provider** | 10 | ` mistral`, `01.ai`, `alibaba`, `anthropic`, `deepseek`, `google`, `meta`, `moonshot`, `openai`, `zhipu` |
| **hardware** | 3 | `h100`, `h800`, `tpu_v5` |
| **source** | 10 | `alibaba_pricing`, `anthropic_pricing`, `deepseek_pricing`, `google_pricing`, `meta_blog`, `mistral_pricing`, `moonshot_pricing`, `openai_pricing`, `yi_pricing`, `zhipu_pricing` |

#### Sample Data (First 3 rows)

| model | provider | input_price_per_1m_tokens | output_price_per_1m_tokens | cached_input_price_per_1m_tokens | context_window_tokens | max_output_tokens | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| gpt-4o | openai | 5.0 | 15.0 | 2.5 | 128000 | 4096 | ... |
| gpt-4o-mini | openai | 0.15 | 0.6 | 0.075 | 128000 | 16384 | ... |
| gpt-4-turbo | openai | 10.0 | 30.0 | 5.0 | 128000 | 4096 | ... |

---

### File: `DATA/New folder/unit_economics/saas_benchmarks.csv`

- **Size:** 0.92 KB
- **Total Rows:** 9
- **Total Columns:** 15
- **Category Columns:** arr_band
- **Numeric Columns:** arr_midpoint_usd, n_companies, nrr_median, grr_median, expansion_rate_median, logo_churn_median, gross_margin_median, sales_marketing_pct_rd, rd_pct_revenue, cac_months_median, ltv_cac_median, rule_of_40_median, net_income_margin_median, free_cash_flow_margin_median
- **Date Columns:** *None*
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **arr_band** | 9 | `1-5M`, `10-25M`, `100-250M`, `1B+`, `25-50M`, `250-500M`, `5-10M`, `50-100M`, `500M-1B` |

#### Sample Data (First 3 rows)

| arr_band | arr_midpoint_usd | n_companies | nrr_median | grr_median | expansion_rate_median | logo_churn_median | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1-5M | 3000000 | 150 | 1.12 | 0.92 | 0.18 | 0.12 | ... |
| 5-10M | 7500000 | 85 | 1.15 | 0.94 | 0.22 | 0.1 | ... |
| 10-25M | 17500000 | 60 | 1.18 | 0.95 | 0.25 | 0.08 | ... |

---

### File: `DATA/New folder/unit_economics/training_costs.csv`

- **Size:** 2.60 KB
- **Total Rows:** 23
- **Total Columns:** 13
- **Category Columns:** organization, gpu_type, source
- **Numeric Columns:** parameters_b, compute_flops, compute_cost_usd, training_tokens, training_time_days, gpu_count, training_cost_per_token, training_cost_per_flop
- **Date Columns:** release_date
- **Text Columns:** model

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **organization** | 10 | `01.ai`, `alibaba`, `anthropic`, `deepseek`, `google`, `meta`, `mistral`, `nvidia`, `openai`, `zhipu` |
| **gpu_type** | 3 | `a100_80gb`, `h100`, `tpu_v5` |
| **source** | 12 | `anthropic_blog`, `deepseek_blog`, `epoch_ai/semi_analysis`, `google_blog`, `meta_blog`, `mistral_blog`, `nvidia_blog`, `openai_blog`, `qwen_blog`, `semi_analysis`, `yi_blog`, `zhipu_blog` |

#### Sample Data (First 3 rows)

| model | organization | release_date | parameters_b | compute_flops | compute_cost_usd | training_tokens | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| gpt-4 | openai | 2023-03-14 | 1760 | 2.15e+25 | 63000000 | 13000000000000 | ... |
| gpt-4-turbo | openai | 2023-11-06 | 1760 | 2.15e+25 | 50000000 | 13000000000000 | ... |
| gpt-4o | openai | 2024-05-13 | 1760 | 2.15e+25 | 40000000 | 13000000000000 | ... |

---

### File: `DATA/calibration_parameters.csv`

- **Size:** 4.24 KB
- **Total Rows:** 27
- **Total Columns:** 7
- **Category Columns:** unit, source_data_files
- **Numeric Columns:** calibrated_value, confidence
- **Date Columns:** *None*
- **Text Columns:** parameter_name, derivation_method, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **unit** | 13 | `L_per_MWh`, `MW`, `USD_billions_per_quarter`, `USD_per_MW_yr`, `USD_per_MWh_per_50USD_ton`, `USD_per_MWh_per_USD_per_MMBtu`, `fraction`, `multiplier`, `per_quarter`, `per_year`, `quarters`, `ton_CO2_per_MWh`, `x` |
| **source_data_files** | 15 | `carbon_prices.csv`, `enterprise_contracts.csv`, `grid_connection_delays.csv`, `grid_services_revenue.csv`, `hedge_ratios.csv`, `macro_data.csv`, `onsite_gen_capacity.csv`, `productivity_meta_analysis.csv`, `real_historical_trails.csv`, `sec_financials.csv`, `technology_parameters.csv`, `technology_parameters.csv + heat_rates.csv`, `technology_parameters.csv + onsite_gen_capacity.csv`, `transformer_shortage.csv`, `usitc_data.csv` |

#### Sample Data (First 3 rows)

| parameter_name | calibrated_value | unit | derivation_method | source_data_files | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- |
| gridConnectionDelay | 10.0 | quarters | LBNL Queued Up 2025 median IR-to-COD ... | grid_connection_delays.csv | 0.85 | Ceiling of mean queue quarters across... |
| powerGrowthCap | 0.12 | per_year | 1 - (withdrawal_rate/100) from LBNL 2... | grid_connection_delays.csv | 0.8 | US completion rate ~13% → cap ~12%/yr |
| transformerShortage | 0.29 | fraction | NIAC 2024: 120 weeks lead time vs 50 ... | transformer_shortage.csv | 0.75 | Severity index 0-1 |

---

### File: `DATA/carbon_prices.csv`

- **Size:** 2.77 KB
- **Total Rows:** 16
- **Total Columns:** 9
- **Category Columns:** jurisdiction, program, local_currency, date, source, source_url
- **Numeric Columns:** carbon_price_usd_per_ton, price_local_currency
- **Date Columns:** *None*
- **Text Columns:** notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **jurisdiction** | 10 | `california`, `canada`, `china`, `eu`, `korea`, `new_zealand`, `quebec`, `rggi`, `uk`, `washington` |
| **program** | 9 | `cap_and_trade`, `cca`, `eu_ets`, `federal_fuel_charge`, `k_ets`, `national_ets`, `nz_ets`, `rggi`, `uk_ets` |
| **local_currency** | 7 | `CAD`, `CNY`, `EUR`, `GBP`, `KRW`, `NZD`, `USD` |
| **date** | 8 | `2023`, `2024`, `2024-01`, `2024-03`, `2024-05`, `2024-06`, `2024-11`, `2025-06` |
| **source** | 12 | `CARB Auction Results`, `CARB Joint Auction`, `China Carbon Market`, `ESMA Carbon Markets Report 2025`, `Environment Canada`, `Korea Exchange`, `NZ ETS`, `RGGI Annual Report 2024`, `RGGI Auction 63`, `RGGI Auction 64`, `UK ETS Authority`, `WA Ecology` |
| **source_url** | 13 | `https://ecology.wa.gov/`, `https://ww2.arb.ca.gov/`, `https://ww2.arb.ca.gov/news/california-and-quebec-release-summary-results-40th-joint-cap-and-trade-allowance-auction`, `https://ww2.arb.ca.gov/sites/default/files/2024-02/nc-feb_2024_summary_results_report.pdf`, `https://www.canada.ca/en/environment-climate-change.html`, `https://www.epa.govt.nz/`, `https://www.esma.europa.eu/sites/default/files/2025-10/ESMA50-481369926-30552_Carbon_Markets_Report_2025.pdf`, `https://www.gov.uk/government/organisations/uk-emissions-trading-scheme-authority`, `https://www.krx.co.kr/`, `https://www.mee.gov.cn/`, `https://www.rggi.org/sites/default/files/Uploads/Auction-Materials/63/Auction_63_Market_Monitor_Report.pdf`, `https://www.rggi.org/sites/default/files/Uploads/Auction-Materials/64/PR060724_Auction64.pdf`, `https://www.rggi.org/sites/default/files/Uploads/Market-Monitor/Annual-Reports/MM_2024_Annual_Report.pdf` |

#### Sample Data (First 3 rows)

| jurisdiction | program | carbon_price_usd_per_ton | price_local_currency | local_currency | date | source | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| eu | eu_ets | 70 | 65 | EUR | 2024 | ESMA Carbon Markets Report 2025 | ... |
| eu | eu_ets | 82 | 77 | EUR | 2023 | ESMA Carbon Markets Report 2025 | ... |
| eu | eu_ets | 84 | 79 | EUR | 2025-06 | ESMA Carbon Markets Report 2025 | ... |

---

### File: `DATA/china_api_pricing.csv`

- **Size:** 2.13 KB
- **Total Rows:** 22
- **Total Columns:** 9
- **Category Columns:** provider, currency, date, source, source_url, notes
- **Numeric Columns:** input_price_usd_per_million_tokens, output_price_usd_per_million_tokens
- **Date Columns:** *None*
- **Text Columns:** model

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **provider** | 12 | `alibaba`, `anthropic`, `baichuan`, `bytedance`, `deepseek`, `google`, `minimax`, `moonshot`, `openai`, `tencent`, `zero_one_ai`, `zhipu_ai` |
| **currency** | 1 | `USD` |
| **date** | 1 | `2024-11` |
| **source** | 12 | `01.ai Platform`, `Alibaba Cloud DashScope`, `Anthropic API`, `Baichuan Platform`, `DeepSeek Platform`, `Google AI Studio`, `Minimax Platform`, `Moonshot Platform`, `OpenAI API`, `Tencent Cloud`, `VolcEngine`, `Zhipu AI Platform` |
| **source_url** | 12 | `https://ai.google.dev/pricing`, `https://api.minimax.chat/`, `https://cloud.tencent.com/`, `https://dashscope.aliyuncs.com/`, `https://docs.anthropic.com/claude/reference/pricing`, `https://open.bigmodel.cn/`, `https://platform.01.ai/`, `https://platform.baichuan-ai.com/`, `https://platform.deepseek.com/`, `https://platform.moonshot.cn/`, `https://platform.openai.com/docs/pricing`, `https://www.volcengine.com/` |
| **notes** | 3 | `Input $0.14, Output $0.28`, `Lite version`, `~1 RMB/M tokens input/output` |

#### Sample Data (First 3 rows)

| provider | model | input_price_usd_per_million_tokens | output_price_usd_per_million_tokens | currency | date | source | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| zhipu_ai | glm_4 | 0.14 | 0.14 | USD | 2024-11 | Zhipu AI Platform | ... |
| zhipu_ai | glm_4v | 0.28 | 0.28 | USD | 2024-11 | Zhipu AI Platform | ... |
| zhipu_ai | glm_4_air | 0.07 | 0.07 | USD | 2024-11 | Zhipu AI Platform | ... |

---

### File: `DATA/china_benchmarks.csv`

- **Size:** 3.01 KB
- **Total Rows:** 26
- **Total Columns:** 11
- **Category Columns:** organization, benchmark, date, language, model_type, parameters_b, source, source_url, notes
- **Numeric Columns:** score
- **Date Columns:** *None*
- **Text Columns:** model

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **organization** | 12 | `alibaba`, `anthropic`, `baichuan`, `deepseek`, `google`, `meta`, `minimax`, `moonshot`, `nvidia`, `openai`, `zero_one_ai`, `zhipu_ai` |
| **benchmark** | 1 | `lmsys_chatbot_arena` |
| **date** | 10 | `2024-01`, `2024-03`, `2024-04`, `2024-05`, `2024-06`, `2024-07`, `2024-08`, `2024-09`, `2024-10`, `2024-11` |
| **language** | 2 | `en`, `zh/en` |
| **model_type** | 3 | `multimodal`, `open_weight`, `proprietary` |
| **parameters_b** | 11 | `1.5`, `14`, `3`, `32`, `34`, `405`, `6`, `7`, `70`, `72`, `?` |
| **source** | 12 | `01.ai / LMSYS`, `Alibaba / LMSYS`, `Anthropic / LMSYS`, `Baichuan / LMSYS`, `DeepSeek / LMSYS`, `Google / LMSYS`, `Meta / LMSYS`, `MiniMax / LMSYS`, `Moonshot AI / LMSYS`, `NVIDIA / LMSYS`, `OpenAI / LMSYS`, `Zhipu AI / LMSYS` |
| **source_url** | 1 | `https://chat.lmsys.org/` |
| **notes** | 2 | `GLM-5.2 release`, `Qwen2.5 release` |

#### Sample Data (First 3 rows)

| model | organization | benchmark | score | date | language | model_type | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| glm_5_2 | zhipu_ai | lmsys_chatbot_arena | 1247 | 2024-11 | zh/en | proprietary | ... |
| glm_4 | zhipu_ai | lmsys_chatbot_arena | 1198 | 2024-06 | zh/en | proprietary | ... |
| glm_4v | zhipu_ai | lmsys_chatbot_arena | 1156 | 2024-08 | zh/en | multimodal | ... |

---

### File: `DATA/enterprise_contracts.csv`

- **Size:** 2.28 KB
- **Total Rows:** 15
- **Total Columns:** 12
- **Category Columns:** company, contract_type, source, source_url, notes
- **Numeric Columns:** avg_contract_length_years, renewal_rate_pct, downsizing_pct_at_renewal, expansion_pct_at_renewal, net_revenue_retention_pct, gross_revenue_retention_pct, year
- **Date Columns:** *None*
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **company** | 9 | `aws`, `azure`, `databricks`, `gcp`, `meta`, `oracle`, `salesforce`, `servicenow`, `snowflake` |
| **contract_type** | 6 | `committed_use_discounts`, `enterprise_agreement`, `enterprise_saas`, `reserved_instances`, `savings_plans`, `universal_credits` |
| **source** | 12 | `AWS 10-K / Analyst`, `AWS 10-K / Analyst Reports`, `AWS 10-K / Flexera State of Cloud`, `Alphabet 10-K / Analyst`, `Databricks S-1 / Analyst`, `Meta 10-K / Analyst`, `Microsoft 10-K / Analyst`, `Microsoft 10-K / Flexera`, `Oracle 10-K / Analyst`, `Salesforce 10-K / ICONIQ`, `ServiceNow 10-K / KeyBanc`, `Snowflake 10-K / ICONIQ` |
| **source_url** | 7 | `https://info.flexera.com/CM-REPORT-State-of-the-Cloud`, `https://www.sec.gov/`, `https://www.sec.gov/Archives/edgar/data/1018724/000101872424000023/amzn-20231231.htm`, `https://www.sec.gov/Archives/edgar/data/1326801/000132680124000023/meta-20231231.htm`, `https://www.sec.gov/Archives/edgar/data/1341439/000134143924000023/orcl-20231231.htm`, `https://www.sec.gov/Archives/edgar/data/1652044/000165204424000022/goog-20231231.htm`, `https://www.sec.gov/Archives/edgar/data/789019/000078901924000023/msft-20240630.htm` |
| **notes** | 11 | `5yr CUD higher retention`, `Azure consumption commit`, `CRM NRR best-in-class`, `Consumption-based; high expansion`, `Data/AI platform expansion`, `EA typically 3-5yr; NRR ~115%`, `GCP committed use`, `ITSM platform stickiness`, `Internal + external cloud`, `RI 3yr no upfront`, `UC model` |

#### Sample Data (First 3 rows)

| company | contract_type | avg_contract_length_years | renewal_rate_pct | downsizing_pct_at_renewal | expansion_pct_at_renewal | net_revenue_retention_pct | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aws | enterprise_agreement | 3 | 95 | 15 | 25 | 115 | ... |
| aws | reserved_instances | 3 | 90 | 20 | 10 | 105 | ... |
| aws | savings_plans | 3 | 92 | 18 | 15 | 110 | ... |

---

### File: `DATA/fuel_prices.csv`

- **Size:** 2.61 KB
- **Total Rows:** 19
- **Total Columns:** 8
- **Category Columns:** fuel_type, region, source_url
- **Numeric Columns:** price_usd_per_mmbtu, price_usd_per_kg, date
- **Date Columns:** *None*
- **Text Columns:** source, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **fuel_type** | 4 | `biogas`, `diesel`, `hydrogen`, `natural_gas` |
| **region** | 13 | `blue_smr_ccs_us`, `california_lcfs`, `delivered_blue_us`, `delivered_green_us`, `gray_smr_us`, `green_pem_us`, `henry_hub`, `jkm_asia`, `pg_e_citygate`, `ttf_europe`, `us_average`, `us_gulf_coast`, `waha_tx` |
| **source_url** | 12 | `https://fred.stlouisfed.org/series/AHHNGSP`, `https://ww2.arb.ca.gov/`, `https://www.eia.gov/`, `https://www.eia.gov/dnav/ng/ng_pri_sum_dcu_nus_m.htm`, `https://www.eia.gov/dnav/pet/pet_pri_gnd_dcus_nus_w.htm`, `https://www.eia.gov/outlooks/steo/`, `https://www.eia.gov/todayinenergy/detail.php?id=64184`, `https://www.energy.gov/`, `https://www.epa.gov/agstar`, `https://www.hydrogen.energy.gov/`, `https://www.hydrogen.energy.gov/docs/hydrogenprogramlibraries/pdfs/24005-clean-hydrogen-production-cost-pem-electrolyzer.pdf`, `https://www.ice.com/` |

#### Sample Data (First 3 rows)

| fuel_type | region | price_usd_per_mmbtu | price_usd_per_kg | source | source_url | date | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| natural_gas | henry_hub | 2.21 | nan | EIA Annual Average 2024 | https://www.eia.gov/todayinenergy/det... | 2024 | ... |
| natural_gas | henry_hub | 3.52 | nan | EIA/FRED 2025 Average | https://fred.stlouisfed.org/series/AH... | 2025 | ... |
| natural_gas | henry_hub | 4.5 | nan | EIA STEO Forecast 2026 | https://www.eia.gov/outlooks/steo/ | 2026 | ... |

---

### File: `DATA/grid_connection_delays.csv`

- **Size:** 4.11 KB
- **Total Rows:** 33
- **Total Columns:** 13
- **Category Columns:** region, iso, project_type, source, source_url, notes
- **Numeric Columns:** median_ir_to_cod_months, median_ia_to_cod_months, withdrawal_rate_pct, completion_rate_pct, total_active_gw, total_withdrawn_gw, date
- **Date Columns:** *None*
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **region** | 1 | `us` |
| **iso** | 7 | `caiso`, `ercot`, `miso`, `non_iso`, `nyiso`, `pjm`, `spp` |
| **project_type** | 5 | `battery`, `data_center`, `natural_gas`, `solar`, `wind` |
| **source** | 2 | `LBNL Queued Up 2025`, `LBNL Queued Up 2025 / Industry` |
| **source_url** | 1 | `https://emp.lbl.gov/publications/queued-2025-edition` |
| **notes** | 7 | `CAISO solar projects 2018-2024`, `ERCOT fastest queue`, `Estimated for large loads`, `Gas +72% YoY 2024`, `Gas projects faster`, `PJM reform transition`, `Southeast/West non-ISO` |

#### Sample Data (First 3 rows)

| region | iso | project_type | median_ir_to_cod_months | median_ia_to_cod_months | withdrawal_rate_pct | completion_rate_pct | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| us | caiso | solar | 72 | 50 | 75 | 14 | ... |
| us | caiso | wind | 60 | 45 | 70 | 15 | ... |
| us | caiso | battery | 48 | 36 | 65 | 18 | ... |

---

### File: `DATA/grid_services_revenue.csv`

- **Size:** 4.40 KB
- **Total Rows:** 28
- **Total Columns:** 8
- **Category Columns:** iso, service, date, source, source_url, notes
- **Numeric Columns:** price_usd_per_mw_yr, volume_mw
- **Date Columns:** *None*
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **iso** | 7 | `caiso`, `ercot`, `iso_ne`, `miso`, `nyiso`, `pjm`, `spp` |
| **service** | 13 | `capacity`, `capacity_2024_25`, `capacity_2025_26`, `day_ahead_scheduling_reserve`, `ecrs`, `non_spinning_reserve`, `regulation`, `regulation_down`, `regulation_up`, `responsive_reserve`, `spinning_reserve`, `supplemental_reserve`, `synchronous_reserve` |
| **date** | 4 | `2023-07`, `2024-01`, `2024-06`, `2024-07` |
| **source** | 11 | `CAISO Monthly Market Performance`, `ERCOT Monthly Report`, `ISO-NE FCA`, `ISO-NE Markets`, `MISO State of the Market 2024`, `NYISO ICAP Market`, `NYISO Market Data`, `PJM 2024/25 BRA Report`, `PJM 2025/26 BRA Report`, `PJM State of the Market 2024`, `SPP Marketplace` |
| **source_url** | 10 | `https://www.caiso.com/content/monthly-market-performance/jan-2024/ancillary-services-1.html`, `https://www.caiso.com/content/monthly-market-performance/jun-2024/ancillary-services.html`, `https://www.iso-ne.com/markets-operations/markets`, `https://www.monitoringanalytics.com/reports/Reports/2024/IMM_2024_State_of_the_Market_Report_for_PJM.pdf`, `https://www.nyiso.com/market-data`, `https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2024-2025/2024-2025-base-residual-auction-report.ashx`, `https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2025-2026/2025-2026-base-residual-auction-report.pdf`, `https://www.potomaceconomics.com/wp-content/uploads/2025/01/2024-12_Nodal_Monthly_Report.pdf`, `https://www.potomaceconomics.com/wp-content/uploads/2025/06/2024-MISO-SOM_Report_Body_Final.pdf`, `https://www.spp.org/marketplace/` |
| **notes** | 13 | `$269.92/MW-day * 365 = $98,520/MW-yr RTO`, `$28.92/MW-day * 365`, `Ancillary services $0.13/MWh all-in`, `Capacity market`, `ERCOT Contingency Reserve Service`, `Forward Capacity Auction`, `IFM average price`, `June 2024 average`, `Potomac Economics`, `RRS (spinning)`, `Regulation`, `Regulation market`, `Regulation movement` |

#### Sample Data (First 3 rows)

| iso | service | price_usd_per_mw_yr | volume_mw | date | source | source_url | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| caiso | regulation_up | 45000 | 1200 | 2024-01 | CAISO Monthly Market Performance | https://www.caiso.com/content/monthly... | ... |
| caiso | regulation_down | 38000 | 1100 | 2024-01 | CAISO Monthly Market Performance | https://www.caiso.com/content/monthly... | ... |
| caiso | spinning_reserve | 25000 | 800 | 2024-01 | CAISO Monthly Market Performance | https://www.caiso.com/content/monthly... | ... |

---

### File: `DATA/heat_rates.csv`

- **Size:** 3.40 KB
- **Total Rows:** 16
- **Total Columns:** 11
- **Category Columns:** unit, technology, fuel_type, date, source, source_url, notes
- **Numeric Columns:** heat_rate_btu_per_kwh_hhv, heat_rate_btu_per_kwh_lhv, electrical_efficiency_lhv_pct, degradation_pct_per_year
- **Date Columns:** *None*
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **unit** | 8 | `ballard_fc`, `bloom_es5`, `caterpillar_fc`, `ge_7ha`, `mitsubishi_m501jac`, `plug_power_gen`, `siemens_hl`, `wartsila_18v50` |
| **technology** | 5 | `gas_turbine`, `hydrogen`, `rice`, `sofc`, `solid_oxide` |
| **fuel_type** | 2 | `hydrogen`, `natural_gas` |
| **date** | 5 | `2024-01`, `2025-01`, `2026-01`, `2027-01`, `2028-01` |
| **source** | 8 | `Ballard Fuel Cells / DOE`, `Bloom Energy ES6.5 Datasheet`, `Caterpillar / DOE`, `GE Vernova 7HA.03 Specs`, `MHI M501JAC Specs`, `Plug Power GenSure / DOE H2A`, `Siemens Energy HL-Class`, `Wärtsilä 50SG Datasheet` |
| **source_url** | 8 | `https://assets.siemens-energy.com/dam/6a81abd9-6c46-42c9-9034-b036013f322b/210923-HL-ClassFactSheet-05-pdf_Original%20file.pdf`, `https://power.mhi.com/products/gasturbines/lineup/m501j/`, `https://www.ballard.com/`, `https://www.bloomenergy.com/wp-content/uploads/bloom-energy-server-datasheet-feb-2026.pdf`, `https://www.cat.com/`, `https://www.gevernova.com/content/dam/gepower-new/global/en_US/downloads/gas-new-site/products/gas-turbines/7ha.03-takeaway.pdf`, `https://www.plugpower.com/wp-content/uploads/2016/03/GenSure_E-1000x_Spec012916.pdf`, `https://www.wartsila.com/docs/default-source/energy-docs/technology-products/product-leaflets/wartsila-50sg.pdf` |
| **notes** | 9 | `Degradation`, `Degradation +50 Btu/kWh/yr`, `GT Heat Rate <8333 kJ/kWh = 7898 Btu/kWh LHV`, `HHV 5811-7127 Btu/kWh range; midpoint 6800`, `Heat rate 7207 kJ/kWh = 6834 Btu/kWh LHV at generator terminals`, `PEM FC system`, `PEM FC ~55% LHV; HHV = LHV/0.885`, `SC Net Heat Rate LHV 7897 Btu/kWh; HHV approx`, `Simple cycle heat rate 7775 Btu/kWh LHV per Gas Turbine World` |

#### Sample Data (First 3 rows)

| unit | technology | fuel_type | heat_rate_btu_per_kwh_hhv | heat_rate_btu_per_kwh_lhv | electrical_efficiency_lhv_pct | date | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bloom_es5 | sofc | natural_gas | 6800 | 6324 | 65.0 | 2024-01 | ... |
| bloom_es5 | sofc | natural_gas | 6850 | 6371 | 64.5 | 2025-01 | ... |
| bloom_es5 | sofc | natural_gas | 6900 | 6417 | 64.0 | 2026-01 | ... |

---

### File: `DATA/hedge_ratios.csv`

- **Size:** 2.10 KB
- **Total Rows:** 16
- **Total Columns:** 9
- **Category Columns:** company, commodity, instruments, date, source_url, notes
- **Numeric Columns:** hedge_ratio, tenor_yr
- **Date Columns:** *None*
- **Text Columns:** source

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **company** | 6 | `aws`, `google`, `intel`, `meta`, `microsoft`, `oracle` |
| **commodity** | 1 | `natural_gas` |
| **instruments** | 3 | `swaps`, `swaps_collars`, `swaps_collars_physical` |
| **date** | 3 | `2024-01`, `2025-01`, `2026-01` |
| **source_url** | 7 | `https://www.sec.gov/`, `https://www.sec.gov/Archives/edgar/data/1018724/000101872424000023/amzn-20231231.htm`, `https://www.sec.gov/Archives/edgar/data/1326801/000132680124000023/meta-20231231.htm`, `https://www.sec.gov/Archives/edgar/data/1341439/000134143924000023/orcl-20231231.htm`, `https://www.sec.gov/Archives/edgar/data/1652044/000165204424000022/goog-20231231.htm`, `https://www.sec.gov/Archives/edgar/data/50863/000005086324000023/intc-20231230.htm`, `https://www.sec.gov/Archives/edgar/data/789019/000078901924000023/msft-20240630.htm` |
| **notes** | 9 | `Commodity derivatives: natural gas hedges`, `Commodity hedging program`, `Natural gas hedges for datacenters`, `Natural gas hedges for manufacturing`, `Natural gas procurement hedges`, `Physical and financial hedges`, `Projected`, `Updated`, `Updated hedge ratio` |

#### Sample Data (First 3 rows)

| company | commodity | hedge_ratio | tenor_yr | instruments | date | source | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| microsoft | natural_gas | 0.65 | 3 | swaps_collars | 2024-01 | Microsoft 10-K 2024 | ... |
| microsoft | natural_gas | 0.7 | 2 | swaps_collars | 2025-01 | Microsoft 10-K 2025 | ... |
| microsoft | natural_gas | 0.75 | 2 | swaps_collars | 2026-01 | Microsoft 10-K 2026 (est.) | ... |

---

### File: `DATA/macro/fred_core_series.csv`

- **Size:** 1.72 KB
- **Total Rows:** 18
- **Total Columns:** 7
- **Category Columns:** units, frequency, source
- **Numeric Columns:** last_value
- **Date Columns:** last_date
- **Text Columns:** series_id, title

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **units** | 11 | `Billions of Chained 2017 Dollars`, `Dollars per Barrel`, `Dollars per Million BTU`, `Index 1982-1984=100`, `Index 1st Qtr 1966=100`, `Index 2006=100`, `Index 2017=100`, `Percent`, `Thousands of Persons`, `U.S. Dollars per Metric Ton`, `U.S. Dollars per Pound` |
| **frequency** | 3 | `Daily`, `Monthly`, `Quarterly` |
| **source** | 1 | `FRED` |

#### Sample Data (First 3 rows)

| series_id | title | units | frequency | last_value | last_date | source |
| --- | --- | --- | --- | --- | --- | --- |
| GDPC1 | Real Gross Domestic Product | Billions of Chained 2017 Dollars | Quarterly | 23769.0 | 2026-01-01 | FRED |
| CPIAUCSL | Consumer Price Index for All Urban Co... | Index 1982-1984=100 | Monthly | 316.437 | 2026-03-01 | FRED |
| PCEPILFE | Personal Consumption Expenditures: Ch... | Index 2017=100 | Monthly | 123.4 | 2026-03-01 | FRED |

---

### File: `DATA/macro/fred_series_catalog.csv`

- **Size:** 2.09 KB
- **Total Rows:** 23
- **Total Columns:** 6
- **Category Columns:** frequency, units, source
- **Numeric Columns:** *None*
- **Date Columns:** last_updated
- **Text Columns:** series_id, series_name

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **frequency** | 3 | `Daily`, `Monthly`, `Quarterly` |
| **units** | 14 | `Billions of Chained 2017 Dollars`, `Billions of Dollars`, `Dollars per Barrel`, `Dollars per Hour`, `Dollars per Million BTU`, `Index 1966Q1=100`, `Index 1982-1984=100`, `Index 2017=100`, `Index Jan 2006=100`, `Level in Thousands`, `Millions of Dollars`, `Percent`, `Percent of Capacity`, `U.S. Dollars per Metric Ton` |
| **source** | 1 | `FRED` |

#### Sample Data (First 3 rows)

| series_id | series_name | frequency | units | source | last_updated |
| --- | --- | --- | --- | --- | --- |
| GDPC1 | Real Gross Domestic Product | Quarterly | Billions of Chained 2017 Dollars | FRED | 2026-07-09 |
| CPIAUCSL | Consumer Price Index for All Urban Co... | Monthly | Index 1982-1984=100 | FRED | 2026-07-09 |
| PCEPILFE | Personal Consumption Expenditures: Ch... | Monthly | Index 2017=100 | FRED | 2026-07-09 |

---

### File: `DATA/onsite_gen_capacity.csv`

- **Size:** 4.10 KB
- **Total Rows:** 27
- **Total Columns:** 11
- **Category Columns:** company, region, technology, fuel_type, source_url
- **Numeric Columns:** capacity_mw, cod_year, capacity_factor, heat_rate_btu_per_kwh
- **Date Columns:** *None*
- **Text Columns:** deployment_source, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **company** | 10 | `aws`, `coreweave`, `cyrusone`, `digital_realty`, `equinix`, `google`, `intel`, `meta`, `microsoft`, `oracle` |
| **region** | 1 | `us` |
| **technology** | 4 | `bloom_sofc`, `gas_turbine`, `hydrogen_fc`, `solar_storage` |
| **fuel_type** | 3 | `hydrogen`, `natural_gas`, `sunlight` |
| **source_url** | 7 | `https://sustainability.fb.com/`, `https://www.ballard.com/`, `https://www.bloomenergy.com/`, `https://www.caiso.com/`, `https://www.gevernova.com/`, `https://www.plugpower.com/`, `https://www.sec.gov/Archives/edgar/data/1664703/000162828025016212/a202410kars.pdf` |

#### Sample Data (First 3 rows)

| company | region | technology | capacity_mw | cod_year | capacity_factor | heat_rate_btu_per_kwh | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| microsoft | us | bloom_sofc | 20.0 | 2024 | 0.9 | 6800 | ... |
| microsoft | us | bloom_sofc | 20.0 | 2025 | 0.9 | 6800 | ... |
| microsoft | us | bloom_sofc | 20.0 | 2026 | 0.9 | 6800 | ... |

---

### File: `DATA/power/fuel_prices.csv`

- **Size:** 4.47 KB
- **Total Rows:** 144
- **Total Columns:** 6
- **Category Columns:** hub, source
- **Numeric Columns:** price_usd_mmbtu, basis_diff_usd_mmbtu, volatility_pct
- **Date Columns:** *None*
- **Text Columns:** date

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **hub** | 3 | `henry_hub`, `jk`, `ttf` |
| **source** | 2 | `eia`, `ice` |

#### Sample Data (First 3 rows)

| hub | date | price_usd_mmbtu | basis_diff_usd_mmbtu | volatility_pct | source |
| --- | --- | --- | --- | --- | --- |
| henry_hub | 2023-01 | 2.5 | 0.0 | 35 | eia |
| henry_hub | 2023-02 | 2.3 | 0.0 | 35 | eia |
| henry_hub | 2023-03 | 2.1 | 0.0 | 35 | eia |

---

### File: `DATA/power/grid_services_revenue.csv`

- **Size:** 1.24 KB
- **Total Rows:** 22
- **Total Columns:** 6
- **Category Columns:** iso, service, date, source
- **Numeric Columns:** price_usd_mw_yr, volume_mw
- **Date Columns:** *None*
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **iso** | 7 | `caiso`, `ercot`, `iso-ne`, `miso`, `nyiso`, `pjm`, `spp` |
| **service** | 8 | `capacity`, `non_spinning_reserve`, `regulation`, `regulation_down`, `regulation_up`, `responsive_reserve`, `spinning_reserve`, `synchronized_reserve` |
| **date** | 1 | `2024-01` |
| **source** | 14 | `caiso_market_report`, `caiso_ra_report`, `ercot_energy_only`, `ercot_market_report`, `iso-ne_market_report`, `iso-ne_ra_report`, `miso_market_report`, `miso_ra_report`, `nyiso_market_report`, `nyiso_ra_report`, `pjm_market_report`, `pjm_ra_report`, `spp_market_report`, `spp_ra_report` |

#### Sample Data (First 3 rows)

| iso | service | price_usd_mw_yr | volume_mw | date | source |
| --- | --- | --- | --- | --- | --- |
| caiso | regulation_up | 45000 | 1200 | 2024-01 | caiso_market_report |
| caiso | regulation_down | 38000 | 1100 | 2024-01 | caiso_market_report |
| caiso | spinning_reserve | 25000 | 800 | 2024-01 | caiso_market_report |

---

### File: `DATA/power/heat_rates.csv`

- **Size:** 1.09 KB
- **Total Rows:** 16
- **Total Columns:** 7
- **Category Columns:** unit, technology, fuel_type, date, source
- **Numeric Columns:** heat_rate_btu_kwh, degradation_pct_yr
- **Date Columns:** *None*
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **unit** | 8 | `ballard_fc`, `bloom_es5`, `caterpillar_fc`, `ge_7ha`, `mitsubishi_m501`, `plug_power_gen`, `siemens_hl`, `wartsila_18v50` |
| **technology** | 5 | `gas_turbine`, `hydrogen`, `rice`, `sofc`, `solid_oxide` |
| **fuel_type** | 2 | `hydrogen`, `natural_gas` |
| **date** | 5 | `2024-01`, `2025-01`, `2026-01`, `2027-01`, `2028-01` |
| **source** | 8 | `ballard_specs`, `bloomenergy_whitepaper`, `caterpillar_specs`, `ge_specs`, `mitsubishi_specs`, `plug_power_specs`, `siemens_specs`, `wartsila_specs` |

#### Sample Data (First 3 rows)

| unit | technology | fuel_type | heat_rate_btu_kwh | date | degradation_pct_yr | source |
| --- | --- | --- | --- | --- | --- | --- |
| bloom_es5 | sofc | natural_gas | 6800 | 2024-01 | 0.5 | bloomenergy_whitepaper |
| bloom_es5 | sofc | natural_gas | 6850 | 2025-01 | 0.5 | bloomenergy_whitepaper |
| bloom_es5 | sofc | natural_gas | 6900 | 2026-01 | 0.5 | bloomenergy_whitepaper |

---

### File: `DATA/power/hedge_ratios.csv`

- **Size:** 0.95 KB
- **Total Rows:** 16
- **Total Columns:** 7
- **Category Columns:** company, commodity, instruments, date, source
- **Numeric Columns:** hedge_ratio, tenor_yr
- **Date Columns:** *None*
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **company** | 6 | `aws`, `google`, `intel`, `meta`, `microsoft`, `oracle` |
| **commodity** | 1 | `natural_gas` |
| **instruments** | 3 | `swaps`, `swaps_collars`, `swaps_collars_physical` |
| **date** | 3 | `2024-01`, `2025-01`, `2026-01` |
| **source** | 6 | `alphabet_10k`, `amazon_10k`, `intel_10k`, `meta_10k`, `microsoft_10k`, `oracle_10k` |

#### Sample Data (First 3 rows)

| company | commodity | hedge_ratio | tenor_yr | instruments | date | source |
| --- | --- | --- | --- | --- | --- | --- |
| microsoft | natural_gas | 0.65 | 3 | swaps_collars | 2024-01 | microsoft_10k |
| microsoft | natural_gas | 0.7 | 2 | swaps_collars | 2025-01 | microsoft_10k |
| microsoft | natural_gas | 0.75 | 2 | swaps_collars | 2026-01 | microsoft_10k |

---

### File: `DATA/power/onsite_gen_capacity.csv`

- **Size:** 1.96 KB
- **Total Rows:** 25
- **Total Columns:** 9
- **Category Columns:** company, region, technology, fuel_type
- **Numeric Columns:** capacity_mw, cod_year, capacity_factor, heat_rate_btu_kwh
- **Date Columns:** *None*
- **Text Columns:** deployment_source

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **company** | 9 | `aws`, `coreweave`, `cyrusone`, `digital_realty`, `equinix`, `google`, `intel`, `microsoft`, `oracle` |
| **region** | 1 | `us` |
| **technology** | 3 | `bloom_sofc`, `gas_turbine`, `hydrogen_fc` |
| **fuel_type** | 2 | `hydrogen`, `natural_gas` |

#### Sample Data (First 3 rows)

| company | region | technology | capacity_mw | cod_year | capacity_factor | heat_rate_btu_kwh | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| microsoft | us | bloom_sofc | 20.0 | 2024 | 0.9 | 6800 | ... |
| microsoft | us | bloom_sofc | 20.0 | 2025 | 0.9 | 6800 | ... |
| microsoft | us | bloom_sofc | 20.0 | 2026 | 0.9 | 6800 | ... |

---

### File: `DATA/productivity/meta_analysis_studies.csv`

- **Size:** 2.67 KB
- **Total Rows:** 15
- **Total Columns:** 14
- **Category Columns:** study, category, intervention, industry, task_type, study_design, quality_score, source, source_url
- **Numeric Columns:** sample_size, effect_size_pct, ci_lower_pct, ci_upper_pct, date
- **Date Columns:** *None*
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **study** | 15 | `agrawal_2023`, `brynjolfsson_2023`, `cui_2024`, `dellacqua_2023`, `eloundou_2023`, `felten_2023`, `kalliamvakou_2022`, `kanazawa_2023`, `liu_2024`, `moradi_2023`, `noy_2023`, `peng_2023`, `tabachnyk_2022`, `wang_2023`, `zhang_2023` |
| **category** | 8 | `coding`, `consulting`, `customer_support`, `general`, `legal`, `rd_drug`, `rd_materials`, `writing` |
| **intervention** | 13 | `ai_analysis`, `ai_assistant`, `ai_discovery`, `ai_exposure`, `ai_pair_programming`, `ai_review`, `chatgpt`, `codex`, `copilot`, `genai_assistant`, `github_copilot`, `llm_exposure`, `ml_code_completion` |
| **industry** | 9 | `all_occupations`, `consulting`, `customer_service`, `legal`, `materials_science`, `pharma`, `professional_services`, `software_engineering`, `technology` |
| **task_type** | 13 | `business_writing`, `code_generation`, `customer_support`, `debugging`, `document_review`, `drug_discovery`, `experiment_design`, `market_research`, `occupation_level`, `productivity`, `strategy_analysis`, `task_automation`, `ticket_resolution` |
| **study_design** | 4 | `meta_analysis`, `quasi_exp`, `rct`, `survey` |
| **quality_score** | 2 | `high`, `medium` |
| **source** | 15 | `Agrawal et al. 2023`, `Brynjolfsson et al. 2023 NBER`, `Cui et al. 2024 QJE`, `Dell'Acqua et al. 2023 (BCG)`, `Eloundou et al. 2023 (OpenAI)`, `Felten et al. 2023`, `Kalliamvakou et al. 2022 (GitHub)`, `Kanazawa et al. 2023`, `Liu et al. 2024`, `Moradi et al. 2023`, `Noy & Zhang 2023 Science`, `Peng et al. 2023 (Microsoft)`, `Tabachnyk & Nikolov 2022`, `Wang et al. 2023 Nature`, `Zhang et al. 2023` |
| **source_url** | 14 | `https://arxiv.org/abs/2210.05711`, `https://arxiv.org/abs/2302.06590`, `https://arxiv.org/abs/2303.10130`, `https://arxiv.org/abs/2305.14822`, `https://arxiv.org/abs/2305.15024`, `https://arxiv.org/abs/2306.07822`, `https://arxiv.org/abs/2306.17175`, `https://doi.org/10.1093/qje/qjae012`, `https://github.blog/2022-09-07-research-quantifying-github-copilots-impact/`, `https://www.hbs.edu/ris/Publication%20Files/24-013_0f7c8c5a-6b4b-4c7d-9c5a-8f9e5b7f5c6d.pdf`, `https://www.nature.com/articles/s41586-023-06735-2`, `https://www.nature.com/articles/s41587-024-02123-4`, `https://www.nber.org/papers/w31161`, `https://www.science.org/doi/10.1126/science.adh2586` |

#### Sample Data (First 3 rows)

| study | category | intervention | industry | task_type | sample_size | effect_size_pct | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| peng_2023 | coding | github_copilot | software_engineering | code_generation | 95 | 55.8 | ... |
| tabachnyk_2022 | coding | ml_code_completion | software_engineering | code_generation | 120 | 37.0 | ... |
| moradi_2023 | coding | ai_pair_programming | software_engineering | debugging | 80 | 28.5 | ... |

---

### File: `DATA/productivity_meta_analysis.csv`

- **Size:** 2.67 KB
- **Total Rows:** 15
- **Total Columns:** 14
- **Category Columns:** study, category, intervention, industry, task_type, study_design, quality_score, source, source_url
- **Numeric Columns:** sample_size, effect_size_pct, ci_lower_pct, ci_upper_pct, date
- **Date Columns:** *None*
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **study** | 15 | `agrawal_2023`, `brynjolfsson_2023`, `cui_2024`, `dellacqua_2023`, `eloundou_2023`, `felten_2023`, `kalliamvakou_2022`, `kanazawa_2023`, `liu_2024`, `moradi_2023`, `noy_2023`, `peng_2023`, `tabachnyk_2022`, `wang_2023`, `zhang_2023` |
| **category** | 8 | `coding`, `consulting`, `customer_support`, `general`, `legal`, `rd_drug`, `rd_materials`, `writing` |
| **intervention** | 13 | `ai_analysis`, `ai_assistant`, `ai_discovery`, `ai_exposure`, `ai_pair_programming`, `ai_review`, `chatgpt`, `codex`, `copilot`, `genai_assistant`, `github_copilot`, `llm_exposure`, `ml_code_completion` |
| **industry** | 9 | `all_occupations`, `consulting`, `customer_service`, `legal`, `materials_science`, `pharma`, `professional_services`, `software_engineering`, `technology` |
| **task_type** | 13 | `business_writing`, `code_generation`, `customer_support`, `debugging`, `document_review`, `drug_discovery`, `experiment_design`, `market_research`, `occupation_level`, `productivity`, `strategy_analysis`, `task_automation`, `ticket_resolution` |
| **study_design** | 4 | `meta_analysis`, `quasi_exp`, `rct`, `survey` |
| **quality_score** | 2 | `high`, `medium` |
| **source** | 15 | `Agrawal et al. 2023`, `Brynjolfsson et al. 2023 NBER`, `Cui et al. 2024 QJE`, `Dell'Acqua et al. 2023 (BCG)`, `Eloundou et al. 2023 (OpenAI)`, `Felten et al. 2023`, `Kalliamvakou et al. 2022 (GitHub)`, `Kanazawa et al. 2023`, `Liu et al. 2024`, `Moradi et al. 2023`, `Noy & Zhang 2023 Science`, `Peng et al. 2023 (Microsoft)`, `Tabachnyk & Nikolov 2022`, `Wang et al. 2023 Nature`, `Zhang et al. 2023` |
| **source_url** | 14 | `https://arxiv.org/abs/2210.05711`, `https://arxiv.org/abs/2302.06590`, `https://arxiv.org/abs/2303.10130`, `https://arxiv.org/abs/2305.14822`, `https://arxiv.org/abs/2305.15024`, `https://arxiv.org/abs/2306.07822`, `https://arxiv.org/abs/2306.17175`, `https://doi.org/10.1093/qje/qjae012`, `https://github.blog/2022-09-07-research-quantifying-github-copilots-impact/`, `https://www.hbs.edu/ris/Publication%20Files/24-013_0f7c8c5a-6b4b-4c7d-9c5a-8f9e5b7f5c6d.pdf`, `https://www.nature.com/articles/s41586-023-06735-2`, `https://www.nature.com/articles/s41587-024-02123-4`, `https://www.nber.org/papers/w31161`, `https://www.science.org/doi/10.1126/science.adh2586` |

#### Sample Data (First 3 rows)

| study | category | intervention | industry | task_type | sample_size | effect_size_pct | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| peng_2023 | coding | github_copilot | software_engineering | code_generation | 95 | 55.8 | ... |
| tabachnyk_2022 | coding | ml_code_completion | software_engineering | code_generation | 120 | 37.0 | ... |
| moradi_2023 | coding | ai_pair_programming | software_engineering | debugging | 80 | 28.5 | ... |

---

### File: `DATA/regional_infrastructure.csv`

- **Size:** 2.47 KB
- **Total Rows:** 13
- **Total Columns:** 13
- **Category Columns:** region, country, source, source_url, notes
- **Numeric Columns:** ppp_factor_usd_base, power_growth_cap_annual_pct, grid_connection_delay_months, gov_coordination_index, cost_per_mw_usd_millions, transformer_shortage_factor, cooling_water_availability, renewable_penetration_pct
- **Date Columns:** *None*
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **region** | 9 | `china`, `eu`, `gulf`, `india`, `japan`, `korea`, `southeast_asia`, `taiwan`, `us` |
| **country** | 13 | `china`, `eu_average`, `india`, `indonesia`, `japan`, `malaysia`, `saudi_arabia`, `singapore`, `south_korea`, `taiwan`, `uae`, `united_states`, `vietnam` |
| **source** | 13 | `World Bank ICP 2021 / CEA India`, `World Bank ICP 2021 / DEWA / SEC`, `World Bank ICP 2021 / EMA / SP Group`, `World Bank ICP 2021 / ENTSO-E / EC`, `World Bank ICP 2021 / EVN / ADB`, `World Bank ICP 2021 / KEPCO / KPX`, `World Bank ICP 2021 / LBNL / EIA`, `World Bank ICP 2021 / METI / OCCTO`, `World Bank ICP 2021 / NBS China / LBNL`, `World Bank ICP 2021 / PLN / ADB`, `World Bank ICP 2021 / SEC / NEOM`, `World Bank ICP 2021 / TNB / Suruhanjaya Tenaga`, `World Bank ICP 2021 / Taipower` |
| **source_url** | 1 | `https://www.worldbank.org/en/programs/icp` |
| **notes** | 10 | `PPP 0.45; power growth from CEA NEP; grid delay from POSOCO`, `PPP 0.50; power growth from PDP8`, `PPP 0.55 (ICP 2021); power growth from NDRC 5-yr plan; grid delay from China grid corp`, `PPP 0.75; power growth from Vision 2030; grid from SEC`, `PPP 0.80; power growth from UAE Energy Strategy 2050; grid from DEWA`, `PPP 0.90; power growth from 10th Basic Plan`, `PPP 0.95; power growth near zero; grid delay from OCCTO`, `PPP 1.05; land/power constrained`, `PPP 1.15 (avg); power growth low due to demand stagnation; grid delay from ENTSO-E TYNDP`, `PPP=1.0 base; power growth from FERC/EIA; grid delay from LBNL Queued Up 2025` |

#### Sample Data (First 3 rows)

| region | country | ppp_factor_usd_base | power_growth_cap_annual_pct | grid_connection_delay_months | gov_coordination_index | cost_per_mw_usd_millions | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| us | united_states | 1.0 | 12 | 24 | 0.5 | 2.5 | ... |
| china | china | 0.55 | 24 | 12 | 0.95 | 1.1 | ... |
| india | india | 0.45 | 18 | 18 | 0.7 | 1.3 | ... |

---

### File: `DATA/technology_parameters.csv`

- **Size:** 8.60 KB
- **Total Rows:** 54
- **Total Columns:** 8
- **Category Columns:** technology, parameter, unit
- **Numeric Columns:** value
- **Date Columns:** date_accessed
- **Text Columns:** source, source_url, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **technology** | 6 | `bloom_sofc`, `gas_turbine_7ha`, `hydrogen_fc_plug`, `rice_wartsila_18v50sg`, `smr_nuscale`, `solar_storage` |
| **parameter** | 10 | `capacity_factor`, `capex_usd_per_kw`, `co2_emissions_ton_per_mwh`, `combined_cycle_heat_rate_btu_per_kwh_lhv`, `degradation_pct_per_year`, `electrical_efficiency_lhv_pct`, `heat_rate_btu_per_kwh_hhv`, `heat_rate_btu_per_kwh_lhv`, `om_usd_per_mwh`, `water_intensity_l_per_mwh` |
| **unit** | 8 | `%`, `%/yr`, `Btu/kWh`, `L/MWh`, `LHV %`, `USD/MWh`, `USD/kW`, `ton CO2/MWh` |

#### Sample Data (First 3 rows)

| technology | parameter | value | unit | source | source_url | date_accessed | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bloom_sofc | heat_rate_btu_per_kwh_hhv | 6800.0 | Btu/kWh | Bloom Energy ES6.5 Datasheet | https://www.bloomenergy.com/wp-conten... | 2026-07-14 | ... |
| bloom_sofc | electrical_efficiency_lhv_pct | 65.0 | LHV % | Bloom Energy ES6.5 Datasheet | https://www.bloomenergy.com/wp-conten... | 2026-07-14 | ... |
| bloom_sofc | capacity_factor | 0.9 | nan | Bloom Energy 10-K 2024 / Industry rep... | https://www.sec.gov/Archives/edgar/da... | 2026-07-14 | ... |

---

### File: `DATA/transformer_shortage.csv`

- **Size:** 2.86 KB
- **Total Rows:** 10
- **Total Columns:** 10
- **Category Columns:** transformer_type, lead_time_weeks_2025, price_increase_pct_2020_2024, source, source_url, notes
- **Numeric Columns:** lead_time_weeks_2021, lead_time_weeks_2022, lead_time_weeks_2023, lead_time_weeks_2024
- **Date Columns:** *None*
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **transformer_type** | 10 | `ak_steel`, `distribution_10_25kva`, `distribution_500_1000kva`, `distribution_50_100kva`, `generator_step_up_100_500mva`, `goes_electrical_steel`, `large_power_500mva_plus`, `metglas_amorphous`, `substation_100_300mva`, `substation_10_50mva` |
| **lead_time_weeks_2025** | 8 | `100`, `110`, `130`, `180`, `210`, `250`, `300`, `Wood Mackenzie / NIAC` |
| **price_increase_pct_2020_2024** | 8 | `60`, `65`, `70`, `75`, `80`, `85`, `90`, `https://www.cisa.gov/sites/default/files/2024-06/DRAFT_NIAC_Addressing%20the%20Critical%20Shortage%20of%20Power%20Transformers%20to%20Ensure%20Reliability%20of%20the%20U.S.%20Grid_Report_06052024_508c.pdf` |
| **source** | 3 | `Amorphous steel supplier`, `Only domestic GOES supplier`, `Wood Mackenzie / NIAC` |
| **source_url** | 1 | `https://www.cisa.gov/sites/default/files/2024-06/DRAFT_NIAC_Addressing%20the%20Critical%20Shortage%20of%20Power%20Transformers%20to%20Ensure%20Reliability%20of%20the%20U.S.%20Grid_Report_06052024_508c.pdf` |
| **notes** | 7 | `>500 MVA LPT`, `GSU for power plants`, `Large substation transformer`, `Single-phase pad-mount`, `Substation power transformer`, `Three-phase pad-mount`, `Three-phase pad-mount substation` |

#### Sample Data (First 3 rows)

| transformer_type | lead_time_weeks_2021 | lead_time_weeks_2022 | lead_time_weeks_2023 | lead_time_weeks_2024 | lead_time_weeks_2025 | price_increase_pct_2020_2024 | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| distribution_10_25kva | 30 | 40 | 60 | 80 | 100 | 60 | ... |
| distribution_50_100kva | 35 | 50 | 70 | 90 | 110 | 65 | ... |
| distribution_500_1000kva | 40 | 60 | 80 | 110 | 130 | 70 | ... |

---

### File: `DATA/wholesale_electricity_prices.csv`

- **Size:** 4.19 KB
- **Total Rows:** 27
- **Total Columns:** 8
- **Category Columns:** region, iso, price_type, source, source_url, notes
- **Numeric Columns:** price_usd_per_mwh, year
- **Date Columns:** *None*
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **region** | 1 | `us` |
| **iso** | 9 | `ca_iso`, `ca_north`, `ercot_north`, `isone`, `miso`, `national_avg`, `nyiso`, `pjm_west`, `spp` |
| **price_type** | 1 | `load_weighted_avg_rt` |
| **source** | 2 | `FERC State of the Markets 2024`, `LBNL ReWEP` |
| **source_url** | 2 | `https://eta-publications.lbl.gov/sites/default/files/rewep-2024update_tech-brief_20240429.pdf`, `https://www.ferc.gov/sites/default/files/2025-03/25_State-of-the-Market_0320_1200.pdf` |
| **notes** | 3 | `CAISO high; Jan 2024 spike from gas`, `Down from $63 in 2022`, `ERCOT lowest; 2023 was $52/MWh` |

#### Sample Data (First 3 rows)

| region | iso | price_usd_per_mwh | price_type | year | source | source_url | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| us | ercot_north | 28 | load_weighted_avg_rt | 2024 | FERC State of the Markets 2024 | https://www.ferc.gov/sites/default/fi... | ... |
| us | spp | 28 | load_weighted_avg_rt | 2024 | FERC State of the Markets 2024 | https://www.ferc.gov/sites/default/fi... | ... |
| us | miso | 31 | load_weighted_avg_rt | 2024 | FERC State of the Markets 2024 | https://www.ferc.gov/sites/default/fi... | ... |

---

### File: `data_centers/DATA_LINEAGE_LOG.csv`

- **Size:** 185.98 KB
- **Total Rows:** 1,607
- **Total Columns:** 7
- **Category Columns:** facility_id, facility_name, field, source_type, confidence, primary_source
- **Numeric Columns:** *None*
- **Date Columns:** *None*
- **Text Columns:** value

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **facility_id** | 52 | `DC-00001`, `DC-00002`, `DC-00003`, `DC-00004`, `DC-00005`, `DC-00006`, `DC-00007`, `DC-00008`, `DC-00009`, `DC-00010`, `DC-00011`, `DC-00012`, `DC-00013`, `DC-00014`, `DC-00015` ... (and more) |
| **facility_name** | 52 | `AVAIO Perseus`, `AWS Gilroy`, `Aligned Waddell Campus`, `Apple Mesa`, `Clarksville Data Center`, `Colossus xAI`, `Compass Goodyear`, `Crusoe Tallgrass`, `Crusoe Tallgrass Wyoming`, `Data City Texas`, `Fermi Phase 2 (Nuclear)`, `Fermi Phase 3 (SMR/Expansion)`, `Fort Meade Campus`, `GW Ranch`, `Google Ohio` ... (and more) |
| **field** | 51 | `annual_power_cost_usd`, `annual_power_mwh`, `annual_revenue_potential_usd`, `capacity_category`, `capacity_mw`, `city`, `cluster_size`, `cooling_detail`, `country`, `est_bf16_pflops`, `est_capex_per_gpu`, `est_capex_per_kw`, `est_fp8_pflops`, `est_gpu_count`, `est_gpus_b200` ... (and more) |
| **source_type** | 2 | `Estimated`, `Public Source` |
| **confidence** | 3 | `A`, `B`, `C` |
| **primary_source** | 41 | `$1.6B+ investment`, `$33B project`, `173 acres, 500-700MW secondary`, `1GW cluster`, `2,069 acres`, `AI/Hyperscale`, `Air cooled, 610 acres`, `Cloud/AI`, `Community opposition`, `Community opposition, NDAs signed`, `Crusoe announcements, WY PSC filings`, `Gilroy city permits, PG&E interconnection`, `Google/Arkansas EDC announcements, Entergy IRP`, `Imperial Datacenter site, CAISO queue, KPBS reporting`, `Largest announced US project` ... (and more) |

#### Sample Data (First 3 rows)

| facility_id | facility_name | field | value | source_type | confidence | primary_source |
| --- | --- | --- | --- | --- | --- | --- |
| DC-00001 | Stratos Hyperscale Campus | facility_id | DC-00001 | Public Source | A | Largest announced US project |
| DC-00001 | Stratos Hyperscale Campus | facility_name | Stratos Hyperscale Campus | Public Source | A | Largest announced US project |
| DC-00001 | Stratos Hyperscale Campus | operator | Bitzero Blockchain Inc. | Public Source | A | Largest announced US project |

---

### File: `data_centers/FACILITY_FINANCIALS.csv`

- **Size:** 5.94 KB
- **Total Rows:** 40
- **Total Columns:** 14
- **Category Columns:** status, tier
- **Numeric Columns:** capacity_mw, capex_billion, gpus, inference_pflops, training_pflops, annual_power_cost_million, revenue_billion_45util, ebitda_billion_45util, roic_45util
- **Date Columns:** *None*
- **Text Columns:** facility_id, name, hyperscaler

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **status** | 4 | `Operating`, `Planned`, `Suspended`, `Under Construction` |
| **tier** | 3 | `Tier 1`, `Tier 2`, `Tier 3` |

#### Sample Data (First 3 rows)

| facility_id | name | hyperscaler | capacity_mw | status | tier | capex_billion | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DC-00001 | Stratos Hyperscale Campus | Bitzero | 9000 | Planned | Tier 1 | 81.0 | ... |
| DC-00002 | Monarch Compute Campus | Nscale | 8000 | Planned | Tier 1 | 72.0 | ... |
| DC-00003 | GW Ranch | Pacifico Energy | 7650 | Planned | Tier 1 | 68.85 | ... |

---

### File: `data_centers/GAP_UNCERTAINTY_REGISTER.csv`

- **Size:** 48.74 KB
- **Total Rows:** 534
- **Total Columns:** 5
- **Category Columns:** facility_id, facility_name, missing_field, impact, suggested_source
- **Numeric Columns:** *None*
- **Date Columns:** *None*
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **facility_id** | 52 | `DC-00001`, `DC-00002`, `DC-00003`, `DC-00004`, `DC-00005`, `DC-00006`, `DC-00007`, `DC-00008`, `DC-00009`, `DC-00010`, `DC-00011`, `DC-00012`, `DC-00013`, `DC-00014`, `DC-00015` ... (and more) |
| **facility_name** | 52 | `AVAIO Perseus`, `AWS Gilroy`, `Aligned Waddell Campus`, `Apple Mesa`, `Clarksville Data Center`, `Colossus xAI`, `Compass Goodyear`, `Crusoe Tallgrass`, `Crusoe Tallgrass Wyoming`, `Data City Texas`, `Fermi Phase 2 (Nuclear)`, `Fermi Phase 3 (SMR/Expansion)`, `Fort Meade Campus`, `GW Ranch`, `Google Ohio` ... (and more) |
| **missing_field** | 13 | `capacity_mw`, `cluster_size`, `cooling_detail`, `generation_mix`, `gpu_generation`, `latitude`, `longitude`, `network_detail`, `ppa_price_mwh`, `total_capex_billion`, `utility`, `voltage_kv`, `water_source_mgd` |
| **impact** | 2 | `High`, `Medium` |
| **suggested_source** | 12 | `Building permits / county GIS / OSM`, `Building permits / vendor case studies`, `Earnings calls / supply chain reports / job postings`, `Network topology papers / vendor reference architectures`, `PeeringDB / submarine cable maps / earnings calls`, `SEC 10-K/10-Q / press releases / bond prospectuses`, `State PUC dockets / utility IRP`, `Utility IRP / sustainability reports`, `Utility interconnection agreement / FERC filings`, `Utility interconnection queue / FERC Form 715`, `Utility regulatory filings / PPA announcements`, `Water rights permits / sustainability reports` |

#### Sample Data (First 3 rows)

| facility_id | facility_name | missing_field | impact | suggested_source |
| --- | --- | --- | --- | --- |
| DC-00001 | Stratos Hyperscale Campus | utility | Medium | State PUC dockets / utility IRP |
| DC-00001 | Stratos Hyperscale Campus | ppa_price_mwh | Medium | Utility regulatory filings / PPA anno... |
| DC-00001 | Stratos Hyperscale Campus | cooling_detail | High | Building permits / vendor case studies |

---

### File: `data_centers/MASTER_CAPABILITY_MATRIX.csv`

- **Size:** 16.90 KB
- **Total Rows:** 52
- **Total Columns:** 40
- **Category Columns:** tenant, hyperscaler_category, country, status, tier, capacity_category, expected_online_date, primary_gpu, utility, generation_mix, cooling_detail, network_detail, gpu_generation, notes
- **Numeric Columns:** latitude, longitude, capacity_mw, it_load_mw, est_gpu_count, cluster_size, training_bf16_pflops, inference_fp8_pflops, est_tokens_per_sec_billions, est_training_runs_per_year_gpt4_class, voltage_kv, ppa_price_mwh, annual_power_mwh, annual_power_cost_usd, power_cost_per_gpu_per_year, water_source_mgd, total_capex_billion, est_capex_per_kw, est_capex_per_gpu, annual_revenue_potential_usd
- **Date Columns:** *None*
- **Text Columns:** facility_id, facility_name, operator, city, state_province, source_notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **tenant** | 14 | `$10 billion+`, `$33 billion`, `$40 billion+`, `2026`, `2027`, `2028`, `2032`, `2036`, `AWS`, `Google (unconfirmed)`, `Meta`, `Microsoft`, `OpenAI/Oracle`, `xAI` |
| **hyperscaler_category** | 15 | `AWS`, `Aligned`, `Apple`, `Crusoe`, `Google`, `Meta`, `Microsoft`, `NTT`, `Oracle`, `Other/Unclassified`, `Prime Data Centers`, `Stargate`, `Stream Data Centers`, `Vantage`, `xAI` |
| **country** | 3 | `Norway`, `United Arab Emirates`, `United States` |
| **status** | 5 | `Expanding`, `Operating`, `Planned`, `Suspended`, `Under Construction` |
| **tier** | 3 | `Tier 1`, `Tier 2`, `Tier 3` |
| **capacity_category** | 5 | `Hyperscale (100-999 MW)`, `Large (51-99 MW)`, `Medium (11-50 MW)`, `Mega campus (>1`, `Unknown` |
| **expected_online_date** | 10 | `$10 billion`, `$14 billion`, `$3.6 billion`, `$300 million`, `$6 billion`, `2025`, `2026`, `2027`, `2028`, `250` |
| **primary_gpu** | 6 | `B200`, `GB200 NVL72`, `H100`, `H100 (est.)`, `TPU v5p/v6`, `Trainium2/Inferentia2` |
| **utility** | 7 | `Entergy Arkansas`, `Entergy Louisiana`, `Georgia Power / Southern Company`, `IID / CAISO`, `Oncor / ERCOT`, `PG&E`, `PacifiCorp / WAPA` |
| **generation_mix** | 7 | `Gas 40%, Nuclear 30%, Coal 15%, Renewable 15%`, `Gas 50%, Nuclear 25%, Renewable 25%`, `Gas 60%, Nuclear 25%, Renewable 15%`, `Solar 30%, Hydro 25%, Gas 25%, Nuclear 15%, Wind 5%`, `Solar 50%, Geothermal 20%, Gas 30%`, `Wind 35%, Solar 25%, Gas 30%, Nuclear 10%`, `Wind 50%, Gas 30%, Coal 20%` |
| **cooling_detail** | 7 | `Direct liquid cooling (DLC)`, `Direct liquid cooling (DLC) 100%`, `Direct-to-chip liquid (80%) + rear-door (20%)`, `Direct-to-chip liquid (TPU pods)`, `Hybrid air/liquid, 100 gas generators + 862MWh BESS`, `Hybrid air/water, 95% free cooling`, `Rear-door heat exchanger + liquid assist` |
| **network_detail** | 7 | `100G/400G to San Jose/Sacramento`, `400G/800G to Denver/Salt Lake`, `Custom optical circuit switching, 1.6T regional`, `InfiniBand NDR 400G, 800G to Chicago/Dallas`, `InfiniBand NDR, 800G to LA/San Diego`, `NVL72 + InfiniBand NDR 400G, 800G ZR+ to Atlanta/Dallas`, `NVL72 + InfiniBand NDR, 1.6T to Dallas` |
| **gpu_generation** | 8 | `GB200 NVL72`, `GB200 NVL72 / GB300`, `H100 (2025), B200 (2026+)`, `H100 / B200`, `H100 / Maia 100`, `H100 / TPU v5`, `TPU v5p / v6`, `Trainium2 / Inferentia2` |
| **notes** | 13 | `1,300 acres`, `100 gas generators, 862MWh BESS`, `100% renewable, recycled water`, `100k GPUs`, `100k GPUs by 2026`, `3 of 5 buildings broke ground`, `AI/Cloud`, `AI/Hyperscale`, `Building 4 268MW, Bldg 2 260MW`, `Cloud/AI`, `Community opposition`, `Phase 1 approved`, `Water concerns, 31M gal/yr` |

#### Sample Data (First 3 rows)

| facility_id | facility_name | operator | tenant | hyperscaler_category | city | state_province | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DC-00001 | Stratos Hyperscale Campus | Bitzero Blockchain Inc. | nan | Other/Unclassified | nan | Utah | ... |
| DC-00002 | Monarch Compute Campus | Nscale Ltd. | 2027 | Other/Unclassified | nan | West Virginia | ... |
| DC-00003 | GW Ranch | Pacifico Energy | 2027 | Other/Unclassified | nan | Texas | ... |

---

### File: `data_centers/fractracker_us_datacenters.csv`

- **Size:** 711.25 KB
- **Total Rows:** 1,603
- **Total Columns:** 44
- **Category Columns:** state, status, location_confidence, purpose, tenant, sizerank, power_source, dedicated_power_plant, number_of_generators, cooling_source, cooling_type, community_pushback, advocacy_information, resistance_status, nda, community_group_website_2, information_source, info_source_5, info_source_6, info_source_7, info_source_8
- **Numeric Columns:** zip, lat, long, mw, number_of_buildings, property_size_acres, expected_date_online
- **Date Columns:** date_created, date_updated
- **Text Columns:** facility_name, address, city, county, operator_name, facility_size_sqft, project_cost, community_group_website_1, petition_url, other_info, info_source_1, info_source_2, info_source_3, info_source_4

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **state** | 51 | `AK`, `AL`, `AR`, `AZ`, `CA`, `CO`, `CT`, `DE`, `FL`, `GA`, `HI`, `IA`, `ID`, `IL`, `IN` ... (and more) |
| **status** | 7 | `Approved/Permitted/Under construction`, `Cancelled`, `Expanding`, `Operating`, `Pre-proposal`, `Proposed`, `Suspended` |
| **location_confidence** | 6 | `High`, `High `, `Low`, `Medium`, `Medium `, `high ` |
| **purpose** | 27 | ` Multi-tenant industrial park, flex logistics space, and high-density data center facilities`, `AI`, `AI "superfactory"`, `AI / hyperscale data center`, `AI Data center and solar fam`, `AI and Bitcoin`, `AI and Cloud Computing`, `AI data center / hyperscale campus`, `AI for Nuclear Research`, `AI/cloud-computing`, `Bitcoin`, `Bitcoin transitioning to AI`, `Colocation / enterprise data center`, `Colocation data center`, `Crypto` ... (and more) |
| **tenant** | 2 | `Anthropic`, `Multiple colocation tenants` |
| **sizerank** | 7 | `Hyperscale (100-999 MW)`, `Hyperscale (101-999 MW)`, `Large (51-99 MW)`, `Medium (11-50 MW)`, `Mega campus (>1,000 MW)`, `Small (0-10 MW)`, `Unknown` |
| **power_source** | 21 | `Biomass`, `Coal`, `Coal, Natural gas, Biomass`, `Fuel Cells`, `Grid (unspecified mix)`, `Grid (unspecified mix), Biomass`, `Grid (unspecified mix), Solar`, `Hybrid (onsite and grid)`, `Hydroelectric`, `Hydroelectric, Grid (unspecified mix)`, `Natural gas`, `Natural gas, Hybrid (onsite and grid)`, `Natural gas, Nuclear, Solar`, `Nuclear`, `Nuclear, Solar, Geothermal, Grid (unspecified mix)` ... (and more) |
| **dedicated_power_plant** | 22 | `2`, `Bluebonnet Electric Cooperative`, `EW Brown Generation Station`, `Georgia Power`, `May use jet engines from retired military planes`, `Northwestern Energy`, `Possibly`, `Salt River Project (SRP) substation`, `Yes`, `Yes `, `Yes - Adams Fork Energy Project Power Station 1`, `Yes - Adams Fork Energy Project Power Station 2`, `Yes - Apollo Generating Station`, `Yes - Bluegrass Power Station`, `Yes - Brightloop Hyrogen Plant / Monarch` ... (and more) |
| **number_of_generators** | 13 | `0`, `1.2 GW diesel`, `100 natural gas-powered backup emergency generators connected to Southern California Gas Company’s high-pressure gas line`, `115 diesel-fueled generators`, `12`, `12-24`, `14 on-site diesel generators`, `15`, `158 diesel backup generators`, `25 2.5MW emergency generators for redundancy purposes`, `516`, `6`, `813` |
| **cooling_source** | 3 | `Air`, `Hybrid air/water`, `Water` |
| **cooling_type** | 3 | `Closed loop`, `Fans`, `Open loop` |
| **community_pushback** | 3 | `Unknown`, `Yes`, `Yes ` |
| **advocacy_information** | 63 | `12-month moratorium`, `180 day moratorium in place in Harlingen as of May 2026.`, `A citizens' group ("We say NO! to Atlas Development's data center") has organized against the project, citing concerns over power and water usage, as well as an open meetings complaint filed in November 2025 regarding the sale process.`, `A public hearing is being held March 19 at 7:00 PM in the town of Alabama on Judge Rd. Public comments being accepted through March 31: https://docs.google.com/document/d/1V9JcpmERQ7EZ5vxm9KiaX6AqYO6XUkpuCELwxKIxHKs/edit?usp=drivesdk`, `Advocacy against the Franklin Partners LLC data center in Pavilion Township was primarily driven by a rapid grassroots movement of local residents. Concerned neighbors quickly organized to challenge the proposed zoning changes, leading to packed town hall meetings and an eventual project withdrawal in late 2025.`, `Advocacy regarding Project Springbank in Adairsville, GA, centers on a successful community-led campaign that resulted in the developer, Atlas Development, withdrawing its rezoning application in May 2025. Despite the project being formally cancelled, local and statewide advocacy remains high to prevent similar developments from resurfacing.`, `Advocacy surrounding data centers in Illinois has intensified in early 2026, shifting from isolated local protests to a coordinated statewide legislative push.`, `Approved at the municipal level. `, `As of March 2026, Project Jupiter, a proposed $165 billion AI data center complex in Santa Teresa, NM, is facing intense pushback from a coalition of 16 environmental and civil rights organizations. Advocacy centers on the project's potential to strain finite natural resources and its bypassing of state environmental regulations.`, `Bessemer Data Center - We Say No!`, `By a 5-4 vote, the commission voted against rezoning the site (also called Crooked Creek) in April 2026`, `By a 5-4 vote, the commission voted in favor of rezoning the site in April 2026`, `Climate Revolution NJ`, `Community advocacy surrounding the xAI project at 5420 Tulane Rd is led by a coalition of environmental justice and civil rights groups. These organizations are primarily concerned with the impact of massive energy and water demands on South Memphis, a region they describe as already overburdened by decades of industrial pollution.`, `Community meeting held Nov 2025 regarding proposed 900 MW, $19 B Kingsboro AI data center by Energy Storage Solutions. Environmental and utility-rate concerns raised by residents and NC Environmental Justice Network. Local organizing ongoing; county considering sale of Kingsboro Business Park land for project.` ... (and more) |
| **resistance_status** | 3 | `Emerging Concern`, `Organized Advocacy`, `Unknown` |
| **nda** | 8 | `Active (Tenant identity legally shielded)`, `Bessemer Mayor Kenneth Gulley, the city attorney, and other city leaders signed NDAs`, `Every elected official is under an NDA including the Montana Public Service Commission`, `Marion County officials confirmed that the council signed a nondisclosure agreement`, `No`, `Officials knew of the Meta plan as “Project Accordion” for more than a year before it was officially announced`, `Yes`, `Yes- https://www.al.com/news/2025/10/secrecy-agreements-fuel-pushback-of-14-billion-alabama-data-center.html` |
| **community_group_website_2** | 32 | `https://capitalbnews.org/meta-richland-parish-ai-data-center/`, `https://centerforcoalfieldjustice.org/`, `https://cwfnc.org/stokes/`, `https://friendsofblackwater.org/`, `https://linktr.ee/residentsunitedlowell`, `https://neighbors4change.com/`, `https://wilmingtondatacenter.org/`, `https://wvrivers.org/`, `https://www.change.org/p/stop-the-construction-of-michigan-s-largest-data-center-in-howell`, `https://www.datacenterdynamics.com/en/news/oracle-and-openai-start-construction-on-stargate-data-center-campus-in-saline-township-michigan/`, `https://www.facebook.com/groups/1117995533656453`, `https://www.facebook.com/groups/1140996281561878/`, `https://www.facebook.com/groups/1359906715176907/`, `https://www.facebook.com/groups/1397482882419331/`, `https://www.facebook.com/groups/1469043077373264/` ... (and more) |
| **information_source** | 6 | `Crowdsourced`, `FOIA/ public records request`, `Media Monitoring`, `Other`, `PEC`, `Sci4GA` |
| **info_source_5** | 72 | `https://cleanview.co/public/data-centers/georgia/1896/fairwater-2---atlanta`, `https://datacenterwatch.substack.com/p/briefing-11212025`, `https://epoch.ai/data/data-centers/satellite-explorer/CoreweaveHeliosAftonTexas?ref=404media.co`, `https://epoch.ai/data/data-centers/satellite-explorer/MetaPrometheusNewAlbanyOhio?ref=404media.co`, `https://epoch.ai/data/data-centers/satellite-explorer/OpenAIOracleStargateAbileneTexas?ref=404media.co`, `https://finance.yahoo.com/news/ai-power-darling-fermi-implodes-185100893.html`, `https://fox56.com/news/local/archbald-residents-unite-against-unanswered-questions-on-data-centers`, `https://local21news.com/news/local/a-new-data-center-might-be-build-in-cumberland-county-and-its-700-acres-ai-carlisle-artificial-intelligence-pennsylvania-data-center-partners-powerhouse-pa`, `https://opsb.ohio.gov/news/opsb-authorizes-construction-of-wood-county-power-plant`, `https://planetdetroit.org/2026/01/allen-park-postpones-data-center-decision/`, `https://planetdetroit.org/2026/02/project-cannoli-preliminary-site-plan/`, `https://spotlightdelaware.org/2026/03/26/delaware-city-data-center-environmental-denial-upheld-by-state-board/`, `https://tecfusions.com/?clarksville#solutions-newkensington`, `https://tompkinsweekly.com/articles/cayuga-data-campus-lansing/`, `https://triblive.com/local/valley-news-dispatch/springdale-planning-commission-oks-data-center-project-proposal-moves-to-council/` ... (and more) |
| **info_source_6** | 44 | `https://dep.wv.gov/daq/permitting/Documents/Fundamental%20Data%20LLC;%20Ridgeline%20Facility/093-00034_APPL_13-3713.pdf`, `https://elpasomatters.org/2025/09/25/stargate-open-ai-oracle-project-jupiter-data-center-dona-ana-new-mexico-el-paso-texas/`, `https://epoch.ai/data/data-centers/satellite-explorer/AnthropicAmazonProjectRainierNewCarlisleIndiana?ref=404media.co`, `https://fermiamerica.com/`, `https://fox56.com/news/local/archbald-residents-unite-against-unanswered-questions-on-data-centers`, `https://ithacavoice.org/2026/01/local-groups-file-suit-against-terawulf-lansing-zoning-board-over-data-center/`, `https://news.azpm.org/p/azpmnews/2026/5/28/229919-arizona-water-officials-approve-wells-tied-to-project-blue-data-center/`, `https://oilandgaswatch.org/facility/rec_d4f1u60q7easr8ra1g3g`, `https://planetdetroit.org/2026/02/saline-data-center-air-wetlands-permits/`, `https://planetdetroit.org/2026/03/google-dte-data-center-van-buren/`, `https://triblive.com/local/regional/sprawling-data-center-campus-proposed-next-to-old-bruce-mansfield-power-plant-in-shippingport/`, `https://triblive.com/local/valley-news-dispatch/upper-burrell-data-center-nets-first-tenant-at-former-alcoa-research-site/`, `https://wgxa.tv/news/local/environmental-advocate-urges-twiggs-county-to-reject-data-center-plans-near-ocmulgee-river`, `https://wsbt.com/news/local/st-joseph-county-council-denies-rezoning-of-land-for-data-center-votes-7-2-marathon-meeting-hours-long-public-opinion-13-billion-dollar-project-amazon-new-carlisle-approval-process-plan-commission-st-joseph-county-indiana`, `https://www.bgr.com/1990532/meta-new-aid-data-center-size-70-football-fields-residents-scared-water/` ... (and more) |
| **info_source_7** | 25 | `https://abc3340.com/news/abc-3340-news-iteam/bessemer-unveils-revised-project-marvel-data-center-campus-plan-amid-ongoing-controversy`, `https://epoch.ai/data/data-centers/satellite-explorer/MicrosoftFairwaterMountPleasantWisconsin?ref=404media.co`, `https://lailluminator.com/briefs/entergy-builds-power-plant-for-data-center/`, `https://oilandgaswatch.org/facility/rec_d4f1u60q7easr8ra1g30`, `https://oilandgaswatch.org/facility/rec_d5eiru1uih89upkga2qg`, `https://paenvironmentdaily.blogspot.com/2025/12/dep-to-host-jan-6-public-information.html`, `https://pbswisconsin.org/news-item/the-local-battles-over-data-center-developments-in-wisconsin/?fbclid=IwY2xjawQb89xleHRuA2FlbQIxMQBzcnRjBmFwcF9pZBAyMjIwMzkxNzg4MjAwODkyAAEe_9n-9GXVsrmup4ro8JcBXofGIGDBBJOvEis3IhU4EDbZm0ChkaEapPFbbd8_aem_HvzltHtS42i2Jp2jBPjrRA`, `https://trackdatacenters.com/state/pennsylvania`, `https://truthout.org/articles/new-york-residents-are-fighting-a-data-center-backed-by-a-billionaire-trump-ally/`, `https://www.41nbc.com/twiggs-county-data-center-rezoning-approval/`, `https://www.alleghenyfront.org/meta-beaver-valley-nuclear-power-plant-ai-data-centers/`, `https://www.businesswire.com/news/home/20260401716982/en/Homer-City-Redevelopment-Crosses-the-First-Steel-Threshold`, `https://www.datacenterdynamics.com/en/news/google-confirms-1gw-data-center-campus-near-detroit-michigan-partners-with-dte-energy-on-27gw-power-generation/`, `https://www.datacenterdynamics.com/en/news/groups-sue-to-stall-data-center-project-in-do%C3%B1a-ana-county-new-mexico/`, `https://www.datacenterdynamics.com/en/news/or/` ... (and more) |
| **info_source_8** | 14 | `https://bgindependentmedia.org/meta-data-center-how-it-went-from-economic-development-coup-to-project-local-residents-rue/`, `https://insideclimatenews.org/news/13112025/proposed-alabama-data-center-clashes-with-northern-beltline-birmingham-darter/`, `https://planetdetroit.org/2025/12/billion-dollar-data-center-paused/`, `https://www.41nbc.com/twiggs-county-data-center-rezoning-approval/`, `https://www.datacenterdynamics.com/en/news/google-confirms-it-is-behind-403-acre-data-center-campus-in-hermantown-minnesota/`, `https://www.datacenterdynamics.com/en/news/meta-purchases-additional-1400-acres-for-hyperion-mega-data-center-expansion/`, `https://www.datacenterdynamics.com/en/news/oracle-revealed-as-tenant-of-project-jupiter-data-center-campus-in-new-mexico/`, `https://www.datacenterdynamics.com/en/news/riot-platforms-files-to-add-building-to-cryptomine-and-data-center-campus-in-corsicana-texas/`, `https://www.datacenterdynamics.com/en/news/shippingport-industrial-park/`, `https://www.datacenterdynamics.com/en/news/vantage-tops-out-second-building-at-openais-lighthouse-campus-in-wisconsin/`, `https://www.nytimes.com/2026/03/17/nyregion/ai-data-center-new-york.html`, `https://www.wisn.com/article/whats-that-sound-its-mount-pleasants-new-ai-data-center/70850595`, `https://www.wvia.org/news/local/2026-05-01/fast-track-no-more-pa-kicks-archbald-data-center-campus-off-permit-program`, `https://www.wvxu.org/environment/2025-12-03/developers-data-center-butler-county` |

#### Sample Data (First 3 rows)

| facility_name | address | city | state | zip | county | lat | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Global Stack Data Center | nan | nan | nan | nan | Napa | 38.585007 | ... |
| Stak Energy Data Center | Dalton Hwy, 26 miles south of Deadhorse | North Slope Borough | AK | nan | North Slope | 69.90071 | ... |
| Prudhoe Bay Data Center | Dalton Hwy | Prudhoe Bay | AK | 99734.0 | North Slope | 70.18478 | ... |

---

### File: `data_centers/global_datacenters_github.csv`

- **Size:** 1679.19 KB
- **Total Rows:** 18,110
- **Total Columns:** 6
- **Category Columns:** *None*
- **Numeric Columns:** *None*
- **Date Columns:** *None*
- **Text Columns:** name, company, city, state, country, address

#### Sample Data (First 3 rows)

| name | company | city | state | country | address |
| --- | --- | --- | --- | --- | --- |
| NAP de las Americas Madrid | Terremark | Madrid | nan | Spain | Calle de Yecora, 4 28009 Madrid Spain |
| Central Office 2 | StarHub Ltd. | Singapore | nan | Singapore | 19 Tai Seng Dr 535222 Singapore Singa... |
| Cluj-Napoca | GTS Telecom SRL | Cluj-Napoca | nan | Romania | Str. Garii nr. 21 400267 Cluj-Napoca ... |

---

### File: `data_centers/hyperscaler_focused_projects.csv`

- **Size:** 9.24 KB
- **Total Rows:** 52
- **Total Columns:** 16
- **Category Columns:** hyperscaler_category, tenant, country, status, capacity_category, expected_online_date, project_cost_usd, purpose
- **Numeric Columns:** capacity_mw
- **Date Columns:** *None*
- **Text Columns:** facility_name, operator, city, state_province, cooling_type, power_source, source_url

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **hyperscaler_category** | 15 | `AWS`, `Aligned`, `Apple`, `Crusoe`, `Google`, `Meta`, `Microsoft`, `NTT`, `Oracle`, `Other/Unclassified`, `Prime Data Centers`, `Stargate`, `Stream Data Centers`, `Vantage`, `xAI` |
| **tenant** | 14 | `$10 billion+`, `$33 billion`, `$40 billion+`, `2026`, `2027`, `2028`, `2032`, `2036`, `AWS`, `Google (unconfirmed)`, `Meta`, `Microsoft`, `OpenAI/Oracle`, `xAI` |
| **country** | 3 | `Norway`, `United Arab Emirates`, `United States` |
| **status** | 7 | `Approved/Permitted/Under construction`, `Expanding`, `Operating`, `Planned`, `Proposed`, `Suspended`, `Under Construction` |
| **capacity_category** | 5 | `Hyperscale (100-999 MW)`, `Large (51-99 MW)`, `Medium (11-50 MW)`, `Mega campus (>1`, `Unknown` |
| **expected_online_date** | 10 | `$10 billion`, `$14 billion`, `$3.6 billion`, `$300 million`, `$6 billion`, `2025`, `2026`, `2027`, `2028`, `250` |
| **project_cost_usd** | 8 | `$10 billion`, `$29 million`, `$8 billion`, `$800 million`, `1218`, `1600`, `290`, `687` |
| **purpose** | 8 | `2027`, `AI/Hyperscale`, `AWS`, `Cloud/AI`, `Google`, `Meta`, `OpenAI/Oracle`, `OpenAI/Oracle/MGX` |

#### Sample Data (First 3 rows)

| hyperscaler_category | facility_name | operator | tenant | city | state_province | country | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Other/Unclassified | Stratos Hyperscale Campus | Bitzero Blockchain Inc. | nan | nan | Utah | United States | ... |
| Other/Unclassified | Monarch Compute Campus | Nscale Ltd. | 2027 | nan | West Virginia | United States | ... |
| Other/Unclassified | GW Ranch | Pacifico Energy | 2027 | nan | Texas | United States | ... |

---

### File: `data_centers/key_hyperscale_projects.csv`

> [!WARNING]
> Failed to analyze CSV file. Error: Error tokenizing data. C error: Expected 19 fields in line 25, saw 20


### File: `data_centers/master_facility_list.csv`

- **Size:** 10.39 KB
- **Total Rows:** 52
- **Total Columns:** 19
- **Category Columns:** tenant, hyperscaler_category, country, status, capacity_category, expected_online_date, purpose, notes, tier
- **Numeric Columns:** capacity_mw, project_cost_usd
- **Date Columns:** *None*
- **Text Columns:** facility_id, facility_name, operator, city, state_province, cooling_type, power_source, source_url

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **tenant** | 14 | `$10 billion+`, `$33 billion`, `$40 billion+`, `2026`, `2027`, `2028`, `2032`, `2036`, `AWS`, `Google (unconfirmed)`, `Meta`, `Microsoft`, `OpenAI/Oracle`, `xAI` |
| **hyperscaler_category** | 15 | `AWS`, `Aligned`, `Apple`, `Crusoe`, `Google`, `Meta`, `Microsoft`, `NTT`, `Oracle`, `Other/Unclassified`, `Prime Data Centers`, `Stargate`, `Stream Data Centers`, `Vantage`, `xAI` |
| **country** | 3 | `Norway`, `United Arab Emirates`, `United States` |
| **status** | 5 | `Expanding`, `Operating`, `Planned`, `Suspended`, `Under Construction` |
| **capacity_category** | 5 | `Hyperscale (100-999 MW)`, `Large (51-99 MW)`, `Medium (11-50 MW)`, `Mega campus (>1`, `Unknown` |
| **expected_online_date** | 10 | `$10 billion`, `$14 billion`, `$3.6 billion`, `$300 million`, `$6 billion`, `2025`, `2026`, `2027`, `2028`, `250` |
| **purpose** | 8 | `2027`, `AI/Hyperscale`, `AWS`, `Cloud/AI`, `Google`, `Meta`, `OpenAI/Oracle`, `OpenAI/Oracle/MGX` |
| **notes** | 13 | `1,300 acres`, `100 gas generators, 862MWh BESS`, `100% renewable, recycled water`, `100k GPUs`, `100k GPUs by 2026`, `3 of 5 buildings broke ground`, `AI/Cloud`, `AI/Hyperscale`, `Building 4 268MW, Bldg 2 260MW`, `Cloud/AI`, `Community opposition`, `Phase 1 approved`, `Water concerns, 31M gal/yr` |
| **tier** | 3 | `Tier 1`, `Tier 2`, `Tier 3` |

#### Sample Data (First 3 rows)

| facility_id | facility_name | operator | tenant | hyperscaler_category | city | state_province | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DC-00001 | Stratos Hyperscale Campus | Bitzero Blockchain Inc. | nan | Other/Unclassified | nan | Utah | ... |
| DC-00002 | Monarch Compute Campus | Nscale Ltd. | 2027 | Other/Unclassified | nan | West Virginia | ... |
| DC-00003 | GW Ranch | Pacifico Energy | 2027 | Other/Unclassified | nan | Texas | ... |

---

### File: `data_centers/master_facility_list_v2.csv`

- **Size:** 10.57 KB
- **Total Rows:** 52
- **Total Columns:** 21
- **Category Columns:** tenant, country, status, capacity_category, expected_online_date, purpose, notes, tier
- **Numeric Columns:** latitude, longitude, capacity_mw, project_cost_usd
- **Date Columns:** *None*
- **Text Columns:** facility_id, facility_name, operator, hyperscaler_category, city, state_province, cooling_type, power_source, source_url

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **tenant** | 14 | `$10 billion+`, `$33 billion`, `$40 billion+`, `2026`, `2027`, `2028`, `2032`, `2036`, `AWS`, `Google (unconfirmed)`, `Meta`, `Microsoft`, `OpenAI/Oracle`, `xAI` |
| **country** | 3 | `Norway`, `United Arab Emirates`, `United States` |
| **status** | 5 | `Expanding`, `Operating`, `Planned`, `Suspended`, `Under Construction` |
| **capacity_category** | 5 | `Hyperscale (100-999 MW)`, `Large (51-99 MW)`, `Medium (11-50 MW)`, `Mega campus (>1`, `Unknown` |
| **expected_online_date** | 10 | `$10 billion`, `$14 billion`, `$3.6 billion`, `$300 million`, `$6 billion`, `2025`, `2026`, `2027`, `2028`, `250` |
| **purpose** | 8 | `2027`, `AI/Hyperscale`, `AWS`, `Cloud/AI`, `Google`, `Meta`, `OpenAI/Oracle`, `OpenAI/Oracle/MGX` |
| **notes** | 13 | `1,300 acres`, `100 gas generators, 862MWh BESS`, `100% renewable, recycled water`, `100k GPUs`, `100k GPUs by 2026`, `3 of 5 buildings broke ground`, `AI/Cloud`, `AI/Hyperscale`, `Building 4 268MW, Bldg 2 260MW`, `Cloud/AI`, `Community opposition`, `Phase 1 approved`, `Water concerns, 31M gal/yr` |
| **tier** | 3 | `Tier 1`, `Tier 2`, `Tier 3` |

#### Sample Data (First 3 rows)

| facility_id | facility_name | operator | tenant | hyperscaler_category | city | state_province | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DC-00001 | Stratos Hyperscale Campus | Bitzero Blockchain Inc. | nan | Bitzero | nan | Utah | ... |
| DC-00002 | Monarch Compute Campus | Nscale Ltd. | 2027 | Nscale | nan | West Virginia | ... |
| DC-00003 | GW Ranch | Pacifico Energy | 2027 | Pacifico Energy | nan | Texas | ... |

---

### File: `data_centers/master_facility_list_v3_enriched.csv`

- **Size:** 22.01 KB
- **Total Rows:** 52
- **Total Columns:** 53
- **Category Columns:** tenant, hyperscaler_category, country, status, capacity_category, expected_online_date, purpose, notes, tier, utility, generation_mix, cooling_detail, network_detail, gpu_generation, primary_gpu
- **Numeric Columns:** capacity_mw, project_cost_usd, it_load_mw, est_gpus_h100, est_gpus_b200, est_gpus_mi300x, est_gpus_gb200_nvl72, est_racks_50kw, est_racks_100kw, est_bf16_pflops, est_fp8_pflops, voltage_kv, ppa_price_mwh, water_source_mgd, cluster_size, total_capex_billion, est_capex_per_kw, est_capex_per_gpu, est_gpu_count, training_bf16_pflops, inference_fp8_pflops, est_tokens_per_sec_billions, est_training_runs_per_year_gpt4_class, annual_power_mwh, annual_power_cost_usd, annual_revenue_potential_usd, power_cost_per_gpu_per_year, latitude, longitude
- **Date Columns:** *None*
- **Text Columns:** facility_id, facility_name, operator, city, state_province, cooling_type, power_source, source_url, source_notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **tenant** | 14 | `$10 billion+`, `$33 billion`, `$40 billion+`, `2026`, `2027`, `2028`, `2032`, `2036`, `AWS`, `Google (unconfirmed)`, `Meta`, `Microsoft`, `OpenAI/Oracle`, `xAI` |
| **hyperscaler_category** | 15 | `AWS`, `Aligned`, `Apple`, `Crusoe`, `Google`, `Meta`, `Microsoft`, `NTT`, `Oracle`, `Other/Unclassified`, `Prime Data Centers`, `Stargate`, `Stream Data Centers`, `Vantage`, `xAI` |
| **country** | 3 | `Norway`, `United Arab Emirates`, `United States` |
| **status** | 5 | `Expanding`, `Operating`, `Planned`, `Suspended`, `Under Construction` |
| **capacity_category** | 5 | `Hyperscale (100-999 MW)`, `Large (51-99 MW)`, `Medium (11-50 MW)`, `Mega campus (>1`, `Unknown` |
| **expected_online_date** | 10 | `$10 billion`, `$14 billion`, `$3.6 billion`, `$300 million`, `$6 billion`, `2025`, `2026`, `2027`, `2028`, `250` |
| **purpose** | 8 | `2027`, `AI/Hyperscale`, `AWS`, `Cloud/AI`, `Google`, `Meta`, `OpenAI/Oracle`, `OpenAI/Oracle/MGX` |
| **notes** | 13 | `1,300 acres`, `100 gas generators, 862MWh BESS`, `100% renewable, recycled water`, `100k GPUs`, `100k GPUs by 2026`, `3 of 5 buildings broke ground`, `AI/Cloud`, `AI/Hyperscale`, `Building 4 268MW, Bldg 2 260MW`, `Cloud/AI`, `Community opposition`, `Phase 1 approved`, `Water concerns, 31M gal/yr` |
| **tier** | 3 | `Tier 1`, `Tier 2`, `Tier 3` |
| **utility** | 7 | `Entergy Arkansas`, `Entergy Louisiana`, `Georgia Power / Southern Company`, `IID / CAISO`, `Oncor / ERCOT`, `PG&E`, `PacifiCorp / WAPA` |
| **generation_mix** | 7 | `Gas 40%, Nuclear 30%, Coal 15%, Renewable 15%`, `Gas 50%, Nuclear 25%, Renewable 25%`, `Gas 60%, Nuclear 25%, Renewable 15%`, `Solar 30%, Hydro 25%, Gas 25%, Nuclear 15%, Wind 5%`, `Solar 50%, Geothermal 20%, Gas 30%`, `Wind 35%, Solar 25%, Gas 30%, Nuclear 10%`, `Wind 50%, Gas 30%, Coal 20%` |
| **cooling_detail** | 7 | `Direct liquid cooling (DLC)`, `Direct liquid cooling (DLC) 100%`, `Direct-to-chip liquid (80%) + rear-door (20%)`, `Direct-to-chip liquid (TPU pods)`, `Hybrid air/liquid, 100 gas generators + 862MWh BESS`, `Hybrid air/water, 95% free cooling`, `Rear-door heat exchanger + liquid assist` |
| **network_detail** | 7 | `100G/400G to San Jose/Sacramento`, `400G/800G to Denver/Salt Lake`, `Custom optical circuit switching, 1.6T regional`, `InfiniBand NDR 400G, 800G to Chicago/Dallas`, `InfiniBand NDR, 800G to LA/San Diego`, `NVL72 + InfiniBand NDR 400G, 800G ZR+ to Atlanta/Dallas`, `NVL72 + InfiniBand NDR, 1.6T to Dallas` |
| **gpu_generation** | 8 | `GB200 NVL72`, `GB200 NVL72 / GB300`, `H100 (2025), B200 (2026+)`, `H100 / B200`, `H100 / Maia 100`, `H100 / TPU v5`, `TPU v5p / v6`, `Trainium2 / Inferentia2` |
| **primary_gpu** | 6 | `B200`, `GB200 NVL72`, `H100`, `H100 (est.)`, `TPU v5p/v6`, `Trainium2/Inferentia2` |

#### Sample Data (First 3 rows)

| facility_id | facility_name | operator | tenant | hyperscaler_category | city | state_province | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DC-00001 | Stratos Hyperscale Campus | Bitzero Blockchain Inc. | nan | Other/Unclassified | nan | Utah | ... |
| DC-00002 | Monarch Compute Campus | Nscale Ltd. | 2027 | Other/Unclassified | nan | West Virginia | ... |
| DC-00003 | GW Ranch | Pacifico Energy | 2027 | Other/Unclassified | nan | Texas | ... |

---

### File: `data_centers/master_global_datacenters.csv`

- **Size:** 2993.55 KB
- **Total Rows:** 19,694
- **Total Columns:** 25
- **Category Columns:** source, status, capacity_category, cooling_type, power_source, tenant, purpose, community_pushback
- **Numeric Columns:** capacity_mw, property_size_acres, expected_online_date, latitude, longitude
- **Date Columns:** date_added, last_updated
- **Text Columns:** facility_name, operator, city, state_province, country, address, facility_size_sqft, project_cost_usd, notes, source_url

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **source** | 4 | `DCMap_Pipeline`, `DataCenterMap`, `FracTracker_US`, `GitHub_GlobalMap` |
| **status** | 8 | `Cancelled`, `Expanding`, `Operating`, `Planned`, `Pre-proposal`, `Reference`, `Suspended`, `Under Construction` |
| **capacity_category** | 22 | `Hyperscale (100-999 MW)`, `Hyperscale (101-999 MW)`, `Large (51-99 MW)`, `Medium (11-50 MW)`, `Mega campus (>1,000 MW)`, `Small (0-10 MW)`, `Total facilities: 186`, `Total facilities: 188`, `Total facilities: 212`, `Total facilities: 215`, `Total facilities: 259`, `Total facilities: 260`, `Total facilities: 286`, `Total facilities: 289`, `Total facilities: 298` ... (and more) |
| **cooling_type** | 3 | `Closed loop`, `Fans`, `Open loop` |
| **power_source** | 21 | `Biomass`, `Coal`, `Coal, Natural gas, Biomass`, `Fuel Cells`, `Grid (unspecified mix)`, `Grid (unspecified mix), Biomass`, `Grid (unspecified mix), Solar`, `Hybrid (onsite and grid)`, `Hydroelectric`, `Hydroelectric, Grid (unspecified mix)`, `Natural gas`, `Natural gas, Hybrid (onsite and grid)`, `Natural gas, Nuclear, Solar`, `Nuclear`, `Nuclear, Solar, Geothermal, Grid (unspecified mix)` ... (and more) |
| **tenant** | 2 | `Anthropic`, `Multiple colocation tenants` |
| **purpose** | 29 | `AI`, `AI "superfactory"`, `AI / hyperscale data center`, `AI Data center and solar fam`, `AI and Bitcoin`, `AI and Cloud Computing`, `AI data center / hyperscale campus`, `AI for Nuclear Research`, `AI/Hyperscale`, `AI/cloud-computing`, `Bitcoin`, `Bitcoin transitioning to AI`, `Colocation / enterprise data center`, `Colocation data center`, `Country-level aggregate` ... (and more) |
| **community_pushback** | 2 | `Unknown`, `Yes` |

#### Sample Data (First 3 rows)

| source | facility_name | operator | city | state_province | country | address | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub_GlobalMap | NAP de las Americas Madrid | Terremark | Madrid | nan | Spain | Calle de Yecora, 4 28009 Madrid Spain | ... |
| GitHub_GlobalMap | Central Office 2 | StarHub Ltd. | Singapore | nan | Singapore | 19 Tai Seng Dr 535222 Singapore Singa... | ... |
| GitHub_GlobalMap | Cluj-Napoca | GTS Telecom SRL | Cluj-Napoca | nan | Romania | Str. Garii nr. 21 400267 Cluj-Napoca ... | ... |

---

### File: `data_centers/module_17_enterprise_contract_lag.csv`

- **Size:** 2.67 KB
- **Total Rows:** 11
- **Total Columns:** 9
- **Category Columns:** module, metric, unit, source, source_url, confidence, notes
- **Numeric Columns:** value
- **Date Columns:** date_accessed
- **Text Columns:** *None*

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **module** | 1 | `Enterprise_Contract_Lag` |
| **metric** | 11 | `average_contract_length`, `average_pilot_duration_months`, `capacity_block_duration_aws_google_azure`, `contract_lag_to_revenue_recognition_months`, `contract_renewal_window_months_before_expiry`, `enterprise_ai_budget_committed_vs_experimental`, `enterprise_ai_pilot_to_production_rate`, `gpu_reservation_lead_time_months`, `on_demand_share_of_hyperscaler_revenue`, `renewal_rate_hyperscaler_cloud`, `reserved_capacity_share_of_hyperscaler_revenue` |
| **unit** | 3 | `months`, `percent`, `years` |
| **source** | 11 | `ASC 606 revenue recognition; hyperscaler earnings calls Q4 2025`, `AWS Capacity Blocks docs; Google Cloud Future Reservations; Azure Reserved Instances`, `Deloitte State of AI in Enterprise 2025; Gartner AI Pilot Survey 2025`, `Gartner IT Spending Forecast 2025; Flexera State of Cloud Report 2025`, `McKinsey State of AI 2025; IDC AI Adoption Tracker 2025`, `Morgan Stanley CIO Survey 2025; Piper Sandler IT Spend Survey 2025`, `NVIDIA H100/B200 allocation reports; CoreWeave/lambda capacity blocks`, `Salesforce 10-K FY2024; Microsoft 10-K FY2024; Google 10-K FY2024`, `Synergy Research Group 2025; KeyBanc Capital Markets Cloud Survey 2025`, `Synergy Research Group Q4 2025`, `Synergy Research Group Q4 2025; Canalys Cloud Channels Analysis 2025` |
| **source_url** | 9 | `https://aws.amazon.com`, `https://www.deloitte.com`, `https://www.fasb.org`, `https://www.gartner.com`, `https://www.mckinsey.com`, `https://www.morganstanley.com`, `https://www.nvidia.com`, `https://www.sec.gov/edgar`, `https://www.synergyresearch.com` |
| **confidence** | 2 | `High`, `Medium` |
| **notes** | 9 | `1-3 year committed capacity blocks standard for AI workloads`, `70% of AI budget in committed contracts vs 30% experimental`, `Enterprise cloud agreements typically 3-year committed spend`, `GPU capacity blocks require 3-9 month advance reservation`, `Net revenue retention >130% for major hyperscalers`, `Only 12% of AI pilots reach production (88% failure rate per Forrester 2026)`, `Renewal negotiations typically start 6-12 months before expiry`, `Reserved instances / committed use discounts dominate hyperscaler revenue`, `Revenue recognized ratably over contract term; 3-month lag typical` |

#### Sample Data (First 3 rows)

| module | metric | value | unit | source | source_url | date_accessed | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Enterprise_Contract_Lag | average_contract_length | 3 | years | Salesforce 10-K FY2024; Microsoft 10-... | https://www.sec.gov/edgar | 2026-07-14 | ... |
| Enterprise_Contract_Lag | contract_renewal_window_months_before... | 6 | months | Gartner IT Spending Forecast 2025; Fl... | https://www.gartner.com | 2026-07-14 | ... |
| Enterprise_Contract_Lag | reserved_capacity_share_of_hyperscale... | 0.65 | percent | Synergy Research Group Q4 2025; Canal... | https://www.synergyresearch.com | 2026-07-14 | ... |

---

### File: `data_centers/module_18_agentic_liability_compliance.csv`

> [!WARNING]
> Failed to analyze CSV file. Error: Error tokenizing data. C error: Expected 9 fields in line 9, saw 10


### File: `data_centers/module_19_physical_infra_constraints.csv`

- **Size:** 7.33 KB
- **Total Rows:** 34
- **Total Columns:** 9
- **Category Columns:** module, unit, confidence
- **Numeric Columns:** value
- **Date Columns:** date_accessed
- **Text Columns:** metric, source, source_url, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **module** | 1 | `Physical_Infra_Constraints` |
| **unit** | 12 | `GB`, `GW`, `MW_per_MGD`, `USD`, `WPM`, `count`, `months`, `percent`, `ratio`, `units`, `weeks`, `year` |
| **confidence** | 3 | `High`, `Low`, `Medium` |

#### Sample Data (First 3 rows)

| module | metric | value | unit | source | source_url | date_accessed | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Physical_Infra_Constraints | us_grid_connection_queue_gw | 2600.0 | GW | LBNL Queued Up 2024; PJM/ERCOT/CAISO/... | https://queuedup.lbl.gov | 2026-07-14 | ... |
| Physical_Infra_Constraints | us_data_center_queue_gw | 300.0 | GW | LBNL Queued Up 2024 (filtered for dat... | https://queuedup.lbl.gov | 2026-07-14 | ... |
| Physical_Infra_Constraints | transformer_lead_time_weeks | 128.0 | weeks | Wood Mackenzie Q2 2025 Transformer Su... | https://www.woodmac.com | 2026-07-14 | ... |

---

### File: `data_centers/module_20_systems_dynamics.csv`

- **Size:** 16.92 KB
- **Total Rows:** 81
- **Total Columns:** 9
- **Category Columns:** module, unit, confidence
- **Numeric Columns:** value
- **Date Columns:** date_accessed
- **Text Columns:** metric, source, source_url, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **module** | 1 | `Systems_Dynamics` |
| **unit** | 7 | `GW`, `USD_B`, `USD_M`, `USD_T`, `count`, `months`, `ratio` |
| **confidence** | 3 | `High`, `Low`, `Medium` |

#### Sample Data (First 3 rows)

| module | metric | value | unit | source | source_url | date_accessed | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Systems_Dynamics | ai_capex_to_revenue_ratio_hyperscalers | 0.52 | ratio | American Century Investments 2026; In... | https://www.americancentury.com | 2026-07-14 | ... |
| Systems_Dynamics | ai_capex_growth_rate_2025_yoy | 0.73 | ratio | Introl Blog 2026; Company earnings 2025 | https://blakecrosley.com | 2026-07-14 | ... |
| Systems_Dynamics | ai_capex_2026_projected_billion_usd | 602.0 | USD_B | Introl Blog 2026; Goldman Sachs 2025;... | https://blakecrosley.com | 2026-07-14 | ... |

---

### File: `data_centers/module_21_jevons_paradox.csv`

- **Size:** 5.57 KB
- **Total Rows:** 26
- **Total Columns:** 9
- **Category Columns:** module, unit, source_url, confidence
- **Numeric Columns:** value
- **Date Columns:** date_accessed
- **Text Columns:** metric, source, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **module** | 1 | `Jevons_Paradox` |
| **unit** | 3 | `USD`, `USD_B`, `ratio` |
| **source_url** | 13 | `https://agentmarketcap.ai`, `https://arxiv.org`, `https://deepmind.google`, `https://developer.nvidia.com`, `https://epochai.org`, `https://github.com/apache/tvm`, `https://llmcompare.dev`, `https://openrouter.ai`, `https://www.digitalapplied.com`, `https://www.groq.com`, `https://www.idc.com`, `https://www.nvidia.com`, `https://www.semianalysis.com` |
| **confidence** | 3 | `High`, `Low`, `Medium` |

#### Sample Data (First 3 rows)

| module | metric | value | unit | source | source_url | date_accessed | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Jevons_Paradox | inference_cost_reduction_rate_annual_pct | 0.5 | ratio | LLMCompare 2026; LLM Pricing Trends 2... | https://llmcompare.dev | 2026-07-14 | ... |
| Jevons_Paradox | training_cost_reduction_rate_annual_pct | 0.4 | ratio | Epoch AI 2025; SemiAnalysis training ... | https://epochai.org | 2026-07-14 | ... |
| Jevons_Paradox | hardware_utilization_improvement_rate... | 0.3 | ratio | NVIDIA Hopper/Blackwell architecture;... | https://www.nvidia.com | 2026-07-14 | ... |

---

### File: `data_centers/module_22_open_source_commoditization.csv`

- **Size:** 5.94 KB
- **Total Rows:** 28
- **Total Columns:** 9
- **Category Columns:** module, unit, source_url, confidence
- **Numeric Columns:** value
- **Date Columns:** date_accessed
- **Text Columns:** metric, source, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **module** | 1 | `Open_Source_Commoditization` |
| **unit** | 6 | `USD`, `USD_M`, `count`, `date`, `points`, `ratio` |
| **source_url** | 11 | `https://ai.meta.com`, `https://alphacorp.ai`, `https://amirteymoori.com`, `https://artificialanalysis.ai`, `https://chinaapi.ai`, `https://github.com/THUDM/GLM-4`, `https://huggingface.co`, `https://llmcompare.dev`, `https://precisionaiacademy.com`, `https://pricepertoken.com`, `https://whatllm.org` |
| **confidence** | 2 | `High`, `Medium` |

#### Sample Data (First 3 rows)

| module | metric | value | unit | source | source_url | date_accessed | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Open_Source_Commoditization | open_source_model_count_2025 | 59 | count | WhatLLM 2025; Artificial Analysis 2026 | https://whatllm.org | 2026-07-14 | ... |
| Open_Source_Commoditization | open_source_share_pct | 0.63 | ratio | WhatLLM 2025 | https://whatllm.org | 2026-07-14 | ... |
| Open_Source_Commoditization | quality_gap_open_vs_closed_2025_points | 7 | points | WhatLLM 2025; Artificial Analysis 2026 | https://whatllm.org | 2026-07-14 | ... |

---

### File: `data_centers/module_23_compute_supply_cycle.csv`

- **Size:** 5.23 KB
- **Total Rows:** 24
- **Total Columns:** 9
- **Category Columns:** module, unit, source_url, confidence
- **Numeric Columns:** value
- **Date Columns:** date_accessed
- **Text Columns:** metric, source, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **module** | 1 | `Compute_Supply_Cycle` |
| **unit** | 9 | `GB`, `USD_B`, `boolean`, `category`, `days`, `months`, `ratio`, `weeks`, `wpm` |
| **source_url** | 14 | `https://agentmarketcap.ai`, `https://blakecrosley.com`, `https://gpuaas.com`, `https://semianalysis.com`, `https://www.amazonaws.com`, `https://www.cbre.com`, `https://www.marvell.com`, `https://www.nvidia.com`, `https://www.semiconductors.org`, `https://www.skhynix.com`, `https://www.telegeography.com`, `https://www.trendforce.com`, `https://www.tsmc.com`, `https://www.vertiv.com` |
| **confidence** | 3 | `High`, `Low`, `Medium` |

#### Sample Data (First 3 rows)

| module | metric | value | unit | source | source_url | date_accessed | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Compute_Supply_Cycle | gpu_order_to_delivery_lead_time_months | 6 | months | NVIDIA earnings calls 2025; SemiAnaly... | https://www.nvidia.com | 2026-07-14 | ... |
| Compute_Supply_Cycle | wafer_allocation_nvidia_pct_tsmc_5nm | 0.60 | ratio | SemiAnalysis 2025; TSMC earnings call... | https://www.tsmc.com | 2026-07-14 | ... |
| Compute_Supply_Cycle | cowos_monthly_capacity_2024_wpm | 35000 | wpm | TrendForce 2024; TSMC earnings 2024 | https://www.trendforce.com | 2026-07-14 | ... |

---

### File: `data_centers/module_24_capital_market_reflexivity.csv`

- **Size:** 4.10 KB
- **Total Rows:** 17
- **Total Columns:** 9
- **Category Columns:** module, unit, source_url, confidence
- **Numeric Columns:** value
- **Date Columns:** date_accessed
- **Text Columns:** metric, source, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **module** | 1 | `Capital_Market_Reflexivity` |
| **unit** | 4 | `USD`, `USD_B`, `quarters`, `ratio` |
| **source_url** | 12 | `https://agentmarketcap.ai`, `https://blakecrosley.com`, `https://intuitionlabs.ai`, `https://www.americancentury.com`, `https://www.bloomberg.com`, `https://www.cboe.com`, `https://www.epfr.com`, `https://www.factset.com`, `https://www.finra.org`, `https://www.morganstanley.com`, `https://www.spdji.com`, `https://www.spglobal.com` |
| **confidence** | 3 | `High`, `Low`, `Medium` |

#### Sample Data (First 3 rows)

| module | metric | value | unit | source | source_url | date_accessed | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Capital_Market_Reflexivity | valuation_to_funding_cost_elasticity | 0.35 | ratio | Morgan Stanley 2026; American Century... | https://www.morganstanley.com | 2026-07-14 | ... |
| Capital_Market_Reflexivity | capex_to_revenue_sensitivity_hypersca... | 0.35 | ratio | Morgan Stanley 2026; American Century... | https://www.morganstanley.com | 2026-07-14 | ... |
| Capital_Market_Reflexivity | downward_deleveraging_multiplier | 2.5 | ratio | Morgan Stanley 2026; American Century... | https://www.morganstanley.com | 2026-07-14 | ... |

---

### File: `data_centers/module_25_revenue_quality.csv`

- **Size:** 5.77 KB
- **Total Rows:** 27
- **Total Columns:** 9
- **Category Columns:** module, unit, source_url, confidence
- **Numeric Columns:** value
- **Date Columns:** date_accessed
- **Text Columns:** metric, source, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **module** | 1 | `Revenue_Quality` |
| **unit** | 3 | `count`, `points`, `ratio` |
| **source_url** | 12 | `https://aws.amazon.com`, `https://dcmap.us`, `https://gpuaas.com`, `https://menlovc.com`, `https://sacra.com`, `https://tenki.cloud`, `https://www.bvp.com`, `https://www.equinix.com`, `https://www.flexera.com`, `https://www.keybanc.com`, `https://www.sec.gov`, `https://www.together.ai` |
| **confidence** | 3 | `High`, `Low`, `Medium` |

#### Sample Data (First 3 rows)

| module | metric | value | unit | source | source_url | date_accessed | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue_Quality | high_quality_revenue_pct_hyperscalers | 0.65 | ratio | KeyBanc SaaS Survey 2025; ICONIQ 2025... | https://www.keybanc.com | 2026-07-14 | ... |
| Revenue_Quality | medium_quality_revenue_pct_hyperscalers | 0.25 | ratio | KeyBanc SaaS Survey 2025; ICONIQ 2025 | https://www.keybanc.com | 2026-07-14 | ... |
| Revenue_Quality | low_quality_revenue_pct_hyperscalers | 0.1 | ratio | KeyBanc SaaS Survey 2025; ICONIQ 2025 | https://www.keybanc.com | 2026-07-14 | ... |

---

### File: `data_centers/module_26_national_strategic_investment.csv`

- **Size:** 6.20 KB
- **Total Rows:** 25
- **Total Columns:** 9
- **Category Columns:** module, unit, confidence
- **Numeric Columns:** value
- **Date Columns:** date_accessed
- **Text Columns:** metric, source, source_url, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **module** | 1 | `National_Strategic_Investment` |
| **unit** | 7 | `EUR_B`, `GBP_B`, `SGD_M`, `USD_B`, `boolean`, `count`, `ratio` |
| **confidence** | 2 | `High`, `Medium` |

#### Sample Data (First 3 rows)

| module | metric | value | unit | source | source_url | date_accessed | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| National_Strategic_Investment | us_chips_act_total_funding_billion_usd | 52.7 | USD_B | CHIPS and Science Act 2022; Commerce ... | https://www.commerce.gov | 2026-07-14 | ... |
| National_Strategic_Investment | us_chips_act_disbursed_2025_billion_usd | 15.0 | USD_B | Commerce Dept CHIPS Program Office 20... | https://www.chips.gov | 2026-07-14 | ... |
| National_Strategic_Investment | us_chips_act_private_investment_lever... | 450.0 | USD_B | SIA 2025 CHIPS Act Impact Report; S&P... | https://www.semiconductors.org | 2026-07-14 | ... |

---

### File: `data_centers/module_27_labor_market_transformation.csv`

- **Size:** 6.46 KB
- **Total Rows:** 29
- **Total Columns:** 9
- **Category Columns:** module, unit, source_url, confidence
- **Numeric Columns:** value
- **Date Columns:** date_accessed
- **Text Columns:** metric, source, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **module** | 1 | `Labor_Market_Transformation` |
| **unit** | 6 | `USD`, `USD_B`, `date`, `millions`, `months`, `ratio` |
| **source_url** | 15 | `https://agentmarketcap.ai`, `https://hai.stanford.edu`, `https://mindstudio.ai`, `https://www.anthropic.com`, `https://www.bls.gov`, `https://www.deloitte.com`, `https://www.federalreserve.gov`, `https://www.goldmansachs.com`, `https://www.imf.org`, `https://www.mckinsey.com`, `https://www.mindstudio.ai`, `https://www.nber.org`, `https://www.science.org`, `https://www.swfte.com`, `https://www.weforum.org` |
| **confidence** | 3 | `High`, `Low`, `Medium` |

#### Sample Data (First 3 rows)

| module | metric | value | unit | source | source_url | date_accessed | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Labor_Market_Transformation | us_jobs_displaced_by_ai_2025_millions | 1.5 | millions | Goldman Sachs 2026; McKinsey 2025; IM... | https://www.goldmansachs.com | 2026-07-14 | ... |
| Labor_Market_Transformation | us_jobs_augmented_by_ai_2025_millions | 12.0 | millions | McKinsey 2025; Goldman Sachs 2026 | https://www.mckinsey.com | 2026-07-14 | ... |
| Labor_Market_Transformation | global_jobs_displaced_by_ai_2030_mill... | 83.0 | millions | IMF 2025; WEF Future of Jobs 2025 | https://www.imf.org | 2026-07-14 | ... |

---

### File: `data_centers/module_28_regulatory_scenario.csv`

- **Size:** 6.12 KB
- **Total Rows:** 28
- **Total Columns:** 9
- **Category Columns:** module, unit, confidence
- **Numeric Columns:** *None*
- **Date Columns:** date_accessed
- **Text Columns:** metric, value, source, source_url, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **module** | 1 | `Regulatory_Scenario` |
| **unit** | 9 | `EUR_B`, `USD`, `USD_B`, `USD_M`, `boolean`, `category`, `count`, `date`, `ratio` |
| **confidence** | 2 | `High`, `Medium` |

#### Sample Data (First 3 rows)

| module | metric | value | unit | source | source_url | date_accessed | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Regulatory_Scenario | eu_ai_act_effective_date | 2025-08-01 | date | Official Journal EU 2024; EUR-Lex 320... | https://eur-lex.europa.eu | 2026-07-14 | ... |
| Regulatory_Scenario | eu_ai_act_high_risk_compliance_deadline | 2026-08-02 | date | EU AI Act Article 113; European Commi... | https://ec.europa.eu | 2026-07-14 | ... |
| Regulatory_Scenario | eu_ai_act_gpai_compliance_deadline | 2025-08-02 | date | EU AI Act Article 113; GPAI Code of P... | https://ec.europa.eu | 2026-07-14 | ... |

---

### File: `data_centers/module_29_ai_adoption_diffusion.csv`

- **Size:** 10.75 KB
- **Total Rows:** 52
- **Total Columns:** 9
- **Category Columns:** module, unit, source_url, confidence
- **Numeric Columns:** value
- **Date Columns:** date_accessed
- **Text Columns:** metric, source, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **module** | 1 | `AI_Adoption_Diffusion` |
| **unit** | 5 | `USD_B`, `USD_M`, `date`, `months`, `ratio` |
| **source_url** | 10 | `https://aiindex.stanford.edu`, `https://menlovc.com`, `https://www.bassmodel.com`, `https://www.deloitte.com`, `https://www.gartner.com`, `https://www.idc.com`, `https://www.mckinsey.com`, `https://www.microsoft.com`, `https://www.swfte.com`, `https://www.writer.com` |
| **confidence** | 3 | `High`, `Low`, `Medium` |

#### Sample Data (First 3 rows)

| module | metric | value | unit | source | source_url | date_accessed | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AI_Adoption_Diffusion | consumer_ai_users_global_billion | 1.75 | USD_B | Menlo Ventures Consumer AI 2025; Stan... | https://menlovc.com | 2026-07-14 | ... |
| AI_Adoption_Diffusion | us_adult_ai_usage_6month_pct | 0.61 | ratio | Menlo Ventures 2025 (5,031 US adults ... | https://menlovc.com | 2026-07-14 | ... |
| AI_Adoption_Diffusion | enterprise_ai_adoption_pct | 0.88 | ratio | McKinsey State of AI 2025; Microsoft ... | https://www.mckinsey.com | 2026-07-14 | ... |

---

### File: `data_centers/module_30_global_macro_feedback.csv`

- **Size:** 8.01 KB
- **Total Rows:** 39
- **Total Columns:** 9
- **Category Columns:** module, unit, confidence
- **Numeric Columns:** value
- **Date Columns:** date_accessed
- **Text Columns:** metric, source, source_url, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **module** | 1 | `Global_Macro_Feedback` |
| **unit** | 8 | `GW`, `TWh`, `USD`, `USD_B`, `USD_T`, `bps`, `percent`, `ratio` |
| **confidence** | 2 | `High`, `Medium` |

#### Sample Data (First 3 rows)

| module | metric | value | unit | source | source_url | date_accessed | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Global_Macro_Feedback | global_gdp_growth_2025_pct | 3.3 | percent | IMF WEO Oct 2025; World Bank Jan 2026 | https://www.imf.org | 2026-07-14 | ... |
| Global_Macro_Feedback | global_gdp_growth_2026_pct | 3.0 | percent | IMF WEO Update Jan 2026; IMF WEO Apr ... | https://www.imf.org | 2026-07-14 | ... |
| Global_Macro_Feedback | global_gdp_growth_2027_pct | 3.4 | percent | IMF WEO Update Jan 2026 | https://www.imf.org | 2026-07-14 | ... |

---

### File: `data_centers/module_31_black_swan_stress_test.csv`

- **Size:** 9.90 KB
- **Total Rows:** 49
- **Total Columns:** 9
- **Category Columns:** module, unit, confidence
- **Numeric Columns:** value
- **Date Columns:** date_accessed
- **Text Columns:** metric, source, source_url, notes

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **module** | 7 | `# Combined scenario weights (must sum to 1.0)`, `# Combined stress test: simultaneous shocks`, `# Stress Test Scenarios (quantified)`, `Black_Swan_Stress_Test`, `Scenario_Weights`, `Stress_Test_Combined`, `Stress_Test_Scenario` |
| **unit** | 3 | `USD_B`, `months`, `ratio` |
| **confidence** | 5 | `Capex cut 70% (credit freeze + demand collapse + supply disruption)`, `High`, `Low`, `Medium`, `Very_Low` |

#### Sample Data (First 3 rows)

| module | metric | value | unit | source | source_url | date_accessed | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Black_Swan_Stress_Test | global_recession_probability_annual | 0.15 | ratio | IMF 2026; OECD 2026; Historical frequ... | https://www.imf.org | 2026-07-14 | ... |
| Black_Swan_Stress_Test | global_recession_gdp_decline_pct | 0.035 | ratio | IMF 2026; Historical average 1960-2024 | https://www.imf.org | 2026-07-14 | ... |
| Black_Swan_Stress_Test | energy_crisis_probability_annual | 0.05 | ratio | IEA 2026; Historical 1973, 1979, 1990... | https://www.iea.org | 2026-07-14 | ... |

---

### File: `fractracker_us_datacenters.csv`

- **Size:** 711.25 KB
- **Total Rows:** 1,603
- **Total Columns:** 44
- **Category Columns:** state, status, location_confidence, purpose, tenant, sizerank, power_source, dedicated_power_plant, number_of_generators, cooling_source, cooling_type, community_pushback, advocacy_information, resistance_status, nda, community_group_website_2, information_source, info_source_5, info_source_6, info_source_7, info_source_8
- **Numeric Columns:** zip, lat, long, mw, number_of_buildings, property_size_acres, expected_date_online
- **Date Columns:** date_created, date_updated
- **Text Columns:** facility_name, address, city, county, operator_name, facility_size_sqft, project_cost, community_group_website_1, petition_url, other_info, info_source_1, info_source_2, info_source_3, info_source_4

#### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **state** | 51 | `AK`, `AL`, `AR`, `AZ`, `CA`, `CO`, `CT`, `DE`, `FL`, `GA`, `HI`, `IA`, `ID`, `IL`, `IN` ... (and more) |
| **status** | 7 | `Approved/Permitted/Under construction`, `Cancelled`, `Expanding`, `Operating`, `Pre-proposal`, `Proposed`, `Suspended` |
| **location_confidence** | 6 | `High`, `High `, `Low`, `Medium`, `Medium `, `high ` |
| **purpose** | 27 | ` Multi-tenant industrial park, flex logistics space, and high-density data center facilities`, `AI`, `AI "superfactory"`, `AI / hyperscale data center`, `AI Data center and solar fam`, `AI and Bitcoin`, `AI and Cloud Computing`, `AI data center / hyperscale campus`, `AI for Nuclear Research`, `AI/cloud-computing`, `Bitcoin`, `Bitcoin transitioning to AI`, `Colocation / enterprise data center`, `Colocation data center`, `Crypto` ... (and more) |
| **tenant** | 2 | `Anthropic`, `Multiple colocation tenants` |
| **sizerank** | 7 | `Hyperscale (100-999 MW)`, `Hyperscale (101-999 MW)`, `Large (51-99 MW)`, `Medium (11-50 MW)`, `Mega campus (>1,000 MW)`, `Small (0-10 MW)`, `Unknown` |
| **power_source** | 21 | `Biomass`, `Coal`, `Coal, Natural gas, Biomass`, `Fuel Cells`, `Grid (unspecified mix)`, `Grid (unspecified mix), Biomass`, `Grid (unspecified mix), Solar`, `Hybrid (onsite and grid)`, `Hydroelectric`, `Hydroelectric, Grid (unspecified mix)`, `Natural gas`, `Natural gas, Hybrid (onsite and grid)`, `Natural gas, Nuclear, Solar`, `Nuclear`, `Nuclear, Solar, Geothermal, Grid (unspecified mix)` ... (and more) |
| **dedicated_power_plant** | 22 | `2`, `Bluebonnet Electric Cooperative`, `EW Brown Generation Station`, `Georgia Power`, `May use jet engines from retired military planes`, `Northwestern Energy`, `Possibly`, `Salt River Project (SRP) substation`, `Yes`, `Yes `, `Yes - Adams Fork Energy Project Power Station 1`, `Yes - Adams Fork Energy Project Power Station 2`, `Yes - Apollo Generating Station`, `Yes - Bluegrass Power Station`, `Yes - Brightloop Hyrogen Plant / Monarch` ... (and more) |
| **number_of_generators** | 13 | `0`, `1.2 GW diesel`, `100 natural gas-powered backup emergency generators connected to Southern California Gas Company’s high-pressure gas line`, `115 diesel-fueled generators`, `12`, `12-24`, `14 on-site diesel generators`, `15`, `158 diesel backup generators`, `25 2.5MW emergency generators for redundancy purposes`, `516`, `6`, `813` |
| **cooling_source** | 3 | `Air`, `Hybrid air/water`, `Water` |
| **cooling_type** | 3 | `Closed loop`, `Fans`, `Open loop` |
| **community_pushback** | 3 | `Unknown`, `Yes`, `Yes ` |
| **advocacy_information** | 63 | `12-month moratorium`, `180 day moratorium in place in Harlingen as of May 2026.`, `A citizens' group ("We say NO! to Atlas Development's data center") has organized against the project, citing concerns over power and water usage, as well as an open meetings complaint filed in November 2025 regarding the sale process.`, `A public hearing is being held March 19 at 7:00 PM in the town of Alabama on Judge Rd. Public comments being accepted through March 31: https://docs.google.com/document/d/1V9JcpmERQ7EZ5vxm9KiaX6AqYO6XUkpuCELwxKIxHKs/edit?usp=drivesdk`, `Advocacy against the Franklin Partners LLC data center in Pavilion Township was primarily driven by a rapid grassroots movement of local residents. Concerned neighbors quickly organized to challenge the proposed zoning changes, leading to packed town hall meetings and an eventual project withdrawal in late 2025.`, `Advocacy regarding Project Springbank in Adairsville, GA, centers on a successful community-led campaign that resulted in the developer, Atlas Development, withdrawing its rezoning application in May 2025. Despite the project being formally cancelled, local and statewide advocacy remains high to prevent similar developments from resurfacing.`, `Advocacy surrounding data centers in Illinois has intensified in early 2026, shifting from isolated local protests to a coordinated statewide legislative push.`, `Approved at the municipal level. `, `As of March 2026, Project Jupiter, a proposed $165 billion AI data center complex in Santa Teresa, NM, is facing intense pushback from a coalition of 16 environmental and civil rights organizations. Advocacy centers on the project's potential to strain finite natural resources and its bypassing of state environmental regulations.`, `Bessemer Data Center - We Say No!`, `By a 5-4 vote, the commission voted against rezoning the site (also called Crooked Creek) in April 2026`, `By a 5-4 vote, the commission voted in favor of rezoning the site in April 2026`, `Climate Revolution NJ`, `Community advocacy surrounding the xAI project at 5420 Tulane Rd is led by a coalition of environmental justice and civil rights groups. These organizations are primarily concerned with the impact of massive energy and water demands on South Memphis, a region they describe as already overburdened by decades of industrial pollution.`, `Community meeting held Nov 2025 regarding proposed 900 MW, $19 B Kingsboro AI data center by Energy Storage Solutions. Environmental and utility-rate concerns raised by residents and NC Environmental Justice Network. Local organizing ongoing; county considering sale of Kingsboro Business Park land for project.` ... (and more) |
| **resistance_status** | 3 | `Emerging Concern`, `Organized Advocacy`, `Unknown` |
| **nda** | 8 | `Active (Tenant identity legally shielded)`, `Bessemer Mayor Kenneth Gulley, the city attorney, and other city leaders signed NDAs`, `Every elected official is under an NDA including the Montana Public Service Commission`, `Marion County officials confirmed that the council signed a nondisclosure agreement`, `No`, `Officials knew of the Meta plan as “Project Accordion” for more than a year before it was officially announced`, `Yes`, `Yes- https://www.al.com/news/2025/10/secrecy-agreements-fuel-pushback-of-14-billion-alabama-data-center.html` |
| **community_group_website_2** | 32 | `https://capitalbnews.org/meta-richland-parish-ai-data-center/`, `https://centerforcoalfieldjustice.org/`, `https://cwfnc.org/stokes/`, `https://friendsofblackwater.org/`, `https://linktr.ee/residentsunitedlowell`, `https://neighbors4change.com/`, `https://wilmingtondatacenter.org/`, `https://wvrivers.org/`, `https://www.change.org/p/stop-the-construction-of-michigan-s-largest-data-center-in-howell`, `https://www.datacenterdynamics.com/en/news/oracle-and-openai-start-construction-on-stargate-data-center-campus-in-saline-township-michigan/`, `https://www.facebook.com/groups/1117995533656453`, `https://www.facebook.com/groups/1140996281561878/`, `https://www.facebook.com/groups/1359906715176907/`, `https://www.facebook.com/groups/1397482882419331/`, `https://www.facebook.com/groups/1469043077373264/` ... (and more) |
| **information_source** | 6 | `Crowdsourced`, `FOIA/ public records request`, `Media Monitoring`, `Other`, `PEC`, `Sci4GA` |
| **info_source_5** | 72 | `https://cleanview.co/public/data-centers/georgia/1896/fairwater-2---atlanta`, `https://datacenterwatch.substack.com/p/briefing-11212025`, `https://epoch.ai/data/data-centers/satellite-explorer/CoreweaveHeliosAftonTexas?ref=404media.co`, `https://epoch.ai/data/data-centers/satellite-explorer/MetaPrometheusNewAlbanyOhio?ref=404media.co`, `https://epoch.ai/data/data-centers/satellite-explorer/OpenAIOracleStargateAbileneTexas?ref=404media.co`, `https://finance.yahoo.com/news/ai-power-darling-fermi-implodes-185100893.html`, `https://fox56.com/news/local/archbald-residents-unite-against-unanswered-questions-on-data-centers`, `https://local21news.com/news/local/a-new-data-center-might-be-build-in-cumberland-county-and-its-700-acres-ai-carlisle-artificial-intelligence-pennsylvania-data-center-partners-powerhouse-pa`, `https://opsb.ohio.gov/news/opsb-authorizes-construction-of-wood-county-power-plant`, `https://planetdetroit.org/2026/01/allen-park-postpones-data-center-decision/`, `https://planetdetroit.org/2026/02/project-cannoli-preliminary-site-plan/`, `https://spotlightdelaware.org/2026/03/26/delaware-city-data-center-environmental-denial-upheld-by-state-board/`, `https://tecfusions.com/?clarksville#solutions-newkensington`, `https://tompkinsweekly.com/articles/cayuga-data-campus-lansing/`, `https://triblive.com/local/valley-news-dispatch/springdale-planning-commission-oks-data-center-project-proposal-moves-to-council/` ... (and more) |
| **info_source_6** | 44 | `https://dep.wv.gov/daq/permitting/Documents/Fundamental%20Data%20LLC;%20Ridgeline%20Facility/093-00034_APPL_13-3713.pdf`, `https://elpasomatters.org/2025/09/25/stargate-open-ai-oracle-project-jupiter-data-center-dona-ana-new-mexico-el-paso-texas/`, `https://epoch.ai/data/data-centers/satellite-explorer/AnthropicAmazonProjectRainierNewCarlisleIndiana?ref=404media.co`, `https://fermiamerica.com/`, `https://fox56.com/news/local/archbald-residents-unite-against-unanswered-questions-on-data-centers`, `https://ithacavoice.org/2026/01/local-groups-file-suit-against-terawulf-lansing-zoning-board-over-data-center/`, `https://news.azpm.org/p/azpmnews/2026/5/28/229919-arizona-water-officials-approve-wells-tied-to-project-blue-data-center/`, `https://oilandgaswatch.org/facility/rec_d4f1u60q7easr8ra1g3g`, `https://planetdetroit.org/2026/02/saline-data-center-air-wetlands-permits/`, `https://planetdetroit.org/2026/03/google-dte-data-center-van-buren/`, `https://triblive.com/local/regional/sprawling-data-center-campus-proposed-next-to-old-bruce-mansfield-power-plant-in-shippingport/`, `https://triblive.com/local/valley-news-dispatch/upper-burrell-data-center-nets-first-tenant-at-former-alcoa-research-site/`, `https://wgxa.tv/news/local/environmental-advocate-urges-twiggs-county-to-reject-data-center-plans-near-ocmulgee-river`, `https://wsbt.com/news/local/st-joseph-county-council-denies-rezoning-of-land-for-data-center-votes-7-2-marathon-meeting-hours-long-public-opinion-13-billion-dollar-project-amazon-new-carlisle-approval-process-plan-commission-st-joseph-county-indiana`, `https://www.bgr.com/1990532/meta-new-aid-data-center-size-70-football-fields-residents-scared-water/` ... (and more) |
| **info_source_7** | 25 | `https://abc3340.com/news/abc-3340-news-iteam/bessemer-unveils-revised-project-marvel-data-center-campus-plan-amid-ongoing-controversy`, `https://epoch.ai/data/data-centers/satellite-explorer/MicrosoftFairwaterMountPleasantWisconsin?ref=404media.co`, `https://lailluminator.com/briefs/entergy-builds-power-plant-for-data-center/`, `https://oilandgaswatch.org/facility/rec_d4f1u60q7easr8ra1g30`, `https://oilandgaswatch.org/facility/rec_d5eiru1uih89upkga2qg`, `https://paenvironmentdaily.blogspot.com/2025/12/dep-to-host-jan-6-public-information.html`, `https://pbswisconsin.org/news-item/the-local-battles-over-data-center-developments-in-wisconsin/?fbclid=IwY2xjawQb89xleHRuA2FlbQIxMQBzcnRjBmFwcF9pZBAyMjIwMzkxNzg4MjAwODkyAAEe_9n-9GXVsrmup4ro8JcBXofGIGDBBJOvEis3IhU4EDbZm0ChkaEapPFbbd8_aem_HvzltHtS42i2Jp2jBPjrRA`, `https://trackdatacenters.com/state/pennsylvania`, `https://truthout.org/articles/new-york-residents-are-fighting-a-data-center-backed-by-a-billionaire-trump-ally/`, `https://www.41nbc.com/twiggs-county-data-center-rezoning-approval/`, `https://www.alleghenyfront.org/meta-beaver-valley-nuclear-power-plant-ai-data-centers/`, `https://www.businesswire.com/news/home/20260401716982/en/Homer-City-Redevelopment-Crosses-the-First-Steel-Threshold`, `https://www.datacenterdynamics.com/en/news/google-confirms-1gw-data-center-campus-near-detroit-michigan-partners-with-dte-energy-on-27gw-power-generation/`, `https://www.datacenterdynamics.com/en/news/groups-sue-to-stall-data-center-project-in-do%C3%B1a-ana-county-new-mexico/`, `https://www.datacenterdynamics.com/en/news/or/` ... (and more) |
| **info_source_8** | 14 | `https://bgindependentmedia.org/meta-data-center-how-it-went-from-economic-development-coup-to-project-local-residents-rue/`, `https://insideclimatenews.org/news/13112025/proposed-alabama-data-center-clashes-with-northern-beltline-birmingham-darter/`, `https://planetdetroit.org/2025/12/billion-dollar-data-center-paused/`, `https://www.41nbc.com/twiggs-county-data-center-rezoning-approval/`, `https://www.datacenterdynamics.com/en/news/google-confirms-it-is-behind-403-acre-data-center-campus-in-hermantown-minnesota/`, `https://www.datacenterdynamics.com/en/news/meta-purchases-additional-1400-acres-for-hyperion-mega-data-center-expansion/`, `https://www.datacenterdynamics.com/en/news/oracle-revealed-as-tenant-of-project-jupiter-data-center-campus-in-new-mexico/`, `https://www.datacenterdynamics.com/en/news/riot-platforms-files-to-add-building-to-cryptomine-and-data-center-campus-in-corsicana-texas/`, `https://www.datacenterdynamics.com/en/news/shippingport-industrial-park/`, `https://www.datacenterdynamics.com/en/news/vantage-tops-out-second-building-at-openais-lighthouse-campus-in-wisconsin/`, `https://www.nytimes.com/2026/03/17/nyregion/ai-data-center-new-york.html`, `https://www.wisn.com/article/whats-that-sound-its-mount-pleasants-new-ai-data-center/70850595`, `https://www.wvia.org/news/local/2026-05-01/fast-track-no-more-pa-kicks-archbald-data-center-campus-off-permit-program`, `https://www.wvxu.org/environment/2025-12-03/developers-data-center-butler-county` |

#### Sample Data (First 3 rows)

| facility_name | address | city | state | zip | county | lat | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Global Stack Data Center | nan | nan | nan | nan | Napa | 38.585007 | ... |
| Stak Energy Data Center | Dalton Hwy, 26 miles south of Deadhorse | North Slope Borough | AK | nan | North Slope | 69.90071 | ... |
| Prudhoe Bay Data Center | Dalton Hwy | Prudhoe Bay | AK | 99734.0 | North Slope | 70.18478 | ... |

---

### File: `global_datacenters_github.csv`

- **Size:** 1679.19 KB
- **Total Rows:** 18,110
- **Total Columns:** 6
- **Category Columns:** *None*
- **Numeric Columns:** *None*
- **Date Columns:** *None*
- **Text Columns:** name, company, city, state, country, address

#### Sample Data (First 3 rows)

| name | company | city | state | country | address |
| --- | --- | --- | --- | --- | --- |
| NAP de las Americas Madrid | Terremark | Madrid | nan | Spain | Calle de Yecora, 4 28009 Madrid Spain |
| Central Office 2 | StarHub Ltd. | Singapore | nan | Singapore | 19 Tai Seng Dr 535222 Singapore Singa... |
| Cluj-Napoca | GTS Telecom SRL | Cluj-Napoca | nan | Romania | Str. Garii nr. 21 400267 Cluj-Napoca ... |

---

## 3. Excel Files Analysis (Advanced Methodology)

### File: `DATA/DataWeb-Query-Export.xlsx`

- **Size:** 0.16 MB
- **Sheets in Workbook:** 2

#### Sheet: `Query Parameters`

- **Rows:** 32
- **Total Columns:** 2
- **Category Columns:** *None*
- **Numeric Columns:** *None*
- **Date/Time Columns:** *None*
- **Text Columns:** Download Date, 2026-07-09 05:42:20.082000

##### Sample Data

| Download Date | 2026-07-09 05:42:20.082000 |
| --- | --- |
| Step 1: Trade Flow and Classification... | nan |
| Trade Flow | Imports For Consumption |
| Classification System | HTS Items |

#### Sheet: `Query Results`

- **Rows:** 4,239
- **Total Columns:** 9
- **Category Columns:** Data Type, Description, Quantity Description
- **Numeric Columns:** Year, Quarter, HTS Number, Customs Value, Unnamed: 8
- **Date/Time Columns:** *None*
- **Text Columns:** Country

##### Categorical Variable Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **Data Type** | 4 | `Customs Value`, `Data Type`, `First Unit of Quantity`, `Total: ` |
| **Description** | 4 | `Description`, `MEMORIES, ELECTRONIC INTEGRATED CIRCUITS`, `PARTS FOR ELECTRONIC INTEGRATED CIRCUITS AND MICROASSEMBLIES`, `PROCESSORS AND CONTROLLERS, ELECTRONIC INTEGRATED CIRCUITS` |
| **Quantity Description** | 3 | `Quantity Description`, `Value for: number`, `number` |

##### Sample Data

| Data Type | Country | Year | Quarter | HTS Number | Description | Quantity Description | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Customs Value | Afghanistan | 2025 | 2 | 854290 | PARTS FOR ELECTRONIC INTEGRATED CIRCU... | Value for: number | ... |
| Customs Value | Afghanistan | 2026 | 1 | 854231 | PROCESSORS AND CONTROLLERS, ELECTRONI... | Value for: number | ... |
| Customs Value | Albania | 2023 | 4 | 854231 | PROCESSORS AND CONTROLLERS, ELECTRONI... | Value for: number | ... |

---

### File: `DATA/LBNL_Ix_Queue_Data_File_thru2025.xlsx`

> [!WARNING]
> Failed to analyze Excel file. Error: float() argument must be a string or a real number, not 'datetime.datetime'

## 4. JSON Datasets Analysis (Advanced Methodology)

### File: `data_centers/TESM_FULL_RESULTS.json`

- **Size:** 720.76 KB
- **Format:** Hierarchical/Nested JSON Document
#### JSON Structure Summary

- **Object** containing keys:
  - **assessment** (str): sample = `SPECULATIVE EXCESS`
  - **backtest**: object
    - **Object** containing keys:
      - **episodes**: object
        - **Object** containing keys:
          - **cloud_2010**: object
            - **Object** containing keys:
              - **actual** (dict): sample = `None`
              - **directional_accuracy** (float): sample = `1.0`
              - **mae** (float): sample = `0.0`
              - **prediction** (dict): sample = `None`
              - **rmse** (float): sample = `0.0`
          - **dotcom_1999**: object
            - **Object** containing keys:
              - **actual** (dict): sample = `None`
              - **directional_accuracy** (float): sample = `1.0`
              - **mae** (float): sample = `0.01833333333333333`
              - **prediction** (dict): sample = `None`
              - **rmse** (float): sample = `0.031754264805429415`
          - **gfc_2007**: object
            - **Object** containing keys:
              - **actual** (dict): sample = `None`
              - **directional_accuracy** (float): sample = `1.0`
              - **mae** (float): sample = `0.0`
              - **prediction** (dict): sample = `None`
              - **rmse** (float): sample = `0.0`
          - **japan_1989**: object
            - **Object** containing keys:
              - **actual** (dict): sample = `None`
              - **directional_accuracy** (float): sample = `1.0`
              - **mae** (float): sample = `0.0`
              - **prediction** (dict): sample = `None`
              - **rmse** (float): sample = `0.0`
          - **telecom_1996**: object
            - **Object** containing keys:
              - **actual** (dict): sample = `None`
              - **directional_accuracy** (float): sample = `1.0`
              - **mae** (float): sample = `0.015000000000000005`
              - **prediction** (dict): sample = `None`
              - **rmse** (float): sample = `0.025980762113533167`
      - **summary**: object
        - **Object** containing keys:
          - **avg_directional_accuracy** (float): sample = `1.0`
          - **avg_mae** (float): sample = `0.006666666666666666`
          - **avg_rmse** (float): sample = `0.011547005383792516`
  - **dcf_valuations**: object
    - **Object** containing keys:
      - **AWS**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `432471623135.37427`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `129470336989.28976`
          - **pv_terminal** (float): sample = `303001286146.0845`
          - **terminal_value** (float): sample = `717314238176.9327`
      - **Beale Infrastructure**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `47681535947.182976`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `14274565536.792004`
          - **pv_terminal** (float): sample = `33406970410.390972`
          - **terminal_value** (float): sample = `79086448227.73337`
      - **Bitzero**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `1009710827437.6365`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `302280182321.1519`
          - **pv_terminal** (float): sample = `707430645116.4846`
          - **terminal_value** (float): sample = `1674745611542.0344`
      - **Crusoe**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `383803176747.10205`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `114900317090.75322`
          - **pv_terminal** (float): sample = `268902859656.34882`
          - **terminal_value** (float): sample = `636590861944.3828`
      - **Energy Abundance**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `560949429516.9015`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `167933126217.5536`
          - **pv_terminal** (float): sample = `393016303299.3479`
          - **terminal_value** (float): sample = `930412519953.355`
      - **Fermi America**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `1009710827437.6365`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `302280182321.1519`
          - **pv_terminal** (float): sample = `707430645116.4846`
          - **terminal_value** (float): sample = `1674745611542.0344`
      - **Google**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `37023205602.91058`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `11083748966.188568`
          - **pv_terminal** (float): sample = `25939456636.72202`
          - **terminal_value** (float): sample = `61408127380.433174`
      - **GridFree AI**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `560949429516.9015`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `167933126217.5536`
          - **pv_terminal** (float): sample = `393016303299.3479`
          - **terminal_value** (float): sample = `930412519953.355`
      - **Homer City**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `504855413718.81824`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `151140091160.57596`
          - **pv_terminal** (float): sample = `353715322558.2423`
          - **terminal_value** (float): sample = `837372805771.0172`
      - **Joule Capital**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `448761397920.7355`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `134347056103.5983`
          - **pv_terminal** (float): sample = `314414341817.13715`
          - **terminal_value** (float): sample = `744333091588.6804`
      - **Meta**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `753655071500.9617`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `225623996722.60837`
          - **pv_terminal** (float): sample = `528031074778.35333`
          - **terminal_value** (float): sample = `1250041585486.1086`
      - **Microsoft**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `35454884032.54568`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `10614235797.323013`
          - **pv_terminal** (float): sample = `24840648235.222664`
          - **terminal_value** (float): sample = `58806848285.38696`
      - **NTT**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `22439460626.447334`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `6717769152.346496`
          - **pv_terminal** (float): sample = `15721691474.10084`
          - **terminal_value** (float): sample = `37218961298.930954`
      - **New Era Energy**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `785330128477.269`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `235106654269.35272`
          - **pv_terminal** (float): sample = `550223474207.9164`
          - **terminal_value** (float): sample = `1302579065747.695`
      - **Northpoint Development**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `113088196026.62111`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `33855555060.30121`
          - **pv_terminal** (float): sample = `79232640966.3199`
          - **terminal_value** (float): sample = `187572476065.66516`
      - **Nscale**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `897518160073.4347`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `268692724383.30795`
          - **pv_terminal** (float): sample = `628825435690.1267`
          - **terminal_value** (float): sample = `1488658494112.3687`
      - **Oracle**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `263397485121.8552`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `78854101255.52493`
          - **pv_terminal** (float): sample = `184543383866.33026`
          - **terminal_value** (float): sample = `436881303351.4596`
      - **Other/Unclassified**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `311326655235.7983`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `93202801781.30893`
          - **pv_terminal** (float): sample = `218123853454.48935`
          - **terminal_value** (float): sample = `516378487230.2128`
      - **Pacifico Energy**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `858253739745.1874`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `256938016190.59018`
          - **pv_terminal** (float): sample = `601315723554.5972`
          - **terminal_value** (float): sample = `1423533000904.23`
      - **Prime Data Centers**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `26926425598.129757`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `8061045418.0380745`
          - **pv_terminal** (float): sample = `18865380180.091682`
          - **terminal_value** (float): sample = `44661215745.71918`
      - **STAK Energy**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `336568730556.5337`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `100759598165.7544`
          - **pv_terminal** (float): sample = `235809132390.7793`
          - **terminal_value** (float): sample = `558245974159.0148`
      - **Sailfish Digital**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `560949429516.9015`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `167933126217.5536`
          - **pv_terminal** (float): sample = `393016303299.3479`
          - **terminal_value** (float): sample = `930412519953.355`
      - **Stream Data Centers**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `22439460626.447334`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `6717769152.346496`
          - **pv_terminal** (float): sample = `15721691474.10084`
          - **terminal_value** (float): sample = `37218961298.930954`
      - **Tract**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `269254984445.22705`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `80607678532.60356`
          - **pv_terminal** (float): sample = `188647305912.6235`
          - **terminal_value** (float): sample = `446596779327.212`
      - **Vantage**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `19743552979.604317`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `5910687131.569581`
          - **pv_terminal** (float): sample = `13832865848.034735`
          - **terminal_value** (float): sample = `32747424124.14334`
      - **Vermaland**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `673137461113.0674`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `201519196331.5088`
          - **pv_terminal** (float): sample = `471618264781.5586`
          - **terminal_value** (float): sample = `1116491948318.0295`
      - **xAI**: object
        - **Object** containing keys:
          - **assumptions**: object
            - **Object** containing keys:
              - **capex_intensity** (float): sample = `0.3`
              - **ebitda_margin** (float): sample = `0.35`
              - **revenue_growth** (float): sample = `0.2`
              - **terminal_growth** (float): sample = `0.025`
              - **wacc** (float): sample = `0.09`
          - **enterprise_value** (float): sample = `21823470453.86891`
          - **projections**: array
            - **Array** of length 10 containing `dict` items.
          - **pv_explicit** (float): sample = `6533358312.514689`
          - **pv_terminal** (float): sample = `15290112141.354221`
          - **terminal_value** (float): sample = `36197256063.881905`
  - **hyperscaler_aggregate**: object
    - **Object** containing keys:
      - **AWS**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `2773`
          - **capex_billion** (float): sample = `24.8`
          - **ebitda_billion** (float): sample = `146.06290100013334`
          - **gpus** (int): sample = `2464641`
          - **inference_pflops** (float): sample = `2822.5`
          - **revenue_billion** (float): sample = `146.93202965613332`
          - **roic** (float): sample = `5.889633104844086`
      - **Beale Infrastructure**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `425`
          - **capex_billion** (float): sample = `3.825`
          - **ebitda_billion** (float): sample = `16.0621772328`
          - **gpus** (int): sample = `377740`
          - **inference_pflops** (float): sample = `432.6`
          - **revenue_billion** (float): sample = `16.1997793128`
          - **roic** (float): sample = `4.199262021647059`
      - **Bitzero**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `9000`
          - **capex_billion** (float): sample = `81.0`
          - **ebitda_billion** (float): sample = `340.620504624`
          - **gpus** (int): sample = `7999200`
          - **inference_pflops** (float): sample = `9160.6`
          - **revenue_billion** (float): sample = `343.048776624`
          - **roic** (float): sample = `4.205191415111111`
      - **Crusoe**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `5400`
          - **capex_billion** (float): sample = `10.0`
          - **ebitda_billion** (float): sample = `129.1481223872`
          - **gpus** (int): sample = `4799520`
          - **inference_pflops** (float): sample = `5496.4`
          - **revenue_billion** (float): sample = `130.3969479872`
          - **roic** (float): sample = `12.91481223872`
      - **Energy Abundance**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `5000`
          - **capex_billion** (float): sample = `45.0`
          - **ebitda_billion** (float): sample = `188.84782368`
          - **gpus** (int): sample = `4444000`
          - **inference_pflops** (float): sample = `5089.2`
          - **revenue_billion** (float): sample = `190.58230368`
          - **roic** (float): sample = `4.196618304`
      - **Fermi America**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `9000`
          - **capex_billion** (float): sample = `81.0`
          - **ebitda_billion** (float): sample = `339.926712624`
          - **gpus** (int): sample = `7999200`
          - **inference_pflops** (float): sample = `9160.6`
          - **revenue_billion** (float): sample = `343.048776624`
          - **roic** (float): sample = `4.196626081777778`
      - **Google**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `330`
          - **capex_billion** (float): sample = `10.0`
          - **ebitda_billion** (float): sample = `12.46414093344`
          - **gpus** (int): sample = `293303`
          - **inference_pflops** (float): sample = `335.9`
          - **revenue_billion** (float): sample = `12.57861661344`
          - **roic** (float): sample = `1.2464140933439998`
      - **GridFree AI**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `5000`
          - **capex_billion** (float): sample = `45.0`
          - **ebitda_billion** (float): sample = `188.84782368`
          - **gpus** (int): sample = `4444000`
          - **inference_pflops** (float): sample = `5089.2`
          - **revenue_billion** (float): sample = `190.58230368`
          - **roic** (float): sample = `4.196618304`
      - **Homer City**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `4500`
          - **capex_billion** (float): sample = `40.5`
          - **ebitda_billion** (float): sample = `170.067425112`
          - **gpus** (int): sample = `3999600`
          - **inference_pflops** (float): sample = `4580.3`
          - **revenue_billion** (float): sample = `171.524388312`
          - **roic** (float): sample = `4.199195681777778`
      - **Joule Capital**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `4000`
          - **capex_billion** (float): sample = `36.0`
          - **ebitda_billion** (float): sample = `151.387240944`
          - **gpus** (int): sample = `3555200`
          - **inference_pflops** (float): sample = `4071.4`
          - **revenue_billion** (float): sample = `152.466472944`
          - **roic** (float): sample = `4.205201137333333`
      - **Meta**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `10150`
          - **capex_billion** (float): sample = `21.35`
          - **ebitda_billion** (float): sample = `253.30962170792728`
          - **gpus** (int): sample = `9021320`
          - **inference_pflops** (float): sample = `10331.1`
          - **revenue_billion** (float): sample = `256.0539545079273`
          - **roic** (float): sample = `11.864619283743666`
      - **Microsoft**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `316`
          - **capex_billion** (float): sample = `2.932`
          - **ebitda_billion** (float): sample = `11.943222225800001`
          - **gpus** (int): sample = `280860`
          - **inference_pflops** (float): sample = `321.7`
          - **revenue_billion** (float): sample = `12.045780100800002`
          - **roic** (float): sample = `4.073404579058663`
      - **NTT**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `200`
          - **capex_billion** (float): sample = `1.8`
          - **ebitda_billion** (float): sample = `7.5590422272`
          - **gpus** (int): sample = `177760`
          - **inference_pflops** (float): sample = `203.6`
          - **revenue_billion** (float): sample = `7.6237961472`
          - **roic** (float): sample = `4.199467904`
      - **New Era Energy**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `7000`
          - **capex_billion** (float): sample = `63.0`
          - **ebitda_billion** (float): sample = `264.764999352`
          - **gpus** (int): sample = `6221600`
          - **inference_pflops** (float): sample = `7124.9`
          - **revenue_billion** (float): sample = `266.815540152`
          - **roic** (float): sample = `4.202619037333333`
      - **Northpoint Development**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `1008`
          - **capex_billion** (float): sample = `9.072`
          - **ebitda_billion** (float): sample = `38.11084236`
          - **gpus** (int): sample = `895910`
          - **inference_pflops** (float): sample = `1026.0`
          - **revenue_billion** (float): sample = `38.421661176`
          - **roic** (float): sample = `4.200930595238095`
      - **Nscale**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `8000`
          - **capex_billion** (float): sample = `72.0`
          - **ebitda_billion** (float): sample = `302.772906888`
          - **gpus** (int): sample = `7110400`
          - **inference_pflops** (float): sample = `8142.7`
          - **revenue_billion** (float): sample = `304.931370888`
          - **roic** (float): sample = `4.205179262333333`
      - **Oracle**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `2630`
          - **capex_billion** (float): sample = `18.27`
          - **ebitda_billion** (float): sample = `88.52942553842826`
          - **gpus** (int): sample = `2337544`
          - **inference_pflops** (float): sample = `2676.8999999999996`
          - **revenue_billion** (float): sample = `89.48917113842825`
          - **roic** (float): sample = `4.845617161380857`
      - **Other/Unclassified**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `2775`
          - **capex_billion** (float): sample = `24.975`
          - **ebitda_billion** (float): sample = `104.91432372240003`
          - **gpus** (int): sample = `2466420`
          - **inference_pflops** (float): sample = `2824.5`
          - **revenue_billion** (float): sample = `105.77308404240003`
          - **roic** (float): sample = `4.20077372261862`
      - **Pacifico Energy**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `7650`
          - **capex_billion** (float): sample = `68.85`
          - **ebitda_billion** (float): sample = `288.93754823039995`
          - **gpus** (int): sample = `6799320`
          - **inference_pflops** (float): sample = `7786.5`
          - **revenue_billion** (float): sample = `291.5913026304`
          - **roic** (float): sample = `4.196623794196078`
      - **Prime Data Centers**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `240`
          - **capex_billion** (float): sample = `2.16`
          - **ebitda_billion** (float): sample = `9.07053567264`
          - **gpus** (int): sample = `213312`
          - **inference_pflops** (float): sample = `244.3`
          - **revenue_billion** (float): sample = `9.148240376639999`
          - **roic** (float): sample = `4.199322070666667`
      - **STAK Energy**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `3000`
          - **capex_billion** (float): sample = `27.0`
          - **ebitda_billion** (float): sample = `112.498955208`
          - **gpus** (int): sample = `2666400`
          - **inference_pflops** (float): sample = `3053.5`
          - **revenue_billion** (float): sample = `114.349067208`
          - **roic** (float): sample = `4.166627970666666`
      - **Sailfish Digital**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `5000`
          - **capex_billion** (float): sample = `45.0`
          - **ebitda_billion** (float): sample = `188.84782368`
          - **gpus** (int): sample = `4444000`
          - **inference_pflops** (float): sample = `5089.2`
          - **revenue_billion** (float): sample = `190.58230368`
          - **roic** (float): sample = `4.196618304`
      - **Stream Data Centers**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `200`
          - **capex_billion** (float): sample = `1.8`
          - **ebitda_billion** (float): sample = `7.5590422272`
          - **gpus** (int): sample = `177760`
          - **inference_pflops** (float): sample = `203.6`
          - **revenue_billion** (float): sample = `7.6237961472`
          - **roic** (float): sample = `4.199467904`
      - **Tract**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `2400`
          - **capex_billion** (float): sample = `21.6`
          - **ebitda_billion** (float): sample = `90.73920896640001`
          - **gpus** (int): sample = `2133120`
          - **inference_pflops** (float): sample = `2442.8`
          - **revenue_billion** (float): sample = `91.4792537664`
          - **roic** (float): sample = `4.200889304`
      - **Vantage**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `176`
          - **capex_billion** (float): sample = `1.584`
          - **ebitda_billion** (float): sample = `6.65087934776`
          - **gpus** (int): sample = `156428`
          - **inference_pflops** (float): sample = `179.1`
          - **revenue_billion** (float): sample = `6.70786279776`
          - **roic** (float): sample = `4.198787467020202`
      - **Vermaland**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `6000`
          - **capex_billion** (float): sample = `54.0`
          - **ebitda_billion** (float): sample = `226.755516816`
          - **gpus** (int): sample = `5332800`
          - **inference_pflops** (float): sample = `6107.0`
          - **revenue_billion** (float): sample = `228.698134416`
          - **roic** (float): sample = `4.199176237333333`
      - **xAI**: object
        - **Object** containing keys:
          - **capacity_mw** (int): sample = `300`
          - **capex_billion** (float): sample = `2.7`
          - **ebitda_billion** (float): sample = `7.322008177066667`
          - **gpus** (int): sample = `266640`
          - **inference_pflops** (float): sample = `305.4`
          - **revenue_billion** (float): sample = `7.414513777066667`
          - **roic** (float): sample = `2.711854880395062`
  - **monte_carlo**: object
    - **Object** containing keys:
      - **AWS**: object
        - **Object** containing keys:
          - **mean** (float): sample = `651327401605.2299`
          - **median** (float): sample = `346879426082.77356`
          - **p10** (float): sample = `-160898174661.76364`
          - **p25** (float): sample = `-26827875895.863045`
          - **p75** (float): sample = `936338679032.964`
          - **p90** (float): sample = `1815704009663.9116`
          - **prob_below_capex** (float): sample = `0.3056`
          - **std** (float): sample = `1080916344983.4253`
      - **Beale Infrastructure**: object
        - **Object** containing keys:
          - **mean** (float): sample = `75267503007.67479`
          - **median** (float): sample = `41587177867.85884`
          - **p10** (float): sample = `-16270646564.824673`
          - **p25** (float): sample = `-1646725541.1343083`
          - **p75** (float): sample = `109615755407.81071`
          - **p90** (float): sample = `205414099512.30246`
          - **prob_below_capex** (float): sample = `0.2946`
          - **std** (float): sample = `122108444298.4314`
      - **Bitzero**: object
        - **Object** containing keys:
          - **mean** (float): sample = `1585241099574.879`
          - **median** (float): sample = `881886957400.9463`
          - **p10** (float): sample = `-378936183491.9781`
          - **p25** (float): sample = `-42388437911.613815`
          - **p75** (float): sample = `2283494589242.5586`
          - **p90** (float): sample = `4252152309483.3877`
          - **prob_below_capex** (float): sample = `0.2974`
          - **std** (float): sample = `2648533574359.597`
      - **Crusoe**: object
        - **Object** containing keys:
          - **mean** (float): sample = `590778290623.6519`
          - **median** (float): sample = `337984800515.53723`
          - **p10** (float): sample = `-131732258500.59134`
          - **p25** (float): sample = `-16786463958.192127`
          - **p75** (float): sample = `847038041573.9484`
          - **p90** (float): sample = `1623417033270.7073`
          - **prob_below_capex** (float): sample = `0.2822`
          - **std** (float): sample = `935701387100.3738`
      - **Energy Abundance**: object
        - **Object** containing keys:
          - **mean** (float): sample = `840992097974.85`
          - **median** (float): sample = `484266814600.8783`
          - **p10** (float): sample = `-209756760289.0043`
          - **p25** (float): sample = `-29343365310.4169`
          - **p75** (float): sample = `1241453147025.6697`
          - **p90** (float): sample = `2345792270294.7925`
          - **prob_below_capex** (float): sample = `0.3042`
          - **std** (float): sample = `1308965319044.1758`
      - **Fermi America**: object
        - **Object** containing keys:
          - **mean** (float): sample = `1566286706326.6006`
          - **median** (float): sample = `855469239168.4241`
          - **p10** (float): sample = `-360038756133.01245`
          - **p25** (float): sample = `-48404653240.417786`
          - **p75** (float): sample = `2291555373913.651`
          - **p90** (float): sample = `4334264220147.19`
          - **prob_below_capex** (float): sample = `0.3038`
          - **std** (float): sample = `2482178781846.565`
      - **Google**: object
        - **Object** containing keys:
          - **mean** (float): sample = `58165267982.17335`
          - **median** (float): sample = `32739361830.25139`
          - **p10** (float): sample = `-12232243297.172276`
          - **p25** (float): sample = `-1271665895.6832623`
          - **p75** (float): sample = `84089587967.54143`
          - **p90** (float): sample = `156144921334.88022`
          - **prob_below_capex** (float): sample = `0.338`
          - **std** (float): sample = `91360233485.00618`
      - **GridFree AI**: object
        - **Object** containing keys:
          - **mean** (float): sample = `852882452004.0604`
          - **median** (float): sample = `469104400778.2201`
          - **p10** (float): sample = `-213683136945.496`
          - **p25** (float): sample = `-33272696618.334805`
          - **p75** (float): sample = `1255981962231.8706`
          - **p90** (float): sample = `2367678050726.5767`
          - **prob_below_capex** (float): sample = `0.3102`
          - **std** (float): sample = `1385445554603.0723`
      - **Homer City**: object
        - **Object** containing keys:
          - **mean** (float): sample = `806513626820.9758`
          - **median** (float): sample = `441295796153.2001`
          - **p10** (float): sample = `-178205953712.5378`
          - **p25** (float): sample = `-28784504919.051125`
          - **p75** (float): sample = `1166463790815.3708`
          - **p90** (float): sample = `2252440013763.0156`
          - **prob_below_capex** (float): sample = `0.3084`
          - **std** (float): sample = `1312952168048.8003`
      - **Joule Capital**: object
        - **Object** containing keys:
          - **mean** (float): sample = `733753455935.1212`
          - **median** (float): sample = `386727395990.74585`
          - **p10** (float): sample = `-164801375049.41357`
          - **p25** (float): sample = `-16727664641.482489`
          - **p75** (float): sample = `1044446614695.8374`
          - **p90** (float): sample = `2017969616910.8547`
          - **prob_below_capex** (float): sample = `0.2958`
          - **std** (float): sample = `1262396760377.0854`
      - **Meta**: object
        - **Object** containing keys:
          - **mean** (float): sample = `1152313460344.7612`
          - **median** (float): sample = `666067443241.0647`
          - **p10** (float): sample = `-263540160068.99033`
          - **p25** (float): sample = `-23702019299.25762`
          - **p75** (float): sample = `1685101243661.4878`
          - **p90** (float): sample = `3152904942214.4287`
          - **prob_below_capex** (float): sample = `0.2758`
          - **std** (float): sample = `1802610291283.1448`
      - **Microsoft**: object
        - **Object** containing keys:
          - **mean** (float): sample = `55323610235.40799`
          - **median** (float): sample = `30031249260.346268`
          - **p10** (float): sample = `-12087854127.554785`
          - **p25** (float): sample = `-1581334497.627592`
          - **p75** (float): sample = `79709641033.41107`
          - **p90** (float): sample = `151675320395.4205`
          - **prob_below_capex** (float): sample = `0.3036`
          - **std** (float): sample = `92267094334.09988`
      - **NTT**: object
        - **Object** containing keys:
          - **mean** (float): sample = `35880411513.49098`
          - **median** (float): sample = `20004586121.57766`
          - **p10** (float): sample = `-7522306340.871952`
          - **p25** (float): sample = `-523194866.89536065`
          - **p75** (float): sample = `50252518195.20754`
          - **p90** (float): sample = `95821252964.73465`
          - **prob_below_capex** (float): sample = `0.2822`
          - **std** (float): sample = `58859120762.9902`
      - **New Era Energy**: object
        - **Object** containing keys:
          - **mean** (float): sample = `1167571024544.8777`
          - **median** (float): sample = `665637311783.7573`
          - **p10** (float): sample = `-292574361507.65753`
          - **p25** (float): sample = `-37436214347.27362`
          - **p75** (float): sample = `1696170235713.9565`
          - **p90** (float): sample = `3236352915876.247`
          - **prob_below_capex** (float): sample = `0.3008`
          - **std** (float): sample = `1873668705819.0447`
      - **Northpoint Development**: object
        - **Object** containing keys:
          - **mean** (float): sample = `177264962031.26813`
          - **median** (float): sample = `99439809262.19788`
          - **p10** (float): sample = `-40565469190.99141`
          - **p25** (float): sample = `-4385152567.376331`
          - **p75** (float): sample = `254913448729.13513`
          - **p90** (float): sample = `492863077395.45496`
          - **prob_below_capex** (float): sample = `0.293`
          - **std** (float): sample = `279218569619.44916`
      - **Nscale**: object
        - **Object** containing keys:
          - **mean** (float): sample = `1370518240912.6123`
          - **median** (float): sample = `771218749949.4697`
          - **p10** (float): sample = `-322295772769.70325`
          - **p25** (float): sample = `-35657500049.0895`
          - **p75** (float): sample = `1975270492511.3562`
          - **p90** (float): sample = `3756490378852.361`
          - **prob_below_capex** (float): sample = `0.301`
          - **std** (float): sample = `2154882238209.996`
      - **Oracle**: object
        - **Object** containing keys:
          - **mean** (float): sample = `402225975694.2375`
          - **median** (float): sample = `239478242691.9408`
          - **p10** (float): sample = `-98819681751.80466`
          - **p25** (float): sample = `-10455140264.000465`
          - **p75** (float): sample = `599022034421.524`
          - **p90** (float): sample = `1098816927826.2716`
          - **prob_below_capex** (float): sample = `0.2924`
          - **std** (float): sample = `615764116364.468`
      - **Other/Unclassified**: object
        - **Object** containing keys:
          - **mean** (float): sample = `485138388626.279`
          - **median** (float): sample = `259218657009.9745`
          - **p10** (float): sample = `-108122103858.10475`
          - **p25** (float): sample = `-16923729129.128798`
          - **p75** (float): sample = `685238051662.2483`
          - **p90** (float): sample = `1308722077686.173`
          - **prob_below_capex** (float): sample = `0.3096`
          - **std** (float): sample = `839015817793.1691`
      - **Pacifico Energy**: object
        - **Object** containing keys:
          - **mean** (float): sample = `1318255636152.0908`
          - **median** (float): sample = `705282400547.6978`
          - **p10** (float): sample = `-306840640514.935`
          - **p25** (float): sample = `-45047151540.77223`
          - **p75** (float): sample = `1906875507145.5264`
          - **p90** (float): sample = `3689862344125.7974`
          - **prob_below_capex** (float): sample = `0.3054`
          - **std** (float): sample = `2137729323755.0027`
      - **Prime Data Centers**: object
        - **Object** containing keys:
          - **mean** (float): sample = `41964363778.37287`
          - **median** (float): sample = `22670765492.516235`
          - **p10** (float): sample = `-9573794578.055344`
          - **p25** (float): sample = `-1155046034.705137`
          - **p75** (float): sample = `59641639909.69914`
          - **p90** (float): sample = `116675439200.7612`
          - **prob_below_capex** (float): sample = `0.2996`
          - **std** (float): sample = `68793675024.41576`
      - **STAK Energy**: object
        - **Object** containing keys:
          - **mean** (float): sample = `509118243557.8026`
          - **median** (float): sample = `280985578593.84937`
          - **p10** (float): sample = `-125727998389.05113`
          - **p25** (float): sample = `-14521513998.165398`
          - **p75** (float): sample = `751428632838.8228`
          - **p90** (float): sample = `1368181149195.4614`
          - **prob_below_capex** (float): sample = `0.3008`
          - **std** (float): sample = `854928838804.6492`
      - **Sailfish Digital**: object
        - **Object** containing keys:
          - **mean** (float): sample = `864931189259.1663`
          - **median** (float): sample = `479131467988.1587`
          - **p10** (float): sample = `-187535588895.83368`
          - **p25** (float): sample = `-20805281364.66423`
          - **p75** (float): sample = `1210790330737.0208`
          - **p90** (float): sample = `2360481162823.773`
          - **prob_below_capex** (float): sample = `0.2972`
          - **std** (float): sample = `1408686094109.3752`
      - **Stream Data Centers**: object
        - **Object** containing keys:
          - **mean** (float): sample = `34202857114.24575`
          - **median** (float): sample = `18234176154.14573`
          - **p10** (float): sample = `-8740932643.349052`
          - **p25** (float): sample = `-1465646572.4079266`
          - **p75** (float): sample = `49802704736.48352`
          - **p90** (float): sample = `92965980251.25792`
          - **prob_below_capex** (float): sample = `0.317`
          - **std** (float): sample = `57185219547.66962`
      - **Tract**: object
        - **Object** containing keys:
          - **mean** (float): sample = `416573945722.7565`
          - **median** (float): sample = `233205065745.5585`
          - **p10** (float): sample = `-98520438012.1109`
          - **p25** (float): sample = `-11484883912.759481`
          - **p75** (float): sample = `611724757802.2373`
          - **p90** (float): sample = `1145061374636.7065`
          - **prob_below_capex** (float): sample = `0.3`
          - **std** (float): sample = `664507600268.0295`
      - **Vantage**: object
        - **Object** containing keys:
          - **mean** (float): sample = `31156341405.30129`
          - **median** (float): sample = `17467449655.54345`
          - **p10** (float): sample = `-6169433353.450904`
          - **p25** (float): sample = `-596632002.2967451`
          - **p75** (float): sample = `44531307105.86664`
          - **p90** (float): sample = `82900060534.4213`
          - **prob_below_capex** (float): sample = `0.2924`
          - **std** (float): sample = `51256823738.89659`
      - **Vermaland**: object
        - **Object** containing keys:
          - **mean** (float): sample = `1060748374135.246`
          - **median** (float): sample = `566709975575.9252`
          - **p10** (float): sample = `-238548933449.48337`
          - **p25** (float): sample = `-35438093006.50159`
          - **p75** (float): sample = `1515169716322.1836`
          - **p90** (float): sample = `2960651064256.7686`
          - **prob_below_capex** (float): sample = `0.3048`
          - **std** (float): sample = `1739446887899.7222`
      - **xAI**: object
        - **Object** containing keys:
          - **mean** (float): sample = `34031430077.000813`
          - **median** (float): sample = `18446166421.131893`
          - **p10** (float): sample = `-7833177584.541601`
          - **p25** (float): sample = `-804107815.4530977`
          - **p75** (float): sample = `49590266572.411255`
          - **p90** (float): sample = `95744326950.65425`
          - **prob_below_capex** (float): sample = `0.304`
          - **std** (float): sample = `53830721844.98997`
  - **scenario_analysis**: object
    - **Object** containing keys:
      - **probabilities**: object
        - **Object** containing keys:
          - **base** (float): sample = `0.4`
          - **bear** (float): sample = `0.2`
          - **black_swan** (float): sample = `0.05`
          - **bull** (float): sample = `0.25`
          - **stagnation** (float): sample = `0.1`
      - **scenarios**: object
        - **Object** containing keys:
          - **base**: object
            - **Object** containing keys:
              - **scenario** (str): sample = `Gradual Deflation`
              - **terminal** (dict): sample = `None`
              - **yearly** (list): sample = `None`
          - **bear**: object
            - **Object** containing keys:
              - **scenario** (str): sample = `Bubble Burst`
              - **terminal** (dict): sample = `None`
              - **yearly** (list): sample = `None`
          - **black_swan**: object
            - **Object** containing keys:
              - **scenario** (str): sample = `TSMC+Recession`
              - **terminal** (dict): sample = `None`
              - **yearly** (list): sample = `None`
          - **bull**: object
            - **Object** containing keys:
              - **scenario** (str): sample = `Productivity Boom`
              - **terminal** (dict): sample = `None`
              - **yearly** (list): sample = `None`
          - **stagnation**: object
            - **Object** containing keys:
              - **scenario** (str): sample = `Japan Stagnation`
              - **terminal** (dict): sample = `None`
              - **yearly** (list): sample = `None`
      - **weighted**: object
        - **Object** containing keys:
          - **capex_5yr** (float): sample = `185858704998.40005`
          - **ebitda_5yr** (float): sample = `5006250109396.641`
          - **ev** (float): sample = `87055285672101.08`
          - **revenue_5yr** (float): sample = `5038688169345.641`
          - **roic_5yr** (float): sample = `5.276485180365318`
  - **scenario_matrix**: object
    - **Object** containing keys:
      - **A+B+C+D+E_1.0_0.2_0.3_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `29141139279.258186`
          - **ev** (float): sample = `129628672298.1654`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.3_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `29141139279.258186`
          - **ev** (float): sample = `100822300676.35086`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.3_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `29141139279.258186`
          - **ev** (float): sample = `72015929054.53633`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.3_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48345185867.35273`
          - **ev** (float): sample = `194443008447.2481`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.3_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48345185867.35273`
          - **ev** (float): sample = `151233451014.5263`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.3_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48345185867.35273`
          - **ev** (float): sample = `108023893581.8045`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.3_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `59867613820.20946`
          - **ev** (float): sample = `233331610136.69772`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.3_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `59867613820.20946`
          - **ev** (float): sample = `181480141217.43155`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.3_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `59867613820.20946`
          - **ev** (float): sample = `129628672298.1654`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `62915755506.98183`
          - **ev** (float): sample = `194443008447.2481`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `62915755506.98183`
          - **ev** (float): sample = `151233451014.5263`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `62915755506.98183`
          - **ev** (float): sample = `108023893581.8045`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `82119802095.07637`
          - **ev** (float): sample = `291664512670.8722`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `82119802095.07637`
          - **ev** (float): sample = `226850176521.78946`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `82119802095.07637`
          - **ev** (float): sample = `162035840372.70676`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `93642230047.9331`
          - **ev** (float): sample = `349997415205.04663`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `93642230047.9331`
          - **ev** (float): sample = `272220211826.14734`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `93642230047.9331`
          - **ev** (float): sample = `194443008447.2481`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.7_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `62915755506.98183`
          - **ev** (float): sample = `194443008447.2481`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.7_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `62915755506.98183`
          - **ev** (float): sample = `151233451014.5263`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.7_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `62915755506.98183`
          - **ev** (float): sample = `108023893581.8045`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.7_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `82119802095.07637`
          - **ev** (float): sample = `291664512670.8722`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.7_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `82119802095.07637`
          - **ev** (float): sample = `226850176521.78946`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.7_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `82119802095.07637`
          - **ev** (float): sample = `162035840372.70676`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.7_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `93642230047.9331`
          - **ev** (float): sample = `349997415205.04663`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.7_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `93642230047.9331`
          - **ev** (float): sample = `272220211826.14734`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.2_0.7_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `93642230047.9331`
          - **ev** (float): sample = `194443008447.2481`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.3_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.465454`
          - **ev** (float): sample = `97975159295.12502`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.3_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.465454`
          - **ev** (float): sample = `76202901673.98611`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.3_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.465454`
          - **ev** (float): sample = `54430644052.84723`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.3_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.559998`
          - **ev** (float): sample = `146962738942.68753`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.3_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.559998`
          - **ev** (float): sample = `114304352510.97917`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.3_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.559998`
          - **ev** (float): sample = `81645966079.27084`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.3_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.416725`
          - **ev** (float): sample = `176355286731.22504`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.3_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.416725`
          - **ev** (float): sample = `137165223013.17502`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.3_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.416725`
          - **ev** (float): sample = `97975159295.12502`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `146962738942.68753`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `114304352510.97917`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `81645966079.27084`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `220444108414.03128`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `171456528766.46875`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `122468949118.90627`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `264532930096.83755`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `205747834519.76254`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `146962738942.68753`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.7_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `146962738942.68753`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.7_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `114304352510.97917`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.7_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `81645966079.27084`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.7_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `220444108414.03128`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.7_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `171456528766.46875`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.7_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `122468949118.90627`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.7_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `264532930096.83755`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.7_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `205747834519.76254`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.5_0.7_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `146962738942.68753`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.3_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `55770475291.07116`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.3_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `43377036337.49979`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.3_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `30983597383.92842`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.3_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `83655712936.60674`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.3_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `65065554506.24968`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.3_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `46475396075.89263`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.3_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `762035421.6930904`
          - **ev** (float): sample = `100386855523.92809`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.3_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `762035421.6930904`
          - **ev** (float): sample = `78078665407.49962`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.3_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `762035421.6930904`
          - **ev** (float): sample = `55770475291.07116`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `83655712936.60674`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `65065554506.24968`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `46475396075.89263`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `125483569404.9101`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `97598331759.37451`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `69713094113.83894`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `4983862450.158545`
          - **ev** (float): sample = `150580283285.89212`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `4983862450.158545`
          - **ev** (float): sample = `117117998111.24942`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `4983862450.158545`
          - **ev** (float): sample = `83655712936.60674`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.7_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `83655712936.60674`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.7_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `65065554506.24968`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.7_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `46475396075.89263`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.7_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `125483569404.9101`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.7_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `97598331759.37451`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.7_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `69713094113.83894`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.7_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `4983862450.158545`
          - **ev** (float): sample = `150580283285.89212`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.7_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `4983862450.158545`
          - **ev** (float): sample = `117117998111.24942`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_1.0_0.9_0.7_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `4983862450.158545`
          - **ev** (float): sample = `83655712936.60674`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.3_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6624728460.775764`
          - **ev** (float): sample = `97221504223.62405`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.3_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6624728460.775764`
          - **ev** (float): sample = `75616725507.26315`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.3_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6624728460.775764`
          - **ev** (float): sample = `54011946790.90225`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.3_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `25828775048.870308`
          - **ev** (float): sample = `145832256335.4361`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.3_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `25828775048.870308`
          - **ev** (float): sample = `113425088260.89473`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.3_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `25828775048.870308`
          - **ev** (float): sample = `81017920186.35338`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.3_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `37351203001.727036`
          - **ev** (float): sample = `174998707602.52332`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.3_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `37351203001.727036`
          - **ev** (float): sample = `136110105913.07367`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.3_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `37351203001.727036`
          - **ev** (float): sample = `97221504223.62405`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `29141139279.258194`
          - **ev** (float): sample = `145832256335.4361`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `29141139279.258194`
          - **ev** (float): sample = `113425088260.89473`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `29141139279.258194`
          - **ev** (float): sample = `81017920186.35338`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48345185867.35274`
          - **ev** (float): sample = `218748384503.1541`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48345185867.35274`
          - **ev** (float): sample = `170137632391.34207`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48345185867.35274`
          - **ev** (float): sample = `121526880279.53006`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `59867613820.209465`
          - **ev** (float): sample = `262498061403.78497`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `59867613820.209465`
          - **ev** (float): sample = `204165158869.61053`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `59867613820.209465`
          - **ev** (float): sample = `145832256335.4361`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.7_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `29141139279.258194`
          - **ev** (float): sample = `145832256335.4361`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.7_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `29141139279.258194`
          - **ev** (float): sample = `113425088260.89473`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.7_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `29141139279.258194`
          - **ev** (float): sample = `81017920186.35338`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.7_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48345185867.35274`
          - **ev** (float): sample = `218748384503.1541`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.7_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48345185867.35274`
          - **ev** (float): sample = `170137632391.34207`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.7_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48345185867.35274`
          - **ev** (float): sample = `121526880279.53006`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.7_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `59867613820.209465`
          - **ev** (float): sample = `262498061403.78497`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.7_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `59867613820.209465`
          - **ev** (float): sample = `204165158869.61053`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.2_0.7_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `59867613820.209465`
          - **ev** (float): sample = `145832256335.4361`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.3_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `73481369471.34377`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.3_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `57152176255.489586`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.3_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `40822983039.63542`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.3_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8941466935.008488`
          - **ev** (float): sample = `110222054207.01564`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.3_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8941466935.008488`
          - **ev** (float): sample = `85728264383.23438`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.3_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8941466935.008488`
          - **ev** (float): sample = `61234474559.45313`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.3_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `20463894887.865215`
          - **ev** (float): sample = `132266465048.41878`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.3_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `20463894887.865215`
          - **ev** (float): sample = `102873917259.88127`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.3_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `20463894887.865215`
          - **ev** (float): sample = `73481369471.34377`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.4654617`
          - **ev** (float): sample = `110222054207.01566`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.4654617`
          - **ev** (float): sample = `85728264383.23439`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.4654617`
          - **ev** (float): sample = `61234474559.45314`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.560005`
          - **ev** (float): sample = `165333081310.5235`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.560005`
          - **ev** (float): sample = `128592396574.8516`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.560005`
          - **ev** (float): sample = `91851711839.17972`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.41673`
          - **ev** (float): sample = `198399697572.62817`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.41673`
          - **ev** (float): sample = `154310875889.8219`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.41673`
          - **ev** (float): sample = `110222054207.01566`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.7_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.4654617`
          - **ev** (float): sample = `110222054207.01566`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.7_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.4654617`
          - **ev** (float): sample = `85728264383.23439`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.7_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.4654617`
          - **ev** (float): sample = `61234474559.45314`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.7_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.560005`
          - **ev** (float): sample = `165333081310.5235`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.7_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.560005`
          - **ev** (float): sample = `128592396574.8516`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.7_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.560005`
          - **ev** (float): sample = `91851711839.17972`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.7_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.41673`
          - **ev** (float): sample = `198399697572.62817`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.7_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.41673`
          - **ev** (float): sample = `154310875889.8219`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.5_0.7_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.41673`
          - **ev** (float): sample = `110222054207.01566`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.3_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `41827856468.303375`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.3_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `32532777253.124844`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.3_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `23237698037.94632`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.3_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `62741784702.45506`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.3_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `48799165879.68727`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.3_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `34856547056.91948`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.3_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `75290141642.94608`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.3_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `58558999055.624725`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.3_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `41827856468.303375`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `62741784702.45506`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `48799165879.68727`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `34856547056.91948`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `94112677053.6826`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `73198748819.5309`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `52284820585.37922`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `762035421.6930923`
          - **ev** (float): sample = `112935212464.41911`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `762035421.6930923`
          - **ev** (float): sample = `87838498583.43709`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `762035421.6930923`
          - **ev** (float): sample = `62741784702.45506`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.7_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `62741784702.45506`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.7_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `48799165879.68727`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.7_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `34856547056.91948`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.7_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `94112677053.6826`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.7_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `73198748819.5309`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.7_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `52284820585.37922`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.7_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `762035421.6930923`
          - **ev** (float): sample = `112935212464.41911`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.7_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `762035421.6930923`
          - **ev** (float): sample = `87838498583.43709`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_2.0_0.9_0.7_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `762035421.6930923`
          - **ev** (float): sample = `62741784702.45506`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.3_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `77777203378.89923`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.3_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `60493380405.81051`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.3_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `43209557432.721794`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.3_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `14570569639.629093`
          - **ev** (float): sample = `116665805068.34885`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.3_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `14570569639.629093`
          - **ev** (float): sample = `90740070608.71576`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.3_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `14570569639.629093`
          - **ev** (float): sample = `64814336149.08269`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.3_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `26092997592.48582`
          - **ev** (float): sample = `139998966082.01862`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.3_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `26092997592.48582`
          - **ev** (float): sample = `108888084730.45892`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.3_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `26092997592.48582`
          - **ev** (float): sample = `77777203378.89923`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12253831165.39637`
          - **ev** (float): sample = `116665805068.34885`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12253831165.39637`
          - **ev** (float): sample = `90740070608.71577`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12253831165.39637`
          - **ev** (float): sample = `64814336149.082695`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31457877753.490913`
          - **ev** (float): sample = `174998707602.5233`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31457877753.490913`
          - **ev** (float): sample = `136110105913.07364`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31457877753.490913`
          - **ev** (float): sample = `97221504223.62404`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42980305706.34764`
          - **ev** (float): sample = `209998449123.02792`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42980305706.34764`
          - **ev** (float): sample = `163332127095.6884`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42980305706.34764`
          - **ev** (float): sample = `116665805068.34885`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.7_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12253831165.39637`
          - **ev** (float): sample = `116665805068.34885`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.7_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12253831165.39637`
          - **ev** (float): sample = `90740070608.71577`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.7_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12253831165.39637`
          - **ev** (float): sample = `64814336149.082695`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.7_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31457877753.490913`
          - **ev** (float): sample = `174998707602.5233`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.7_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31457877753.490913`
          - **ev** (float): sample = `136110105913.07364`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.7_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31457877753.490913`
          - **ev** (float): sample = `97221504223.62404`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.7_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42980305706.34764`
          - **ev** (float): sample = `209998449123.02792`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.7_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42980305706.34764`
          - **ev** (float): sample = `163332127095.6884`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.2_0.7_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42980305706.34764`
          - **ev** (float): sample = `116665805068.34885`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.3_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `58785095577.075005`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.3_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `45721741004.39167`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.3_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `32658386431.708336`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.3_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `1905088554.232727`
          - **ev** (float): sample = `88177643365.6125`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.3_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `1905088554.232727`
          - **ev** (float): sample = `68582611506.587494`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.3_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `1905088554.232727`
          - **ev** (float): sample = `48987579647.5625`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.3_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `13427516507.089455`
          - **ev** (float): sample = `105813172038.73502`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.3_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `13427516507.089455`
          - **ev** (float): sample = `82299133807.905`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.3_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `13427516507.089455`
          - **ev** (float): sample = `58785095577.075005`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `88177643365.61252`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `68582611506.58751`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `48987579647.56251`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12459656125.396366`
          - **ev** (float): sample = `132266465048.41878`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12459656125.396366`
          - **ev** (float): sample = `102873917259.88127`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12459656125.396366`
          - **ev** (float): sample = `73481369471.34377`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23982084078.253094`
          - **ev** (float): sample = `158719758058.10254`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23982084078.253094`
          - **ev** (float): sample = `123448700711.85751`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23982084078.253094`
          - **ev** (float): sample = `88177643365.61252`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.7_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `88177643365.61252`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.7_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `68582611506.58751`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.7_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `48987579647.56251`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.7_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12459656125.396366`
          - **ev** (float): sample = `132266465048.41878`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.7_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12459656125.396366`
          - **ev** (float): sample = `102873917259.88127`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.7_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12459656125.396366`
          - **ev** (float): sample = `73481369471.34377`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.7_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23982084078.253094`
          - **ev** (float): sample = `158719758058.10254`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.7_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23982084078.253094`
          - **ev** (float): sample = `123448700711.85751`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.5_0.7_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23982084078.253094`
          - **ev** (float): sample = `88177643365.61252`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.3_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `33462285174.642693`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.3_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `26026221802.49987`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.3_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `18590158430.35705`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.3_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `50193427761.964035`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.3_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `39039332703.7498`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.3_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `27885237645.535576`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.3_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `60232113314.35685`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.3_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `46847199244.49976`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.3_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `33462285174.642693`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `50193427761.96404`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `39039332703.74981`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `27885237645.53558`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `75290141642.94606`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `58558999055.62471`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `41827856468.30337`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `90348169971.53528`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `70270798866.74965`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `50193427761.96404`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.7_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `50193427761.96404`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.7_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `39039332703.74981`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.7_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `27885237645.53558`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.7_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `75290141642.94606`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.7_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `58558999055.62471`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.7_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `41827856468.30337`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.7_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `90348169971.53528`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.7_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `70270798866.74965`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D+E_3.0_0.9_0.7_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `50193427761.96404`
          - **levels**: array
            - **Array** of length 5 containing `float` items.
          - **perspectives**: array
            - **Array** of length 5 containing `str` items.
      - **A+B+C+D_1.0_0.2_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `29141139279.258186`
          - **ev** (float): sample = `144031858109.07266`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.2_0.3_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48345185867.35273`
          - **ev** (float): sample = `216047787163.609`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.2_0.3_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `59867613820.20946`
          - **ev** (float): sample = `259257344596.3308`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.2_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `62915755506.98183`
          - **ev** (float): sample = `216047787163.609`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.2_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `82119802095.07637`
          - **ev** (float): sample = `324071680745.4135`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.2_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `93642230047.9331`
          - **ev** (float): sample = `388886016894.4962`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.2_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `62915755506.98183`
          - **ev** (float): sample = `216047787163.609`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.2_0.7_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `82119802095.07637`
          - **ev** (float): sample = `324071680745.4135`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.2_0.7_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `93642230047.9331`
          - **ev** (float): sample = `388886016894.4962`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.5_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.465454`
          - **ev** (float): sample = `108861288105.69446`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.5_0.3_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.559998`
          - **ev** (float): sample = `163291932158.5417`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.5_0.3_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.416725`
          - **ev** (float): sample = `195950318590.25003`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `163291932158.5417`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.5_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `244937898237.81253`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.5_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `293925477885.37506`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.5_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `163291932158.5417`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.5_0.7_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `244937898237.81253`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.5_0.7_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `293925477885.37506`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.9_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `61967194767.85684`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.9_0.3_0.75**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `92950792151.78526`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.9_0.3_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `762035421.6930904`
          - **ev** (float): sample = `111540950582.14232`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.9_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `92950792151.78526`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.9_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `139426188227.6779`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.9_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `4983862450.158545`
          - **ev** (float): sample = `167311425873.21347`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.9_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `92950792151.78526`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.9_0.7_0.75**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `139426188227.6779`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_1.0_0.9_0.7_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `4983862450.158545`
          - **ev** (float): sample = `167311425873.21347`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.2_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6624728460.775764`
          - **ev** (float): sample = `108023893581.8045`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.2_0.3_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `25828775048.870308`
          - **ev** (float): sample = `162035840372.70676`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.2_0.3_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `37351203001.727036`
          - **ev** (float): sample = `194443008447.2481`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.2_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `29141139279.258194`
          - **ev** (float): sample = `162035840372.70676`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.2_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48345185867.35274`
          - **ev** (float): sample = `243053760559.06012`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.2_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `59867613820.209465`
          - **ev** (float): sample = `291664512670.8722`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.2_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `29141139279.258194`
          - **ev** (float): sample = `162035840372.70676`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.2_0.7_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48345185867.35274`
          - **ev** (float): sample = `243053760559.06012`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.2_0.7_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `59867613820.209465`
          - **ev** (float): sample = `291664512670.8722`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.5_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `81645966079.27084`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.5_0.3_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8941466935.008488`
          - **ev** (float): sample = `122468949118.90627`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.5_0.3_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `20463894887.865215`
          - **ev** (float): sample = `146962738942.68753`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.4654617`
          - **ev** (float): sample = `122468949118.90628`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.5_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.560005`
          - **ev** (float): sample = `183703423678.35944`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.5_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.41673`
          - **ev** (float): sample = `220444108414.0313`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.5_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.4654617`
          - **ev** (float): sample = `122468949118.90628`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.5_0.7_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.560005`
          - **ev** (float): sample = `183703423678.35944`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.5_0.7_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.41673`
          - **ev** (float): sample = `220444108414.0313`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.9_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `46475396075.89264`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.9_0.3_0.75**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `69713094113.83896`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.9_0.3_0.9**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `83655712936.60675`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.9_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `69713094113.83896`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.9_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `104569641170.75844`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.9_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `762035421.6930923`
          - **ev** (float): sample = `125483569404.91013`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.9_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `69713094113.83896`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.9_0.7_0.75**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `104569641170.75844`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_2.0_0.9_0.7_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `762035421.6930923`
          - **ev** (float): sample = `125483569404.91013`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.2_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `86419114865.44359`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.2_0.3_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `14570569639.629093`
          - **ev** (float): sample = `129628672298.16537`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.2_0.3_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `26092997592.48582`
          - **ev** (float): sample = `155554406757.79846`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.2_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12253831165.39637`
          - **ev** (float): sample = `129628672298.16539`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.2_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31457877753.490913`
          - **ev** (float): sample = `194443008447.24808`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.2_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42980305706.34764`
          - **ev** (float): sample = `233331610136.6977`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.2_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12253831165.39637`
          - **ev** (float): sample = `129628672298.16539`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.2_0.7_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31457877753.490913`
          - **ev** (float): sample = `194443008447.24808`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.2_0.7_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42980305706.34764`
          - **ev** (float): sample = `233331610136.6977`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.5_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `65316772863.41667`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.5_0.3_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `1905088554.232727`
          - **ev** (float): sample = `97975159295.125`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.5_0.3_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `13427516507.089455`
          - **ev** (float): sample = `117570191154.15001`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `97975159295.12502`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.5_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12459656125.396366`
          - **ev** (float): sample = `146962738942.68753`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.5_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23982084078.253094`
          - **ev** (float): sample = `176355286731.22504`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.5_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `97975159295.12502`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.5_0.7_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12459656125.396366`
          - **ev** (float): sample = `146962738942.68753`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.5_0.7_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23982084078.253094`
          - **ev** (float): sample = `176355286731.22504`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.9_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `37180316860.7141`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.9_0.3_0.75**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `55770475291.07115`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.9_0.3_0.9**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `66924570349.285385`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.9_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `55770475291.07116`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.9_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `83655712936.60674`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.9_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `100386855523.92809`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.9_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `55770475291.07116`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.9_0.7_0.75**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `83655712936.60674`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+D_3.0_0.9_0.7_0.9**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `100386855523.92809`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.2_0.3_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `67549232455.44727`
          - **ev** (float): sample = `259257344596.3308`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.2_0.3_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `67549232455.44727`
          - **ev** (float): sample = `201644601352.70172`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.2_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `67549232455.44727`
          - **ev** (float): sample = `144031858109.07266`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.2_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `101323848683.17091`
          - **ev** (float): sample = `388886016894.4962`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.2_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `101323848683.17091`
          - **ev** (float): sample = `302466902029.0526`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.2_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `101323848683.17091`
          - **ev** (float): sample = `216047787163.609`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.2_0.7_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `101323848683.17091`
          - **ev** (float): sample = `388886016894.4962`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.2_0.7_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `101323848683.17091`
          - **ev** (float): sample = `302466902029.0526`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.2_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `101323848683.17091`
          - **ev** (float): sample = `216047787163.609`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.5_0.3_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65454`
          - **ev** (float): sample = `195950318590.25003`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.5_0.3_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65454`
          - **ev** (float): sample = `152405803347.97223`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.5_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65454`
          - **ev** (float): sample = `108861288105.69446`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `293925477885.37506`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `228608705021.95834`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `163291932158.5417`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.5_0.7_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `293925477885.37506`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.5_0.7_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `228608705021.95834`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.5_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `163291932158.5417`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.9_0.3_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8443654056.930906`
          - **ev** (float): sample = `111540950582.14232`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.9_0.3_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8443654056.930906`
          - **ev** (float): sample = `86754072674.99957`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.9_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8443654056.930906`
          - **ev** (float): sample = `61967194767.85684`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.9_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12665481085.39636`
          - **ev** (float): sample = `167311425873.21347`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.9_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12665481085.39636`
          - **ev** (float): sample = `130131109012.49936`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.9_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12665481085.39636`
          - **ev** (float): sample = `92950792151.78526`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.9_0.7_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12665481085.39636`
          - **ev** (float): sample = `167311425873.21347`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.9_0.7_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12665481085.39636`
          - **ev** (float): sample = `130131109012.49936`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_1.0_0.9_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12665481085.39636`
          - **ev** (float): sample = `92950792151.78526`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.2_0.3_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `45032821636.96485`
          - **ev** (float): sample = `194443008447.2481`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.2_0.3_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `45032821636.96485`
          - **ev** (float): sample = `151233451014.5263`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.2_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `45032821636.96485`
          - **ev** (float): sample = `108023893581.8045`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.2_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `67549232455.44728`
          - **ev** (float): sample = `291664512670.8722`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.2_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `67549232455.44728`
          - **ev** (float): sample = `226850176521.78946`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.2_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `67549232455.44728`
          - **ev** (float): sample = `162035840372.70676`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.2_0.7_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `67549232455.44728`
          - **ev** (float): sample = `291664512670.8722`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.2_0.7_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `67549232455.44728`
          - **ev** (float): sample = `226850176521.78946`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.2_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `67549232455.44728`
          - **ev** (float): sample = `162035840372.70676`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.5_0.3_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `28145513523.10303`
          - **ev** (float): sample = `146962738942.68753`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.5_0.3_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `28145513523.10303`
          - **ev** (float): sample = `114304352510.97917`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.5_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `28145513523.10303`
          - **ev** (float): sample = `81645966079.27084`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65455`
          - **ev** (float): sample = `220444108414.0313`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65455`
          - **ev** (float): sample = `171456528766.46878`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65455`
          - **ev** (float): sample = `122468949118.90628`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.5_0.7_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65455`
          - **ev** (float): sample = `220444108414.0313`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.5_0.7_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65455`
          - **ev** (float): sample = `171456528766.46878`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.5_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65455`
          - **ev** (float): sample = `122468949118.90628`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.9_0.3_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `5629102704.620605`
          - **ev** (float): sample = `83655712936.60675`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.9_0.3_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `5629102704.620605`
          - **ev** (float): sample = `65065554506.24969`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.9_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `5629102704.620605`
          - **ev** (float): sample = `46475396075.89264`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.9_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8443654056.930908`
          - **ev** (float): sample = `125483569404.91013`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.9_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8443654056.930908`
          - **ev** (float): sample = `97598331759.37454`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.9_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8443654056.930908`
          - **ev** (float): sample = `69713094113.83896`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.9_0.7_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8443654056.930908`
          - **ev** (float): sample = `125483569404.91013`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.9_0.7_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8443654056.930908`
          - **ev** (float): sample = `97598331759.37454`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_2.0_0.9_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8443654056.930908`
          - **ev** (float): sample = `69713094113.83896`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.2_0.3_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `33774616227.723637`
          - **ev** (float): sample = `155554406757.79846`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.2_0.3_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `33774616227.723637`
          - **ev** (float): sample = `120986760811.62102`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.2_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `33774616227.723637`
          - **ev** (float): sample = `86419114865.44359`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.2_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `50661924341.58546`
          - **ev** (float): sample = `233331610136.6977`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.2_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `50661924341.58546`
          - **ev** (float): sample = `181480141217.43155`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.2_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `50661924341.58546`
          - **ev** (float): sample = `129628672298.16539`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.2_0.7_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `50661924341.58546`
          - **ev** (float): sample = `233331610136.6977`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.2_0.7_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `50661924341.58546`
          - **ev** (float): sample = `181480141217.43155`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.2_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `50661924341.58546`
          - **ev** (float): sample = `129628672298.16539`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.5_0.3_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `21109135142.32727`
          - **ev** (float): sample = `117570191154.15001`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.5_0.3_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `21109135142.32727`
          - **ev** (float): sample = `91443482008.78334`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.5_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `21109135142.32727`
          - **ev** (float): sample = `65316772863.41667`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31663702713.49091`
          - **ev** (float): sample = `176355286731.22504`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31663702713.49091`
          - **ev** (float): sample = `137165223013.17502`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31663702713.49091`
          - **ev** (float): sample = `97975159295.12502`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.5_0.7_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31663702713.49091`
          - **ev** (float): sample = `176355286731.22504`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.5_0.7_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31663702713.49091`
          - **ev** (float): sample = `137165223013.17502`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.5_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31663702713.49091`
          - **ev** (float): sample = `97975159295.12502`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.9_0.3_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `4221827028.465453`
          - **ev** (float): sample = `66924570349.285385`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.9_0.3_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `4221827028.465453`
          - **ev** (float): sample = `52052443604.99974`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.9_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `4221827028.465453`
          - **ev** (float): sample = `37180316860.7141`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.9_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6332740542.69818`
          - **ev** (float): sample = `100386855523.92809`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.9_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6332740542.69818`
          - **ev** (float): sample = `78078665407.49962`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.9_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6332740542.69818`
          - **ev** (float): sample = `55770475291.07116`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.9_0.7_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6332740542.69818`
          - **ev** (float): sample = `100386855523.92809`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.9_0.7_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6332740542.69818`
          - **ev** (float): sample = `78078665407.49962`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C+E_3.0_0.9_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6332740542.69818`
          - **ev** (float): sample = `55770475291.07116`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+C_1.0_0.2_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `67549232455.44727`
          - **ev** (float): sample = `288063716218.1453`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_1.0_0.2_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `101323848683.17091`
          - **ev** (float): sample = `432095574327.218`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_1.0_0.2_0.7**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `101323848683.17091`
          - **ev** (float): sample = `432095574327.218`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_1.0_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65454`
          - **ev** (float): sample = `217722576211.38892`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_1.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `326583864317.0834`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_1.0_0.5_0.7**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `326583864317.0834`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_1.0_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8443654056.930906`
          - **ev** (float): sample = `123934389535.71368`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_1.0_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12665481085.39636`
          - **ev** (float): sample = `185901584303.57053`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_1.0_0.9_0.7**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12665481085.39636`
          - **ev** (float): sample = `185901584303.57053`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_2.0_0.2_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `45032821636.96485`
          - **ev** (float): sample = `216047787163.609`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_2.0_0.2_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `67549232455.44728`
          - **ev** (float): sample = `324071680745.4135`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_2.0_0.2_0.7**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `67549232455.44728`
          - **ev** (float): sample = `324071680745.4135`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_2.0_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `28145513523.10303`
          - **ev** (float): sample = `163291932158.5417`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_2.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65455`
          - **ev** (float): sample = `244937898237.81256`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_2.0_0.5_0.7**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65455`
          - **ev** (float): sample = `244937898237.81256`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_2.0_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `5629102704.620605`
          - **ev** (float): sample = `92950792151.78528`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_2.0_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8443654056.930908`
          - **ev** (float): sample = `139426188227.67792`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_2.0_0.9_0.7**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8443654056.930908`
          - **ev** (float): sample = `139426188227.67792`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_3.0_0.2_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `33774616227.723637`
          - **ev** (float): sample = `172838229730.88718`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_3.0_0.2_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `50661924341.58546`
          - **ev** (float): sample = `259257344596.33078`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_3.0_0.2_0.7**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `50661924341.58546`
          - **ev** (float): sample = `259257344596.33078`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_3.0_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `21109135142.32727`
          - **ev** (float): sample = `130633545726.83334`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_3.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31663702713.49091`
          - **ev** (float): sample = `195950318590.25003`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_3.0_0.5_0.7**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31663702713.49091`
          - **ev** (float): sample = `195950318590.25003`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_3.0_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `4221827028.465453`
          - **ev** (float): sample = `74360633721.4282`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_3.0_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6332740542.69818`
          - **ev** (float): sample = `111540950582.14232`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+C_3.0_0.9_0.7**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6332740542.69818`
          - **ev** (float): sample = `111540950582.14232`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D+E_1.0_0.2_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `62915755506.98183`
          - **ev** (float): sample = `194443008447.2481`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.2_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `62915755506.98183`
          - **ev** (float): sample = `151233451014.5263`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.2_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `62915755506.98183`
          - **ev** (float): sample = `108023893581.8045`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.2_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `82119802095.07637`
          - **ev** (float): sample = `291664512670.8722`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.2_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `82119802095.07637`
          - **ev** (float): sample = `226850176521.78946`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.2_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `82119802095.07637`
          - **ev** (float): sample = `162035840372.70676`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.2_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `93642230047.9331`
          - **ev** (float): sample = `349997415205.04663`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.2_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `93642230047.9331`
          - **ev** (float): sample = `272220211826.14734`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.2_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `93642230047.9331`
          - **ev** (float): sample = `194443008447.2481`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `146962738942.68753`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `114304352510.97917`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `81645966079.27084`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `220444108414.03128`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `171456528766.46875`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `122468949118.90627`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `264532930096.83755`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `205747834519.76254`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `146962738942.68753`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.9_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `83655712936.60674`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.9_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `65065554506.24968`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.9_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `46475396075.89263`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.9_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `125483569404.9101`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.9_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `97598331759.37451`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.9_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `69713094113.83894`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.9_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `4983862450.158545`
          - **ev** (float): sample = `150580283285.89212`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.9_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `4983862450.158545`
          - **ev** (float): sample = `117117998111.24942`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_1.0_0.9_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `4983862450.158545`
          - **ev** (float): sample = `83655712936.60674`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.2_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `29141139279.258194`
          - **ev** (float): sample = `145832256335.4361`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.2_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `29141139279.258194`
          - **ev** (float): sample = `113425088260.89473`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.2_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `29141139279.258194`
          - **ev** (float): sample = `81017920186.35338`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.2_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48345185867.35274`
          - **ev** (float): sample = `218748384503.1541`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.2_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48345185867.35274`
          - **ev** (float): sample = `170137632391.34207`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.2_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48345185867.35274`
          - **ev** (float): sample = `121526880279.53006`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.2_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `59867613820.209465`
          - **ev** (float): sample = `262498061403.78497`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.2_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `59867613820.209465`
          - **ev** (float): sample = `204165158869.61053`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.2_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `59867613820.209465`
          - **ev** (float): sample = `145832256335.4361`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.4654617`
          - **ev** (float): sample = `110222054207.01566`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.4654617`
          - **ev** (float): sample = `85728264383.23439`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.4654617`
          - **ev** (float): sample = `61234474559.45314`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.560005`
          - **ev** (float): sample = `165333081310.5235`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.560005`
          - **ev** (float): sample = `128592396574.8516`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.560005`
          - **ev** (float): sample = `91851711839.17972`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.41673`
          - **ev** (float): sample = `198399697572.62817`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.41673`
          - **ev** (float): sample = `154310875889.8219`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.41673`
          - **ev** (float): sample = `110222054207.01566`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.9_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `62741784702.45506`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.9_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `48799165879.68727`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.9_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `34856547056.91948`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.9_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `94112677053.6826`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.9_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `73198748819.5309`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.9_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `52284820585.37922`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.9_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `762035421.6930923`
          - **ev** (float): sample = `112935212464.41911`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.9_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `762035421.6930923`
          - **ev** (float): sample = `87838498583.43709`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_2.0_0.9_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `762035421.6930923`
          - **ev** (float): sample = `62741784702.45506`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.2_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12253831165.39637`
          - **ev** (float): sample = `116665805068.34885`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.2_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12253831165.39637`
          - **ev** (float): sample = `90740070608.71577`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.2_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12253831165.39637`
          - **ev** (float): sample = `64814336149.082695`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.2_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31457877753.490913`
          - **ev** (float): sample = `174998707602.5233`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.2_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31457877753.490913`
          - **ev** (float): sample = `136110105913.07364`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.2_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31457877753.490913`
          - **ev** (float): sample = `97221504223.62404`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.2_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42980305706.34764`
          - **ev** (float): sample = `209998449123.02792`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.2_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42980305706.34764`
          - **ev** (float): sample = `163332127095.6884`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.2_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42980305706.34764`
          - **ev** (float): sample = `116665805068.34885`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `88177643365.61252`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `68582611506.58751`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `48987579647.56251`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12459656125.396366`
          - **ev** (float): sample = `132266465048.41878`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12459656125.396366`
          - **ev** (float): sample = `102873917259.88127`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12459656125.396366`
          - **ev** (float): sample = `73481369471.34377`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23982084078.253094`
          - **ev** (float): sample = `158719758058.10254`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23982084078.253094`
          - **ev** (float): sample = `123448700711.85751`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23982084078.253094`
          - **ev** (float): sample = `88177643365.61252`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.9_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `50193427761.96404`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.9_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `39039332703.74981`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.9_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `27885237645.53558`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.9_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `75290141642.94606`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.9_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `58558999055.62471`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.9_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `41827856468.30337`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.9_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `90348169971.53528`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.9_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `70270798866.74965`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D+E_3.0_0.9_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `50193427761.96404`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+B+D_1.0_0.2_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `62915755506.98183`
          - **ev** (float): sample = `216047787163.609`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_1.0_0.2_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `82119802095.07637`
          - **ev** (float): sample = `324071680745.4135`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_1.0_0.2_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `93642230047.9331`
          - **ev** (float): sample = `388886016894.4962`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_1.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `163291932158.5417`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_1.0_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `244937898237.81253`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_1.0_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `293925477885.37506`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_1.0_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `92950792151.78526`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_1.0_0.9_0.75**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `139426188227.6779`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_1.0_0.9_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `4983862450.158545`
          - **ev** (float): sample = `167311425873.21347`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_2.0_0.2_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `29141139279.258194`
          - **ev** (float): sample = `162035840372.70676`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_2.0_0.2_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48345185867.35274`
          - **ev** (float): sample = `243053760559.06012`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_2.0_0.2_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `59867613820.209465`
          - **ev** (float): sample = `291664512670.8722`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_2.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.4654617`
          - **ev** (float): sample = `122468949118.90628`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_2.0_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.560005`
          - **ev** (float): sample = `183703423678.35944`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_2.0_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.41673`
          - **ev** (float): sample = `220444108414.0313`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_2.0_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `69713094113.83896`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_2.0_0.9_0.75**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `104569641170.75844`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_2.0_0.9_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `762035421.6930923`
          - **ev** (float): sample = `125483569404.91013`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_3.0_0.2_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12253831165.39637`
          - **ev** (float): sample = `129628672298.16539`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_3.0_0.2_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31457877753.490913`
          - **ev** (float): sample = `194443008447.24808`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_3.0_0.2_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42980305706.34764`
          - **ev** (float): sample = `233331610136.6977`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_3.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `97975159295.12502`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_3.0_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12459656125.396366`
          - **ev** (float): sample = `146962738942.68753`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_3.0_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23982084078.253094`
          - **ev** (float): sample = `176355286731.22504`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_3.0_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `55770475291.07116`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_3.0_0.9_0.75**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `83655712936.60674`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+D_3.0_0.9_0.9**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `100386855523.92809`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_1.0_0.2_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `101323848683.17091`
          - **ev** (float): sample = `388886016894.4962`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_1.0_0.2_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `101323848683.17091`
          - **ev** (float): sample = `302466902029.0526`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_1.0_0.2_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `101323848683.17091`
          - **ev** (float): sample = `216047787163.609`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_1.0_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `293925477885.37506`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_1.0_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `228608705021.95834`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_1.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `163291932158.5417`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_1.0_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12665481085.39636`
          - **ev** (float): sample = `167311425873.21347`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_1.0_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12665481085.39636`
          - **ev** (float): sample = `130131109012.49936`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_1.0_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12665481085.39636`
          - **ev** (float): sample = `92950792151.78526`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_2.0_0.2_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `67549232455.44728`
          - **ev** (float): sample = `291664512670.8722`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_2.0_0.2_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `67549232455.44728`
          - **ev** (float): sample = `226850176521.78946`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_2.0_0.2_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `67549232455.44728`
          - **ev** (float): sample = `162035840372.70676`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_2.0_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65455`
          - **ev** (float): sample = `220444108414.0313`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_2.0_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65455`
          - **ev** (float): sample = `171456528766.46878`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_2.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65455`
          - **ev** (float): sample = `122468949118.90628`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_2.0_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8443654056.930908`
          - **ev** (float): sample = `125483569404.91013`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_2.0_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8443654056.930908`
          - **ev** (float): sample = `97598331759.37454`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_2.0_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8443654056.930908`
          - **ev** (float): sample = `69713094113.83896`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_3.0_0.2_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `50661924341.58546`
          - **ev** (float): sample = `233331610136.6977`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_3.0_0.2_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `50661924341.58546`
          - **ev** (float): sample = `181480141217.43155`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_3.0_0.2_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `50661924341.58546`
          - **ev** (float): sample = `129628672298.16539`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_3.0_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31663702713.49091`
          - **ev** (float): sample = `176355286731.22504`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_3.0_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31663702713.49091`
          - **ev** (float): sample = `137165223013.17502`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_3.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31663702713.49091`
          - **ev** (float): sample = `97975159295.12502`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_3.0_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6332740542.69818`
          - **ev** (float): sample = `100386855523.92809`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_3.0_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6332740542.69818`
          - **ev** (float): sample = `78078665407.49962`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B+E_3.0_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6332740542.69818`
          - **ev** (float): sample = `55770475291.07116`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+B_1.0_0.2**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `101323848683.17091`
          - **ev** (float): sample = `432095574327.218`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+B_1.0_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `326583864317.0834`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+B_1.0_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `12665481085.39636`
          - **ev** (float): sample = `185901584303.57053`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+B_2.0_0.2**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `67549232455.44728`
          - **ev** (float): sample = `324071680745.4135`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+B_2.0_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65455`
          - **ev** (float): sample = `244937898237.81256`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+B_2.0_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `8443654056.930908`
          - **ev** (float): sample = `139426188227.67792`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+B_3.0_0.2**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `50661924341.58546`
          - **ev** (float): sample = `259257344596.33078`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+B_3.0_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `31663702713.49091`
          - **ev** (float): sample = `195950318590.25003`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+B_3.0_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6332740542.69818`
          - **ev** (float): sample = `111540950582.14232`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+C+D+E_1.0_0.3_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.119995`
          - **ev** (float): sample = `150731014300.19232`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.3_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.119995`
          - **ev** (float): sample = `117235233344.59401`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.3_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.119995`
          - **ev** (float): sample = `83739452388.99573`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.3_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.21454`
          - **ev** (float): sample = `226096521450.28848`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.3_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.21454`
          - **ev** (float): sample = `175852850016.89102`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.3_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.21454`
          - **ev** (float): sample = `125609178583.49359`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.3_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07126`
          - **ev** (float): sample = `271315825740.3462`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.3_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07126`
          - **ev** (float): sample = `211023420020.26923`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.3_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07126`
          - **ev** (float): sample = `150731014300.19232`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `226096521450.28848`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `175852850016.89105`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `125609178583.4936`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `339144782175.43274`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `263779275025.33658`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `188413767875.24042`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `406973738610.5193`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `316535130030.4039`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `226096521450.28848`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.7_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `226096521450.28848`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.7_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `175852850016.89105`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.7_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `125609178583.4936`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.7_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `339144782175.43274`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.7_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `263779275025.33658`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.7_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `188413767875.24042`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.7_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `406973738610.5193`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.7_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `316535130030.4039`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_1.0_0.7_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `226096521450.28848`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.3_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `17882933870.016975`
          - **ev** (float): sample = `113048260725.14424`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.3_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `17882933870.016975`
          - **ev** (float): sample = `87926425008.44553`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.3_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `17882933870.016975`
          - **ev** (float): sample = `62804589291.7468`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.3_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `37086980458.11152`
          - **ev** (float): sample = `169572391087.71637`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.3_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `37086980458.11152`
          - **ev** (float): sample = `131889637512.66829`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.3_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `37086980458.11152`
          - **ev** (float): sample = `94206883937.62021`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.3_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48609408410.96825`
          - **ev** (float): sample = `203486869305.25964`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.3_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48609408410.96825`
          - **ev** (float): sample = `158267565015.20193`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.3_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48609408410.96825`
          - **ev** (float): sample = `113048260725.14424`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.12001`
          - **ev** (float): sample = `169572391087.71637`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.12001`
          - **ev** (float): sample = `131889637512.66829`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.12001`
          - **ev** (float): sample = `94206883937.62021`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.214554`
          - **ev** (float): sample = `254358586631.57455`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.214554`
          - **ev** (float): sample = `197834456269.0024`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.214554`
          - **ev** (float): sample = `141310325906.4303`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07129`
          - **ev** (float): sample = `305230303957.88947`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07129`
          - **ev** (float): sample = `237401347522.80292`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07129`
          - **ev** (float): sample = `169572391087.71637`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.7_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.12001`
          - **ev** (float): sample = `169572391087.71637`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.7_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.12001`
          - **ev** (float): sample = `131889637512.66829`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.7_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.12001`
          - **ev** (float): sample = `94206883937.62021`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.7_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.214554`
          - **ev** (float): sample = `254358586631.57455`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.7_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.214554`
          - **ev** (float): sample = `197834456269.0024`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.7_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.214554`
          - **ev** (float): sample = `141310325906.4303`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.7_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07129`
          - **ev** (float): sample = `305230303957.88947`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.7_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07129`
          - **ev** (float): sample = `237401347522.80292`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_2.0_0.7_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07129`
          - **ev** (float): sample = `169572391087.71637`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.3_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.465454`
          - **ev** (float): sample = `90438608580.11539`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.3_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.465454`
          - **ev** (float): sample = `70341140006.75641`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.3_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.465454`
          - **ev** (float): sample = `50243671433.39744`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.3_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.559998`
          - **ev** (float): sample = `135657912870.1731`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.3_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.559998`
          - **ev** (float): sample = `105511710010.13461`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.3_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.559998`
          - **ev** (float): sample = `75365507150.09616`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.3_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.416725`
          - **ev** (float): sample = `162789495444.2077`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.3_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.416725`
          - **ev** (float): sample = `126614052012.16153`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.3_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.416725`
          - **ev** (float): sample = `90438608580.11539`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `135657912870.1731`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `105511710010.13461`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `75365507150.09616`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `203486869305.25964`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `158267565015.20193`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `113048260725.14424`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `244184243166.31158`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `189921078018.2423`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `135657912870.1731`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.7_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `135657912870.1731`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.7_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `105511710010.13461`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.7_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `75365507150.09616`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.7_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `203486869305.25964`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.7_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `158267565015.20193`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.7_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `113048260725.14424`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.7_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `244184243166.31158`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.7_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `189921078018.2423`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D+E_3.0_0.7_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `135657912870.1731`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **A+C+D_1.0_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.119995`
          - **ev** (float): sample = `167478904777.99146`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_1.0_0.3_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.21454`
          - **ev** (float): sample = `251218357166.98718`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_1.0_0.3_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07126`
          - **ev** (float): sample = `301462028600.38464`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_1.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `251218357166.9872`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_1.0_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `376827535750.48083`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_1.0_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `452193042900.57697`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_1.0_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `251218357166.9872`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_1.0_0.7_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `376827535750.48083`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_1.0_0.7_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `452193042900.57697`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_2.0_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `17882933870.016975`
          - **ev** (float): sample = `125609178583.4936`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_2.0_0.3_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `37086980458.11152`
          - **ev** (float): sample = `188413767875.24042`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_2.0_0.3_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `48609408410.96825`
          - **ev** (float): sample = `226096521450.28848`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_2.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.12001`
          - **ev** (float): sample = `188413767875.24042`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_2.0_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.214554`
          - **ev** (float): sample = `282620651812.8606`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_2.0_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07129`
          - **ev** (float): sample = `339144782175.43274`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_2.0_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.12001`
          - **ev** (float): sample = `188413767875.24042`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_2.0_0.7_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.214554`
          - **ev** (float): sample = `282620651812.8606`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_2.0_0.7_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07129`
          - **ev** (float): sample = `339144782175.43274`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_3.0_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `3810177108.465454`
          - **ev** (float): sample = `100487342866.79488`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_3.0_0.3_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `23014223696.559998`
          - **ev** (float): sample = `150731014300.19232`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_3.0_0.3_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `34536651649.416725`
          - **ev** (float): sample = `180877217160.23077`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_3.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `150731014300.19232`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_3.0_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `226096521450.28848`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_3.0_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `271315825740.3462`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_3.0_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `150731014300.19232`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_3.0_0.7_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `226096521450.28848`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+D_3.0_0.7_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `271315825740.3462`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_1.0_0.3_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.30908`
          - **ev** (float): sample = `301462028600.38464`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_1.0_0.3_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.30908`
          - **ev** (float): sample = `234470466689.18802`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_1.0_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.30908`
          - **ev** (float): sample = `167478904777.99146`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_1.0_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `452193042900.57697`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_1.0_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `351705700033.7821`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_1.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `251218357166.9872`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_1.0_0.7_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `452193042900.57697`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_1.0_0.7_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `351705700033.7821`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_1.0_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `251218357166.9872`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_2.0_0.3_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `56291027046.20606`
          - **ev** (float): sample = `226096521450.28848`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_2.0_0.3_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `56291027046.20606`
          - **ev** (float): sample = `175852850016.89105`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_2.0_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `56291027046.20606`
          - **ev** (float): sample = `125609178583.4936`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_2.0_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.3091`
          - **ev** (float): sample = `339144782175.43274`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_2.0_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.3091`
          - **ev** (float): sample = `263779275025.33658`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_2.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.3091`
          - **ev** (float): sample = `188413767875.24042`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_2.0_0.7_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.3091`
          - **ev** (float): sample = `339144782175.43274`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_2.0_0.7_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.3091`
          - **ev** (float): sample = `263779275025.33658`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_2.0_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.3091`
          - **ev** (float): sample = `188413767875.24042`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_3.0_0.3_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65454`
          - **ev** (float): sample = `180877217160.23077`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_3.0_0.3_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65454`
          - **ev** (float): sample = `140682280013.51282`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_3.0_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65454`
          - **ev** (float): sample = `100487342866.79488`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_3.0_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `271315825740.3462`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_3.0_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `211023420020.26923`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_3.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `150731014300.19232`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_3.0_0.7_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `271315825740.3462`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_3.0_0.7_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `211023420020.26923`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C+E_3.0_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `150731014300.19232`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+C_1.0_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.30908`
          - **ev** (float): sample = `334957809555.9829`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+C_1.0_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `502436714333.9744`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+C_1.0_0.7**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `502436714333.9744`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+C_2.0_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `56291027046.20606`
          - **ev** (float): sample = `251218357166.9872`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+C_2.0_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.3091`
          - **ev** (float): sample = `376827535750.48083`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+C_2.0_0.7**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.3091`
          - **ev** (float): sample = `376827535750.48083`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+C_3.0_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `42218270284.65454`
          - **ev** (float): sample = `200974685733.58975`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+C_3.0_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `301462028600.38464`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+C_3.0_0.7**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `301462028600.38464`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+D+E_1.0_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `226096521450.28848`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_1.0_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `175852850016.89105`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_1.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `125609178583.4936`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_1.0_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `339144782175.43274`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_1.0_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `263779275025.33658`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_1.0_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `188413767875.24042`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_1.0_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `406973738610.5193`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_1.0_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `316535130030.4039`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_1.0_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `226096521450.28848`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_2.0_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.12001`
          - **ev** (float): sample = `169572391087.71637`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_2.0_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.12001`
          - **ev** (float): sample = `131889637512.66829`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_2.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.12001`
          - **ev** (float): sample = `94206883937.62021`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_2.0_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.214554`
          - **ev** (float): sample = `254358586631.57455`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_2.0_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.214554`
          - **ev** (float): sample = `197834456269.0024`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_2.0_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.214554`
          - **ev** (float): sample = `141310325906.4303`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_2.0_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07129`
          - **ev** (float): sample = `305230303957.88947`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_2.0_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07129`
          - **ev** (float): sample = `237401347522.80292`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_2.0_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07129`
          - **ev** (float): sample = `169572391087.71637`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_3.0_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `135657912870.1731`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_3.0_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `105511710010.13461`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_3.0_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `75365507150.09616`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_3.0_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `203486869305.25964`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_3.0_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `158267565015.20193`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_3.0_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `113048260725.14424`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_3.0_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `244184243166.31158`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_3.0_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `189921078018.2423`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D+E_3.0_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `135657912870.1731`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **A+D_1.0_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `251218357166.9872`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+D_1.0_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `376827535750.48083`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+D_1.0_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `452193042900.57697`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+D_2.0_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.12001`
          - **ev** (float): sample = `188413767875.24042`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+D_2.0_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.214554`
          - **ev** (float): sample = `282620651812.8606`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+D_2.0_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07129`
          - **ev** (float): sample = `339144782175.43274`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+D_3.0_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `24919312250.792732`
          - **ev** (float): sample = `150731014300.19232`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+D_3.0_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `44123358838.887276`
          - **ev** (float): sample = `226096521450.28848`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+D_3.0_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `55645786791.744`
          - **ev** (float): sample = `271315825740.3462`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+E_1.0_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `452193042900.57697`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+E_1.0_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `351705700033.7821`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+E_1.0_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `251218357166.9872`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+E_2.0_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.3091`
          - **ev** (float): sample = `339144782175.43274`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+E_2.0_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.3091`
          - **ev** (float): sample = `263779275025.33658`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+E_2.0_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.3091`
          - **ev** (float): sample = `188413767875.24042`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+E_3.0_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `271315825740.3462`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+E_3.0_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `211023420020.26923`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A+E_3.0_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `150731014300.19232`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **A1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `502436714333.9744`
          - **level** (float): sample = `1.0`
          - **perspectives**: array
            - **Array** of length 1 containing `str` items.
      - **A2**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.3091`
          - **ev** (float): sample = `376827535750.48083`
          - **level** (float): sample = `2.0`
          - **perspectives**: array
            - **Array** of length 1 containing `str` items.
      - **A3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `63327405426.98182`
          - **ev** (float): sample = `301462028600.38464`
          - **level** (float): sample = `3.0`
          - **perspectives**: array
            - **Array** of length 1 containing `str` items.
      - **B+C+D+E_0.2_0.3_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `96690371734.70546`
          - **ev** (float): sample = `194443008447.2481`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.3_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `96690371734.70546`
          - **ev** (float): sample = `151233451014.5263`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.3_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `96690371734.70546`
          - **ev** (float): sample = `108023893581.8045`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.3_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `115894418322.8`
          - **ev** (float): sample = `291664512670.8722`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.3_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `115894418322.8`
          - **ev** (float): sample = `226850176521.78946`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.3_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `115894418322.8`
          - **ev** (float): sample = `162035840372.70676`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.3_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `127416846275.65674`
          - **ev** (float): sample = `349997415205.04663`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.3_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `127416846275.65674`
          - **ev** (float): sample = `272220211826.14734`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.3_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `127416846275.65674`
          - **ev** (float): sample = `194443008447.2481`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `164239604190.15274`
          - **ev** (float): sample = `291664512670.8722`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `164239604190.15274`
          - **ev** (float): sample = `226850176521.78946`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `164239604190.15274`
          - **ev** (float): sample = `162035840372.70676`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `183443650778.24728`
          - **ev** (float): sample = `437496769006.3082`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `183443650778.24728`
          - **ev** (float): sample = `340275264782.68414`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `183443650778.24728`
          - **ev** (float): sample = `243053760559.06012`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `194966078731.104`
          - **ev** (float): sample = `524996122807.56995`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `194966078731.104`
          - **ev** (float): sample = `408330317739.22107`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `194966078731.104`
          - **ev** (float): sample = `291664512670.8722`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.7_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `164239604190.15274`
          - **ev** (float): sample = `291664512670.8722`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.7_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `164239604190.15274`
          - **ev** (float): sample = `226850176521.78946`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.7_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `164239604190.15274`
          - **ev** (float): sample = `162035840372.70676`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.7_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `183443650778.24728`
          - **ev** (float): sample = `437496769006.3082`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.7_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `183443650778.24728`
          - **ev** (float): sample = `340275264782.68414`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.7_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `183443650778.24728`
          - **ev** (float): sample = `243053760559.06012`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.7_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `194966078731.104`
          - **ev** (float): sample = `524996122807.56995`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.7_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `194966078731.104`
          - **ev** (float): sample = `408330317739.22107`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.2_0.7_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `194966078731.104`
          - **ev** (float): sample = `291664512670.8722`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.3_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.119995`
          - **ev** (float): sample = `146962738942.68753`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.3_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.119995`
          - **ev** (float): sample = `114304352510.97917`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.3_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.119995`
          - **ev** (float): sample = `81645966079.27084`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.3_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.21454`
          - **ev** (float): sample = `220444108414.03128`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.3_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.21454`
          - **ev** (float): sample = `171456528766.46875`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.3_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.21454`
          - **ev** (float): sample = `122468949118.90627`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.3_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07126`
          - **ev** (float): sample = `264532930096.83755`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.3_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07126`
          - **ev** (float): sample = `205747834519.76254`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.3_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07126`
          - **ev** (float): sample = `146962738942.68753`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `220444108414.0313`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `171456528766.46878`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `122468949118.90628`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `330666162621.047`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `257184793149.7032`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `183703423678.35944`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `396799395145.25635`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `308621751779.6438`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `220444108414.0313`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.7_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `220444108414.0313`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.7_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `171456528766.46878`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.7_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `122468949118.90628`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.7_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `330666162621.047`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.7_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `257184793149.7032`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.7_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `183703423678.35944`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.7_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `396799395145.25635`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.7_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `308621751779.6438`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.5_0.7_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `220444108414.0313`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.3_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `83655712936.60675`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.3_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `65065554506.24969`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.3_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `46475396075.89264`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.3_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `125483569404.91013`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.3_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `97598331759.37454`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.3_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `69713094113.83896`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.3_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `9205689478.623997`
          - **ev** (float): sample = `150580283285.89215`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.3_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `9205689478.623997`
          - **ev** (float): sample = `117117998111.24945`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.3_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `9205689478.623997`
          - **ev** (float): sample = `83655712936.60675`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `125483569404.91013`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `97598331759.37454`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `69713094113.83896`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6126915582.698177`
          - **ev** (float): sample = `188225354107.3652`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6126915582.698177`
          - **ev** (float): sample = `146397497639.0618`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6126915582.698177`
          - **ev** (float): sample = `104569641170.75844`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `17649343535.554905`
          - **ev** (float): sample = `225870424928.83823`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `17649343535.554905`
          - **ev** (float): sample = `175676997166.87418`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `17649343535.554905`
          - **ev** (float): sample = `125483569404.91013`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.7_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `125483569404.91013`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.7_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `97598331759.37454`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.7_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `69713094113.83896`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.7_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6126915582.698177`
          - **ev** (float): sample = `188225354107.3652`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.7_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6126915582.698177`
          - **ev** (float): sample = `146397497639.0618`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.7_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6126915582.698177`
          - **ev** (float): sample = `104569641170.75844`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.7_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `17649343535.554905`
          - **ev** (float): sample = `225870424928.83823`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.7_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `17649343535.554905`
          - **ev** (float): sample = `175676997166.87418`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D+E_0.9_0.7_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `17649343535.554905`
          - **ev** (float): sample = `125483569404.91013`
          - **levels**: array
            - **Array** of length 4 containing `float` items.
          - **perspectives**: array
            - **Array** of length 4 containing `str` items.
      - **B+C+D_0.2_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `96690371734.70546`
          - **ev** (float): sample = `216047787163.609`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.2_0.3_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `115894418322.8`
          - **ev** (float): sample = `324071680745.4135`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.2_0.3_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `127416846275.65674`
          - **ev** (float): sample = `388886016894.4962`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.2_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `164239604190.15274`
          - **ev** (float): sample = `324071680745.4135`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.2_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `183443650778.24728`
          - **ev** (float): sample = `486107521118.12024`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.2_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `194966078731.104`
          - **ev** (float): sample = `583329025341.7444`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.2_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `164239604190.15274`
          - **ev** (float): sample = `324071680745.4135`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.2_0.7_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `183443650778.24728`
          - **ev** (float): sample = `486107521118.12024`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.2_0.7_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `194966078731.104`
          - **ev** (float): sample = `583329025341.7444`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.5_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `46028447393.119995`
          - **ev** (float): sample = `163291932158.5417`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.5_0.3_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `65232493981.21454`
          - **ev** (float): sample = `244937898237.81253`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.5_0.3_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `76754921934.07126`
          - **ev** (float): sample = `293925477885.37506`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `244937898237.81256`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.5_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `367406847356.7189`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.5_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `440888216828.0626`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.5_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `244937898237.81256`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.5_0.7_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `367406847356.7189`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.5_0.7_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `440888216828.0626`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.9_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `92950792151.78528`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.9_0.3_0.75**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `139426188227.67792`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.9_0.3_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `9205689478.623997`
          - **ev** (float): sample = `167311425873.2135`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.9_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `139426188227.67792`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.9_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6126915582.698177`
          - **ev** (float): sample = `209139282341.51688`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.9_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `17649343535.554905`
          - **ev** (float): sample = `250967138809.82025`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.9_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `139426188227.67792`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.9_0.7_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6126915582.698177`
          - **ev** (float): sample = `209139282341.51688`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+D_0.9_0.7_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `17649343535.554905`
          - **ev** (float): sample = `250967138809.82025`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.2_0.3_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `135098464910.89455`
          - **ev** (float): sample = `388886016894.4962`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.2_0.3_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `135098464910.89455`
          - **ev** (float): sample = `302466902029.0526`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.2_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `135098464910.89455`
          - **ev** (float): sample = `216047787163.609`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.2_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `202647697366.34183`
          - **ev** (float): sample = `583329025341.7444`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.2_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `202647697366.34183`
          - **ev** (float): sample = `453700353043.5789`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.2_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `202647697366.34183`
          - **ev** (float): sample = `324071680745.4135`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.2_0.7_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `202647697366.34183`
          - **ev** (float): sample = `583329025341.7444`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.2_0.7_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `202647697366.34183`
          - **ev** (float): sample = `453700353043.5789`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.2_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `202647697366.34183`
          - **ev** (float): sample = `324071680745.4135`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.5_0.3_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.30908`
          - **ev** (float): sample = `293925477885.37506`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.5_0.3_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.30908`
          - **ev** (float): sample = `228608705021.95834`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.5_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.30908`
          - **ev** (float): sample = `163291932158.5417`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `440888216828.0626`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `342913057532.93756`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `244937898237.81256`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.5_0.7_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `440888216828.0626`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.5_0.7_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `342913057532.93756`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.5_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `244937898237.81256`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.9_0.3_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `16887308113.861813`
          - **ev** (float): sample = `167311425873.2135`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.9_0.3_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `16887308113.861813`
          - **ev** (float): sample = `130131109012.49937`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.9_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `16887308113.861813`
          - **ev** (float): sample = `92950792151.78528`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.9_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `25330962170.79272`
          - **ev** (float): sample = `250967138809.82025`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.9_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `25330962170.79272`
          - **ev** (float): sample = `195196663518.74908`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.9_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `25330962170.79272`
          - **ev** (float): sample = `139426188227.67792`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.9_0.7_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `25330962170.79272`
          - **ev** (float): sample = `250967138809.82025`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.9_0.7_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `25330962170.79272`
          - **ev** (float): sample = `195196663518.74908`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C+E_0.9_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `25330962170.79272`
          - **ev** (float): sample = `139426188227.67792`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+C_0.2_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `135098464910.89455`
          - **ev** (float): sample = `432095574327.218`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+C_0.2_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `202647697366.34183`
          - **ev** (float): sample = `648143361490.827`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+C_0.2_0.7**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `202647697366.34183`
          - **ev** (float): sample = `648143361490.827`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+C_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `84436540569.30908`
          - **ev** (float): sample = `326583864317.0834`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+C_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `489875796475.6251`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+C_0.5_0.7**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `489875796475.6251`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+C_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `16887308113.861813`
          - **ev** (float): sample = `185901584303.57056`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+C_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `25330962170.79272`
          - **ev** (float): sample = `278852376455.35583`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+C_0.9_0.7**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `25330962170.79272`
          - **ev** (float): sample = `278852376455.35583`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+D+E_0.2_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `164239604190.15274`
          - **ev** (float): sample = `291664512670.8722`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.2_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `164239604190.15274`
          - **ev** (float): sample = `226850176521.78946`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.2_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `164239604190.15274`
          - **ev** (float): sample = `162035840372.70676`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.2_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `183443650778.24728`
          - **ev** (float): sample = `437496769006.3082`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.2_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `183443650778.24728`
          - **ev** (float): sample = `340275264782.68414`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.2_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `183443650778.24728`
          - **ev** (float): sample = `243053760559.06012`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.2_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `194966078731.104`
          - **ev** (float): sample = `524996122807.56995`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.2_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `194966078731.104`
          - **ev** (float): sample = `408330317739.22107`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.2_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `194966078731.104`
          - **ev** (float): sample = `291664512670.8722`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `220444108414.0313`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `171456528766.46878`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `122468949118.90628`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `330666162621.047`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `257184793149.7032`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `183703423678.35944`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `396799395145.25635`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `308621751779.6438`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `220444108414.0313`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.9_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `125483569404.91013`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.9_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `97598331759.37454`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.9_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `69713094113.83896`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.9_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6126915582.698177`
          - **ev** (float): sample = `188225354107.3652`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.9_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6126915582.698177`
          - **ev** (float): sample = `146397497639.0618`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.9_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6126915582.698177`
          - **ev** (float): sample = `104569641170.75844`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.9_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `17649343535.554905`
          - **ev** (float): sample = `225870424928.83823`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.9_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `17649343535.554905`
          - **ev** (float): sample = `175676997166.87418`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D+E_0.9_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `17649343535.554905`
          - **ev** (float): sample = `125483569404.91013`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **B+D_0.2_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `164239604190.15274`
          - **ev** (float): sample = `324071680745.4135`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+D_0.2_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `183443650778.24728`
          - **ev** (float): sample = `486107521118.12024`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+D_0.2_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `194966078731.104`
          - **ev** (float): sample = `583329025341.7444`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+D_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `88246717677.77455`
          - **ev** (float): sample = `244937898237.81256`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+D_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `107450764265.8691`
          - **ev** (float): sample = `367406847356.7189`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+D_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `118973192218.72583`
          - **ev** (float): sample = `440888216828.0626`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+D_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (int): sample = `0`
          - **ev** (float): sample = `139426188227.67792`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+D_0.9_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `6126915582.698177`
          - **ev** (float): sample = `209139282341.51688`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+D_0.9_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `17649343535.554905`
          - **ev** (float): sample = `250967138809.82025`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+E_0.2_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `202647697366.34183`
          - **ev** (float): sample = `583329025341.7444`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+E_0.2_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `202647697366.34183`
          - **ev** (float): sample = `453700353043.5789`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+E_0.2_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `202647697366.34183`
          - **ev** (float): sample = `324071680745.4135`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+E_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `440888216828.0626`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+E_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `342913057532.93756`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+E_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `244937898237.81256`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+E_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `25330962170.79272`
          - **ev** (float): sample = `250967138809.82025`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+E_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `25330962170.79272`
          - **ev** (float): sample = `195196663518.74908`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B+E_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `25330962170.79272`
          - **ev** (float): sample = `139426188227.67792`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **B1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `202647697366.34183`
          - **ev** (float): sample = `648143361490.827`
          - **level** (float): sample = `0.2`
          - **perspectives**: array
            - **Array** of length 1 containing `str` items.
      - **B2**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `126654810853.96364`
          - **ev** (float): sample = `489875796475.6251`
          - **level** (float): sample = `0.5`
          - **perspectives**: array
            - **Array** of length 1 containing `str` items.
      - **B3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `25330962170.79272`
          - **ev** (float): sample = `278852376455.35583`
          - **level** (float): sample = `0.9`
          - **perspectives**: array
            - **Array** of length 1 containing `str` items.
      - **C+D+E_0.3_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `130464987962.42908`
          - **ev** (float): sample = `226096521450.28848`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.3_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `130464987962.42908`
          - **ev** (float): sample = `175852850016.89105`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.3_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `130464987962.42908`
          - **ev** (float): sample = `125609178583.4936`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.3_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `149669034550.52362`
          - **ev** (float): sample = `339144782175.43274`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.3_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `149669034550.52362`
          - **ev** (float): sample = `263779275025.33658`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.3_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `149669034550.52362`
          - **ev** (float): sample = `188413767875.24042`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.3_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `161191462503.38034`
          - **ev** (float): sample = `406973738610.5193`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.3_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `161191462503.38034`
          - **ev** (float): sample = `316535130030.4039`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.3_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `161191462503.38034`
          - **ev** (float): sample = `226096521450.28848`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.5_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `214901528531.7382`
          - **ev** (float): sample = `339144782175.43274`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.5_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `214901528531.7382`
          - **ev** (float): sample = `263779275025.33658`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.5_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `214901528531.7382`
          - **ev** (float): sample = `188413767875.24042`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.5_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `234105575119.83273`
          - **ev** (float): sample = `508717173263.1491`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.5_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `234105575119.83273`
          - **ev** (float): sample = `395668912538.0048`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.5_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `234105575119.83273`
          - **ev** (float): sample = `282620651812.8606`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.5_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `245628003072.68945`
          - **ev** (float): sample = `610460607915.7789`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.5_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `245628003072.68945`
          - **ev** (float): sample = `474802695045.60583`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.5_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `245628003072.68945`
          - **ev** (float): sample = `339144782175.43274`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.7_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `214901528531.7382`
          - **ev** (float): sample = `339144782175.43274`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.7_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `214901528531.7382`
          - **ev** (float): sample = `263779275025.33658`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.7_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `214901528531.7382`
          - **ev** (float): sample = `188413767875.24042`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.7_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `234105575119.83273`
          - **ev** (float): sample = `508717173263.1491`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.7_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `234105575119.83273`
          - **ev** (float): sample = `395668912538.0048`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.7_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `234105575119.83273`
          - **ev** (float): sample = `282620651812.8606`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.7_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `245628003072.68945`
          - **ev** (float): sample = `610460607915.7789`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.7_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `245628003072.68945`
          - **ev** (float): sample = `474802695045.60583`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D+E_0.7_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `245628003072.68945`
          - **ev** (float): sample = `339144782175.43274`
          - **levels**: array
            - **Array** of length 3 containing `float` items.
          - **perspectives**: array
            - **Array** of length 3 containing `str` items.
      - **C+D_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `130464987962.42908`
          - **ev** (float): sample = `251218357166.9872`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+D_0.3_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `149669034550.52362`
          - **ev** (float): sample = `376827535750.48083`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+D_0.3_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `161191462503.38034`
          - **ev** (float): sample = `452193042900.57697`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+D_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `214901528531.7382`
          - **ev** (float): sample = `376827535750.48083`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+D_0.5_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `234105575119.83273`
          - **ev** (float): sample = `565241303625.7212`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+D_0.5_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `245628003072.68945`
          - **ev** (float): sample = `678289564350.8655`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+D_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `214901528531.7382`
          - **ev** (float): sample = `376827535750.48083`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+D_0.7_0.75**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `234105575119.83273`
          - **ev** (float): sample = `565241303625.7212`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+D_0.7_0.9**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `245628003072.68945`
          - **ev** (float): sample = `678289564350.8655`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+E_0.3_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `168873081138.61816`
          - **ev** (float): sample = `452193042900.57697`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+E_0.3_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `168873081138.61816`
          - **ev** (float): sample = `351705700033.7821`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+E_0.3_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `168873081138.61816`
          - **ev** (float): sample = `251218357166.9872`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+E_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `253309621707.92728`
          - **ev** (float): sample = `678289564350.8655`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+E_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `253309621707.92728`
          - **ev** (float): sample = `527558550050.67316`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+E_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `253309621707.92728`
          - **ev** (float): sample = `376827535750.48083`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+E_0.7_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `253309621707.92728`
          - **ev** (float): sample = `678289564350.8655`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+E_0.7_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `253309621707.92728`
          - **ev** (float): sample = `527558550050.67316`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C+E_0.7_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `253309621707.92728`
          - **ev** (float): sample = `376827535750.48083`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **C1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `168873081138.61816`
          - **ev** (float): sample = `502436714333.9744`
          - **level** (float): sample = `0.3`
          - **perspectives**: array
            - **Array** of length 1 containing `str` items.
      - **C2**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `253309621707.92728`
          - **ev** (float): sample = `753655071500.9617`
          - **level** (float): sample = `0.5`
          - **perspectives**: array
            - **Array** of length 1 containing `str` items.
      - **C3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `253309621707.92728`
          - **ev** (float): sample = `753655071500.9617`
          - **level** (float): sample = `0.7`
          - **perspectives**: array
            - **Array** of length 1 containing `str` items.
      - **D+E_0.5_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `214901528531.7382`
          - **ev** (float): sample = `339144782175.43274`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **D+E_0.5_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `214901528531.7382`
          - **ev** (float): sample = `263779275025.33658`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **D+E_0.5_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `214901528531.7382`
          - **ev** (float): sample = `188413767875.24042`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **D+E_0.75_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `234105575119.83273`
          - **ev** (float): sample = `508717173263.1491`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **D+E_0.75_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `234105575119.83273`
          - **ev** (float): sample = `395668912538.0048`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **D+E_0.75_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `234105575119.83273`
          - **ev** (float): sample = `282620651812.8606`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **D+E_0.9_0.1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `245628003072.68945`
          - **ev** (float): sample = `610460607915.7789`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **D+E_0.9_0.3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `245628003072.68945`
          - **ev** (float): sample = `474802695045.60583`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **D+E_0.9_0.5**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `245628003072.68945`
          - **ev** (float): sample = `339144782175.43274`
          - **levels**: array
            - **Array** of length 2 containing `float` items.
          - **perspectives**: array
            - **Array** of length 2 containing `str` items.
      - **D1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `214901528531.7382`
          - **ev** (float): sample = `376827535750.48083`
          - **level** (float): sample = `0.5`
          - **perspectives**: array
            - **Array** of length 1 containing `str` items.
      - **D2**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `234105575119.83273`
          - **ev** (float): sample = `565241303625.7212`
          - **level** (float): sample = `0.75`
          - **perspectives**: array
            - **Array** of length 1 containing `str` items.
      - **D3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `245628003072.68945`
          - **ev** (float): sample = `678289564350.8655`
          - **level** (float): sample = `0.9`
          - **perspectives**: array
            - **Array** of length 1 containing `str` items.
      - **E1**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `253309621707.92728`
          - **ev** (float): sample = `678289564350.8655`
          - **level** (float): sample = `0.1`
          - **perspectives**: array
            - **Array** of length 1 containing `str` items.
      - **E2**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `253309621707.92728`
          - **ev** (float): sample = `527558550050.67316`
          - **level** (float): sample = `0.3`
          - **perspectives**: array
            - **Array** of length 1 containing `str` items.
      - **E3**: object
        - **Object** containing keys:
          - **ebitda** (float): sample = `253309621707.92728`
          - **ev** (float): sample = `376827535750.48083`
          - **level** (float): sample = `0.5`
          - **perspectives**: array
            - **Array** of length 1 containing `str` items.
  - **scenario_matrix_count** (int): sample = `1023`
  - **scorecard**: object
    - **Object** containing keys:
      - **Asset Utilization**: object
        - **Object** containing keys:
          - **rationale** (str): sample = `45% GPU utilization vs 5% dark fiber; improving fa`
          - **score** (int): sample = `3`
          - **weight** (float): sample = `0.15`
      - **CapEx Discipline**: object
        - **Object** containing keys:
          - **rationale** (str): sample = `Aggressive: 52% capex/revenue, 2.5x revenue; needs`
          - **score** (int): sample = `2`
          - **weight** (float): sample = `0.15`
      - **Concentration Risk**: object
        - **Object** containing keys:
          - **rationale** (str): sample = `Mega-projects create correlated downside; top 3 = `
          - **score** (int): sample = `2`
          - **weight** (float): sample = `0.1`
      - **Fundamental Quality**: object
        - **Object** containing keys:
          - **rationale** (str): sample = `Real revenue ($600B+ cloud), profitable IPOs (40%)`
          - **score** (int): sample = `4`
          - **weight** (float): sample = `0.2`
      - **Monetization Visibility**: object
        - **Object** containing keys:
          - **rationale** (str): sample = `Enterprise contracts, cloud revenue, inference API`
          - **score** (int): sample = `4`
          - **weight** (float): sample = `0.1`
      - **Supply Constraints**: object
        - **Object** containing keys:
          - **rationale** (str): sample = `HBM/CoWoS/transformer constraints limit overbuild `
          - **score** (int): sample = `4`
          - **weight** (float): sample = `0.1`
      - **Valuation Metrics**: object
        - **Object** containing keys:
          - **rationale** (str): sample = `P/E reasonable (35x) but P/S elevated (8.5x); Mag7`
          - **score** (int): sample = `2`
          - **weight** (float): sample = `0.2`
  - **weighted_score** (float): sample = `2.95`

---

### File: `data_centers/dcf_valuations.json`

- **Size:** 69.80 KB
- **Format:** Hierarchical/Nested JSON Document
#### JSON Structure Summary

- **Object** containing keys:
  - **AWS**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `59267098414.70518`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `7248948727.679999`
            - **ebitda** (float): sample = `8457106848.959999`
            - **fcf** (float): sample = `1208158121.2799997`
            - **pv_fcf** (float): sample = `1108401946.1284401`
            - **revenue** (float): sample = `24163162425.6`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `17742970390.747093`
      - **pv_terminal** (float): sample = `41524128023.958084`
      - **terminal_value** (float): sample = `98302712303.031`
  - **Beale Infrastructure**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `9128882650.712217`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `1116552084.48`
            - **ebitda** (float): sample = `1302644098.56`
            - **fcf** (float): sample = `186092014.07999992`
            - **pv_fcf** (float): sample = `170726618.42201826`
            - **revenue** (float): sample = `3721840281.6`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `2732941191.7355375`
      - **pv_terminal** (float): sample = `6395941458.97668`
      - **terminal_value** (float): sample = `15141519474.799112`
  - **Bitzero**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `193354739610.88385`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `23649185318.399998`
            - **ebitda** (float): sample = `27590716204.8`
            - **fcf** (float): sample = `3941530886.4000015`
            - **pv_fcf** (float): sample = `3616083382.0183496`
            - **revenue** (float): sample = `78830617728.0`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `57885192823.53314`
      - **pv_terminal** (float): sample = `135469546787.35072`
      - **terminal_value** (float): sample = `320705684077.8316`
  - **Crusoe**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `160659364053.45395`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `19650219494.399998`
            - **ebitda** (float): sample = `22925256076.8`
            - **fcf** (float): sample = `3275036582.4000015`
            - **pv_fcf** (float): sample = `3004620717.7981663`
            - **revenue** (float): sample = `65500731648.0`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `48097079419.18438`
      - **pv_terminal** (float): sample = `112562284634.26956`
      - **terminal_value** (float): sample = `266475863772.26843`
  - **Energy Abundance**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `107417664592.27748`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `13138236288.0`
            - **ebitda** (float): sample = `15327942335.999998`
            - **fcf** (float): sample = `2189706047.999998`
            - **pv_fcf** (float): sample = `2008904631.1926587`
            - **revenue** (float): sample = `43794120960.0`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `32157950925.282566`
      - **pv_terminal** (float): sample = `75259713666.99492`
      - **terminal_value** (float): sample = `178167112295.4478`
  - **Fermi America**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `193354739610.88385`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `23649185318.399998`
            - **ebitda** (float): sample = `27590716204.8`
            - **fcf** (float): sample = `3941530886.4000015`
            - **pv_fcf** (float): sample = `3616083382.0183496`
            - **revenue** (float): sample = `78830617728.0`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `57885192823.53314`
      - **pv_terminal** (float): sample = `135469546787.35072`
      - **terminal_value** (float): sample = `320705684077.8316`
  - **Google**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `7093175307.991388`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `867565065.6`
            - **ebitda** (float): sample = `1012159243.1999999`
            - **fcf** (float): sample = `144594177.5999999`
            - **pv_fcf** (float): sample = `132655208.80733936`
            - **revenue** (float): sample = `2891883552.0`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `2123505331.4984462`
      - **pv_terminal** (float): sample = `4969669976.492942`
      - **terminal_value** (float): sample = `11765016177.060461`
  - **GridFree AI**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `107417664592.27748`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `13138236288.0`
            - **ebitda** (float): sample = `15327942335.999998`
            - **fcf** (float): sample = `2189706047.999998`
            - **pv_fcf** (float): sample = `2008904631.1926587`
            - **revenue** (float): sample = `43794120960.0`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `32157950925.282566`
      - **pv_terminal** (float): sample = `75259713666.99492`
      - **terminal_value** (float): sample = `178167112295.4478`
  - **Homer City**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `96677369805.44193`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `11824592659.199999`
            - **ebitda** (float): sample = `13795358102.4`
            - **fcf** (float): sample = `1970765443.2000008`
            - **pv_fcf** (float): sample = `1808041691.0091748`
            - **revenue** (float): sample = `39415308864.0`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `28942596411.76657`
      - **pv_terminal** (float): sample = `67734773393.67536`
      - **terminal_value** (float): sample = `160352842038.9158`
  - **Joule Capital**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `85937075018.60626`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `10510949030.399998`
            - **ebitda** (float): sample = `12262773868.799997`
            - **fcf** (float): sample = `1751824838.3999996`
            - **pv_fcf** (float): sample = `1607178750.8256876`
            - **revenue** (float): sample = `35036496767.99999`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `25727241898.250565`
      - **pv_terminal** (float): sample = `60209833120.3557`
      - **terminal_value** (float): sample = `142538571782.38354`
  - **Meta**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `300740165111.9762`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `36783478448.64`
            - **ebitda** (float): sample = `42914058190.08`
            - **fcf** (float): sample = `6130579741.440002`
            - **pv_fcf** (float): sample = `5624385083.88991`
            - **revenue** (float): sample = `122611594828.8`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `90033492234.6431`
      - **pv_terminal** (float): sample = `210706672877.33313`
      - **terminal_value** (float): sample = `498819323363.96295`
  - **Microsoft**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `6792461635.996458`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `830784827.52`
            - **ebitda** (float): sample = `969248965.4399999`
            - **fcf** (float): sample = `138464137.91999996`
            - **pv_fcf** (float): sample = `127031319.1926605`
            - **revenue** (float): sample = `2769282758.4`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `2033479770.5883296`
      - **pv_terminal** (float): sample = `4758981865.408129`
      - **terminal_value** (float): sample = `11266240796.209845`
  - **NTT**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `4294646242.3420877`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `525277451.5199999`
            - **ebitda** (float): sample = `612823693.4399999`
            - **fcf** (float): sample = `87546241.92000002`
            - **pv_fcf** (float): sample = `80317653.13761468`
            - **revenue** (float): sample = `1750924838.3999999`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `1285701226.3941445`
      - **pv_terminal** (float): sample = `3008945015.947943`
      - **terminal_value** (float): sample = `7123267129.600165`
  - **New Era Energy**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `150386202101.5807`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `18393710803.2`
            - **ebitda** (float): sample = `21459329270.399998`
            - **fcf** (float): sample = `3065618467.199997`
            - **pv_fcf** (float): sample = `2812494006.6055017`
            - **revenue** (float): sample = `61312369344.0`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `45021571874.40786`
      - **pv_terminal** (float): sample = `105364630227.17282`
      - **terminal_value** (float): sample = `249436398186.6397`
  - **Northpoint Development**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `21657675300.403038`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `2648946582.7199993`
            - **ebitda** (float): sample = `3090437679.839999`
            - **fcf** (float): sample = `441491097.1199999`
            - **pv_fcf** (float): sample = `405037703.7798164`
            - **revenue** (float): sample = `8829821942.399998`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `6483723716.295877`
      - **pv_terminal** (float): sample = `15173951584.107159`
      - **terminal_value** (float): sample = `35922261780.23483`
  - **Nscale**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `171866791675.2519`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `21020998060.8`
            - **ebitda** (float): sample = `24524497737.6`
            - **fcf** (float): sample = `3503499676.799999`
            - **pv_fcf** (float): sample = `3214219886.972476`
            - **revenue** (float): sample = `70069993536.0`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `51452280901.43985`
      - **pv_terminal** (float): sample = `120414510773.81206`
      - **terminal_value** (float): sample = `285064938699.70404`
  - **Oracle**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `276337328884.88416`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `33798771699.84`
            - **ebitda** (float): sample = `39431900316.479996`
            - **fcf** (float): sample = `5633128616.639996`
            - **pv_fcf** (float): sample = `5168007905.174308`
            - **revenue** (float): sample = `112662572332.8`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `82727941394.31177`
      - **pv_terminal** (float): sample = `193609387490.57236`
      - **terminal_value** (float): sample = `458343831005.2109`
  - **Other/Unclassified**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `59614890674.60423`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `7291487139.839999`
            - **ebitda** (float): sample = `8506734996.48`
            - **fcf** (float): sample = `1215247856.6400003`
            - **pv_fcf** (float): sample = `1114906290.495413`
            - **revenue** (float): sample = `24304957132.8`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `17847090010.8159`
      - **pv_terminal** (float): sample = `41767800663.78833`
      - **terminal_value** (float): sample = `98879574059.0571`
  - **Pacifico Energy**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `164349321160.66296`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `20101537520.64`
            - **ebitda** (float): sample = `23451793774.079998`
            - **fcf** (float): sample = `3350256253.4399986`
            - **pv_fcf** (float): sample = `3073629590.311925`
            - **revenue** (float): sample = `67005125068.799995`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `49201753031.48479`
      - **pv_terminal** (float): sample = `115147568129.17818`
      - **terminal_value** (float): sample = `272596170006.63763`
  - **Prime Data Centers**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `5157999790.119069`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `630874077.12`
            - **ebitda** (float): sample = `736019756.64`
            - **fcf** (float): sample = `105145679.51999998`
            - **pv_fcf** (float): sample = `96463926.16513759`
            - **revenue** (float): sample = `2102913590.4`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `1544165987.5296876`
      - **pv_terminal** (float): sample = `3613833802.5893817`
      - **terminal_value** (float): sample = `8555258870.263209`
  - **STAK Energy**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `64449127082.974365`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `7882761772.799999`
            - **ebitda** (float): sample = `9196555401.599998`
            - **fcf** (float): sample = `1313793628.7999992`
            - **pv_fcf** (float): sample = `1205315255.7798157`
            - **revenue** (float): sample = `26275872576.0`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `19294329976.15729`
      - **pv_terminal** (float): sample = `45154797106.81707`
      - **terminal_value** (float): sample = `106897826404.25606`
  - **Sailfish Digital**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `107417664592.27748`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `13138236288.0`
            - **ebitda** (float): sample = `15327942335.999998`
            - **fcf** (float): sample = `2189706047.999998`
            - **pv_fcf** (float): sample = `2008904631.1926587`
            - **revenue** (float): sample = `43794120960.0`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `32157950925.282566`
      - **pv_terminal** (float): sample = `75259713666.99492`
      - **terminal_value** (float): sample = `178167112295.4478`
  - **Stream Data Centers**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `4294646242.3420877`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `525277451.5199999`
            - **ebitda** (float): sample = `612823693.4399999`
            - **fcf** (float): sample = `87546241.92000002`
            - **pv_fcf** (float): sample = `80317653.13761468`
            - **revenue** (float): sample = `1750924838.3999999`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `1285701226.3941445`
      - **pv_terminal** (float): sample = `3008945015.947943`
      - **terminal_value** (float): sample = `7123267129.600165`
  - **Tract**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `51557829993.987335`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `6306029418.24`
            - **ebitda** (float): sample = `7357034321.28`
            - **fcf** (float): sample = `1051004903.04`
            - **pv_fcf** (float): sample = `964224681.6880733`
            - **revenue** (float): sample = `21020098060.8`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `15435023401.913576`
      - **pv_terminal** (float): sample = `36122806592.07376`
      - **terminal_value** (float): sample = `85515820150.39217`
  - **Vantage**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `3778105786.0680475`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `462099476.16`
            - **ebitda** (float): sample = `539116055.52`
            - **fcf** (float): sample = `77016579.35999995`
            - **pv_fcf** (float): sample = `70657412.25688069`
            - **revenue** (float): sample = `1540331587.2`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `1131062948.725075`
      - **pv_terminal** (float): sample = `2647042837.3429723`
      - **terminal_value** (float): sample = `6266513058.215008`
  - **Vermaland**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `128898254165.94873`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `15765523545.599998`
            - **ebitda** (float): sample = `18393110803.199997`
            - **fcf** (float): sample = `2627587257.5999985`
            - **pv_fcf** (float): sample = `2410630511.5596313`
            - **revenue** (float): sample = `52551745152.0`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `38588659952.31458`
      - **pv_terminal** (float): sample = `90309594213.63414`
      - **terminal_value** (float): sample = `213795652808.51212`
  - **xAI**: object
    - **Object** containing keys:
      - **assumptions**: object
        - **Object** containing keys:
          - **capex_intensity** (float): sample = `0.3`
          - **ebitda_margin** (float): sample = `0.35`
          - **revenue_growth** (float): sample = `0.2`
          - **terminal_growth** (float): sample = `0.025`
          - **wacc** (float): sample = `0.09`
      - **enterprise_value** (float): sample = `6445648544.493507`
      - **projections**: array
        - **Array** of length 10 containing `dict` items.
          - **Object** containing keys:
            - **capex** (float): sample = `788366177.2799999`
            - **ebitda** (float): sample = `919760540.1599997`
            - **fcf** (float): sample = `131394362.87999988`
            - **pv_fcf** (float): sample = `120545287.04587144`
            - **revenue** (float): sample = `2627887257.5999994`
            - **year** (int): sample = `1`
      - **pv_explicit** (float): sample = `1929653287.1218565`
      - **pv_terminal** (float): sample = `4515995257.371651`
      - **terminal_value** (float): sample = `10691003126.931934`

---

### File: `data_centers/master_facility_list_v2.json`

- **Size:** 32.98 KB
- **Format:** Tabular JSON (List of records)
- **Total Records:** 52
- **Total Columns/Keys:** 21
- **Category Fields:** capacity_category, country, expected_online_date, notes, purpose, status, tenant, tier
- **Numeric Fields:** capacity_mw, latitude, longitude, project_cost_usd
- **Text Fields:** city, cooling_type, facility_id, facility_name, hyperscaler_category, operator, power_source, source_url, state_province

#### Categorical Field Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **capacity_category** | 5 | `Hyperscale (100-999 MW)`, `Large (51-99 MW)`, `Medium (11-50 MW)`, `Mega campus (>1`, `Unknown` |
| **country** | 3 | `Norway`, `United Arab Emirates`, `United States` |
| **expected_online_date** | 11 | ``, `$10 billion`, `$14 billion`, `$3.6 billion`, `$300 million`, `$6 billion`, `2025`, `2026`, `2027`, `2028`, `250` |
| **notes** | 14 | ``, `1,300 acres`, `100 gas generators, 862MWh BESS`, `100% renewable, recycled water`, `100k GPUs`, `100k GPUs by 2026`, `3 of 5 buildings broke ground`, `AI/Cloud`, `AI/Hyperscale`, `Building 4 268MW, Bldg 2 260MW`, `Cloud/AI`, `Community opposition`, `Phase 1 approved`, `Water concerns, 31M gal/yr` |
| **purpose** | 9 | ``, `2027`, `AI/Hyperscale`, `AWS`, `Cloud/AI`, `Google`, `Meta`, `OpenAI/Oracle`, `OpenAI/Oracle/MGX` |
| **status** | 5 | `Expanding`, `Operating`, `Planned`, `Suspended`, `Under Construction` |
| **tenant** | 15 | ``, `$10 billion+`, `$33 billion`, `$40 billion+`, `2026`, `2027`, `2028`, `2032`, `2036`, `AWS`, `Google (unconfirmed)`, `Meta`, `Microsoft`, `OpenAI/Oracle`, `xAI` |
| **tier** | 3 | `Tier 1`, `Tier 2`, `Tier 3` |

#### Sample Records

| capacity_category | capacity_mw | city | cooling_type | country | expected_online_date | facility_id | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mega campus (>1 | 9000 |  |  | United States |  | DC-00001 | ... |
| Mega campus (>1 | 8000 |  |  | United States |  | DC-00002 | ... |
| Mega campus (>1 | 7650 |  |  | United States |  | DC-00003 | ... |

---

### File: `data_centers/master_facility_list_v3_enriched.json`

- **Size:** 84.06 KB
- **Format:** Tabular JSON (List of records)
- **Total Records:** 52
- **Total Columns/Keys:** 53
- **Category Fields:** capacity_category, cooling_detail, country, expected_online_date, generation_mix, gpu_generation, hyperscaler_category, network_detail, notes, primary_gpu, purpose, status, tenant, tier, utility
- **Numeric Fields:** annual_power_cost_usd, annual_power_mwh, annual_revenue_potential_usd, capacity_mw, cluster_size, est_bf16_pflops, est_capex_per_gpu, est_capex_per_kw, est_fp8_pflops, est_gpu_count, est_gpus_b200, est_gpus_gb200_nvl72, est_gpus_h100, est_gpus_mi300x, est_racks_100kw, est_racks_50kw, est_tokens_per_sec_billions, est_training_runs_per_year_gpt4_class, inference_fp8_pflops, it_load_mw, latitude, longitude, power_cost_per_gpu_per_year, ppa_price_mwh, project_cost_usd, total_capex_billion, training_bf16_pflops, voltage_kv, water_source_mgd
- **Text Fields:** city, cooling_type, facility_id, facility_name, operator, power_source, source_notes, source_url, state_province

#### Categorical Field Details

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **capacity_category** | 5 | `Hyperscale (100-999 MW)`, `Large (51-99 MW)`, `Medium (11-50 MW)`, `Mega campus (>1`, `Unknown` |
| **cooling_detail** | 8 | ``, `Direct liquid cooling (DLC)`, `Direct liquid cooling (DLC) 100%`, `Direct-to-chip liquid (80%) + rear-door (20%)`, `Direct-to-chip liquid (TPU pods)`, `Hybrid air/liquid, 100 gas generators + 862MWh BESS`, `Hybrid air/water, 95% free cooling`, `Rear-door heat exchanger + liquid assist` |
| **country** | 3 | `Norway`, `United Arab Emirates`, `United States` |
| **expected_online_date** | 11 | ``, `$10 billion`, `$14 billion`, `$3.6 billion`, `$300 million`, `$6 billion`, `2025`, `2026`, `2027`, `2028`, `250` |
| **generation_mix** | 8 | ``, `Gas 40%, Nuclear 30%, Coal 15%, Renewable 15%`, `Gas 50%, Nuclear 25%, Renewable 25%`, `Gas 60%, Nuclear 25%, Renewable 15%`, `Solar 30%, Hydro 25%, Gas 25%, Nuclear 15%, Wind 5%`, `Solar 50%, Geothermal 20%, Gas 30%`, `Wind 35%, Solar 25%, Gas 30%, Nuclear 10%`, `Wind 50%, Gas 30%, Coal 20%` |
| **gpu_generation** | 9 | ``, `GB200 NVL72`, `GB200 NVL72 / GB300`, `H100 (2025), B200 (2026+)`, `H100 / B200`, `H100 / Maia 100`, `H100 / TPU v5`, `TPU v5p / v6`, `Trainium2 / Inferentia2` |
| **hyperscaler_category** | 15 | `AWS`, `Aligned`, `Apple`, `Crusoe`, `Google`, `Meta`, `Microsoft`, `NTT`, `Oracle`, `Other/Unclassified`, `Prime Data Centers`, `Stargate`, `Stream Data Centers`, `Vantage`, `xAI` |
| **network_detail** | 8 | ``, `100G/400G to San Jose/Sacramento`, `400G/800G to Denver/Salt Lake`, `Custom optical circuit switching, 1.6T regional`, `InfiniBand NDR 400G, 800G to Chicago/Dallas`, `InfiniBand NDR, 800G to LA/San Diego`, `NVL72 + InfiniBand NDR 400G, 800G ZR+ to Atlanta/Dallas`, `NVL72 + InfiniBand NDR, 1.6T to Dallas` |
| **notes** | 14 | ``, `1,300 acres`, `100 gas generators, 862MWh BESS`, `100% renewable, recycled water`, `100k GPUs`, `100k GPUs by 2026`, `3 of 5 buildings broke ground`, `AI/Cloud`, `AI/Hyperscale`, `Building 4 268MW, Bldg 2 260MW`, `Cloud/AI`, `Community opposition`, `Phase 1 approved`, `Water concerns, 31M gal/yr` |
| **primary_gpu** | 6 | `B200`, `GB200 NVL72`, `H100`, `H100 (est.)`, `TPU v5p/v6`, `Trainium2/Inferentia2` |
| **purpose** | 9 | ``, `2027`, `AI/Hyperscale`, `AWS`, `Cloud/AI`, `Google`, `Meta`, `OpenAI/Oracle`, `OpenAI/Oracle/MGX` |
| **status** | 5 | `Expanding`, `Operating`, `Planned`, `Suspended`, `Under Construction` |
| **tenant** | 15 | ``, `$10 billion+`, `$33 billion`, `$40 billion+`, `2026`, `2027`, `2028`, `2032`, `2036`, `AWS`, `Google (unconfirmed)`, `Meta`, `Microsoft`, `OpenAI/Oracle`, `xAI` |
| **tier** | 3 | `Tier 1`, `Tier 2`, `Tier 3` |
| **utility** | 8 | ``, `Entergy Arkansas`, `Entergy Louisiana`, `Georgia Power / Southern Company`, `IID / CAISO`, `Oncor / ERCOT`, `PG&E`, `PacifiCorp / WAPA` |

#### Sample Records

| annual_power_cost_usd | annual_power_mwh | annual_revenue_potential_usd | capacity_category | capacity_mw | city | cluster_size | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2428272000.0 | 69379200.0 | 2997181440.0 | Mega campus (>1 | 9000 |  |  | ... |
| 2158464000.0 | 61670400.0 | 2664161280.0 | Mega campus (>1 | 8000 |  |  | ... |
| 2653754400.0 | 58972320.0 | 2547604224.0 | Mega campus (>1 | 7650 |  |  | ... |

---

### File: `data_centers/scenario_analysis.json`

- **Size:** 267.33 KB
- **Format:** Hierarchical/Nested JSON Document
#### JSON Structure Summary

- **Object** containing keys:
  - **probabilities**: object
    - **Object** containing keys:
      - **base** (float): sample = `0.4`
      - **bear** (float): sample = `0.25`
      - **bull** (float): sample = `0.25`
      - **stagnation** (float): sample = `0.1`
  - **scenarios**: object
    - **Object** containing keys:
      - **base**: object
        - **Object** containing keys:
          - **scenario** (str): sample = `Gradual Deflation`
          - **terminal**: object
            - **Object** containing keys:
              - **final_year_fcff** (float): sample = `755203936241.0`
              - **implied_enterprise_value** (float): sample = `13100298105187.305`
              - **pv_fcff** (float): sample = `2095897891389.874`
              - **terminal_value** (float): sample = `11004400213797.432`
          - **yearly**: array
            - **Array** of length 5 containing `dict` items.
      - **bear**: object
        - **Object** containing keys:
          - **scenario** (str): sample = `Bubble Burst (Dot-com style)`
          - **terminal**: object
            - **Object** containing keys:
              - **final_year_fcff** (float): sample = `428911724345.0`
              - **implied_enterprise_value** (float): sample = `7515667001477.457`
              - **pv_fcff** (float): sample = `1265810446736.0269`
              - **terminal_value** (float): sample = `6249856554741.43`
          - **yearly**: array
            - **Array** of length 5 containing `dict` items.
      - **bull**: object
        - **Object** containing keys:
          - **scenario** (str): sample = `Productivity Boom`
          - **terminal**: object
            - **Object** containing keys:
              - **final_year_fcff** (float): sample = `1119743076036.5999`
              - **implied_enterprise_value** (float): sample = `19421604439493.67`
              - **pv_fcff** (float): sample = `3105348188674.6436`
              - **terminal_value** (float): sample = `16316256250819.027`
          - **yearly**: array
            - **Array** of length 5 containing `dict` items.
      - **stagnation**: object
        - **Object** containing keys:
          - **scenario** (str): sample = `Japan-style Stagnation`
          - **terminal**: object
            - **Object** containing keys:
              - **final_year_fcff** (float): sample = `592057830293.0`
              - **implied_enterprise_value** (float): sample = `10307982553332.38`
              - **pv_fcff** (float): sample = `1680854169062.9507`
              - **terminal_value** (float): sample = `8627128384269.43`
          - **yearly**: array
            - **Array** of length 5 containing `dict` items.
  - **weighted**: object
    - **Object** containing keys:
      - **capex_5yr** (float): sample = `188532930969.60004`
      - **ebitda_5yr** (float): sample = `936983988590.7`
      - **ev** (float): sample = `13005235357650.941`
      - **revenue_5yr** (float): sample = `969422048539.7`
      - **roic_5yr** (float): sample = `1.5215938837053191`

---

## 5. SEC DERA Text/TSV Datasets (Advanced Methodology)

> [!NOTE]
> These are large tab-separated text files containing XBRL financial statement dataset chunks.
> The scanner reads these files using a streaming generator to map headers and estimate categories without exhausting system memory.

### Quarter: `2023q1`

#### File: `DATA/2023q1/num.txt`

- **Size:** 447.86 MB
- **Total Rows:** 3,428,670
- **Total Columns:** 10
- **Category Columns:** version, uom, coreg
- **Numeric Columns:** ddate, qtrs, value
- **Text Columns:** adsh, tag, segments, footnote

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 13 | `0000950170-23-010339`, `0001022079-23-000018`, `0001145765-23-000006`, `0001213900-23-002013`, `0001213900-23-025399`, `0001410578-23-000167`, `0001610520-23-000052`, `0001713952-23-000008`, `ifrs/2021`, `ifrs/2022`, `us-gaap-sup/2022q3`, `us-gaap/2021`, `us-gaap/2022` |
| **uom** | 5 | `CHF`, `EUR`, `USD`, `pure`, `shares` |
| **coreg** | 4 | ``, `Cnk`, `ConsolidatedBank`, `TheDowChemicalCompany` |

##### Sample Records

| adsh | tag | version | ddate | qtrs | uom | segments | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0001370368-23-000026 | Assets | us-gaap/2022 | 20221231 | 0 | CHF | LegalEntity=ConsolidatedBank; | ... |
| 0001818644-23-000003 | AccumulatedOtherComprehensiveIncomeLo... | us-gaap/2022 | 20211231 | 0 | USD |  | ... |
| 0000950170-23-005096 | AssetsCurrent | us-gaap/2022 | 20221231 | 0 | USD |  | ... |

#### File: `DATA/2023q1/pre.txt`

- **Size:** 94.61 MB
- **Total Rows:** 804,536
- **Total Columns:** 10
- **Category Columns:** adsh, stmt, rfile, version
- **Numeric Columns:** report, line, inpth, negating
- **Text Columns:** tag, plabel

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **adsh** | 1 | `0000002178-23-000038` |
| **stmt** | 4 | `BS`, `CF`, `EQ`, `IS` |
| **rfile** | 1 | `H` |
| **version** | 2 | `0000002178-23-000038`, `us-gaap/2022` |

##### Sample Records

| adsh | report | line | stmt | inpth | rfile | tag | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002178-23-000038 | 3 | 3 | BS | 0 | H | CashAndCashEquivalentsAtCarryingValue | ... |
| 0000002178-23-000038 | 3 | 4 | BS | 0 | H | RestrictedCashCurrent | ... |
| 0000002178-23-000038 | 3 | 5 | BS | 0 | H | AccountsReceivableNetCurrent | ... |

#### File: `DATA/2023q1/sub.txt`

- **Size:** 1.94 MB
- **Total Rows:** 6,754
- **Total Columns:** 36
- **Category Columns:** countryba, countryma, countryinc, afs, form, fp, aciks
- **Numeric Columns:** cik, sic, zipba, zipma, ein, changed, wksi, fye, period, fy, filed, prevrpt, detail, nciks
- **Text Columns:** adsh, name, stprba, cityba, bas1, bas2, baph, stprma, cityma, mas1, mas2, stprinc, former, accepted, instance

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **countryba** | 2 | `CA`, `US` |
| **countryma** | 2 | `CA`, `US` |
| **countryinc** | 3 | ``, `CA`, `US` |
| **afs** | 4 | ``, `1-LAF`, `2-ACC`, `4-NON` |
| **form** | 3 | `10-K`, `10-Q`, `6-K` |
| **fp** | 4 | `FY`, `Q1`, `Q2`, `Q3` |
| **aciks** | 4 | ``, `1901876`, `4515`, `81027 73986 92487 1702494 50172 1721781 6879` |

##### Sample Records

| adsh | cik | name | sic | countryba | stprba | cityba | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002178-23-000038 | 2178 | ADAMS RESOURCES & ENERGY, INC. | 5172 | US | TX | HOUSTON | ... |
| 0000002488-23-000047 | 2488 | ADVANCED MICRO DEVICES INC | 3674 | US | CA | SANTA CLARA | ... |
| 0000002969-23-000014 | 2969 | AIR PRODUCTS & CHEMICALS, INC. | 2810 | US | PA | ALLENTOWN | ... |

#### File: `DATA/2023q1/tag.txt`

- **Size:** 20.95 MB
- **Total Rows:** 103,115
- **Total Columns:** 9
- **Category Columns:** version, datatype, iord, crdr
- **Numeric Columns:** custom, abstract
- **Text Columns:** tag, tlabel, doc

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 1 | `us-gaap/2021` |
| **datatype** | 1 | `monetary` |
| **iord** | 2 | `D`, `I` |
| **crdr** | 2 | `C`, `D` |

##### Sample Records

| tag | version | custom | abstract | datatype | iord | crdr | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AccountsAndNotesReceivableNet | us-gaap/2021 | 0 | 0 | monetary | I | D | ... |
| AccountsAndOtherReceivablesNetCurrent | us-gaap/2021 | 0 | 0 | monetary | I | D | ... |
| AccountsNotesAndLoansReceivableNetCur... | us-gaap/2021 | 0 | 0 | monetary | I | D | ... |

---

### Quarter: `2023q2`

#### File: `DATA/2023q2/num.txt`

- **Size:** 446.98 MB
- **Total Rows:** 3,393,990
- **Total Columns:** 10
- **Category Columns:** version, uom, coreg
- **Numeric Columns:** ddate, qtrs, value
- **Text Columns:** adsh, tag, segments, footnote

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 17 | `0000028823-23-000117`, `0001140361-23-024799`, `0001193125-23-105776`, `0001287750-23-000021`, `0001493152-23-011998`, `0001493152-23-016192`, `0001493152-23-017508`, `0001554855-23-000224`, `0001628280-23-021482`, `0001654954-23-006034`, `0001683168-23-002352`, `0001714174-23-000037`, `0001762359-23-000021`, `ifrs/2022`, `us-gaap/2021` ... (and more) |
| **uom** | 10 | `BRL`, `CAD`, `CNY`, `COP`, `EUR`, `HKD`, `KRW`, `Rate`, `USD`, `shares` |
| **coreg** | 2 | ``, `CubesmartLPAndSubsidiaries` |

##### Sample Records

| adsh | tag | version | ddate | qtrs | uom | segments | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0001477932-23-002748 | AdditionalPaidInCapital | us-gaap/2022 | 20220930 | 0 | USD |  | ... |
| 0001493152-23-012139 | AccountsPayableAndOtherAccruedLiabili... | us-gaap/2022 | 20211231 | 0 | USD |  | ... |
| 0001683168-23-002352 | StockBasedCompensationRelatedPartyValue | 0001683168-23-002352 | 20230228 | 1 | USD | EquityComponents=SeriesAPreferredStocks; | ... |

#### File: `DATA/2023q2/pre.txt`

- **Size:** 100.62 MB
- **Total Rows:** 867,701
- **Total Columns:** 10
- **Category Columns:** adsh, stmt, rfile, version
- **Numeric Columns:** report, line, inpth, negating
- **Text Columns:** tag, plabel

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **adsh** | 2 | `0000002178-23-000064`, `0000002488-23-000076` |
| **stmt** | 4 | `BS`, `CF`, `EQ`, `IS` |
| **rfile** | 1 | `H` |
| **version** | 4 | `0000002178-23-000064`, `0000002488-23-000076`, `us-gaap/2022`, `us-gaap/2023` |

##### Sample Records

| adsh | report | line | stmt | inpth | rfile | tag | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002178-23-000064 | 2 | 3 | BS | 0 | H | CashAndCashEquivalentsAtCarryingValue | ... |
| 0000002178-23-000064 | 2 | 4 | BS | 0 | H | RestrictedCashCurrent | ... |
| 0000002178-23-000064 | 2 | 5 | BS | 0 | H | AccountsReceivableNetCurrent | ... |

#### File: `DATA/2023q2/sub.txt`

- **Size:** 2.33 MB
- **Total Rows:** 8,039
- **Total Columns:** 36
- **Category Columns:** countryba, countryma, countryinc, afs, form, fp, aciks
- **Numeric Columns:** cik, sic, zipba, zipma, ein, changed, wksi, fye, period, fy, filed, prevrpt, detail, nciks
- **Text Columns:** adsh, name, stprba, cityba, bas1, bas2, baph, stprma, cityma, mas1, mas2, stprinc, former, accepted, instance

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **countryba** | 2 | `CA`, `US` |
| **countryma** | 2 | `CA`, `US` |
| **countryinc** | 2 | ``, `US` |
| **afs** | 3 | `1-LAF`, `2-ACC`, `4-NON` |
| **form** | 3 | `10-K`, `10-Q`, `8-K` |
| **fp** | 4 | `FY`, `Q1`, `Q2`, `Q3` |
| **aciks** | 4 | ``, `1901876`, `4515`, `81027 73986 92487 1702494 50172 1721781 6879` |

##### Sample Records

| adsh | cik | name | sic | countryba | stprba | cityba | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002178-23-000064 | 2178 | ADAMS RESOURCES & ENERGY, INC. | 5172 | US | TX | HOUSTON | ... |
| 0000002488-23-000076 | 2488 | ADVANCED MICRO DEVICES INC | 3674 | US | CA | SANTA CLARA | ... |
| 0000002969-23-000023 | 2969 | AIR PRODUCTS & CHEMICALS, INC. | 2810 | US | PA | ALLENTOWN | ... |

#### File: `DATA/2023q2/tag.txt`

- **Size:** 21.21 MB
- **Total Rows:** 106,511
- **Total Columns:** 9
- **Category Columns:** version, datatype, iord, crdr
- **Numeric Columns:** custom, abstract
- **Text Columns:** tag, tlabel, doc

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 1 | `us-gaap/2021` |
| **datatype** | 2 | `monetary`, `shares` |
| **iord** | 2 | `D`, `I` |
| **crdr** | 3 | ``, `C`, `D` |

##### Sample Records

| tag | version | custom | abstract | datatype | iord | crdr | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AccountsAndNotesReceivableNet | us-gaap/2021 | 0 | 0 | monetary | I | D | ... |
| AccountsAndOtherReceivablesNetCurrent | us-gaap/2021 | 0 | 0 | monetary | I | D | ... |
| AccountsNotesAndLoansReceivableNetCur... | us-gaap/2021 | 0 | 0 | monetary | I | D | ... |

---

### Quarter: `2023q3`

#### File: `DATA/2023q3/num.txt`

- **Size:** 471.34 MB
- **Total Rows:** 3,572,434
- **Total Columns:** 10
- **Category Columns:** version, uom
- **Numeric Columns:** ddate, qtrs, value
- **Text Columns:** adsh, tag, segments, coreg, footnote

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 10 | `0000277509-23-000047`, `0000895417-23-000059`, `0000933036-23-000141`, `0001140361-23-037198`, `0001193125-23-223657`, `0001437749-23-025909`, `0001466026-23-000024`, `ifrs/2023`, `us-gaap/2022`, `us-gaap/2023` |
| **uom** | 5 | `CAD`, `INR`, `USD`, `pure`, `shares` |

##### Sample Records

| adsh | tag | version | ddate | qtrs | uom | segments | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000950170-23-041482 | AllocatedShareBasedCompensationExpense | us-gaap/2022 | 20230630 | 2 | USD |  | ... |
| 0000879526-23-000036 | ComprehensiveIncomeNetOfTaxIncludingP... | us-gaap/2023 | 20230630 | 1 | USD |  | ... |
| 0000950170-23-039847 | ComprehensiveIncomeNetOfTaxIncludingP... | us-gaap/2023 | 20230630 | 2 | USD |  | ... |

#### File: `DATA/2023q3/pre.txt`

- **Size:** 90.02 MB
- **Total Rows:** 774,797
- **Total Columns:** 10
- **Category Columns:** adsh, stmt, rfile, version
- **Numeric Columns:** report, line, inpth, negating
- **Text Columns:** tag, plabel

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **adsh** | 2 | `0000002178-23-000082`, `0000002488-23-000139` |
| **stmt** | 4 | `BS`, `CF`, `EQ`, `IS` |
| **rfile** | 1 | `H` |
| **version** | 3 | `0000002178-23-000082`, `0000002488-23-000139`, `us-gaap/2023` |

##### Sample Records

| adsh | report | line | stmt | inpth | rfile | tag | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002178-23-000082 | 2 | 9 | BS | 0 | H | CashAndCashEquivalentsAtCarryingValue | ... |
| 0000002178-23-000082 | 2 | 10 | BS | 0 | H | RestrictedCashCurrent | ... |
| 0000002178-23-000082 | 2 | 11 | BS | 0 | H | AccountsReceivableNetCurrent | ... |

#### File: `DATA/2023q3/sub.txt`

- **Size:** 2.03 MB
- **Total Rows:** 7,067
- **Total Columns:** 36
- **Category Columns:** countryba, countryma, countryinc, afs, form, fp, aciks
- **Numeric Columns:** cik, sic, zipba, zipma, ein, changed, wksi, fye, period, fy, filed, prevrpt, detail, nciks
- **Text Columns:** adsh, name, stprba, cityba, bas1, bas2, baph, stprma, cityma, mas1, mas2, stprinc, former, accepted, instance

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **countryba** | 2 | `CA`, `US` |
| **countryma** | 2 | `CA`, `US` |
| **countryinc** | 2 | ``, `US` |
| **afs** | 3 | `1-LAF`, `2-ACC`, `4-NON` |
| **form** | 3 | `10-K`, `10-Q`, `10-Q/A` |
| **fp** | 4 | `FY`, `Q1`, `Q2`, `Q3` |
| **aciks** | 4 | ``, `1901876`, `4515`, `81027 73986 92487 1702494 50172 1721781 6879` |

##### Sample Records

| adsh | cik | name | sic | countryba | stprba | cityba | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002178-23-000082 | 2178 | ADAMS RESOURCES & ENERGY, INC. | 5172 | US | TX | HOUSTON | ... |
| 0000002488-23-000139 | 2488 | ADVANCED MICRO DEVICES INC | 3674 | US | CA | SANTA CLARA | ... |
| 0000002969-23-000037 | 2969 | AIR PRODUCTS & CHEMICALS, INC. | 2810 | US | PA | ALLENTOWN | ... |

#### File: `DATA/2023q3/tag.txt`

- **Size:** 17.85 MB
- **Total Rows:** 89,580
- **Total Columns:** 9
- **Category Columns:** version, datatype, iord, crdr
- **Numeric Columns:** custom, abstract
- **Text Columns:** tag, tlabel, doc

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 2 | `dei/2022`, `us-gaap/2022` |
| **datatype** | 2 | `monetary`, `pure` |
| **iord** | 2 | `D`, `I` |
| **crdr** | 3 | ``, `C`, `D` |

##### Sample Records

| tag | version | custom | abstract | datatype | iord | crdr | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EntityListingDepositoryReceiptRatio | dei/2022 | 0 | 0 | pure | I |  | ... |
| AccountsAndFinancingReceivableAllowan... | us-gaap/2022 | 0 | 0 | monetary | I | C | ... |
| AccountsAndNotesReceivableNet | us-gaap/2022 | 0 | 0 | monetary | I | D | ... |

---

### Quarter: `2023q4`

#### File: `DATA/2023q4/num.txt`

- **Size:** 490.46 MB
- **Total Rows:** 3,699,124
- **Total Columns:** 10
- **Category Columns:** version, uom, coreg
- **Numeric Columns:** ddate, qtrs, value
- **Text Columns:** adsh, tag, segments, footnote

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 9 | `0001140361-23-048206`, `0001140361-23-052812`, `0001213900-23-099953`, `0001410578-23-002441`, `0001493152-23-045550`, `0001784535-23-000048`, `ifrs/2023`, `us-gaap/2022`, `us-gaap/2023` |
| **uom** | 6 | `CAD`, `EUR`, `JPY`, `USD`, `pure`, `shares` |
| **coreg** | 2 | ``, `VICIPropertiesLP` |

##### Sample Records

| adsh | tag | version | ddate | qtrs | uom | segments | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0001437749-23-031921 | AccumulatedOtherComprehensiveIncomeLo... | us-gaap/2023 | 20221231 | 0 | USD |  | ... |
| 0001493152-23-045550 | AdjustmentsForDecreaseIncreaseInGover... | 0001493152-23-045550 | 20220831 | 4 | USD |  | ... |
| 0000950123-23-011049 | RevenueFromContractWithCustomerExclud... | us-gaap/2023 | 20230930 | 4 | USD | ProductOrService=ComputerAidedDesign; | ... |

#### File: `DATA/2023q4/pre.txt`

- **Size:** 89.70 MB
- **Total Rows:** 769,208
- **Total Columns:** 10
- **Category Columns:** adsh, stmt, rfile, version
- **Numeric Columns:** report, line, inpth, negating
- **Text Columns:** tag, plabel

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **adsh** | 1 | `0000002178-23-000091` |
| **stmt** | 4 | `BS`, `CF`, `EQ`, `IS` |
| **rfile** | 1 | `H` |
| **version** | 2 | `0000002178-23-000091`, `us-gaap/2023` |

##### Sample Records

| adsh | report | line | stmt | inpth | rfile | tag | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002178-23-000091 | 2 | 9 | BS | 0 | H | CashAndCashEquivalentsAtCarryingValue | ... |
| 0000002178-23-000091 | 2 | 10 | BS | 0 | H | RestrictedCashCurrent | ... |
| 0000002178-23-000091 | 2 | 11 | BS | 0 | H | AccountsReceivableNetCurrent | ... |

#### File: `DATA/2023q4/sub.txt`

- **Size:** 1.98 MB
- **Total Rows:** 6,882
- **Total Columns:** 36
- **Category Columns:** countryba, countryma, countryinc, afs, form, fp, aciks
- **Numeric Columns:** cik, sic, zipba, zipma, ein, changed, wksi, fye, period, fy, filed, prevrpt, detail, nciks
- **Text Columns:** adsh, name, stprba, cityba, bas1, bas2, baph, stprma, cityma, mas1, mas2, stprinc, former, accepted, instance

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **countryba** | 2 | `CA`, `US` |
| **countryma** | 2 | `CA`, `US` |
| **countryinc** | 2 | ``, `US` |
| **afs** | 3 | `1-LAF`, `2-ACC`, `4-NON` |
| **form** | 2 | `10-K`, `10-Q` |
| **fp** | 4 | `FY`, `Q1`, `Q2`, `Q3` |
| **aciks** | 4 | ``, `1901876`, `4515`, `81027 73986 92487 1702494 50172 1721781 6879` |

##### Sample Records

| adsh | cik | name | sic | countryba | stprba | cityba | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002178-23-000091 | 2178 | ADAMS RESOURCES & ENERGY, INC. | 5172 | US | TX | HOUSTON | ... |
| 0000002488-23-000195 | 2488 | ADVANCED MICRO DEVICES INC | 3674 | US | CA | SANTA CLARA | ... |
| 0000002969-23-000047 | 2969 | AIR PRODUCTS & CHEMICALS, INC. | 2810 | US | PA | ALLENTOWN | ... |

#### File: `DATA/2023q4/tag.txt`

- **Size:** 17.56 MB
- **Total Rows:** 88,228
- **Total Columns:** 9
- **Category Columns:** version, datatype, iord, crdr
- **Numeric Columns:** custom, abstract
- **Text Columns:** tag, tlabel, doc

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 1 | `us-gaap/2022` |
| **datatype** | 1 | `monetary` |
| **iord** | 2 | `D`, `I` |
| **crdr** | 2 | `C`, `D` |

##### Sample Records

| tag | version | custom | abstract | datatype | iord | crdr | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AccountsAndNotesReceivableNet | us-gaap/2022 | 0 | 0 | monetary | I | D | ... |
| AccountsAndOtherReceivablesNetCurrent | us-gaap/2022 | 0 | 0 | monetary | I | D | ... |
| AccountsNotesAndLoansReceivableNetCur... | us-gaap/2022 | 0 | 0 | monetary | I | D | ... |

---

### Quarter: `2024q1`

#### File: `DATA/2024q1/num.txt`

- **Size:** 464.20 MB
- **Total Rows:** 3,428,694
- **Total Columns:** 10
- **Category Columns:** version, uom
- **Numeric Columns:** ddate, qtrs, value
- **Text Columns:** adsh, tag, segments, coreg, footnote

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 14 | `0000034903-24-000032`, `0000200406-24-000013`, `0000950170-24-016336`, `0001097362-24-000007`, `0001171520-24-000130`, `0001437749-24-005794`, `0001493152-24-011639`, `0001537435-24-000022`, `0001558370-24-001254`, `0001558370-24-002368`, `0001584425-24-000014`, `0001628280-24-008857`, `ifrs/2023`, `us-gaap/2023` |
| **uom** | 8 | `CAD`, `DKK`, `EUR`, `GBP`, `Rate`, `USD`, `pure`, `shares` |

##### Sample Records

| adsh | tag | version | ddate | qtrs | uom | segments | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0001477932-24-000711 | AccruedLiabilitiesCurrent | us-gaap/2023 | 20231231 | 0 | USD |  | ... |
| 0001025378-24-000037 | AllocatedShareBasedCompensationExpense | us-gaap/2023 | 20211231 | 4 | USD |  | ... |
| 0001213900-24-027206 | AdjustmentsToAdditionalPaidInCapitalS... | us-gaap/2023 | 20221231 | 4 | USD |  | ... |

#### File: `DATA/2024q1/pre.txt`

- **Size:** 85.51 MB
- **Total Rows:** 726,155
- **Total Columns:** 10
- **Category Columns:** stmt, rfile, version
- **Numeric Columns:** report, line, inpth, negating
- **Text Columns:** adsh, tag, plabel

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **stmt** | 6 | `BS`, `CF`, `CI`, `EQ`, `IS`, `UN` |
| **rfile** | 1 | `H` |
| **version** | 17 | `0000798359-24-000019`, `0000950170-24-023267`, `0001124796-24-000018`, `0001193125-24-006261`, `0001193125-24-047942`, `0001213900-24-014155`, `0001356115-24-000007`, `0001410578-24-000239`, `0001433660-24-000008`, `0001437749-24-008852`, `0001493152-24-006734`, `0001545772-24-000004`, `0001628280-24-002923`, `0001683168-24-000494`, `0001830210-24-000025` ... (and more) |

##### Sample Records

| adsh | report | line | stmt | inpth | rfile | tag | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000950170-24-015673 | 3 | 14 | CF | 0 | H | IncreaseDecreaseInDeferredIncomeTaxes | ... |
| 0001477932-24-000767 | 4 | 17 | IS | 0 | H | IncomeLossFromContinuingOperationsBef... | ... |
| 0001071739-24-000037 | 3 | 21 | BS | 0 | H | LongTermDebtCurrent | ... |

#### File: `DATA/2024q1/sub.txt`

- **Size:** 1.73 MB
- **Total Rows:** 6,028
- **Total Columns:** 36
- **Category Columns:** countryba, countryma, countryinc, stprinc, afs, form, fp, aciks
- **Numeric Columns:** cik, sic, ein, changed, wksi, fye, period, fy, filed, prevrpt, detail, nciks
- **Text Columns:** adsh, name, stprba, cityba, zipba, bas1, bas2, baph, stprma, cityma, zipma, mas1, mas2, former, accepted, instance

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **countryba** | 12 | ``, `BM`, `CA`, `CH`, `CN`, `DE`, `GB`, `IL`, `JP`, `LU`, `MY`, `US` |
| **countryma** | 11 | ``, `BM`, `CA`, `DE`, `GB`, `IL`, `JP`, `LU`, `MY`, `US`, `VG` |
| **countryinc** | 8 | ``, `BM`, `CA`, `GB`, `IL`, `JP`, `US`, `VG` |
| **stprinc** | 19 | ``, `AB`, `BC`, `DE`, `FL`, `GA`, `MA`, `MD`, `MN`, `NC`, `NJ`, `NV`, `NY`, `OH`, `ON` ... (and more) |
| **afs** | 4 | ``, `1-LAF`, `2-ACC`, `4-NON` |
| **form** | 8 | `10-K`, `10-Q`, `20-F`, `40-F`, `6-K`, `F-1`, `S-1/A`, `SP 15D2` |
| **fp** | 5 | ``, `FY`, `Q1`, `Q2`, `Q3` |
| **aciks** | 2 | ``, `3153 41091 1160661 1004155 66904` |

##### Sample Records

| adsh | cik | name | sic | countryba | stprba | cityba | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0001161697-24-000084 | 1438901 | AUTO PARTS 4LESS GROUP, INC. | 7389 | US | NV | NORTH LAS VEGAS | ... |
| 0001059556-24-000017 | 1059556 | MOODYS CORP /DE/ | 7320 | US | NY | NEW YORK | ... |
| 0001206264-24-000050 | 1206264 | TEMPUR SEALY INTERNATIONAL, INC. | 2510 | US | KY | LEXINGTON | ... |

#### File: `DATA/2024q1/tag.txt`

- **Size:** 17.76 MB
- **Total Rows:** 86,529
- **Total Columns:** 9
- **Category Columns:** version, datatype, iord, crdr
- **Numeric Columns:** custom, abstract
- **Text Columns:** tag, tlabel, doc

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 1 | `us-gaap/2022` |
| **datatype** | 2 | `monetary`, `perShare` |
| **iord** | 2 | `D`, `I` |
| **crdr** | 3 | ``, `C`, `D` |

##### Sample Records

| tag | version | custom | abstract | datatype | iord | crdr | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AccountsAndNotesReceivableNet | us-gaap/2022 | 0 | 0 | monetary | I | D | ... |
| AccountsAndOtherReceivablesNetCurrent | us-gaap/2022 | 0 | 0 | monetary | I | D | ... |
| AccountsNotesAndLoansReceivableNetCur... | us-gaap/2022 | 0 | 0 | monetary | I | D | ... |

---

### Quarter: `2024q2`

#### File: `DATA/2024q2/num.txt`

- **Size:** 460.00 MB
- **Total Rows:** 3,426,170
- **Total Columns:** 10
- **Category Columns:** version, uom, coreg
- **Numeric Columns:** ddate, qtrs, value
- **Text Columns:** adsh, tag, segments, footnote

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 9 | `0001062993-24-009960`, `0001193125-24-098519`, `0001287750-24-000028`, `0001410578-24-000966`, `0001493152-24-012404`, `0001671284-24-000037`, `ifrs/2023`, `us-gaap/2023`, `us-gaap/2024` |
| **uom** | 9 | `CAD`, `CLP`, `CNY`, `KRW`, `MXN`, `SGD`, `USD`, `pure`, `shares` |
| **coreg** | 3 | ``, `ProgressEnergy`, `VerisResidentialLP` |

##### Sample Records

| adsh | tag | version | ddate | qtrs | uom | segments | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0001104659-24-066053 | AdjustmentsForDecreaseIncreaseInInven... | ifrs/2023 | 20230331 | 3 | USD |  | ... |
| 0001437749-24-016942 | AllowanceForDoubtfulAccountsReceivabl... | us-gaap/2024 | 20230930 | 0 | USD |  | ... |
| 0000950170-24-053731 | RevenueFromContractWithCustomerInclud... | us-gaap/2023 | 20240331 | 1 | USD | ProductOrService=OilAndCondensate; | ... |

#### File: `DATA/2024q2/pre.txt`

- **Size:** 97.22 MB
- **Total Rows:** 838,475
- **Total Columns:** 10
- **Category Columns:** adsh, stmt, rfile, version
- **Numeric Columns:** report, line, inpth, negating
- **Text Columns:** tag, plabel

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **adsh** | 2 | `0000002178-24-000054`, `0000002488-24-000056` |
| **stmt** | 4 | `BS`, `CF`, `EQ`, `IS` |
| **rfile** | 1 | `H` |
| **version** | 4 | `0000002178-24-000054`, `0000002488-24-000056`, `us-gaap/2023`, `us-gaap/2024` |

##### Sample Records

| adsh | report | line | stmt | inpth | rfile | tag | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002178-24-000054 | 2 | 8 | BS | 0 | H | CashAndCashEquivalentsAtCarryingValue | ... |
| 0000002178-24-000054 | 2 | 9 | BS | 0 | H | RestrictedCashCurrent | ... |
| 0000002178-24-000054 | 2 | 10 | BS | 0 | H | AccountsReceivableNetCurrent | ... |

#### File: `DATA/2024q2/sub.txt`

- **Size:** 2.22 MB
- **Total Rows:** 7,675
- **Total Columns:** 36
- **Category Columns:** countryba, countryma, countryinc, afs, form, fp, aciks
- **Numeric Columns:** cik, sic, zipba, zipma, ein, changed, wksi, fye, period, fy, filed, prevrpt, detail, nciks
- **Text Columns:** adsh, name, stprba, cityba, bas1, bas2, baph, stprma, cityma, mas1, mas2, stprinc, former, accepted, instance

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **countryba** | 2 | `CA`, `US` |
| **countryma** | 2 | `CA`, `US` |
| **countryinc** | 2 | ``, `US` |
| **afs** | 3 | `1-LAF`, `2-ACC`, `4-NON` |
| **form** | 2 | `10-K`, `10-Q` |
| **fp** | 4 | `FY`, `Q1`, `Q2`, `Q3` |
| **aciks** | 4 | ``, `1901876`, `4515`, `81027 73986 92487 1702494 50172 1721781 6879` |

##### Sample Records

| adsh | cik | name | sic | countryba | stprba | cityba | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002178-24-000054 | 2178 | ADAMS RESOURCES & ENERGY, INC. | 5172 | US | TX | HOUSTON | ... |
| 0000002488-24-000056 | 2488 | ADVANCED MICRO DEVICES INC | 3674 | US | CA | SANTA CLARA | ... |
| 0000002969-24-000026 | 2969 | AIR PRODUCTS & CHEMICALS, INC. | 2810 | US | PA | ALLENTOWN | ... |

#### File: `DATA/2024q2/tag.txt`

- **Size:** 19.33 MB
- **Total Rows:** 97,771
- **Total Columns:** 9
- **Category Columns:** version, datatype, iord, crdr
- **Numeric Columns:** custom, abstract
- **Text Columns:** tag, tlabel, doc

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 1 | `us-gaap/2022` |
| **datatype** | 3 | `monetary`, `perShare`, `shares` |
| **iord** | 2 | `D`, `I` |
| **crdr** | 3 | ``, `C`, `D` |

##### Sample Records

| tag | version | custom | abstract | datatype | iord | crdr | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AccountsAndNotesReceivableNet | us-gaap/2022 | 0 | 0 | monetary | I | D | ... |
| AccountsPayableAndAccruedLiabilitiesC... | us-gaap/2022 | 0 | 0 | monetary | I | C | ... |
| AccountsPayableAndAccruedLiabilitiesC... | us-gaap/2022 | 0 | 0 | monetary | I | C | ... |

---

### Quarter: `2024q3`

#### File: `DATA/2024q3/num.txt`

- **Size:** 475.00 MB
- **Total Rows:** 3,521,878
- **Total Columns:** 10
- **Category Columns:** version, uom, coreg
- **Numeric Columns:** ddate, qtrs, value
- **Text Columns:** adsh, tag, segments, footnote

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 12 | `0000950170-24-093956`, `0001079973-24-001225`, `0001140361-24-037313`, `0001193125-24-173038`, `0001213900-24-066111`, `0001213900-24-069540`, `0001654954-24-012498`, `0001792509-24-000029`, `0001829126-24-004668`, `ifrs/2023`, `us-gaap/2023`, `us-gaap/2024` |
| **uom** | 6 | `CAD`, `GBP`, `Rate`, `USD`, `pure`, `shares` |
| **coreg** | 3 | ``, `FranklinResponsiblySourcedGoldEtf`, `LouisvilleGasAndElectricCo` |

##### Sample Records

| adsh | tag | version | ddate | qtrs | uom | segments | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0001558370-24-011687 | AdditionalPaidInCapital | us-gaap/2024 | 20240630 | 0 | USD |  | ... |
| 0001493152-24-032736 | AccruedPayrollTaxesCurrent | us-gaap/2024 | 20231231 | 0 | USD |  | ... |
| 0001213900-24-067651 | AccretionAmortizationOfDiscountsAndPr... | us-gaap/2024 | 20240630 | 2 | USD |  | ... |

#### File: `DATA/2024q3/pre.txt`

- **Size:** 86.28 MB
- **Total Rows:** 741,760
- **Total Columns:** 10
- **Category Columns:** adsh, stmt, rfile, version
- **Numeric Columns:** report, line, inpth, negating
- **Text Columns:** tag, plabel

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **adsh** | 2 | `0000002178-24-000076`, `0000002488-24-000123` |
| **stmt** | 4 | `BS`, `CF`, `EQ`, `IS` |
| **rfile** | 1 | `H` |
| **version** | 3 | `0000002178-24-000076`, `0000002488-24-000123`, `us-gaap/2024` |

##### Sample Records

| adsh | report | line | stmt | inpth | rfile | tag | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002178-24-000076 | 2 | 8 | BS | 0 | H | CashAndCashEquivalentsAtCarryingValue | ... |
| 0000002178-24-000076 | 2 | 9 | BS | 0 | H | RestrictedCashCurrent | ... |
| 0000002178-24-000076 | 2 | 10 | BS | 0 | H | AccountsReceivableNetCurrent | ... |

#### File: `DATA/2024q3/sub.txt`

- **Size:** 1.93 MB
- **Total Rows:** 6,699
- **Total Columns:** 36
- **Category Columns:** countryba, countryma, countryinc, afs, form, fp, aciks
- **Numeric Columns:** cik, sic, zipba, zipma, ein, changed, wksi, fye, period, fy, filed, prevrpt, detail, nciks
- **Text Columns:** adsh, name, stprba, cityba, bas1, bas2, baph, stprma, cityma, mas1, mas2, stprinc, former, accepted, instance

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **countryba** | 2 | `CA`, `US` |
| **countryma** | 2 | `CA`, `US` |
| **countryinc** | 2 | ``, `US` |
| **afs** | 3 | `1-LAF`, `2-ACC`, `4-NON` |
| **form** | 2 | `10-K`, `10-Q` |
| **fp** | 4 | `FY`, `Q1`, `Q2`, `Q3` |
| **aciks** | 4 | ``, `1901876`, `4515`, `81027 73986 92487 1702494 50172 1721781 6879` |

##### Sample Records

| adsh | cik | name | sic | countryba | stprba | cityba | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002178-24-000076 | 2178 | ADAMS RESOURCES & ENERGY, INC. | 5172 | US | TX | HOUSTON | ... |
| 0000002488-24-000123 | 2488 | ADVANCED MICRO DEVICES INC | 3674 | US | CA | SANTA CLARA | ... |
| 0000002969-24-000043 | 2969 | AIR PRODUCTS & CHEMICALS, INC. | 2810 | US | PA | ALLENTOWN | ... |

#### File: `DATA/2024q3/tag.txt`

- **Size:** 16.70 MB
- **Total Rows:** 83,106
- **Total Columns:** 9
- **Category Columns:** version, datatype, iord, crdr
- **Numeric Columns:** custom, abstract
- **Text Columns:** tag, tlabel, doc

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 1 | `us-gaap/2023` |
| **datatype** | 4 | `monetary`, `perShare`, `percent`, `shares` |
| **iord** | 2 | `D`, `I` |
| **crdr** | 3 | ``, `C`, `D` |

##### Sample Records

| tag | version | custom | abstract | datatype | iord | crdr | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AccountsPayableAndAccruedLiabilitiesC... | us-gaap/2023 | 0 | 0 | monetary | I | C | ... |
| AccountsPayableAndOtherAccruedLiabili... | us-gaap/2023 | 0 | 0 | monetary | I | C | ... |
| AccountsPayableCurrent | us-gaap/2023 | 0 | 0 | monetary | I | C | ... |

---

### Quarter: `2024q4`

#### File: `DATA/2024q4/num.txt`

- **Size:** 502.73 MB
- **Total Rows:** 3,705,078
- **Total Columns:** 10
- **Category Columns:** version, uom, coreg
- **Numeric Columns:** ddate, qtrs, value
- **Text Columns:** adsh, tag, segments, footnote

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 11 | `0001026214-24-000097`, `0001410578-24-001943`, `0001493152-24-045889`, `0001558370-24-013239`, `0001628280-24-045970`, `0001825248-24-000018`, `0002024218-24-000034`, `ifrs/2023`, `ifrs/2024`, `us-gaap/2023`, `us-gaap/2024` |
| **uom** | 4 | `CAD`, `USD`, `pure`, `shares` |
| **coreg** | 2 | ``, `TheBank` |

##### Sample Records

| adsh | tag | version | ddate | qtrs | uom | segments | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000950170-24-120982 | NetIncomeLoss | us-gaap/2024 | 20240331 | 1 | USD | EquityComponents=RetainedEarnings; | ... |
| 0000104889-24-000065 | RetainedEarningsAccumulatedDeficit | us-gaap/2024 | 20231231 | 0 | USD |  | ... |
| 0000789933-24-000055 | IncomeLossFromContinuingOperationsBef... | us-gaap/2024 | 20240930 | 1 | USD |  | ... |

#### File: `DATA/2024q4/pre.txt`

- **Size:** 86.21 MB
- **Total Rows:** 737,504
- **Total Columns:** 10
- **Category Columns:** adsh, stmt, rfile, version
- **Numeric Columns:** report, line, inpth, negating
- **Text Columns:** tag, plabel

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **adsh** | 2 | `0000002178-24-000096`, `0000002488-24-000163` |
| **stmt** | 4 | `BS`, `CF`, `EQ`, `IS` |
| **rfile** | 1 | `H` |
| **version** | 3 | `0000002178-24-000096`, `0000002488-24-000163`, `us-gaap/2024` |

##### Sample Records

| adsh | report | line | stmt | inpth | rfile | tag | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002178-24-000096 | 2 | 8 | BS | 0 | H | CashAndCashEquivalentsAtCarryingValue | ... |
| 0000002178-24-000096 | 2 | 9 | BS | 0 | H | RestrictedCashCurrent | ... |
| 0000002178-24-000096 | 2 | 10 | BS | 0 | H | AccountsReceivableNetCurrent | ... |

#### File: `DATA/2024q4/sub.txt`

- **Size:** 1.87 MB
- **Total Rows:** 6,491
- **Total Columns:** 36
- **Category Columns:** countryba, countryma, countryinc, stprinc, afs, form, fp
- **Numeric Columns:** cik, sic, zipba, zipma, ein, changed, wksi, fye, period, fy, filed, prevrpt, detail, nciks, aciks
- **Text Columns:** adsh, name, stprba, cityba, bas1, bas2, baph, stprma, cityma, mas1, mas2, former, accepted, instance

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **countryba** | 12 | ``, `AE`, `AU`, `CA`, `CH`, `CN`, `DE`, `GB`, `IE`, `JP`, `SG`, `US` |
| **countryma** | 11 | `AE`, `AU`, `CA`, `CH`, `CN`, `DE`, `GB`, `IE`, `JP`, `SG`, `US` |
| **countryinc** | 8 | ``, `AU`, `BM`, `CA`, `IE`, `KY`, `US`, `VG` |
| **stprinc** | 20 | ``, `CA`, `CO`, `DE`, `FL`, `GA`, `IN`, `MD`, `MS`, `NC`, `NJ`, `NM`, `NV`, `NY`, `OH` ... (and more) |
| **afs** | 4 | ``, `1-LAF`, `2-ACC`, `4-NON` |
| **form** | 10 | `10-K`, `10-Q`, `10-Q/A`, `20-F`, `6-K`, `F-1`, `F-1/A`, `S-1`, `S-1/A`, `S-4/A` |
| **fp** | 5 | ``, `FY`, `Q1`, `Q2`, `Q3` |

##### Sample Records

| adsh | cik | name | sic | countryba | stprba | cityba | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0001628280-24-043777 | 789460 | WORLD KINECT CORP | 5172 | US | FL | MIAMI | ... |
| 0000950170-24-122438 | 1720116 | RED VIOLET, INC. | 7372 | US | FL | BOCA RATON | ... |
| 0000060667-24-000169 | 60667 | LOWES COMPANIES INC | 5211 | US | NC | MOORESVILLE | ... |

#### File: `DATA/2024q4/tag.txt`

- **Size:** 16.86 MB
- **Total Rows:** 84,365
- **Total Columns:** 9
- **Category Columns:** version, datatype, iord, crdr
- **Numeric Columns:** custom, abstract
- **Text Columns:** tag, tlabel, doc

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 1 | `us-gaap/2023` |
| **datatype** | 4 | `monetary`, `perShare`, `percent`, `shares` |
| **iord** | 2 | `D`, `I` |
| **crdr** | 3 | ``, `C`, `D` |

##### Sample Records

| tag | version | custom | abstract | datatype | iord | crdr | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AccountsPayableAndAccruedLiabilitiesC... | us-gaap/2023 | 0 | 0 | monetary | I | C | ... |
| AccountsPayableAndOtherAccruedLiabili... | us-gaap/2023 | 0 | 0 | monetary | I | C | ... |
| AccountsPayableCurrent | us-gaap/2023 | 0 | 0 | monetary | I | C | ... |

---

### Quarter: `2025q1`

#### File: `DATA/2025q1/num.txt`

- **Size:** 505.63 MB
- **Total Rows:** 3,658,551
- **Total Columns:** 10
- **Category Columns:** version, uom, coreg
- **Numeric Columns:** ddate, qtrs, value
- **Text Columns:** adsh, tag, segments, footnote

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 11 | `0000950170-25-026749`, `0001398344-25-006254`, `0001437749-25-006260`, `0001477932-25-002250`, `0001558370-25-000687`, `0001558370-25-001424`, `0001628280-25-008531`, `0001756125-25-000627`, `ifrs/2024`, `us-gaap/2023`, `us-gaap/2024` |
| **uom** | 4 | `CAD`, `GBP`, `USD`, `shares` |
| **coreg** | 4 | ``, `NorthwestNaturalGasCompany`, `PublicServiceCompanyOfNewMexico`, `TangerPropertiesLimitedPartnership` |

##### Sample Records

| adsh | tag | version | ddate | qtrs | uom | segments | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000070145-25-000007 | IncreaseDecreaseInAccountsPayableTrade | us-gaap/2024 | 20241231 | 1 | USD |  | ... |
| 0000351569-25-000006 | OtherIntangibleAssetsNet | us-gaap/2024 | 20241231 | 0 | USD |  | ... |
| 0001555280-25-000102 | OtherComprehensiveIncomeLossCashFlowH... | us-gaap/2024 | 20241231 | 4 | USD | DerivativeInstrumentRisk=NetInvestmen... | ... |

#### File: `DATA/2025q1/pre.txt`

- **Size:** 88.39 MB
- **Total Rows:** 750,778
- **Total Columns:** 10
- **Category Columns:** adsh, stmt, rfile, version
- **Numeric Columns:** report, line, inpth, negating
- **Text Columns:** tag, plabel

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **adsh** | 1 | `0000002488-25-000012` |
| **stmt** | 5 | `BS`, `CF`, `CI`, `EQ`, `IS` |
| **rfile** | 1 | `H` |
| **version** | 2 | `0000002488-25-000012`, `us-gaap/2024` |

##### Sample Records

| adsh | report | line | stmt | inpth | rfile | tag | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002488-25-000012 | 3 | 1 | IS | 0 | H | RevenueFromContractWithCustomerExclud... | ... |
| 0000002488-25-000012 | 3 | 2 | IS | 0 | H | CostOfGoodsAndServiceExcludingDepreci... | ... |
| 0000002488-25-000012 | 3 | 3 | IS | 0 | H | CostDepreciationAmortizationAndDepletion | ... |

#### File: `DATA/2025q1/sub.txt`

- **Size:** 1.79 MB
- **Total Rows:** 6,231
- **Total Columns:** 36
- **Category Columns:** countryba, countryma, countryinc, afs, form, fp
- **Numeric Columns:** cik, sic, zipba, zipma, ein, changed, wksi, fye, period, fy, filed, prevrpt, detail, nciks, aciks
- **Text Columns:** adsh, name, stprba, cityba, bas1, bas2, baph, stprma, cityma, mas1, mas2, stprinc, former, accepted, instance

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **countryba** | 2 | `CA`, `US` |
| **countryma** | 2 | `CA`, `US` |
| **countryinc** | 3 | ``, `CA`, `US` |
| **afs** | 4 | ``, `1-LAF`, `2-ACC`, `4-NON` |
| **form** | 3 | `10-K`, `10-Q`, `6-K` |
| **fp** | 4 | `FY`, `Q1`, `Q2`, `Q3` |

##### Sample Records

| adsh | cik | name | sic | countryba | stprba | cityba | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000015615-25-000021 | 15615 | MASTEC INC | 1623 | US | FL | CORAL GABLES | ... |
| 0000016058-25-000032 | 16058 | CACI INTERNATIONAL INC /DE/ | 7373 | US | VA | RESTON | ... |
| 0000016732-25-000026 | 16732 | CAMPBELL'S CO | 2000 | US | NJ | CAMDEN | ... |

#### File: `DATA/2025q1/tag.txt`

- **Size:** 18.49 MB
- **Total Rows:** 90,655
- **Total Columns:** 9
- **Category Columns:** datatype, iord, crdr
- **Numeric Columns:** custom, abstract
- **Text Columns:** tag, version, tlabel, doc

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **datatype** | 3 | `monetary`, `perShare`, `shares` |
| **iord** | 2 | `D`, `I` |
| **crdr** | 3 | ``, `C`, `D` |

##### Sample Records

| tag | version | custom | abstract | datatype | iord | crdr | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ContractWithCustomerLiabilityNetOfDis... | 0000940944-25-000003 | 1 | 0 | monetary | I | C | ... |
| IncreaseDecreaseInOtherOperatingCapital | 0000940944-25-000003 | 1 | 0 | monetary | D | C | ... |
| OtherComprehensiveIncomeLossUnrecogni... | 0000940944-25-000003 | 1 | 0 | monetary | D | C | ... |

---

### Quarter: `2025q2`

#### File: `DATA/2025q2/num.txt`

- **Size:** 475.17 MB
- **Total Rows:** 3,409,930
- **Total Columns:** 10
- **Category Columns:** adsh, version, uom, footnote
- **Numeric Columns:** ddate, qtrs, value
- **Text Columns:** tag, segments, coreg

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **adsh** | 2 | `0000002488-25-000047`, `0000002969-25-000027` |
| **version** | 3 | `0000002488-25-000047`, `us-gaap/2024`, `us-gaap/2025` |
| **uom** | 2 | `USD`, `shares` |
| **footnote** | 2 | ``, `Includes balances associated with a consolidated variable interest entity ("VIE"), including amounts reflected in "Total Assets" that can only be used to settle obligations of the VIE of $6,225.5 and $4,393.9 as of 31 March 2025 and 30 September 2024, respectively, as well as liabilities of the VIE reflected within "Total Liabilities" for which creditors do not have recourse to the general credit of Air Products of $4,479.5 and $3,473.4 as of 31 March 2025 and 30 September 2024, respectively. Refer to Note` |

##### Sample Records

| adsh | tag | version | ddate | qtrs | uom | segments | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002488-25-000047 | AccountsPayableCurrent | us-gaap/2025 | 20250331 | 0 | USD |  | ... |
| 0000002488-25-000047 | AssetsCurrent | us-gaap/2025 | 20250331 | 0 | USD |  | ... |
| 0000002488-25-000047 | CashAndCashEquivalentsAtCarryingValue... | us-gaap/2025 | 20240331 | 0 | USD |  | ... |

#### File: `DATA/2025q2/pre.txt`

- **Size:** 89.36 MB
- **Total Rows:** 769,822
- **Total Columns:** 10
- **Category Columns:** adsh, stmt, rfile, version
- **Numeric Columns:** report, line, inpth, negating
- **Text Columns:** tag, plabel

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **adsh** | 1 | `0000002488-25-000047` |
| **stmt** | 5 | `BS`, `CF`, `CI`, `EQ`, `IS` |
| **rfile** | 1 | `H` |
| **version** | 2 | `0000002488-25-000047`, `us-gaap/2025` |

##### Sample Records

| adsh | report | line | stmt | inpth | rfile | tag | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002488-25-000047 | 2 | 1 | IS | 0 | H | RevenueFromContractWithCustomerExclud... | ... |
| 0000002488-25-000047 | 2 | 2 | IS | 0 | H | CostOfGoodsAndServiceExcludingDepreci... | ... |
| 0000002488-25-000047 | 2 | 3 | IS | 0 | H | AmortizationOfAcquisitionRelatedIntan... | ... |

#### File: `DATA/2025q2/sub.txt`

- **Size:** 2.03 MB
- **Total Rows:** 7,009
- **Total Columns:** 36
- **Category Columns:** countryba, countryma, countryinc, stprinc, afs, form, fp
- **Numeric Columns:** cik, sic, zipba, zipma, ein, changed, wksi, fye, period, fy, filed, prevrpt, detail, nciks, aciks
- **Text Columns:** adsh, name, stprba, cityba, bas1, bas2, baph, stprma, cityma, mas1, mas2, former, accepted, instance

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **countryba** | 9 | `CA`, `CN`, `FR`, `GB`, `IE`, `IL`, `PR`, `SG`, `US` |
| **countryma** | 8 | `CA`, `CN`, `FR`, `GB`, `IL`, `PR`, `SG`, `US` |
| **countryinc** | 7 | ``, `CA`, `FR`, `IE`, `KY`, `US`, `VG` |
| **stprinc** | 17 | ``, `DE`, `FL`, `MA`, `MD`, `ME`, `MI`, `MN`, `NJ`, `NV`, `NY`, `ON`, `PA`, `TX`, `VA` ... (and more) |
| **afs** | 4 | ``, `1-LAF`, `2-ACC`, `4-NON` |
| **form** | 8 | `10-K`, `10-K/A`, `10-Q`, `10-Q/A`, `20-F`, `6-K`, `POS AM`, `S-4/A` |
| **fp** | 5 | ``, `FY`, `Q1`, `Q2`, `Q3` |

##### Sample Records

| adsh | cik | name | sic | countryba | stprba | cityba | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000950170-25-071771 | 1965934 | OVERLAND ADVANTAGE |  | US | NY | NEW YORK | ... |
| 0000950170-25-070633 | 2052153 | APOLLO ORIGINATION II (UL) CAPITAL TRUST |  | US | NY | NEW YORK | ... |
| 0000816956-25-000011 | 816956 | CONMED CORP | 3845 | US | FL | LARGO | ... |

#### File: `DATA/2025q2/tag.txt`

- **Size:** 18.00 MB
- **Total Rows:** 89,426
- **Total Columns:** 9
- **Category Columns:** datatype, iord, crdr
- **Numeric Columns:** custom, abstract
- **Text Columns:** tag, version, tlabel, doc

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **datatype** | 2 | `monetary`, `shares` |
| **iord** | 2 | `D`, `I` |
| **crdr** | 3 | ``, `C`, `D` |

##### Sample Records

| tag | version | custom | abstract | datatype | iord | crdr | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OperatingLeaseLiabilityInitialRecogni... | 0000730708-25-000115 | 1 | 0 | monetary | D | C | ... |
| ProceedFromDisposalOfPropertyPlantAnd... | 0001079973-25-000827 | 1 | 0 | monetary | D | D | ... |
| NoncashDistributionsOfDigitalAssetsTo... | 0000950170-25-072818 | 1 | 0 | monetary | D | C | ... |

---

### Quarter: `2025q3`

#### File: `DATA/2025q3/num.txt`

- **Size:** 517.08 MB
- **Total Rows:** 3,720,081
- **Total Columns:** 10
- **Category Columns:** version, uom, coreg
- **Numeric Columns:** ddate, qtrs, value
- **Text Columns:** adsh, tag, segments, footnote

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 17 | `0000732712-25-000086`, `0000789933-25-000041`, `0000950170-25-103884`, `0000950170-25-104004`, `0001006837-25-000104`, `0001131554-25-000083`, `0001213900-25-059827`, `0001375365-25-000027`, `0001437749-25-025734`, `0001558370-25-011408`, `0001640334-25-001439`, `0001731122-25-001057`, `0001860742-25-000018`, `ifrs/2024`, `ifrs/2025` ... (and more) |
| **uom** | 8 | `CAD`, `CNY`, `EUR`, `GBP`, `HKD`, `USD`, `pure`, `shares` |
| **coreg** | 3 | ``, `CubesmartLPAndSubsidiaries`, `PotomacElectricPowerCompany` |

##### Sample Records

| adsh | tag | version | ddate | qtrs | uom | segments | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0001558370-25-010773 | CashAndCashEquivalentsAtCarryingValue | us-gaap/2024 | 20241231 | 0 | USD |  | ... |
| 0001558370-25-011005 | ComprehensiveIncomeNetOfTax | us-gaap/2024 | 20250630 | 2 | USD |  | ... |
| 0001558370-25-010783 | DeferredIncomeTaxExpenseBenefit | us-gaap/2024 | 20250630 | 2 | USD |  | ... |

#### File: `DATA/2025q3/pre.txt`

- **Size:** 84.60 MB
- **Total Rows:** 725,889
- **Total Columns:** 10
- **Category Columns:** adsh, stmt, rfile, version
- **Numeric Columns:** report, line, inpth, negating
- **Text Columns:** tag, plabel

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **adsh** | 1 | `0000002488-25-000108` |
| **stmt** | 4 | `BS`, `CF`, `CI`, `IS` |
| **rfile** | 1 | `H` |
| **version** | 2 | `0000002488-25-000108`, `us-gaap/2025` |

##### Sample Records

| adsh | report | line | stmt | inpth | rfile | tag | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002488-25-000108 | 2 | 1 | IS | 0 | H | RevenueFromContractWithCustomerExclud... | ... |
| 0000002488-25-000108 | 2 | 2 | IS | 0 | H | CostOfGoodsAndServiceExcludingDepreci... | ... |
| 0000002488-25-000108 | 2 | 3 | IS | 0 | H | AmortizationOfAcquisitionRelatedIntan... | ... |

#### File: `DATA/2025q3/sub.txt`

- **Size:** 1.89 MB
- **Total Rows:** 6,541
- **Total Columns:** 36
- **Category Columns:** countryba, countryma, countryinc, afs, form, fp, aciks
- **Numeric Columns:** cik, sic, zipba, zipma, ein, changed, wksi, fye, period, fy, filed, prevrpt, detail, nciks
- **Text Columns:** adsh, name, stprba, cityba, bas1, bas2, baph, stprma, cityma, mas1, mas2, stprinc, former, accepted, instance

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **countryba** | 2 | `CA`, `US` |
| **countryma** | 2 | `CA`, `US` |
| **countryinc** | 3 | ``, `CA`, `US` |
| **afs** | 3 | `1-LAF`, `2-ACC`, `4-NON` |
| **form** | 3 | `10-K`, `10-Q`, `11-K` |
| **fp** | 5 | ``, `FY`, `Q1`, `Q2`, `Q3` |
| **aciks** | 3 | ``, `1806931`, `81027 73986 92487 1702494 50172 1721781 6879` |

##### Sample Records

| adsh | cik | name | sic | countryba | stprba | cityba | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000008947-25-000140 | 8947 | AZZ INC | 3470 | US | TX | FORT WORTH | ... |
| 0000009326-25-000014 | 9326 | BALCHEM CORP | 2800 | US | NJ | MONTVALE | ... |
| 0000010048-25-000025 | 10048 | BARNWELL INDUSTRIES INC | 1311 | US | HI | HONOLULU | ... |

#### File: `DATA/2025q3/tag.txt`

- **Size:** 16.89 MB
- **Total Rows:** 83,782
- **Total Columns:** 9
- **Category Columns:** version, datatype, iord, crdr
- **Numeric Columns:** custom, abstract
- **Text Columns:** tag, tlabel, doc

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 2 | `dei/2024`, `us-gaap/2024` |
| **datatype** | 2 | `monetary`, `pure` |
| **iord** | 2 | `D`, `I` |
| **crdr** | 3 | ``, `C`, `D` |

##### Sample Records

| tag | version | custom | abstract | datatype | iord | crdr | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EntityListingDepositoryReceiptRatio | dei/2024 | 0 | 0 | pure | I |  | ... |
| AcceleratedShareRepurchaseProgramAdju... | us-gaap/2024 | 0 | 0 | monetary | D | C | ... |
| AcceleratedShareRepurchasesAdjustment... | us-gaap/2024 | 0 | 0 | monetary | D | D | ... |

---

### Quarter: `2025q4`

#### File: `DATA/2025q4/num.txt`

- **Size:** 541.28 MB
- **Total Rows:** 3,832,977
- **Total Columns:** 10
- **Category Columns:** adsh, version, uom, segments
- **Numeric Columns:** ddate, qtrs, value
- **Text Columns:** tag, coreg, footnote

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **adsh** | 1 | `0000002488-25-000166` |
| **version** | 2 | `0000002488-25-000166`, `us-gaap/2025` |
| **uom** | 2 | `USD`, `shares` |
| **segments** | 5 | ``, `ClassOfStock=CommonStock;`, `ConsolidationItems=CorporateNonSegment;`, `EquityComponents=AdditionalPaidInCapital;`, `IncomeStatementBalanceSheetAndAdditionalDisclosuresByDisposalGroupsIncludingDiscontinuedOperations=ZTManufacturing;` |

##### Sample Records

| adsh | tag | version | ddate | qtrs | uom | segments | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002488-25-000166 | AccountsPayableCurrent | us-gaap/2025 | 20241231 | 0 | USD |  | ... |
| 0000002488-25-000166 | AccountsPayableCurrent | us-gaap/2025 | 20250930 | 0 | USD |  | ... |
| 0000002488-25-000166 | AccountsReceivableNetCurrent | us-gaap/2025 | 20241231 | 0 | USD |  | ... |

#### File: `DATA/2025q4/pre.txt`

- **Size:** 84.28 MB
- **Total Rows:** 719,346
- **Total Columns:** 10
- **Category Columns:** stmt, rfile, version
- **Numeric Columns:** report, line, inpth, negating
- **Text Columns:** adsh, tag, plabel

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **stmt** | 4 | `BS`, `CF`, `EQ`, `IS` |
| **rfile** | 1 | `H` |
| **version** | 13 | `0001104659-25-104466`, `0001193125-25-269484`, `0001193125-25-278812`, `0001213900-25-102150`, `0001213900-25-111547`, `0001437749-25-033297`, `0001628280-25-049697`, `0001829126-25-009216`, `0001840856-25-000022`, `0001913847-25-000029`, `ifrs/2024`, `us-gaap/2024`, `us-gaap/2025` |

##### Sample Records

| adsh | report | line | stmt | inpth | rfile | tag | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0001562762-25-000269 | 3 | 21 | BS | 1 | H | CommonStockSharesOutstanding | ... |
| 0001443575-25-000051 | 4 | 36 | IS | 0 | H | EarningsPerShareBasic | ... |
| 0001057706-25-000012 | 4 | 26 | IS | 0 | H | FeesAndCommissionsMortgageBankingAndS... | ... |

#### File: `DATA/2025q4/sub.txt`

- **Size:** 1.81 MB
- **Total Rows:** 6,304
- **Total Columns:** 36
- **Category Columns:** countryba, countryma, countryinc, afs, form, fp, aciks
- **Numeric Columns:** cik, sic, zipba, zipma, ein, changed, wksi, fye, period, fy, filed, prevrpt, detail, nciks
- **Text Columns:** adsh, name, stprba, cityba, bas1, bas2, baph, stprma, cityma, mas1, mas2, stprinc, former, accepted, instance

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **countryba** | 2 | `CA`, `US` |
| **countryma** | 2 | `CA`, `US` |
| **countryinc** | 3 | ``, `CA`, `US` |
| **afs** | 3 | `1-LAF`, `2-ACC`, `4-NON` |
| **form** | 2 | `10-K`, `10-Q` |
| **fp** | 4 | `FY`, `Q1`, `Q2`, `Q3` |
| **aciks** | 4 | ``, `1901876`, `4515`, `81027 73986 92487 1702494 50172 1721781 6879` |

##### Sample Records

| adsh | cik | name | sic | countryba | stprba | cityba | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002488-25-000166 | 2488 | ADVANCED MICRO DEVICES INC | 3674 | US | CA | SANTA CLARA | ... |
| 0000002969-25-000055 | 2969 | AIR PRODUCTS & CHEMICALS, INC. | 2810 | US | PA | ALLENTOWN | ... |
| 0000003499-25-000026 | 3499 | ALEXANDERS INC | 6798 | US | NJ | PARAMUS | ... |

#### File: `DATA/2025q4/tag.txt`

- **Size:** 17.11 MB
- **Total Rows:** 84,907
- **Total Columns:** 9
- **Category Columns:** version, datatype, iord, crdr
- **Numeric Columns:** custom, abstract
- **Text Columns:** tag, tlabel, doc

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 1 | `us-gaap/2024` |
| **datatype** | 3 | `monetary`, `perShare`, `shares` |
| **iord** | 2 | `D`, `I` |
| **crdr** | 3 | ``, `C`, `D` |

##### Sample Records

| tag | version | custom | abstract | datatype | iord | crdr | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AccountsPayableAndOtherAccruedLiabili... | us-gaap/2024 | 0 | 0 | monetary | I | C | ... |
| AccountsPayableTradeCurrent | us-gaap/2024 | 0 | 0 | monetary | I | C | ... |
| AccruedIncomeTaxesNoncurrent | us-gaap/2024 | 0 | 0 | monetary | I | C | ... |

---

### Quarter: `2026q1`

#### File: `DATA/2026q1/num.txt`

- **Size:** 533.47 MB
- **Total Rows:** 3,690,955
- **Total Columns:** 10
- **Category Columns:** adsh, version, uom, segments
- **Numeric Columns:** ddate, qtrs, value
- **Text Columns:** tag, coreg, footnote

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **adsh** | 1 | `0000002488-26-000018` |
| **version** | 2 | `0000002488-26-000018`, `us-gaap/2025` |
| **uom** | 2 | `USD`, `shares` |
| **segments** | 16 | ``, `BusinessAcquisition=OtherAcquisitions;`, `BusinessAcquisition=ZTSystems;`, `BusinessSegments=ClientAndGaming;ConsolidationItems=OperatingSegments;`, `BusinessSegments=Datacenter;ConsolidationItems=OperatingSegments;`, `BusinessSegments=Gaming;ProductOrService=Gaming;`, `ClassOfStock=CommonStock;`, `ConsolidationItems=MaterialReconcilingItems;`, `ConsolidationItems=OperatingSegments;`, `EquityComponents=AccumulatedOtherComprehensiveIncome;`, `EquityComponents=AdditionalPaidInCapital;`, `EquityComponents=RetainedEarnings;`, `EquityComponents=TreasuryStockCommon;`, `Geographical=OtherCountries;`, `Geographical=US;` ... (and more) |

##### Sample Records

| adsh | tag | version | ddate | qtrs | uom | segments | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002488-26-000018 | AccumulatedOtherComprehensiveIncomeLo... | us-gaap/2025 | 20241231 | 0 | USD |  | ... |
| 0000002488-26-000018 | AdjustmentForAmortization | us-gaap/2025 | 20251231 | 4 | USD |  | ... |
| 0000002488-26-000018 | AdjustmentsToAdditionalPaidInCapitalW... | us-gaap/2025 | 20241231 | 4 | USD | EquityComponents=AdditionalPaidInCapi... | ... |

#### File: `DATA/2026q1/pre.txt`

- **Size:** 86.37 MB
- **Total Rows:** 733,134
- **Total Columns:** 10
- **Category Columns:** adsh, stmt, rfile, version
- **Numeric Columns:** report, line, inpth, negating
- **Text Columns:** tag, plabel

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **adsh** | 1 | `0000002488-26-000018` |
| **stmt** | 5 | `BS`, `CF`, `CI`, `EQ`, `IS` |
| **rfile** | 1 | `H` |
| **version** | 2 | `0000002488-26-000018`, `us-gaap/2025` |

##### Sample Records

| adsh | report | line | stmt | inpth | rfile | tag | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000002488-26-000018 | 3 | 1 | IS | 0 | H | RevenueFromContractWithCustomerExclud... | ... |
| 0000002488-26-000018 | 3 | 2 | IS | 0 | H | CostOfGoodsAndServiceExcludingDepreci... | ... |
| 0000002488-26-000018 | 3 | 3 | IS | 0 | H | AmortizationOfAcquisitionRelatedIntan... | ... |

#### File: `DATA/2026q1/sub.txt`

- **Size:** 1.77 MB
- **Total Rows:** 6,169
- **Total Columns:** 36
- **Category Columns:** countryba, countryma, countryinc, afs, form, fp
- **Numeric Columns:** cik, sic, zipma, ein, changed, wksi, fye, period, fy, filed, prevrpt, detail, nciks, aciks
- **Text Columns:** adsh, name, stprba, cityba, zipba, bas1, bas2, baph, stprma, cityma, mas1, mas2, stprinc, former, accepted, instance

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **countryba** | 5 | ``, `BM`, `CA`, `GB`, `US` |
| **countryma** | 4 | ``, `CA`, `GB`, `US` |
| **countryinc** | 4 | ``, `GB`, `PA`, `US` |
| **afs** | 4 | ``, `1-LAF`, `2-ACC`, `4-NON` |
| **form** | 6 | `10-K`, `10-K/A`, `10-Q`, `11-K`, `20-F`, `40-F` |
| **fp** | 5 | ``, `FY`, `Q1`, `Q2`, `Q3` |

##### Sample Records

| adsh | cik | name | sic | countryba | stprba | cityba | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0000006955-26-000025 | 6955 | ENERPAC TOOL GROUP CORP | 3590 | US | WI | MILWAUKEE | ... |
| 0000014693-26-000010 | 14693 | BROWN FORMAN CORP | 2080 | US | KY | LOUISVILLE | ... |
| 0000014846-26-000007 | 14846 | BRT APARTMENTS CORP. | 6798 | US | NY | GREAT NECK | ... |

#### File: `DATA/2026q1/tag.txt`

- **Size:** 18.78 MB
- **Total Rows:** 91,794
- **Total Columns:** 9
- **Category Columns:** version, datatype, iord, crdr
- **Numeric Columns:** custom, abstract
- **Text Columns:** tag, tlabel, doc

##### Sample Categorical Details (First 100 rows sample)

| Category Column | Unique Values Count | Samples / Categories |
|---|---|---|
| **version** | 1 | `us-gaap/2024` |
| **datatype** | 2 | `monetary`, `shares` |
| **iord** | 2 | `D`, `I` |
| **crdr** | 3 | ``, `C`, `D` |

##### Sample Records

| tag | version | custom | abstract | datatype | iord | crdr | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AccountsAndNotesReceivableNet | us-gaap/2024 | 0 | 0 | monetary | I | D | ... |
| AccountsAndOtherReceivablesNetCurrent | us-gaap/2024 | 0 | 0 | monetary | I | D | ... |
| AccountsNotesAndLoansReceivableNetCur... | us-gaap/2024 | 0 | 0 | monetary | I | D | ... |

---
