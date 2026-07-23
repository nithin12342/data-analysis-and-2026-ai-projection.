# Master Consolidated Database - Table Schema Reference

**Database:** `databases/deduplicated_tesm_database.duckdb`  
**Generated:** 2026-07-23  
**Total Tables:** 146  
**Total Rows:** ~4,620,000  

---

## Table Index

### SEC Numeric Facts (2 tables)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `sec_num_2025q4` | 3,832,977 | adsh, tag, version, ddate, qtrs, uom, segments, coreg, value, footnote, cik, name, form, period, fy, fp, filed |
| `sec_num_2026q1` | 500 | (same as above) |

---

### SEC Tags (3 tables)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `sec_tags` | 103,115 | tag, version, custom, abstract, datatype, iord, crdr, tlabel, doc |
| `sec_tag_2025q4` | 84,907 | (same as above) |
| `sec_tag_2026q1` | 500 | (same as above) |

---

### SEC Submissions (17 tables)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `sec_submissions_2023q1` | 6,754 | adsh, cik, name, sic, countryba, stprba, cityba, zipba, bas1, bas2, baph, countryma, stprma, cityma, zipma, mas1, mas2, countryinc, stprinc, ein, former, changed, afs, wksi, fye, form, period, fy, fp, filed, accepted, prevrpt, detail, instance, nciks, aciks |
| `sec_submissions_2023q2` | 8,039 | (same as above) |
| `sec_submissions_2023q3` | 7,067 | (same as above) |
| `sec_submissions_2023q4` | 6,882 | (same as above) |
| `sec_submissions_2024q1` | 6,028 | (same as above) |
| `sec_submissions_2024q2` | 7,675 | (same as above) |
| `sec_submissions_2024q3` | 6,699 | (same as above) |
| `sec_submissions_2024q4` | 6,491 | (same as above) |
| `sec_submissions_2025q1` | 6,231 | (same as above) |
| `sec_submissions_2025q2` | 7,009 | (same as above) |
| `sec_submissions_2025q3` | 6,541 | (same as above) |
| `sec_submissions_2025q4` | 6,304 | (same as above) |
| `sec_submissions_2026q1` | 6,169 | (same as above) |
| `sec_sub_2025q2` | 7,009 | (same as above) |
| `sec_sub_2025q3` | 6,541 | (same as above) |
| `sec_sub_2025q4` | 1,000 | (same as above) |
| `sec_sub_2026q1` | 1,000 | (same as above) |

---

### SEC Quarterly Financials (3 tables)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `sec_quarterly_financials` | 41,710 | adsh, tag, version, ddate, qtrs, uom, segments, coreg, value, footnote, cik, name, form, period, fy, fp, filed |
| `sec_company_quarterly_derived` | 291 | cik, name, period, fy, fp, form, revenue, rd_expense, sm_expense, ga_expense, sbc, operating_income, net_income, ocf, capex, acquisitions, cash, short_term_investments, total_assets, total_liabilities, equity, deferred_rev_current, deferred_rev_noncurrent, rpo, debt_current, debt_noncurrent, lease_liab_current, lease_liab_noncurrent, capex_intensity, rd_intensity, sbc_pct_revenue, operating_margin, net_margin, ocf_to_capex, debt_to_assets, debt_to_equity, total_deferred_revenue, rpo_to_deferred_ratio, fcf_margin, total_debt, cash_and_investments, cash_to_debt |
| `sec_company_quarterly_metrics` | 291 | cik, name, form, period, fy, fp, filed, revenue, revenues_alt, revenue_incl_tax, rd_expense, sm_expense, ga_expense, sbc, operating_income, pretax_income, net_income, ocf, capex, capex_alt, acquisitions, debt_issuance, debt_repayment, share_repurchases, dividends, cash, short_term_investments, receivables, inventory, ppe_net, lease_rou_asset, intangibles, goodwill, total_assets, payables, deferred_rev_current, deferred_rev_noncurrent, rpo, debt_current, debt_noncurrent, lease_liab_current, lease_liab_noncurrent, total_liabilities, equity, segment_revenue, segment_profit |

---

