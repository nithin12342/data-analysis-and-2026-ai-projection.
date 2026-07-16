# Free Data Source Guide for 54 Missing TESM Tables

**Purpose:** where to source each missing table for the AI TESM / AI-vs-dot-com model, using free or public sources wherever possible.

**Important rule:** every sourced or estimated record should include provenance columns:

```text
source, source_url, confidence, estimation_method, notes, date_collected
```

Suggested confidence scale:

```text
1.00 = official filing / exchange / government
0.90 = company IR / audited report
0.80 = government or exchange-like public dataset
0.70 = reputable public market source
0.60 = reputable media / public analyst estimate
0.50 = multiple public reports but no primary filing
0.40 = model-derived proxy
0.30 = weak proxy
```

---

## P0 — Highest Priority Tables

### 1. `company_security_master`

**Purpose:** map companies across SEC, ticker, sector, model sector, and AI ecosystem role.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| SEC company tickers JSON | https://www.sec.gov/files/company_tickers.json | CIK, ticker, title |
| SEC submissions API | https://data.sec.gov/submissions/CIK0000320193.json | legal name, SIC, forms, fiscal year end |
| SEC EDGAR search | https://www.sec.gov/edgar/search/ | company filing lookup |
| Nasdaq symbol directory | https://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs | listed tickers |
| NYSE listed companies | https://www.nyse.com/listings_directory/stock | listed tickers |
| OpenFIGI API | https://www.openfigi.com/api | FIGI/identifier mapping, free with limits |

**Collection method:**

1. Start with your SEC companies from `sec_company_quarterly_derived`.
2. Join SEC CIKs to `company_tickers.json`.
3. Add manual `model_sector` and `ai_ecosystem_role` classifications.
4. Add exchange from Nasdaq/NYSE where available.

---

### 2. `equity_prices_daily`

**Purpose:** daily prices for valuation, drawdowns, sector comparisons.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Stooq CSV | https://stooq.com/q/d/l/?s=nvda.us&i=d | free daily OHLCV CSV |
| Yahoo Finance chart endpoint, unofficial | https://query1.finance.yahoo.com/v8/finance/chart/NVDA?period1=0&period2=9999999999&interval=1d | daily prices, unofficial |
| Nasdaq historical data pages | https://www.nasdaq.com/market-activity/stocks/nvda/historical | manual spot checks |

**Collection method:**

Use Stooq for all listed stocks if available:

```text
https://stooq.com/q/d/l/?s={ticker_lower}.us&i=d
```

Example:

```text
https://stooq.com/q/d/l/?s=msft.us&i=d
https://stooq.com/q/d/l/?s=nvda.us&i=d
```

---

### 3. `shares_outstanding_quarterly`

**Purpose:** compute market cap.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| SEC CompanyFacts API | https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json | `EntityCommonStockSharesOutstanding`, weighted shares |
| SEC DERA financial statement data | https://www.sec.gov/dera/data/financial-statement-data-sets | XBRL bulk facts |
| SEC 10-Q / 10-K cover page | https://www.sec.gov/edgar/search/ | common shares outstanding |

**SEC tags to try:**

```text
EntityCommonStockSharesOutstanding
WeightedAverageNumberOfSharesOutstandingBasic
WeightedAverageNumberOfDilutedSharesOutstanding
WeightedAverageNumberOfSharesOutstandingDiluted
```

---

### 4. `market_cap_quarterly`

**Purpose:** quarterly market capitalization aligned with SEC financials.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Stooq | https://stooq.com/q/d/l/?s=nvda.us&i=d | quarter-end close price |
| SEC CompanyFacts | https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json | shares outstanding |
| SEC company tickers JSON | https://www.sec.gov/files/company_tickers.json | ticker-CIK map |

**Formula:**

```text
market_cap_usd = quarter_end_adjusted_close × shares_outstanding
```

---

### 5. `enterprise_value_quarterly`

**Purpose:** enterprise value for multiples.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Your DuckDB SEC tables | local `all_company_quarterly` | cash, debt |
| SEC CompanyFacts | https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json | cash, debt, minority interest if needed |
| SEC filings | https://www.sec.gov/edgar/search/ | preferred equity / minority interest if needed |

**Formula:**

```text
enterprise_value = market_cap + total_debt + preferred_equity + minority_interest - cash_and_investments
```

Use your existing fields:

```text
total_debt, cash_and_investments
```

---

### 6. `valuation_multiples_quarterly`

