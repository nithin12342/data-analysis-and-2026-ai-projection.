# Data Acquisition Cluster Matrix for 54 TESM Tables

**Objective:** partition the 54 proposed missing/enrichment tables by the fastest realistic free acquisition route.

**Clusters requested:**

| Cluster | Meaning | Typical automation |
|---|---|---|
| **A. Bulk download / direct CSV available** | Public downloadable CSV/JSON/ZIP, official archive, or derived from bulk tables. | Batch downloader + parser |
| **B. Free API available** | Public API endpoint is available without paid subscription. May still have rate limits. | API client + rate limiter |
| **C. Login / verification / API key needed** | Free or freemium, but needs account, API key, developer registration, or anti-bot/manual verification. | API client after registration, or manual verified download |
| **D. Web scraping possible and relatively friendly** | Public web pages, HTML tables, PDFs, investor pages, docs, ETF holdings pages, pricing pages. Must respect robots.txt and ToS. | Polite scraper + HTML/PDF parser |
| **E. Very fragmented / AI-agent research needed** | No single clean source. Requires web search, source triangulation, manual review, confidence scoring, and estimates. | AI agent + search + extraction + human review |

**Important note:** Some tables are *derived*. They are classified by the easiest acquisition route for the raw inputs. For example, `valuation_multiples_quarterly` is derived from SEC financials + prices + shares, so it is classified as **A**.

---

# 1. Cluster Summary

| Cluster | Count | Tables |
|---|---:|---|
| **A. Bulk download / direct CSV available** | 18 | `company_security_master`, `equity_prices_daily`, `market_cap_quarterly`, `enterprise_value_quarterly`, `valuation_multiples_quarterly`, `dotcom_ipo_database`, `cloud_rpo_maturity_schedule`, `macro_timeseries_fred`, `monte_carlo_distributions`, `monte_carlo_correlation_matrix`, `endpoint_calibration_sector_level`, `market_indices_daily`, `sector_etf_prices_daily`, `institutional_ownership_13f`, `short_interest`, `margin_debt_market_sentiment`, `facility_interconnection_status`, `shock_recovery_curves` |
| **B. Free API available** | 8 | `shares_outstanding_quarterly`, `ai_ipo_database`, `open_source_model_registry`, `huggingface_model_downloads`, `github_model_activity`, `model_routing_mix`, `agent_incident_database`, `national_ai_investment_recipients` |
| **C. Login / verification / API key needed** | 5 | `private_ai_valuation_rounds`, `private_ai_usage_estimates`, `analyst_estimates_quarterly`, `options_volume_summary`, `gpu_secondary_market_prices` |
| **D. Web scraping possible and friendly** | 6 | `company_segments_quarterly`, `enterprise_contract_maturity_proxy`, `gpu_reservation_expiration_proxy`, `sector_etf_holdings`, `ai_efficiency_timeseries`, `training_runs_by_company` |
| **E. Fragmented / AI-agent web research needed** | 17 | `cloud_ai_revenue_split_estimated`, `vendor_token_usage_proxy`, `token_usage_by_workload_proxy`, `private_ai_company_financials_estimated`, `dotcom_company_financials_proxy`, `dotcom_drawdown_summary`, `dotcom_survival_outcomes`, `endpoint_calibration_company_level`, `inference_request_volume_proxy`, `agentic_tco_case_studies`, `workflow_integration_case_studies`, `gpu_order_book_proxy`, `wafer_hbm_allocation_proxy`, `facility_ppa_contracts`, `facility_water_rights`, `facility_gpu_deployment`, `regulatory_company_exposure` |
| **Total** | **54** | — |

---

# 2. Complete 54-Table Acquisition Matrix

