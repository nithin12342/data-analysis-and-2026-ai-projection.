# Master Consolidated Database - Table Schema Reference

**Database:** `databases/master_consolidated.duckdb`  
**Generated:** 2026-07-16  
**Total Tables:** 106  
**Total Rows:** ~185,000  

---

## Table Index

### SEC DERA Quarterly Financials (30 tables)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `sec_company_quarterly_derived` | 291 | cik, name, period, fy, fp, form, revenue, rd_expense, sm_expense, ga_expense, sbc, operating_income, net_income, ocf, capex, acquisitions, cash, short_term_investments, total_assets, total_liabilities, equity, deferred_rev_current, deferred_rev_noncurrent, rpo, debt_current, debt_noncurrent, lease_liab_current, lease_liab_noncurrent, capex_intensity, rd_intensity, sbc_pct_revenue, operating_margin, net_margin, ocf_to_capex, debt_to_assets, debt_to_equity, total_deferred_revenue, rpo_to_deferred_ratio, fcf_margin, total_debt, cash_and_investments, cash_to_debt |
| `sec_company_quarterly_metrics` | 291 | cik, name, form, period, fy, fp, filed, revenue, revenues_alt, revenue_incl_tax, rd_expense, sm_expense, ga_expense, sbc, operating_income, pretax_income, net_income, ocf, capex, capex_alt, acquisitions, debt_issuance, debt_repayment, share_repurchases, dividends, cash, short_term_investments, receivables, inventory, ppe_net, lease_rou_asset, intangibles, goodwill, total_assets, payables, deferred_rev_current, deferred_rev_noncurrent, rpo, debt_current, debt_noncurrent, lease_liab_current, lease_liab_noncurrent, total_liabilities, equity, segment_revenue, segment_profit |
| `sec_quarterly_financials` | 41,710 | adsh, tag, version, ddate, qtrs, uom, segments, coreg, value, footnote, cik, name, form, period, fy, fp, filed |
| `sec_tags` | 103,115 | tag, version, custom, abstract, datatype, iord, crdr, tlabel, doc |
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

---

