# Deep Research Plan: New Data Sources for TESM Model Enhancement

**Objective:** Discover and acquire new public/free data sources to fill critical gaps in the TESM model, focusing on high-impact, immediately usable datasets.

---

## Phase 1: AI Adoption & Usage Telemetry (Priority: P0)

### Target Data
- Vendor-reported usage metrics (OpenAI, Anthropic, Google, Microsoft, AWS, Meta)
- Third-party adoption estimates (Gartner, IDC, Morgan Stanley CIO Survey, Flexera)
- Alternative data proxies (GitHub, Hugging Face, ArXiv, job postings, web traffic)

### Research Queries
1. "OpenAI ChatGPT MAU DAU subscribers 2024 2025 earnings call transcript"
2. "Anthropic Claude API usage statistics 2024"
3. "Microsoft Copilot seats enterprise adoption 2024"
4. "AWS Bedrock model invocations Trainium Inferentia adoption"
5. "Google Gemini Vertex AI API calls TPU utilization"
6. "Meta Llama downloads Hugging Face 2024"
7. "Morgan Stanley CIO survey AI adoption 2024 2025"
8. "Flexera State of Cloud Report 2024 reserved instances"
9. "GitHub Copilot adoption statistics 2024"
10. "Hugging Face model downloads leaderboard 2024"

### Expected Outputs
- `DATA/adoption/vendor_reported_metrics.csv` - quarterly time series
- `DATA/adoption/third_party_surveys.csv` - survey-based estimates
- `DATA/adoption/alternative_proxies.csv` - GitHub/HF/ArXiv/jobs/web traffic

---

## Phase 2: Chinese AI Ecosystem Data (Priority: P0)

### Target Data
- Model benchmarks (LMSYS Chatbot Arena, OpenCompass, C-Eval, CMMLU, SuperCLUE, FlagEval)
- API pricing for Chinese providers (Zhipu, Baichuan, 01.ai, Moonshot, MiniMax, Alibaba, Tencent, ByteDance)
- Chinese data center costs (land, construction, electricity, water, labor)
- PPP adjustment factors by category

### Research Queries
1. "LMSYS Chatbot Arena Elo ratings Chinese models GLM Qwen Yi DeepSeek 2024"
2. "OpenCompass benchmark results 2024 Chinese LLMs"
3. "Zhipu AI GLM pricing API 2024"
4. "Baichuan AI API pricing 2024"
5. "01.ai Yi series pricing platform.01.ai"
6. "Moonshot Kimi API pricing platform.moonshot.cn"
7. "Alibaba Qwen DashScope pricing 2024"
8. "Tencent Hunyuan API pricing cloud.tencent.com"
9. "ByteDance Doubao API pricing volcengine.com"
10. "China data center construction cost per MW 2024 JLL CBRE"
11. "China industrial electricity price by province 2024"
12. "China engineering salaries Levels.fyi 51job Zhaopin 2024"
13. "World Bank ICP 2021 PPP China expenditure categories"

### Expected Outputs
- `DATA/china/model_benchmarks.csv` - normalized Elo scores over time
- `DATA/china/api_pricing.csv` - quarterly pricing by provider/model
- `DATA/china/dc_costs.csv` - city-tier level cost breakdowns
- `DATA/china/ppp_factors.csv` - category-level PPP adjustments

---

## Phase 3: Productivity Studies Meta-Analysis (Priority: P0)

### Target Data
- Effect sizes from RCTs/quasi-experiments on AI productivity
- Study metadata: sample, task, model, outcome, quality score
- Industry-specific results (coding, writing, support, legal, consulting, R&D)

### Research Queries
1. "Peng et al 2023 GitHub Copilot productivity RCT effect size"
2. "Noy Zhang 2023 Science writing productivity ChatGPT experiment"
3. "Dell'Acqua et al 2023 BCG consultants AI productivity"
4. "Brynjolfsson et al 2023 NBER customer support generative AI"
5. "Cui et al 2024 QJE customer support agents AI"
6. "Kanazawa et al 2023 legal AI productivity"
7. "Agrawal et al 2023 consulting AI productivity"
8. "Wang et al 2023 materials discovery AI"
9. "Liu et al 2024 drug discovery AI productivity"
10. "Eloundou et al 2023 OpenAI occupation exposure"
11. "Felten Raj Seamans 2021 2023 AI exposure scores O*NET"
12. "Acemoglu Restrepo automation labor share 2018 2020"