| # | Table | Primary Cluster | Best free/public source route | Core links | Recommended acquisition method | Notes |
|---:|---|---|---|---|---|---|
| 1 | `company_security_master` | **A. Bulk download** | SEC company tickers JSON + Nasdaq/NYSE symbol directories | SEC tickers: https://www.sec.gov/files/company_tickers.json ; Nasdaq symbols: https://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs ; NYSE listings: https://www.nyse.com/listings_directory/stock | Bulk JSON/CSV ingestion, then manual/model-sector classification | Easiest foundational table. Add `model_sector` manually. |
| 2 | `equity_prices_daily` | **A. Bulk download** | Stooq direct CSV per ticker; Yahoo chart endpoint as fallback | Stooq example: https://stooq.com/q/d/l/?s=nvda.us&i=d ; Yahoo example: https://query1.finance.yahoo.com/v8/finance/chart/NVDA?period1=0&period2=9999999999&interval=1d | Batch ticker loop, save OHLCV | Stooq is simplest no-login CSV. Yahoo is unofficial, use carefully. |
| 3 | `shares_outstanding_quarterly` | **B. Free API** | SEC CompanyFacts API + SEC DERA facts | Example: https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json ; SEC DERA: https://www.sec.gov/dera/data/financial-statement-data-sets | API pull by CIK; extract share tags | Use tags: `EntityCommonStockSharesOutstanding`, `WeightedAverageNumberOfDilutedSharesOutstanding`. |
| 4 | `market_cap_quarterly` | **A. Bulk download / derived** | Derived from Stooq/Yahoo prices + SEC shares | Stooq: https://stooq.com/ ; SEC tickers: https://www.sec.gov/files/company_tickers.json | Compute quarter-end price × shares | No separate source needed after price/share tables. |
| 5 | `enterprise_value_quarterly` | **A. Bulk download / derived** | Derived from SEC financials + market cap | SEC DERA: https://www.sec.gov/dera/data/financial-statement-data-sets ; SEC CompanyFacts API: https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json | Compute EV = market cap + debt - cash | Your current DuckDB already has cash/debt fields. |
| 6 | `valuation_multiples_quarterly` | **A. Bulk download / derived** | Derived from SEC financials + EV + market cap | SEC DERA + Stooq | Compute P/S, EV/revenue, EV/EBITDA, FCF yield, etc. | High-value table for bubble analysis. |
| 7 | `company_segments_quarterly` | **D. Web scraping friendly** | SEC 10-K/10-Q HTML segment tables + company IR pages | SEC search: https://www.sec.gov/edgar/search/ ; Amazon IR: https://ir.aboutamazon.com/ ; Microsoft IR: https://www.microsoft.com/en-us/investor ; NVIDIA IR: https://investor.nvidia.com/ | Scrape/parse SEC HTML footnotes and IR presentations | XBRL has some segment data, but normalized segment tables require parsing. |
| 8 | `cloud_ai_revenue_split_estimated` | **E. Fragmented / AI-agent research** | Earnings call comments, 10-Q/10-K, IR decks, AI cloud deal announcements | Microsoft IR: https://www.microsoft.com/en-us/investor ; Amazon IR: https://ir.aboutamazon.com/ ; Alphabet IR: https://abc.xyz/investor/ ; Oracle IR: https://investor.oracle.com/ | AI agent searches filings/transcripts for AI contribution comments, then triangulates estimates | No direct official AI cloud revenue split usually exists. Store confidence. |
| 9 | `vendor_token_usage_proxy` | **E. Fragmented / AI-agent research** | Vendor disclosures, OpenRouter, traffic proxies, user counts, GPU-capacity proxies | OpenRouter rankings: https://openrouter.ai/rankings ; OpenRouter models API: https://openrouter.ai/api/v1/models ; Google Trends: https://trends.google.com/trends/ | Estimate tokens from users × prompts or revenue ÷ price | True token usage is proprietary; use proxy methods with confidence tiers. |
| 10 | `token_usage_by_workload_proxy` | **E. Fragmented / AI-agent research** | Product blogs, customer stories, OpenRouter categories, GitHub Copilot posts, Salesforce/Microsoft cases | GitHub blog: https://github.blog/tag/github-copilot/ ; Microsoft customers: https://customers.microsoft.com/ ; Salesforce stories: https://www.salesforce.com/customer-success-stories/ | AI agent classifies public usage evidence by workload | Requires workload tagging and assumptions. |
| 11 | `private_ai_company_financials_estimated` | **E. Fragmented / AI-agent research** | Company blogs, Reuters, TechCrunch, investor disclosures, public estimates | Reuters AI: https://www.reuters.com/technology/artificial-intelligence/ ; TechCrunch AI: https://techcrunch.com/category/artificial-intelligence/ ; SEC search: https://www.sec.gov/edgar/search/ | AI agent searches company-by-company; store metric-level rows | Use long format: `company, date, metric, value`. |
| 12 | `private_ai_valuation_rounds` | **C. Login / API key / verification** | Crunchbase free snippets, media reports, company announcements; PitchBook/Forge paid if available | Crunchbase: https://www.crunchbase.com/ ; TechCrunch: https://techcrunch.com/ ; Reuters AI: https://www.reuters.com/technology/artificial-intelligence/ | Manual/account-assisted extraction + media triangulation | Free complete private valuations are not clean; Crunchbase often requires login. |
| 13 | `private_ai_usage_estimates` | **C. Login / API key / verification** | Similarweb free snippets/login, app stores, Google Trends, company disclosures | Similarweb: https://www.similarweb.com/ ; Google Trends: https://trends.google.com/trends/ ; Google Play: https://play.google.com/store/apps | Use public traffic/app/user proxies; some portals may need login | Treat as estimates, not audited facts. |
| 14 | `ai_ipo_database` | **B. Free API** | SEC S-1/F-1 filings, SEC submissions API, Nasdaq/NYSE IPO pages | SEC search: https://www.sec.gov/edgar/search/ ; SEC submissions API example: https://data.sec.gov/submissions/CIK0001045810.json ; Nasdaq IPOs: https://www.nasdaq.com/market-activity/ipos ; NYSE IPO center: https://www.nyse.com/ipo-center | SEC API discovers filings; parse S-1 tables | Free but parsing S-1 quality fields takes work. |
| 15 | `dotcom_ipo_database` | **A. Bulk download** | Jay Ritter IPO data + SEC historical archives | Jay Ritter: https://site.warrington.ufl.edu/ritter/ipo-data/ ; SEC archives: https://www.sec.gov/Archives/edgar/ | Download IPO spreadsheets, enrich with SEC S-1 financials | Best free starting point for IPO returns/proceeds. |
| 16 | `dotcom_company_financials_proxy` | **E. Fragmented / AI-agent research** | SEC historical 10-K/10-Q/S-1 filings, old annual reports, Internet Archive | SEC Archives: https://www.sec.gov/Archives/edgar/ ; SEC search: https://www.sec.gov/edgar/search/ ; Internet Archive: https://web.archive.org/ | AI agent builds cohort, finds filings, extracts financials | No free clean Compustat replacement; start with 25–50 firms. |
| 17 | `dotcom_drawdown_summary` | **E. Fragmented / AI-agent research** | Stooq/Yahoo for survivors; manual sources for delisted firms | Stooq: https://stooq.com/ ; Internet Archive: https://web.archive.org/ ; SEC search: https://www.sec.gov/edgar/search/ | Automated for survivors, AI-agent/manual for delisted/bankrupt firms | CRSP is ideal but not free. Use confidence scoring. |
| 18 | `dotcom_survival_outcomes` | **E. Fragmented / AI-agent research** | SEC filings, bankruptcy references, Internet Archive, Wikipedia as seed only | SEC search: https://www.sec.gov/edgar/search/ ; CourtListener: https://www.courtlistener.com/ ; Internet Archive: https://web.archive.org/ | AI agent validates company outcome from multiple sources | Use Wikipedia only as seed; verify via filings/news. |
| 19 | `cloud_rpo_maturity_schedule` | **A. Bulk download / filings** | SEC 10-K/10-Q RPO maturity disclosures | SEC search: https://www.sec.gov/edgar/search/ ; Salesforce IR: https://investor.salesforce.com/ ; ServiceNow IR: https://www.servicenow.com/company/investor-relations.html | Parse ASC 606 RPO tables from filings | Some RPO values are XBRL; maturity buckets often in HTML footnotes. |
| 20 | `enterprise_contract_maturity_proxy` | **D. Web scraping friendly** | Cloud pricing/docs for reserved instances, savings plans, capacity blocks + RPO tables | AWS RI: https://aws.amazon.com/ec2/pricing/reserved-instances/ ; AWS Capacity Blocks: https://aws.amazon.com/ec2/capacityblocks/ ; Azure Reservations: https://azure.microsoft.com/en-us/pricing/reservations/ ; GCP CUD: https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts | Scrape docs/pricing terms; combine with RPO/deferred revenue | Actual contract-level maturity is private; proxy from terms and RPO. |
| 21 | `gpu_reservation_expiration_proxy` | **D. Web scraping friendly** | AWS Capacity Blocks, GPU cloud provider pages, public capacity deals | AWS Capacity Blocks: https://aws.amazon.com/ec2/capacityblocks/ ; Lambda: https://lambdalabs.com/service/gpu-cloud ; RunPod: https://www.runpod.io/pricing ; CoreWeave newsroom: https://www.coreweave.com/newsroom | Scrape GPU reservation terms and public deals | Customer-specific expiries usually private. |
| 22 | `macro_timeseries_fred` | **A. Bulk download** | FRED direct CSV endpoint | FRED CSV example: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10 ; FRED API docs: https://fred.stlouisfed.org/docs/api/fred/ | Direct CSV download for each series | No API key needed for CSV graph endpoint. |
| 23 | `monte_carlo_distributions` | **A. Bulk download / derived** | Derived from FRED, equity prices, current module tables, stress tables | FRED: https://fred.stlouisfed.org/ ; local DuckDB stress/module tables | Compute empirical p05/p50/p95 and fit distributions | This is a generated calibration table. |
| 24 | `monte_carlo_correlation_matrix` | **A. Bulk download / derived** | Derived from FRED, equity prices, commodity time series, scenario tables | FRED: https://fred.stlouisfed.org/ ; Stooq: https://stooq.com/ | Compute correlations from historical changes/returns | Add expert priors only for unobservable correlations. |
| 25 | `endpoint_calibration_company_level` | **E. Fragmented / AI-agent research** | Dot-com/telecom/cloud/smartphone company panels from SEC + price histories | SEC Archives: https://www.sec.gov/Archives/edgar/ ; Jay Ritter: https://site.warrington.ufl.edu/ritter/ipo-data/ ; Stooq: https://stooq.com/ | AI agent creates historical firm panel | Company-level calibration is the hardest free historical task. |
| 26 | `endpoint_calibration_sector_level` | **A. Bulk download / derived** | Ken French industry portfolios, FRED/index/ETF data, Stooq | Ken French: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html ; FRED: https://fred.stlouisfed.org/ ; Stooq: https://stooq.com/ | Bulk sector/index histories, compute drawdown/recovery paths | Sector-level history is much easier than company-level. |
| 27 | `analyst_estimates_quarterly` | **C. Login / API key / verification** | Nasdaq/Yahoo free pages; full APIs usually require account/key | Nasdaq earnings example: https://www.nasdaq.com/market-activity/stocks/nvda/earnings ; Yahoo analysis example: https://finance.yahoo.com/quote/NVDA/analysis | Scrape public pages or use registered free/freemium APIs | FactSet/IBES/Refinitiv are better but paid. |
| 28 | `market_indices_daily` | **A. Bulk download** | Stooq/FRED CSVs | Stooq: https://stooq.com/ ; FRED: https://fred.stlouisfed.org/ | Direct CSV download | Include NASDAQ, S&P 500, SOXX/SMH/QQQ if available. |
| 29 | `sector_etf_prices_daily` | **A. Bulk download** | Stooq ETF CSVs, Yahoo fallback | Stooq example: https://stooq.com/q/d/l/?s=smh.us&i=d ; Yahoo finance: https://finance.yahoo.com/quote/SMH/history | Batch ETF tickers | Good for sector-rotation return proxies. |
| 30 | `sector_etf_holdings` | **D. Web scraping friendly** | ETF issuer holding CSVs/pages | iShares SOXX: https://www.ishares.com/us/products/239705/ishares-semiconductor-etf ; VanEck SMH: https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/holdings/ ; Invesco QQQ: https://www.invesco.com/qqq-etf/en/about.html | Download issuer holdings CSVs or scrape holdings tables | Usually public; structure varies by issuer. |
| 31 | `institutional_ownership_13f` | **A. Bulk download** | SEC 13F-HR filings and full index | SEC search: https://www.sec.gov/edgar/search/ ; SEC full index: https://www.sec.gov/Archives/edgar/full-index/ ; SEC 13F FAQ: https://www.sec.gov/divisions/investment/13ffaq | Bulk filing discovery + parse information tables | Official and free, but parsing many filings is compute-heavy. |
| 32 | `short_interest` | **A. Bulk download** | FINRA/Nasdaq/NYSE short interest | FINRA: https://www.finra.org/finra-data/browse-catalog/equity-short-interest ; Nasdaq example: https://www.nasdaq.com/market-activity/stocks/nvda/short-interest ; NYSE: https://www.nyse.com/market-data/reference/nyse-group-short-interest | Download/parse short-interest data | Best free sentiment/crowding proxy. |
| 33 | `options_volume_summary` | **C. Login / API key / verification** | OCC/Cboe aggregate reports, Yahoo/Nasdaq option chains | Cboe stats: https://www.cboe.com/us/options/market_statistics/ ; OCC reports: https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest ; Nasdaq option chain: https://www.nasdaq.com/market-activity/stocks/nvda/option-chain | Aggregate public reports are easy; ticker-level chains may require scraping/API/key | Full Greeks/gamma are not free. |
| 34 | `margin_debt_market_sentiment` | **A. Bulk download** | FINRA margin statistics + FRED proxies | FINRA margin stats: https://www.finra.org/rules-guidance/key-topics/margin-accounts/margin-statistics ; FRED: https://fred.stlouisfed.org/ | Download monthly margin stats | Strong bubble-sentiment context. |
| 35 | `open_source_model_registry` | **B. Free API** | Hugging Face API, GitHub API, leaderboards | HF API: https://huggingface.co/api/models ; HF docs: https://huggingface.co/docs/hub/api ; GitHub API: https://docs.github.com/en/rest ; LMArena: https://lmarena.ai/leaderboard | API pull + leaderboard enrichment | GitHub token optional for higher rate limit. |
| 36 | `huggingface_model_downloads` | **B. Free API** | Hugging Face model API | HF API: https://huggingface.co/api/models ; model endpoint pattern: https://huggingface.co/api/models/{repo_id} | API pagination and repo-specific calls | Very useful open-source adoption table. |
| 37 | `github_model_activity` | **B. Free API** | GitHub REST API, GH Archive | GitHub REST API: https://docs.github.com/en/rest ; GH Archive: https://www.gharchive.org/ | API pull stars/forks/issues; GH Archive for history | Unauthenticated GitHub has low rate limits; token optional. |
| 38 | `ai_efficiency_timeseries` | **D. Web scraping friendly** | Provider pricing pages, OpenRouter API, Artificial Analysis free pages, vLLM/NVIDIA benchmarks | OpenAI pricing: https://platform.openai.com/docs/pricing ; Anthropic pricing: https://docs.anthropic.com/en/docs/about-claude/pricing ; OpenRouter API: https://openrouter.ai/api/v1/models ; Artificial Analysis: https://artificialanalysis.ai/ | Scrape/API collect price, latency, throughput snapshots | Full historical efficiency is not centralized; build a time series going forward. |
| 39 | `model_routing_mix` | **B. Free API** | OpenRouter rankings/API, HF model data | OpenRouter rankings: https://openrouter.ai/rankings ; OpenRouter API: https://openrouter.ai/api/v1/models ; HF API: https://huggingface.co/api/models | API + ranking snapshots | True routing shares are vendor-private; this is a proxy. |
| 40 | `inference_request_volume_proxy` | **E. Fragmented / AI-agent research** | Vendor disclosures, OpenRouter, web/app traffic, user metrics | OpenRouter rankings: https://openrouter.ai/rankings ; Similarweb: https://www.similarweb.com/ ; Google Trends: https://trends.google.com/trends/ | AI agent triangulates request volume proxies | Actual requests per day are rarely disclosed. |
| 41 | `training_runs_by_company` | **D. Web scraping friendly** | Epoch AI model data, model technical reports, arXiv, provider blogs | Epoch AI models: https://epoch.ai/data/ai-models ; arXiv API: https://info.arxiv.org/help/api/index.html ; Stanford AI Index: https://aiindex.stanford.edu/report/ | Scrape/download model records, enrich with technical reports | Good for frontier models; incomplete for private internal runs. |
| 42 | `agentic_tco_case_studies` | **E. Fragmented / AI-agent research** | Vendor/customer stories, consulting reports, earnings comments | Microsoft customers: https://customers.microsoft.com/ ; Salesforce stories: https://www.salesforce.com/customer-success-stories/ ; ServiceNow customers: https://www.servicenow.com/customers.html ; Intercom customers: https://www.intercom.com/customers | AI agent extracts case-study facts and estimates TCO | Public stories are biased; use confidence scoring. |
| 43 | `workflow_integration_case_studies` | **E. Fragmented / AI-agent research** | Customer stories, GitHub Copilot blogs, ServiceNow/Salesforce/Microsoft case studies | Microsoft customers: https://customers.microsoft.com/ ; GitHub Copilot: https://github.blog/tag/github-copilot/ ; Google Cloud customers: https://cloud.google.com/customers | AI agent tags workflow, automation rate, integration depth | Requires NLP extraction from narrative case studies. |
| 44 | `agent_incident_database` | **B. Free API / public databases** | AI Incident Database, OECD AI incidents, CourtListener, FTC cases | AIID: https://incidentdatabase.ai/ ; OECD incidents: https://oecd.ai/en/incidents ; CourtListener: https://www.courtlistener.com/ ; FTC cases: https://www.ftc.gov/legal-library/browse/cases-proceedings | API/scrape incident sources; normalize taxonomy | Good source for liability-risk examples. |
| 45 | `gpu_order_book_proxy` | **E. Fragmented / AI-agent research** | NVIDIA/AMD/Dell/SMCI/HPE earnings calls, 10-Qs, press releases | NVIDIA IR: https://investor.nvidia.com/ ; AMD IR: https://ir.amd.com/ ; Supermicro IR: https://ir.supermicro.com/ ; Dell IR: https://investors.delltechnologies.com/ | AI agent extracts backlog/order comments | True order book/customer allocation is private. |
| 46 | `wafer_hbm_allocation_proxy` | **E. Fragmented / AI-agent research** | TSMC/SK Hynix/Micron/Samsung IR, TrendForce free reports, SEMI | TSMC IR: https://investor.tsmc.com/ ; SK hynix IR: https://www.skhynix.com/eng/ir/irData.do ; Micron IR: https://investors.micron.com/ ; TrendForce: https://www.trendforce.com/presscenter | AI agent triangulates allocation from earnings/commentary | Customer-level allocation is usually not public. |
| 47 | `gpu_secondary_market_prices` | **C. Login / API key / verification** | eBay sold listings/API, Vast.ai, RunPod, Lambda prices | eBay: https://www.ebay.com/ ; Vast.ai pricing: https://vast.ai/pricing ; RunPod: https://www.runpod.io/pricing ; Lambda: https://lambdalabs.com/service/gpu-cloud | Marketplace API/account or manual sampling | Respect marketplace ToS; eBay API needs developer registration. |
| 48 | `facility_ppa_contracts` | **E. Fragmented / AI-agent research** | FERC eLibrary, utility dockets, PUC filings, sustainability reports | FERC eLibrary: https://elibrary.ferc.gov/eLibrary/search ; EIA electricity: https://www.eia.gov/electricity/data.php ; LevelTen resources: https://www.leveltenenergy.com/resources | AI agent searches facility/operator/utility dockets | PPA details are scattered and often redacted. |
| 49 | `facility_interconnection_status` | **A. Bulk download** | ISO/RTO interconnection queues + FERC dockets | PJM: https://www.pjm.com/planning/service-requests ; ERCOT: https://www.ercot.com/gridinfo/resource ; CAISO: https://www.caiso.com/generation-transmission/generation/generator-interconnection ; MISO: https://www.misoenergy.org/planning/generator-interconnection/ ; NYISO: https://www.nyiso.com/interconnections | Download ISO queue files, match facility geography/operator | Good bulk availability, but schema differs by ISO. |
| 50 | `facility_water_rights` | **E. Fragmented / AI-agent research** | State water boards, USGS, EPA ECHO, county permits | USGS Water Data: https://waterdata.usgs.gov/ ; EPA ECHO: https://echo.epa.gov/ ; USGS Water Use: https://www.usgs.gov/mission-areas/water-resources/science/water-use-united-states | AI agent searches facility/county/state water permits | Water rights are state/county fragmented. |
| 51 | `facility_gpu_deployment` | **E. Fragmented / AI-agent research** | Press releases, NVIDIA case studies, DCD articles, SEC purchase obligations | NVIDIA customer stories: https://www.nvidia.com/en-us/customer-stories/ ; DCD: https://www.datacenterdynamics.com/en/news/ ; CoreWeave newsroom: https://www.coreweave.com/newsroom | AI agent matches facility to GPU/cluster claims | Actual GPU deployments are often estimated. |
| 52 | `regulatory_company_exposure` | **E. Fragmented / AI-agent research** | Regulations + company geographic revenue/risk factors + export controls | EU AI Act: https://eur-lex.europa.eu/eli/reg/2024/1689/oj ; NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework ; BIS/Federal Register: https://www.federalregister.gov/agencies/industry-and-security-bureau ; CSL: https://www.trade.gov/consolidated-screening-list | AI agent maps company revenues/models/geographies to rules | Requires judgment and documented assumptions. |
| 53 | `national_ai_investment_recipients` | **B. Free API** | CHIPS.gov, USAspending API, EU TED/state aid, government procurement | CHIPS funding: https://www.chips.gov/funding-status ; USAspending: https://www.usaspending.gov/ ; SAM data: https://sam.gov/data-services ; EU TED: https://ted.europa.eu/ ; EU State Aid: https://competition-policy.ec.europa.eu/state-aid/transparency/public-search_en | API/bulk government award collection | Government award data is public but needs entity matching. |
| 54 | `shock_recovery_curves` | **A. Bulk download / derived** | FRED, NBER recession dates, IMF/World Bank, your historical backtest | NBER cycles: https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions ; FRED: https://fred.stlouisfed.org/ ; IMF data: https://www.imf.org/en/Data ; World Bank: https://data.worldbank.org/ | Build event windows and compute average recovery paths | Derived table from bulk macro/market history. |