**Purpose:** valuation, bubble score, endpoint classifier.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Your DuckDB SEC tables | local | revenue, EBIT proxy, OCF, CapEx, FCF |
| `market_cap_quarterly` | derived | market cap |
| `enterprise_value_quarterly` | derived | EV |
| Stooq/Yahoo price data | https://stooq.com/q/d/l/?s=nvda.us&i=d | price history |

**Metrics to compute:**

```text
price_to_sales = market_cap / revenue_ttm
ev_to_revenue = enterprise_value / revenue_ttm
ev_to_ebit = enterprise_value / ebit_ttm
fcf_yield = fcf_ttm / market_cap
earnings_yield = net_income_ttm / market_cap
```

---

### 7. `company_segments_quarterly`

**Purpose:** separate AI/cloud/data-center/semiconductor segment revenue.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| SEC CompanyFacts | https://data.sec.gov/api/xbrl/companyfacts/CIK0001018724.json | segment tags when available |
| SEC 10-K / 10-Q HTML | https://www.sec.gov/edgar/search/ | segment notes and tables |
| Amazon IR | https://ir.aboutamazon.com/ | AWS revenue |
| Microsoft IR | https://www.microsoft.com/en-us/investor | Intelligent Cloud / Azure commentary |
| Alphabet IR | https://abc.xyz/investor/ | Google Cloud revenue |
| NVIDIA IR | https://investor.nvidia.com/ | Data Center revenue |
| AMD IR | https://ir.amd.com/ | Data Center revenue |
| Oracle IR | https://investor.oracle.com/ | Cloud revenue |

**Collection method:**

1. Pull SEC `segment_revenue` facts where possible.
2. Parse 10-K/10-Q segment tables manually or with BeautifulSoup.
3. Normalize segment names to `cloud`, `semiconductor_data_center`, `enterprise_software`, `advertising`, etc.

---

### 8. `cloud_ai_revenue_split_estimated`

**Purpose:** estimate AI-specific cloud revenue.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Microsoft Investor Relations | https://www.microsoft.com/en-us/investor | Azure AI commentary |
| Amazon IR | https://ir.aboutamazon.com/ | AWS AI/Bedrock/Trainium commentary |
| Alphabet IR | https://abc.xyz/investor/ | Google Cloud AI commentary |
| Oracle IR | https://investor.oracle.com/ | OCI AI deals / RPO |
| Meta IR | https://investor.fb.com/ | CapEx / AI infra comments |
| SEC filings | https://www.sec.gov/edgar/search/ | official segment revenue, RPO |
| NVIDIA IR | https://investor.nvidia.com/ | customer / demand commentary proxy |

**Free proxy methods:**

```text
1. Management commentary: AI contribution to cloud growth.
2. GPU capacity proxy: GPU_count × utilization × GPU_hour_price.
3. CapEx attribution proxy: AI_capex × required_revenue_yield.
4. RPO proxy: AI deal backlog / total cloud RPO.
```

---

### 9. `vendor_token_usage_proxy`

**Purpose:** estimate actual token demand, since true token data is usually private.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Vendor reported metrics table | local `vendor_reported_metrics` | users, usage disclosures |
| OpenRouter rankings | https://openrouter.ai/rankings | model usage proxy |
| OpenRouter models API | https://openrouter.ai/api/v1/models | model prices/context windows |
| Hugging Face API | https://huggingface.co/api/models | open model adoption proxy |
| Google Trends | https://trends.google.com/trends/ | demand/search interest proxy |
| Similarweb free pages | https://www.similarweb.com/ | traffic snippets, limited free |
| Company blogs | https://openai.com/news/ | user and product disclosures |

**Proxy methods:**

```text
estimated_tokens = estimated_API_revenue / blended_price_per_token
estimated_tokens = MAU × prompts_per_user_per_month × tokens_per_prompt
estimated_tokens = deployed_GPU_count × utilization × tokens_per_gpu_hour
```

---

### 10. `token_usage_by_workload_proxy`

**Purpose:** split token demand into chat, coding, agents, search, document, etc.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Vendor blogs | https://openai.com/news/ | workload announcements |
| GitHub Copilot blog | https://github.blog/ | coding usage proxy |
| Microsoft customer stories | https://customers.microsoft.com/ | enterprise workload proxies |
| Salesforce customer stories | https://www.salesforce.com/customer-success-stories/ | agent/customer service use cases |
| OpenRouter categories | https://openrouter.ai/rankings | model usage mix proxy |
| Hugging Face task tags | https://huggingface.co/models | model task categories |

**Collection method:**

Tag each vendor/model by workload and estimate usage shares from public product mix.

---

### 11. `private_ai_company_financials_estimated`