### SEC Facts (13 tables)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `sec_facts_2023q1` | 3,410 | adsh, tag, version, ddate, qtrs, uom, segments, coreg, value, footnote, cik, name, form, period, fy, fp, filed |
| `sec_facts_2023q2` | 2,828 | (same as above) |
| `sec_facts_2023q3` | 3,215 | (same as above) |
| `sec_facts_2023q4` | 3,453 | (same as above) |
| `sec_facts_2024q1` | 3,315 | (same as above) |
| `sec_facts_2024q2` | 2,800 | (same as above) |
| `sec_facts_2024q3` | 3,231 | (same as above) |
| `sec_facts_2024q4` | 3,634 | (same as above) |
| `sec_facts_2025q1` | 3,358 | (same as above) |
| `sec_facts_2025q2` | 2,759 | (same as above) |
| `sec_facts_2025q3` | 3,091 | (same as above) |
| `sec_facts_2025q4` | 3,394 | (same as above) |
| `sec_facts_2026q1` | 3,222 | (same as above) |

---

### Datacenter Data (2 tables)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `global_datacenters_github` | 18,110 | name, company, city, state, country, address |
| `master_global_datacenters` | 19,694 | source, facility_name, operator, city, state_province, country, address, status, capacity_mw, capacity_category, facility_size_sqft, property_size_acres, project_cost_usd, expected_online_date, latitude, longitude, cooling_type, power_source, tenant, purpose, community_pushback, notes, source_url, date_added, last_updated |

---

### Market Data (1 table)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `equity_prices_daily` | 10,620 | ticker, date, open, high, low, close, volume, adj_close |

---

### Final Analytic Tables (3 tables)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `final_company_panel_quarterly` | 669 | cik, company_name, period, fy, fp, form, revenue, net_income, operating_income, ocf, capex, cash, total_assets, total_liabilities, debt_current, debt_noncurrent, rpo, sbc, rd_expense, capex_intensity, rd_intensity, sbc_pct_revenue, operating_margin, net_margin, ocf_to_capex, debt_to_assets, debt_to_equity, fcf_margin, cash_to_debt |
| `final_valuation_panel_quarterly` | 293 | cik, company_name, period, revenue, net_income, operating_income, cash, total_assets, total_liabilities, debt_current, debt_noncurrent, total_debt, rpo, market_cap, price_to_sales, price_to_earnings, enterprise_value |
| `sec_company_financials_derived` | 896 | cik, entity_name, revenue, net_income, operating_income, rd_expense, cash, total_assets, total_liabilities, shares_outstanding, rpo_current, rpo_noncurrent, rpo_total |

---

### SEC Company Facts (1 table)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `sec_company_facts_complete` | 14,218,546 | cik, entity_name, tag, unit, value, start, end, frame |

---

### Data Dictionary (1 table)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `data_dictionary` | 2,388 | table_name, column_name, data_type, description, source, last_updated |

---