### Expected Outputs
- `DATA/productivity/meta_analysis_studies.csv` - 50+ studies with effect sizes
- `DATA/productivity/pooled_priors.json` - Bayesian priors by category
- `DATA/productivity/onet_ai_exposure.csv` - occupation-level exposure scores

---

## Phase 4: Cloud Revenue Quality & Contract Mapping (Priority: P0)

### Target Data
- AWS/Azure/GCP pricing pages (historical + current)
- Contract type taxonomy mapping to quality tiers
- 10-K segment notes for revenue recognition policies
- Reserved Instance / Savings Plan / Committed Use Discount utilization rates

### Research Queries
1. "AWS pricing history reserved instances savings plans 2020-2024"
2. "Azure reserved instances savings plans pricing history"
3. "GCP committed use discounts pricing history"
4. "AWS enterprise agreement discount tiers"
5. "Cloud revenue recognition policy 10-K deferred revenue RPO"
6. "Synergy Research cloud market share quarterly 2020-2024"
7. "Flexera State of Cloud reserved vs on-demand utilization 2024"

### Expected Outputs
- `DATA/revenue_quality/cloud_pricing_history.csv` - daily/weekly price points
- `DATA/revenue_quality/contract_taxonomy.csv` - mapping to High/Med/Low quality
- `DATA/revenue_quality/rpo_segment_notes.csv` - extracted from 10-Ks

---

## Phase 5: Macro & Financial Market Data (Priority: P1)

### Target Data
- FRED time series (GDP, CPI, rates, spreads, FX, commodities)
- Equity factors (Fama-French, momentum)
- Sector ETF flows
- Institutional 13F holdings
- Analyst estimates (IBES summaries)

### Research Queries
1. "FRED API key GDP CPI Fed funds 10Y treasury spreads"
2. "Ken French data library factors monthly daily"
3. "ETF flows SMH SOXX IGV BOTZ ARKK 2020-2024"
4. "13F institutional holdings NVDA AMD MSFT GOOGL AMZN META"
5. "Analyst estimates NVIDIA revenue EPS 2024 2025 2026"

### Expected Outputs
- `DATA/macro/fred_core_series.parquet` - monthly/quarterly
- `DATA/macro/ff_factors.parquet` - daily
- `DATA/macro/etf_flows.csv` - daily
- `DATA/macro/analyst_estimates.csv` - quarterly

---

## Phase 6: Semiconductor Supply Chain Physical Data (Priority: P1)

### Target Data
- Wafer starts by node (TSMC, Samsung, Intel)
- CoWoS/advanced packaging capacity
- HBM production and allocation
- GPU shipments by SKU
- Data center build trackers
- ODM build slots

### Research Queries
1. "TSMC wafer starts 4nm 3nm quarterly 2023 2024"
2. "CoWoS capacity TSMC ASE Amkor 2024"
3. "HBM3 HBM3E production SK Hynix Samsung Micron 2024"
4. "NVIDIA H100 H200 B100 B200 shipments quarterly 2023 2024"
5. "AMD MI300 MI325 shipments quarterly"
6. "Data center construction tracker DC Byte Structure Research 2024"
7. "ODM server build slots Quanta Wiwynn Inventec Foxconn Supermicro"

### Expected Outputs
- `DATA/semiconductor/wafer_starts.csv` - quarterly by node/foundry
- `DATA/semiconductor/packaging_capacity.csv` - quarterly
- `DATA/semiconductor/hbm_production.csv` - quarterly
- `DATA/semiconductor/gpu_shipments.csv` - quarterly by SKU
- `DATA/semiconductor/dc_build_tracker.csv` - quarterly

---

## Phase 7: Enterprise AI Agent Deployment Data (Priority: P1)

### Target Data
- Verified agent counts from earnings calls/investor days
- Task automation metrics (tickets resolved, code committed, emails drafted)
- ROI/TCO case studies from vendors and enterprises

### Research Queries
1. "Google 1302 AI agents earnings call 2024"
2. "Salesforce 20000 AI agents Dreamforce 2024"
3. "ServiceNow AI agents Now Assist deployment 2024"
4. "Intercom Fin AI agent resolution rate 2024"
5. "Sierra AI agent case study 2024"
6. "Ada customer service AI automation rate 2024"
7. "GitHub Copilot enterprise seats adoption 2024"
8. "Amazon Q Developer enterprise adoption 2024"

### Expected Outputs
- `DATA/agents/deployment_counts.csv` - verified counts by company/date
- `DATA/agents/automation_metrics.csv` - task-level automation rates
- `DATA/agents/roi_case_studies.csv` - TCO/ROI from vendor/enterprise sources