**Purpose:** private AI revenue, burn, customers, employees.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| OpenAI news | https://openai.com/news/ | company disclosures |
| Anthropic news | https://www.anthropic.com/news | company disclosures |
| Mistral news | https://mistral.ai/news/ | company disclosures |
| xAI news | https://x.ai/news | company disclosures |
| Hugging Face blog | https://huggingface.co/blog | company/product disclosures |
| Reuters AI news | https://www.reuters.com/technology/artificial-intelligence/ | valuation/revenue reports |
| TechCrunch AI | https://techcrunch.com/category/artificial-intelligence/ | funding/revenue reports |
| Crunchbase free pages | https://www.crunchbase.com/ | funding snippets, limited free |
| SEC filings of investors | https://www.sec.gov/edgar/search/ | Microsoft/OpenAI, Amazon/Anthropic disclosures |

**Collection method:** store each metric as one row: `company, date, metric, value, source, confidence`.

---

### 12. `private_ai_valuation_rounds`

**Purpose:** private valuation history.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Crunchbase free pages | https://www.crunchbase.com/ | funding-round snippets |
| TechCrunch | https://techcrunch.com/ | funding announcements |
| Reuters | https://www.reuters.com/technology/artificial-intelligence/ | large rounds |
| Company press releases | company IR/blog pages | official funding announcements |
| SEC filings of strategic investors | https://www.sec.gov/edgar/search/ | investment disclosures |

**Note:** PitchBook/Forge/Caplight are better but not free. Use public triangulation and confidence scoring.

---

### 13. `private_ai_usage_estimates`

**Purpose:** private AI users, API customers, web/app traffic, token estimates.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Similarweb free pages | https://www.similarweb.com/ | website traffic snippets |
| Google Trends | https://trends.google.com/trends/ | attention proxy |
| App Store public pages | https://www.apple.com/app-store/ | app ranking/manual |
| Google Play public pages | https://play.google.com/store/apps | app ranking/manual |
| OpenRouter rankings | https://openrouter.ai/rankings | API/model usage proxy |
| Company blogs | OpenAI/Anthropic/Mistral/xAI sites | disclosed usage counts |

---

### 14. `ai_ipo_database`

**Purpose:** current AI IPO quality.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| SEC EDGAR S-1/F-1 | https://www.sec.gov/edgar/search/ | IPO prospectuses |
| SEC submissions API | https://data.sec.gov/submissions/CIK0001045810.json | find S-1/F-1 filings |
| Nasdaq IPO calendar | https://www.nasdaq.com/market-activity/ipos | IPO dates/prices |
| NYSE IPO Center | https://www.nyse.com/ipo-center | IPO details |
| Renaissance Capital free IPO pages | https://www.renaissancecapital.com/IPO-Center | IPO summaries, limited free |

**Collection method:** parse S-1 financial statements and prospectus sections.

---

### 15. `dotcom_ipo_database`

**Purpose:** dot-com IPO benchmark.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Jay Ritter IPO data | https://site.warrington.ufl.edu/ritter/ipo-data/ | IPO returns/proceeds datasets |
| SEC historical EDGAR | https://www.sec.gov/Archives/edgar/ | old S-1 filings |
| SEC EDGAR search | https://www.sec.gov/edgar/search/ | historical filing lookup |
| Internet Archive | https://web.archive.org/ | old company pages / reports |
| Wikipedia dot-com bubble lists | https://en.wikipedia.org/wiki/Dot-com_bubble | initial company list only, low confidence |

**Note:** use Jay Ritter as the starting point; use SEC filings to add revenue/profitability.

---

### 16. `dotcom_company_financials_proxy`

**Purpose:** dot-com company financials.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| SEC historical EDGAR archives | https://www.sec.gov/Archives/edgar/ | 10-K, 10-Q, S-1 |
| SEC EDGAR search | https://www.sec.gov/edgar/search/ | filing lookup |
| Internet Archive | https://web.archive.org/ | old annual reports / investor pages |
| Company successor IR pages | e.g. Amazon, eBay, Booking | survivors' old annual reports |

**Collection method:** start with 25–50 representative dot-com firms and manually/semiautomatically parse filings.

---

### 17. `dotcom_drawdown_summary`

**Purpose:** crash/drawdown calibration.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Stooq | https://stooq.com/q/d/l/?s=amzn.us&i=d | survivor price histories |
| Yahoo Finance, unofficial | https://query1.finance.yahoo.com/v8/finance/chart/AMZN?period1=0&period2=9999999999&interval=1d | survivor price histories |
| SEC filings | https://www.sec.gov/edgar/search/ | bankruptcy/delisting/acquisition clues |
| Internet Archive | https://web.archive.org/ | delisted firms and old investor data |
| Wikipedia pages | https://en.wikipedia.org/ | low-confidence outcome dates, verify elsewhere |