### Water/Energy Data (1 table)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `usgs_water` | 3,223 | STATE, STATEFIPS, COUNTY, COUNTYFIPS, FIPS, YEAR, TP-TotPop, PS-GWPop, PS-SWPop, PS-TOPop, PS-WGWFr, PS-WGWSa, PS-WGWTo, PS-WSWFr, PS-WSWSa, PS-WSWTo, PS-WFrTo, PS-WSaTo, PS-Wtotl, DO-SSPop, DO-WGWFr, DO-WSWFr, DO-WFrTo, DO-SSPCp, DO-PSDel, DO-PSPCp, DO-WDelv, IN-WGWFr, IN-WGWSa, IN-WGWTo, IN-WSWFr, IN-WSWSa, IN-WSWTo, IN-WFrTo, IN-WSaTo, IN-Wtotl, IR-WGWFr, IR-WSWFr, IR-WFrTo, IR-RecWW, IR-CUsFr, IR-IrSpr, IR-IrMic, IR-IrSur, IR-IrTot, IC-WGWFr, IC-WSWFr, IC-WFrTo, IC-RecWW, IC-CUsFr, IC-IrSpr, IC-IrMic, IC-IrSur, IC-IrTot, IG-WGWFr, IG-WSWFr, IG-WFrTo, IG-RecWW, IG-CUsFr, IG-IrSpr, IG-IrMic, IG-IrSur, IG-IrTot, LI-WGWFr, LI-WSWFr, LI-WFrTo, AQ-WGWFr, AQ-WGWSa, AQ-WGWTo, AQ-WSWFr, AQ-WSWSa, AQ-WSWTo, AQ-WFrTo, AQ-WSaTo, AQ-Wtotl, MI-WGWFr, MI-WGWSa, MI-WGWTo, MI-WSWFr, MI-WSWSa, MI-WSWTo, MI-WFrTo, MI-WSaTo, MI-Wtotl, PT-WGWFr, PT-WGWSa, PT-WGWTo, PT-WSWFr, PT-WSWSa, PT-WSWTo, PT-WFrTo, PT-WSaTo, PT-Wtotl, PT-RecWW, PT-PSDel, PT-CUsFr, PT-CUsSa, PT-CUTot, PT-Power, PO-WGWFr, PO-WGWSa, PO-WGWTo, PO-WSWFr, PO-WSWSa, PO-WSWTo, PO-WFrTo, PO-WSaTo, PO-Wtotl, PO-RecWW, PO-PSDel, PO-CUsFr, PO-CUsSa, PO-CUTot, PO-Power, PC-WGWFr, PC-WGWSa, PC-WGWTo, PC-WSWFr, PC-WSWSa, PC-WSWTo, PC-WFrTo, PC-WSaTo, PC-Wtotl, PC-RecWW, PC-PSDel, PC-CUsFr, PC-CUsSa, PC-CUTot, PC-Power, TO-WGWFr, TO-WGWSa, TO-WGWTo, TO-WSWFr, TO-WSWSa, TO-WSWTo, TO-WFrTo, TO-WSaTo, TO-Wtotl, TO-CUsFrPartial, TO-CUsSaPartial, TO-CUTotPartial |

---

### AI/ML Data (12 tables)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `api_pricing` | 795 | provider, model, input_price_per_mtok, output_price_per_mtok, cached_input_price_per_mtok, context_window, date, source |
| `model_company_quarterly_derived` | 291 | cik, name, period, fy, fp, form, revenue, rd_expense, sm_expense, ga_expense, sbc, operating_income, net_income, ocf, capex, acquisitions, cash, short_term_investments, total_assets, total_liabilities, equity, deferred_rev_current, deferred_rev_noncurrent, rpo, debt_current, debt_noncurrent, lease_liab_current, lease_liab_noncurrent, capex_intensity, rd_intensity, sbc_pct_revenue, operating_margin, net_margin, ocf_to_capex, debt_to_assets, debt_to_equity, total_deferred_revenue, rpo_to_deferred_ratio, fcf_margin, total_debt, cash_and_investments, cash_to_debt |
| `model_company_quarterly_metrics` | 291 | cik, name, form, period, fy, fp, filed, revenue, revenues_alt, revenue_incl_tax, rd_expense, sm_expense, ga_expense, sbc, operating_income, pretax_income, net_income, ocf, capex, capex_alt, acquisitions, debt_issuance, debt_repayment, share_repurchases, dividends, cash, short_term_investments, receivables, inventory, ppe_net, lease_rou_asset, intangibles, goodwill, total_assets, payables, deferred_rev_current, deferred_rev_noncurrent, rpo, debt_current, debt_noncurrent, lease_liab_current, lease_liab_noncurrent, total_liabilities, equity, segment_revenue, segment_profit |
| `china_api_pricing` | 239 | provider, model, input_price_usd_per_million_tokens, output_price_usd_per_million_tokens, currency, date, source, source_url, notes |
| `huggingface_model_downloads` | 100 | model_id, date, downloads |
| `open_source_model_registry` | 100 | model_id, author, downloads, likes, last_modified |
| `training_costs` | 23 | model, organization, release_date, parameters_b, compute_flops, compute_cost_usd, training_tokens, training_time_days, gpu_type, gpu_count, training_cost_per_token, training_cost_per_flop, source |
| `gpu_economics` | 17 | provider, gpu_type, hourly_price_usd, annual_price_usd_1yr, annual_price_usd_3yr, memory_gb, memory_bandwidth_gbps, tflops_fp16, tflops_bf16, nvlink_gbps, form_factor, date, source |
| `model_benchmarks` | 16 | model, organization, benchmark, elo, ci_low, ci_high, date, category, language |
| `github_model_activity` | 4 | repo, date, stars, forks, open_issues |
| `training_runs_by_company` | 4 | model, developer, release_date, parameters_b, compute_flops |
| `gpu_order_book_proxy` | 2 | manufacturer, customer, gpu_model, estimated_units, backlog_value_usd_millions |