---

# 3. Cluster-by-Cluster Work Plan

## A. Bulk download / direct CSV available

**Tables:** 18

```text
company_security_master
equity_prices_daily
market_cap_quarterly
enterprise_value_quarterly
valuation_multiples_quarterly
dotcom_ipo_database
cloud_rpo_maturity_schedule
macro_timeseries_fred
monte_carlo_distributions
monte_carlo_correlation_matrix
endpoint_calibration_sector_level
market_indices_daily
sector_etf_prices_daily
institutional_ownership_13f
short_interest
margin_debt_market_sentiment
facility_interconnection_status
shock_recovery_curves
```

**Fastest scripts to write:**

```text
collect_sec_company_master.py
collect_stooq_prices.py
collect_fred_timeseries.py
collect_sec_13f.py
collect_finra_short_interest.py
collect_iso_interconnection_queues.py
build_valuation_multiples.py
build_monte_carlo_distributions.py
```

---

## B. Free API available

**Tables:** 8

```text
shares_outstanding_quarterly
ai_ipo_database
open_source_model_registry
huggingface_model_downloads
github_model_activity
model_routing_mix
agent_incident_database
national_ai_investment_recipients
```

**Fastest scripts to write:**

```text
collect_sec_companyfacts.py
collect_sec_s1_filings.py
collect_huggingface_models.py
collect_github_activity.py
collect_openrouter_models.py
collect_ai_incidents.py
collect_usaspending_ai_awards.py
```

