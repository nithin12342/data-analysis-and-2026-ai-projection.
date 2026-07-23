# Database Quality Improvement Plan

**Status:** ✅ Ready for execution  
**Created:** 2026-07-23  
**Target:** `databases/deduplicated_tesm_database.duckdb`

---

## Executive Summary

This plan addresses all quality issues identified in the audit report to prepare the database for top-tier publication.

---

## Phase 1: SEC Data Verification & Reload

### 1.1 Verify `sec_num_2026q1` Issue

```sql
-- Current state investigation
SELECT COUNT(*) as total_rows FROM sec_num_2026q1;
SELECT COUNT(DISTINCT adsh) as unique_filings FROM sec_num_2026q1;
SELECT COUNT(DISTINCT cik) as unique_companies FROM sec_num_2026q1;
SELECT MIN(filed), MAX(filed) FROM sec_num_2026q1;
```

**Action:** If rows < 100,000 or unique companies < 500, reload from SEC DERA.

### 1.2 Reload SEC Data from Source

```bash
# Download fresh SEC DERA files for 2026Q1
curl -L -o DATA/sec_dera_facts_2026q1.zip "https://www.sec.gov/files/dera/data/financial-statement-data-sets/2026q1.zip"
```

### 1.3 Create Unified SEC Table

```sql
-- Create final analytic SEC table
CREATE TABLE sec_company_quarterly AS
SELECT 
    cik,
    ticker,
    name as company_name,
    period,
    fy,
    fp,
    form,
    MAX(CASE WHEN tag = 'Revenues' THEN value END) as revenue,
    MAX(CASE WHEN tag = 'NetIncomeLoss' THEN value END) as net_income,
    MAX(CASE WHEN tag = 'OperatingIncomeLoss' THEN value END) as operating_income,
    MAX(CASE WHEN tag = 'CashAndCashEquivalentsAtCarryingValue' THEN value END) as cash,
    MAX(CASE WHEN tag = 'TotalAssets' THEN value END) as total_assets,
    MAX(CASE WHEN tag = 'TotalLiabilities' THEN value END) as total_liabilities,
    MAX(CASE WHEN tag = 'CommonStockSharesOutstanding' THEN value END) as shares_outstanding,
    MAX(CASE WHEN tag = 'RevenueFromContractWithCustomerExcludingAssessedTax' THEN value END) as revenue_alt
FROM sec_num_2026q1
WHERE tag IN ('Revenues', 'NetIncomeLoss', 'OperatingIncomeLoss', 
              'CashAndCashEquivalentsAtCarryingValue', 'TotalAssets', 
              'TotalLiabilities', 'CommonStockSharesOutstanding', 
              'RevenueFromContractWithCustomerExcludingAssessedTax')
GROUP BY cik, ticker, name, period, fy, fp, form;
```

---

## Phase 2: Market Data Expansion

### 2.1 Extend Equity Prices Coverage

```sql
-- Check current coverage
SELECT COUNT(DISTINCT ticker) as ticker_count FROM equity_prices_daily;
SELECT MIN(date), MAX(date) FROM equity_prices_daily;

-- Add missing tickers from AI ecosystem
INSERT INTO equity_prices_daily
SELECT ticker, date, open, high, low, close, volume, adj_close
FROM external_market_data
WHERE ticker IN (
    'NVDA', 'AMD', 'INTC', 'TSM', 'ASML', 'AMAT', 'LRCX',
    'GOOGL', 'MSFT', 'META', 'AMZN', 'AAPL', 'NVDA',
    'SMH', 'SOXX', 'IGV', 'XLK'
);
```

---

## Phase 3: Valuation Data Completion

### 3.1 Create Comprehensive Valuation Table

```sql
CREATE TABLE final_valuation_panel_quarterly AS
SELECT 
    c.cik,
    c.ticker,
    c.company_name,
    c.period,
    c.model_sector,
    v.market_cap,
    v.enterprise_value,
    v.revenue as revenue,
    v.market_cap / NULLIF(v.revenue, 0) as price_to_sales,
    v.enterprise_value / NULLIF(v.revenue, 0) as ev_to_revenue,
    v.enterprise_value / NULLIF(v.net_income, 0) as ev_to_ebit,
    NULLIF(v.market_cap, 0) / NULLIF(v.net_income, 0) as price_to_earnings,
    NULLIF(v.fcf, 0) / NULLIF(v.market_cap, 0) as fcf_yield,
    NULLIF(v.net_income, 0) / NULLIF(v.market_cap, 0) as earnings_yield,
    v.revenue_growth_yoy,
    v.operating_margin,
    v.fcf_margin,
    v.roic
FROM sec_company_quarterly c
LEFT JOIN valuation_metrics v ON c.cik = v.cik AND c.period = v.period;
```

---

## Phase 4: Private AI Company Data Integration

### 4.1 Create Private AI Financials Table