---

### Power/Energy Data (7 tables)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `fuel_prices` | 144 | hub, date, price_usd_mmbtu, basis_diff_usd_mmbtu, volatility_pct, source |
| `power_fuel_prices` | 144 | (same as fuel_prices) |
| `heat_rates` | 16 | unit, technology, fuel_type, heat_rate_btu_kwh, date, degradation_pct_yr, source |
| `power_heat_rates` | 16 | (same as heat_rates) |
| `hedge_ratios` | 16 | company, commodity, hedge_ratio, tenor_yr, instruments, date, source |
| `power_hedge_ratios` | 16 | (same as hedge_ratios) |
| `onsite_gen_capacity` | 25 | company, region, technology, capacity_mw, cod_year, capacity_factor, heat_rate_btu_kwh, fuel_type, deployment_source |
| `power_onsite_gen_capacity` | 23 | (same as onsite_gen_capacity) |
| `grid_services_revenue` | 28 | iso, service, price_usd_mw_yr, volume_mw, date, source |
| `grid_connection_delays` | 33 | region, iso, project_type, median_ir_to_cod_months, median_ia_to_cod_months, withdrawal_rate_pct, completion_rate_pct, total_active_gw, total_withdrawn_gw, date, source, source_url, notes |
| `transformer_shortage` | 10 | transformer_type, lead_time_weeks_2021, lead_time_weeks_2022, lead_time_weeks_2023, lead_time_weeks_2024, lead_time_weeks_2025, price_increase_pct_2020_2024, source, source_url, notes |
| `wholesale_electricity_prices` | 27 | region, iso, price_usd_per_mwh, price_type, year, source, source_url, notes |
| `carbon_prices` | 16 | jurisdiction, program, carbon_price_usd_per_ton, price_local_currency, local_currency, date, source, source_url, notes |

---

### Model Modules (15 tables)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `module_17_enterprise_contract_lag` | 11 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |
| `module_18_agentic_liability_compliance` | 16 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |
| `module_19_physical_infra_constraints` | 34 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |
| `module_20_systems_dynamics` | 81 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |
| `module_21_jevons_paradox` | 26 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |
| `module_22_open_source_commoditization` | 28 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |
| `module_23_compute_supply_cycle` | 24 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |
| `module_24_capital_market_reflexivity` | 17 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |
| `module_25_revenue_quality` | 27 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |
| `module_26_national_strategic_investment` | 25 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |
| `module_27_labor_market_transformation` | 29 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |
| `module_28_regulatory_scenario` | 28 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |
| `module_29_ai_adoption_diffusion` | 52 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |
| `module_30_global_macro_feedback` | 39 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |
| `module_31_black_swan_stress_test` | 52 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |

---

### Scenario Data (4 tables)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `scenario_matrix` | 27 | scenario_name, description, probability, pA_agentic_tco, pB_ppp_pricing, pC_phys_infra, pD_contract_cliff, pE_val_multiple, horizon_years, key_assumptions |
| `stress_scenarios` | 20 | scenario_id, scenario_name, category, probability_annual, gdp_shock_pct, unemployment_delta_pct, credit_spread_mult, equity_shock_pct, energy_shock_pct, semiconductor_shock_pct, regulation_shock, cyber_shock, ai_safety_shock, duration_quarters, correlation_structure, source |
| `historical_backtest` | 9 | episode, start_date, end_date, trigger, pre_crisis_valuation, post_crisis_valuation, peak_to_trough_pct, duration_months, recovery_months, key_drivers, model_predicted_trough, model_predicted_recovery, rmse, mae, directional_accuracy, calibration_notes |
| `module_31_black_swan_stress_test` | 52 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |
| `module_28_regulatory_scenario` | 28 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |

---

## Summary Statistics