---

## Phase 8: Regulatory Scenario Database (Priority: P1)

### Target Data
- Jurisdiction × regulation matrix with status, requirements, compliance costs
- Export control entity lists (BIS, MOFCOM)
- Enforcement actions and fines

### Research Queries
1. "EU AI Act conformity assessment cost estimates 2024"
2. "NIST AI RMF implementation cost 2024"
3. "China Interim Measures GenAI filing requirements 2024"
4. "BIS Entity List AI companies 2024"
5. "US export controls 3A090 4A090 5A002 5D002 AI chips 2024"
6. "GDPR Article 22 automated decision fines 2024"
7. "UK AI regulation white paper consultation response 2024"

### Expected Outputs
- `DATA/regulatory/jurisdiction_rule_matrix.csv` - structured schema
- `DATA/regulatory/export_controls.csv` - entity lists with ECCN mapping
- `DATA/regulatory/enforcement_actions.csv` - fines, dates, companies

---

## Phase 9: Labor Market Transformation Data (Priority: P1)

### Target Data
- O*NET 28.0 task descriptors × AI exposure scores
- Displaced worker survey outcomes
- JOLTS/QCEW by AI-exposed industries
- Reskilling program outcomes (WIOA, Coursera, edX, Guild)

### Research Queries
1. "O*NET 28.0 download CSV tasks skills knowledge"
2. "Felten Raj Seamans AI exposure scores replication 2023"
3. "BLS CPS displaced worker supplement 2024"
4. "JOLTS job openings information technology 2020-2024"
5. "WIOA training outcomes 2023 2024"
6. "Coursera enterprise AI course completion rates 2024"
7. "Lightcast AI job postings growth 2020-2024"

### Expected Outputs
- `DATA/labor/onet_ai_exposure.csv` - occupation × exposure score
- `DATA/labor/displaced_worker_outcomes.csv` - reemployment, wage change
- `DATA/labor/jolts_ai_industries.csv` - monthly
- `DATA/labor/reskilling_outcomes.csv` - program-level

---

## Phase 10: Unit Economics Data (Priority: P1)

### Target Data
- Per-model training costs (GPT-4, Claude 3, Llama 3, Gemini 1.5)
- Per-API-call inference costs by model, context length, batch
- Per-GPU hourly economics (cloud vs on-prem, utilization breakeven)
- SaaS benchmarks (CAC, LTV, churn, gross margin by ARR scale)

### Research Queries
1. "GPT-4 training cost estimate 2024 SemiAnalysis Epoch AI"
2. "Claude 3 Opus Sonnet Haiku training compute 2024"
3. "Llama 3 405B training compute FLOPs 2024"
4. "AI inference cost per token H100 A100 2024"
5. "Lambda Labs RunPod CoreWeave H100 hourly pricing 2024"
6. "SaaS Capital KeyBanc ICONIQ benchmarks 2024 CAC LTV churn"
7. "Bessemer Cloud Index unit economics 2024"

### Expected Outputs
- `DATA/unit_economics/training_costs.csv` - model × compute × cost
- `DATA/unit_economics/inference_costs.csv` - model × context × batch × cost
- `DATA/unit_economics/gpu_economics.csv` - provider × GPU × utilization × breakeven
- `DATA/unit_economics/saas_benchmarks.csv` - ARR band × metrics

---

## Execution Strategy

### Week 1-2: Parallel Search & Discovery
- Run all research queries via websearch
- Catalog findings in `RESEARCH_FINDINGS.md` with source URLs, access method, data format
- Prioritize: downloadable CSV/JSON/API > scrapeable HTML > PDF tables > paywalled

### Week 3-4: Acquisition & Structuring
- Download/acquire top-priority datasets
- Normalize schemas, create parquet/CSV files in `DATA/` subdirectories
- Document provenance in `DATA_MANIFEST.json`

### Week 5-6: Integration
- Extend `calibrate.py` with new ingestion modules
- Add new parameters to `DEFAULT_PARAMS` in `engine.js`
- Re-run calibration → new `param_overrides.js`
- Validate against historical backtests

---

## Success Criteria

| Metric | Target |
|--------|--------|
| New data categories added | ≥ 8 of 10 phases |
| Datasets with quarterly time series | ≥ 15 |
| Parameters calibrated from new data | ≥ 20 |
| Backtest RMSE improvement | > 10% on at least 1 episode |
| Reproducibility | All sources documented with access date, method, license |