---

## C. Login / verification / API key needed

**Tables:** 5

```text
private_ai_valuation_rounds
private_ai_usage_estimates
analyst_estimates_quarterly
options_volume_summary
gpu_secondary_market_prices
```

**Recommended approach:**

1. Use public pages first.
2. Register only where free API keys help: GitHub high rate limits, eBay developer API, OpenFIGI if needed, Nasdaq/Yahoo alternatives.
3. Avoid paid data dependencies in the first pass.

---

## D. Web scraping possible and relatively friendly

**Tables:** 6

```text
company_segments_quarterly
enterprise_contract_maturity_proxy
gpu_reservation_expiration_proxy
sector_etf_holdings
ai_efficiency_timeseries
training_runs_by_company
```

**Rules:**

```text
respect robots.txt
use low request rates
cache all downloaded pages
store source_url per row
prefer official CSV/PDF when available
```

---

## E. Fragmented / AI-agent research needed

**Tables:** 17

```text
cloud_ai_revenue_split_estimated
vendor_token_usage_proxy
token_usage_by_workload_proxy
private_ai_company_financials_estimated
dotcom_company_financials_proxy
dotcom_drawdown_summary
dotcom_survival_outcomes
endpoint_calibration_company_level
inference_request_volume_proxy
agentic_tco_case_studies
workflow_integration_case_studies
gpu_order_book_proxy
wafer_hbm_allocation_proxy
facility_ppa_contracts
facility_water_rights
facility_gpu_deployment
regulatory_company_exposure
```