**Note:** delisted stock histories are not fully free. Use proxy peak/trough/outcome where daily data is unavailable.

---

### 18. `dotcom_survival_outcomes`

**Purpose:** survival/bankruptcy/acquisition outcomes.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| SEC filings | https://www.sec.gov/edgar/search/ | 8-K, merger, bankruptcy disclosures |
| Internet Archive | https://web.archive.org/ | old company status |
| Wikipedia | https://en.wikipedia.org/ | initial outcome list, verify |
| BankruptcyData free snippets | https://www.bankruptcydata.com/ | limited free, manual checks |
| CourtListener | https://www.courtlistener.com/ | legal/bankruptcy case references |

---

### 19. `cloud_rpo_maturity_schedule`

**Purpose:** contract cliff from RPO maturity.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| SEC 10-K / 10-Q | https://www.sec.gov/edgar/search/ | RPO maturity tables |
| Microsoft IR | https://www.microsoft.com/en-us/investor | RPO / cloud commitments |
| Salesforce IR | https://investor.salesforce.com/ | RPO / deferred revenue |
| ServiceNow IR | https://www.servicenow.com/company/investor-relations.html | RPO |
| Oracle IR | https://investor.oracle.com/ | RPO / cloud backlog |
| Alphabet IR | https://abc.xyz/investor/ | Google Cloud disclosures |
| Amazon IR | https://ir.aboutamazon.com/ | AWS disclosures |

**Collection method:** parse ASC 606 RPO tables and deferred revenue maturity disclosures.

---

### 20. `enterprise_contract_maturity_proxy`

**Purpose:** estimate contract renewals by quarter/year.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| AWS Reserved Instances | https://aws.amazon.com/ec2/pricing/reserved-instances/ | 1/3-year terms |
| AWS Savings Plans | https://aws.amazon.com/savingsplans/ | commitment terms |
| AWS Capacity Blocks | https://aws.amazon.com/ec2/capacityblocks/ | GPU reservation terms |
| Azure Reservations | https://azure.microsoft.com/en-us/pricing/reservations/ | reservation terms |
| Azure Savings Plan | https://azure.microsoft.com/en-us/pricing/offers/savings-plan-compute/ | commitment terms |
| GCP Committed Use Discounts | https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts | 1/3-year terms |
| Oracle Universal Credits | https://www.oracle.com/cloud/universal-credits/ | commitment structures |
| SEC RPO disclosures | https://www.sec.gov/edgar/search/ | maturity buckets |

---

### 21. `gpu_reservation_expiration_proxy`

**Purpose:** GPU capacity reservation expiry and downsizing risk.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| AWS Capacity Blocks | https://aws.amazon.com/ec2/capacityblocks/ | capacity-block terms |
| CoreWeave news | https://www.coreweave.com/newsroom | public AI capacity deals |
| Lambda Cloud pricing | https://lambdalabs.com/service/gpu-cloud | GPU pricing / reservations |
| RunPod pricing | https://www.runpod.io/pricing | GPU rental pricing |
| Oracle Cloud GPU | https://www.oracle.com/cloud/compute/gpu/ | GPU cloud offerings |
| Company 8-K / 10-Q filings | https://www.sec.gov/edgar/search/ | large capacity contracts if disclosed |

**Note:** actual customer-level expiry is private; use proxy estimates and confidence scores.

---

### 22. `macro_timeseries_fred`

**Purpose:** full macro history.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| FRED CSV pattern | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10 | no API key needed for CSV |
| FRED API docs | https://fred.stlouisfed.org/docs/api/fred/ | structured API |
| FRED main | https://fred.stlouisfed.org/ | search series |

**CSV pattern:**

```text
https://fred.stlouisfed.org/graph/fredgraph.csv?id=SERIES_ID
```

Examples:

```text
https://fred.stlouisfed.org/graph/fredgraph.csv?id=FEDFUNDS
https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10
https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y
https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2
```

---

### 23. `monte_carlo_distributions`

**Purpose:** replace hardcoded Monte Carlo assumptions.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Your DuckDB historical tables | local | empirical distributions |
| FRED macro time series | https://fred.stlouisfed.org/ | macro distributions |
| Historical backtest table | local `historical_backtest` | endpoint/drawdown priors |
| Stress scenarios table | local `stress_scenarios` | shock magnitudes |
| Public studies / module tables | local module tables | productivity/TCO/elasticity priors |