### Consolidated Module & CSV Data (74 tables)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `all_company_quarterly` | 291 | cik, name, period, fy, fp, form, revenue, rd_expense, sm_expense, ga_expense, sbc, operating_income, net_income, ocf, capex, acquisitions, cash, short_term_investments, total_assets, total_liabilities, equity, deferred_rev_current, deferred_rev_noncurrent, rpo, debt_current, debt_noncurrent, lease_liab_current, lease_liab_noncurrent, capex_intensity, rd_intensity, sbc_pct_revenue, operating_margin, net_margin, ocf_to_capex, debt_to_assets, debt_to_equity, total_deferred_revenue, rpo_to_deferred_ratio, fcf_margin, total_debt, cash_and_investments, cash_to_debt |
| `hyperscaler_capex` | 79 | name, period, fy, fp, form, revenue, capex, capex_intensity, ocf, ocf_to_capex, rd_expense, rd_intensity, sbc, sbc_pct_revenue, operating_margin, net_margin, fcf_margin |
| `semiconductor_metrics` | 160 | name, period, fy, fp, form, revenue, rd_expense, rd_intensity, capex, capex_intensity, sbc, sbc_pct_revenue, operating_margin, total_debt, cash_and_investments |
| `dc_reit_metrics` | 26 | name, period, fy, fp, form, revenue, capex, capex_intensity, total_debt, cash_and_investments, debt_to_equity, operating_margin, fcf_margin |
| `sbc_burden` | 277 | name, period, fy, fp, revenue, sbc, sbc_pct_revenue, net_income |
| `sbc_burden_full` | 277 | name, period, fy, fp, form, revenue, sbc, sbc_pct_revenue, net_income, rd_expense, rd_intensity, operating_margin |
| `rpo_deferred_revenue` | 155 | name, period, fy, fp, revenue, rpo, total_deferred_revenue, deferred_rev_current, deferred_rev_noncurrent, rpo_to_deferred_ratio |
| `deployment_counts` | 32 | company, deployment_date, agent_count, agent_type, use_case, productivity_gain_pct, cost_savings_usd, roi_multiple, source |
| `enterprise_contracts` | 15 | company, contract_type, avg_contract_length_years, renewal_rate_pct, downsizing_pct_at_renewal, expansion_pct_at_renewal, net_revenue_retention_pct, gross_revenue_retention_pct, year, source, source_url, notes |
| `vendor_reported_metrics` | 31 | vendor, metric, date, value, source, confidence |
| `api_pricing` | 31 | provider, model, input_price_per_mtok, output_price_per_mtok, cached_input_price_per_mtok, context_window, date, source |
| `inference_costs` | 25 | model, provider, input_price_per_1m_tokens, output_price_per_1m_tokens, cached_input_price_per_1m_tokens, context_window_tokens, max_output_tokens, throughput_tokens_per_sec, avg_latency_ms, hardware, utilization_pct, hw_cost_per_hour, effective_input_per_1m, effective_output_per_1m, date, source |
| `china_api_pricing` | 22 | provider, model, input_price_usd_per_million_tokens, output_price_usd_per_million_tokens, currency, date, source, source_url, notes |
| `china_benchmarks` | 26 | model, organization, benchmark, score, date, language, model_type, parameters_b, source, source_url, notes |
| `model_benchmarks` | 16 | model, organization, benchmark, elo, ci_low, ci_high, date, category, language |
| `cloud_contract_mapping` | 33 | provider, contract_type, quality_tier, price_discount_pct, commitment_term_years, upfront_option, capacity_reservation, flexibility_score, switching_cost_score, typical_customer_segment, annual_churn_pct, expansion_rate_pct, nrr_pct, date, source |
| `saas_benchmarks` | 9 | arr_band, arr_midpoint_usd, n_companies, nrr_median, grr_median, expansion_rate_median, logo_churn_median, gross_margin_median, sales_marketing_pct_rd, rd_pct_revenue, cac_months_median, ltv_cac_median, rule_of_40_median, net_income_margin_median, free_cash_flow_margin_median |
| `unit_economics_saas_benchmarks` | 9 | (same as saas_benchmarks) |
| `gpu_economics` | 17 | provider, gpu_type, hourly_price_usd, annual_price_usd_1yr, annual_price_usd_3yr, memory_gb, memory_bandwidth_gbps, tflops_fp16, tflops_bf16, nvlink_gbps, form_factor, date, source |
| `training_costs` | 23 | model, organization, release_date, parameters_b, compute_flops, compute_cost_usd, training_tokens, training_time_days, gpu_type, gpu_count, training_cost_per_token, training_cost_per_flop, source |
| `supply_chain_quarterly` | 13 | quarter, tsmc_3nm_monthly_wafers, tsmc_4nm_5nm_monthly_wafers, tsmc_cowos_monthly_wafers, tsmc_cowos_l_pct, tsmc_cowos_s_pct, nvidia_h100_shipments, amd_mi300_shipments, hbm3e_monthly_units, coWos_capacity_kwpm, coWos_demand_kwpm, gap_pct |
| `meta_analysis_studies` | 15 | study, category, intervention, industry, task_type, sample_size, effect_size_pct, ci_lower_pct, ci_upper_pct, study_design, quality_score, source, source_url, date |
| `productivity_meta_analysis` | 15 | (same as meta_analysis_studies) |
| `productivity_meta_analysis_studies` | 15 | (same as meta_analysis_studies) |
| `onet_ai_exposure` | 55 | occupation_code, occupation_title, ai_exposure_felten_2021, ai_exposure_felten_2023, language_modeling_exposure, image_generation_exposure, reasoning_exposure, automation_probability, augmentation_probability, displacement_risk, wage_2023, employment_2023, education_level, task_count, routine_task_pct, abstract_task_pct, manual_task_pct |
| `regional_infrastructure` | 13 | region, country, ppp_factor_usd_base, power_growth_cap_annual_pct, grid_connection_delay_months, gov_coordination_index, cost_per_mw_usd_millions, transformer_shortage_factor, cooling_water_availability, renewable_penetration_pct, source, source_url, notes |
| `fuel_prices` | 144 | hub, date, price_usd_mmbtu, basis_diff_usd_mmbtu, volatility_pct, source |
| `power_fuel_prices` | 144 | (same as fuel_prices) |
| `heat_rates` | 16 | unit, technology, fuel_type, heat_rate_btu_kwh, date, degradation_pct_yr, source |
| `power_heat_rates` | 16 | (same as heat_rates) |
| `hedge_ratios` | 16 | company, commodity, hedge_ratio, tenor_yr, instruments, date, source |
| `power_hedge_ratios` | 16 | (same as hedge_ratios) |
| `onsite_gen_capacity` | 25 | company, region, technology, capacity_mw, cod_year, capacity_factor, heat_rate_btu_kwh, fuel_type, deployment_source |
| `power_onsite_gen_capacity` | 23 | (same as onsite_gen_capacity) |
| `grid_services_revenue` | 22 | iso, service, price_usd_mw_yr, volume_mw, date, source |
| `grid_connection_delays` | 33 | region, iso, project_type, median_ir_to_cod_months, median_ia_to_cod_months, withdrawal_rate_pct, completion_rate_pct, total_active_gw, total_withdrawn_gw, date, source, source_url, notes |
| `transformer_shortage` | 10 | transformer_type, lead_time_weeks_2021, lead_time_weeks_2022, lead_time_weeks_2023, lead_time_weeks_2024, lead_time_weeks_2025, price_increase_pct_2020_2024, source, source_url, notes |
| `wholesale_electricity_prices` | 27 | region, iso, price_usd_per_mwh, price_type, year, source, source_url, notes |
| `carbon_prices` | 16 | jurisdiction, program, carbon_price_usd_per_ton, price_local_currency, local_currency, date, source, source_url, notes |
| `calibration_parameters` | 27 | parameter_name, calibrated_value, unit, derivation_method, source_data_files, confidence, notes |
| `technology_parameters` | 54 | technology, parameter, value, unit, source, source_url, date_accessed, notes |
| `jurisdiction_rule_matrix` | 20 | jurisdiction, regulation, tier, status, effective_date, requirements, compliance_cost_low, compliance_cost_median, compliance_cost_high, cost_unit, enforcement_probability, source |
| `stress_scenarios` | 20 | scenario_id, scenario_name, category, probability_annual, gdp_shock_pct, unemployment_delta_pct, credit_spread_mult, equity_shock_pct, energy_shock_pct, semiconductor_shock_pct, regulation_shock, cyber_shock, ai_safety_shock, duration_quarters, correlation_structure, source |
| `scenario_matrix` | 27 | scenario_name, description, probability, pA_agentic_tco, pB_ppp_pricing, pC_phys_infra, pD_contract_cliff, pE_val_multiple, horizon_years, key_assumptions |
| `historical_backtest` | 9 | episode, start_date, end_date, trigger, pre_crisis_valuation, post_crisis_valuation, peak_to_trough_pct, duration_months, recovery_months, key_drivers, model_predicted_trough, model_predicted_recovery, rmse, mae, directional_accuracy, calibration_notes |
| `master_facility_list_v3_enriched` | 52 | facility_id, facility_name, operator, tenant, hyperscaler_category, city, state_province, country, status, capacity_mw, capacity_category, expected_online_date, project_cost_usd, cooling_type, power_source, purpose, source_url, notes, tier, it_load_mw, est_gpus_h100, est_gpus_b200, est_gpus_mi300x, est_gpus_gb200_nvl72, est_racks_50kw, est_racks_100kw, est_bf16_pflops, est_fp8_pflops, utility, voltage_kv, ppa_price_mwh, generation_mix, cooling_detail, water_source_mgd, network_detail, gpu_generation, cluster_size, total_capex_billion, est_capex_per_kw, est_capex_per_gpu, source_notes, primary_gpu, est_gpu_count, training_bf16_pflops, inference_fp8_pflops, est_tokens_per_sec_billions, est_training_runs_per_year_gpt4_class, annual_power_mwh, annual_power_cost_usd, annual_revenue_potential_usd, power_cost_per_gpu_per_year, latitude, longitude |
| `master_facility_list_v2` | 52 | facility_id, facility_name, operator, tenant, hyperscaler_category, city, state_province, country, latitude, longitude, status, capacity_mw, capacity_category, expected_online_date, project_cost_usd, cooling_type, power_source, purpose, source_url, notes, tier |
| `master_facility_list` | 52 | facility_id, facility_name, operator, tenant, hyperscaler_category, city, state_province, country, status, capacity_mw, capacity_category, expected_online_date, project_cost_usd, cooling_type, power_source, purpose, source_url, notes, tier |
| `master_global_datacenters` | 19,694 | source, facility_name, operator, city, state_province, country, address, status, capacity_mw, capacity_category, facility_size_sqft, property_size_acres, project_cost_usd, expected_online_date, latitude, longitude, cooling_type, power_source, tenant, purpose, community_pushback, notes, source_url, date_added, last_updated |
| `master_capability_matrix` | 52 | facility_id, facility_name, operator, tenant, hyperscaler_category, city, state_province, country, latitude, longitude, status, tier, capacity_mw, capacity_category, expected_online_date, it_load_mw, primary_gpu, est_gpu_count, cluster_size, training_bf16_pflops, inference_fp8_pflops, est_tokens_per_sec_billions, est_training_runs_per_year_gpt4_class, utility, voltage_kv, ppa_price_mwh, generation_mix, annual_power_mwh, annual_power_cost_usd, power_cost_per_gpu_per_year, cooling_detail, water_source_mgd, network_detail, gpu_generation, cluster_size, total_capex_billion, est_capex_per_kw, est_capex_per_gpu, annual_revenue_potential_usd, source_notes, notes |
| `key_hyperscale_projects` | 52 | source, facility_name, operator, city, state_province, country, status, capacity_mw, capacity_category, facility_size_sqft, property_size_acres, project_cost_usd, expected_online_date, tenant, purpose, notes, source_url, last_updated |
| `hyperscaler_focused_projects` | 52 | hyperscaler_category, facility_name, operator, tenant, city, state_province, country, status, capacity_mw, capacity_category, expected_online_date, project_cost_usd, cooling_type, power_source, purpose, source_url |
| `facility_financials` | 40 | facility_id, name, hyperscaler, capacity_mw, status, tier, capex_billion, gpus, inference_pflops, training_pflops, annual_power_cost_million, revenue_billion_45util, ebitda_billion_45util, roic_45util |
| `fractracker_us_datacenters` | 1,603 | facility_name, address, city, state, zip, county, lat, long, status, location_confidence, purpose, operator_name, tenant, mw, sizerank, power_source, dedicated_power_plant, number_of_generators, number_of_buildings, cooling_source, cooling_type, facility_size_sqft, property_size_acres, project_cost, expected_date_online, community_pushback, advocacy_information, resistance_status, nda, community_group_website_1, community_group_website_2, petition_url, other_info, information_source, info_source_1, info_source_2, info_source_3, info_source_4, info_source_5, info_source_6, info_source_7, info_source_8, date_created, date_updated |
| `global_datacenters_github` | 18,110 | name, company, city, state, country, address |
| `data_lineage_log` | 1,607 | facility_id, facility_name, field, value, source_type, confidence, primary_source |
| `gap_uncertainty_register` | 534 | facility_id, facility_name, missing_field, impact, suggested_source |
| `fred_core_series` | 18 | series_id, title, units, frequency, last_value, last_date, source |
| `fred_series_catalog` | 23 | series_id, series_name, frequency, units, source, last_updated |

---

### Module Parameter Tables (15 tables)

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

### Model Tables (2 tables)

| Table | Rows | Key Columns |
|-------|------|-------------|
| `model_company_quarterly_derived` | 291 | (same as sec_company_quarterly_derived) |
| `model_company_quarterly_metrics` | 291 | (same as sec_company_quarterly_metrics) |

---

## Summary Statistics

| Category | Tables | Total Rows |
|----------|--------|------------|
| SEC DERA (facts, submissions, tags, model) | 30 | ~140,000 |
| Consolidated CSV/Module data | 74 | ~44,000 |
| Model duplicates | 2 | 582 |
| **TOTAL** | **106** | **~185,000** |

---

## Master Views (3 views)

| View | Description |
|------|-------------|
| `master.company_financials` | Unified financials for all 23 SEC companies (291 quarters) |
| `master.hyperscaler_summary` | Aggregated CapEx, R&D, SBC, FCF for 6 hyperscalers |
| `master.semiconductor_summary` | Aggregated metrics for 13 semiconductor companies |

---

*Generated by `query_tables.py` against `databases/master_consolidated.duckdb`*