**Recommended AI-agent workflow:**

```text
1. Define entity list.
2. Search web for official source first.
3. Search SEC/IR pages second.
4. Search reputable media third.
5. Extract metric/value/date/source_url.
6. Assign confidence score.
7. Store every estimate in long format.
8. Never overwrite raw facts; create derived/proxy values separately.
```

---

# 4. Implementation Priority Matrix

| Priority | Cluster | Tables | Reason |
|---|---|---|---|
| **Week 1** | A/B | `company_security_master`, `equity_prices_daily`, `shares_outstanding_quarterly`, `market_cap_quarterly`, `enterprise_value_quarterly`, `valuation_multiples_quarterly`, `macro_timeseries_fred` | Fixes biggest valuation and macro gap fastest. |
| **Week 2** | A/B/D | `company_segments_quarterly`, `ai_ipo_database`, `dotcom_ipo_database`, `market_indices_daily`, `sector_etf_prices_daily`, `sector_etf_holdings` | Enables public market and IPO comparison. |
| **Week 3** | E/C | `private_ai_company_financials_estimated`, `private_ai_valuation_rounds`, `private_ai_usage_estimates`, `cloud_ai_revenue_split_estimated`, `vendor_token_usage_proxy` | Fills private AI and token-demand gaps with proxies. |
| **Week 4** | A/B/C | `institutional_ownership_13f`, `short_interest`, `options_volume_summary`, `margin_debt_market_sentiment`, `open_source_model_registry`, `huggingface_model_downloads`, `github_model_activity` | Adds sentiment, reflexivity, and open-source adoption. |
| **Week 5+** | D/E | Agentic TCO, workflow integration, facility PPA/water/GPU deployment, regulatory exposure | Publication-quality enrichment. |

---

# 5. Final Recommendation

If speed matters, start with the **A and B clusters**, because they are the most automatable and least ambiguous.

**First 7 tables to build immediately:**

```text
company_security_master
equity_prices_daily
shares_outstanding_quarterly
market_cap_quarterly
enterprise_value_quarterly
valuation_multiples_quarterly
macro_timeseries_fred
```

These will make the current model much stronger than another round of infrastructure enrichment.