**Collection method:** derive distributions from your existing and newly collected time series; store p05/p50/p95 and distribution type.

---

### 24. `monte_carlo_correlation_matrix`

**Purpose:** correlated shocks instead of independent draws.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| FRED time series | https://fred.stlouisfed.org/ | macro correlations |
| Equity prices from Stooq | https://stooq.com/ | stock/sector correlations |
| Commodity prices from FRED/EIA | https://fred.stlouisfed.org/ | gas/oil/commodity correlations |
| Your stress scenarios | local | expert/assumption correlations |

**Collection method:** compute correlations from historical returns/changes; use expert priors only where no data exists.

---

### 25. `endpoint_calibration_company_level`

**Purpose:** calibrate crash/stagnation/boom labels.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| SEC historical filings | https://www.sec.gov/Archives/edgar/ | company financials |
| Jay Ritter IPO data | https://site.warrington.ufl.edu/ritter/ipo-data/ | IPO cohorts |
| Stooq prices | https://stooq.com/ | survivor price history |
| Internet Archive | https://web.archive.org/ | failed company documents |
| FRED / public indices | https://fred.stlouisfed.org/ | macro context |

---

### 26. `endpoint_calibration_sector_level`

**Purpose:** sector-level endpoint history.

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Stooq index/ETF prices | https://stooq.com/ | sector index history where available |
| FRED NASDAQ / S&P series | https://fred.stlouisfed.org/ | broad market history |
| Kenneth French data library | https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html | factor/industry portfolios |
| Jay Ritter IPO data | https://site.warrington.ufl.edu/ritter/ipo-data/ | IPO-cycle context |
| SIA semiconductor statistics | https://www.semiconductors.org/ | semiconductor cycle context |

---

## P1 — Important Enrichment Tables

### 27. `analyst_estimates_quarterly`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Nasdaq earnings forecast pages | https://www.nasdaq.com/market-activity/stocks/nvda/earnings | EPS estimates, limited |
| Yahoo Finance analysis pages, unofficial scrape | https://finance.yahoo.com/quote/NVDA/analysis | estimates, unofficial |
| Company guidance in earnings releases | company IR pages | official guidance |
| SEC 8-K earnings releases | https://www.sec.gov/edgar/search/ | official guidance exhibits |

**Note:** FactSet/IBES/Refinitiv are better but not free. Use guidance + free estimate pages with lower confidence.

---

### 28. `market_indices_daily`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Stooq | https://stooq.com/ | index/ETF daily history |
| FRED | https://fred.stlouisfed.org/ | some index and market series |
| Nasdaq | https://www.nasdaq.com/market-activity/index/comp | index levels |

Examples via Stooq often use symbols like:

```text
^ndq, ^spx, qqq.us, spy.us, smh.us, soxx.us
```

Verify each symbol manually.

---

### 29. `sector_etf_prices_daily`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Stooq ETF CSV | https://stooq.com/q/d/l/?s=smh.us&i=d | ETF daily prices |
| Yahoo Finance ETF pages, unofficial | https://finance.yahoo.com/quote/SMH/history | ETF prices |
| ETF issuer pages | iShares/SPDR/Invesco/Vanguard | price/NAV checks |

ETF candidates:

```text
SPY, QQQ, XLK, SMH, SOXX, IGV, SKYY, CLOU, BOTZ, XLU, VNQ, SRVR, ARKK
```

---

### 30. `sector_etf_holdings`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| iShares ETFs | https://www.ishares.com/us/products/239705/ishares-semiconductor-etf | SOXX holdings CSV |
| VanEck SMH | https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/holdings/ | SMH holdings |
| State Street SPDR | https://www.ssga.com/us/en/intermediary/etfs | SPDR holdings |
| Invesco QQQ | https://www.invesco.com/qqq-etf/en/about.html | QQQ holdings |
| Vanguard ETFs | https://investor.vanguard.com/investment-products/etfs | Vanguard holdings |

---

### 31. `institutional_ownership_13f`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| SEC EDGAR 13F search | https://www.sec.gov/edgar/search/ | official 13F filings |
| SEC daily/full index | https://www.sec.gov/Archives/edgar/full-index/ | bulk filing discovery |
| SEC 13F FAQ | https://www.sec.gov/divisions/investment/13ffaq | filing context |

**Method:** download `13F-HR` information tables from major managers and parse XML/TXT.

---