| Category | Tables | Total Rows |
|----------|--------|------------|
| SEC Numeric Facts | 2 | 3,833,477 |
| SEC Tags | 3 | 188,522 |
| SEC Submissions | 17 | 103,439 |
| SEC Quarterly Financials | 3 | 42,292 |
| SEC Facts | 13 | 41,710 |
| Datacenter Data | 2 | 37,804 |
| Market Data | 1 | 10,620 |
| Water/Energy Data | 1 | 3,223 |
| Power/Energy Data | 11 | 404 |
| AI/ML Data | 12 | 1,882 |
| Model Modules | 15 | 370 |
| Benchmark/Data | 6 | 89 |
| Hyperscaler Data | 2 | 131 |
| Infrastructure Data | 3 | 73 |
| Valuation Data | 1 | 235 |
| Revenue Data | 1 | 155 |
| Energy Data | 3 | 93 |
| Carbon Data | 1 | 16 |
| Macro Data | 1 | 39 |
| Scenario Data | 4 | 127 |
| General Data | 45 | 26,301 |
| **TOTAL** | **140** | **~4,459,000** |

---

## Summary Statistics

| Category | Tables | Total Rows |
|----------|--------|------------|
| SEC Numeric Facts | 2 | 3,833,477 |
| SEC Tags | 3 | 188,522 |
| SEC Submissions | 17 | 103,439 |
| SEC Quarterly Financials | 3 | 42,292 |
| SEC Facts | 13 | 41,710 |
| Datacenter Data | 2 | 37,804 |
| Market Data | 1 | 10,620 |
| Water/Energy Data | 1 | 3,223 |
| Power/Energy Data | 11 | 404 |
| AI/ML Data | 12 | 1,882 |
| Model Modules | 15 | 370 |
| Benchmark/Data | 6 | 89 |
| Hyperscaler Data | 2 | 131 |
| Infrastructure Data | 3 | 73 |
| Valuation Data | 1 | 235 |
| Revenue Data | 1 | 155 |
| Energy Data | 3 | 93 |
| Carbon Data | 1 | 16 |
| Macro Data | 1 | 39 |
| Scenario Data | 4 | 127 |
| General Data | 45 | 26,301 |
| **Final Analytic Tables** | **3** | **1,858** |
| **SEC Company Facts** | **1** | **14,218,546** |
| **Data Dictionary** | **1** | **2,388** |
| **TOTAL** | **146** | **~4,620,000** |

---

## Source Databases Consolidated

| Source Database | Tables | Rows |
|-----------------|--------|------|
| `databases/all_databases_consolidated.duckdb` | 119 | ~4,300,000 |
| `DATA/tesm_54_tables.duckdb` | 22 | 15,000 |

---

## Data Quality Notes

### Issues Identified
- `sec_num_2026q1` contains only 500 rows (incomplete - needs reload from SEC DERA)
- `equity_prices_daily` covers only 12 unique tickers (limited market coverage)
- `market_cap_quarterly` has only 235 rows (limited company coverage)

### Actions Taken
- ✅ Created `final_company_panel_quarterly` - unified financials from SEC data (669 rows)
- ✅ Created `final_valuation_panel_quarterly` - valuation metrics with P/S, P/E, EV/Revenue (293 rows)
- ✅ Created `sec_company_facts_complete` - 14.2M SEC company facts from `more data/companyfacts.zip`
- ✅ Created `sec_company_financials_derived` - 896 companies with revenue, net income, assets
- ✅ Created `data_dictionary` - metadata for all tables (2,388 entries)
- ✅ Integrated SEC data from `DATA/not preprocessed/more data/companyfacts.zip` (1.29 GB)

### Publication Readiness
| Venue | Readiness |
|-------|-----------|
| Company/Team Presentation | **YES** (8.5/10) |
| Preprint | **YES** (7/10) |
| Applied Journal | **POSSIBLY** (6.5/10) |
| Top Finance/Economics | **NO** (3.5/10) |

---

## Recommendations for Improvement

1. **Reload SEC data**: `sec_num_2026q1` needs complete reload from SEC DERA
2. **Expand market data**: Add 50+ tickers for broader coverage
3. **Add private AI data**: Include OpenAI, Anthropic, xAI, etc.
4. **Create dot-com comparison**: Build IPO database and financials
5. **Add token usage**: Create actual demand/usage proxies

---

*Generated by `audit_report.py` against `databases/deduplicated_tesm_database.duckdb`*