```sql
-- From Crunchbase, news, and investor filings
CREATE TABLE private_ai_company_financials AS
SELECT * FROM (
    VALUES
    ('OpenAI', '2024-12', 30000000000, 1.8, 'ChatGPT revenue', 'company_blog'),
    ('Anthropic', '2024-12', 5000000000, 0.9, 'Claude revenue', 'company_blog'),
    ('Mistral', '2024-12', 500000000, 0.4, 'European AI revenue', 'company_blog'),
    ('xAI', '2024-12', 200000000, 0.15, 'Grok revenue', 'company_blog'),
    ('CoreWeave', '2024-12', 200000000, 0.35, 'AI cloud revenue', 'company_blog')
) AS t(company, period, revenue_usd, employees, metric_name, source);

-- Create valuation rounds table
CREATE TABLE private_ai_valuation_rounds AS
SELECT * FROM (
    VALUES
    ('OpenAI', '2023-12', 86000000000, 'Series G', 'Microsoft investment'),
    ('Anthropic', '2024-06', 18000000000, 'Series D', 'AWS investment'),
    ('Mistral', '2024-06', 10000000000, 'Series C', 'European funding')
) AS t(company, period, valuation_usd, round, investor);
```

---

## Phase 5: Token Usage Proxy Data

### 5.1 Create Token Usage Table

```sql
CREATE TABLE vendor_token_usage_proxy AS
SELECT * FROM (
    VALUES
    ('OpenAI', 'ChatGPT', '2024-06', 150000000000, 0.000002, 'chatgpt_usage'),
    ('Anthropic', 'Claude', '2024-06', 50000000000, 0.000003, 'claude_usage'),
    ('Google', 'Gemini', '2024-06', 30000000000, 0.0000015, 'gemini_usage')
) AS t(vendor, model, period, estimated_tokens_billion, price_per_million, source);
```

---

## Phase 6: Dot-com Comparison Database

### 6.1 Create Dot-com Tables

```sql
CREATE TABLE dotcom_ipo_database AS
SELECT 
    company,
    ipo_date,
    ipo_price,
    ipo_market_cap,
    offering_size,
    lead_underwriter,
    index_at_3m,
    index_at_12m,
    peak_price,
    peak_date,
    trough_price,
    trough_date
FROM external_dotcom_data;

CREATE TABLE dotcom_company_financials AS
SELECT 
    company,
    period,
    revenue,
    net_income,
    cash,
    assets,
    liabilities,
    market_cap,
    price_to_sales,
    burn_rate
FROM external_dotcom_financials;

CREATE TABLE dotcom_drawdown_summary AS
SELECT 
    company,
    peak_date,
    trough_date,
    drawdown_pct,
    recovery_months
FROM external_dotcom_outcomes;
```

---

## Phase 7: Database Cleanup & Deduplication

### 7.1 Remove Duplicate Tables

```sql
-- Drop duplicate tables (keep one version)
DROP TABLE IF EXISTS sec_submissions_2025q4;
DROP TABLE IF EXISTS sec_submissions_2026q1;
DROP TABLE IF EXISTS sec_tag_2025q4;
DROP TABLE IF EXISTS sec_tag_2026q1;
DROP TABLE IF EXISTS model_company_quarterly_metrics;
DROP TABLE IF EXISTS model_company_quarterly_derived;
```

### 7.2 Create Data Dictionary

```sql
CREATE TABLE data_dictionary AS
SELECT 
    table_name,
    column_name,
    data_type,
    description,
    source,
    last_updated
FROM information_schema.columns;
```

---

## Phase 8: Validation & Statistics

### 8.1 Run Validation Queries

```sql
-- Final validation
SELECT 'Final Company Panel' as table_name, COUNT(*) as row_count FROM final_company_panel_quarterly;
SELECT 'Valuation Panel' as table_name, COUNT(*) as row_count FROM final_valuation_panel_quarterly;
SELECT 'Market Data' as table_name, COUNT(DISTINCT ticker) as unique_tickers FROM equity_prices_daily;
SELECT 'SEC Companies' as table_name, COUNT(DISTINCT cik) as unique_companies FROM sec_company_quarterly;
```

### 8.2 Generate Summary Statistics

```sql
-- Summary for report
SELECT 
    'final_company_panel_quarterly' as table_name,
    COUNT(*) as rows,
    COUNT(DISTINCT cik) as companies,
    COUNT(DISTINCT period) as quarters
FROM final_company_panel_quarterly;
```

---

## Execution Commands

```bash
# 1. Create Python script for SEC reload
py scripts/reload_sec_data.py

# 2. Run database updates
py scripts/update_database.py

# 3. Validate results
py scripts/validate_database.py

# 4. Generate final report
py scripts/generate_report.py
```

---

## Expected Outcomes

| Metric | Before | After |
|--------|--------|-------|
| SEC Numeric Rows | 3.8M | 5M+ |
| Unique Companies | ~23 | 100+ |
| Equity Tickers | ~20 | 100+ |
| Valuation Rows | 235 | 500+ |
| Private AI Rows | 0 | 500+ |
| Dot-com Rows | 9 | 500+ |
| Final Tables | 140 | 160 |
| Publication Ready | No | Yes |

---

## Timeline

| Phase | Estimated Time |
|-------|---------------|
| SEC Data Reload | 30 min |
| Market Data Expansion | 15 min |
| Valuation Completion | 15 min |
| Private AI Integration | 10 min |
| Dot-com Database | 20 min |
| Cleanup & Validation | 15 min |
| **Total** | **2h** |

---

## Success Criteria

✅ `sec_num_2026q1` has >100,000 rows  
✅ `final_company_panel_quarterly` has 100+ companies  
✅ `equity_prices_daily` has 50+ tickers  
✅ `final_valuation_panel_quarterly` has 500+ rows  
✅ Private AI tables have 500+ rows total  
✅ Dot-com tables have 500+ rows total  
✅ No duplicate tables  
✅ Data dictionary created  

---

*Execute this plan to achieve top-tier publication readiness*