### 32. `short_interest`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| FINRA short interest | https://www.finra.org/finra-data/browse-catalog/equity-short-interest | official short-interest data |
| Nasdaq short interest pages | https://www.nasdaq.com/market-activity/stocks/nvda/short-interest | ticker-level page |
| NYSE short interest | https://www.nyse.com/market-data/reference/nyse-group-short-interest | NYSE data/reference |

---

### 33. `options_volume_summary`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Cboe options statistics | https://www.cboe.com/us/options/market_statistics/ | aggregate options stats |
| OCC volume/open interest reports | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest | volume/open interest |
| Yahoo option chains, unofficial | https://finance.yahoo.com/quote/NVDA/options | ticker options chain |
| Nasdaq option chain pages | https://www.nasdaq.com/market-activity/stocks/nvda/option-chain | ticker options chain |

---

### 34. `margin_debt_market_sentiment`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| FINRA margin statistics | https://www.finra.org/rules-guidance/key-topics/margin-accounts/margin-statistics | margin debt |
| FRED margin-related series | https://fred.stlouisfed.org/ | search margin debt / financial conditions |

---

### 35. `open_source_model_registry`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Hugging Face model API | https://huggingface.co/api/models | model list/metadata |
| Hugging Face docs | https://huggingface.co/docs/hub/api | API reference |
| GitHub API | https://docs.github.com/en/rest | repo metadata |
| Papers With Code | https://paperswithcode.com/ | benchmarks/tasks |
| LMArena leaderboard | https://lmarena.ai/leaderboard | model quality ranking |
| OpenCompass leaderboard | https://opencompass.org.cn/leaderboard-llm | Chinese/global benchmark data |

---

### 36. `huggingface_model_downloads`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Hugging Face API | https://huggingface.co/api/models | downloads, likes, model metadata |
| Hugging Face Hub docs | https://huggingface.co/docs/hub/api | API documentation |

Example endpoint:

```text
https://huggingface.co/api/models/{repo_id}
```

---

### 37. `github_model_activity`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| GitHub REST API | https://docs.github.com/en/rest | stars, forks, issues, contributors |
| GitHub search | https://github.com/search | manual repo discovery |
| GH Archive | https://www.gharchive.org/ | large-scale public GitHub event archive |

---

### 38. `ai_efficiency_timeseries`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Artificial Analysis | https://artificialanalysis.ai/ | pricing, latency, quality data, some free |
| OpenRouter model data | https://openrouter.ai/api/v1/models | pricing/context metadata |
| OpenAI pricing | https://platform.openai.com/docs/pricing | API price changes |
| Anthropic pricing | https://docs.anthropic.com/en/docs/about-claude/pricing | API prices |
| Google AI pricing | https://ai.google.dev/pricing | API prices |
| vLLM project | https://github.com/vllm-project/vllm | serving benchmarks / releases |
| NVIDIA inference performance | https://developer.nvidia.com/deep-learning-performance-training-inference/ai-inference | hardware performance notes |

---

### 39. `model_routing_mix`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| OpenRouter rankings | https://openrouter.ai/rankings | model popularity proxy |
| OpenRouter models API | https://openrouter.ai/api/v1/models | model metadata |
| Hugging Face API | https://huggingface.co/api/models | open model popularity proxy |
| Provider blogs | OpenAI/Anthropic/Google/Mistral blogs | model mix announcements |

---

### 40. `inference_request_volume_proxy`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Vendor usage disclosures | company blogs / earnings calls | direct/indirect request volume |
| OpenRouter rankings | https://openrouter.ai/rankings | API usage proxy |
| Similarweb | https://www.similarweb.com/ | web traffic proxy |
| Google Trends | https://trends.google.com/trends/ | demand proxy |
| App Store / Google Play pages | https://play.google.com/store/apps | app demand proxy |

---

### 41. `training_runs_by_company`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Epoch AI model database | https://epoch.ai/data/ai-models | notable model compute/training data |
| Stanford AI Index | https://aiindex.stanford.edu/report/ | model/training trend context |
| Model technical reports | provider blogs/arXiv | training tokens, GPUs, compute |
| arXiv API | https://info.arxiv.org/help/api/index.html | model paper discovery |
| NVIDIA technical blogs | https://developer.nvidia.com/blog | training hardware benchmarks |

---

### 42. `agentic_tco_case_studies`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Microsoft customer stories | https://customers.microsoft.com/ | Copilot case studies |
| Salesforce customer stories | https://www.salesforce.com/customer-success-stories/ | Agentforce cases |
| ServiceNow customers | https://www.servicenow.com/customers.html | Now Assist cases |
| Intercom customers | https://www.intercom.com/customers | Fin bot cases |
| Ada customers | https://www.ada.cx/customers/ | AI support cases |
| Deloitte insights | https://www.deloitte.com/global/en/insights.html | AI enterprise reports |
| McKinsey AI insights | https://www.mckinsey.com/capabilities/quantumblack/our-insights | AI productivity reports |

---

### 43. `workflow_integration_case_studies`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Microsoft customer stories | https://customers.microsoft.com/ | workflow integration examples |
| Salesforce customer stories | https://www.salesforce.com/customer-success-stories/ | sales/support workflow cases |
| ServiceNow customers | https://www.servicenow.com/customers.html | ITSM/enterprise workflow cases |
| GitHub Copilot customer stories | https://github.blog/tag/github-copilot/ | software workflow data |
| Google Cloud customer stories | https://cloud.google.com/customers | Gemini/Vertex AI cases |

---

### 44. `agent_incident_database`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| AI Incident Database | https://incidentdatabase.ai/ | AI incidents |
| OECD AI Incidents Monitor | https://oecd.ai/en/incidents | AI incident tracking |
| NIST AI RMF | https://www.nist.gov/itl/ai-risk-management-framework | risk taxonomy |
| CourtListener | https://www.courtlistener.com/ | lawsuits / legal incidents |
| FTC enforcement actions | https://www.ftc.gov/legal-library/browse/cases-proceedings | AI/consumer enforcement |

---

### 45. `gpu_order_book_proxy`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| NVIDIA Investor Relations | https://investor.nvidia.com/ | shipment/backlog commentary |
| AMD Investor Relations | https://ir.amd.com/ | MI300 / data-center commentary |
| Supermicro IR | https://ir.supermicro.com/ | server order/backlog proxy |
| Dell IR | https://investors.delltechnologies.com/ | AI server backlog |
| HPE IR | https://investors.hpe.com/ | AI systems backlog |
| CoreWeave newsroom | https://www.coreweave.com/newsroom | capacity deals |
| SEC filings | https://www.sec.gov/edgar/search/ | purchase obligations / customer deals |

---

### 46. `wafer_hbm_allocation_proxy`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| TSMC Investor Relations | https://investor.tsmc.com/ | capacity, CoWoS commentary |
| SK hynix IR | https://www.skhynix.com/eng/ir/irData.do | HBM commentary |
| Micron IR | https://investors.micron.com/ | HBM commentary |
| Samsung IR | https://www.samsung.com/global/ir/ | memory/HBM commentary |
| TrendForce press center | https://www.trendforce.com/presscenter | free supply-chain estimates |
| SEMI | https://www.semi.org/ | industry capacity context |

---

### 47. `gpu_secondary_market_prices`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| eBay sold listings | https://www.ebay.com/ | used GPU price proxy, manual/scrape carefully |
| Lambda pricing | https://lambdalabs.com/service/gpu-cloud | rental price proxy |
| RunPod pricing | https://www.runpod.io/pricing | rental price proxy |
| Vast.ai pricing | https://vast.ai/pricing | spot GPU rental proxy |
| CoreWeave pricing/contact pages | https://www.coreweave.com/ | cloud price proxy |

**Note:** follow site terms; use manual sampling if scraping is restricted.

---

## P2 — Facility, Regulation, Strategic Investment Tables

### 48. `facility_ppa_contracts`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| FERC eLibrary | https://elibrary.ferc.gov/eLibrary/search | power contracts / dockets |
| EIA electricity data | https://www.eia.gov/electricity/data.php | power market context |
| Utility IRP filings | state PUC websites | PPA/large load references |
| LevelTen public reports | https://www.leveltenenergy.com/resources | PPA price trends, limited free |
| Company sustainability reports | company IR pages | renewable PPAs |

---

### 49. `facility_interconnection_status`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| PJM service requests | https://www.pjm.com/planning/service-requests | interconnection projects |
| ERCOT resource interconnection | https://www.ercot.com/gridinfo/resource | Texas queue context |
| CAISO interconnection | https://www.caiso.com/generation-transmission/generation/generator-interconnection | CAISO queue |
| MISO generator interconnection | https://www.misoenergy.org/planning/generator-interconnection/ | MISO queue |
| SPP interconnection | https://www.spp.org/engineering/generator-interconnection/ | SPP queue |
| NYISO interconnections | https://www.nyiso.com/interconnections | NYISO queue |
| ISO-NE interconnection | https://www.iso-ne.com/system-planning/interconnection-service | New England queue |
| FERC eLibrary | https://elibrary.ferc.gov/eLibrary/search | transmission/interconnection dockets |

---

### 50. `facility_water_rights`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| USGS Water Data | https://waterdata.usgs.gov/ | water data |
| EPA ECHO | https://echo.epa.gov/ | permits/compliance |
| USGS Water Use | https://www.usgs.gov/mission-areas/water-resources/science/water-use-united-states | water-use context |
| State water boards | varies by state | permits/water rights |
| County planning documents | county websites | facility water commitments |

---

### 51. `facility_gpu_deployment`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| Facility press releases | operator/company newsrooms | GPU counts and deployment claims |
| NVIDIA case studies | https://www.nvidia.com/en-us/customer-stories/ | cluster details |
| CoreWeave newsroom | https://www.coreweave.com/newsroom | deployment details |
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/ | public data-center GPU reports |
| SEC filings | https://www.sec.gov/edgar/search/ | CapEx/purchase commitments |

---

### 52. `regulatory_company_exposure`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| EU AI Act text | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | EU AI obligations |
| NIST AI RMF | https://www.nist.gov/itl/ai-risk-management-framework | US AI risk framework |
| White House AI resources | https://www.whitehouse.gov/ostp/ai/ | US AI policy |
| BIS Federal Register | https://www.federalregister.gov/agencies/industry-and-security-bureau | export controls |
| Consolidated Screening List | https://www.trade.gov/consolidated-screening-list | restricted-party mapping |
| FTC cases | https://www.ftc.gov/legal-library/browse/cases-proceedings | AI/privacy enforcement |
| SEC filings | https://www.sec.gov/edgar/search/ | company geographic revenue/risk factors |

---

### 53. `national_ai_investment_recipients`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| CHIPS.gov funding status | https://www.chips.gov/funding-status | US semiconductor grants |
| USAspending | https://www.usaspending.gov/ | US federal awards/contracts |
| SAM.gov data services | https://sam.gov/data-services | US contract opportunities/data |
| EU State Aid Transparency Public Search | https://competition-policy.ec.europa.eu/state-aid/transparency/public-search_en | EU subsidies |
| EU TED tenders | https://ted.europa.eu/ | EU public procurement |
| UK Contracts Finder | https://www.contractsfinder.service.gov.uk/ | UK public contracts |
| OECD AI Policy Observatory | https://oecd.ai/ | national AI policy tracking |
| India MeitY | https://www.meity.gov.in/ | India AI/semiconductor programs |
| Japan METI | https://www.meti.go.jp/english/ | Japan industrial policy |

---

### 54. `shock_recovery_curves`

**Free sources:**

| Source | Link | Use |
|---|---|---|
| FRED macro time series | https://fred.stlouisfed.org/ | recession/recovery history |
| NBER business cycle dates | https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions | recession dates |
| IMF data | https://www.imf.org/en/Data | global macro shocks |
| World Bank data | https://data.worldbank.org/ | global macro history |
| FRED credit spreads | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2 | credit stress curves |
| Your `historical_backtest` table | local | tech-sector recovery calibration |
| Your `stress_scenarios` table | local | shock magnitudes |

**Collection method:** compute quarter-by-quarter average paths after historical shocks.

---

# Recommended Fast Build Order

Build these first because they unlock valuation and publishability fastest:

```text
1. company_security_master
2. equity_prices_daily
3. shares_outstanding_quarterly
4. market_cap_quarterly
5. enterprise_value_quarterly
6. valuation_multiples_quarterly
7. company_segments_quarterly
8. cloud_ai_revenue_split_estimated
9. vendor_token_usage_proxy
10. ai_ipo_database
11. dotcom_ipo_database
12. dotcom_drawdown_summary
```

Then build:

```text
13. private_ai_company_financials_estimated
14. private_ai_valuation_rounds
15. cloud_rpo_maturity_schedule
16. enterprise_contract_maturity_proxy
17. macro_timeseries_fred
18. monte_carlo_distributions
19. monte_carlo_correlation_matrix
20. endpoint_calibration_company_level
21. endpoint_calibration_sector_level
```

---

# Notes on Free vs Non-Free Limits

Some data cannot be perfectly sourced for free:

```text
CRSP delisted daily returns
Compustat historical dot-com financials
FactSet / Refinitiv / IBES analyst estimates
PitchBook private company financials
Forge / Caplight secondary prices
SensorTower / Similarweb full app and web telemetry
IDC / Gartner surveys
actual enterprise contract schedules
actual vendor token telemetry
```

Use free proxies, triangulate from multiple public sources, and store confidence scores.
