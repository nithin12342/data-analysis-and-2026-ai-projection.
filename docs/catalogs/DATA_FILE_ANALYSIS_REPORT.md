# Comprehensive Data File Analysis Report

**Generated:** 2026-07-15T16:42:10.006698
**Root Directory:** `C:\Users\NITHING\Desktop\projections`

## Executive Summary

- **Total Files Analyzed:** 90
- **Total Size:** 8.81 MB
- **CSV Files:** 70 (8.12 MB)
- **Non-CSV Files:** 20 (0.69 MB)

### Non-CSV Files by Extension

| Extension | Count |
|-----------|-------|
| .md | 10 |
| .py | 8 |
| .js | 2 |

## CSV File Analysis

### `fractracker_us_datacenters.csv`

- **Size:** 0.69 MB (728,322 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 1,603
- **Columns:** 44

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 23 | state, status, location_confidence, purpose, tenant, sizerank, power_source, dedicated_power_plant, number_of_generators, number_of_buildings, cooling_source, cooling_type, expected_date_online, community_pushback, advocacy_information, resistance_status, nda, community_group_website_2, information_source, info_source_5, info_source_6, info_source_7, info_source_8 |
| Numeric | 4 | zip, lat, long, property_size_acres |
| Date | 0 | — |
| Text | 17 | facility_name, address, city, county, operator_name, mw, facility_size_sqft, project_cost, community_group_website_1, petition_url, other_info, info_source_1, info_source_2, info_source_3, info_source_4, date_created, date_updated |

#### Category Column Details

**state** — Unique values: 51, Nulls: 1
**status** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| Proposed | 729 |
| Operating | 529 |
| Approved/Permitted/Under construction | 159 |
| Cancelled | 65 |
| Expanding | 60 |
| Suspended | 59 |
| Pre-proposal | 2 |

**location_confidence** — Unique values: 6, Nulls: 5

| Value | Count |
|-------|-------|
| High | 1261 |
| Medium | 282 |
| Low | 49 |
| Medium  | 3 |
| High  | 2 |
| high  | 1 |

**purpose** — Unique values: 27, Nulls: 1529

| Value | Count |
|-------|-------|
| AI | 40 |
| Crypto | 5 |
| Bitcoin transitioning to AI | 3 |
| AI Data center and solar fam | 2 |
| Bitcoin | 2 |
| Telecom / network data center | 1 |
| AI/cloud-computing | 1 |
| cloud services | 1 |
| Colocation / enterprise data center | 1 |
| Hyperscale cloud data-center campus | 1 |
| Cryptocurrency mining data center | 1 |
| AI "superfactory" | 1 |
| Hyperscale Cloud & AI Workloads | 1 |
| Telecommunication routing | 1 |
| AI and Bitcoin | 1 |

**tenant** — Unique values: 2, Nulls: 1601

| Value | Count |
|-------|-------|
| Multiple colocation tenants | 1 |
| Anthropic | 1 |

**sizerank** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| Unknown | 892 |
| Hyperscale (100-999 MW) | 340 |
| Medium (11-50 MW) | 120 |
| Mega campus (>1,000 MW) | 113 |
| Small (0-10 MW) | 100 |
| Large (51-99 MW) | 37 |
| Hyperscale (101-999 MW) | 1 |

**power_source** — Unique values: 21, Nulls: 1487

| Value | Count |
|-------|-------|
| Grid (unspecified mix) | 45 |
| Natural gas | 35 |
| Hybrid (onsite and grid) | 6 |
| Solar | 5 |
| Nuclear | 4 |
| Oil/Diesel | 2 |
| Coal | 2 |
| Natural gas, Hybrid (onsite and grid) | 2 |
| Solar, Grid (unspecified mix) | 2 |
| Fuel Cells | 2 |
| Solar, Grid (unspecified mix), Natural gas | 1 |
| Hydroelectric | 1 |
| Biomass | 1 |
| Hydroelectric, Grid (unspecified mix) | 1 |
| Wind, Solar | 1 |

**dedicated_power_plant** — Unique values: 22, Nulls: 1571

| Value | Count |
|-------|-------|
| Yes | 11 |
| Salt River Project (SRP) substation | 1 |
| May use jet engines from retired military planes | 1 |
| Georgia Power | 1 |
| EW Brown Generation Station | 1 |
| 2 | 1 |
| Northwestern Energy | 1 |
| Yes  | 1 |
| Yes - Apollo Generating Station | 1 |
| Yes - fuel cell system | 1 |
| Yes - Bluegrass Power Station | 1 |
| Yes - PowerConneX I, II, and III New Albany Energy Center | 1 |
| Yes - Socrates North Power Generation Project | 1 |
| Yes - Homer City Generating Station | 1 |
| Yes - Greene County Power Station | 1 |

**number_of_generators** — Unique values: 13, Nulls: 1590

| Value | Count |
|-------|-------|
| 25 2.5MW emergency generators for redundancy purposes | 1 |
| 100 natural gas-powered backup emergency generators connected to Southern California Gas Company’s high-pressure gas line | 1 |
| 14 on-site diesel generators | 1 |
| 15 | 1 |
| 516 | 1 |
| 0 | 1 |
| 12-24 | 1 |
| 1.2 GW diesel | 1 |
| 12 | 1 |
| 6 | 1 |
| 158 diesel backup generators | 1 |
| 115 diesel-fueled generators | 1 |
| 813 | 1 |

**number_of_buildings** — Unique values: 43, Nulls: 1406

| Value | Count |
|-------|-------|
| 2 | 26 |
| 3 | 25 |
| 6 | 23 |
| 4 | 18 |
| 5 | 12 |
| 10 | 11 |
| 7 | 10 |
| 12 | 8 |
| 8 | 8 |
| 9 | 6 |
| 14 | 5 |
| 1 | 3 |
| 15 | 3 |
| 30 | 3 |
| 20 | 3 |

**cooling_source** — Unique values: 3, Nulls: 1553

| Value | Count |
|-------|-------|
| Water | 31 |
| Air | 16 |
| Hybrid air/water | 3 |

**cooling_type** — Unique values: 3, Nulls: 1541

| Value | Count |
|-------|-------|
| Closed loop | 58 |
| Fans | 2 |
| Open loop | 2 |

**expected_date_online** — Unique values: 16, Nulls: 1470

| Value | Count |
|-------|-------|
| 2027 | 48 |
| 2028 | 27 |
| 2026 | 23 |
| 2030 | 12 |
| 2029 | 8 |
| 2025 | 3 |
| 2032 | 2 |
| 2027-28 | 2 |
| Full buildout by 2037 | 1 |
| Full buildout by 2035 | 1 |
| 2036 | 1 |
| Buildout by 2028 | 1 |
| 2024 | 1 |
| 20027 | 1 |
| 2035 | 1 |

**community_pushback** — Unique values: 3, Nulls: 11

| Value | Count |
|-------|-------|
| Unknown | 1330 |
| Yes | 260 |
| Yes  | 2 |

**advocacy_information** — Unique values: 63, Nulls: 1539
**resistance_status** — Unique values: 3, Nulls: 1520

| Value | Count |
|-------|-------|
| Organized Advocacy | 58 |
| Emerging Concern | 23 |
| Unknown | 2 |

**nda** — Unique values: 8, Nulls: 1592

| Value | Count |
|-------|-------|
| Yes | 4 |
| Bessemer Mayor Kenneth Gulley, the city attorney, and other city leaders signed NDAs | 1 |
| Yes- https://www.al.com/news/2025/10/secrecy-agreements-fuel-pushback-of-14-billion-alabama-data-center.html | 1 |
| Active (Tenant identity legally shielded) | 1 |
| No | 1 |
| Every elected official is under an NDA including the Montana Public Service Commission | 1 |
| Officials knew of the Meta plan as “Project Accordion” for more than a year before it was officially announced | 1 |
| Marion County officials confirmed that the council signed a nondisclosure agreement | 1 |

**community_group_website_2** — Unique values: 32, Nulls: 1570

| Value | Count |
|-------|-------|
| https://wvrivers.org/ | 2 |
| https://www.facebook.com/groups/740748888833453 | 1 |
| https://www.facebook.com/groups/4339680782970126 | 1 |
| https://www.facebook.com/groups/1117995533656453 | 1 |
| https://www.facebook.com/profile.php?id=61585975718358 | 1 |
| https://www.nodatacentermpk.org/ | 1 |
| https://www.facebook.com/groups/942876081944302/ | 1 |
| https://www.facebook.com/groups/1397482882419331/ | 1 |
| https://www.facebook.com/groups/1359906715176907/ | 1 |
| https://www.swarmatl.org/ | 1 |
| https://www.facebook.com/groups/1469043077373264/ | 1 |
| https://www.facebook.com/groups/882581394736535/ | 1 |
| https://www.gofundme.com/f/defend-hobarts-future-no-data-centers | 1 |
| https://capitalbnews.org/meta-richland-parish-ai-data-center/ | 1 |
| https://www.facebook.com/groups/283244782323144/ | 1 |

**information_source** — Unique values: 6, Nulls: 0

| Value | Count |
|-------|-------|
| Media Monitoring | 1021 |
| PEC | 386 |
| Sci4GA | 104 |
| Crowdsourced | 51 |
| Other | 39 |
| FOIA/ public records request | 2 |

**info_source_5** — Unique values: 72, Nulls: 1530
**info_source_6** — Unique values: 44, Nulls: 1559

| Value | Count |
|-------|-------|
| https://www.datacenterdynamics.com/en/news/alabamas-planned-14bn-project-marvel-data-center-could-double-in-size/ | 1 |
| https://news.azpm.org/p/azpmnews/2026/5/28/229919-arizona-water-officials-approve-wells-tied-to-project-blue-data-center/ | 1 |
| https://wgxa.tv/news/local/environmental-advocate-urges-twiggs-county-to-reject-data-center-plans-near-ocmulgee-river | 1 |
| https://www.indystar.com/story/news/local/marion-county/2025/09/22/google-withdraws-controversial-data-center-in-franklin-township-indianapolis-city-county-council/86165695007/ | 1 |
| https://wsbt.com/news/local/st-joseph-county-council-denies-rezoning-of-land-for-data-center-votes-7-2-marathon-meeting-hours-long-public-opinion-13-billion-dollar-project-amazon-new-carlisle-approval-process-plan-commission-st-joseph-county-indiana | 1 |
| https://epoch.ai/data/data-centers/satellite-explorer/AnthropicAmazonProjectRainierNewCarlisleIndiana?ref=404media.co | 1 |
| https://www.lpm.org/news/2025-06-03/oldham-county-data-center-switches-sites-reduces-size-amid-local-resistance | 1 |
| https://www.bgr.com/1990532/meta-new-aid-data-center-size-70-football-fields-residents-scared-water/ | 1 |
| https://www.cbsnews.com/boston/news/inside-lowell-markley-data-center | 1 |
| https://www.whmi.com/news/article/developers-withdraw-re-zoning-application-for-proposed-data-center-in-howell-twp?fbclid=IwY2xjawOjxD5leHRuA2FlbQIxMABicmlkETFGTWdNTnFwVzhHUFAxcXRrc3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHqbt42SjPESM_B2BmdYNZGnBkWqqW2rX4bXuiVk3lYnyLj84qbo_n3pDm2Yp_aem_SOH2yzjxxo5bOquwuYeBEw | 1 |
| https://www.crainsdetroit.com/technology/cdb-anthropic-projectflex-datacenter-20260414/?utm_id=gfta-ur-260414&share-code=F4JNH5GIING7NDXCBOJBJ5QVZM&user_id=9885400&customer_secondary_source=cdb_articleGifting&fbclid=IwdGRjcARLdD9jbGNrBEt0NmV4dG4DYWVtAjExAHNydGMGYXBwX2lkDDM1MDY4NTUzMTcyOAABHuy4NDQbhkRm0MqYKNA8xHVyzE_IEbw7Q63iYC4OtY7wS2VOuDb-HW1V_hun_aem_aeBEd6Vy6DKHXUxdtutdIw | 1 |
| https://planetdetroit.org/2026/02/saline-data-center-air-wetlands-permits/ | 1 |
| https://planetdetroit.org/2026/03/google-dte-data-center-van-buren/ | 1 |
| https://www.mprnews.org/story/2025/10/22/hermantown-delays-permits-for-disputed-data-center | 1 |
| https://elpasomatters.org/2025/09/25/stargate-open-ai-oracle-project-jupiter-data-center-dona-ana-new-mexico-el-paso-texas/ | 1 |

**info_source_7** — Unique values: 25, Nulls: 1578

| Value | Count |
|-------|-------|
| https://abc3340.com/news/abc-3340-news-iteam/bessemer-unveils-revised-project-marvel-data-center-campus-plan-amid-ongoing-controversy | 1 |
| https://www.41nbc.com/twiggs-county-data-center-rezoning-approval/ | 1 |
| https://lailluminator.com/briefs/entergy-builds-power-plant-for-data-center/ | 1 |
| https://www.whmi.com/news/article/vangilder-family-farm-data-center | 1 |
| https://www.datacenterdynamics.com/en/news/or/ | 1 |
| https://www.datacenterdynamics.com/en/news/google-confirms-1gw-data-center-campus-near-detroit-michigan-partners-with-dte-energy-on-27gw-power-generation/ | 1 |
| https://www.mprnews.org/story/2025/11/14/hermantown-data-center-developer-plans-public-meeting | 1 |
| https://www.datacenterdynamics.com/en/news/groups-sue-to-stall-data-center-project-in-do%C3%B1a-ana-county-new-mexico/ | 1 |
| https://truthout.org/articles/new-york-residents-are-fighting-a-data-center-backed-by-a-billionaire-trump-ally/ | 1 |
| https://www.ithaca.com/news/lansing/flx-strong-clean-file-lawsuit-against-lansing-zba-terawulf-to-block-data-center/article_97b45f0f-c849-497c-9daa-6040f1f1710b.html | 1 |
| https://oilandgaswatch.org/facility/rec_d5eiru1uih89upkga2qg | 1 |
| https://www.journal-news.com/news/residents-say-no-on-1b-data-center-project-wants-hamilton-to-do-the-same/L3YUSLLR2VHMDFXVBXKPBTOHCA/ | 1 |
| https://oilandgaswatch.org/facility/rec_d4f1u60q7easr8ra1g30 | 1 |
| https://paenvironmentdaily.blogspot.com/2025/12/dep-to-host-jan-6-public-information.html | 1 |
| https://www.spotlightpa.org/news/2026/03/pennsylvania-data-centers-archbald-ai-evictions-environment/?utm_source=ActiveCampaign&utm_medium=email&utm_content=6%20data%20centers%20%20One%20PA%20borough&utm_campaign=PA%20Post%2003%2019%2026%20%28Copy%29 | 1 |

**info_source_8** — Unique values: 14, Nulls: 1589

| Value | Count |
|-------|-------|
| https://insideclimatenews.org/news/13112025/proposed-alabama-data-center-clashes-with-northern-beltline-birmingham-darter/ | 1 |
| https://www.41nbc.com/twiggs-county-data-center-rezoning-approval/ | 1 |
| https://www.datacenterdynamics.com/en/news/meta-purchases-additional-1400-acres-for-hyperion-mega-data-center-expansion/ | 1 |
| https://planetdetroit.org/2025/12/billion-dollar-data-center-paused/ | 1 |
| https://www.datacenterdynamics.com/en/news/google-confirms-it-is-behind-403-acre-data-center-campus-in-hermantown-minnesota/ | 1 |
| https://www.datacenterdynamics.com/en/news/oracle-revealed-as-tenant-of-project-jupiter-data-center-campus-in-new-mexico/ | 1 |
| https://www.nytimes.com/2026/03/17/nyregion/ai-data-center-new-york.html | 1 |
| https://bgindependentmedia.org/meta-data-center-how-it-went-from-economic-development-coup-to-project-local-residents-rue/ | 1 |
| https://www.wvxu.org/environment/2025-12-03/developers-data-center-butler-county | 1 |
| https://www.wvia.org/news/local/2026-05-01/fast-track-no-more-pa-kicks-archbald-data-center-campus-off-permit-program | 1 |
| https://www.datacenterdynamics.com/en/news/shippingport-industrial-park/ | 1 |
| https://www.datacenterdynamics.com/en/news/riot-platforms-files-to-add-building-to-cryptomine-and-data-center-campus-in-corsicana-texas/ | 1 |
| https://www.wisn.com/article/whats-that-sound-its-mount-pleasants-new-ai-data-center/70850595 | 1 |
| https://www.datacenterdynamics.com/en/news/vantage-tops-out-second-building-at-openais-lighthouse-campus-in-wisconsin/ | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| zip | 42285.76 | 25908.90 | 1085.00 | 99734.00 | 30294.00 |
| lat | 37.68 | 4.21 | 21.48 | 70.18 | 38.76 |
| long | -87.35 | 12.57 | -158.02 | -67.02 | -84.06 |
| property_size_acres | 460.38 | 2001.15 | 1.00 | 40000.00 | 117.00 |

#### Sample Data (First 3 Rows)

| facility_name | address | city | state | zip | county | lat | long | status | location_confidence | purpose | operator_name | tenant | mw | sizerank | power_source | dedicated_power_plant | number_of_generators | number_of_buildings | cooling_source | cooling_type | facility_size_sqft | property_size_acres | project_cost | expected_date_online | community_pushback | advocacy_information | resistance_status | nda | community_group_website_1 | community_group_website_2 | petition_url | other_info | information_source | info_source_1 | info_source_2 | info_source_3 | info_source_4 | info_source_5 | info_source_6 | info_source_7 | info_source_8 | date_created | date_updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Global Stack Data Center | nan | nan | nan | nan | Napa | 38.585007 | -122.58886 | Proposed | Medium | nan | Global Stack/ Edge | nan | 10 | Small (0-10 MW) | nan | nan | nan | nan | nan | nan | nan | 70.0 | nan | nan | Yes | nan | Emerging Concern | nan | nan | nan | nan | nan | Media Monitoring | https://www.datacenterdynamics.com/en/news/develop | https://calistoga.civicweb.net/document/116181/Glo | nan | nan | nan | nan | nan | nan | 06/29/2026 | 06/29/2026 |
| Stak Energy Data Center | Dalton Hwy, 26 miles south of Deadhorse | North Slope Borough | AK | nan | North Slope | 69.90071 | -148.81477 | Proposed | Medium | nan | Stak | nan | 3000 | Mega campus (>1,000 MW) | Natural gas | Yes | nan | nan | nan | nan | nan | 715.0 | nan | 2028 | Unknown | nan | nan | nan | nan | nan | nan | nan | Media Monitoring | https://www.datacenterdynamics.com/en/news/stak-en | https://www.cbc.ca/news/canada/north/yukon-alaska- | nan | nan | nan | nan | nan | nan | 05/20/2026 | 06/24/2026 |
| Prudhoe Bay Data Center | Dalton Hwy | Prudhoe Bay | AK | 99734.0 | North Slope | 70.18478 | -148.44 | Operating | Medium | nan | Far North Digital, LLC | nan | 120 | Hyperscale (100-999 MW) | nan | nan | nan | nan | Air | nan | nan | 100.0 | nan | nan | Unknown | nan | nan | nan | nan | nan | nan | nan | Media Monitoring | https://www.fn-digital.com/data-center | https://www.datacenterdynamics.com/en/news/stak-en | nan | nan | nan | nan | nan | nan | 05/20/2026 | 05/20/2026 |

---

### `global_datacenters_github.csv`

- **Size:** 1.64 MB (1,719,488 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 18,110
- **Columns:** 6

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 0 | — |
| Numeric | 0 | — |
| Date | 0 | — |
| Text | 6 | name, company, city, state, country, address |

#### Sample Data (First 3 Rows)

| name | company | city | state | country | address |
| --- | --- | --- | --- | --- | --- |
| NAP de las Americas Madrid | Terremark | Madrid | nan | Spain | Calle de Yecora, 4 28009 Madrid Spain |
| Central Office 2 | StarHub Ltd. | Singapore | nan | Singapore | 19 Tai Seng Dr 535222 Singapore Singapore |
| Cluj-Napoca | GTS Telecom SRL | Cluj-Napoca | nan | Romania | Str. Garii nr. 21 400267 Cluj-Napoca Romania |

---

### `DATA\calibration_parameters.csv`

- **Size:** 0.0 MB (4,337 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 27
- **Columns:** 7

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 2 | unit, source_data_files |
| Numeric | 2 | calibrated_value, confidence |
| Date | 0 | — |
| Text | 3 | parameter_name, derivation_method, notes |

#### Category Column Details

**unit** — Unique values: 13, Nulls: 0

| Value | Count |
|-------|-------|
| fraction | 11 |
| quarters | 2 |
| per_year | 2 |
| x | 2 |
| per_quarter | 2 |
| USD_billions_per_quarter | 1 |
| MW | 1 |
| USD_per_MWh_per_USD_per_MMBtu | 1 |
| USD_per_MW_yr | 1 |
| ton_CO2_per_MWh | 1 |
| USD_per_MWh_per_50USD_ton | 1 |
| L_per_MWh | 1 |
| multiplier | 1 |

**source_data_files** — Unique values: 15, Nulls: 0

| Value | Count |
|-------|-------|
| onsite_gen_capacity.csv | 5 |
| enterprise_contracts.csv | 4 |
| macro_data.csv | 4 |
| grid_connection_delays.csv | 2 |
| technology_parameters.csv + onsite_gen_capacity.csv | 2 |
| transformer_shortage.csv | 1 |
| usitc_data.csv | 1 |
| sec_financials.csv | 1 |
| technology_parameters.csv + heat_rates.csv | 1 |
| hedge_ratios.csv | 1 |
| grid_services_revenue.csv | 1 |
| carbon_prices.csv | 1 |
| technology_parameters.csv | 1 |
| productivity_meta_analysis.csv | 1 |
| real_historical_trails.csv | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| calibrated_value | 1685.41 | 7687.56 | 0.00 | 39773.00 | 0.85 |
| confidence | 0.80 | 0.07 | 0.70 | 0.95 | 0.80 |

#### Sample Data (First 3 Rows)

| parameter_name | calibrated_value | unit | derivation_method | source_data_files | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- |
| gridConnectionDelay | 10.0 | quarters | LBNL Queued Up 2025 median IR-to-COD all regions/t | grid_connection_delays.csv | 0.85 | Ceiling of mean queue quarters across ISOs |
| powerGrowthCap | 0.12 | per_year | 1 - (withdrawal_rate/100) from LBNL 2025; US weigh | grid_connection_delays.csv | 0.8 | US completion rate ~13% → cap ~12%/yr |
| transformerShortage | 0.29 | fraction | NIAC 2024: 120 weeks lead time vs 50 pre-pandemic  | transformer_shortage.csv | 0.75 | Severity index 0-1 |

---

### `DATA\carbon_prices.csv`

- **Size:** 0.0 MB (2,838 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 16
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 7 | jurisdiction, program, local_currency, date, source, source_url, notes |
| Numeric | 2 | carbon_price_usd_per_ton, price_local_currency |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**jurisdiction** — Unique values: 10, Nulls: 0

| Value | Count |
|-------|-------|
| eu | 3 |
| california | 3 |
| rggi | 3 |
| uk | 1 |
| canada | 1 |
| quebec | 1 |
| china | 1 |
| korea | 1 |
| new_zealand | 1 |
| washington | 1 |

**program** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| cap_and_trade | 4 |
| eu_ets | 3 |
| rggi | 3 |
| uk_ets | 1 |
| federal_fuel_charge | 1 |
| national_ets | 1 |
| k_ets | 1 |
| nz_ets | 1 |
| cca | 1 |

**local_currency** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| USD | 7 |
| EUR | 3 |
| CAD | 2 |
| GBP | 1 |
| CNY | 1 |
| KRW | 1 |
| NZD | 1 |

**date** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| 2024 | 8 |
| 2024-05 | 2 |
| 2023 | 1 |
| 2025-06 | 1 |
| 2024-11 | 1 |
| 2024-01 | 1 |
| 2024-06 | 1 |
| 2024-03 | 1 |

**source** — Unique values: 12, Nulls: 0

| Value | Count |
|-------|-------|
| ESMA Carbon Markets Report 2025 | 3 |
| CARB Auction Results | 3 |
| RGGI Annual Report 2024 | 1 |
| RGGI Auction 64 | 1 |
| RGGI Auction 63 | 1 |
| UK ETS Authority | 1 |
| Environment Canada | 1 |
| CARB Joint Auction | 1 |
| China Carbon Market | 1 |
| Korea Exchange | 1 |
| NZ ETS | 1 |
| WA Ecology | 1 |

**source_url** — Unique values: 13, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.esma.europa.eu/sites/default/files/2025-10/ESMA50-481369926-30552_Carbon_Markets_Report_2025.pdf | 3 |
| https://ww2.arb.ca.gov/sites/default/files/2024-02/nc-feb_2024_summary_results_report.pdf | 2 |
| https://ww2.arb.ca.gov/news/california-and-quebec-release-summary-results-40th-joint-cap-and-trade-allowance-auction | 1 |
| https://ww2.arb.ca.gov/ | 1 |
| https://www.rggi.org/sites/default/files/Uploads/Market-Monitor/Annual-Reports/MM_2024_Annual_Report.pdf | 1 |
| https://www.rggi.org/sites/default/files/Uploads/Auction-Materials/64/PR060724_Auction64.pdf | 1 |
| https://www.rggi.org/sites/default/files/Uploads/Auction-Materials/63/Auction_63_Market_Monitor_Report.pdf | 1 |
| https://www.gov.uk/government/organisations/uk-emissions-trading-scheme-authority | 1 |
| https://www.canada.ca/en/environment-climate-change.html | 1 |
| https://www.mee.gov.cn/ | 1 |
| https://www.krx.co.kr/ | 1 |
| https://www.epa.govt.nz/ | 1 |
| https://ecology.wa.gov/ | 1 |

**notes** — Unique values: 16, Nulls: 0

| Value | Count |
|-------|-------|
| 2024 average EUR 64.76/t; 2025 YTD avg ~EUR 73 | 1 |
| 2023 average | 1 |
| Spot price June 2025 | 1 |
| May 2024 auction settlement $38.35; Feb $41.76 | 1 |
| Nov 2024 auction $30.24 current vintage | 1 |
| Floor price $24.04 2024 | 1 |
| Volume-weighted avg auction clearing price $20.17 2024 | 1 |
| Auction 64 clearing $21.03 | 1 |
| Auction 63 clearing $16.00 (CCR triggered) | 1 |
| 2024 average ~GBP 35-40; linked to EU ETS historically | 1 |
| Federal carbon price CAD 80/tCO2e 2024; rising to CAD 170 by 2030 | 1 |
| Linked with California; same settlement price CAD | 1 |
| 2024 average ~CNY 85/t; power sector only; expanding to steel/cement | 1 |
| 2024 average ~KRW 24,000/t; phase 3 (2021-2025) | 1 |
| 2024 average ~NZD 55/t | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| carbon_price_usd_per_ton | 40.62 | 23.53 | 12.00 | 84.00 | 36.50 |
| price_local_currency | 1545.56 | 5987.90 | 16.00 | 24000.00 | 51.00 |

#### Sample Data (First 3 Rows)

| jurisdiction | program | carbon_price_usd_per_ton | price_local_currency | local_currency | date | source | source_url | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| eu | eu_ets | 70 | 65 | EUR | 2024 | ESMA Carbon Markets Report 2025 | https://www.esma.europa.eu/sites/default/files/202 | 2024 average EUR 64.76/t; 2025 YTD avg ~EUR 73 |
| eu | eu_ets | 82 | 77 | EUR | 2023 | ESMA Carbon Markets Report 2025 | https://www.esma.europa.eu/sites/default/files/202 | 2023 average |
| eu | eu_ets | 84 | 79 | EUR | 2025-06 | ESMA Carbon Markets Report 2025 | https://www.esma.europa.eu/sites/default/files/202 | Spot price June 2025 |

---

### `DATA\china_api_pricing.csv`

- **Size:** 0.0 MB (2,182 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 22
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 6 | provider, currency, date, source, source_url, notes |
| Numeric | 2 | input_price_usd_per_million_tokens, output_price_usd_per_million_tokens |
| Date | 0 | — |
| Text | 1 | model |

#### Category Column Details

**provider** — Unique values: 12, Nulls: 0

| Value | Count |
|-------|-------|
| zhipu_ai | 3 |
| alibaba | 3 |
| baichuan | 2 |
| zero_one_ai | 2 |
| tencent | 2 |
| bytedance | 2 |
| deepseek | 2 |
| openai | 2 |
| moonshot | 1 |
| minimax | 1 |
| anthropic | 1 |
| google | 1 |

**currency** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| USD | 22 |

**date** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2024-11 | 22 |

**source** — Unique values: 12, Nulls: 0

| Value | Count |
|-------|-------|
| Zhipu AI Platform | 3 |
| Alibaba Cloud DashScope | 3 |
| Baichuan Platform | 2 |
| 01.ai Platform | 2 |
| Tencent Cloud | 2 |
| VolcEngine | 2 |
| DeepSeek Platform | 2 |
| OpenAI API | 2 |
| Moonshot Platform | 1 |
| Minimax Platform | 1 |
| Anthropic API | 1 |
| Google AI Studio | 1 |

**source_url** — Unique values: 12, Nulls: 0

| Value | Count |
|-------|-------|
| https://open.bigmodel.cn/ | 3 |
| https://dashscope.aliyuncs.com/ | 3 |
| https://platform.baichuan-ai.com/ | 2 |
| https://platform.01.ai/ | 2 |
| https://cloud.tencent.com/ | 2 |
| https://www.volcengine.com/ | 2 |
| https://platform.deepseek.com/ | 2 |
| https://platform.openai.com/docs/pricing | 2 |
| https://platform.moonshot.cn/ | 1 |
| https://api.minimax.chat/ | 1 |
| https://docs.anthropic.com/claude/reference/pricing | 1 |
| https://ai.google.dev/pricing | 1 |

**notes** — Unique values: 3, Nulls: 19

| Value | Count |
|-------|-------|
| ~1 RMB/M tokens input/output | 1 |
| Lite version | 1 |
| Input $0.14, Output $0.28 | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| input_price_usd_per_million_tokens | 0.41 | 0.80 | 0.03 | 3.00 | 0.13 |
| output_price_usd_per_million_tokens | 1.50 | 3.79 | 0.03 | 15.00 | 0.15 |

#### Sample Data (First 3 Rows)

| provider | model | input_price_usd_per_million_tokens | output_price_usd_per_million_tokens | currency | date | source | source_url | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| zhipu_ai | glm_4 | 0.14 | 0.14 | USD | 2024-11 | Zhipu AI Platform | https://open.bigmodel.cn/ | ~1 RMB/M tokens input/output |
| zhipu_ai | glm_4v | 0.28 | 0.28 | USD | 2024-11 | Zhipu AI Platform | https://open.bigmodel.cn/ | nan |
| zhipu_ai | glm_4_air | 0.07 | 0.07 | USD | 2024-11 | Zhipu AI Platform | https://open.bigmodel.cn/ | Lite version |

---

### `DATA\china_benchmarks.csv`

- **Size:** 0.0 MB (3,084 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 26
- **Columns:** 11

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 9 | organization, benchmark, date, language, model_type, parameters_b, source, source_url, notes |
| Numeric | 1 | score |
| Date | 0 | — |
| Text | 1 | model |

#### Category Column Details

**organization** — Unique values: 12, Nulls: 0

| Value | Count |
|-------|-------|
| alibaba | 7 |
| zhipu_ai | 3 |
| zero_one_ai | 2 |
| deepseek | 2 |
| baichuan | 2 |
| openai | 2 |
| anthropic | 2 |
| meta | 2 |
| minimax | 1 |
| moonshot | 1 |
| google | 1 |
| nvidia | 1 |

**benchmark** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| lmsys_chatbot_arena | 26 |

**date** — Unique values: 10, Nulls: 0

| Value | Count |
|-------|-------|
| 2024-09 | 6 |
| 2024-05 | 5 |
| 2024-07 | 4 |
| 2024-06 | 3 |
| 2024-08 | 3 |
| 2024-11 | 1 |
| 2024-10 | 1 |
| 2024-04 | 1 |
| 2024-01 | 1 |
| 2024-03 | 1 |

**language** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| zh/en | 18 |
| en | 8 |

**model_type** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| open_weight | 14 |
| proprietary | 11 |
| multimodal | 1 |

**parameters_b** — Unique values: 11, Nulls: 0

| Value | Count |
|-------|-------|
| ? | 16 |
| 72 | 1 |
| 32 | 1 |
| 14 | 1 |
| 7 | 1 |
| 3 | 1 |
| 1.5 | 1 |
| 34 | 1 |
| 6 | 1 |
| 405 | 1 |
| 70 | 1 |

**source** — Unique values: 12, Nulls: 0

| Value | Count |
|-------|-------|
| Alibaba / LMSYS | 7 |
| Zhipu AI / LMSYS | 3 |
| 01.ai / LMSYS | 2 |
| DeepSeek / LMSYS | 2 |
| Baichuan / LMSYS | 2 |
| OpenAI / LMSYS | 2 |
| Anthropic / LMSYS | 2 |
| Meta / LMSYS | 2 |
| MiniMax / LMSYS | 1 |
| Moonshot AI / LMSYS | 1 |
| Google / LMSYS | 1 |
| NVIDIA / LMSYS | 1 |

**source_url** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| https://chat.lmsys.org/ | 26 |

**notes** — Unique values: 2, Nulls: 24

| Value | Count |
|-------|-------|
| GLM-5.2 release | 1 |
| Qwen2.5 release | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| score | 1179.81 | 72.29 | 1015.00 | 1287.00 | 1185.50 |

#### Sample Data (First 3 Rows)

| model | organization | benchmark | score | date | language | model_type | parameters_b | source | source_url | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| glm_5_2 | zhipu_ai | lmsys_chatbot_arena | 1247 | 2024-11 | zh/en | proprietary | ? | Zhipu AI / LMSYS | https://chat.lmsys.org/ | GLM-5.2 release |
| glm_4 | zhipu_ai | lmsys_chatbot_arena | 1198 | 2024-06 | zh/en | proprietary | ? | Zhipu AI / LMSYS | https://chat.lmsys.org/ | nan |
| glm_4v | zhipu_ai | lmsys_chatbot_arena | 1156 | 2024-08 | zh/en | multimodal | ? | Zhipu AI / LMSYS | https://chat.lmsys.org/ | nan |

---

### `DATA\enterprise_contracts.csv`

- **Size:** 0.0 MB (2,334 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 15
- **Columns:** 12

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 5 | company, contract_type, source, source_url, notes |
| Numeric | 7 | avg_contract_length_years, renewal_rate_pct, downsizing_pct_at_renewal, expansion_pct_at_renewal, net_revenue_retention_pct, gross_revenue_retention_pct, year |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**company** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| aws | 3 |
| azure | 3 |
| gcp | 3 |
| oracle | 1 |
| salesforce | 1 |
| servicenow | 1 |
| databricks | 1 |
| snowflake | 1 |
| meta | 1 |

**contract_type** — Unique values: 6, Nulls: 0

| Value | Count |
|-------|-------|
| enterprise_agreement | 4 |
| enterprise_saas | 4 |
| reserved_instances | 2 |
| savings_plans | 2 |
| committed_use_discounts | 2 |
| universal_credits | 1 |

**source** — Unique values: 12, Nulls: 0

| Value | Count |
|-------|-------|
| Alphabet 10-K / Analyst | 3 |
| Microsoft 10-K / Analyst | 2 |
| AWS 10-K / Analyst Reports | 1 |
| AWS 10-K / Flexera State of Cloud | 1 |
| AWS 10-K / Analyst | 1 |
| Microsoft 10-K / Flexera | 1 |
| Oracle 10-K / Analyst | 1 |
| Salesforce 10-K / ICONIQ | 1 |
| ServiceNow 10-K / KeyBanc | 1 |
| Databricks S-1 / Analyst | 1 |
| Snowflake 10-K / ICONIQ | 1 |
| Meta 10-K / Analyst | 1 |

**source_url** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.sec.gov/ | 7 |
| https://info.flexera.com/CM-REPORT-State-of-the-Cloud | 2 |
| https://www.sec.gov/Archives/edgar/data/1326801/000132680124000023/meta-20231231.htm | 2 |
| https://www.sec.gov/Archives/edgar/data/1018724/000101872424000023/amzn-20231231.htm | 1 |
| https://www.sec.gov/Archives/edgar/data/789019/000078901924000023/msft-20240630.htm | 1 |
| https://www.sec.gov/Archives/edgar/data/1652044/000165204424000022/goog-20231231.htm | 1 |
| https://www.sec.gov/Archives/edgar/data/1341439/000134143924000023/orcl-20231231.htm | 1 |

**notes** — Unique values: 11, Nulls: 4

| Value | Count |
|-------|-------|
| EA typically 3-5yr; NRR ~115% | 1 |
| RI 3yr no upfront | 1 |
| Azure consumption commit | 1 |
| GCP committed use | 1 |
| 5yr CUD higher retention | 1 |
| UC model | 1 |
| CRM NRR best-in-class | 1 |
| ITSM platform stickiness | 1 |
| Data/AI platform expansion | 1 |
| Consumption-based; high expansion | 1 |
| Internal + external cloud | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| avg_contract_length_years | 3.13 | 0.52 | 3.00 | 5.00 | 3.00 |
| renewal_rate_pct | 90.93 | 2.74 | 85.00 | 95.00 | 91.00 |
| downsizing_pct_at_renewal | 17.00 | 5.17 | 8.00 | 25.00 | 18.00 |
| expansion_pct_at_renewal | 21.93 | 12.38 | 8.00 | 50.00 | 20.00 |
| net_revenue_retention_pct | 112.87 | 9.26 | 100.00 | 130.00 | 110.00 |
| gross_revenue_retention_pct | 95.73 | 1.91 | 92.00 | 99.00 | 96.00 |
| year | 2024.00 | 0.00 | 2024.00 | 2024.00 | 2024.00 |

#### Sample Data (First 3 Rows)

| company | contract_type | avg_contract_length_years | renewal_rate_pct | downsizing_pct_at_renewal | expansion_pct_at_renewal | net_revenue_retention_pct | gross_revenue_retention_pct | year | source | source_url | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aws | enterprise_agreement | 3 | 95 | 15 | 25 | 115 | 98 | 2024 | AWS 10-K / Analyst Reports | https://www.sec.gov/Archives/edgar/data/1018724/00 | EA typically 3-5yr; NRR ~115% |
| aws | reserved_instances | 3 | 90 | 20 | 10 | 105 | 95 | 2024 | AWS 10-K / Flexera State of Cloud | https://info.flexera.com/CM-REPORT-State-of-the-Cl | RI 3yr no upfront |
| aws | savings_plans | 3 | 92 | 18 | 15 | 110 | 96 | 2024 | AWS 10-K / Analyst | https://www.sec.gov/ | nan |

---

### `DATA\fuel_prices.csv`

- **Size:** 0.0 MB (2,669 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 19
- **Columns:** 8

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 5 | fuel_type, region, source, source_url, notes |
| Numeric | 3 | price_usd_per_mmbtu, price_usd_per_kg, date |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**fuel_type** — Unique values: 4, Nulls: 0

| Value | Count |
|-------|-------|
| natural_gas | 9 |
| hydrogen | 6 |
| diesel | 2 |
| biogas | 2 |

**region** — Unique values: 13, Nulls: 0

| Value | Count |
|-------|-------|
| henry_hub | 3 |
| ttf_europe | 2 |
| jkm_asia | 2 |
| us_gulf_coast | 2 |
| green_pem_us | 2 |
| pg_e_citygate | 1 |
| waha_tx | 1 |
| blue_smr_ccs_us | 1 |
| gray_smr_us | 1 |
| delivered_green_us | 1 |
| delivered_blue_us | 1 |
| us_average | 1 |
| california_lcfs | 1 |

**source** — Unique values: 17, Nulls: 0

| Value | Count |
|-------|-------|
| ICE/Refinitiv 2024 Average | 2 |
| ICE/Refinitiv 2023 Average | 2 |
| EIA Annual Average 2024 | 1 |
| EIA/FRED 2025 Average | 1 |
| EIA STEO Forecast 2026 | 1 |
| EIA Citygate 2024 Average | 1 |
| EIA/Platts 2024 Average | 1 |
| EIA Weekly Retail 2024 Average | 1 |
| EIA Weekly Retail 2025 Average | 1 |
| DOE H2A 2024 (PEM; $0.03/kWh; 97% CF) | 1 |
| DOE H2A 2024 (PEM) | 1 |
| DOE H2A 2024 (SMR+CCS) | 1 |
| DOE H2A 2024 (SMR) | 1 |
| Industry estimates 2024 (delivery + compression) | 1 |
| Industry estimates 2024 | 1 |

**source_url** — Unique values: 12, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.ice.com/ | 4 |
| https://www.eia.gov/dnav/pet/pet_pri_gnd_dcus_nus_w.htm | 2 |
| https://www.hydrogen.energy.gov/docs/hydrogenprogramlibraries/pdfs/24005-clean-hydrogen-production-cost-pem-electrolyzer.pdf | 2 |
| https://www.hydrogen.energy.gov/ | 2 |
| https://www.energy.gov/ | 2 |
| https://www.eia.gov/todayinenergy/detail.php?id=64184 | 1 |
| https://fred.stlouisfed.org/series/AHHNGSP | 1 |
| https://www.eia.gov/outlooks/steo/ | 1 |
| https://www.eia.gov/dnav/ng/ng_pri_sum_dcu_nus_m.htm | 1 |
| https://www.eia.gov/ | 1 |
| https://www.epa.gov/agstar | 1 |
| https://ww2.arb.ca.gov/ | 1 |

**notes** — Unique values: 18, Nulls: 0

| Value | Count |
|-------|-------|
| Ultra-low sulfur diesel retail | 2 |
| Annual average spot price 2024 | 1 |
| Annual average 2025 | 1 |
| Current forecast | 1 |
| TTF front-month average 2024 | 1 |
| TTF front-month average 2023 | 1 |
| JKM front-month average 2024 | 1 |
| JKM front-month average 2023 | 1 |
| PG&E citygate price includes basis | 1 |
| Waha hub Permian basis | 1 |
| LCOH $5-7/kg 2022$; converted to $/MMBtu using 1 kg H2 = 0.12 MMBtu LHV | 1 |
| Levelized cost $5-7/kg 2022$ | 1 |
| Levelized cost ~$1.5-2.5/kg | 1 |
| Levelized cost ~$1-2/kg | 1 |
| Delivered cost including liquefaction/transport | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| price_usd_per_mmbtu | 11.27 | 7.07 | 2.10 | 22.00 | 12.25 |
| price_usd_per_kg | 4.50 | 2.35 | 1.50 | 8.00 | 4.75 |
| date | 2024.11 | 0.66 | 2023.00 | 2026.00 | 2024.00 |

#### Sample Data (First 3 Rows)

| fuel_type | region | price_usd_per_mmbtu | price_usd_per_kg | source | source_url | date | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| natural_gas | henry_hub | 2.21 | nan | EIA Annual Average 2024 | https://www.eia.gov/todayinenergy/detail.php?id=64 | 2024 | Annual average spot price 2024 |
| natural_gas | henry_hub | 3.52 | nan | EIA/FRED 2025 Average | https://fred.stlouisfed.org/series/AHHNGSP | 2025 | Annual average 2025 |
| natural_gas | henry_hub | 4.5 | nan | EIA STEO Forecast 2026 | https://www.eia.gov/outlooks/steo/ | 2026 | Current forecast |

---

### `DATA\grid_connection_delays.csv`

- **Size:** 0.0 MB (4,204 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 33
- **Columns:** 13

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 6 | region, iso, project_type, source, source_url, notes |
| Numeric | 7 | median_ir_to_cod_months, median_ia_to_cod_months, withdrawal_rate_pct, completion_rate_pct, total_active_gw, total_withdrawn_gw, date |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**region** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| us | 33 |

**iso** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| caiso | 5 |
| pjm | 5 |
| ercot | 5 |
| miso | 5 |
| non_iso | 5 |
| nyiso | 4 |
| spp | 4 |

**project_type** — Unique values: 5, Nulls: 0

| Value | Count |
|-------|-------|
| solar | 7 |
| wind | 7 |
| battery | 7 |
| data_center | 7 |
| natural_gas | 5 |

**source** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| LBNL Queued Up 2025 | 26 |
| LBNL Queued Up 2025 / Industry | 7 |

**source_url** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| https://emp.lbl.gov/publications/queued-2025-edition | 33 |

**notes** — Unique values: 7, Nulls: 26

| Value | Count |
|-------|-------|
| CAISO solar projects 2018-2024 | 1 |
| Gas projects faster | 1 |
| Estimated for large loads | 1 |
| PJM reform transition | 1 |
| Gas +72% YoY 2024 | 1 |
| ERCOT fastest queue | 1 |
| Southeast/West non-ISO | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| median_ir_to_cod_months | 46.55 | 10.61 | 24.00 | 72.00 | 48.00 |
| median_ia_to_cod_months | 31.91 | 9.69 | 12.00 | 50.00 | 30.00 |
| withdrawal_rate_pct | 60.79 | 8.89 | 40.00 | 75.00 | 62.00 |
| completion_rate_pct | 20.52 | 5.57 | 13.00 | 35.00 | 19.00 |
| total_active_gw | 99.42 | 100.22 | 5.00 | 400.00 | 72.00 |
| total_withdrawn_gw | 388.55 | 462.00 | 12.00 | 2000.00 | 200.00 |
| date | 2024.00 | 0.00 | 2024.00 | 2024.00 | 2024.00 |

#### Sample Data (First 3 Rows)

| region | iso | project_type | median_ir_to_cod_months | median_ia_to_cod_months | withdrawal_rate_pct | completion_rate_pct | total_active_gw | total_withdrawn_gw | date | source | source_url | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| us | caiso | solar | 72 | 50 | 75 | 14 | 200 | 1200 | 2024 | LBNL Queued Up 2025 | https://emp.lbl.gov/publications/queued-2025-editi | CAISO solar projects 2018-2024 |
| us | caiso | wind | 60 | 45 | 70 | 15 | 50 | 300 | 2024 | LBNL Queued Up 2025 | https://emp.lbl.gov/publications/queued-2025-editi | nan |
| us | caiso | battery | 48 | 36 | 65 | 18 | 300 | 500 | 2024 | LBNL Queued Up 2025 | https://emp.lbl.gov/publications/queued-2025-editi | nan |

---

### `DATA\grid_services_revenue.csv`

- **Size:** 0.0 MB (4,501 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 28
- **Columns:** 8

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 6 | iso, service, date, source, source_url, notes |
| Numeric | 2 | price_usd_per_mw_yr, volume_mw |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**iso** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| caiso | 8 |
| pjm | 5 |
| ercot | 5 |
| miso | 3 |
| nyiso | 3 |
| iso_ne | 2 |
| spp | 2 |

**service** — Unique values: 13, Nulls: 0

| Value | Count |
|-------|-------|
| spinning_reserve | 5 |
| regulation | 5 |
| regulation_up | 3 |
| regulation_down | 3 |
| non_spinning_reserve | 3 |
| capacity | 2 |
| capacity_2025_26 | 1 |
| capacity_2024_25 | 1 |
| synchronous_reserve | 1 |
| day_ahead_scheduling_reserve | 1 |
| responsive_reserve | 1 |
| ecrs | 1 |
| supplemental_reserve | 1 |

**date** — Unique values: 4, Nulls: 0

| Value | Count |
|-------|-------|
| 2024-01 | 22 |
| 2024-06 | 4 |
| 2024-07 | 1 |
| 2023-07 | 1 |

**source** — Unique values: 11, Nulls: 0

| Value | Count |
|-------|-------|
| CAISO Monthly Market Performance | 8 |
| ERCOT Monthly Report | 5 |
| PJM State of the Market 2024 | 3 |
| MISO State of the Market 2024 | 3 |
| NYISO Market Data | 2 |
| SPP Marketplace | 2 |
| PJM 2025/26 BRA Report | 1 |
| PJM 2024/25 BRA Report | 1 |
| NYISO ICAP Market | 1 |
| ISO-NE Markets | 1 |
| ISO-NE FCA | 1 |

**source_url** — Unique values: 10, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.potomaceconomics.com/wp-content/uploads/2025/01/2024-12_Nodal_Monthly_Report.pdf | 5 |
| https://www.caiso.com/content/monthly-market-performance/jan-2024/ancillary-services-1.html | 4 |
| https://www.caiso.com/content/monthly-market-performance/jun-2024/ancillary-services.html | 4 |
| https://www.monitoringanalytics.com/reports/Reports/2024/IMM_2024_State_of_the_Market_Report_for_PJM.pdf | 3 |
| https://www.potomaceconomics.com/wp-content/uploads/2025/06/2024-MISO-SOM_Report_Body_Final.pdf | 3 |
| https://www.nyiso.com/market-data | 3 |
| https://www.iso-ne.com/markets-operations/markets | 2 |
| https://www.spp.org/marketplace/ | 2 |
| https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2025-2026/2025-2026-base-residual-auction-report.pdf | 1 |
| https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2024-2025/2024-2025-base-residual-auction-report.ashx | 1 |

**notes** — Unique values: 13, Nulls: 15

| Value | Count |
|-------|-------|
| IFM average price | 1 |
| June 2024 average | 1 |
| $269.92/MW-day * 365 = $98,520/MW-yr RTO | 1 |
| $28.92/MW-day * 365 | 1 |
| Regulation market | 1 |
| Potomac Economics | 1 |
| RRS (spinning) | 1 |
| ERCOT Contingency Reserve Service | 1 |
| Ancillary services $0.13/MWh all-in | 1 |
| Regulation movement | 1 |
| Capacity market | 1 |
| Regulation | 1 |
| Forward Capacity Auction | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| price_usd_per_mw_yr | 27736.64 | 21574.11 | 1670.00 | 98520.00 | 23500.00 |
| volume_mw | 13285.32 | 37266.76 | 200.00 | 147478.00 | 800.00 |

#### Sample Data (First 3 Rows)

| iso | service | price_usd_per_mw_yr | volume_mw | date | source | source_url | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| caiso | regulation_up | 45000 | 1200 | 2024-01 | CAISO Monthly Market Performance | https://www.caiso.com/content/monthly-market-perfo | IFM average price |
| caiso | regulation_down | 38000 | 1100 | 2024-01 | CAISO Monthly Market Performance | https://www.caiso.com/content/monthly-market-perfo | nan |
| caiso | spinning_reserve | 25000 | 800 | 2024-01 | CAISO Monthly Market Performance | https://www.caiso.com/content/monthly-market-perfo | nan |

---

### `DATA\heat_rates.csv`

- **Size:** 0.0 MB (3,479 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 16
- **Columns:** 11

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 7 | unit, technology, fuel_type, date, source, source_url, notes |
| Numeric | 4 | heat_rate_btu_per_kwh_hhv, heat_rate_btu_per_kwh_lhv, electrical_efficiency_lhv_pct, degradation_pct_per_year |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**unit** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| bloom_es5 | 5 |
| ge_7ha | 3 |
| siemens_hl | 2 |
| wartsila_18v50 | 2 |
| mitsubishi_m501jac | 1 |
| plug_power_gen | 1 |
| ballard_fc | 1 |
| caterpillar_fc | 1 |

**technology** — Unique values: 5, Nulls: 0

| Value | Count |
|-------|-------|
| gas_turbine | 6 |
| sofc | 5 |
| rice | 2 |
| hydrogen | 2 |
| solid_oxide | 1 |

**fuel_type** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| natural_gas | 13 |
| hydrogen | 3 |

**date** — Unique values: 5, Nulls: 0

| Value | Count |
|-------|-------|
| 2024-01 | 8 |
| 2025-01 | 4 |
| 2026-01 | 2 |
| 2027-01 | 1 |
| 2028-01 | 1 |

**source** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| Bloom Energy ES6.5 Datasheet | 5 |
| GE Vernova 7HA.03 Specs | 3 |
| Siemens Energy HL-Class | 2 |
| Wärtsilä 50SG Datasheet | 2 |
| MHI M501JAC Specs | 1 |
| Plug Power GenSure / DOE H2A | 1 |
| Ballard Fuel Cells / DOE | 1 |
| Caterpillar / DOE | 1 |

**source_url** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.bloomenergy.com/wp-content/uploads/bloom-energy-server-datasheet-feb-2026.pdf | 5 |
| https://www.gevernova.com/content/dam/gepower-new/global/en_US/downloads/gas-new-site/products/gas-turbines/7ha.03-takeaway.pdf | 3 |
| https://assets.siemens-energy.com/dam/6a81abd9-6c46-42c9-9034-b036013f322b/210923-HL-ClassFactSheet-05-pdf_Original%20file.pdf | 2 |
| https://www.wartsila.com/docs/default-source/energy-docs/technology-products/product-leaflets/wartsila-50sg.pdf | 2 |
| https://power.mhi.com/products/gasturbines/lineup/m501j/ | 1 |
| https://www.plugpower.com/wp-content/uploads/2016/03/GenSure_E-1000x_Spec012916.pdf | 1 |
| https://www.ballard.com/ | 1 |
| https://www.cat.com/ | 1 |

**notes** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| Degradation +50 Btu/kWh/yr | 4 |
| Degradation | 4 |
| PEM FC system | 2 |
| HHV 5811-7127 Btu/kWh range; midpoint 6800 | 1 |
| SC Net Heat Rate LHV 7897 Btu/kWh; HHV approx | 1 |
| GT Heat Rate <8333 kJ/kWh = 7898 Btu/kWh LHV | 1 |
| Simple cycle heat rate 7775 Btu/kWh LHV per Gas Turbine World | 1 |
| Heat rate 7207 kJ/kWh = 6834 Btu/kWh LHV at generator terminals | 1 |
| PEM FC ~55% LHV; HHV = LHV/0.885 | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| heat_rate_btu_per_kwh_hhv | 7912.50 | 1377.01 | 6200.00 | 9700.00 | 7750.00 |
| heat_rate_btu_per_kwh_lhv | 7308.75 | 1349.42 | 5500.00 | 9021.00 | 7207.50 |
| electrical_efficiency_lhv_pct | 52.76 | 8.88 | 42.40 | 65.00 | 51.75 |
| degradation_pct_per_year | 0.53 | 0.14 | 0.30 | 0.70 | 0.50 |

#### Sample Data (First 3 Rows)

| unit | technology | fuel_type | heat_rate_btu_per_kwh_hhv | heat_rate_btu_per_kwh_lhv | electrical_efficiency_lhv_pct | date | degradation_pct_per_year | source | source_url | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bloom_es5 | sofc | natural_gas | 6800 | 6324 | 65.0 | 2024-01 | 0.5 | Bloom Energy ES6.5 Datasheet | https://www.bloomenergy.com/wp-content/uploads/blo | HHV 5811-7127 Btu/kWh range; midpoint 6800 |
| bloom_es5 | sofc | natural_gas | 6850 | 6371 | 64.5 | 2025-01 | 0.5 | Bloom Energy ES6.5 Datasheet | https://www.bloomenergy.com/wp-content/uploads/blo | Degradation +50 Btu/kWh/yr |
| bloom_es5 | sofc | natural_gas | 6900 | 6417 | 64.0 | 2026-01 | 0.5 | Bloom Energy ES6.5 Datasheet | https://www.bloomenergy.com/wp-content/uploads/blo | Degradation +50 Btu/kWh/yr |

---

### `DATA\hedge_ratios.csv`

- **Size:** 0.0 MB (2,147 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 16
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 7 | company, commodity, instruments, date, source, source_url, notes |
| Numeric | 2 | hedge_ratio, tenor_yr |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**company** — Unique values: 6, Nulls: 0

| Value | Count |
|-------|-------|
| microsoft | 3 |
| google | 3 |
| aws | 3 |
| meta | 3 |
| oracle | 2 |
| intel | 2 |

**commodity** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| natural_gas | 16 |

**instruments** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| swaps | 7 |
| swaps_collars | 6 |
| swaps_collars_physical | 3 |

**date** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| 2024-01 | 6 |
| 2025-01 | 6 |
| 2026-01 | 4 |

**source** — Unique values: 16, Nulls: 0

| Value | Count |
|-------|-------|
| Microsoft 10-K 2024 | 1 |
| Microsoft 10-K 2025 | 1 |
| Microsoft 10-K 2026 (est.) | 1 |
| Alphabet 10-K 2024 | 1 |
| Alphabet 10-K 2025 | 1 |
| Alphabet 10-K 2026 (est.) | 1 |
| Amazon 10-K 2024 | 1 |
| Amazon 10-K 2025 | 1 |
| Amazon 10-K 2026 (est.) | 1 |
| Meta 10-K 2024 | 1 |
| Meta 10-K 2025 | 1 |
| Meta 10-K 2026 (est.) | 1 |
| Oracle 10-K 2024 | 1 |
| Oracle 10-K 2025 | 1 |
| Intel 10-K 2024 | 1 |

**source_url** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.sec.gov/ | 10 |
| https://www.sec.gov/Archives/edgar/data/789019/000078901924000023/msft-20240630.htm | 1 |
| https://www.sec.gov/Archives/edgar/data/1652044/000165204424000022/goog-20231231.htm | 1 |
| https://www.sec.gov/Archives/edgar/data/1018724/000101872424000023/amzn-20231231.htm | 1 |
| https://www.sec.gov/Archives/edgar/data/1326801/000132680124000023/meta-20231231.htm | 1 |
| https://www.sec.gov/Archives/edgar/data/1341439/000134143924000023/orcl-20231231.htm | 1 |
| https://www.sec.gov/Archives/edgar/data/50863/000005086324000023/intc-20231230.htm | 1 |

**notes** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| Updated | 5 |
| Projected | 4 |
| Commodity derivatives: natural gas hedges | 1 |
| Updated hedge ratio | 1 |
| Natural gas hedges for datacenters | 1 |
| Physical and financial hedges | 1 |
| Natural gas procurement hedges | 1 |
| Commodity hedging program | 1 |
| Natural gas hedges for manufacturing | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| hedge_ratio | 0.65 | 0.08 | 0.50 | 0.80 | 0.65 |
| tenor_yr | 2.38 | 0.50 | 2.00 | 3.00 | 2.00 |

#### Sample Data (First 3 Rows)

| company | commodity | hedge_ratio | tenor_yr | instruments | date | source | source_url | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| microsoft | natural_gas | 0.65 | 3 | swaps_collars | 2024-01 | Microsoft 10-K 2024 | https://www.sec.gov/Archives/edgar/data/789019/000 | Commodity derivatives: natural gas hedges |
| microsoft | natural_gas | 0.7 | 2 | swaps_collars | 2025-01 | Microsoft 10-K 2025 | https://www.sec.gov/ | Updated hedge ratio |
| microsoft | natural_gas | 0.75 | 2 | swaps_collars | 2026-01 | Microsoft 10-K 2026 (est.) | https://www.sec.gov/ | Projected |

---

### `DATA\onsite_gen_capacity.csv`

- **Size:** 0.0 MB (4,203 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 27
- **Columns:** 11

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 6 | company, region, technology, fuel_type, deployment_source, source_url |
| Numeric | 4 | capacity_mw, cod_year, capacity_factor, heat_rate_btu_per_kwh |
| Date | 0 | — |
| Text | 1 | notes |

#### Category Column Details

**company** — Unique values: 10, Nulls: 0

| Value | Count |
|-------|-------|
| microsoft | 6 |
| aws | 6 |
| google | 4 |
| oracle | 3 |
| intel | 2 |
| meta | 2 |
| coreweave | 1 |
| equinix | 1 |
| digital_realty | 1 |
| cyrusone | 1 |

**region** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| us | 27 |

**technology** — Unique values: 4, Nulls: 0

| Value | Count |
|-------|-------|
| bloom_sofc | 21 |
| gas_turbine | 3 |
| hydrogen_fc | 2 |
| solar_storage | 1 |

**fuel_type** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| natural_gas | 24 |
| hydrogen | 2 |
| sunlight | 1 |

**deployment_source** — Unique values: 18, Nulls: 0

| Value | Count |
|-------|-------|
| Bloom Energy 10-K / Microsoft sustainability | 3 |
| Bloom Energy / Intel PPA | 3 |
| Bloom Energy Oregon 3 sites | 3 |
| Bloom Energy Silicon Valley PPA | 3 |
| Bloom Energy 10-K Oracle 1.6GW | 2 |
| Plug Power / Microsoft | 1 |
| Ballard / Caterpillar / Microsoft | 1 |
| Chicago 3x66MW | 1 |
| Grid connection queue | 1 |
| Bloom Energy 10-K Oracle 1.2GW | 1 |
| Bloom Energy Intel 2014 | 1 |
| Bloom Energy Intel 2024 | 1 |
| Bloom Energy CoreWeave 2026 | 1 |
| Bloom Energy Equinix 2024 | 1 |
| Bloom Energy DLR 2024 | 1 |

**source_url** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.bloomenergy.com/ | 18 |
| https://www.sec.gov/Archives/edgar/data/1664703/000162828025016212/a202410kars.pdf | 3 |
| https://sustainability.fb.com/ | 2 |
| https://www.plugpower.com/ | 1 |
| https://www.ballard.com/ | 1 |
| https://www.gevernova.com/ | 1 |
| https://www.caiso.com/ | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| capacity_mw | 220.39 | 459.03 | 1.50 | 1600.00 | 50.00 |
| cod_year | 2023.37 | 3.84 | 2008.00 | 2026.00 | 2024.00 |
| capacity_factor | 0.86 | 0.13 | 0.25 | 0.90 | 0.90 |
| heat_rate_btu_per_kwh | 6751.85 | 1657.47 | 0.00 | 9500.00 | 6800.00 |

#### Sample Data (First 3 Rows)

| company | region | technology | capacity_mw | cod_year | capacity_factor | heat_rate_btu_per_kwh | fuel_type | deployment_source | source_url | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| microsoft | us | bloom_sofc | 20.0 | 2024 | 0.9 | 6800 | natural_gas | Bloom Energy 10-K / Microsoft sustainability | https://www.bloomenergy.com/ | Bloom Energy Server ES-5/ES-6 at Microsoft datacen |
| microsoft | us | bloom_sofc | 20.0 | 2025 | 0.9 | 6800 | natural_gas | Bloom Energy 10-K / Microsoft sustainability | https://www.bloomenergy.com/ | Planned deployment |
| microsoft | us | bloom_sofc | 20.0 | 2026 | 0.9 | 6800 | natural_gas | Bloom Energy 10-K / Microsoft sustainability | https://www.bloomenergy.com/ | Planned deployment |

---

### `DATA\productivity_meta_analysis.csv`

- **Size:** 0.0 MB (2,736 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 15
- **Columns:** 14

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 9 | study, category, intervention, industry, task_type, study_design, quality_score, source, source_url |
| Numeric | 5 | sample_size, effect_size_pct, ci_lower_pct, ci_upper_pct, date |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**study** — Unique values: 15, Nulls: 0

| Value | Count |
|-------|-------|
| peng_2023 | 1 |
| tabachnyk_2022 | 1 |
| moradi_2023 | 1 |
| noy_2023 | 1 |
| dellacqua_2023 | 1 |
| brynjolfsson_2023 | 1 |
| cui_2024 | 1 |
| kanazawa_2023 | 1 |
| agrawal_2023 | 1 |
| wang_2023 | 1 |
| liu_2024 | 1 |
| eloundou_2023 | 1 |
| felten_2023 | 1 |
| kalliamvakou_2022 | 1 |
| zhang_2023 | 1 |

**category** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| coding | 5 |
| consulting | 2 |
| customer_support | 2 |
| general | 2 |
| writing | 1 |
| legal | 1 |
| rd_materials | 1 |
| rd_drug | 1 |

**intervention** — Unique values: 13, Nulls: 0

| Value | Count |
|-------|-------|
| ai_assistant | 2 |
| ai_discovery | 2 |
| github_copilot | 1 |
| ml_code_completion | 1 |
| ai_pair_programming | 1 |
| chatgpt | 1 |
| genai_assistant | 1 |
| ai_review | 1 |
| ai_analysis | 1 |
| llm_exposure | 1 |
| ai_exposure | 1 |
| copilot | 1 |
| codex | 1 |

**industry** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| software_engineering | 5 |
| consulting | 2 |
| all_occupations | 2 |
| professional_services | 1 |
| technology | 1 |
| customer_service | 1 |
| legal | 1 |
| materials_science | 1 |
| pharma | 1 |

**task_type** — Unique values: 13, Nulls: 0

| Value | Count |
|-------|-------|
| code_generation | 3 |
| debugging | 1 |
| business_writing | 1 |
| strategy_analysis | 1 |
| customer_support | 1 |
| ticket_resolution | 1 |
| document_review | 1 |
| market_research | 1 |
| experiment_design | 1 |
| drug_discovery | 1 |
| task_automation | 1 |
| occupation_level | 1 |
| productivity | 1 |

**study_design** — Unique values: 4, Nulls: 0

| Value | Count |
|-------|-------|
| rct | 10 |
| quasi_exp | 2 |
| meta_analysis | 2 |
| survey | 1 |

**quality_score** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| high | 12 |
| medium | 3 |

**source** — Unique values: 15, Nulls: 0

| Value | Count |
|-------|-------|
| Peng et al. 2023 (Microsoft) | 1 |
| Tabachnyk & Nikolov 2022 | 1 |
| Moradi et al. 2023 | 1 |
| Noy & Zhang 2023 Science | 1 |
| Dell'Acqua et al. 2023 (BCG) | 1 |
| Brynjolfsson et al. 2023 NBER | 1 |
| Cui et al. 2024 QJE | 1 |
| Kanazawa et al. 2023 | 1 |
| Agrawal et al. 2023 | 1 |
| Wang et al. 2023 Nature | 1 |
| Liu et al. 2024 | 1 |
| Eloundou et al. 2023 (OpenAI) | 1 |
| Felten et al. 2023 | 1 |
| Kalliamvakou et al. 2022 (GitHub) | 1 |
| Zhang et al. 2023 | 1 |

**source_url** — Unique values: 14, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.nber.org/papers/w31161 | 2 |
| https://arxiv.org/abs/2302.06590 | 1 |
| https://arxiv.org/abs/2210.05711 | 1 |
| https://arxiv.org/abs/2305.15024 | 1 |
| https://www.science.org/doi/10.1126/science.adh2586 | 1 |
| https://www.hbs.edu/ris/Publication%20Files/24-013_0f7c8c5a-6b4b-4c7d-9c5a-8f9e5b7f5c6d.pdf | 1 |
| https://doi.org/10.1093/qje/qjae012 | 1 |
| https://arxiv.org/abs/2306.07822 | 1 |
| https://www.nature.com/articles/s41586-023-06735-2 | 1 |
| https://www.nature.com/articles/s41587-024-02123-4 | 1 |
| https://arxiv.org/abs/2303.10130 | 1 |
| https://arxiv.org/abs/2306.17175 | 1 |
| https://github.blog/2022-09-07-research-quantifying-github-copilots-impact/ | 1 |
| https://arxiv.org/abs/2305.14822 | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| sample_size | 1027.93 | 1398.57 | 80.00 | 5172.00 | 500.00 |
| effect_size_pct | 31.55 | 13.12 | 12.00 | 55.80 | 31.00 |
| ci_lower_pct | 22.91 | 10.74 | 8.00 | 40.20 | 22.00 |
| ci_upper_pct | 40.18 | 15.88 | 16.00 | 71.40 | 42.00 |
| date | 2023.00 | 0.53 | 2022.00 | 2024.00 | 2023.00 |

#### Sample Data (First 3 Rows)

| study | category | intervention | industry | task_type | sample_size | effect_size_pct | ci_lower_pct | ci_upper_pct | study_design | quality_score | source | source_url | date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| peng_2023 | coding | github_copilot | software_engineering | code_generation | 95 | 55.8 | 40.2 | 71.4 | rct | high | Peng et al. 2023 (Microsoft) | https://arxiv.org/abs/2302.06590 | 2023 |
| tabachnyk_2022 | coding | ml_code_completion | software_engineering | code_generation | 120 | 37.0 | 25.0 | 49.0 | quasi_exp | high | Tabachnyk & Nikolov 2022 | https://arxiv.org/abs/2210.05711 | 2022 |
| moradi_2023 | coding | ai_pair_programming | software_engineering | debugging | 80 | 28.5 | 15.0 | 42.0 | rct | medium | Moradi et al. 2023 | https://arxiv.org/abs/2305.15024 | 2023 |

---

### `DATA\regional_infrastructure.csv`

- **Size:** 0.0 MB (2,526 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 13
- **Columns:** 13

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 5 | region, country, source, source_url, notes |
| Numeric | 8 | ppp_factor_usd_base, power_growth_cap_annual_pct, grid_connection_delay_months, gov_coordination_index, cost_per_mw_usd_millions, transformer_shortage_factor, cooling_water_availability, renewable_penetration_pct |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**region** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| southeast_asia | 4 |
| gulf | 2 |
| us | 1 |
| china | 1 |
| india | 1 |
| eu | 1 |
| japan | 1 |
| korea | 1 |
| taiwan | 1 |

**country** — Unique values: 13, Nulls: 0

| Value | Count |
|-------|-------|
| united_states | 1 |
| china | 1 |
| india | 1 |
| uae | 1 |
| saudi_arabia | 1 |
| eu_average | 1 |
| japan | 1 |
| south_korea | 1 |
| taiwan | 1 |
| vietnam | 1 |
| indonesia | 1 |
| malaysia | 1 |
| singapore | 1 |

**source** — Unique values: 13, Nulls: 0

| Value | Count |
|-------|-------|
| World Bank ICP 2021 / LBNL / EIA | 1 |
| World Bank ICP 2021 / NBS China / LBNL | 1 |
| World Bank ICP 2021 / CEA India | 1 |
| World Bank ICP 2021 / DEWA / SEC | 1 |
| World Bank ICP 2021 / SEC / NEOM | 1 |
| World Bank ICP 2021 / ENTSO-E / EC | 1 |
| World Bank ICP 2021 / METI / OCCTO | 1 |
| World Bank ICP 2021 / KEPCO / KPX | 1 |
| World Bank ICP 2021 / Taipower | 1 |
| World Bank ICP 2021 / EVN / ADB | 1 |
| World Bank ICP 2021 / PLN / ADB | 1 |
| World Bank ICP 2021 / TNB / Suruhanjaya Tenaga | 1 |
| World Bank ICP 2021 / EMA / SP Group | 1 |

**source_url** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.worldbank.org/en/programs/icp | 13 |

**notes** — Unique values: 10, Nulls: 3

| Value | Count |
|-------|-------|
| PPP=1.0 base; power growth from FERC/EIA; grid delay from LBNL Queued Up 2025 | 1 |
| PPP 0.55 (ICP 2021); power growth from NDRC 5-yr plan; grid delay from China grid corp | 1 |
| PPP 0.45; power growth from CEA NEP; grid delay from POSOCO | 1 |
| PPP 0.80; power growth from UAE Energy Strategy 2050; grid from DEWA | 1 |
| PPP 0.75; power growth from Vision 2030; grid from SEC | 1 |
| PPP 1.15 (avg); power growth low due to demand stagnation; grid delay from ENTSO-E TYNDP | 1 |
| PPP 0.95; power growth near zero; grid delay from OCCTO | 1 |
| PPP 0.90; power growth from 10th Basic Plan | 1 |
| PPP 0.50; power growth from PDP8 | 1 |
| PPP 1.05; land/power constrained | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| ppp_factor_usd_base | 0.77 | 0.24 | 0.45 | 1.15 | 0.80 |
| power_growth_cap_annual_pct | 13.69 | 8.05 | 4.00 | 28.00 | 12.00 |
| grid_connection_delay_months | 20.46 | 11.44 | 6.00 | 48.00 | 18.00 |
| gov_coordination_index | 0.69 | 0.18 | 0.30 | 0.95 | 0.70 |
| cost_per_mw_usd_millions | 2.05 | 0.76 | 1.10 | 3.50 | 1.80 |
| transformer_shortage_factor | 0.14 | 0.06 | 0.05 | 0.25 | 0.15 |
| cooling_water_availability | 0.16 | 0.11 | 0.05 | 0.40 | 0.15 |
| renewable_penetration_pct | 19.69 | 12.68 | 2.00 | 45.00 | 22.00 |

#### Sample Data (First 3 Rows)

| region | country | ppp_factor_usd_base | power_growth_cap_annual_pct | grid_connection_delay_months | gov_coordination_index | cost_per_mw_usd_millions | transformer_shortage_factor | cooling_water_availability | renewable_penetration_pct | source | source_url | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| us | united_states | 1.0 | 12 | 24 | 0.5 | 2.5 | 0.2 | 0.35 | 22 | World Bank ICP 2021 / LBNL / EIA | https://www.worldbank.org/en/programs/icp | PPP=1.0 base; power growth from FERC/EIA; grid del |
| china | china | 0.55 | 24 | 12 | 0.95 | 1.1 | 0.1 | 0.15 | 35 | World Bank ICP 2021 / NBS China / LBNL | https://www.worldbank.org/en/programs/icp | PPP 0.55 (ICP 2021); power growth from NDRC 5-yr p |
| india | india | 0.45 | 18 | 18 | 0.7 | 1.3 | 0.15 | 0.1 | 25 | World Bank ICP 2021 / CEA India | https://www.worldbank.org/en/programs/icp | PPP 0.45; power growth from CEA NEP; grid delay fr |

---

### `DATA\technology_parameters.csv`

- **Size:** 0.01 MB (8,806 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 54
- **Columns:** 8

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 5 | technology, parameter, unit, source_url, date_accessed |
| Numeric | 1 | value |
| Date | 0 | — |
| Text | 2 | source, notes |

#### Category Column Details

**technology** — Unique values: 6, Nulls: 0

| Value | Count |
|-------|-------|
| gas_turbine_7ha | 10 |
| rice_wartsila_18v50sg | 9 |
| hydrogen_fc_plug | 9 |
| solar_storage | 9 |
| smr_nuscale | 9 |
| bloom_sofc | 8 |

**parameter** — Unique values: 10, Nulls: 0

| Value | Count |
|-------|-------|
| heat_rate_btu_per_kwh_hhv | 6 |
| electrical_efficiency_lhv_pct | 6 |
| capacity_factor | 6 |
| co2_emissions_ton_per_mwh | 6 |
| water_intensity_l_per_mwh | 6 |
| capex_usd_per_kw | 6 |
| om_usd_per_mwh | 6 |
| degradation_pct_per_year | 6 |
| heat_rate_btu_per_kwh_lhv | 5 |
| combined_cycle_heat_rate_btu_per_kwh_lhv | 1 |

**unit** — Unique values: 8, Nulls: 6

| Value | Count |
|-------|-------|
| Btu/kWh | 12 |
| ton CO2/MWh | 6 |
| L/MWh | 6 |
| USD/kW | 6 |
| USD/MWh | 6 |
| %/yr | 6 |
| LHV % | 5 |
| % | 1 |

**source_url** — Unique values: 19, Nulls: 7

| Value | Count |
|-------|-------|
| https://www.bloomenergy.com/wp-content/uploads/bloom-energy-server-datasheet-feb-2026.pdf | 5 |
| https://www.wartsila.com/ | 5 |
| https://www.gevernova.com/content/dam/gepower-new/global/en_US/downloads/gas-new-site/products/gas-turbines/7ha.03-takeaway.pdf | 4 |
| https://www.plugpower.com/ | 4 |
| https://www.nuscalepower.com/ | 4 |
| https://www.sec.gov/Archives/edgar/data/1664703/000162828025016212/a202410kars.pdf | 3 |
| https://www.eia.gov/ | 3 |
| https://www.wartsila.com/docs/default-source/energy-docs/technology-products/product-leaflets/wartsila-50sg.pdf | 3 |
| https://www.hydrogen.energy.gov/ | 3 |
| https://atb.nrel.gov/ | 3 |
| https://www.plugpower.com/wp-content/uploads/2016/03/GenSure_E-1000x_Spec012916.pdf | 2 |
| https://www.eia.gov/electricity/annual/ | 1 |
| https://www.epa.gov/ | 1 |
| https://www.epri.com/ | 1 |
| https://www.gevernova.com/ | 1 |

**date_accessed** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-07-14 | 54 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| value | 1433.54 | 2745.83 | 0.00 | 9500.00 | 1.20 |

#### Sample Data (First 3 Rows)

| technology | parameter | value | unit | source | source_url | date_accessed | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bloom_sofc | heat_rate_btu_per_kwh_hhv | 6800.0 | Btu/kWh | Bloom Energy ES6.5 Datasheet | https://www.bloomenergy.com/wp-content/uploads/blo | 2026-07-14 | HHV basis; range 5811-7127 Btu/kWh per datasheet |
| bloom_sofc | electrical_efficiency_lhv_pct | 65.0 | LHV % | Bloom Energy ES6.5 Datasheet | https://www.bloomenergy.com/wp-content/uploads/blo | 2026-07-14 | Cumulative electrical efficiency LHV net AC |
| bloom_sofc | capacity_factor | 0.9 | nan | Bloom Energy 10-K 2024 / Industry reports | https://www.sec.gov/Archives/edgar/data/1664703/00 | 2026-07-14 | Typically operating with load factors between 80%  |

---

### `DATA\transformer_shortage.csv`

- **Size:** 0.0 MB (2,924 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 10
- **Columns:** 10

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 10 | transformer_type, lead_time_weeks_2021, lead_time_weeks_2022, lead_time_weeks_2023, lead_time_weeks_2024, lead_time_weeks_2025, price_increase_pct_2020_2024, source, source_url, notes |
| Numeric | 0 | — |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**transformer_type** — Unique values: 10, Nulls: 0

| Value | Count |
|-------|-------|
| distribution_10_25kva | 1 |
| distribution_50_100kva | 1 |
| distribution_500_1000kva | 1 |
| substation_10_50mva | 1 |
| substation_100_300mva | 1 |
| generator_step_up_100_500mva | 1 |
| large_power_500mva_plus | 1 |
| goes_electrical_steel | 1 |
| ak_steel | 1 |
| metglas_amorphous | 1 |

**lead_time_weeks_2021** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| 60 | 2 |
| 30 | 1 |
| 35 | 1 |
| 40 | 1 |
| 50 | 1 |
| 80 | 1 |
| tonnes_per_year | 1 |
| 120000 | 1 |
| 50000 | 1 |

**lead_time_weeks_2022** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| 90 | 2 |
| 100 | 2 |
| 40 | 1 |
| 50 | 1 |
| 60 | 1 |
| 70 | 1 |
| 120 | 1 |
| domestic_production_pct | 1 |

**lead_time_weeks_2023** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| 0 | 2 |
| 60 | 1 |
| 70 | 1 |
| 80 | 1 |
| 100 | 1 |
| 120 | 1 |
| 130 | 1 |
| 160 | 1 |
| import_dependence_pct | 1 |

**lead_time_weeks_2024** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| 90 | 2 |
| 80 | 1 |
| 110 | 1 |
| 140 | 1 |
| 180 | 1 |
| 200 | 1 |
| 210 | 1 |
| price_increase_pct_2020_2024 | 1 |
| 85 | 1 |

**lead_time_weeks_2025** — Unique values: 8, Nulls: 1

| Value | Count |
|-------|-------|
| Wood Mackenzie / NIAC | 2 |
| 100 | 1 |
| 110 | 1 |
| 130 | 1 |
| 180 | 1 |
| 210 | 1 |
| 250 | 1 |
| 300 | 1 |

**price_increase_pct_2020_2024** — Unique values: 8, Nulls: 1

| Value | Count |
|-------|-------|
| https://www.cisa.gov/sites/default/files/2024-06/DRAFT_NIAC_Addressing%20the%20Critical%20Shortage%20of%20Power%20Transformers%20to%20Ensure%20Reliability%20of%20the%20U.S.%20Grid_Report_06052024_508c.pdf | 2 |
| 60 | 1 |
| 65 | 1 |
| 70 | 1 |
| 75 | 1 |
| 80 | 1 |
| 85 | 1 |
| 90 | 1 |

**source** — Unique values: 3, Nulls: 1

| Value | Count |
|-------|-------|
| Wood Mackenzie / NIAC | 7 |
| Only domestic GOES supplier | 1 |
| Amorphous steel supplier | 1 |

**source_url** — Unique values: 1, Nulls: 3

| Value | Count |
|-------|-------|
| https://www.cisa.gov/sites/default/files/2024-06/DRAFT_NIAC_Addressing%20the%20Critical%20Shortage%20of%20Power%20Transformers%20to%20Ensure%20Reliability%20of%20the%20U.S.%20Grid_Report_06052024_508c.pdf | 7 |

**notes** — Unique values: 7, Nulls: 3

| Value | Count |
|-------|-------|
| Single-phase pad-mount | 1 |
| Three-phase pad-mount | 1 |
| Three-phase pad-mount substation | 1 |
| Substation power transformer | 1 |
| Large substation transformer | 1 |
| GSU for power plants | 1 |
| >500 MVA LPT | 1 |

#### Sample Data (First 3 Rows)

| transformer_type | lead_time_weeks_2021 | lead_time_weeks_2022 | lead_time_weeks_2023 | lead_time_weeks_2024 | lead_time_weeks_2025 | price_increase_pct_2020_2024 | source | source_url | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| distribution_10_25kva | 30 | 40 | 60 | 80 | 100 | 60 | Wood Mackenzie / NIAC | https://www.cisa.gov/sites/default/files/2024-06/D | Single-phase pad-mount |
| distribution_50_100kva | 35 | 50 | 70 | 90 | 110 | 65 | Wood Mackenzie / NIAC | https://www.cisa.gov/sites/default/files/2024-06/D | Three-phase pad-mount |
| distribution_500_1000kva | 40 | 60 | 80 | 110 | 130 | 70 | Wood Mackenzie / NIAC | https://www.cisa.gov/sites/default/files/2024-06/D | Three-phase pad-mount substation |

---

### `DATA\wholesale_electricity_prices.csv`

- **Size:** 0.0 MB (4,291 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 27
- **Columns:** 8

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 6 | region, iso, price_type, source, source_url, notes |
| Numeric | 2 | price_usd_per_mwh, year |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**region** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| us | 27 |

**iso** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| ercot_north | 3 |
| spp | 3 |
| miso | 3 |
| ca_north | 3 |
| pjm_west | 3 |
| nyiso | 3 |
| isone | 3 |
| ca_iso | 3 |
| national_avg | 3 |

**price_type** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| load_weighted_avg_rt | 27 |

**source** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| FERC State of the Markets 2024 | 16 |
| LBNL ReWEP | 11 |

**source_url** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.ferc.gov/sites/default/files/2025-03/25_State-of-the-Market_0320_1200.pdf | 16 |
| https://eta-publications.lbl.gov/sites/default/files/rewep-2024update_tech-brief_20240429.pdf | 11 |

**notes** — Unique values: 3, Nulls: 24

| Value | Count |
|-------|-------|
| ERCOT lowest; 2023 was $52/MWh | 1 |
| CAISO high; Jan 2024 spike from gas | 1 |
| Down from $63 in 2022 | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| price_usd_per_mwh | 51.33 | 17.05 | 28.00 | 85.00 | 51.00 |
| year | 2022.89 | 0.89 | 2021.00 | 2024.00 | 2023.00 |

#### Sample Data (First 3 Rows)

| region | iso | price_usd_per_mwh | price_type | year | source | source_url | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| us | ercot_north | 28 | load_weighted_avg_rt | 2024 | FERC State of the Markets 2024 | https://www.ferc.gov/sites/default/files/2025-03/2 | ERCOT lowest; 2023 was $52/MWh |
| us | spp | 28 | load_weighted_avg_rt | 2024 | FERC State of the Markets 2024 | https://www.ferc.gov/sites/default/files/2025-03/2 | nan |
| us | miso | 31 | load_weighted_avg_rt | 2024 | FERC State of the Markets 2024 | https://www.ferc.gov/sites/default/files/2025-03/2 | nan |

---

### `DATA\macro\fred_core_series.csv`

- **Size:** 0.0 MB (1,766 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 18
- **Columns:** 7

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 6 | series_id, title, units, frequency, last_date, source |
| Numeric | 1 | last_value |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**series_id** — Unique values: 18, Nulls: 0

| Value | Count |
|-------|-------|
| GDPC1 | 1 |
| CPIAUCSL | 1 |
| PCEPILFE | 1 |
| FEDFUNDS | 1 |
| DGS10 | 1 |
| T10Y2Y | 1 |
| BAMLC0A0CMEY | 1 |
| BAMLH0A0HYM2 | 1 |
| DTWEXBGS | 1 |
| DCOILWTICO | 1 |
| DHHNGSP | 1 |
| PCOPPUSDM | 1 |
| PLITUSDM | 1 |
| PCOBUSDM | 1 |
| UNRATE | 1 |

**title** — Unique values: 18, Nulls: 0

| Value | Count |
|-------|-------|
| Real Gross Domestic Product | 1 |
| Consumer Price Index for All Urban Consumers: All Items | 1 |
| Personal Consumption Expenditures: Chain-type Price Index Less Food and Energy | 1 |
| Federal Funds Effective Rate | 1 |
| 10-Year Treasury Constant Maturity Rate | 1 |
| 10-Year Treasury Constant Minus 2-Year Treasury Constant | 1 |
| ICE BofA US Corporate Index Effective Yield | 1 |
| ICE BofA US High Yield Index Effective Yield | 1 |
| Broad Trade Weighted U.S. Dollar Index: Broad | 1 |
| Crude Oil Prices: West Texas Intermediate (WTI) - Cushing Oklahoma | 1 |
| Henry Hub Natural Gas Spot Price | 1 |
| Global price of Copper | 1 |
| Global price of Lithium | 1 |
| Global price of Cobalt | 1 |
| Unemployment Rate | 1 |

**units** — Unique values: 11, Nulls: 0

| Value | Count |
|-------|-------|
| Percent | 6 |
| Index 2017=100 | 2 |
| U.S. Dollars per Metric Ton | 2 |
| Billions of Chained 2017 Dollars | 1 |
| Index 1982-1984=100 | 1 |
| Index 2006=100 | 1 |
| Dollars per Barrel | 1 |
| Dollars per Million BTU | 1 |
| U.S. Dollars per Pound | 1 |
| Thousands of Persons | 1 |
| Index 1st Qtr 1966=100 | 1 |

**frequency** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| Monthly | 9 |
| Daily | 8 |
| Quarterly | 1 |

**last_date** — Unique values: 4, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-07-01 | 8 |
| 2026-03-01 | 6 |
| 2026-06-01 | 3 |
| 2026-01-01 | 1 |

**source** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| FRED | 18 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| last_value | 12999.71 | 37681.88 | 0.35 | 158900.00 | 61.95 |

#### Sample Data (First 3 Rows)

| series_id | title | units | frequency | last_value | last_date | source |
| --- | --- | --- | --- | --- | --- | --- |
| GDPC1 | Real Gross Domestic Product | Billions of Chained 2017 Dollars | Quarterly | 23769.0 | 2026-01-01 | FRED |
| CPIAUCSL | Consumer Price Index for All Urban Consumers: All  | Index 1982-1984=100 | Monthly | 316.437 | 2026-03-01 | FRED |
| PCEPILFE | Personal Consumption Expenditures: Chain-type Pric | Index 2017=100 | Monthly | 123.4 | 2026-03-01 | FRED |

---

### `DATA\macro\fred_series_catalog.csv`

- **Size:** 0.0 MB (2,143 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 23
- **Columns:** 6

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 4 | frequency, units, source, last_updated |
| Numeric | 0 | — |
| Date | 0 | — |
| Text | 2 | series_id, series_name |

#### Category Column Details

**frequency** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| Monthly | 12 |
| Daily | 9 |
| Quarterly | 2 |

**units** — Unique values: 14, Nulls: 0

| Value | Count |
|-------|-------|
| Percent | 6 |
| U.S. Dollars per Metric Ton | 3 |
| Index 2017=100 | 2 |
| Dollars per Barrel | 2 |
| Billions of Chained 2017 Dollars | 1 |
| Index 1982-1984=100 | 1 |
| Index Jan 2006=100 | 1 |
| Dollars per Million BTU | 1 |
| Level in Thousands | 1 |
| Dollars per Hour | 1 |
| Index 1966Q1=100 | 1 |
| Percent of Capacity | 1 |
| Millions of Dollars | 1 |
| Billions of Dollars | 1 |

**source** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| FRED | 23 |

**last_updated** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-07-09 | 23 |

#### Sample Data (First 3 Rows)

| series_id | series_name | frequency | units | source | last_updated |
| --- | --- | --- | --- | --- | --- |
| GDPC1 | Real Gross Domestic Product | Quarterly | Billions of Chained 2017 Dollars | FRED | 2026-07-09 |
| CPIAUCSL | Consumer Price Index for All Urban Consumers | Monthly | Index 1982-1984=100 | FRED | 2026-07-09 |
| PCEPILFE | Personal Consumption Expenditures: Chain-type Pric | Monthly | Index 2017=100 | FRED | 2026-07-09 |

---

### `DATA\New folder\adoption\vendor_reported_metrics.csv`

- **Size:** 0.0 MB (2,370 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 31
- **Columns:** 6

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 3 | vendor, date, source |
| Numeric | 1 | confidence |
| Date | 0 | — |
| Text | 2 | metric, value |

#### Category Column Details

**vendor** — Unique values: 6, Nulls: 0

| Value | Count |
|-------|-------|
| microsoft | 11 |
| anthropic | 10 |
| google | 3 |
| meta | 3 |
| openai | 2 |
| aws | 2 |

**date** — Unique values: 11, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-02-01 | 8 |
| 2024-07-30 | 7 |
| 2026-04-30 | 4 |
| 2024-07-01 | 4 |
| 2025-09-04 | 2 |
| 2026-06-02 | 1 |
| 2024-10-15 | 1 |
| 2026-01-15 | 1 |
| 2025-09-01 | 1 |
| 2026-05-01 | 1 |
| 2025-07-01 | 1 |

**source** — Unique values: 13, Nulls: 0

| Value | Count |
|-------|-------|
| MSFT FY24 Q4 earnings | 7 |
| Anthropic pricing | 6 |
| Analytics Insight | 4 |
| Anthropic disclosure | 3 |
| Google Cloud ROI study | 2 |
| MSFT earnings calls | 2 |
| Reuters/Sensor Tower | 1 |
| MSFT earnings call | 1 |
| Similarweb | 1 |
| Google Cloud blog | 1 |
| re:Invent keynotes | 1 |
| AWS ML blog | 1 |
| Llama release blogs | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| confidence | 0.86 | 0.08 | 0.70 | 0.95 | 0.90 |

#### Sample Data (First 3 Rows)

| vendor | metric | date | value | source | confidence |
| --- | --- | --- | --- | --- | --- |
| openai | chatgpt_mau | 2026-06-02 | 1000000000 | Reuters/Sensor Tower | 0.9 |
| openai | chatgpt_plus_subscribers | 2024-10-15 | 11000000 | MSFT earnings call | 0.9 |
| anthropic | claude_ai_traffic_jan2026 | 2026-01-15 | 202900000 | Similarweb | 0.85 |

---

### `DATA\New folder\agents\deployment_counts.csv`

- **Size:** 0.0 MB (2,732 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 32
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 2 | agent_type, source |
| Numeric | 4 | agent_count, productivity_gain_pct, cost_savings_usd, roi_multiple |
| Date | 0 | — |
| Text | 3 | company, deployment_date, use_case |

#### Category Column Details

**agent_type** — Unique values: 11, Nulls: 0

| Value | Count |
|-------|-------|
| agentforce | 13 |
| copilot_m365 | 10 |
| gemini_enterprise | 1 |
| copilot | 1 |
| claude_enterprise | 1 |
| bedrock_agents | 1 |
| now_assist | 1 |
| fin | 1 |
| sierra_agents | 1 |
| ada_agents | 1 |
| decagon_agents | 1 |

**source** — Unique values: 13, Nulls: 0

| Value | Count |
|-------|-------|
| salesforce_customer_story | 11 |
| microsoft_customer_story | 9 |
| salesforce_press_release | 2 |
| google_cloud_next_2025 | 1 |
| microsoft_earnings_q2_2025 | 1 |
| github_blog | 1 |
| anthropic_blog | 1 |
| aws_reinvent | 1 |
| servicenow_press | 1 |
| intercom_case_study | 1 |
| sierra_blog | 1 |
| ada_case_study | 1 |
| decagon_blog | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| agent_count | 63287.56 | 139141.10 | 50.00 | 740000.00 | 6000.00 |
| productivity_gain_pct | 5.44 | 13.15 | 0.00 | 45.00 | 0.00 |
| cost_savings_usd | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| roi_multiple | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

#### Sample Data (First 3 Rows)

| company | deployment_date | agent_count | agent_type | use_case | productivity_gain_pct | cost_savings_usd | roi_multiple | source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google | 2025-01-15 | 1302 | gemini_enterprise | general_enterprise | 0 | 0 | 0 | google_cloud_next_2025 |
| salesforce | 2025-10-13 | 20000 | agentforce | customer_service_sales | 0 | 0 | 0 | salesforce_press_release |
| microsoft | 2025-01-30 | 150000 | copilot_m365 | productivity_suite | 0 | 0 | 0 | microsoft_earnings_q2_2025 |

---

### `DATA\New folder\china\api_pricing.csv`

- **Size:** 0.0 MB (2,217 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 31
- **Columns:** 8

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 3 | provider, date, source |
| Numeric | 4 | input_price_per_mtok, output_price_per_mtok, cached_input_price_per_mtok, context_window |
| Date | 0 | — |
| Text | 1 | model |

#### Category Column Details

**provider** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| zhipu-ai | 18 |
| baichuan | 7 |
| moonshot | 2 |
| 01.ai | 1 |
| alibaba | 1 |
| tencent | 1 |
| bytedance | 1 |

**date** — Unique values: 5, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-04-17 | 14 |
| 2026-06-11 | 11 |
| 2026-06-13 | 3 |
| 2026-06-16 | 2 |
| 2025-12-22 | 1 |

**source** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| z.ai pricing | 18 |
| AI_COST | 4 |
| ComputeUnion | 3 |
| toolcenter.ai | 2 |
| platform.01.ai | 1 |
| dashscope.aliyuncs.com | 1 |
| cloud.tencent.com | 1 |
| volcengine.com | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| input_price_per_mtok | 0.36 | 0.53 | 0.00 | 2.20 | 0.04 |
| output_price_per_mtok | 1.36 | 2.05 | 0.00 | 8.90 | 0.10 |
| cached_input_price_per_mtok | 0.06 | 0.11 | 0.00 | 0.45 | 0.00 |
| context_window | 396619.35 | 362689.41 | 128000.00 | 1000000.00 | 204800.00 |

#### Sample Data (First 3 Rows)

| provider | model | input_price_per_mtok | output_price_per_mtok | cached_input_price_per_mtok | context_window | date | source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| zhipu-ai | glm-5.2 | 1.0 | 3.2 | 0.2 | 1000000 | 2026-06-13 | z.ai pricing |
| zhipu-ai | glm-5-turbo | 1.2 | 4.0 | 0.24 | 1000000 | 2026-06-13 | z.ai pricing |
| zhipu-ai | glm-5-code | 1.2 | 5.0 | 0.3 | 1000000 | 2026-06-13 | z.ai pricing |

---

### `DATA\New folder\china\model_benchmarks.csv`

- **Size:** 0.0 MB (1,289 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 16
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 6 | model, organization, benchmark, date, category, language |
| Numeric | 3 | elo, ci_low, ci_high |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**model** — Unique values: 16, Nulls: 0

| Value | Count |
|-------|-------|
| glm-5.2 | 1 |
| glm-4.7 | 1 |
| deepseek-v4 | 1 |
| deepseek-r1 | 1 |
| qwen-3-max | 1 |
| qwen-3.5-397b-reasoning | 1 |
| yi-large | 1 |
| kimi-k2.5-thinking | 1 |
| kimi-k2 | 1 |
| baichuan-4 | 1 |
| ernie-5.0 | 1 |
| dola-seed-2.0-preview | 1 |
| step-1o | 1 |
| internvl-3-78b | 1 |
| glm-4v-plus | 1 |

**organization** — Unique values: 11, Nulls: 0

| Value | Count |
|-------|-------|
| zhipu-ai | 3 |
| deepseek | 2 |
| alibaba | 2 |
| moonshot | 2 |
| 01.ai | 1 |
| baichuan | 1 |
| baidu | 1 |
| bytedance | 1 |
| stepfun | 1 |
| shanghai-ai-lab | 1 |
| tencent | 1 |

**benchmark** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| lmsys_chatbot_arena | 11 |
| mmbench | 3 |
| opencompass | 2 |

**date** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-03-02 | 5 |
| 2026-06-01 | 3 |
| 2026-06-11 | 2 |
| 2026-04-17 | 2 |
| 2026-01-13 | 1 |
| 2026-04-14 | 1 |
| 2026-01-25 | 1 |
| 2025-12-31 | 1 |

**category** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| chat | 11 |
| multimodal | 3 |
| reasoning | 2 |

**language** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| zh/en | 16 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| elo | 1024.39 | 660.89 | 79.00 | 1549.00 | 1445.00 |
| ci_low | 1000.44 | 646.77 | 75.00 | 1509.00 | 1410.00 |
| ci_high | 1048.25 | 675.17 | 83.00 | 1589.00 | 1480.00 |

#### Sample Data (First 3 Rows)

| model | organization | benchmark | elo | ci_low | ci_high | date | category | language |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| glm-5.2 | zhipu-ai | lmsys_chatbot_arena | 1541.0 | 1506 | 1576 | 2026-03-02 | chat | zh/en |
| glm-4.7 | zhipu-ai | lmsys_chatbot_arena | 1541.0 | 1506 | 1576 | 2026-03-02 | chat | zh/en |
| deepseek-v4 | deepseek | lmsys_chatbot_arena | 1445.0 | 1410 | 1480 | 2026-06-01 | chat | zh/en |

---

### `DATA\New folder\labor\onet_ai_exposure.csv`

- **Size:** 0.01 MB (6,307 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 55
- **Columns:** 17

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 1 | education_level |
| Numeric | 14 | ai_exposure_felten_2021, ai_exposure_felten_2023, language_modeling_exposure, image_generation_exposure, reasoning_exposure, automation_probability, augmentation_probability, displacement_risk, wage_2023, employment_2023, task_count, routine_task_pct, abstract_task_pct, manual_task_pct |
| Date | 0 | — |
| Text | 2 | occupation_code, occupation_title |

#### Category Column Details

**education_level** — Unique values: 6, Nulls: 0

| Value | Count |
|-------|-------|
| bachelor | 23 |
| hs_diploma | 16 |
| doctorate | 6 |
| master | 5 |
| less_hs | 3 |
| associate | 2 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| ai_exposure_felten_2021 | 0.42 | 0.19 | 0.10 | 0.75 | 0.40 |
| ai_exposure_felten_2023 | 0.52 | 0.19 | 0.15 | 0.85 | 0.50 |
| language_modeling_exposure | 0.46 | 0.19 | 0.10 | 0.80 | 0.45 |
| image_generation_exposure | 0.15 | 0.09 | 0.05 | 0.60 | 0.15 |
| reasoning_exposure | 0.45 | 0.13 | 0.20 | 0.70 | 0.45 |
| automation_probability | 0.21 | 0.15 | 0.05 | 0.65 | 0.20 |
| augmentation_probability | 0.29 | 0.07 | 0.10 | 0.40 | 0.30 |
| displacement_risk | 0.21 | 0.15 | 0.05 | 0.65 | 0.20 |
| wage_2023 | 80927.27 | 46833.77 | 28000.00 | 300000.00 | 75000.00 |
| employment_2023 | 973818.18 | 938806.36 | 40000.00 | 3500000.00 | 700000.00 |
| task_count | 63.36 | 13.88 | 35.00 | 90.00 | 65.00 |
| routine_task_pct | 41.00 | 13.59 | 10.00 | 70.00 | 40.00 |
| abstract_task_pct | 44.91 | 17.68 | 10.00 | 85.00 | 50.00 |
| manual_task_pct | 14.09 | 7.14 | 5.00 | 30.00 | 10.00 |

#### Sample Data (First 3 Rows)

| occupation_code | occupation_title | ai_exposure_felten_2021 | ai_exposure_felten_2023 | language_modeling_exposure | image_generation_exposure | reasoning_exposure | automation_probability | augmentation_probability | displacement_risk | wage_2023 | employment_2023 | education_level | task_count | routine_task_pct | abstract_task_pct | manual_task_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 11-1011 | Chief Executives | 0.12 | 0.15 | 0.1 | 0.05 | 0.2 | 0.05 | 0.1 | 0.05 | 300000 | 280000 | doctorate | 50 | 10 | 85 | 5 |
| 11-3021 | Computer and Information Systems Managers | 0.45 | 0.55 | 0.4 | 0.2 | 0.5 | 0.15 | 0.3 | 0.15 | 180000 | 500000 | bachelor | 80 | 20 | 70 | 10 |
| 13-1111 | Management Analysts | 0.6 | 0.7 | 0.65 | 0.15 | 0.6 | 0.25 | 0.4 | 0.25 | 95000 | 750000 | bachelor | 60 | 30 | 60 | 10 |

---

### `DATA\New folder\productivity\meta_analysis_studies.csv`

- **Size:** 0.0 MB (2,027 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 20
- **Columns:** 11

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 3 | category, model, doi |
| Numeric | 6 | n_sample, effect_size_pct, ci_low, ci_high, quality_score, publication_year |
| Date | 0 | — |
| Text | 2 | study, task_type |

#### Category Column Details

**category** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| coding | 9 |
| customersupport | 3 |
| writing | 2 |
| consulting | 2 |
| legal | 1 |
| materials | 1 |
| pharma | 1 |
| devops | 1 |

**model** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| github_copilot | 7 |
| gpt4 | 3 |
| gpt_based_assistant | 3 |
| chatgpt | 2 |
| gpt_based | 2 |
| various | 2 |
| codex | 1 |

**doi** — Unique values: 11, Nulls: 0

| Value | Count |
|-------|-------|
| SSRN | 6 |
| 10.48550/arXiv.2302.06590 | 2 |
| 10.1126/science.adh2586 | 2 |
| NBER.w31161 | 2 |
| Microsoft Research | 2 |
| SSRN.4573321 | 1 |
| QJE.2024 | 1 |
| SSRN.4945566 | 1 |
| Accenture Research | 1 |
| DORA Report | 1 |
| Stack Overflow | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| n_sample | 3931.75 | 11010.72 | 95.00 | 50000.00 | 444.00 |
| effect_size_pct | 24.77 | 15.19 | 0.00 | 55.80 | 25.00 |
| ci_low | 16.36 | 11.00 | 0.00 | 40.00 | 15.00 |
| ci_high | 33.09 | 21.06 | 0.00 | 89.00 | 32.00 |
| quality_score | 0.86 | 0.07 | 0.70 | 0.95 | 0.85 |
| publication_year | 2023.50 | 0.83 | 2022.00 | 2025.00 | 2023.00 |

#### Sample Data (First 3 Rows)

| study | category | task_type | model | n_sample | effect_size_pct | ci_low | ci_high | quality_score | publication_year | doi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| peng_2023 | coding | http_server_implementation | github_copilot | 95 | 55.8 | 21.0 | 89.0 | 0.9 | 2023 | 10.48550/arXiv.2302.06590 |
| noy_zhang_2023 | writing | professional_writing_tasks | chatgpt | 444 | 37.0 | 28.0 | 46.0 | 0.95 | 2023 | 10.1126/science.adh2586 |
| dellacqua_2023 | consulting | complex_consulting_tasks | gpt4 | 758 | 12.0 | 8.0 | 16.0 | 0.9 | 2023 | SSRN.4573321 |

---

### `DATA\New folder\regulatory\jurisdiction_rule_matrix.csv`

- **Size:** 0.0 MB (3,570 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 20
- **Columns:** 12

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 7 | jurisdiction, regulation, tier, status, effective_date, cost_unit, source |
| Numeric | 4 | compliance_cost_low, compliance_cost_median, compliance_cost_high, enforcement_probability |
| Date | 0 | — |
| Text | 1 | requirements |

#### Category Column Details

**jurisdiction** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| eu | 7 |
| us | 6 |
| china | 3 |
| uk | 1 |
| india | 1 |
| uae | 1 |
| ksa | 1 |

**regulation** — Unique values: 17, Nulls: 0

| Value | Count |
|-------|-------|
| ai_act | 4 |
| gdpr_art22 | 1 |
| dsa | 1 |
| dma | 1 |
| eo_14110 | 1 |
| nist_rmf | 1 |
| sec_ai_disclosure | 1 |
| copyright_nyt_v_openai | 1 |
| bis_3a090_4a090 | 1 |
| bis_ai_diffusion | 1 |
| interim_measures_genai | 1 |
| data_security_law | 1 |
| pipil | 1 |
| ai_white_paper | 1 |
| dpdp_act | 1 |

**tier** — Unique values: 19, Nulls: 0

| Value | Count |
|-------|-------|
| active | 2 |
| high_risk | 1 |
| gpai_systemic | 1 |
| gpai_standard | 1 |
| prohibited | 1 |
| automated_decisions | 1 |
| vlop | 1 |
| gatekeeper | 1 |
| ai_safety | 1 |
| voluntary | 1 |
| public_cos | 1 |
| litigation | 1 |
| export_controls | 1 |
| global_licensing | 1 |
| filing_required | 1 |

**status** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| active | 18 |
| banned | 1 |
| suspended | 1 |

**effective_date** — Unique values: 18, Nulls: 0

| Value | Count |
|-------|-------|
| 2025-08-02 | 2 |
| 2023-01-01 | 2 |
| 2026-08-02 | 1 |
| 2025-02-02 | 1 |
| 2018-05-25 | 1 |
| 2024-08-25 | 1 |
| 2024-03-06 | 1 |
| 2023-10-30 | 1 |
| 2024-01-01 | 1 |
| 2023-12-27 | 1 |
| 2025-01-16 | 1 |
| 2025-05-01 | 1 |
| 2023-08-15 | 1 |
| 2021-09-01 | 1 |
| 2021-11-01 | 1 |

**cost_unit** — Unique values: 14, Nulls: 0

| Value | Count |
|-------|-------|
| eur_per_model_per_year | 4 |
| eur_per_year | 2 |
| usd_per_license | 2 |
| cny_per_org_per_year | 2 |
| eur_per_system_per_year | 1 |
| usd_per_model_per_year | 1 |
| usd_per_org_per_year | 1 |
| usd_per_filing | 1 |
| usd_per_case | 1 |
| cny_per_model_per_year | 1 |
| gbp_per_model_per_year | 1 |
| inr_per_org_per_year | 1 |
| aed_per_model_per_year | 1 |
| sar_per_model_per_year | 1 |

**source** — Unique values: 17, Nulls: 0

| Value | Count |
|-------|-------|
| cranium_ai_blog | 2 |
| ec_enforcement | 2 |
| csaregulations | 2 |
| eu_commission_impact_assessment | 1 |
| eu_ai_act_text | 1 |
| dpaguidance | 1 |
| whitehouse_factsheet | 1 |
| nist_publication | 1 |
| sec_guidance | 1 |
| court_filings | 1 |
| bis_federal_register | 1 |
| bis_guidance_june2025 | 1 |
| cac_filings | 1 |
| dsit_consultation | 1 |
| meity_draft | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| compliance_cost_low | 195500.00 | 310194.76 | 0.00 | 1000000.00 | 50000.00 |
| compliance_cost_median | 1162500.00 | 2386082.18 | 0.00 | 10000000.00 | 200000.00 |
| compliance_cost_high | 7960000.00 | 22217593.79 | 0.00 | 100000000.00 | 1000000.00 |
| enforcement_probability | 0.77 | 0.24 | 0.00 | 1.00 | 0.82 |

#### Sample Data (First 3 Rows)

| jurisdiction | regulation | tier | status | effective_date | requirements | compliance_cost_low | compliance_cost_median | compliance_cost_high | cost_unit | enforcement_probability | source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| eu | ai_act | high_risk | active | 2026-08-02 | conformity_assessment,risk_management,data_governa | 50000 | 200000 | 1000000 | eur_per_model_per_year | 0.9 | eu_commission_impact_assessment |
| eu | ai_act | gpai_systemic | active | 2025-08-02 | technical_documentation,transparency_reports,train | 100000 | 500000 | 2000000 | eur_per_model_per_year | 0.95 | cranium_ai_blog |
| eu | ai_act | gpai_standard | active | 2025-08-02 | technical_documentation,transparency_reports,train | 25000 | 100000 | 500000 | eur_per_model_per_year | 0.9 | cranium_ai_blog |

---

### `DATA\New folder\revenue_quality\cloud_contract_mapping.csv`

- **Size:** 0.0 MB (3,692 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 33
- **Columns:** 15

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 7 | provider, quality_tier, upfront_option, capacity_reservation, typical_customer_segment, date, source |
| Numeric | 7 | price_discount_pct, commitment_term_years, flexibility_score, switching_cost_score, annual_churn_pct, expansion_rate_pct, nrr_pct |
| Date | 0 | — |
| Text | 1 | contract_type |

#### Category Column Details

**provider** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| aws | 17 |
| azure | 9 |
| gcp | 7 |

**quality_tier** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| high | 21 |
| medium | 8 |
| low | 4 |

**upfront_option** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| reserved | 12 |
| savings_plan | 8 |
| none | 4 |
| spend | 3 |
| ea | 2 |
| marketplace | 1 |
| services | 1 |
| license | 1 |
| auto | 1 |

**capacity_reservation** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| yes | 17 |
| none | 16 |

**typical_customer_segment** — Unique values: 6, Nulls: 0

| Value | Count |
|-------|-------|
| enterprise | 21 |
| established | 5 |
| startups/small | 3 |
| growing | 2 |
| batch/fault_tolerant | 1 |
| steady | 1 |

**date** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2025-01-01 | 33 |

**source** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| aws_pricing | 14 |
| azure_pricing | 8 |
| gcp_pricing | 7 |
| aws_ea | 1 |
| aws_marketplace | 1 |
| aws_services | 1 |
| azure_ea | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| price_discount_pct | 36.52 | 23.48 | 0.00 | 90.00 | 40.00 |
| commitment_term_years | 1.70 | 1.19 | 0.00 | 3.00 | 1.00 |
| flexibility_score | 0.44 | 0.26 | 0.10 | 1.00 | 0.40 |
| switching_cost_score | 3.61 | 1.22 | 1.00 | 5.00 | 4.00 |
| annual_churn_pct | 0.11 | 0.09 | 0.02 | 0.50 | 0.08 |
| expansion_rate_pct | 0.32 | 0.10 | 0.05 | 0.50 | 0.35 |
| nrr_pct | 1.31 | 0.11 | 1.05 | 1.50 | 1.35 |

#### Sample Data (First 3 Rows)

| provider | contract_type | quality_tier | price_discount_pct | commitment_term_years | upfront_option | capacity_reservation | flexibility_score | switching_cost_score | typical_customer_segment | annual_churn_pct | expansion_rate_pct | nrr_pct | date | source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aws | on_demand | low | 0 | 0 | none | none | 1.0 | 1 | startups/small | 0.25 | 0.15 | 1.1 | 2025-01-01 | aws_pricing |
| aws | savings_plan_1yr_no_upfront | medium | 27 | 1 | savings_plan | none | 0.7 | 3 | growing | 0.15 | 0.25 | 1.25 | 2025-01-01 | aws_pricing |
| aws | savings_plan_1yr_partial_upfront | medium | 37 | 1 | savings_plan | none | 0.6 | 3 | established | 0.12 | 0.28 | 1.28 | 2025-01-01 | aws_pricing |

---

### `DATA\New folder\revenue_quality\saas_benchmarks.csv`

- **Size:** 0.0 MB (1,360 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 11
- **Columns:** 20

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 2 | arr_band, source |
| Numeric | 18 | arr_min, arr_max, nrr_median, nrr_p25, nrr_p75, grr_median, grr_p25, grr_p75, logo_churn_pct, expansion_rate_pct, gross_margin_pct, sm_magic_number, cac_payback_months, ltv_cac_ratio, rule_of_40_pct, net_dollar_retention_pct, sample_size, year |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**arr_band** — Unique values: 11, Nulls: 0

| Value | Count |
|-------|-------|
| 0_1M | 1 |
| 1M_3M | 1 |
| 3M_5M | 1 |
| 5M_10M | 1 |
| 10M_25M | 1 |
| 25M_50M | 1 |
| 50M_100M | 1 |
| 100M_250M | 1 |
| 250M_500M | 1 |
| 500M_1B | 1 |
| 1B_plus | 1 |

**source** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| saas_capital | 11 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| arr_min | 176727272.73 | 313401050.06 | 0.00 | 1000000000.00 | 25000000.00 |
| arr_max | 1085818181.82 | 2972486293.26 | 1000000.00 | 10000000000.00 | 50000000.00 |
| nrr_median | 120.00 | 6.63 | 110.00 | 130.00 | 120.00 |
| nrr_p25 | 115.00 | 6.63 | 105.00 | 125.00 | 115.00 |
| nrr_p75 | 130.00 | 6.63 | 120.00 | 140.00 | 130.00 |
| grr_median | 100.00 | 3.32 | 95.00 | 105.00 | 100.00 |
| grr_p25 | 95.91 | 3.48 | 90.00 | 101.00 | 96.00 |
| grr_p75 | 104.09 | 3.18 | 100.00 | 109.00 | 104.00 |
| logo_churn_pct | 0.05 | 0.04 | 0.01 | 0.12 | 0.05 |
| expansion_rate_pct | 0.28 | 0.07 | 0.18 | 0.38 | 0.28 |
| gross_margin_pct | 0.84 | 0.03 | 0.78 | 0.89 | 0.84 |
| sm_magic_number | 2.35 | 1.26 | 0.80 | 4.50 | 2.00 |
| cac_payback_months | 6.27 | 3.23 | 2.00 | 12.00 | 6.00 |
| ltv_cac_ratio | 5.32 | 1.30 | 3.50 | 7.50 | 5.00 |
| rule_of_40_pct | 49.73 | 8.68 | 35.00 | 62.00 | 50.00 |
| net_dollar_retention_pct | 120.00 | 6.63 | 110.00 | 130.00 | 120.00 |
| sample_size | 50.18 | 24.29 | 12.00 | 89.00 | 52.00 |
| year | 2024.00 | 0.00 | 2024.00 | 2024.00 | 2024.00 |

#### Sample Data (First 3 Rows)

| arr_band | arr_min | arr_max | nrr_median | nrr_p25 | nrr_p75 | grr_median | grr_p25 | grr_p75 | logo_churn_pct | expansion_rate_pct | gross_margin_pct | sm_magic_number | cac_payback_months | ltv_cac_ratio | rule_of_40_pct | net_dollar_retention_pct | sample_size | source | year |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0_1M | 0 | 1000000 | 110 | 105 | 120 | 95 | 90 | 100 | 0.12 | 0.18 | 0.78 | 0.8 | 12 | 3.5 | 35 | 110 | 45 | saas_capital | 2024 |
| 1M_3M | 1000000 | 3000000 | 112 | 107 | 122 | 96 | 92 | 100 | 0.1 | 0.2 | 0.8 | 1.0 | 10 | 4.0 | 40 | 112 | 67 | saas_capital | 2024 |
| 3M_5M | 3000000 | 5000000 | 114 | 109 | 124 | 97 | 93 | 101 | 0.08 | 0.22 | 0.81 | 1.2 | 9 | 4.2 | 42 | 114 | 52 | saas_capital | 2024 |

---

### `DATA\New folder\semiconductor\supply_chain_quarterly.csv`

- **Size:** 0.0 MB (1,037 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 13
- **Columns:** 12

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 1 | quarter |
| Numeric | 11 | tsmc_3nm_monthly_wafers, tsmc_4nm_5nm_monthly_wafers, tsmc_cowos_monthly_wafers, tsmc_cowos_l_pct, tsmc_cowos_s_pct, nvidia_h100_shipments, amd_mi300_shipments, hbm3e_monthly_units, coWos_capacity_kwpm, coWos_demand_kwpm, gap_pct |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**quarter** — Unique values: 13, Nulls: 0

| Value | Count |
|-------|-------|
| 2023Q4 | 1 |
| 2024Q1 | 1 |
| 2024Q2 | 1 |
| 2024Q3 | 1 |
| 2024Q4 | 1 |
| 2025Q1 | 1 |
| 2025Q2 | 1 |
| 2025Q3 | 1 |
| 2025Q4 | 1 |
| 2026Q1 | 1 |
| 2026Q2 | 1 |
| 2026Q3 | 1 |
| 2026Q4 | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| tsmc_3nm_monthly_wafers | 93461.54 | 78511.80 | 0.00 | 180000.00 | 130000.00 |
| tsmc_4nm_5nm_monthly_wafers | 154615.38 | 129332.61 | 0.00 | 290000.00 | 220000.00 |
| tsmc_cowos_monthly_wafers | 58615.38 | 34272.29 | 14000.00 | 115000.00 | 55000.00 |
| tsmc_cowos_l_pct | 0.62 | 0.19 | 0.30 | 0.85 | 0.65 |
| tsmc_cowos_s_pct | 0.38 | 0.19 | 0.15 | 0.70 | 0.35 |
| nvidia_h100_shipments | 1776923.08 | 926601.18 | 500000.00 | 3200000.00 | 1800000.00 |
| amd_mi300_shipments | 215384.62 | 108271.68 | 50000.00 | 375000.00 | 225000.00 |
| hbm3e_monthly_units | 54230.77 | 45085.39 | 0.00 | 120000.00 | 60000.00 |
| coWos_capacity_kwpm | 58.62 | 34.27 | 14.00 | 115.00 | 55.00 |
| coWos_demand_kwpm | 73.85 | 24.76 | 35.00 | 110.00 | 75.00 |
| gap_pct | 27.55 | 22.57 | -4.50 | 62.50 | 26.70 |

#### Sample Data (First 3 Rows)

| quarter | tsmc_3nm_monthly_wafers | tsmc_4nm_5nm_monthly_wafers | tsmc_cowos_monthly_wafers | tsmc_cowos_l_pct | tsmc_cowos_s_pct | nvidia_h100_shipments | amd_mi300_shipments | hbm3e_monthly_units | coWos_capacity_kwpm | coWos_demand_kwpm | gap_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2023Q4 | 0 | 0 | 14000 | 0.3 | 0.7 | 500000 | 50000 | 0 | 14 | 35 | 60.0 |
| 2024Q1 | 0 | 0 | 15000 | 0.3 | 0.7 | 600000 | 75000 | 0 | 15 | 40 | 62.5 |
| 2024Q2 | 0 | 0 | 25000 | 0.4 | 0.6 | 800000 | 100000 | 0 | 25 | 50 | 50.0 |

---

### `DATA\New folder\stress_scenarios\historical_backtest.csv`

- **Size:** 0.0 MB (1,804 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 9
- **Columns:** 16

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 6 | episode, start_date, end_date, trigger, key_drivers, calibration_notes |
| Numeric | 10 | pre_crisis_valuation, post_crisis_valuation, peak_to_trough_pct, duration_months, recovery_months, model_predicted_trough, model_predicted_recovery, rmse, mae, directional_accuracy |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**episode** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| dotcom | 1 |
| telecom | 1 |
| japan | 1 |
| railway | 1 |
| gfc | 1 |
| cloud | 1 |
| smartphone | 1 |
| semi_2018 | 1 |
| semi_2000 | 1 |

**start_date** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| 1999-03-01 | 2 |
| 1989-12-01 | 1 |
| 1845-01-01 | 1 |
| 2007-10-01 | 1 |
| 2006-01-01 | 1 |
| 2007-01-01 | 1 |
| 2018-01-01 | 1 |
| 2000-03-01 | 1 |

**end_date** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| 2002-10-01 | 2 |
| 2003-03-01 | 1 |
| 1850-12-01 | 1 |
| 2009-03-01 | 1 |
| 2024-01-01 | 1 |
| 2021-01-01 | 1 |
| 2019-12-01 | 1 |
| 2001-12-01 | 1 |

**trigger** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| excessive_valuation | 1 |
| fiber_overbuild | 1 |
| asset_bubble | 1 |
| mania | 1 |
| housing_crisis | 1 |
| gradual_adoption | 1 |
| product_cycle | 1 |
| inventory_correction | 1 |
| dotcom_crash | 1 |

**key_drivers** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| excessive valuation, revenue-less IPOs, Fed tightening | 1 |
| excessive capex, demand overestimation, debt overhang | 1 |
| monetary tightening, demographic shift, zombie firms | 1 |
| speculative frenzy, overbuilding, regulatory crackdown | 1 |
| subprime mortgages, leverage, securitization | 1 |
| gradual adoption, enterprise migration, network effects | 1 |
| iPhone launch, app ecosystem, saturation | 1 |
| memory oversupply, trade tension, demand normalization | 1 |
| dotcom crash, inventory correction, demand collapse | 1 |

**calibration_notes** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| good fit on duration; underestimated depth | 1 |
| overestimated recovery speed | 1 |
| structural factors not fully captured | 1 |
| limited data quality | 1 |
| good fit; credit channel well captured | 1 |
| long adoption curve well modeled | 1 |
| S-curve adoption well captured | 1 |
| cyclical dynamics captured | 1 |
| severity underestimated | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| pre_crisis_valuation | 5481.67 | 12667.29 | 0.00 | 39000.00 | 1200.00 |
| post_crisis_valuation | 278934.56 | 564559.50 | 15.00 | 1500000.00 | 676.00 |
| peak_to_trough_pct | -53.89 | 34.86 | -85.00 | 0.00 | -67.00 |
| duration_months | 85.11 | 75.31 | 17.00 | 216.00 | 44.00 |
| recovery_months | 71.00 | 76.60 | 0.00 | 240.00 | 48.00 |
| model_predicted_trough | 251302.22 | 514076.78 | 20.00 | 1400000.00 | 750.00 |
| model_predicted_recovery | 58.56 | 58.97 | 0.00 | 180.00 | 42.00 |
| rmse | 0.14 | 0.05 | 0.06 | 0.22 | 0.14 |
| mae | 0.80 | 0.28 | 0.38 | 1.25 | 0.85 |
| directional_accuracy | 0.88 | 0.09 | 0.70 | 0.98 | 0.92 |

#### Sample Data (First 3 Rows)

| episode | start_date | end_date | trigger | pre_crisis_valuation | post_crisis_valuation | peak_to_trough_pct | duration_months | recovery_months | key_drivers | model_predicted_trough | model_predicted_recovery | rmse | mae | directional_accuracy | calibration_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dotcom | 1999-03-01 | 2002-10-01 | excessive_valuation | 5000 | 1100 | -78 | 44 | 87 | excessive valuation, revenue-less IPOs, Fed tighte | 1200 | 90 | 0.12 | 0.85 | 0.92 | good fit on duration; underestimated depth |
| telecom | 1999-03-01 | 2002-10-01 | fiber_overbuild | 2000 | 300 | -85 | 44 | 96 | excessive capex, demand overestimation, debt overh | 400 | 80 | 0.15 | 0.92 | 0.88 | overestimated recovery speed |
| japan | 1989-12-01 | 2003-03-01 | asset_bubble | 39000 | 7600 | -81 | 159 | 240 | monetary tightening, demographic shift, zombie fir | 8500 | 180 | 0.18 | 1.25 | 0.75 | structural factors not fully captured |

---

### `DATA\New folder\stress_scenarios\scenario_matrix.csv`

- **Size:** 0.0 MB (3,268 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 27
- **Columns:** 10

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 0 | — |
| Numeric | 7 | probability, pA_agentic_tco, pB_ppp_pricing, pC_phys_infra, pD_contract_cliff, pE_val_multiple, horizon_years |
| Date | 0 | — |
| Text | 3 | scenario_name, description, key_assumptions |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| probability | 0.05 | 0.07 | 0.01 | 0.35 | 0.03 |
| pA_agentic_tco | 1.27 | 0.33 | 0.80 | 2.00 | 1.00 |
| pB_ppp_pricing | 1.27 | 0.33 | 0.80 | 2.00 | 1.00 |
| pC_phys_infra | 1.27 | 0.33 | 0.80 | 2.00 | 1.00 |
| pD_contract_cliff | 1.27 | 0.33 | 0.80 | 2.00 | 1.00 |
| pE_val_multiple | 1.21 | 0.33 | 0.80 | 2.00 | 1.00 |
| horizon_years | 5.00 | 0.00 | 5.00 | 5.00 | 5.00 |

#### Sample Data (First 3 Rows)

| scenario_name | description | probability | pA_agentic_tco | pB_ppp_pricing | pC_phys_infra | pD_contract_cliff | pE_val_multiple | horizon_years | key_assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline | Baseline: all perspectives at median | 0.35 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 5 | current trends persist |
| optimistic | Optimistic: favorable on all fronts | 0.1 | 0.8 | 0.8 | 0.8 | 0.8 | 0.8 | 5 | productivity gains accelerate; infra constraints e |
| pessimistic | Pessimistic: adverse on all fronts | 0.15 | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 5 | TCO inflation; pricing pressure; infra bottlenecks |

---

### `DATA\New folder\stress_scenarios\stress_scenarios.csv`

- **Size:** 0.0 MB (2,343 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 20
- **Columns:** 16

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 3 | category, correlation_structure, source |
| Numeric | 11 | probability_annual, gdp_shock_pct, unemployment_delta_pct, credit_spread_mult, equity_shock_pct, energy_shock_pct, semiconductor_shock_pct, regulation_shock, cyber_shock, ai_safety_shock, duration_quarters |
| Date | 0 | — |
| Text | 2 | scenario_id, scenario_name |

#### Category Column Details

**category** — Unique values: 10, Nulls: 0

| Value | Count |
|-------|-------|
| technology | 5 |
| macroeconomic | 2 |
| supply_shock | 2 |
| geopolitical | 2 |
| policy | 2 |
| energy | 2 |
| combined | 2 |
| cyber | 1 |
| financial | 1 |
| health | 1 |

**correlation_structure** — Unique values: 18, Nulls: 0

| Value | Count |
|-------|-------|
| global_correlation | 3 |
| regional_correlation | 1 |
| regional_EU_heavy | 1 |
| TSMC_concentration | 1 |
| cloud_concentration | 1 |
| regulatory_response | 1 |
| jurisdiction_specific | 1 |
| innovation_diffusion | 1 |
| manufacturing_roadmap | 1 |
| NIST timeline | 1 |
| ITER/DOE | 1 |
| supply_demand_mismatch | 1 |
| policy_correlation | 1 |
| election_cycle | 1 |
| worst_case | 1 |

**source** — Unique values: 19, Nulls: 0

| Value | Count |
|-------|-------|
| Historical | 2 |
| IMF/NBER | 1 |
| IEA/OECD | 1 |
| SemiAnalysis | 1 |
| CSIS/RAND | 1 |
| Verizon DBIR/Ponemon | 1 |
| Expert elicitation | 1 |
| BIS/IMF | 1 |
| Legal analysis | 1 |
| Patent analysis | 1 |
| IRDS/TSMC | 1 |
| NIST | 1 |
| DOE/IAEA | 1 |
| 1970s analogue | 1 |
| Policy analysis | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| probability_annual | 0.05 | 0.05 | 0.01 | 0.20 | 0.03 |
| gdp_shock_pct | -2.19 | 3.09 | -12.00 | 0.50 | -1.00 |
| unemployment_delta_pct | 1.51 | 1.97 | -0.50 | 7.00 | 0.75 |
| credit_spread_mult | 1.83 | 1.08 | 0.70 | 5.00 | 1.50 |
| equity_shock_pct | -21.00 | 19.24 | -60.00 | 15.00 | -20.00 |
| energy_shock_pct | 49.50 | 72.53 | -50.00 | 250.00 | 30.00 |
| semiconductor_shock_pct | -10.00 | 28.10 | -90.00 | 20.00 | 0.00 |
| regulation_shock | 0.35 | 0.49 | 0.00 | 1.00 | 0.00 |
| cyber_shock | 0.05 | 0.22 | 0.00 | 1.00 | 0.00 |
| ai_safety_shock | 0.10 | 0.31 | 0.00 | 1.00 | 0.00 |
| duration_quarters | 10.60 | 8.08 | 4.00 | 40.00 | 8.00 |

#### Sample Data (First 3 Rows)

| scenario_id | scenario_name | category | probability_annual | gdp_shock_pct | unemployment_delta_pct | credit_spread_mult | equity_shock_pct | energy_shock_pct | semiconductor_shock_pct | regulation_shock | cyber_shock | ai_safety_shock | duration_quarters | correlation_structure | source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| s1 | Global Recession | macroeconomic | 0.15 | -4.0 | 3.5 | 2.5 | -35 | 20 | 0 | 0 | 0 | 0 | 8 | regional_correlation | IMF/NBER |
| s2 | Energy Crisis | supply_shock | 0.05 | -2.0 | 1.5 | 1.8 | -20 | 150 | 0 | 0 | 0 | 0 | 6 | regional_EU_heavy | IEA/OECD |
| s3 | Semiconductor Supply Disruption | supply_shock | 0.03 | -1.5 | 1.0 | 1.5 | -25 | 30 | -40 | 0 | 0 | 0 | 8 | TSMC_concentration | SemiAnalysis |

---

### `DATA\New folder\unit_economics\gpu_economics.csv`

- **Size:** 0.0 MB (1,896 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 17
- **Columns:** 13

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 5 | provider, gpu_type, form_factor, date, source |
| Numeric | 8 | hourly_price_usd, annual_price_usd_1yr, annual_price_usd_3yr, memory_gb, memory_bandwidth_gbps, tflops_fp16, tflops_bf16, nvlink_gbps |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**provider** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| onprem | 4 |
| aws | 3 |
| azure | 2 |
| gcp | 2 |
| lambda | 2 |
| runpod | 2 |
| coreweave | 2 |

**gpu_type** — Unique values: 14, Nulls: 0

| Value | Count |
|-------|-------|
| 8x A100 80GB | 3 |
| 8x H100 | 2 |
| p5.48xlarge (8x H100) | 1 |
| p4d.24xlarge (8x A100) | 1 |
| p4de.24xlarge (8x A100 80GB) | 1 |
| ND96asr_v4 (8x A100) | 1 |
| ND96amsr_A100_v4 (8x A100 80GB) | 1 |
| a2-ultragpu-8g (8x A100) | 1 |
| a3-highgpu-8g (8x H100) | 1 |
| 8x H100 SXM | 1 |
| h100_80gb_sxm | 1 |
| h100_80gb_pcie | 1 |
| a100_80gb_sxm | 1 |
| a100_80gb_pcie | 1 |

**form_factor** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| 8x GPU server | 13 |
| GPU card | 4 |

**date** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-01-01 | 17 |

**source** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| NVIDIA list price | 4 |
| AWS pricing | 3 |
| Azure pricing | 2 |
| GCP pricing | 2 |
| Lambda Labs | 2 |
| RunPod | 2 |
| CoreWeave | 2 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| hourly_price_usd | 4136.11 | 8511.70 | 9.00 | 25000.00 | 31.00 |
| annual_price_usd_1yr | 165832.41 | 120764.68 | 10000.00 | 358810.00 | 131400.00 |
| annual_price_usd_3yr | 437061.18 | 332314.28 | 10000.00 | 961920.00 | 352000.00 |
| memory_gb | 508.24 | 244.85 | 80.00 | 640.00 | 640.00 |
| memory_bandwidth_gbps | 2214.71 | 870.76 | 1555.00 | 3350.00 | 1555.00 |
| tflops_fp16 | 1813.29 | 1849.61 | 312.00 | 3958.00 | 312.00 |
| tflops_bf16 | 3626.59 | 3699.23 | 624.00 | 7916.00 | 624.00 |
| nvlink_gbps | 705.88 | 147.78 | 600.00 | 900.00 | 600.00 |

#### Sample Data (First 3 Rows)

| provider | gpu_type | hourly_price_usd | annual_price_usd_1yr | annual_price_usd_3yr | memory_gb | memory_bandwidth_gbps | tflops_fp16 | tflops_bf16 | nvlink_gbps | form_factor | date | source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aws | p5.48xlarge (8x H100) | 30.6 | 268056 | 718960 | 640 | 3350 | 3958 | 7916 | 900 | 8x GPU server | 2026-01-01 | AWS pricing |
| aws | p4d.24xlarge (8x A100) | 32.77 | 287065 | 769500 | 640 | 1555 | 312 | 624 | 600 | 8x GPU server | 2026-01-01 | AWS pricing |
| aws | p4de.24xlarge (8x A100 80GB) | 40.96 | 358810 | 961920 | 640 | 1555 | 312 | 624 | 600 | 8x GPU server | 2026-01-01 | AWS pricing |

---

### `DATA\New folder\unit_economics\inference_costs.csv`

- **Size:** 0.0 MB (2,937 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 25
- **Columns:** 16

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 4 | provider, hardware, date, source |
| Numeric | 11 | input_price_per_1m_tokens, output_price_per_1m_tokens, cached_input_price_per_1m_tokens, context_window_tokens, max_output_tokens, throughput_tokens_per_sec, avg_latency_ms, utilization_pct, hw_cost_per_hour, effective_input_per_1m, effective_output_per_1m |
| Date | 0 | — |
| Text | 1 | model |

#### Category Column Details

**provider** — Unique values: 10, Nulls: 0

| Value | Count |
|-------|-------|
| openai | 4 |
| anthropic | 3 |
| google | 3 |
| meta | 3 |
|  mistral | 3 |
| alibaba | 3 |
| deepseek | 2 |
| zhipu | 2 |
| moonshot | 1 |
| 01.ai | 1 |

**hardware** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| h100 | 20 |
| tpu_v5 | 3 |
| h800 | 2 |

**date** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2025-01-01 | 25 |

**source** — Unique values: 10, Nulls: 0

| Value | Count |
|-------|-------|
| openai_pricing | 4 |
| anthropic_pricing | 3 |
| google_pricing | 3 |
| meta_blog | 3 |
| mistral_pricing | 3 |
| alibaba_pricing | 3 |
| deepseek_pricing | 2 |
| zhipu_pricing | 2 |
| moonshot_pricing | 1 |
| yi_pricing | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| input_price_per_1m_tokens | 1.72 | 3.54 | 0.00 | 15.00 | 0.40 |
| output_price_per_1m_tokens | 6.90 | 15.76 | 0.00 | 75.00 | 1.50 |
| cached_input_price_per_1m_tokens | 0.59 | 1.26 | 0.00 | 5.00 | 0.10 |
| context_window_tokens | 340907.56 | 477766.70 | 16385.00 | 2000000.00 | 128000.00 |
| max_output_tokens | 8028.16 | 2205.76 | 4096.00 | 16384.00 | 8192.00 |
| throughput_tokens_per_sec | 80.40 | 29.51 | 40.00 | 150.00 | 70.00 |
| avg_latency_ms | 13.91 | 4.47 | 6.70 | 25.00 | 14.30 |
| utilization_pct | 70.00 | 0.00 | 70.00 | 70.00 | 70.00 |
| hw_cost_per_hour | 4.30 | 0.41 | 3.50 | 4.50 | 4.50 |
| effective_input_per_1m | 2.23 | 4.58 | 0.00 | 19.29 | 0.51 |
| effective_output_per_1m | 8.93 | 20.32 | 0.00 | 96.43 | 1.93 |

#### Sample Data (First 3 Rows)

| model | provider | input_price_per_1m_tokens | output_price_per_1m_tokens | cached_input_price_per_1m_tokens | context_window_tokens | max_output_tokens | throughput_tokens_per_sec | avg_latency_ms | hardware | utilization_pct | hw_cost_per_hour | effective_input_per_1m | effective_output_per_1m | date | source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gpt-4o | openai | 5.0 | 15.0 | 2.5 | 128000 | 4096 | 80 | 12.5 | h100 | 70 | 4.5 | 6.43 | 19.29 | 2025-01-01 | openai_pricing |
| gpt-4o-mini | openai | 0.15 | 0.6 | 0.075 | 128000 | 16384 | 120 | 8.3 | h100 | 70 | 4.5 | 0.18 | 0.71 | 2025-01-01 | openai_pricing |
| gpt-4-turbo | openai | 10.0 | 30.0 | 5.0 | 128000 | 4096 | 60 | 16.7 | h100 | 70 | 4.5 | 13.17 | 39.52 | 2025-01-01 | openai_pricing |

---

### `DATA\New folder\unit_economics\saas_benchmarks.csv`

- **Size:** 0.0 MB (946 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 9
- **Columns:** 15

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 1 | arr_band |
| Numeric | 14 | arr_midpoint_usd, n_companies, nrr_median, grr_median, expansion_rate_median, logo_churn_median, gross_margin_median, sales_marketing_pct_rd, rd_pct_revenue, cac_months_median, ltv_cac_median, rule_of_40_median, net_income_margin_median, free_cash_flow_margin_median |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**arr_band** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| 1-5M | 1 |
| 5-10M | 1 |
| 10-25M | 1 |
| 25-50M | 1 |
| 50-100M | 1 |
| 100-250M | 1 |
| 250-500M | 1 |
| 500M-1B | 1 |
| 1B+ | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| arr_midpoint_usd | 326722222.22 | 503788901.17 | 3000000.00 | 1500000000.00 | 75000000.00 |
| n_companies | 43.44 | 48.59 | 3.00 | 150.00 | 25.00 |
| nrr_median | 1.22 | 0.07 | 1.12 | 1.32 | 1.22 |
| grr_median | 0.96 | 0.02 | 0.92 | 0.99 | 0.97 |
| expansion_rate_median | 0.30 | 0.07 | 0.18 | 0.40 | 0.30 |
| logo_churn_median | 0.06 | 0.03 | 0.02 | 0.12 | 0.06 |
| gross_margin_median | 0.83 | 0.03 | 0.78 | 0.87 | 0.83 |
| sales_marketing_pct_rd | 0.33 | 0.07 | 0.22 | 0.45 | 0.32 |
| rd_pct_revenue | 0.19 | 0.05 | 0.12 | 0.28 | 0.18 |
| cac_months_median | 9.11 | 2.93 | 5.00 | 14.00 | 9.00 |
| ltv_cac_median | 5.28 | 0.74 | 4.20 | 6.50 | 5.20 |
| rule_of_40_median | 0.51 | 0.09 | 0.35 | 0.62 | 0.52 |
| net_income_margin_median | 0.02 | 0.10 | -0.15 | 0.15 | 0.05 |
| free_cash_flow_margin_median | 0.11 | 0.09 | -0.05 | 0.22 | 0.12 |

#### Sample Data (First 3 Rows)

| arr_band | arr_midpoint_usd | n_companies | nrr_median | grr_median | expansion_rate_median | logo_churn_median | gross_margin_median | sales_marketing_pct_rd | rd_pct_revenue | cac_months_median | ltv_cac_median | rule_of_40_median | net_income_margin_median | free_cash_flow_margin_median |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1-5M | 3000000 | 150 | 1.12 | 0.92 | 0.18 | 0.12 | 0.78 | 0.45 | 0.28 | 14 | 4.2 | 0.35 | -0.15 | -0.05 |
| 5-10M | 7500000 | 85 | 1.15 | 0.94 | 0.22 | 0.1 | 0.78 | 0.4 | 0.25 | 12 | 4.5 | 0.4 | -0.1 | 0.0 |
| 10-25M | 17500000 | 60 | 1.18 | 0.95 | 0.25 | 0.08 | 0.8 | 0.38 | 0.22 | 11 | 4.8 | 0.45 | -0.05 | 0.05 |

---

### `DATA\New folder\unit_economics\training_costs.csv`

- **Size:** 0.0 MB (2,661 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 23
- **Columns:** 13

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 4 | organization, release_date, gpu_type, source |
| Numeric | 8 | parameters_b, compute_flops, compute_cost_usd, training_tokens, training_time_days, gpu_count, training_cost_per_token, training_cost_per_flop |
| Date | 0 | — |
| Text | 1 | model |

#### Category Column Details

**organization** — Unique values: 10, Nulls: 0

| Value | Count |
|-------|-------|
| anthropic | 5 |
| openai | 4 |
| google | 3 |
| meta | 2 |
| mistral | 2 |
| deepseek | 2 |
| alibaba | 2 |
| 01.ai | 1 |
| zhipu | 1 |
| nvidia | 1 |

**release_date** — Unique values: 18, Nulls: 0

| Value | Count |
|-------|-------|
| 2024-03-04 | 3 |
| 2024-06-20 | 2 |
| 2024-05-14 | 2 |
| 2024-09-19 | 2 |
| 2023-03-14 | 1 |
| 2023-11-06 | 1 |
| 2024-05-13 | 1 |
| 2024-07-18 | 1 |
| 2024-10-22 | 1 |
| 2024-04-18 | 1 |
| 2024-07-23 | 1 |
| 2025-02-05 | 1 |
| 2024-02-26 | 1 |
| 2023-12-11 | 1 |
| 2024-12-26 | 1 |

**gpu_type** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| h100 | 11 |
| a100_80gb | 9 |
| tpu_v5 | 3 |

**source** — Unique values: 12, Nulls: 0

| Value | Count |
|-------|-------|
| semi_analysis | 4 |
| google_blog | 3 |
| openai_blog | 2 |
| anthropic_blog | 2 |
| meta_blog | 2 |
| mistral_blog | 2 |
| deepseek_blog | 2 |
| qwen_blog | 2 |
| epoch_ai/semi_analysis | 1 |
| yi_blog | 1 |
| zhipu_blog | 1 |
| nvidia_blog | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| parameters_b | 730.09 | 723.99 | 32.00 | 2000.00 | 500.00 |
| compute_flops | 9039130434782608863789056.00 | 8887567369924164672552960.00 | 499999999999999991611392.00 | 25000000000000001191182336.00 | 3499999999999999672844288.00 |
| compute_cost_usd | 20913043.48 | 18999791.97 | 3000000.00 | 63000000.00 | 10000000.00 |
| training_tokens | 9369565217391.30 | 5341129841540.06 | 1500000000000.00 | 18000000000000.00 | 10000000000000.00 |
| training_time_days | 45.65 | 23.27 | 20.00 | 100.00 | 35.00 |
| gpu_count | 8739.13 | 6538.12 | 2000.00 | 25000.00 | 8000.00 |
| training_cost_per_token | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| training_cost_per_flop | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

#### Sample Data (First 3 Rows)

| model | organization | release_date | parameters_b | compute_flops | compute_cost_usd | training_tokens | training_time_days | gpu_type | gpu_count | training_cost_per_token | training_cost_per_flop | source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gpt-4 | openai | 2023-03-14 | 1760 | 2.15e+25 | 63000000 | 13000000000000 | 100 | a100_80gb | 25000 | 4.8e-06 | 2.9e-08 | epoch_ai/semi_analysis |
| gpt-4-turbo | openai | 2023-11-06 | 1760 | 2.15e+25 | 50000000 | 13000000000000 | 80 | a100_80gb | 20000 | 3.8e-06 | 2.3e-08 | semi_analysis |
| gpt-4o | openai | 2024-05-13 | 1760 | 2.15e+25 | 40000000 | 13000000000000 | 60 | a100_80gb | 15000 | 3.1e-06 | 1.9e-08 | openai_blog |

---

### `DATA\power\fuel_prices.csv`

- **Size:** 0.0 MB (4,579 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 144
- **Columns:** 6

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 2 | hub, source |
| Numeric | 3 | price_usd_mmbtu, basis_diff_usd_mmbtu, volatility_pct |
| Date | 0 | — |
| Text | 1 | date |

#### Category Column Details

**hub** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| henry_hub | 48 |
| ttf | 48 |
| jk | 48 |

**source** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| ice | 96 |
| eia | 48 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| price_usd_mmbtu | 14.85 | 9.76 | 2.00 | 41.00 | 15.35 |
| basis_diff_usd_mmbtu | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| volatility_pct | 41.67 | 4.73 | 35.00 | 45.00 | 45.00 |

#### Sample Data (First 3 Rows)

| hub | date | price_usd_mmbtu | basis_diff_usd_mmbtu | volatility_pct | source |
| --- | --- | --- | --- | --- | --- |
| henry_hub | 2023-01 | 2.5 | 0.0 | 35 | eia |
| henry_hub | 2023-02 | 2.3 | 0.0 | 35 | eia |
| henry_hub | 2023-03 | 2.1 | 0.0 | 35 | eia |

---

### `DATA\power\grid_services_revenue.csv`

- **Size:** 0.0 MB (1,272 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 22
- **Columns:** 6

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 4 | iso, service, date, source |
| Numeric | 2 | price_usd_mw_yr, volume_mw |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**iso** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| caiso | 5 |
| ercot | 4 |
| pjm | 3 |
| miso | 3 |
| nyiso | 3 |
| iso-ne | 2 |
| spp | 2 |

**service** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| capacity | 7 |
| regulation | 5 |
| spinning_reserve | 3 |
| regulation_up | 2 |
| regulation_down | 2 |
| non_spinning_reserve | 1 |
| synchronized_reserve | 1 |
| responsive_reserve | 1 |

**date** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2024-01 | 22 |

**source** — Unique values: 14, Nulls: 0

| Value | Count |
|-------|-------|
| caiso_market_report | 4 |
| ercot_market_report | 3 |
| pjm_market_report | 2 |
| miso_market_report | 2 |
| nyiso_market_report | 2 |
| caiso_ra_report | 1 |
| pjm_ra_report | 1 |
| ercot_energy_only | 1 |
| miso_ra_report | 1 |
| nyiso_ra_report | 1 |
| iso-ne_market_report | 1 |
| iso-ne_ra_report | 1 |
| spp_market_report | 1 |
| spp_ra_report | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| price_usd_mw_yr | 39772.73 | 15377.57 | 0.00 | 65000.00 | 41000.00 |
| volume_mw | 18443.18 | 36831.59 | 0.00 | 150000.00 | 1000.00 |

#### Sample Data (First 3 Rows)

| iso | service | price_usd_mw_yr | volume_mw | date | source |
| --- | --- | --- | --- | --- | --- |
| caiso | regulation_up | 45000 | 1200 | 2024-01 | caiso_market_report |
| caiso | regulation_down | 38000 | 1100 | 2024-01 | caiso_market_report |
| caiso | spinning_reserve | 25000 | 800 | 2024-01 | caiso_market_report |

---

### `DATA\power\heat_rates.csv`

- **Size:** 0.0 MB (1,112 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 16
- **Columns:** 7

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 5 | unit, technology, fuel_type, date, source |
| Numeric | 2 | heat_rate_btu_kwh, degradation_pct_yr |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**unit** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| bloom_es5 | 5 |
| ge_7ha | 3 |
| siemens_hl | 2 |
| wartsila_18v50 | 2 |
| mitsubishi_m501 | 1 |
| plug_power_gen | 1 |
| ballard_fc | 1 |
| caterpillar_fc | 1 |

**technology** — Unique values: 5, Nulls: 0

| Value | Count |
|-------|-------|
| gas_turbine | 6 |
| sofc | 5 |
| rice | 2 |
| hydrogen | 2 |
| solid_oxide | 1 |

**fuel_type** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| natural_gas | 13 |
| hydrogen | 3 |

**date** — Unique values: 5, Nulls: 0

| Value | Count |
|-------|-------|
| 2024-01 | 8 |
| 2025-01 | 4 |
| 2026-01 | 2 |
| 2027-01 | 1 |
| 2028-01 | 1 |

**source** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| bloomenergy_whitepaper | 5 |
| ge_specs | 3 |
| siemens_specs | 2 |
| wartsila_specs | 2 |
| mitsubishi_specs | 1 |
| plug_power_specs | 1 |
| ballard_specs | 1 |
| caterpillar_specs | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| heat_rate_btu_kwh | 7687.50 | 1481.95 | 5500.00 | 9500.00 | 7600.00 |
| degradation_pct_yr | 0.53 | 0.14 | 0.30 | 0.70 | 0.50 |

#### Sample Data (First 3 Rows)

| unit | technology | fuel_type | heat_rate_btu_kwh | date | degradation_pct_yr | source |
| --- | --- | --- | --- | --- | --- | --- |
| bloom_es5 | sofc | natural_gas | 6800 | 2024-01 | 0.5 | bloomenergy_whitepaper |
| bloom_es5 | sofc | natural_gas | 6850 | 2025-01 | 0.5 | bloomenergy_whitepaper |
| bloom_es5 | sofc | natural_gas | 6900 | 2026-01 | 0.5 | bloomenergy_whitepaper |

---

### `DATA\power\hedge_ratios.csv`

- **Size:** 0.0 MB (976 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 16
- **Columns:** 7

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 5 | company, commodity, instruments, date, source |
| Numeric | 2 | hedge_ratio, tenor_yr |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**company** — Unique values: 6, Nulls: 0

| Value | Count |
|-------|-------|
| microsoft | 3 |
| google | 3 |
| aws | 3 |
| meta | 3 |
| oracle | 2 |
| intel | 2 |

**commodity** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| natural_gas | 16 |

**instruments** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| swaps | 7 |
| swaps_collars | 6 |
| swaps_collars_physical | 3 |

**date** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| 2024-01 | 6 |
| 2025-01 | 6 |
| 2026-01 | 4 |

**source** — Unique values: 6, Nulls: 0

| Value | Count |
|-------|-------|
| microsoft_10k | 3 |
| alphabet_10k | 3 |
| amazon_10k | 3 |
| meta_10k | 3 |
| oracle_10k | 2 |
| intel_10k | 2 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| hedge_ratio | 0.65 | 0.08 | 0.50 | 0.80 | 0.65 |
| tenor_yr | 2.38 | 0.50 | 2.00 | 3.00 | 2.00 |

#### Sample Data (First 3 Rows)

| company | commodity | hedge_ratio | tenor_yr | instruments | date | source |
| --- | --- | --- | --- | --- | --- | --- |
| microsoft | natural_gas | 0.65 | 3 | swaps_collars | 2024-01 | microsoft_10k |
| microsoft | natural_gas | 0.7 | 2 | swaps_collars | 2025-01 | microsoft_10k |
| microsoft | natural_gas | 0.75 | 2 | swaps_collars | 2026-01 | microsoft_10k |

---

### `DATA\power\onsite_gen_capacity.csv`

- **Size:** 0.0 MB (2,004 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 25
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 5 | company, region, technology, fuel_type, deployment_source |
| Numeric | 4 | capacity_mw, cod_year, capacity_factor, heat_rate_btu_kwh |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**company** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| microsoft | 6 |
| aws | 6 |
| google | 4 |
| oracle | 3 |
| intel | 2 |
| coreweave | 1 |
| equinix | 1 |
| digital_realty | 1 |
| cyrusone | 1 |

**region** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| us | 25 |

**technology** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| bloom_sofc | 21 |
| hydrogen_fc | 2 |
| gas_turbine | 2 |

**fuel_type** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| natural_gas | 23 |
| hydrogen | 2 |

**deployment_source** — Unique values: 16, Nulls: 0

| Value | Count |
|-------|-------|
| bloomenergy_aws_ppa | 3 |
| bloomenergy_intel_ppa | 3 |
| bloomenergy_oregon_3_sites | 3 |
| bloomenergy_silicon_valley_ppa | 3 |
| bloomenergy_oracle_1.6gw | 2 |
| plug_power_2022 | 1 |
| ballard_caterpillar_2021 | 1 |
| chicago_3x66mw | 1 |
| grid_connection_queue | 1 |
| bloomenergy_oracle_1.2gw | 1 |
| bloomenergy_intel_2014 | 1 |
| bloomenergy_intel_2024 | 1 |
| bloomenergy_coreweave_2026 | 1 |
| bloomenergy_equinix_2024 | 1 |
| bloomenergy_dlr_2024 | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| capacity_mw | 224.02 | 477.53 | 1.50 | 1600.00 | 30.00 |
| cod_year | 2023.36 | 4.00 | 2008.00 | 2026.00 | 2024.00 |
| capacity_factor | 0.88 | 0.04 | 0.75 | 0.90 | 0.90 |
| heat_rate_btu_kwh | 6912.00 | 857.48 | 5500.00 | 9500.00 | 6800.00 |

#### Sample Data (First 3 Rows)

| company | region | technology | capacity_mw | cod_year | capacity_factor | heat_rate_btu_kwh | fuel_type | deployment_source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| microsoft | us | bloom_sofc | 20.0 | 2024 | 0.9 | 6800 | natural_gas | bloomenergy_aws_ppa |
| microsoft | us | bloom_sofc | 20.0 | 2025 | 0.9 | 6800 | natural_gas | bloomenergy_aws_ppa |
| microsoft | us | bloom_sofc | 20.0 | 2026 | 0.9 | 6800 | natural_gas | bloomenergy_aws_ppa |

---

### `DATA\productivity\meta_analysis_studies.csv`

- **Size:** 0.0 MB (2,736 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 15
- **Columns:** 14

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 9 | study, category, intervention, industry, task_type, study_design, quality_score, source, source_url |
| Numeric | 5 | sample_size, effect_size_pct, ci_lower_pct, ci_upper_pct, date |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**study** — Unique values: 15, Nulls: 0

| Value | Count |
|-------|-------|
| peng_2023 | 1 |
| tabachnyk_2022 | 1 |
| moradi_2023 | 1 |
| noy_2023 | 1 |
| dellacqua_2023 | 1 |
| brynjolfsson_2023 | 1 |
| cui_2024 | 1 |
| kanazawa_2023 | 1 |
| agrawal_2023 | 1 |
| wang_2023 | 1 |
| liu_2024 | 1 |
| eloundou_2023 | 1 |
| felten_2023 | 1 |
| kalliamvakou_2022 | 1 |
| zhang_2023 | 1 |

**category** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| coding | 5 |
| consulting | 2 |
| customer_support | 2 |
| general | 2 |
| writing | 1 |
| legal | 1 |
| rd_materials | 1 |
| rd_drug | 1 |

**intervention** — Unique values: 13, Nulls: 0

| Value | Count |
|-------|-------|
| ai_assistant | 2 |
| ai_discovery | 2 |
| github_copilot | 1 |
| ml_code_completion | 1 |
| ai_pair_programming | 1 |
| chatgpt | 1 |
| genai_assistant | 1 |
| ai_review | 1 |
| ai_analysis | 1 |
| llm_exposure | 1 |
| ai_exposure | 1 |
| copilot | 1 |
| codex | 1 |

**industry** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| software_engineering | 5 |
| consulting | 2 |
| all_occupations | 2 |
| professional_services | 1 |
| technology | 1 |
| customer_service | 1 |
| legal | 1 |
| materials_science | 1 |
| pharma | 1 |

**task_type** — Unique values: 13, Nulls: 0

| Value | Count |
|-------|-------|
| code_generation | 3 |
| debugging | 1 |
| business_writing | 1 |
| strategy_analysis | 1 |
| customer_support | 1 |
| ticket_resolution | 1 |
| document_review | 1 |
| market_research | 1 |
| experiment_design | 1 |
| drug_discovery | 1 |
| task_automation | 1 |
| occupation_level | 1 |
| productivity | 1 |

**study_design** — Unique values: 4, Nulls: 0

| Value | Count |
|-------|-------|
| rct | 10 |
| quasi_exp | 2 |
| meta_analysis | 2 |
| survey | 1 |

**quality_score** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| high | 12 |
| medium | 3 |

**source** — Unique values: 15, Nulls: 0

| Value | Count |
|-------|-------|
| Peng et al. 2023 (Microsoft) | 1 |
| Tabachnyk & Nikolov 2022 | 1 |
| Moradi et al. 2023 | 1 |
| Noy & Zhang 2023 Science | 1 |
| Dell'Acqua et al. 2023 (BCG) | 1 |
| Brynjolfsson et al. 2023 NBER | 1 |
| Cui et al. 2024 QJE | 1 |
| Kanazawa et al. 2023 | 1 |
| Agrawal et al. 2023 | 1 |
| Wang et al. 2023 Nature | 1 |
| Liu et al. 2024 | 1 |
| Eloundou et al. 2023 (OpenAI) | 1 |
| Felten et al. 2023 | 1 |
| Kalliamvakou et al. 2022 (GitHub) | 1 |
| Zhang et al. 2023 | 1 |

**source_url** — Unique values: 14, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.nber.org/papers/w31161 | 2 |
| https://arxiv.org/abs/2302.06590 | 1 |
| https://arxiv.org/abs/2210.05711 | 1 |
| https://arxiv.org/abs/2305.15024 | 1 |
| https://www.science.org/doi/10.1126/science.adh2586 | 1 |
| https://www.hbs.edu/ris/Publication%20Files/24-013_0f7c8c5a-6b4b-4c7d-9c5a-8f9e5b7f5c6d.pdf | 1 |
| https://doi.org/10.1093/qje/qjae012 | 1 |
| https://arxiv.org/abs/2306.07822 | 1 |
| https://www.nature.com/articles/s41586-023-06735-2 | 1 |
| https://www.nature.com/articles/s41587-024-02123-4 | 1 |
| https://arxiv.org/abs/2303.10130 | 1 |
| https://arxiv.org/abs/2306.17175 | 1 |
| https://github.blog/2022-09-07-research-quantifying-github-copilots-impact/ | 1 |
| https://arxiv.org/abs/2305.14822 | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| sample_size | 1027.93 | 1398.57 | 80.00 | 5172.00 | 500.00 |
| effect_size_pct | 31.55 | 13.12 | 12.00 | 55.80 | 31.00 |
| ci_lower_pct | 22.91 | 10.74 | 8.00 | 40.20 | 22.00 |
| ci_upper_pct | 40.18 | 15.88 | 16.00 | 71.40 | 42.00 |
| date | 2023.00 | 0.53 | 2022.00 | 2024.00 | 2023.00 |

#### Sample Data (First 3 Rows)

| study | category | intervention | industry | task_type | sample_size | effect_size_pct | ci_lower_pct | ci_upper_pct | study_design | quality_score | source | source_url | date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| peng_2023 | coding | github_copilot | software_engineering | code_generation | 95 | 55.8 | 40.2 | 71.4 | rct | high | Peng et al. 2023 (Microsoft) | https://arxiv.org/abs/2302.06590 | 2023 |
| tabachnyk_2022 | coding | ml_code_completion | software_engineering | code_generation | 120 | 37.0 | 25.0 | 49.0 | quasi_exp | high | Tabachnyk & Nikolov 2022 | https://arxiv.org/abs/2210.05711 | 2022 |
| moradi_2023 | coding | ai_pair_programming | software_engineering | debugging | 80 | 28.5 | 15.0 | 42.0 | rct | medium | Moradi et al. 2023 | https://arxiv.org/abs/2305.15024 | 2023 |

---

### `data_centers\DATA_LINEAGE_LOG.csv`

- **Size:** 0.18 MB (190,443 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 1,607
- **Columns:** 7

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 6 | facility_id, facility_name, field, source_type, confidence, primary_source |
| Numeric | 0 | — |
| Date | 0 | — |
| Text | 1 | value |

#### Category Column Details

**facility_id** — Unique values: 52, Nulls: 0
**facility_name** — Unique values: 52, Nulls: 0
**field** — Unique values: 51, Nulls: 0
**source_type** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| Public Source | 907 |
| Estimated | 700 |

**confidence** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| A | 796 |
| C | 700 |
| B | 111 |

**primary_source** — Unique values: 41, Nulls: 247

| Value | Count |
|-------|-------|
| Meta Q4'24 earnings, Entergy IRP, LA PSC dockets, Vertiv case study | 90 |
| Crusoe announcements, WY PSC filings | 86 |
| Imperial Datacenter site, CAISO queue, KPBS reporting | 49 |
| Microsoft/QTS announcements, Georgia Power IRP | 47 |
| Gilroy city permits, PG&E interconnection | 47 |
| Stargate Phase 2 announcements, 6 new buildings | 46 |
| Oracle/Stargate announcements, ERCOT queue, Crusoe filings | 46 |
| https://www.datacenterdynamics.com/en/news/xai-colossus-supercomputer-memphis-tennessee/ | 36 |
| Community opposition, NDAs signed | 35 |
| Natural gas, Entergy contract | 35 |
| 1GW cluster | 34 |
| Air cooled, 610 acres | 34 |
| https://www.datacenterdynamics.com/en/news/prime-data-centers-breaks-ground-on-three-out-of-five-buildings-at-its-240mw-campus-in-phoenix-arizona/ | 34 |
| https://www.datacenterdynamics.com/en/news/stargate-norway-aims-lead-europes-ai-infrastructure/ | 34 |
| https://www.datacenterdynamics.com/en/news/meta-to-build-800m-data-center-in-montgomery-alabama/ | 34 |

#### Sample Data (First 3 Rows)

| facility_id | facility_name | field | value | source_type | confidence | primary_source |
| --- | --- | --- | --- | --- | --- | --- |
| DC-00001 | Stratos Hyperscale Campus | facility_id | DC-00001 | Public Source | A | Largest announced US project |
| DC-00001 | Stratos Hyperscale Campus | facility_name | Stratos Hyperscale Campus | Public Source | A | Largest announced US project |
| DC-00001 | Stratos Hyperscale Campus | operator | Bitzero Blockchain Inc. | Public Source | A | Largest announced US project |

---

### `data_centers\FACILITY_FINANCIALS.csv`

- **Size:** 0.01 MB (6,081 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 40
- **Columns:** 14

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 2 | status, tier |
| Numeric | 9 | capacity_mw, capex_billion, gpus, inference_pflops, training_pflops, annual_power_cost_million, revenue_billion_45util, ebitda_billion_45util, roic_45util |
| Date | 0 | — |
| Text | 3 | facility_id, name, hyperscaler |

#### Category Column Details

**status** — Unique values: 4, Nulls: 0

| Value | Count |
|-------|-------|
| Planned | 24 |
| Under Construction | 13 |
| Operating | 2 |
| Suspended | 1 |

**tier** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| Tier 1 | 26 |
| Tier 2 | 11 |
| Tier 3 | 3 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| capacity_mw | 2564.30 | 2546.37 | 48.00 | 9000.00 | 1800.00 |
| capex_billion | 20.40 | 22.74 | 0.43 | 81.00 | 9.54 |
| gpus | 2279149.73 | 2263216.28 | 42662.00 | 7999200.00 | 1599840.00 |
| inference_pflops | 2610.06 | 2591.80 | 48.90 | 9160.60 | 1832.10 |
| training_pflops | 1304.86 | 1295.73 | 24.40 | 4579.70 | 915.90 |
| annual_power_cost_million | 810.95 | 791.55 | 24.05 | 2653.75 | 520.34 |
| revenue_billion_45util | 93.25 | 95.71 | 1.83 | 343.05 | 55.47 |
| ebitda_billion_45util | 92.44 | 94.95 | 1.81 | 340.62 | 54.97 |
| roic_45util | 5.10 | 2.74 | 1.25 | 12.91 | 4.20 |

#### Sample Data (First 3 Rows)

| facility_id | name | hyperscaler | capacity_mw | status | tier | capex_billion | gpus | inference_pflops | training_pflops | annual_power_cost_million | revenue_billion_45util | ebitda_billion_45util | roic_45util |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DC-00001 | Stratos Hyperscale Campus | Bitzero | 9000 | Planned | Tier 1 | 81.0 | 7999200 | 9160.6 | 4579.7 | 2428.272 | 343.048776624 | 340.620504624 | 4.205191415111111 |
| DC-00002 | Monarch Compute Campus | Nscale | 8000 | Planned | Tier 1 | 72.0 | 7110400 | 8142.7 | 4070.8 | 2158.464 | 304.931370888 | 302.772906888 | 4.205179262333333 |
| DC-00003 | GW Ranch | Pacifico Energy | 7650 | Planned | Tier 1 | 68.85 | 6799320 | 7786.5 | 3892.7 | 2653.7544 | 291.5913026304 | 288.93754823039995 | 4.196623794196078 |

---

### `data_centers\fractracker_us_datacenters.csv`

- **Size:** 0.69 MB (728,322 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 1,603
- **Columns:** 44

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 23 | state, status, location_confidence, purpose, tenant, sizerank, power_source, dedicated_power_plant, number_of_generators, number_of_buildings, cooling_source, cooling_type, expected_date_online, community_pushback, advocacy_information, resistance_status, nda, community_group_website_2, information_source, info_source_5, info_source_6, info_source_7, info_source_8 |
| Numeric | 4 | zip, lat, long, property_size_acres |
| Date | 0 | — |
| Text | 17 | facility_name, address, city, county, operator_name, mw, facility_size_sqft, project_cost, community_group_website_1, petition_url, other_info, info_source_1, info_source_2, info_source_3, info_source_4, date_created, date_updated |

#### Category Column Details

**state** — Unique values: 51, Nulls: 1
**status** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| Proposed | 729 |
| Operating | 529 |
| Approved/Permitted/Under construction | 159 |
| Cancelled | 65 |
| Expanding | 60 |
| Suspended | 59 |
| Pre-proposal | 2 |

**location_confidence** — Unique values: 6, Nulls: 5

| Value | Count |
|-------|-------|
| High | 1261 |
| Medium | 282 |
| Low | 49 |
| Medium  | 3 |
| High  | 2 |
| high  | 1 |

**purpose** — Unique values: 27, Nulls: 1529

| Value | Count |
|-------|-------|
| AI | 40 |
| Crypto | 5 |
| Bitcoin transitioning to AI | 3 |
| AI Data center and solar fam | 2 |
| Bitcoin | 2 |
| Telecom / network data center | 1 |
| AI/cloud-computing | 1 |
| cloud services | 1 |
| Colocation / enterprise data center | 1 |
| Hyperscale cloud data-center campus | 1 |
| Cryptocurrency mining data center | 1 |
| AI "superfactory" | 1 |
| Hyperscale Cloud & AI Workloads | 1 |
| Telecommunication routing | 1 |
| AI and Bitcoin | 1 |

**tenant** — Unique values: 2, Nulls: 1601

| Value | Count |
|-------|-------|
| Multiple colocation tenants | 1 |
| Anthropic | 1 |

**sizerank** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| Unknown | 892 |
| Hyperscale (100-999 MW) | 340 |
| Medium (11-50 MW) | 120 |
| Mega campus (>1,000 MW) | 113 |
| Small (0-10 MW) | 100 |
| Large (51-99 MW) | 37 |
| Hyperscale (101-999 MW) | 1 |

**power_source** — Unique values: 21, Nulls: 1487

| Value | Count |
|-------|-------|
| Grid (unspecified mix) | 45 |
| Natural gas | 35 |
| Hybrid (onsite and grid) | 6 |
| Solar | 5 |
| Nuclear | 4 |
| Oil/Diesel | 2 |
| Coal | 2 |
| Natural gas, Hybrid (onsite and grid) | 2 |
| Solar, Grid (unspecified mix) | 2 |
| Fuel Cells | 2 |
| Solar, Grid (unspecified mix), Natural gas | 1 |
| Hydroelectric | 1 |
| Biomass | 1 |
| Hydroelectric, Grid (unspecified mix) | 1 |
| Wind, Solar | 1 |

**dedicated_power_plant** — Unique values: 22, Nulls: 1571

| Value | Count |
|-------|-------|
| Yes | 11 |
| Salt River Project (SRP) substation | 1 |
| May use jet engines from retired military planes | 1 |
| Georgia Power | 1 |
| EW Brown Generation Station | 1 |
| 2 | 1 |
| Northwestern Energy | 1 |
| Yes  | 1 |
| Yes - Apollo Generating Station | 1 |
| Yes - fuel cell system | 1 |
| Yes - Bluegrass Power Station | 1 |
| Yes - PowerConneX I, II, and III New Albany Energy Center | 1 |
| Yes - Socrates North Power Generation Project | 1 |
| Yes - Homer City Generating Station | 1 |
| Yes - Greene County Power Station | 1 |

**number_of_generators** — Unique values: 13, Nulls: 1590

| Value | Count |
|-------|-------|
| 25 2.5MW emergency generators for redundancy purposes | 1 |
| 100 natural gas-powered backup emergency generators connected to Southern California Gas Company’s high-pressure gas line | 1 |
| 14 on-site diesel generators | 1 |
| 15 | 1 |
| 516 | 1 |
| 0 | 1 |
| 12-24 | 1 |
| 1.2 GW diesel | 1 |
| 12 | 1 |
| 6 | 1 |
| 158 diesel backup generators | 1 |
| 115 diesel-fueled generators | 1 |
| 813 | 1 |

**number_of_buildings** — Unique values: 43, Nulls: 1406

| Value | Count |
|-------|-------|
| 2 | 26 |
| 3 | 25 |
| 6 | 23 |
| 4 | 18 |
| 5 | 12 |
| 10 | 11 |
| 7 | 10 |
| 12 | 8 |
| 8 | 8 |
| 9 | 6 |
| 14 | 5 |
| 1 | 3 |
| 15 | 3 |
| 30 | 3 |
| 20 | 3 |

**cooling_source** — Unique values: 3, Nulls: 1553

| Value | Count |
|-------|-------|
| Water | 31 |
| Air | 16 |
| Hybrid air/water | 3 |

**cooling_type** — Unique values: 3, Nulls: 1541

| Value | Count |
|-------|-------|
| Closed loop | 58 |
| Fans | 2 |
| Open loop | 2 |

**expected_date_online** — Unique values: 16, Nulls: 1470

| Value | Count |
|-------|-------|
| 2027 | 48 |
| 2028 | 27 |
| 2026 | 23 |
| 2030 | 12 |
| 2029 | 8 |
| 2025 | 3 |
| 2032 | 2 |
| 2027-28 | 2 |
| Full buildout by 2037 | 1 |
| Full buildout by 2035 | 1 |
| 2036 | 1 |
| Buildout by 2028 | 1 |
| 2024 | 1 |
| 20027 | 1 |
| 2035 | 1 |

**community_pushback** — Unique values: 3, Nulls: 11

| Value | Count |
|-------|-------|
| Unknown | 1330 |
| Yes | 260 |
| Yes  | 2 |

**advocacy_information** — Unique values: 63, Nulls: 1539
**resistance_status** — Unique values: 3, Nulls: 1520

| Value | Count |
|-------|-------|
| Organized Advocacy | 58 |
| Emerging Concern | 23 |
| Unknown | 2 |

**nda** — Unique values: 8, Nulls: 1592

| Value | Count |
|-------|-------|
| Yes | 4 |
| Bessemer Mayor Kenneth Gulley, the city attorney, and other city leaders signed NDAs | 1 |
| Yes- https://www.al.com/news/2025/10/secrecy-agreements-fuel-pushback-of-14-billion-alabama-data-center.html | 1 |
| Active (Tenant identity legally shielded) | 1 |
| No | 1 |
| Every elected official is under an NDA including the Montana Public Service Commission | 1 |
| Officials knew of the Meta plan as “Project Accordion” for more than a year before it was officially announced | 1 |
| Marion County officials confirmed that the council signed a nondisclosure agreement | 1 |

**community_group_website_2** — Unique values: 32, Nulls: 1570

| Value | Count |
|-------|-------|
| https://wvrivers.org/ | 2 |
| https://www.facebook.com/groups/740748888833453 | 1 |
| https://www.facebook.com/groups/4339680782970126 | 1 |
| https://www.facebook.com/groups/1117995533656453 | 1 |
| https://www.facebook.com/profile.php?id=61585975718358 | 1 |
| https://www.nodatacentermpk.org/ | 1 |
| https://www.facebook.com/groups/942876081944302/ | 1 |
| https://www.facebook.com/groups/1397482882419331/ | 1 |
| https://www.facebook.com/groups/1359906715176907/ | 1 |
| https://www.swarmatl.org/ | 1 |
| https://www.facebook.com/groups/1469043077373264/ | 1 |
| https://www.facebook.com/groups/882581394736535/ | 1 |
| https://www.gofundme.com/f/defend-hobarts-future-no-data-centers | 1 |
| https://capitalbnews.org/meta-richland-parish-ai-data-center/ | 1 |
| https://www.facebook.com/groups/283244782323144/ | 1 |

**information_source** — Unique values: 6, Nulls: 0

| Value | Count |
|-------|-------|
| Media Monitoring | 1021 |
| PEC | 386 |
| Sci4GA | 104 |
| Crowdsourced | 51 |
| Other | 39 |
| FOIA/ public records request | 2 |

**info_source_5** — Unique values: 72, Nulls: 1530
**info_source_6** — Unique values: 44, Nulls: 1559

| Value | Count |
|-------|-------|
| https://www.datacenterdynamics.com/en/news/alabamas-planned-14bn-project-marvel-data-center-could-double-in-size/ | 1 |
| https://news.azpm.org/p/azpmnews/2026/5/28/229919-arizona-water-officials-approve-wells-tied-to-project-blue-data-center/ | 1 |
| https://wgxa.tv/news/local/environmental-advocate-urges-twiggs-county-to-reject-data-center-plans-near-ocmulgee-river | 1 |
| https://www.indystar.com/story/news/local/marion-county/2025/09/22/google-withdraws-controversial-data-center-in-franklin-township-indianapolis-city-county-council/86165695007/ | 1 |
| https://wsbt.com/news/local/st-joseph-county-council-denies-rezoning-of-land-for-data-center-votes-7-2-marathon-meeting-hours-long-public-opinion-13-billion-dollar-project-amazon-new-carlisle-approval-process-plan-commission-st-joseph-county-indiana | 1 |
| https://epoch.ai/data/data-centers/satellite-explorer/AnthropicAmazonProjectRainierNewCarlisleIndiana?ref=404media.co | 1 |
| https://www.lpm.org/news/2025-06-03/oldham-county-data-center-switches-sites-reduces-size-amid-local-resistance | 1 |
| https://www.bgr.com/1990532/meta-new-aid-data-center-size-70-football-fields-residents-scared-water/ | 1 |
| https://www.cbsnews.com/boston/news/inside-lowell-markley-data-center | 1 |
| https://www.whmi.com/news/article/developers-withdraw-re-zoning-application-for-proposed-data-center-in-howell-twp?fbclid=IwY2xjawOjxD5leHRuA2FlbQIxMABicmlkETFGTWdNTnFwVzhHUFAxcXRrc3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHqbt42SjPESM_B2BmdYNZGnBkWqqW2rX4bXuiVk3lYnyLj84qbo_n3pDm2Yp_aem_SOH2yzjxxo5bOquwuYeBEw | 1 |
| https://www.crainsdetroit.com/technology/cdb-anthropic-projectflex-datacenter-20260414/?utm_id=gfta-ur-260414&share-code=F4JNH5GIING7NDXCBOJBJ5QVZM&user_id=9885400&customer_secondary_source=cdb_articleGifting&fbclid=IwdGRjcARLdD9jbGNrBEt0NmV4dG4DYWVtAjExAHNydGMGYXBwX2lkDDM1MDY4NTUzMTcyOAABHuy4NDQbhkRm0MqYKNA8xHVyzE_IEbw7Q63iYC4OtY7wS2VOuDb-HW1V_hun_aem_aeBEd6Vy6DKHXUxdtutdIw | 1 |
| https://planetdetroit.org/2026/02/saline-data-center-air-wetlands-permits/ | 1 |
| https://planetdetroit.org/2026/03/google-dte-data-center-van-buren/ | 1 |
| https://www.mprnews.org/story/2025/10/22/hermantown-delays-permits-for-disputed-data-center | 1 |
| https://elpasomatters.org/2025/09/25/stargate-open-ai-oracle-project-jupiter-data-center-dona-ana-new-mexico-el-paso-texas/ | 1 |

**info_source_7** — Unique values: 25, Nulls: 1578

| Value | Count |
|-------|-------|
| https://abc3340.com/news/abc-3340-news-iteam/bessemer-unveils-revised-project-marvel-data-center-campus-plan-amid-ongoing-controversy | 1 |
| https://www.41nbc.com/twiggs-county-data-center-rezoning-approval/ | 1 |
| https://lailluminator.com/briefs/entergy-builds-power-plant-for-data-center/ | 1 |
| https://www.whmi.com/news/article/vangilder-family-farm-data-center | 1 |
| https://www.datacenterdynamics.com/en/news/or/ | 1 |
| https://www.datacenterdynamics.com/en/news/google-confirms-1gw-data-center-campus-near-detroit-michigan-partners-with-dte-energy-on-27gw-power-generation/ | 1 |
| https://www.mprnews.org/story/2025/11/14/hermantown-data-center-developer-plans-public-meeting | 1 |
| https://www.datacenterdynamics.com/en/news/groups-sue-to-stall-data-center-project-in-do%C3%B1a-ana-county-new-mexico/ | 1 |
| https://truthout.org/articles/new-york-residents-are-fighting-a-data-center-backed-by-a-billionaire-trump-ally/ | 1 |
| https://www.ithaca.com/news/lansing/flx-strong-clean-file-lawsuit-against-lansing-zba-terawulf-to-block-data-center/article_97b45f0f-c849-497c-9daa-6040f1f1710b.html | 1 |
| https://oilandgaswatch.org/facility/rec_d5eiru1uih89upkga2qg | 1 |
| https://www.journal-news.com/news/residents-say-no-on-1b-data-center-project-wants-hamilton-to-do-the-same/L3YUSLLR2VHMDFXVBXKPBTOHCA/ | 1 |
| https://oilandgaswatch.org/facility/rec_d4f1u60q7easr8ra1g30 | 1 |
| https://paenvironmentdaily.blogspot.com/2025/12/dep-to-host-jan-6-public-information.html | 1 |
| https://www.spotlightpa.org/news/2026/03/pennsylvania-data-centers-archbald-ai-evictions-environment/?utm_source=ActiveCampaign&utm_medium=email&utm_content=6%20data%20centers%20%20One%20PA%20borough&utm_campaign=PA%20Post%2003%2019%2026%20%28Copy%29 | 1 |

**info_source_8** — Unique values: 14, Nulls: 1589

| Value | Count |
|-------|-------|
| https://insideclimatenews.org/news/13112025/proposed-alabama-data-center-clashes-with-northern-beltline-birmingham-darter/ | 1 |
| https://www.41nbc.com/twiggs-county-data-center-rezoning-approval/ | 1 |
| https://www.datacenterdynamics.com/en/news/meta-purchases-additional-1400-acres-for-hyperion-mega-data-center-expansion/ | 1 |
| https://planetdetroit.org/2025/12/billion-dollar-data-center-paused/ | 1 |
| https://www.datacenterdynamics.com/en/news/google-confirms-it-is-behind-403-acre-data-center-campus-in-hermantown-minnesota/ | 1 |
| https://www.datacenterdynamics.com/en/news/oracle-revealed-as-tenant-of-project-jupiter-data-center-campus-in-new-mexico/ | 1 |
| https://www.nytimes.com/2026/03/17/nyregion/ai-data-center-new-york.html | 1 |
| https://bgindependentmedia.org/meta-data-center-how-it-went-from-economic-development-coup-to-project-local-residents-rue/ | 1 |
| https://www.wvxu.org/environment/2025-12-03/developers-data-center-butler-county | 1 |
| https://www.wvia.org/news/local/2026-05-01/fast-track-no-more-pa-kicks-archbald-data-center-campus-off-permit-program | 1 |
| https://www.datacenterdynamics.com/en/news/shippingport-industrial-park/ | 1 |
| https://www.datacenterdynamics.com/en/news/riot-platforms-files-to-add-building-to-cryptomine-and-data-center-campus-in-corsicana-texas/ | 1 |
| https://www.wisn.com/article/whats-that-sound-its-mount-pleasants-new-ai-data-center/70850595 | 1 |
| https://www.datacenterdynamics.com/en/news/vantage-tops-out-second-building-at-openais-lighthouse-campus-in-wisconsin/ | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| zip | 42285.76 | 25908.90 | 1085.00 | 99734.00 | 30294.00 |
| lat | 37.68 | 4.21 | 21.48 | 70.18 | 38.76 |
| long | -87.35 | 12.57 | -158.02 | -67.02 | -84.06 |
| property_size_acres | 460.38 | 2001.15 | 1.00 | 40000.00 | 117.00 |

#### Sample Data (First 3 Rows)

| facility_name | address | city | state | zip | county | lat | long | status | location_confidence | purpose | operator_name | tenant | mw | sizerank | power_source | dedicated_power_plant | number_of_generators | number_of_buildings | cooling_source | cooling_type | facility_size_sqft | property_size_acres | project_cost | expected_date_online | community_pushback | advocacy_information | resistance_status | nda | community_group_website_1 | community_group_website_2 | petition_url | other_info | information_source | info_source_1 | info_source_2 | info_source_3 | info_source_4 | info_source_5 | info_source_6 | info_source_7 | info_source_8 | date_created | date_updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Global Stack Data Center | nan | nan | nan | nan | Napa | 38.585007 | -122.58886 | Proposed | Medium | nan | Global Stack/ Edge | nan | 10 | Small (0-10 MW) | nan | nan | nan | nan | nan | nan | nan | 70.0 | nan | nan | Yes | nan | Emerging Concern | nan | nan | nan | nan | nan | Media Monitoring | https://www.datacenterdynamics.com/en/news/develop | https://calistoga.civicweb.net/document/116181/Glo | nan | nan | nan | nan | nan | nan | 06/29/2026 | 06/29/2026 |
| Stak Energy Data Center | Dalton Hwy, 26 miles south of Deadhorse | North Slope Borough | AK | nan | North Slope | 69.90071 | -148.81477 | Proposed | Medium | nan | Stak | nan | 3000 | Mega campus (>1,000 MW) | Natural gas | Yes | nan | nan | nan | nan | nan | 715.0 | nan | 2028 | Unknown | nan | nan | nan | nan | nan | nan | nan | Media Monitoring | https://www.datacenterdynamics.com/en/news/stak-en | https://www.cbc.ca/news/canada/north/yukon-alaska- | nan | nan | nan | nan | nan | nan | 05/20/2026 | 06/24/2026 |
| Prudhoe Bay Data Center | Dalton Hwy | Prudhoe Bay | AK | 99734.0 | North Slope | 70.18478 | -148.44 | Operating | Medium | nan | Far North Digital, LLC | nan | 120 | Hyperscale (100-999 MW) | nan | nan | nan | nan | Air | nan | nan | 100.0 | nan | nan | Unknown | nan | nan | nan | nan | nan | nan | nan | Media Monitoring | https://www.fn-digital.com/data-center | https://www.datacenterdynamics.com/en/news/stak-en | nan | nan | nan | nan | nan | nan | 05/20/2026 | 05/20/2026 |

---

### `data_centers\GAP_UNCERTAINTY_REGISTER.csv`

- **Size:** 0.05 MB (49,911 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 534
- **Columns:** 5

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 3 | missing_field, impact, suggested_source |
| Numeric | 0 | — |
| Date | 0 | — |
| Text | 2 | facility_id, facility_name |

#### Category Column Details

**missing_field** — Unique values: 13, Nulls: 0

| Value | Count |
|-------|-------|
| latitude | 51 |
| longitude | 51 |
| utility | 42 |
| ppa_price_mwh | 42 |
| cooling_detail | 42 |
| gpu_generation | 42 |
| cluster_size | 42 |
| total_capex_billion | 42 |
| voltage_kv | 42 |
| generation_mix | 42 |
| water_source_mgd | 42 |
| network_detail | 42 |
| capacity_mw | 12 |

**impact** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| Medium | 396 |
| High | 138 |

**suggested_source** — Unique values: 12, Nulls: 0

| Value | Count |
|-------|-------|
| Building permits / county GIS / OSM | 102 |
| State PUC dockets / utility IRP | 42 |
| Utility regulatory filings / PPA announcements | 42 |
| Building permits / vendor case studies | 42 |
| Earnings calls / supply chain reports / job postings | 42 |
| Network topology papers / vendor reference architectures | 42 |
| SEC 10-K/10-Q / press releases / bond prospectuses | 42 |
| Utility interconnection agreement / FERC filings | 42 |
| Utility IRP / sustainability reports | 42 |
| Water rights permits / sustainability reports | 42 |
| PeeringDB / submarine cable maps / earnings calls | 42 |
| Utility interconnection queue / FERC Form 715 | 12 |

#### Sample Data (First 3 Rows)

| facility_id | facility_name | missing_field | impact | suggested_source |
| --- | --- | --- | --- | --- |
| DC-00001 | Stratos Hyperscale Campus | utility | Medium | State PUC dockets / utility IRP |
| DC-00001 | Stratos Hyperscale Campus | ppa_price_mwh | Medium | Utility regulatory filings / PPA announcements |
| DC-00001 | Stratos Hyperscale Campus | cooling_detail | High | Building permits / vendor case studies |

---

### `data_centers\global_datacenters_github.csv`

- **Size:** 1.64 MB (1,719,488 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 18,110
- **Columns:** 6

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 0 | — |
| Numeric | 0 | — |
| Date | 0 | — |
| Text | 6 | name, company, city, state, country, address |

#### Sample Data (First 3 Rows)

| name | company | city | state | country | address |
| --- | --- | --- | --- | --- | --- |
| NAP de las Americas Madrid | Terremark | Madrid | nan | Spain | Calle de Yecora, 4 28009 Madrid Spain |
| Central Office 2 | StarHub Ltd. | Singapore | nan | Singapore | 19 Tai Seng Dr 535222 Singapore Singapore |
| Cluj-Napoca | GTS Telecom SRL | Cluj-Napoca | nan | Romania | Str. Garii nr. 21 400267 Cluj-Napoca Romania |

---

### `data_centers\hyperscaler_focused_projects.csv`

- **Size:** 0.01 MB (9,461 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 52
- **Columns:** 16

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 9 | hyperscaler_category, tenant, state_province, country, status, capacity_category, expected_online_date, project_cost_usd, purpose |
| Numeric | 2 | cooling_type, power_source |
| Date | 0 | — |
| Text | 5 | facility_name, operator, city, capacity_mw, source_url |

#### Category Column Details

**hyperscaler_category** — Unique values: 15, Nulls: 0

| Value | Count |
|-------|-------|
| Other/Unclassified | 26 |
| Meta | 4 |
| AWS | 3 |
| Google | 3 |
| Microsoft | 3 |
| Oracle | 3 |
| Crusoe | 2 |
| Aligned | 1 |
| Prime Data Centers | 1 |
| Vantage | 1 |
| NTT | 1 |
| Stream Data Centers | 1 |
| Apple | 1 |
| xAI | 1 |
| Stargate | 1 |

**tenant** — Unique values: 14, Nulls: 29

| Value | Count |
|-------|-------|
| 2027 | 5 |
| 2026 | 3 |
| 2028 | 2 |
| 2032 | 2 |
| Microsoft | 2 |
| 2036 | 1 |
| $33 billion | 1 |
| Meta | 1 |
| AWS | 1 |
| $40 billion+ | 1 |
| Google (unconfirmed) | 1 |
| $10 billion+ | 1 |
| xAI | 1 |
| OpenAI/Oracle | 1 |

**state_province** — Unique values: 17, Nulls: 2

| Value | Count |
|-------|-------|
| Arizona | 14 |
| Texas | 8 |
| California | 4 |
| Alabama | 3 |
| Arkansas | 3 |
| Utah | 2 |
| Virginia | 2 |
| Florida | 2 |
| Louisiana | 2 |
| Ohio | 2 |
| Wyoming | 2 |
| West Virginia | 1 |
| New Mexico | 1 |
| Pennsylvania | 1 |
| Alaska | 1 |

**country** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| United States | 50 |
| Norway | 1 |
| United Arab Emirates | 1 |

**status** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| Planned | 21 |
| Approved/Permitted/Under construction | 16 |
| Proposed | 6 |
| Under Construction | 4 |
| Operating | 3 |
| Suspended | 1 |
| Expanding | 1 |

**capacity_category** — Unique values: 5, Nulls: 0

| Value | Count |
|-------|-------|
| Mega campus (>1 | 29 |
| Hyperscale (100-999 MW) | 16 |
| Unknown | 5 |
| Large (51-99 MW) | 1 |
| Medium (11-50 MW) | 1 |

**expected_online_date** — Unique values: 10, Nulls: 39

| Value | Count |
|-------|-------|
| 2026 | 3 |
| 2027 | 2 |
| $14 billion | 1 |
| $6 billion | 1 |
| $3.6 billion | 1 |
| $10 billion | 1 |
| $300 million | 1 |
| 250 | 1 |
| 2028 | 1 |
| 2025 | 1 |

**project_cost_usd** — Unique values: 8, Nulls: 44

| Value | Count |
|-------|-------|
| 1600 | 1 |
| $8 billion | 1 |
| 687 | 1 |
| 290 | 1 |
| 1218 | 1 |
| $800 million | 1 |
| $10 billion | 1 |
| $29 million | 1 |

**purpose** — Unique values: 8, Nulls: 25

| Value | Count |
|-------|-------|
| AI/Hyperscale | 14 |
| Cloud/AI | 5 |
| Meta | 2 |
| OpenAI/Oracle | 2 |
| 2027 | 1 |
| AWS | 1 |
| Google | 1 |
| OpenAI/Oracle/MGX | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| cooling_type | N/A | N/A | N/A | N/A | N/A |
| power_source | N/A | N/A | N/A | N/A | N/A |

#### Sample Data (First 3 Rows)

| hyperscaler_category | facility_name | operator | tenant | city | state_province | country | status | capacity_mw | capacity_category | expected_online_date | project_cost_usd | cooling_type | power_source | purpose | source_url |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Other/Unclassified | Stratos Hyperscale Campus | Bitzero Blockchain Inc. | nan | nan | Utah | United States | Planned | 9000 | Mega campus (>1 | nan | nan | nan | nan | nan | Largest announced US project |
| Other/Unclassified | Monarch Compute Campus | Nscale Ltd. | 2027 | nan | West Virginia | United States | Planned | 8000 | Mega campus (>1 | nan | nan | nan | nan | nan | $1.6B+ investment |
| Other/Unclassified | GW Ranch | Pacifico Energy | 2027 | nan | Texas | United States | Planned | 7650 | Mega campus (>1 | nan | nan | nan | nan | nan | nan |

---

### `data_centers\key_hyperscale_projects.csv`

**Error:** Error tokenizing data. C error: Expected 19 fields in line 25, saw 20


### `data_centers\MASTER_CAPABILITY_MATRIX.csv`

- **Size:** 0.02 MB (17,303 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 52
- **Columns:** 40

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 15 | tenant, hyperscaler_category, state_province, country, status, tier, capacity_category, expected_online_date, primary_gpu, utility, generation_mix, cooling_detail, network_detail, gpu_generation, notes |
| Numeric | 20 | latitude, longitude, capacity_mw, it_load_mw, est_gpu_count, cluster_size, training_bf16_pflops, inference_fp8_pflops, est_tokens_per_sec_billions, est_training_runs_per_year_gpt4_class, voltage_kv, ppa_price_mwh, annual_power_mwh, annual_power_cost_usd, power_cost_per_gpu_per_year, water_source_mgd, total_capex_billion, est_capex_per_kw, est_capex_per_gpu, annual_revenue_potential_usd |
| Date | 0 | — |
| Text | 5 | facility_id, facility_name, operator, city, source_notes |

#### Category Column Details

**tenant** — Unique values: 14, Nulls: 29

| Value | Count |
|-------|-------|
| 2027 | 5 |
| 2026 | 3 |
| 2028 | 2 |
| 2032 | 2 |
| Microsoft | 2 |
| 2036 | 1 |
| $33 billion | 1 |
| Google (unconfirmed) | 1 |
| xAI | 1 |
| OpenAI/Oracle | 1 |
| Meta | 1 |
| AWS | 1 |
| $40 billion+ | 1 |
| $10 billion+ | 1 |

**hyperscaler_category** — Unique values: 15, Nulls: 0

| Value | Count |
|-------|-------|
| Other/Unclassified | 26 |
| Meta | 4 |
| AWS | 3 |
| Oracle | 3 |
| Google | 3 |
| Microsoft | 3 |
| Crusoe | 2 |
| Stargate | 1 |
| xAI | 1 |
| Prime Data Centers | 1 |
| NTT | 1 |
| Stream Data Centers | 1 |
| Vantage | 1 |
| Aligned | 1 |
| Apple | 1 |

**state_province** — Unique values: 17, Nulls: 2

| Value | Count |
|-------|-------|
| Arizona | 14 |
| Texas | 8 |
| California | 4 |
| Alabama | 3 |
| Arkansas | 3 |
| Utah | 2 |
| Louisiana | 2 |
| Virginia | 2 |
| Wyoming | 2 |
| Florida | 2 |
| Ohio | 2 |
| West Virginia | 1 |
| New Mexico | 1 |
| Pennsylvania | 1 |
| Alaska | 1 |

**country** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| United States | 50 |
| United Arab Emirates | 1 |
| Norway | 1 |

**status** — Unique values: 5, Nulls: 0

| Value | Count |
|-------|-------|
| Planned | 27 |
| Under Construction | 20 |
| Operating | 3 |
| Suspended | 1 |
| Expanding | 1 |

**tier** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| Tier 1 | 26 |
| Tier 3 | 15 |
| Tier 2 | 11 |

**capacity_category** — Unique values: 5, Nulls: 0

| Value | Count |
|-------|-------|
| Mega campus (>1 | 29 |
| Hyperscale (100-999 MW) | 16 |
| Unknown | 5 |
| Large (51-99 MW) | 1 |
| Medium (11-50 MW) | 1 |

**expected_online_date** — Unique values: 10, Nulls: 39

| Value | Count |
|-------|-------|
| 2026 | 3 |
| 2027 | 2 |
| $14 billion | 1 |
| $6 billion | 1 |
| 2025 | 1 |
| $300 million | 1 |
| 2028 | 1 |
| $3.6 billion | 1 |
| $10 billion | 1 |
| 250 | 1 |

**primary_gpu** — Unique values: 6, Nulls: 0

| Value | Count |
|-------|-------|
| H100 (est.) | 42 |
| B200 | 4 |
| GB200 NVL72 | 2 |
| H100 | 2 |
| Trainium2/Inferentia2 | 1 |
| TPU v5p/v6 | 1 |

**utility** — Unique values: 7, Nulls: 42

| Value | Count |
|-------|-------|
| Entergy Louisiana | 2 |
| PacifiCorp / WAPA | 2 |
| Oncor / ERCOT | 2 |
| IID / CAISO | 1 |
| Georgia Power / Southern Company | 1 |
| PG&E | 1 |
| Entergy Arkansas | 1 |

**generation_mix** — Unique values: 7, Nulls: 42

| Value | Count |
|-------|-------|
| Gas 60%, Nuclear 25%, Renewable 15% | 2 |
| Wind 50%, Gas 30%, Coal 20% | 2 |
| Wind 35%, Solar 25%, Gas 30%, Nuclear 10% | 2 |
| Solar 50%, Geothermal 20%, Gas 30% | 1 |
| Gas 40%, Nuclear 30%, Coal 15%, Renewable 15% | 1 |
| Solar 30%, Hydro 25%, Gas 25%, Nuclear 15%, Wind 5% | 1 |
| Gas 50%, Nuclear 25%, Renewable 25% | 1 |

**cooling_detail** — Unique values: 7, Nulls: 42

| Value | Count |
|-------|-------|
| Direct-to-chip liquid (80%) + rear-door (20%) | 2 |
| Direct liquid cooling (DLC) | 2 |
| Direct liquid cooling (DLC) 100% | 2 |
| Hybrid air/liquid, 100 gas generators + 862MWh BESS | 1 |
| Rear-door heat exchanger + liquid assist | 1 |
| Hybrid air/water, 95% free cooling | 1 |
| Direct-to-chip liquid (TPU pods) | 1 |

**network_detail** — Unique values: 7, Nulls: 42

| Value | Count |
|-------|-------|
| NVL72 + InfiniBand NDR 400G, 800G ZR+ to Atlanta/Dallas | 2 |
| 400G/800G to Denver/Salt Lake | 2 |
| NVL72 + InfiniBand NDR, 1.6T to Dallas | 2 |
| InfiniBand NDR, 800G to LA/San Diego | 1 |
| InfiniBand NDR 400G, 800G to Chicago/Dallas | 1 |
| 100G/400G to San Jose/Sacramento | 1 |
| Custom optical circuit switching, 1.6T regional | 1 |

**gpu_generation** — Unique values: 8, Nulls: 42

| Value | Count |
|-------|-------|
| H100 (2025), B200 (2026+) | 2 |
| H100 / B200 | 2 |
| GB200 NVL72 / GB300 | 1 |
| H100 / TPU v5 | 1 |
| H100 / Maia 100 | 1 |
| GB200 NVL72 | 1 |
| Trainium2 / Inferentia2 | 1 |
| TPU v5p / v6 | 1 |

**notes** — Unique values: 13, Nulls: 12

| Value | Count |
|-------|-------|
| AI/Hyperscale | 28 |
| Cloud/AI | 1 |
| 100 gas generators, 862MWh BESS | 1 |
| 100k GPUs | 1 |
| Building 4 268MW, Bldg 2 260MW | 1 |
| 3 of 5 buildings broke ground | 1 |
| 100k GPUs by 2026 | 1 |
| 100% renewable, recycled water | 1 |
| Community opposition | 1 |
| Phase 1 approved | 1 |
| Water concerns, 31M gal/yr | 1 |
| 1,300 acres | 1 |
| AI/Cloud | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| latitude | 24.14 | nan | 24.14 | 24.14 | 24.14 |
| longitude | 54.46 | nan | 54.46 | 54.46 | 54.46 |
| capacity_mw | 2564.30 | 2546.37 | 48.00 | 9000.00 | 1800.00 |
| it_load_mw | 2256.58 | 2240.81 | 42.20 | 7920.00 | 1584.00 |
| est_gpu_count | 272521.06 | 342102.51 | 0.00 | 1267200.00 | 93280.00 |
| cluster_size | 91948.80 | 146019.73 | 8192.00 | 500000.00 | 49152.00 |
| training_bf16_pflops | 320.29 | 396.30 | 0.00 | 1425.60 | 109.70 |
| inference_fp8_pflops | 640.77 | 792.83 | 0.00 | 2851.20 | 219.40 |
| est_tokens_per_sec_billions | 0.04 | 0.05 | 0.00 | 0.19 | 0.01 |
| est_training_runs_per_year_gpt4_class | 0.40 | 0.50 | 0.00 | 1.80 | 0.15 |
| voltage_kv | 372.50 | 131.09 | 115.00 | 500.00 | 345.00 |
| ppa_price_mwh | 40.00 | 10.64 | 30.00 | 65.00 | 36.50 |
| annual_power_mwh | 19767675.80 | 19629478.89 | 370022.00 | 69379200.00 | 13875840.00 |
| annual_power_cost_usd | 810951498.73 | 791547588.53 | 24051456.00 | 2653754400.00 | 520344000.00 |
| power_cost_per_gpu_per_year | 2403.70 | 659.25 | 657.00 | 4380.00 | 2300.00 |
| water_source_mgd | 3.67 | 3.35 | 0.80 | 12.00 | 2.75 |
| total_capex_billion | 6.02 | 3.82 | 0.50 | 10.00 | 5.50 |
| est_capex_per_kw | 7242.67 | 9055.01 | 1852.00 | 30303.00 | 5000.00 |
| est_capex_per_gpu | 51440.00 | 64311.33 | 13152.00 | 215220.00 | 35511.00 |
| annual_revenue_potential_usd | 837937537.20 | 830644450.75 | 15988752.00 | 2997181440.00 | 561971520.00 |

#### Sample Data (First 3 Rows)

| facility_id | facility_name | operator | tenant | hyperscaler_category | city | state_province | country | latitude | longitude | status | tier | capacity_mw | capacity_category | expected_online_date | it_load_mw | primary_gpu | est_gpu_count | cluster_size | training_bf16_pflops | inference_fp8_pflops | est_tokens_per_sec_billions | est_training_runs_per_year_gpt4_class | utility | voltage_kv | ppa_price_mwh | generation_mix | annual_power_mwh | annual_power_cost_usd | power_cost_per_gpu_per_year | cooling_detail | water_source_mgd | network_detail | gpu_generation | total_capex_billion | est_capex_per_kw | est_capex_per_gpu | annual_revenue_potential_usd | source_notes | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DC-00001 | Stratos Hyperscale Campus | Bitzero Blockchain Inc. | nan | Other/Unclassified | nan | Utah | United States | nan | nan | Planned | Tier 1 | 9000.0 | Mega campus (>1 | nan | 7920.0 | H100 (est.) | 1267200 | nan | 1253.3 | 2507.8 | 0.19008 | 1.6 | nan | nan | nan | nan | 69379200.0 | 2428272000.0 | 1916.0 | nan | nan | nan | nan | nan | nan | nan | 2997181440.0 | Largest announced US project | AI/Hyperscale |
| DC-00002 | Monarch Compute Campus | Nscale Ltd. | 2027 | Other/Unclassified | nan | West Virginia | United States | nan | nan | Planned | Tier 1 | 8000.0 | Mega campus (>1 | nan | 7040.0 | H100 (est.) | 1126400 | nan | 1114.0 | 2229.1 | 0.16896 | 1.4 | nan | nan | nan | nan | 61670400.0 | 2158464000.0 | 1916.0 | nan | nan | nan | nan | nan | nan | nan | 2664161280.0 | $1.6B+ investment | AI/Hyperscale |
| DC-00003 | GW Ranch | Pacifico Energy | 2027 | Other/Unclassified | nan | Texas | United States | nan | nan | Planned | Tier 1 | 7650.0 | Mega campus (>1 | nan | 6732.0 | H100 (est.) | 1077120 | nan | 1065.3 | 2131.6 | 0.161568 | 1.3 | nan | nan | nan | nan | 58972320.0 | 2653754400.0 | 2464.0 | nan | nan | nan | nan | nan | nan | nan | 2547604224.0 | nan | AI/Hyperscale |

---

### `data_centers\master_facility_list.csv`

- **Size:** 0.01 MB (10,639 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 52
- **Columns:** 19

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 10 | tenant, hyperscaler_category, state_province, country, status, capacity_category, expected_online_date, purpose, notes, tier |
| Numeric | 4 | capacity_mw, project_cost_usd, cooling_type, power_source |
| Date | 0 | — |
| Text | 5 | facility_id, facility_name, operator, city, source_url |

#### Category Column Details

**tenant** — Unique values: 14, Nulls: 29

| Value | Count |
|-------|-------|
| 2027 | 5 |
| 2026 | 3 |
| 2028 | 2 |
| 2032 | 2 |
| Microsoft | 2 |
| 2036 | 1 |
| $33 billion | 1 |
| Google (unconfirmed) | 1 |
| xAI | 1 |
| OpenAI/Oracle | 1 |
| Meta | 1 |
| AWS | 1 |
| $40 billion+ | 1 |
| $10 billion+ | 1 |

**hyperscaler_category** — Unique values: 15, Nulls: 0

| Value | Count |
|-------|-------|
| Other/Unclassified | 26 |
| Meta | 4 |
| AWS | 3 |
| Oracle | 3 |
| Google | 3 |
| Microsoft | 3 |
| Crusoe | 2 |
| Stargate | 1 |
| xAI | 1 |
| Prime Data Centers | 1 |
| NTT | 1 |
| Stream Data Centers | 1 |
| Vantage | 1 |
| Aligned | 1 |
| Apple | 1 |

**state_province** — Unique values: 17, Nulls: 2

| Value | Count |
|-------|-------|
| Arizona | 14 |
| Texas | 8 |
| California | 4 |
| Alabama | 3 |
| Arkansas | 3 |
| Utah | 2 |
| Louisiana | 2 |
| Virginia | 2 |
| Wyoming | 2 |
| Florida | 2 |
| Ohio | 2 |
| West Virginia | 1 |
| New Mexico | 1 |
| Pennsylvania | 1 |
| Alaska | 1 |

**country** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| United States | 50 |
| United Arab Emirates | 1 |
| Norway | 1 |

**status** — Unique values: 5, Nulls: 0

| Value | Count |
|-------|-------|
| Planned | 27 |
| Under Construction | 20 |
| Operating | 3 |
| Suspended | 1 |
| Expanding | 1 |

**capacity_category** — Unique values: 5, Nulls: 0

| Value | Count |
|-------|-------|
| Mega campus (>1 | 29 |
| Hyperscale (100-999 MW) | 16 |
| Unknown | 5 |
| Large (51-99 MW) | 1 |
| Medium (11-50 MW) | 1 |

**expected_online_date** — Unique values: 10, Nulls: 39

| Value | Count |
|-------|-------|
| 2026 | 3 |
| 2027 | 2 |
| $14 billion | 1 |
| $6 billion | 1 |
| 2025 | 1 |
| $300 million | 1 |
| 2028 | 1 |
| $3.6 billion | 1 |
| $10 billion | 1 |
| 250 | 1 |

**purpose** — Unique values: 8, Nulls: 25

| Value | Count |
|-------|-------|
| AI/Hyperscale | 14 |
| Cloud/AI | 5 |
| Meta | 2 |
| OpenAI/Oracle | 2 |
| AWS | 1 |
| OpenAI/Oracle/MGX | 1 |
| 2027 | 1 |
| Google | 1 |

**notes** — Unique values: 13, Nulls: 12

| Value | Count |
|-------|-------|
| AI/Hyperscale | 28 |
| Cloud/AI | 1 |
| 100 gas generators, 862MWh BESS | 1 |
| 100k GPUs | 1 |
| Building 4 268MW, Bldg 2 260MW | 1 |
| 3 of 5 buildings broke ground | 1 |
| 100k GPUs by 2026 | 1 |
| 100% renewable, recycled water | 1 |
| Community opposition | 1 |
| Phase 1 approved | 1 |
| Water concerns, 31M gal/yr | 1 |
| 1,300 acres | 1 |
| AI/Cloud | 1 |

**tier** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| Tier 1 | 26 |
| Tier 3 | 15 |
| Tier 2 | 11 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| capacity_mw | 2564.30 | 2546.37 | 48.00 | 9000.00 | 1800.00 |
| project_cost_usd | 4707250000.00 | 5033488874.53 | 29000000.00 | 10000000000.00 | 4400000000.00 |
| cooling_type | N/A | N/A | N/A | N/A | N/A |
| power_source | N/A | N/A | N/A | N/A | N/A |

#### Sample Data (First 3 Rows)

| facility_id | facility_name | operator | tenant | hyperscaler_category | city | state_province | country | status | capacity_mw | capacity_category | expected_online_date | project_cost_usd | cooling_type | power_source | purpose | source_url | notes | tier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DC-00001 | Stratos Hyperscale Campus | Bitzero Blockchain Inc. | nan | Other/Unclassified | nan | Utah | United States | Planned | 9000.0 | Mega campus (>1 | nan | nan | nan | nan | nan | Largest announced US project | AI/Hyperscale | Tier 1 |
| DC-00002 | Monarch Compute Campus | Nscale Ltd. | 2027 | Other/Unclassified | nan | West Virginia | United States | Planned | 8000.0 | Mega campus (>1 | nan | nan | nan | nan | nan | $1.6B+ investment | AI/Hyperscale | Tier 1 |
| DC-00003 | GW Ranch | Pacifico Energy | 2027 | Other/Unclassified | nan | Texas | United States | Planned | 7650.0 | Mega campus (>1 | nan | nan | nan | nan | nan | nan | AI/Hyperscale | Tier 1 |

---

### `data_centers\master_facility_list_v2.csv`

- **Size:** 0.01 MB (10,822 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 52
- **Columns:** 21

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 9 | tenant, state_province, country, status, capacity_category, expected_online_date, purpose, notes, tier |
| Numeric | 6 | latitude, longitude, capacity_mw, project_cost_usd, cooling_type, power_source |
| Date | 0 | — |
| Text | 6 | facility_id, facility_name, operator, hyperscaler_category, city, source_url |

#### Category Column Details

**tenant** — Unique values: 14, Nulls: 29

| Value | Count |
|-------|-------|
| 2027 | 5 |
| 2026 | 3 |
| 2028 | 2 |
| 2032 | 2 |
| Microsoft | 2 |
| 2036 | 1 |
| $33 billion | 1 |
| Google (unconfirmed) | 1 |
| xAI | 1 |
| OpenAI/Oracle | 1 |
| Meta | 1 |
| AWS | 1 |
| $40 billion+ | 1 |
| $10 billion+ | 1 |

**state_province** — Unique values: 17, Nulls: 2

| Value | Count |
|-------|-------|
| Arizona | 14 |
| Texas | 8 |
| California | 4 |
| Alabama | 3 |
| Arkansas | 3 |
| Utah | 2 |
| Louisiana | 2 |
| Virginia | 2 |
| Wyoming | 2 |
| Florida | 2 |
| Ohio | 2 |
| West Virginia | 1 |
| New Mexico | 1 |
| Pennsylvania | 1 |
| Alaska | 1 |

**country** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| United States | 50 |
| United Arab Emirates | 1 |
| Norway | 1 |

**status** — Unique values: 5, Nulls: 0

| Value | Count |
|-------|-------|
| Planned | 27 |
| Under Construction | 20 |
| Operating | 3 |
| Suspended | 1 |
| Expanding | 1 |

**capacity_category** — Unique values: 5, Nulls: 0

| Value | Count |
|-------|-------|
| Mega campus (>1 | 29 |
| Hyperscale (100-999 MW) | 16 |
| Unknown | 5 |
| Large (51-99 MW) | 1 |
| Medium (11-50 MW) | 1 |

**expected_online_date** — Unique values: 10, Nulls: 39

| Value | Count |
|-------|-------|
| 2026 | 3 |
| 2027 | 2 |
| $14 billion | 1 |
| $6 billion | 1 |
| 2025 | 1 |
| $300 million | 1 |
| 2028 | 1 |
| $3.6 billion | 1 |
| $10 billion | 1 |
| 250 | 1 |

**purpose** — Unique values: 8, Nulls: 25

| Value | Count |
|-------|-------|
| AI/Hyperscale | 14 |
| Cloud/AI | 5 |
| Meta | 2 |
| OpenAI/Oracle | 2 |
| AWS | 1 |
| OpenAI/Oracle/MGX | 1 |
| 2027 | 1 |
| Google | 1 |

**notes** — Unique values: 13, Nulls: 12

| Value | Count |
|-------|-------|
| AI/Hyperscale | 28 |
| Cloud/AI | 1 |
| 100 gas generators, 862MWh BESS | 1 |
| 100k GPUs | 1 |
| Building 4 268MW, Bldg 2 260MW | 1 |
| 3 of 5 buildings broke ground | 1 |
| 100k GPUs by 2026 | 1 |
| 100% renewable, recycled water | 1 |
| Community opposition | 1 |
| Phase 1 approved | 1 |
| Water concerns, 31M gal/yr | 1 |
| 1,300 acres | 1 |
| AI/Cloud | 1 |

**tier** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| Tier 1 | 26 |
| Tier 3 | 15 |
| Tier 2 | 11 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| latitude | 35.05 | 2.69 | 32.05 | 40.51 | 34.38 |
| longitude | -94.73 | 14.70 | -121.56 | -77.95 | -90.38 |
| capacity_mw | 2564.30 | 2546.37 | 48.00 | 9000.00 | 1800.00 |
| project_cost_usd | 4707250000.00 | 5033488874.53 | 29000000.00 | 10000000000.00 | 4400000000.00 |
| cooling_type | N/A | N/A | N/A | N/A | N/A |
| power_source | N/A | N/A | N/A | N/A | N/A |

#### Sample Data (First 3 Rows)

| facility_id | facility_name | operator | tenant | hyperscaler_category | city | state_province | country | latitude | longitude | status | capacity_mw | capacity_category | expected_online_date | project_cost_usd | cooling_type | power_source | purpose | source_url | notes | tier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DC-00001 | Stratos Hyperscale Campus | Bitzero Blockchain Inc. | nan | Bitzero | nan | Utah | United States | nan | nan | Planned | 9000.0 | Mega campus (>1 | nan | nan | nan | nan | nan | Largest announced US project | AI/Hyperscale | Tier 1 |
| DC-00002 | Monarch Compute Campus | Nscale Ltd. | 2027 | Nscale | nan | West Virginia | United States | nan | nan | Planned | 8000.0 | Mega campus (>1 | nan | nan | nan | nan | nan | $1.6B+ investment | AI/Hyperscale | Tier 1 |
| DC-00003 | GW Ranch | Pacifico Energy | 2027 | Pacifico Energy | nan | Texas | United States | nan | nan | Planned | 7650.0 | Mega campus (>1 | nan | nan | nan | nan | nan | nan | AI/Hyperscale | Tier 1 |

---

### `data_centers\master_facility_list_v3_enriched.csv`

- **Size:** 0.02 MB (22,539 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 52
- **Columns:** 53

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 16 | tenant, hyperscaler_category, state_province, country, status, capacity_category, expected_online_date, purpose, notes, tier, utility, generation_mix, cooling_detail, network_detail, gpu_generation, primary_gpu |
| Numeric | 31 | capacity_mw, project_cost_usd, cooling_type, power_source, it_load_mw, est_gpus_h100, est_gpus_b200, est_gpus_mi300x, est_gpus_gb200_nvl72, est_racks_50kw, est_racks_100kw, est_bf16_pflops, est_fp8_pflops, voltage_kv, ppa_price_mwh, water_source_mgd, cluster_size, total_capex_billion, est_capex_per_kw, est_capex_per_gpu, est_gpu_count, training_bf16_pflops, inference_fp8_pflops, est_tokens_per_sec_billions, est_training_runs_per_year_gpt4_class, annual_power_mwh, annual_power_cost_usd, annual_revenue_potential_usd, power_cost_per_gpu_per_year, latitude, longitude |
| Date | 0 | — |
| Text | 6 | facility_id, facility_name, operator, city, source_url, source_notes |

#### Category Column Details

**tenant** — Unique values: 14, Nulls: 29

| Value | Count |
|-------|-------|
| 2027 | 5 |
| 2026 | 3 |
| 2028 | 2 |
| 2032 | 2 |
| Microsoft | 2 |
| 2036 | 1 |
| $33 billion | 1 |
| Google (unconfirmed) | 1 |
| xAI | 1 |
| OpenAI/Oracle | 1 |
| Meta | 1 |
| AWS | 1 |
| $40 billion+ | 1 |
| $10 billion+ | 1 |

**hyperscaler_category** — Unique values: 15, Nulls: 0

| Value | Count |
|-------|-------|
| Other/Unclassified | 26 |
| Meta | 4 |
| AWS | 3 |
| Oracle | 3 |
| Google | 3 |
| Microsoft | 3 |
| Crusoe | 2 |
| Stargate | 1 |
| xAI | 1 |
| Prime Data Centers | 1 |
| NTT | 1 |
| Stream Data Centers | 1 |
| Vantage | 1 |
| Aligned | 1 |
| Apple | 1 |

**state_province** — Unique values: 17, Nulls: 2

| Value | Count |
|-------|-------|
| Arizona | 14 |
| Texas | 8 |
| California | 4 |
| Alabama | 3 |
| Arkansas | 3 |
| Utah | 2 |
| Louisiana | 2 |
| Virginia | 2 |
| Wyoming | 2 |
| Florida | 2 |
| Ohio | 2 |
| West Virginia | 1 |
| New Mexico | 1 |
| Pennsylvania | 1 |
| Alaska | 1 |

**country** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| United States | 50 |
| United Arab Emirates | 1 |
| Norway | 1 |

**status** — Unique values: 5, Nulls: 0

| Value | Count |
|-------|-------|
| Planned | 27 |
| Under Construction | 20 |
| Operating | 3 |
| Suspended | 1 |
| Expanding | 1 |

**capacity_category** — Unique values: 5, Nulls: 0

| Value | Count |
|-------|-------|
| Mega campus (>1 | 29 |
| Hyperscale (100-999 MW) | 16 |
| Unknown | 5 |
| Large (51-99 MW) | 1 |
| Medium (11-50 MW) | 1 |

**expected_online_date** — Unique values: 10, Nulls: 39

| Value | Count |
|-------|-------|
| 2026 | 3 |
| 2027 | 2 |
| $14 billion | 1 |
| $6 billion | 1 |
| 2025 | 1 |
| $300 million | 1 |
| 2028 | 1 |
| $3.6 billion | 1 |
| $10 billion | 1 |
| 250 | 1 |

**purpose** — Unique values: 8, Nulls: 25

| Value | Count |
|-------|-------|
| AI/Hyperscale | 14 |
| Cloud/AI | 5 |
| Meta | 2 |
| OpenAI/Oracle | 2 |
| AWS | 1 |
| OpenAI/Oracle/MGX | 1 |
| 2027 | 1 |
| Google | 1 |

**notes** — Unique values: 13, Nulls: 12

| Value | Count |
|-------|-------|
| AI/Hyperscale | 28 |
| Cloud/AI | 1 |
| 100 gas generators, 862MWh BESS | 1 |
| 100k GPUs | 1 |
| Building 4 268MW, Bldg 2 260MW | 1 |
| 3 of 5 buildings broke ground | 1 |
| 100k GPUs by 2026 | 1 |
| 100% renewable, recycled water | 1 |
| Community opposition | 1 |
| Phase 1 approved | 1 |
| Water concerns, 31M gal/yr | 1 |
| 1,300 acres | 1 |
| AI/Cloud | 1 |

**tier** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| Tier 1 | 26 |
| Tier 3 | 15 |
| Tier 2 | 11 |

**utility** — Unique values: 7, Nulls: 42

| Value | Count |
|-------|-------|
| Entergy Louisiana | 2 |
| PacifiCorp / WAPA | 2 |
| Oncor / ERCOT | 2 |
| IID / CAISO | 1 |
| Georgia Power / Southern Company | 1 |
| PG&E | 1 |
| Entergy Arkansas | 1 |

**generation_mix** — Unique values: 7, Nulls: 42

| Value | Count |
|-------|-------|
| Gas 60%, Nuclear 25%, Renewable 15% | 2 |
| Wind 50%, Gas 30%, Coal 20% | 2 |
| Wind 35%, Solar 25%, Gas 30%, Nuclear 10% | 2 |
| Solar 50%, Geothermal 20%, Gas 30% | 1 |
| Gas 40%, Nuclear 30%, Coal 15%, Renewable 15% | 1 |
| Solar 30%, Hydro 25%, Gas 25%, Nuclear 15%, Wind 5% | 1 |
| Gas 50%, Nuclear 25%, Renewable 25% | 1 |

**cooling_detail** — Unique values: 7, Nulls: 42

| Value | Count |
|-------|-------|
| Direct-to-chip liquid (80%) + rear-door (20%) | 2 |
| Direct liquid cooling (DLC) | 2 |
| Direct liquid cooling (DLC) 100% | 2 |
| Hybrid air/liquid, 100 gas generators + 862MWh BESS | 1 |
| Rear-door heat exchanger + liquid assist | 1 |
| Hybrid air/water, 95% free cooling | 1 |
| Direct-to-chip liquid (TPU pods) | 1 |

**network_detail** — Unique values: 7, Nulls: 42

| Value | Count |
|-------|-------|
| NVL72 + InfiniBand NDR 400G, 800G ZR+ to Atlanta/Dallas | 2 |
| 400G/800G to Denver/Salt Lake | 2 |
| NVL72 + InfiniBand NDR, 1.6T to Dallas | 2 |
| InfiniBand NDR, 800G to LA/San Diego | 1 |
| InfiniBand NDR 400G, 800G to Chicago/Dallas | 1 |
| 100G/400G to San Jose/Sacramento | 1 |
| Custom optical circuit switching, 1.6T regional | 1 |

**gpu_generation** — Unique values: 8, Nulls: 42

| Value | Count |
|-------|-------|
| H100 (2025), B200 (2026+) | 2 |
| H100 / B200 | 2 |
| GB200 NVL72 / GB300 | 1 |
| H100 / TPU v5 | 1 |
| H100 / Maia 100 | 1 |
| GB200 NVL72 | 1 |
| Trainium2 / Inferentia2 | 1 |
| TPU v5p / v6 | 1 |

**primary_gpu** — Unique values: 6, Nulls: 0

| Value | Count |
|-------|-------|
| H100 (est.) | 42 |
| B200 | 4 |
| GB200 NVL72 | 2 |
| H100 | 2 |
| Trainium2/Inferentia2 | 1 |
| TPU v5p/v6 | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| capacity_mw | 2564.30 | 2546.37 | 48.00 | 9000.00 | 1800.00 |
| project_cost_usd | 4707250000.00 | 5033488874.53 | 29000000.00 | 10000000000.00 | 4400000000.00 |
| cooling_type | N/A | N/A | N/A | N/A | N/A |
| power_source | N/A | N/A | N/A | N/A | N/A |
| it_load_mw | 2256.58 | 2240.81 | 42.20 | 7920.00 | 1584.00 |
| est_gpus_h100 | 361053.38 | 358529.35 | 6758.00 | 1267200.00 | 253440.00 |
| est_gpus_b200 | 225658.35 | 224080.86 | 4224.00 | 792000.00 | 158400.00 |
| est_gpus_mi300x | 338487.60 | 336121.21 | 6336.00 | 1188000.00 | 237600.00 |
| est_gpus_gb200_nvl72 | 1353950.40 | 1344484.85 | 25344.00 | 4752000.00 | 950400.00 |
| est_racks_50kw | 45131.57 | 44816.26 | 844.00 | 158400.00 | 31680.00 |
| est_racks_100kw | 22565.78 | 22408.14 | 422.00 | 79200.00 | 15840.00 |
| est_bf16_pflops | 1003.74 | 1261.76 | 0.00 | 4579.70 | 254.45 |
| est_fp8_pflops | 2007.74 | 2523.86 | 0.00 | 9160.60 | 508.95 |
| voltage_kv | 372.50 | 131.09 | 115.00 | 500.00 | 345.00 |
| ppa_price_mwh | 40.00 | 10.64 | 30.00 | 65.00 | 36.50 |
| water_source_mgd | 3.67 | 3.35 | 0.80 | 12.00 | 2.75 |
| cluster_size | 91948.80 | 146019.73 | 8192.00 | 500000.00 | 49152.00 |
| total_capex_billion | 6.02 | 3.82 | 0.50 | 10.00 | 5.50 |
| est_capex_per_kw | 7242.67 | 9055.01 | 1852.00 | 30303.00 | 5000.00 |
| est_capex_per_gpu | 51440.00 | 64311.33 | 13152.00 | 215220.00 | 35511.00 |
| est_gpu_count | 272521.06 | 342102.51 | 0.00 | 1267200.00 | 93280.00 |
| training_bf16_pflops | 320.29 | 396.30 | 0.00 | 1425.60 | 109.70 |
| inference_fp8_pflops | 640.77 | 792.83 | 0.00 | 2851.20 | 219.40 |
| est_tokens_per_sec_billions | 0.04 | 0.05 | 0.00 | 0.19 | 0.01 |
| est_training_runs_per_year_gpt4_class | 0.40 | 0.50 | 0.00 | 1.80 | 0.15 |
| annual_power_mwh | 19767675.80 | 19629478.89 | 370022.00 | 69379200.00 | 13875840.00 |
| annual_power_cost_usd | 810951498.73 | 791547588.53 | 24051456.00 | 2653754400.00 | 520344000.00 |
| annual_revenue_potential_usd | 837937537.20 | 830644450.75 | 15988752.00 | 2997181440.00 | 561971520.00 |
| power_cost_per_gpu_per_year | 2403.70 | 659.25 | 657.00 | 4380.00 | 2300.00 |
| latitude | 24.14 | nan | 24.14 | 24.14 | 24.14 |
| longitude | 54.46 | nan | 54.46 | 54.46 | 54.46 |

#### Sample Data (First 3 Rows)

| facility_id | facility_name | operator | tenant | hyperscaler_category | city | state_province | country | status | capacity_mw | capacity_category | expected_online_date | project_cost_usd | cooling_type | power_source | purpose | source_url | notes | tier | it_load_mw | est_gpus_h100 | est_gpus_b200 | est_gpus_mi300x | est_gpus_gb200_nvl72 | est_racks_50kw | est_racks_100kw | est_bf16_pflops | est_fp8_pflops | utility | voltage_kv | ppa_price_mwh | generation_mix | cooling_detail | water_source_mgd | network_detail | gpu_generation | cluster_size | total_capex_billion | est_capex_per_kw | est_capex_per_gpu | source_notes | primary_gpu | est_gpu_count | training_bf16_pflops | inference_fp8_pflops | est_tokens_per_sec_billions | est_training_runs_per_year_gpt4_class | annual_power_mwh | annual_power_cost_usd | annual_revenue_potential_usd | power_cost_per_gpu_per_year | latitude | longitude |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DC-00001 | Stratos Hyperscale Campus | Bitzero Blockchain Inc. | nan | Other/Unclassified | nan | Utah | United States | Planned | 9000.0 | Mega campus (>1 | nan | nan | nan | nan | nan | Largest announced US project | AI/Hyperscale | Tier 1 | 7920.0 | 1267200.0 | 792000.0 | 1188000.0 | 4752000.0 | 158400.0 | 79200.0 | 4579.7 | 9160.6 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | Largest announced US project | H100 (est.) | 1267200 | 1253.3 | 2507.8 | 0.19008 | 1.6 | 69379200.0 | 2428272000.0 | 2997181440.0 | 1916.0 | nan | nan |
| DC-00002 | Monarch Compute Campus | Nscale Ltd. | 2027 | Other/Unclassified | nan | West Virginia | United States | Planned | 8000.0 | Mega campus (>1 | nan | nan | nan | nan | nan | $1.6B+ investment | AI/Hyperscale | Tier 1 | 7040.0 | 1126400.0 | 704000.0 | 1056000.0 | 4224000.0 | 140800.0 | 70400.0 | 4070.8 | 8142.7 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | $1.6B+ investment | H100 (est.) | 1126400 | 1114.0 | 2229.1 | 0.16896 | 1.4 | 61670400.0 | 2158464000.0 | 2664161280.0 | 1916.0 | nan | nan |
| DC-00003 | GW Ranch | Pacifico Energy | 2027 | Other/Unclassified | nan | Texas | United States | Planned | 7650.0 | Mega campus (>1 | nan | nan | nan | nan | nan | nan | AI/Hyperscale | Tier 1 | 6732.0 | 1077120.0 | 673200.0 | 1009800.0 | 4039200.0 | 134640.0 | 67320.0 | 3892.7 | 7786.5 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | H100 (est.) | 1077120 | 1065.3 | 2131.6 | 0.161568 | 1.3 | 58972320.0 | 2653754400.0 | 2547604224.0 | 2464.0 | nan | nan |

---

### `data_centers\master_global_datacenters.csv`

- **Size:** 2.92 MB (3,065,393 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 19,694
- **Columns:** 25

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 9 | source, status, capacity_category, expected_online_date, cooling_type, power_source, tenant, purpose, community_pushback |
| Numeric | 3 | property_size_acres, latitude, longitude |
| Date | 0 | — |
| Text | 13 | facility_name, operator, city, state_province, country, address, capacity_mw, facility_size_sqft, project_cost_usd, notes, source_url, date_added, last_updated |

#### Category Column Details

**source** — Unique values: 4, Nulls: 0

| Value | Count |
|-------|-------|
| GitHub_GlobalMap | 18089 |
| FracTracker_US | 1579 |
| DataCenterMap | 15 |
| DCMap_Pipeline | 11 |

**status** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| Operating | 18607 |
| Planned | 728 |
| Under Construction | 159 |
| Cancelled | 64 |
| Expanding | 60 |
| Suspended | 59 |
| Reference | 15 |
| Pre-proposal | 2 |

**capacity_category** — Unique values: 22, Nulls: 18089

| Value | Count |
|-------|-------|
| Unknown | 873 |
| Hyperscale (100-999 MW) | 338 |
| Mega campus (>1,000 MW) | 124 |
| Medium (11-50 MW) | 117 |
| Small (0-10 MW) | 100 |
| Large (51-99 MW) | 37 |
| Hyperscale (101-999 MW) | 1 |
| Total facilities: 4497 | 1 |
| Total facilities: 527 | 1 |
| Total facilities: 561 | 1 |
| Total facilities: 369 | 1 |
| Total facilities: 393 | 1 |
| Total facilities: 289 | 1 |
| Total facilities: 286 | 1 |
| Total facilities: 259 | 1 |

**expected_online_date** — Unique values: 16, Nulls: 19554

| Value | Count |
|-------|-------|
| 2027 | 49 |
| 2028 | 27 |
| 2026 | 27 |
| 2030 | 12 |
| 2029 | 8 |
| 2032 | 3 |
| 2025 | 3 |
| 2027-28 | 2 |
| 2036 | 2 |
| Full buildout by 2037 | 1 |
| Full buildout by 2035 | 1 |
| Buildout by 2028 | 1 |
| 2024 | 1 |
| 20027 | 1 |
| 2035 | 1 |

**cooling_type** — Unique values: 3, Nulls: 19632

| Value | Count |
|-------|-------|
| Closed loop | 58 |
| Fans | 2 |
| Open loop | 2 |

**power_source** — Unique values: 21, Nulls: 19579

| Value | Count |
|-------|-------|
| Grid (unspecified mix) | 45 |
| Natural gas | 34 |
| Hybrid (onsite and grid) | 6 |
| Solar | 5 |
| Nuclear | 4 |
| Oil/Diesel | 2 |
| Coal | 2 |
| Natural gas, Hybrid (onsite and grid) | 2 |
| Solar, Grid (unspecified mix) | 2 |
| Fuel Cells | 2 |
| Solar, Grid (unspecified mix), Natural gas | 1 |
| Hydroelectric | 1 |
| Biomass | 1 |
| Hydroelectric, Grid (unspecified mix) | 1 |
| Wind, Solar | 1 |

**tenant** — Unique values: 2, Nulls: 19692

| Value | Count |
|-------|-------|
| Multiple colocation tenants | 1 |
| Anthropic | 1 |

**purpose** — Unique values: 29, Nulls: 19594

| Value | Count |
|-------|-------|
| AI | 40 |
| Country-level aggregate | 15 |
| AI/Hyperscale | 11 |
| Crypto | 5 |
| Bitcoin transitioning to AI | 3 |
| AI Data center and solar fam | 2 |
| Bitcoin | 2 |
| Telecom / network data center | 1 |
| AI/cloud-computing | 1 |
| cloud services | 1 |
| Colocation / enterprise data center | 1 |
| Hyperscale cloud data-center campus | 1 |
| Cryptocurrency mining data center | 1 |
| AI "superfactory" | 1 |
| Hyperscale Cloud & AI Workloads | 1 |

**community_pushback** — Unique values: 2, Nulls: 18126

| Value | Count |
|-------|-------|
| Unknown | 1308 |
| Yes | 260 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| property_size_acres | 465.19 | 2017.67 | 1.00 | 40000.00 | 121.00 |
| latitude | 37.67 | 4.21 | 21.48 | 70.18 | 38.76 |
| longitude | -87.34 | 12.54 | -158.02 | -67.02 | -84.09 |

#### Sample Data (First 3 Rows)

| source | facility_name | operator | city | state_province | country | address | status | capacity_mw | capacity_category | facility_size_sqft | property_size_acres | project_cost_usd | expected_online_date | latitude | longitude | cooling_type | power_source | tenant | purpose | community_pushback | notes | source_url | date_added | last_updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub_GlobalMap | NAP de las Americas Madrid | Terremark | Madrid | nan | Spain | Calle de Yecora, 4 28009 Madrid Spain | Operating | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan |
| GitHub_GlobalMap | Central Office 2 | StarHub Ltd. | Singapore | nan | Singapore | 19 Tai Seng Dr 535222 Singapore Singapore | Operating | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan |
| GitHub_GlobalMap | Cluj-Napoca | GTS Telecom SRL | Cluj-Napoca | nan | Romania | Str. Garii nr. 21 400267 Cluj-Napoca Romania | Operating | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan |

---

### `data_centers\module_17_enterprise_contract_lag.csv`

- **Size:** 0.0 MB (2,729 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 11
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 9 | module, metric, value, unit, source, source_url, date_accessed, confidence, notes |
| Numeric | 0 | — |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**module** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| Enterprise_Contract_Lag | 11 |

**metric** — Unique values: 11, Nulls: 0

| Value | Count |
|-------|-------|
| average_contract_length | 1 |
| contract_renewal_window_months_before_expiry | 1 |
| reserved_capacity_share_of_hyperscaler_revenue | 1 |
| on_demand_share_of_hyperscaler_revenue | 1 |
| gpu_reservation_lead_time_months | 1 |
| enterprise_ai_pilot_to_production_rate | 1 |
| average_pilot_duration_months | 1 |
| contract_lag_to_revenue_recognition_months | 1 |
| renewal_rate_hyperscaler_cloud | 1 |
| enterprise_ai_budget_committed_vs_experimental | 1 |
| capacity_block_duration_aws_google_azure | 1 |

**value** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| 3 | 2 |
| 6 | 2 |
| 0.65 | 1 |
| 0.35 | 1 |
| 0.12 | 1 |
| 8 | 1 |
| 0.95 | 1 |
| 0.70 | 1 |
| 1_3 | 1 |

**unit** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| percent | 5 |
| months | 4 |
| years | 2 |

**source** — Unique values: 11, Nulls: 0

| Value | Count |
|-------|-------|
| Salesforce 10-K FY2024; Microsoft 10-K FY2024; Google 10-K FY2024 | 1 |
| Gartner IT Spending Forecast 2025; Flexera State of Cloud Report 2025 | 1 |
| Synergy Research Group Q4 2025; Canalys Cloud Channels Analysis 2025 | 1 |
| Synergy Research Group Q4 2025 | 1 |
| NVIDIA H100/B200 allocation reports; CoreWeave/lambda capacity blocks | 1 |
| McKinsey State of AI 2025; IDC AI Adoption Tracker 2025 | 1 |
| Deloitte State of AI in Enterprise 2025; Gartner AI Pilot Survey 2025 | 1 |
| ASC 606 revenue recognition; hyperscaler earnings calls Q4 2025 | 1 |
| Synergy Research Group 2025; KeyBanc Capital Markets Cloud Survey 2025 | 1 |
| Morgan Stanley CIO Survey 2025; Piper Sandler IT Spend Survey 2025 | 1 |
| AWS Capacity Blocks docs; Google Cloud Future Reservations; Azure Reserved Instances | 1 |

**source_url** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.synergyresearch.com | 3 |
| https://www.sec.gov/edgar | 1 |
| https://www.gartner.com | 1 |
| https://www.nvidia.com | 1 |
| https://www.mckinsey.com | 1 |
| https://www.deloitte.com | 1 |
| https://www.fasb.org | 1 |
| https://www.morganstanley.com | 1 |
| https://aws.amazon.com | 1 |

**date_accessed** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-07-14 | 11 |

**confidence** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| High | 7 |
| Medium | 4 |

**notes** — Unique values: 9, Nulls: 2

| Value | Count |
|-------|-------|
| Enterprise cloud agreements typically 3-year committed spend | 1 |
| Renewal negotiations typically start 6-12 months before expiry | 1 |
| Reserved instances / committed use discounts dominate hyperscaler revenue | 1 |
| GPU capacity blocks require 3-9 month advance reservation | 1 |
| Only 12% of AI pilots reach production (88% failure rate per Forrester 2026) | 1 |
| Revenue recognized ratably over contract term; 3-month lag typical | 1 |
| Net revenue retention >130% for major hyperscalers | 1 |
| 70% of AI budget in committed contracts vs 30% experimental | 1 |
| 1-3 year committed capacity blocks standard for AI workloads | 1 |

#### Sample Data (First 3 Rows)

| module | metric | value | unit | source | source_url | date_accessed | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Enterprise_Contract_Lag | average_contract_length | 3 | years | Salesforce 10-K FY2024; Microsoft 10-K FY2024; Goo | https://www.sec.gov/edgar | 2026-07-14 | High | Enterprise cloud agreements typically 3-year commi |
| Enterprise_Contract_Lag | contract_renewal_window_months_before_expiry | 6 | months | Gartner IT Spending Forecast 2025; Flexera State o | https://www.gartner.com | 2026-07-14 | Medium | Renewal negotiations typically start 6-12 months b |
| Enterprise_Contract_Lag | reserved_capacity_share_of_hyperscaler_revenue | 0.65 | percent | Synergy Research Group Q4 2025; Canalys Cloud Chan | https://www.synergyresearch.com | 2026-07-14 | High | Reserved instances / committed use discounts domin |

---

### `data_centers\module_18_agentic_liability_compliance.csv`

**Error:** Error tokenizing data. C error: Expected 9 fields in line 9, saw 10


### `data_centers\module_19_physical_infra_constraints.csv`

- **Size:** 0.01 MB (7,511 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 34
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 4 | module, unit, date_accessed, confidence |
| Numeric | 1 | value |
| Date | 0 | — |
| Text | 4 | metric, source, source_url, notes |

#### Category Column Details

**module** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| Physical_Infra_Constraints | 34 |

**unit** — Unique values: 12, Nulls: 0

| Value | Count |
|-------|-------|
| percent | 7 |
| USD | 6 |
| GW | 3 |
| WPM | 3 |
| months | 3 |
| weeks | 2 |
| units | 2 |
| GB | 2 |
| year | 2 |
| ratio | 2 |
| count | 1 |
| MW_per_MGD | 1 |

**date_accessed** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-07-14 | 34 |

**confidence** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| High | 22 |
| Medium | 11 |
| Low | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| value | 14844547.63 | 85726132.99 | 0.13 | 500000000.00 | 100.00 |

#### Sample Data (First 3 Rows)

| module | metric | value | unit | source | source_url | date_accessed | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Physical_Infra_Constraints | us_grid_connection_queue_gw | 2600.0 | GW | LBNL Queued Up 2024; PJM/ERCOT/CAISO/MISO/NYISO/IS | https://queuedup.lbl.gov | 2026-07-14 | High | Total generation+storage in US ISO/RTO queues as o |
| Physical_Infra_Constraints | us_data_center_queue_gw | 300.0 | GW | LBNL Queued Up 2024 (filtered for data center/stor | https://queuedup.lbl.gov | 2026-07-14 | Medium | Estimated data center portion of interconnection q |
| Physical_Infra_Constraints | transformer_lead_time_weeks | 128.0 | weeks | Wood Mackenzie Q2 2025 Transformer Survey; MegaGri | https://www.woodmac.com | 2026-07-14 | High | Standard power transformers: 128 weeks; GSU: 144 w |

---

### `data_centers\module_20_systems_dynamics.csv`

- **Size:** 0.02 MB (17,330 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 81
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 4 | module, unit, date_accessed, confidence |
| Numeric | 1 | value |
| Date | 0 | — |
| Text | 4 | metric, source, source_url, notes |

#### Category Column Details

**module** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| Systems_Dynamics | 81 |

**unit** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| ratio | 58 |
| count | 8 |
| USD_B | 7 |
| months | 3 |
| USD_M | 2 |
| GW | 2 |
| USD_T | 1 |

**date_accessed** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-07-14 | 81 |

**confidence** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| High | 54 |
| Medium | 25 |
| Low | 2 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| value | 414.11 | 2444.31 | 0.05 | 20000.00 | 0.65 |

#### Sample Data (First 3 Rows)

| module | metric | value | unit | source | source_url | date_accessed | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Systems_Dynamics | ai_capex_to_revenue_ratio_hyperscalers | 0.52 | ratio | American Century Investments 2026; Introl Blog 202 | https://www.americancentury.com | 2026-07-14 | High | Meta 52%, AWS 57%, Microsoft 48%, Google 45% capex |
| Systems_Dynamics | ai_capex_growth_rate_2025_yoy | 0.73 | ratio | Introl Blog 2026; Company earnings 2025 | https://blakecrosley.com | 2026-07-14 | High | Big 5 hyperscaler capex: $256B (2024) -> $443B (20 |
| Systems_Dynamics | ai_capex_2026_projected_billion_usd | 602.0 | USD_B | Introl Blog 2026; Goldman Sachs 2025; Company guid | https://blakecrosley.com | 2026-07-14 | High | Big 5 projected $602B capex in 2026 (+36% YoY) |

---

### `data_centers\module_21_jevons_paradox.csv`

- **Size:** 0.01 MB (5,700 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 26
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 5 | module, unit, source_url, date_accessed, confidence |
| Numeric | 1 | value |
| Date | 0 | — |
| Text | 3 | metric, source, notes |

#### Category Column Details

**module** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| Jevons_Paradox | 26 |

**unit** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| ratio | 22 |
| USD_B | 3 |
| USD | 1 |

**source_url** — Unique values: 13, Nulls: 0

| Value | Count |
|-------|-------|
| https://arxiv.org | 5 |
| https://agentmarketcap.ai | 5 |
| https://www.idc.com | 4 |
| https://llmcompare.dev | 2 |
| https://www.digitalapplied.com | 2 |
| https://epochai.org | 1 |
| https://www.nvidia.com | 1 |
| https://github.com/apache/tvm | 1 |
| https://www.groq.com | 1 |
| https://developer.nvidia.com | 1 |
| https://deepmind.google | 1 |
| https://www.semianalysis.com | 1 |
| https://openrouter.ai | 1 |

**date_accessed** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-07-14 | 26 |

**confidence** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| High | 13 |
| Medium | 12 |
| Low | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| value | 30.20 | 68.43 | 0.00 | 255.00 | 0.80 |

#### Sample Data (First 3 Rows)

| module | metric | value | unit | source | source_url | date_accessed | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Jevons_Paradox | inference_cost_reduction_rate_annual_pct | 0.5 | ratio | LLMCompare 2026; LLM Pricing Trends 2026; Together | https://llmcompare.dev | 2026-07-14 | High | API price per 1M tokens falling ~50%/year since GP |
| Jevons_Paradox | training_cost_reduction_rate_annual_pct | 0.4 | ratio | Epoch AI 2025; SemiAnalysis training cost tracker  | https://epochai.org | 2026-07-14 | Medium | Training compute efficiency improving ~40%/year (a |
| Jevons_Paradox | hardware_utilization_improvement_rate_pct | 0.3 | ratio | NVIDIA Hopper/Blackwell architecture; vLLM/SGLang  | https://www.nvidia.com | 2026-07-14 | Medium | KV cache optimization, PagedAttention, tensor para |

---

### `data_centers\module_22_open_source_commoditization.csv`

- **Size:** 0.01 MB (6,085 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 28
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 5 | module, unit, source_url, date_accessed, confidence |
| Numeric | 0 | — |
| Date | 0 | — |
| Text | 4 | metric, value, source, notes |

#### Category Column Details

**module** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| Open_Source_Commoditization | 28 |

**unit** — Unique values: 6, Nulls: 0

| Value | Count |
|-------|-------|
| ratio | 10 |
| count | 8 |
| points | 5 |
| USD | 3 |
| date | 1 |
| USD_M | 1 |

**source_url** — Unique values: 11, Nulls: 0

| Value | Count |
|-------|-------|
| https://whatllm.org | 10 |
| https://amirteymoori.com | 5 |
| https://llmcompare.dev | 2 |
| https://artificialanalysis.ai | 2 |
| https://pricepertoken.com | 2 |
| https://precisionaiacademy.com | 2 |
| https://chinaapi.ai | 1 |
| https://alphacorp.ai | 1 |
| https://huggingface.co | 1 |
| https://ai.meta.com | 1 |
| https://github.com/THUDM/GLM-4 | 1 |

**date_accessed** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-07-14 | 28 |

**confidence** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| High | 21 |
| Medium | 7 |

#### Sample Data (First 3 Rows)

| module | metric | value | unit | source | source_url | date_accessed | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Open_Source_Commoditization | open_source_model_count_2025 | 59 | count | WhatLLM 2025; Artificial Analysis 2026 | https://whatllm.org | 2026-07-14 | High | 59 open source vs 35 proprietary models tracked |
| Open_Source_Commoditization | open_source_share_pct | 0.63 | ratio | WhatLLM 2025 | https://whatllm.org | 2026-07-14 | High | 63% of models in dataset are open source |
| Open_Source_Commoditization | quality_gap_open_vs_closed_2025_points | 7 | points | WhatLLM 2025; Artificial Analysis 2026 | https://whatllm.org | 2026-07-14 | High | Best open (MiniMax-M2: 61) vs best closed (GPT-5:  |

---

### `data_centers\module_23_compute_supply_cycle.csv`

- **Size:** 0.01 MB (5,352 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 24
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 5 | module, unit, source_url, date_accessed, confidence |
| Numeric | 0 | — |
| Date | 0 | — |
| Text | 4 | metric, value, source, notes |

#### Category Column Details

**module** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| Compute_Supply_Cycle | 24 |

**unit** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| ratio | 8 |
| months | 3 |
| wpm | 3 |
| GB | 3 |
| weeks | 3 |
| USD_B | 1 |
| category | 1 |
| days | 1 |
| boolean | 1 |

**source_url** — Unique values: 14, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.tsmc.com | 3 |
| https://www.trendforce.com | 3 |
| https://www.cbre.com | 3 |
| https://semianalysis.com | 3 |
| https://www.skhynix.com | 2 |
| https://agentmarketcap.ai | 2 |
| https://www.nvidia.com | 1 |
| https://www.marvell.com | 1 |
| https://www.vertiv.com | 1 |
| https://www.telegeography.com | 1 |
| https://www.semiconductors.org | 1 |
| https://www.amazonaws.com | 1 |
| https://blakecrosley.com | 1 |
| https://gpuaas.com | 1 |

**date_accessed** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-07-14 | 24 |

**confidence** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| High | 15 |
| Medium | 8 |
| Low | 1 |

#### Sample Data (First 3 Rows)

| module | metric | value | unit | source | source_url | date_accessed | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Compute_Supply_Cycle | gpu_order_to_delivery_lead_time_months | 6 | months | NVIDIA earnings calls 2025; SemiAnalysis supply ch | https://www.nvidia.com | 2026-07-14 | High | H100/B200: 6-9 months from order to delivery |
| Compute_Supply_Cycle | wafer_allocation_nvidia_pct_tsmc_5nm | 0.60 | ratio | SemiAnalysis 2025; TSMC earnings calls 2025 | https://www.tsmc.com | 2026-07-14 | High | NVIDIA consumes ~60% of TSMC 5nm/4N capacity |
| Compute_Supply_Cycle | cowos_monthly_capacity_2024_wpm | 35000 | wpm | TrendForce 2024; TSMC earnings 2024 | https://www.trendforce.com | 2026-07-14 | High | TSMC CoWoS monthly wafer capacity end of 2024 |

---

### `data_centers\module_24_capital_market_reflexivity.csv`

- **Size:** 0.0 MB (4,195 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 17
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 8 | module, metric, unit, source, source_url, date_accessed, confidence, notes |
| Numeric | 1 | value |
| Date | 0 | — |
| Text | 0 | — |

#### Category Column Details

**module** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| Capital_Market_Reflexivity | 17 |

**metric** — Unique values: 17, Nulls: 0

| Value | Count |
|-------|-------|
| valuation_to_funding_cost_elasticity | 1 |
| capex_to_revenue_sensitivity_hyperscalers | 1 |
| downward_deleveraging_multiplier | 1 |
| valuation_overshoot_pct_above_fundamental | 1 |
| ai_capex_as_pct_hyperscaler_revenue | 1 |
| capex_per_incremental_revenue_usd | 1 |
| hyperscaler_capex_2026_billion_usd | 1 |
| passive_fund_flow_to_tech_pct_equity_flows | 1 |
| short_interest_ai_stocks_pct_float | 1 |
| call_option_skew_ai_stocks | 1 |
| margin_debt_yoy_change_pct | 1 |
| valuation_overshoot_correction_lag_quarters | 1 |
| reflexivity_amplification_factor | 1 |
| etf_tech_concentration_pct | 1 |
| index_fund_forced_buying_pct_flows | 1 |

**unit** — Unique values: 4, Nulls: 0

| Value | Count |
|-------|-------|
| ratio | 13 |
| USD_B | 2 |
| USD | 1 |
| quarters | 1 |

**source** — Unique values: 16, Nulls: 0

| Value | Count |
|-------|-------|
| Morgan Stanley 2026; American Century 2026 | 2 |
| Morgan Stanley 2026; American Century 2026; SemiAnalysis 2026 | 1 |
| IntuitionLabs AI Bubble vs Dot-com 2026; Aswath Damodaran 2026 | 1 |
| American Century 2026; Introl 2026; Company 10-Ks 2025 | 1 |
| AgentMarketCap 2026; CoreWeave 2026 guidance | 1 |
| Introl Blog 2026; Goldman Sachs 2025; Company guidance 2025 | 1 |
| EPFR Global 2025; BofA Flow Show 2025; Goldman Sachs Global Portfolio Strategy 2025 | 1 |
| S3 Partners 2026; Bloomberg Short Interest 2026 | 1 |
| Cboe Skew Index 2026; Goldman Sachs Derivatives Research 2026 | 1 |
| FINRA Margin Statistics 2026; NYSE Margin Debt 2026 | 1 |
| IntuitionLabs 2026; Aswath Damodaran 2026; Dot-com 2000-2002 analog | 1 |
| Soros reflexivity theory; Shiller 2025; Morgan Stanley 2026 | 1 |
| SPY/XLK holdings 2026; Bloomberg ETF Flows 2026 | 1 |
| Vanguard/BlackRock/State Street flow data 2025; S&P DJI 2026 | 1 |
| Cboe Global Markets 2026; SpotGamma 2026 | 1 |

**source_url** — Unique values: 12, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.morganstanley.com | 4 |
| https://intuitionlabs.ai | 2 |
| https://www.cboe.com | 2 |
| https://www.americancentury.com | 1 |
| https://agentmarketcap.ai | 1 |
| https://blakecrosley.com | 1 |
| https://www.epfr.com | 1 |
| https://www.spglobal.com | 1 |
| https://www.finra.org | 1 |
| https://www.bloomberg.com | 1 |
| https://www.spdji.com | 1 |
| https://www.factset.com | 1 |

**date_accessed** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-07-14 | 17 |

**confidence** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| High | 8 |
| Medium | 5 |
| Low | 4 |

**notes** — Unique values: 16, Nulls: 0

| Value | Count |
|-------|-------|
| Stock price -> easier funding -> more hiring/capex -> capacity -> revenue | 2 |
| Reverse reflexivity: stock drop -> harder funding -> capex cuts -> capacity -> revenue | 1 |
| AI stocks ~25% above DCF fair value (vs 100%+ in dot-com) | 1 |
| Meta 52%, AWS 57%, Microsoft 48%, Google 45% capex/revenue | 1 |
| CoreWeave: $2.60 capex per $1 new revenue (2026 guide) | 1 |
| Big 5: Amazon $125B, Microsoft $100B+, Google $100B+, Meta $100B, Oracle $20B | 1 |
| 40% of equity inflows to tech (vs 25% pre-2020) | 1 |
| Very low short interest despite high valuations (crowded long) | 1 |
| Call skew elevated: upside speculation > downside protection | 1 |
| Margin debt growing 25% YoY (vs 10% pre-AI boom) | 1 |
| Valuation correction typically lags fundamental inflection by 4-8 quarters | 1 |
| Theoretical: price changes fundamentals which changes price (1.4x loop) | 1 |
| 28% of S&P 500 in 7 tech stocks (vs 18% in 2019) | 1 |
| 60% of equity inflows passive -> forced buying of AI-heavy indices | 1 |
| Dealer gamma exposure creates momentum feedback at key strikes | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| value | 39.36 | 145.48 | 0.03 | 602.00 | 0.52 |

#### Sample Data (First 3 Rows)

| module | metric | value | unit | source | source_url | date_accessed | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Capital_Market_Reflexivity | valuation_to_funding_cost_elasticity | 0.35 | ratio | Morgan Stanley 2026; American Century 2026; SemiAn | https://www.morganstanley.com | 2026-07-14 | Medium | Stock price -> easier funding -> more hiring/capex |
| Capital_Market_Reflexivity | capex_to_revenue_sensitivity_hyperscalers | 0.35 | ratio | Morgan Stanley 2026; American Century 2026 | https://www.morganstanley.com | 2026-07-14 | Medium | Stock price -> easier funding -> more hiring/capex |
| Capital_Market_Reflexivity | downward_deleveraging_multiplier | 2.5 | ratio | Morgan Stanley 2026; American Century 2026 | https://www.morganstanley.com | 2026-07-14 | Low | Reverse reflexivity: stock drop -> harder funding  |

---

### `data_centers\module_25_revenue_quality.csv`

- **Size:** 0.01 MB (5,912 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 27
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 5 | module, unit, source_url, date_accessed, confidence |
| Numeric | 1 | value |
| Date | 0 | — |
| Text | 3 | metric, source, notes |

#### Category Column Details

**module** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| Revenue_Quality | 27 |

**unit** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| ratio | 21 |
| count | 3 |
| points | 3 |

**source_url** — Unique values: 12, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.keybanc.com | 9 |
| https://www.flexera.com | 4 |
| https://www.bvp.com | 3 |
| https://sacra.com | 3 |
| https://tenki.cloud | 1 |
| https://gpuaas.com | 1 |
| https://menlovc.com | 1 |
| https://aws.amazon.com | 1 |
| https://www.together.ai | 1 |
| https://www.equinix.com | 1 |
| https://www.sec.gov | 1 |
| https://dcmap.us | 1 |

**date_accessed** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-07-14 | 27 |

**confidence** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| High | 16 |
| Medium | 9 |
| Low | 2 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| value | 8.23 | 22.43 | 0.02 | 85.00 | 0.60 |

#### Sample Data (First 3 Rows)

| module | metric | value | unit | source | source_url | date_accessed | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue_Quality | high_quality_revenue_pct_hyperscalers | 0.65 | ratio | KeyBanc SaaS Survey 2025; ICONIQ 2025; Bessemer St | https://www.keybanc.com | 2026-07-14 | High | Mission-critical enterprise, long-term contracts,  |
| Revenue_Quality | medium_quality_revenue_pct_hyperscalers | 0.25 | ratio | KeyBanc SaaS Survey 2025; ICONIQ 2025 | https://www.keybanc.com | 2026-07-14 | Medium | API usage, productivity subscriptions, developer p |
| Revenue_Quality | low_quality_revenue_pct_hyperscalers | 0.1 | ratio | KeyBanc SaaS Survey 2025; ICONIQ 2025 | https://www.keybanc.com | 2026-07-14 | Medium | Promotional pricing, experimental, free-tier conve |

---

### `data_centers\module_26_national_strategic_investment.csv`

- **Size:** 0.01 MB (6,345 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 25
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 5 | module, unit, source_url, date_accessed, confidence |
| Numeric | 1 | value |
| Date | 0 | — |
| Text | 3 | metric, source, notes |

#### Category Column Details

**module** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| National_Strategic_Investment | 25 |

**unit** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| USD_B | 13 |
| ratio | 7 |
| EUR_B | 1 |
| count | 1 |
| SGD_M | 1 |
| GBP_B | 1 |
| boolean | 1 |

**source_url** — Unique values: 19, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.whitehouse.gov | 3 |
| https://ec.europa.eu | 2 |
| https://www.nextbigfuture.com | 2 |
| https://www.swfinstitute.org | 2 |
| https://www.bis.doc.gov | 2 |
| https://www.commerce.gov | 1 |
| https://www.chips.gov | 1 |
| https://www.semiconductors.org | 1 |
| https://www.sia-online.org | 1 |
| https://www.pif.gov.sa | 1 |
| https://www.smartnation.gov.sg | 1 |
| https://www.meity.gov.in | 1 |
| https://www.meti.go.jp | 1 |
| https://www.gov.uk | 1 |
| https://www.nap.edu | 1 |

**date_accessed** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-07-14 | 25 |

**confidence** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| High | 20 |
| Medium | 5 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| value | 4140.87 | 19972.63 | 0.05 | 100000.00 | 15.00 |

#### Sample Data (First 3 Rows)

| module | metric | value | unit | source | source_url | date_accessed | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| National_Strategic_Investment | us_chips_act_total_funding_billion_usd | 52.7 | USD_B | CHIPS and Science Act 2022; Commerce Dept 2025 imp | https://www.commerce.gov | 2026-07-14 | High | $52.7B total: $39B incentives, $11B R&D, $2.7B wor |
| National_Strategic_Investment | us_chips_act_disbursed_2025_billion_usd | 15.0 | USD_B | Commerce Dept CHIPS Program Office 2025; SIA 2025 | https://www.chips.gov | 2026-07-14 | High | $15B disbursed by end 2025 (28% of $52.7B) |
| National_Strategic_Investment | us_chips_act_private_investment_leveraged_billion_ | 450.0 | USD_B | SIA 2025 CHIPS Act Impact Report; S&P Global 2025 | https://www.semiconductors.org | 2026-07-14 | High | $53B public -> $450B private investment catalyzed  |

---

### `data_centers\module_27_labor_market_transformation.csv`

- **Size:** 0.01 MB (6,612 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 29
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 5 | module, unit, source_url, date_accessed, confidence |
| Numeric | 1 | value |
| Date | 0 | — |
| Text | 3 | metric, source, notes |

#### Category Column Details

**module** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| Labor_Market_Transformation | 29 |

**unit** — Unique values: 6, Nulls: 0

| Value | Count |
|-------|-------|
| ratio | 17 |
| millions | 6 |
| USD | 2 |
| USD_B | 2 |
| months | 1 |
| date | 1 |

**source_url** — Unique values: 15, Nulls: 0

| Value | Count |
|-------|-------|
| https://www.weforum.org | 4 |
| https://www.goldmansachs.com | 3 |
| https://www.mckinsey.com | 3 |
| https://www.anthropic.com | 3 |
| https://agentmarketcap.ai | 3 |
| https://www.imf.org | 2 |
| https://www.nber.org | 2 |
| https://hai.stanford.edu | 2 |
| https://mindstudio.ai | 1 |
| https://www.swfte.com | 1 |
| https://www.science.org | 1 |
| https://www.mindstudio.ai | 1 |
| https://www.federalreserve.gov | 1 |
| https://www.bls.gov | 1 |
| https://www.deloitte.com | 1 |

**date_accessed** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-07-14 | 29 |

**confidence** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| Medium | 14 |
| High | 12 |
| Low | 3 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| value | 776.09 | 2907.45 | 0.00 | 15000.00 | 0.55 |

#### Sample Data (First 3 Rows)

| module | metric | value | unit | source | source_url | date_accessed | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Labor_Market_Transformation | us_jobs_displaced_by_ai_2025_millions | 1.5 | millions | Goldman Sachs 2026; McKinsey 2025; IMF 2025 | https://www.goldmansachs.com | 2026-07-14 | Medium | ~1.5M US jobs displaced in 2025 (net of augmentati |
| Labor_Market_Transformation | us_jobs_augmented_by_ai_2025_millions | 12.0 | millions | McKinsey 2025; Goldman Sachs 2026 | https://www.mckinsey.com | 2026-07-14 | High | ~12M jobs augmented (8x displacement) |
| Labor_Market_Transformation | global_jobs_displaced_by_ai_2030_millions | 83.0 | millions | IMF 2025; WEF Future of Jobs 2025 | https://www.imf.org | 2026-07-14 | Medium | 83M displaced globally by 2030 (IMF baseline) |

---

### `data_centers\module_28_regulatory_scenario.csv`

- **Size:** 0.01 MB (6,272 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 28
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 4 | module, unit, date_accessed, confidence |
| Numeric | 0 | — |
| Date | 0 | — |
| Text | 5 | metric, value, source, source_url, notes |

#### Category Column Details

**module** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| Regulatory_Scenario | 28 |

**unit** — Unique values: 9, Nulls: 0

| Value | Count |
|-------|-------|
| date | 8 |
| USD_B | 8 |
| ratio | 4 |
| boolean | 2 |
| category | 2 |
| EUR_B | 1 |
| count | 1 |
| USD | 1 |
| USD_M | 1 |

**date_accessed** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-07-14 | 28 |

**confidence** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| High | 22 |
| Medium | 6 |

#### Sample Data (First 3 Rows)

| module | metric | value | unit | source | source_url | date_accessed | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Regulatory_Scenario | eu_ai_act_effective_date | 2025-08-01 | date | Official Journal EU 2024; EUR-Lex 32024R1689 | https://eur-lex.europa.eu | 2026-07-14 | High | EU AI Act entered force Aug 1 2024; phased complia |
| Regulatory_Scenario | eu_ai_act_high_risk_compliance_deadline | 2026-08-02 | date | EU AI Act Article 113; European Commission guidanc | https://ec.europa.eu | 2026-07-14 | High | High-risk AI systems: 24 months from entry into fo |
| Regulatory_Scenario | eu_ai_act_gpai_compliance_deadline | 2025-08-02 | date | EU AI Act Article 113; GPAI Code of Practice 2025 | https://ec.europa.eu | 2026-07-14 | High | General Purpose AI models: 12 months from entry in |

---

### `data_centers\module_29_ai_adoption_diffusion.csv`

- **Size:** 0.01 MB (11,005 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 52
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 5 | module, unit, source_url, date_accessed, confidence |
| Numeric | 1 | value |
| Date | 0 | — |
| Text | 3 | metric, source, notes |

#### Category Column Details

**module** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| AI_Adoption_Diffusion | 52 |

**unit** — Unique values: 5, Nulls: 0

| Value | Count |
|-------|-------|
| ratio | 43 |
| USD_B | 5 |
| date | 2 |
| USD_M | 1 |
| months | 1 |

**source_url** — Unique values: 10, Nulls: 0

| Value | Count |
|-------|-------|
| https://menlovc.com | 13 |
| https://www.mckinsey.com | 11 |
| https://www.swfte.com | 6 |
| https://www.writer.com | 6 |
| https://www.bassmodel.com | 4 |
| https://www.microsoft.com | 4 |
| https://www.gartner.com | 3 |
| https://aiindex.stanford.edu | 3 |
| https://www.idc.com | 1 |
| https://www.deloitte.com | 1 |

**date_accessed** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-07-14 | 52 |

**confidence** — Unique values: 3, Nulls: 0

| Value | Count |
|-------|-------|
| High | 45 |
| Medium | 6 |
| Low | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| value | 2.14 | 5.51 | 0.03 | 37.00 | 0.61 |

#### Sample Data (First 3 Rows)

| module | metric | value | unit | source | source_url | date_accessed | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI_Adoption_Diffusion | consumer_ai_users_global_billion | 1.75 | USD_B | Menlo Ventures Consumer AI 2025; Stanford AI Index | https://menlovc.com | 2026-07-14 | High | 1.7-1.8B global AI users (Menlo/Morning Consult 5, |
| AI_Adoption_Diffusion | us_adult_ai_usage_6month_pct | 0.61 | ratio | Menlo Ventures 2025 (5,031 US adults nationally re | https://menlovc.com | 2026-07-14 | High | 61% US adults used AI in past 6 months (Morning Co |
| AI_Adoption_Diffusion | enterprise_ai_adoption_pct | 0.88 | ratio | McKinsey State of AI 2025; Microsoft AI Diffusion  | https://www.mckinsey.com | 2026-07-14 | High | 88% orgs using AI in at least one function (1,993  |

---

### `data_centers\module_30_global_macro_feedback.csv`

- **Size:** 0.01 MB (8,206 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 39
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 4 | module, unit, date_accessed, confidence |
| Numeric | 1 | value |
| Date | 0 | — |
| Text | 4 | metric, source, source_url, notes |

#### Category Column Details

**module** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| Global_Macro_Feedback | 39 |

**unit** — Unique values: 8, Nulls: 0

| Value | Count |
|-------|-------|
| percent | 24 |
| USD_B | 5 |
| ratio | 3 |
| bps | 2 |
| USD | 2 |
| USD_T | 1 |
| TWh | 1 |
| GW | 1 |

**date_accessed** — Unique values: 1, Nulls: 0

| Value | Count |
|-------|-------|
| 2026-07-14 | 39 |

**confidence** — Unique values: 2, Nulls: 0

| Value | Count |
|-------|-------|
| High | 36 |
| Medium | 3 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| value | 96.56 | 186.14 | 0.40 | 630.50 | 3.80 |

#### Sample Data (First 3 Rows)

| module | metric | value | unit | source | source_url | date_accessed | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Global_Macro_Feedback | global_gdp_growth_2025_pct | 3.3 | percent | IMF WEO Oct 2025; World Bank Jan 2026 | https://www.imf.org | 2026-07-14 | High | IMF: 3.3% 2025 (revised up from 3.2%) |
| Global_Macro_Feedback | global_gdp_growth_2026_pct | 3.0 | percent | IMF WEO Update Jan 2026; IMF WEO Apr 2026 | https://www.imf.org | 2026-07-14 | High | IMF: 3.0% 2026 (stable from 2025); war/tech crossc |
| Global_Macro_Feedback | global_gdp_growth_2027_pct | 3.4 | percent | IMF WEO Update Jan 2026 | https://www.imf.org | 2026-07-14 | High | IMF: 3.4% 2027 recovery as energy shock fades |

---

### `data_centers\module_31_black_swan_stress_test.csv`

- **Size:** 0.01 MB (10,138 bytes)
- **Encoding:** utf-8
- **Delimiter:** `,`
- **Rows:** 49
- **Columns:** 9

#### Column Classification

| Type | Count | Columns |
|------|-------|---------|
| Category | 4 | module, unit, date_accessed, confidence |
| Numeric | 1 | value |
| Date | 0 | — |
| Text | 4 | metric, source, source_url, notes |

#### Category Column Details

**module** — Unique values: 7, Nulls: 0

| Value | Count |
|-------|-------|
| Black_Swan_Stress_Test | 25 |
| Stress_Test_Scenario | 13 |
| Scenario_Weights | 4 |
| Stress_Test_Combined | 4 |
| # Stress Test Scenarios (quantified) | 1 |
| # Combined scenario weights (must sum to 1.0) | 1 |
| # Combined stress test: simultaneous shocks | 1 |

**unit** — Unique values: 3, Nulls: 3

| Value | Count |
|-------|-------|
| ratio | 44 |
| months | 1 |
| USD_B | 1 |

**date_accessed** — Unique values: 4, Nulls: 3

| Value | Count |
|-------|-------|
| 2026-07-14 | 41 |
| Medium | 2 |
| Low | 2 |
| High | 1 |

**confidence** — Unique values: 5, Nulls: 7

| Value | Count |
|-------|-------|
| Medium | 15 |
| Low | 14 |
| High | 10 |
| Very_Low | 2 |
| Capex cut 70% (credit freeze + demand collapse + supply disruption) | 1 |

#### Numeric Column Statistics

| Column | Mean | Std | Min | Max | Median |
|--------|------|-----|-----|-----|--------|
| value | 1.56 | 7.37 | 0.01 | 50.00 | 0.20 |

#### Sample Data (First 3 Rows)

| module | metric | value | unit | source | source_url | date_accessed | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Black_Swan_Stress_Test | global_recession_probability_annual | 0.15 | ratio | IMF 2026; OECD 2026; Historical frequency 1960-202 | https://www.imf.org | 2026-07-14 | High | ~15% annual probability (1 in 7 years historically |
| Black_Swan_Stress_Test | global_recession_gdp_decline_pct | 0.035 | ratio | IMF 2026; Historical average 1960-2024 | https://www.imf.org | 2026-07-14 | High | Average recession: -3.5% global GDP peak-to-trough |
| Black_Swan_Stress_Test | energy_crisis_probability_annual | 0.05 | ratio | IEA 2026; Historical 1973, 1979, 1990, 2000, 2022 | https://www.iea.org | 2026-07-14 | Medium | ~5% annual probability (5 major crises in 50 years |

---

## Non-CSV File Analysis

### `analyze_contracts.py`

- **Extension:** .py
- **Size:** 11.3 KB (11,569 bytes)
- **MIME Type:** text/x-python
- **Encoding:** utf-8
- **Lines:** 279
- **Characters:** 11,569
- **Words:** 1,126
- **MD5:** `c32fb7adfc73bfbaf89469243ee66b47`
- **SHA256:** `96ce3acf9d9d307b34ab86ad1c50fdb384478d6d9410548931fea1f8cfdd2437`

#### Code Structure Analysis

- **Imports (3):** import json, import numpy as np, import pandas as pd
- **Functions (1):** run_simulation_python
- **Constants (1):** DEFAULT_PARAMS
- **Complexity:** 279 lines, 3 imports, 0 classes, 1 functions

#### Extracted Data Patterns

- **File Paths (18):** / constructionDelayMultiplier, / tokenPrice, / lenShort, / lenLong, /cancellation when netSavings is negative, / 0.12, / initialValuation, // 4, \n--- MAXIMUM DOWNSIZING HIT PERIOD ---, / investedCapital...

#### Content Summary

- **Total Lines:** 279
- **Non-Empty Lines:** 228
- **Empty Line Ratio:** 18.28%
- **Avg Line Length:** 40.5 chars
- **Max Line Length:** 130 chars

---

### `analyze_data_files.py`

- **Extension:** .py
- **Size:** 40.49 KB (41,461 bytes)
- **MIME Type:** text/x-python
- **Encoding:** utf-8
- **Lines:** 944
- **Characters:** 41,449
- **Words:** 2,884
- **MD5:** `4e4bef93092351bf4112b8ed13f195eb`
- **SHA256:** `0f502a81d7527848e2e553e1f1d4f4fa19f0a6f2f7750971febab1fafee1269a`

#### Code Structure Analysis

- **Imports (14):** import os, import csv, import json, import re, import hashlib, import mimetypes, from pathlib import Path, from datetime import datetime, from collections import defaultdict, Counter, from typing import Dict, List, Set, Any, Optional...
- **Classes (1):** DataFileAnalyzer
- **Functions (32):** __init__, find_all_files, analyze_csv_files, _analyze_single_csv, _detect_encoding, _detect_delimiter, _analyze_with_pandas, _analyze_with_csv_module, _classify_column, _classify_column_values...
- **Constants (4):** PANDAS_AVAILABLE, PANDAS_AVAILABLE, MAGIC_AVAILABLE, MAGIC_AVAILABLE
- **Complexity:** 944 lines, 14 imports, 1 classes, 32 functions

#### Extracted Data Patterns

- **File Paths (20):** \s, \n, / total_count if total_count , \bv, \., \b\d, \\, / len, /A, /\\...

#### Content Summary

- **Total Lines:** 944
- **Non-Empty Lines:** 831
- **Empty Line Ratio:** 11.97%
- **Avg Line Length:** 42.9 chars
- **Max Line Length:** 201 chars

---

### `app.js`

- **Extension:** .js
- **Size:** 25.91 KB (26,530 bytes)
- **MIME Type:** application/javascript
- **Encoding:** utf-8
- **Lines:** 629
- **Characters:** 26,517
- **Words:** 2,623
- **MD5:** `4c8230ab03e959c26524a6334e147453`
- **SHA256:** `02eae42bff5c3aceb80a19a6f4324dcabff46e8a417ad92399d961a602220c3f`

#### Code Structure Analysis

- **Functions (9):** pppAdjustmentLabel, initControls, updateScenarioMatrix, applyPresetScenario, updateStatsCards, setupFormulaExplorer, renderFormulaDetail, renderCharts, updateDashboard
- **Async Functions:** 4
- **Constants (56):** engine, res, res, res, res, sliders, tabButtons, matrixContainer, explorerList, explorerDetail

#### Extracted Data Patterns

- **File Paths (20):** /td, / TokenPrice, / 100, // Update the UI panel with metrics, // Initial load, /div, /h3, /th, /tbody, // Update UI Dropdowns...
- **Hex Colors (7):** #a0aec0, #ff3366, #4facfe, #00e676, #ffb300, #00f2fe, #f5f6fa

#### Content Summary

- **Total Lines:** 629
- **Non-Empty Lines:** 575
- **Empty Line Ratio:** 8.59%
- **Avg Line Length:** 41.2 chars
- **Max Line Length:** 305 chars

---

### `AUDIT_MODEL.py`

- **Extension:** .py
- **Size:** 7.02 KB (7,186 bytes)
- **MIME Type:** text/x-python
- **Encoding:** utf-8
- **Lines:** 173
- **Characters:** 7,186
- **Words:** 946
- **MD5:** `e7878b3618e31661d892ff3d49da7c4b`
- **SHA256:** `1bd3cba979fcb9c1f9b730c9c3ebbec91a412571d88b08eccdc512cc9847f9bd`

#### Code Structure Analysis

- **Imports (1):** import json
- **Complexity:** 173 lines, 1 imports, 0 classes, 0 functions

#### Extracted Data Patterns

- **File Paths (20):** \n, /hour, / total_mw , / 0.7 , \n3. ROIC CHECK, /PFLOPS assumption, /B , /A, /Revenue multiple, \n6. FACILITY STATUS IGNORED...

#### Content Summary

- **Total Lines:** 173
- **Non-Empty Lines:** 155
- **Empty Line Ratio:** 10.40%
- **Avg Line Length:** 40.5 chars
- **Max Line Length:** 111 chars

---

### `calibrate.py`

- **Extension:** .py
- **Size:** 45.59 KB (46,687 bytes)
- **MIME Type:** text/x-python
- **Encoding:** utf-8
- **Lines:** 1,015
- **Characters:** 46,661
- **Words:** 3,902
- **MD5:** `87119953648b4dbb7f28378cdc810a50`
- **SHA256:** `9d8b750b63dda715b8421c3bc52db791d5f82743723031f20e47612b47e76249`

#### Code Structure Analysis

- **Imports (4):** import os, import json, import pandas as pd, import numpy as np
- **Constants (26):** DATA_DIR, USITC_PATH, LBNL_PATH, SEC_QUARTERS, HYPERSCALER_NAMES, CAPEX_TAGS, RPO_TAGS, REVENUE_TAGS, TECH_PARAMS_PATH, FUEL_PRICES_PATH
- **Complexity:** 1015 lines, 4 imports, 0 classes, 0 functions

#### Extracted Data Patterns

- **File Paths (20):** / gpt4o_input, \n, / 100, / TTF / JKM Correlations ---, / 100 if not ri_data.empty else 1.05, / 1000, \n   Quarters successfully processed, /kWh, / overall_rpo_sum, / total_spend...

#### Content Summary

- **Total Lines:** 1,015
- **Non-Empty Lines:** 890
- **Empty Line Ratio:** 12.32%
- **Avg Line Length:** 45.0 chars
- **Max Line Length:** 187 chars

---

### `chart.js`

- **Extension:** .js
- **Size:** 203.63 KB (208,522 bytes)
- **MIME Type:** application/javascript
- **Encoding:** utf-8
- **Lines:** 15
- **Characters:** 208,522
- **Words:** 3,045
- **MD5:** `e6452e2b454b091f857a45cce7624eae`
- **SHA256:** `48444a82d4edcb5bec0f1965faacdde18d9c17db3063d042abada2f705c9f54a`

#### Code Structure Analysis

- **Classes (39):** xt, Jt, de, hs, cs, Ss, As, Ts, js, tn...
- **Functions (279):** e, s, n, o, a, r, l, d, u, f...
- **Constants (819):** i, e, h, e, n, s, r, n, s, y

#### Extracted Data Patterns

- **Urls (2):** https://www.chartjs.org, https://github.com/kurkle/color#readme
- **Version Numbers (3):** v0.3.2, 4.5.1, v4.5.1
- **File Paths (20):** /o.w, /this._valueRange, /g, /S, /Math.min, /o, /l.weight, /l, /3, /e.count...
- **Hex Colors (2):** #fff, #666

#### Content Summary

- **Total Lines:** 15
- **Non-Empty Lines:** 14
- **Empty Line Ratio:** 6.67%
- **Avg Line Length:** 13900.5 chars
- **Max Line Length:** 199933 chars

---

### `check_data.py`

- **Extension:** .py
- **Size:** 0.51 KB (520 bytes)
- **MIME Type:** text/x-python
- **Encoding:** utf-8
- **Lines:** 10
- **Characters:** 520
- **Words:** 32
- **MD5:** `a06426a2008ee86494a1ebc5dac186cc`
- **SHA256:** `9dcac7760f9771fa30b4501b3924251f61330985a6a47b5041822909067bbc92`

#### Code Structure Analysis

- **Imports (1):** import json
- **Complexity:** 10 lines, 1 imports, 0 classes, 0 functions

#### Extracted Data Patterns

- **File Paths (1):** C:/Users/NITHING/Desktop/projections/data_centers/master_facility_list_v3_enriched.json

#### Content Summary

- **Total Lines:** 10
- **Non-Empty Lines:** 10
- **Empty Line Ratio:** 0.00%
- **Avg Line Length:** 51.1 chars
- **Max Line Length:** 111 chars

---

### `check_data2.py`

- **Extension:** .py
- **Size:** 0.49 KB (504 bytes)
- **MIME Type:** text/x-python
- **Encoding:** utf-8
- **Lines:** 16
- **Characters:** 504
- **Words:** 56
- **MD5:** `a711891656f75a6a7d5daeb2a1d3dbf1`
- **SHA256:** `63d178f47d393b32398a325b1cdfb3573e5d57f5e68ec68c3cb1cb3cef3f0a61`

#### Code Structure Analysis

- **Imports (1):** import json
- **Complexity:** 16 lines, 1 imports, 0 classes, 0 functions

#### Extracted Data Patterns

- **File Paths (2):** \n\nSample values for Meta Hyperion, C:/Users/NITHING/Desktop/projections/data_centers/master_facility_list_v3_enriched.json

#### Content Summary

- **Total Lines:** 16
- **Non-Empty Lines:** 14
- **Empty Line Ratio:** 12.50%
- **Avg Line Length:** 30.6 chars
- **Max Line Length:** 111 chars

---

### `COMPILED_PROJECT.md`

- **Extension:** .md
- **Size:** 101.03 KB (103,458 bytes)
- **MIME Type:** unknown
- **Encoding:** utf-8
- **Lines:** 2,866
- **Characters:** 100,570
- **Words:** 10,004
- **MD5:** `1b9c4b6a2c0ad99199410cb78d1313e7`
- **SHA256:** `0d623074299301098024f0112a967cf6d40f9d0d76aa7049f1c9bfbf0d791e32`

#### Markdown Structure

- **Headers:** 43 (H1: 33, H2: 10, H3: 0)
- **Links:** 10
- **Images:** 0
- **Code Blocks:** 9
- **Tables:** 43
- **Lists:** 17
- **Word Count:** 10,004

**Table of Contents:**
- Complete Project Compilation: TESM Dashboard
  - Table of Contents
  - analyze_contracts.py
- Load the reconciled parameters (v3.0)
- Baseline default parameters
- Merge calibrated parameters
- Run model
- Convert to DataFrame
- Find period of maximum contract expiration
- Find period of maximum downsizing reduction hit
- Calculate summary stats
  - calibrate.py
- Define paths matching your local directory
- All 13 quarters from 2023q1 through 2026q1
- Hyperscaler target names
- GAAP tags
- --- 1. PARSE LBNL GRID QUEUE DATA (~15.2 MB) ---
- --- 2. PARSE USITC SEMICONDUCTOR TRADE CHANNELS (162 KB) ---
- --- 3. PARSE ALL 13 SEC DERA QUARTERS (2023q1 -> 2026q1) ---
- Build time-series DataFrame

#### Extracted Data Patterns

- **Urls (2):** https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');, http://localhost:$
- **Dates Iso (2):** 2026-07-09, 2026-07-10
- **File Paths (20):** /td, // Update the UI panel with metrics, /jpeg, /css, /div, \n--- STEP 4, \n2026 EXPIRATIONS, /KSA, // E, // Select active data set based on the user...
- **Hex Colors (12):** #a0aec0, #ff3366, #4facfe, #00e676, #ffb300, #718096, #00f2fe, #1a2333, #9c27b0, #f5f6fa...

#### Content Summary

- **Total Lines:** 2,866
- **Non-Empty Lines:** 2,448
- **Empty Line Ratio:** 14.58%
- **Avg Line Length:** 34.1 chars
- **Max Line Length:** 305 chars

---

### `context.md`

- **Extension:** .md
- **Size:** 68.58 KB (70,230 bytes)
- **MIME Type:** unknown
- **Encoding:** utf-8
- **Lines:** 2,097
- **Characters:** 69,922
- **Words:** 9,852
- **MD5:** `005722a2d2f6a2f4555fb3a951e54e94`
- **SHA256:** `e18bf1fabc3ce193fe9207438b95a3afa05b9d14cea409e9952191155c6edc1e`

#### Markdown Structure

- **Headers:** 109 (H1: 26, H2: 45, H3: 34)
- **Links:** 0
- **Images:** 0
- **Code Blocks:** 13
- **Tables:** 685
- **Lists:** 423
- **Word Count:** 9,852

**Table of Contents:**
- Comprehensive Financial Modeling: Dot-com Bubble vs. Today's AI Economy
  - 1. Historical Comparison
  - 2. Company Universe
    - AI Model Providers
    - Semiconductor Companies
    - Cloud Infrastructure Providers
    - AI Infrastructure Companies
    - Enterprise AI Companies
  - 3. IPO Quality Analysis
  - 4. AI Adoption Model
  - 5. Capital Expenditure (CapEx) Model
  - 6. AI Efficiency Model
  - 7. Productivity Gains
  - 8. Chinese AI Competition
  - 9. Purchasing Power Parity (PPP)
  - 10. Demand Shock Scenario
  - 11. Enterprise AI Agent Deployment
  - 12. Workflow Integration
  - 13. Financial Modeling
  - 14. Detailed Calculations

#### Extracted Data Patterns

- **Urls (1):** https://www.sec.gov/files/dera/data/financial-statement-data-sets/
- **Dates Iso (3):** 2024-10-15, 2025-08-02, 2024-11-15
- **File Paths (20):** /miss, /blue, /colocation provider, /E, / FactSet , /dark, /yr subscription , /kWh , /power price correlation with AI demand , /kWh...

#### Content Summary

- **Total Lines:** 2,097
- **Non-Empty Lines:** 1,515
- **Empty Line Ratio:** 27.75%
- **Avg Line Length:** 32.3 chars
- **Max Line Length:** 397 chars

---

### `contract_loss_2026_2027.py`

- **Extension:** .py
- **Size:** 7.33 KB (7,504 bytes)
- **MIME Type:** text/x-python
- **Encoding:** utf-8
- **Lines:** 144
- **Characters:** 7,504
- **Words:** 821
- **MD5:** `607c4c2bd7a55b6673126a9cd0f960e4`
- **SHA256:** `d59ddd1a2aabc43e18ff8223b8f4dae46cefdb3a794642122cd74226dbfd8ca6`

#### Code Structure Analysis

- **Imports (3):** import numpy as np, import pandas as pd, import json
- **Constants (5):** DOWNSIZING_RATIO, CONTRACT_MIX_3YR, CONTRACT_MIX_5YR, NORMAL_CHURN, WACC
- **Complexity:** 144 lines, 3 imports, 0 classes, 0 functions

#### Extracted Data Patterns

- **File Paths (10):** \n2026 EXPIRATIONS, \n, \n--- STEP 3, / rev_per_year, \n--- STEP 1, \n2027 EXPIRATIONS, \n--- STEP 4, / , \n--- STEP 2, \n--- STEP 5

#### Content Summary

- **Total Lines:** 144
- **Non-Empty Lines:** 116
- **Empty Line Ratio:** 19.44%
- **Avg Line Length:** 51.1 chars
- **Max Line Length:** 153 chars

---

### `DATA_ANALYSIS_REPORT.md`

- **Extension:** .md
- **Size:** 13.28 KB (13,601 bytes)
- **MIME Type:** unknown
- **Encoding:** utf-8
- **Lines:** 255
- **Characters:** 13,354
- **Words:** 1,960
- **MD5:** `9064a41b2bbe610dcd7b8f8f51df66de`
- **SHA256:** `adb3919e6b2e70aca8df465074c37e3f76a0f1ff354a174d69517958a081e7f3`

#### Markdown Structure

- **Headers:** 19 (H1: 1, H2: 8, H3: 10)
- **Links:** 0
- **Images:** 0
- **Code Blocks:** 2
- **Tables:** 160
- **Lists:** 37
- **Word Count:** 1,960

**Table of Contents:**
- DATA Folder Analysis Report
  - 1. DATA Folder Structure Overview
  - 2. Quarterly SEC DERA Data (13 Quarters: 2023q1 – 2026q1)
    - 2.1 Sample Analysis: 2023q1
    - 2.2 Hyperscaler Coverage Check
  - 3. USITC Semiconductor Trade Data (`DataWeb-Query-Export.xlsx`)
  - 4. LBNL Interconnection Queue Data (`LBNL_Ix_Queue_Data_File_thru2025.xlsx`)
    - 4.1 Key Fields in Complete Queue Data (Sheet 03)
    - 4.2 Calibration Parameters Extracted (per `calibrate.py`)
  - 5. CONTEXT.md Requirements vs. Data Availability
    - ✅ **Fully Supported by Available Data**
    - ⚠️ **Partially Supported (Data Exists but Requires Enrichment)**
    - ❌ **Not Supported (No Data Source Available)**
  - 6. Data Quality Notes
    - SEC DERA (13 Quarters)
    - LBNL Queue (through 2025)
    - USITC Trade (2023-2026)
  - 7. Recommendations
  - 8. Conclusion

#### Extracted Data Patterns

- **Dates Iso (1):** 2026-07-10
- **File Paths (20):** /IS/CF, /grid/SEC data , /Unit Economics, /LBNL/USITC , /13 quarters processed, /RTOs, /RTO/Utility mapping, /year , /quantization adoption , /RTO/Utility ...

#### Content Summary

- **Total Lines:** 255
- **Non-Empty Lines:** 196
- **Empty Line Ratio:** 23.14%
- **Avg Line Length:** 51.4 chars
- **Max Line Length:** 389 chars

---

### `DATA_COLLECTED_BUT_UNUSED.md`

- **Extension:** .md
- **Size:** 14.78 KB (15,133 bytes)
- **MIME Type:** unknown
- **Encoding:** utf-8
- **Lines:** 149
- **Characters:** 15,004
- **Words:** 1,886
- **MD5:** `305a58ee6f7a927b93ddac880fae6915`
- **SHA256:** `908c7dcf2e662017850f7ccfbd6498bbf12fe27e4cd53bd9cc3968eaf567553a`

#### Markdown Structure

- **Headers:** 12 (H1: 1, H2: 8, H3: 3)
- **Links:** 0
- **Images:** 0
- **Code Blocks:** 1
- **Tables:** 137
- **Lists:** 0
- **Word Count:** 1,886

**Table of Contents:**
- Data Collected But Not Used in TESM Model
  - Executive Summary
  - 1. Data Files Fully Loaded But Parameters Never Used in Engine
  - 2. Data Partially Used (Rich Structure Reduced to Single Scalar)
  - 3. Data Structures Passed to Browser But Never Accessed
  - 4. Module-Specific Data Gaps (Per context.md Requirements)
  - 5. Quantified Data Waste
  - 6. Recommended Integration Points
    - High Impact / Low Effort
    - Medium Effort
    - High Effort (Requires New Data)
  - 7. Files to Investigate for Missing Data

#### Extracted Data Patterns

- **Dates Iso (1):** 2026-07-15
- **File Paths (20):** /expansion rates but no agent-specific data , // 16 records , / Low Effort, // 18 records , C:\Users\NITHING\Desktop\projections\, /calibration_parameters.csv, /compliance cost breakdown , /meta_analysis_studies.csv, /MW-yr, /GRR/expansion/downsizing by contract_type to parameterize ...

#### Content Summary

- **Total Lines:** 149
- **Non-Empty Lines:** 119
- **Empty Line Ratio:** 20.13%
- **Avg Line Length:** 99.7 chars
- **Max Line Length:** 487 chars

---

### `DATA_FILE_ANALYSIS_REPORT.md`

- **Extension:** .md
- **Size:** 0.0 KB (0 bytes)
- **MIME Type:** unknown
- **Encoding:** utf-8
- **Lines:** 1
- **Characters:** 0
- **Words:** 0
- **MD5:** `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256:** `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

#### Markdown Structure

- **Headers:** 0 (H1: 0, H2: 0, H3: 0)
- **Links:** 0
- **Images:** 0
- **Code Blocks:** 0
- **Tables:** 0
- **Lists:** 0
- **Word Count:** 0

#### Extracted Data Patterns


#### Content Summary

- **Total Lines:** 1
- **Non-Empty Lines:** 0
- **Empty Line Ratio:** 100.00%
- **Avg Line Length:** 0.0 chars
- **Max Line Length:** 0 chars

---

### `DATA_GAP_REPORT.md`

- **Extension:** .md
- **Size:** 12.85 KB (13,161 bytes)
- **MIME Type:** unknown
- **Encoding:** utf-8
- **Lines:** 174
- **Characters:** 12,669
- **Words:** 1,828
- **MD5:** `27dd3b35895254530ef72762dbd3b3c7`
- **SHA256:** `d9e57dcba9409985ca829688d4d8143532f94e65f16abaef0707a6d2a5cee607`

#### Markdown Structure

- **Headers:** 11 (H1: 1, H2: 7, H3: 3)
- **Links:** 0
- **Images:** 0
- **Code Blocks:** 1
- **Tables:** 182
- **Lists:** 0
- **Word Count:** 1,828

**Table of Contents:**
- TESM Data Gap Analysis: What's Still Missing
  - Executive Summary
  - Module-by-Module Gap Matrix
    - ✅ **Well-Anchored (Empirical time-series + cross-section)**
    - ⚠️ **Partially Anchored (1-2 data points, needs depth)**
    - ❌ **No Empirical Anchor (Pure Placeholder)**
  - 7 Critical Gaps Blocking Publication-Grade
  - Data Acquisition Priority Queue
  - Quick-Start: What You Can Add *This Week* (No Budget)
  - Appendix: Current DATA/ Inventory
  - Next Steps

#### Extracted Data Patterns

- **Dates Iso (1):** 2026-07-10
- **File Paths (20):** /stress_scenarios/expert_priors.csv, /unit_economics/inference_benchmarks.csv, /adoption/token_volume_proxy.csv, /IDC access, /IRA/EU Chips Act/China 14th Plan appropriation tracking, /revisions feedback , /allocation data , /legal exposure quantification , /Restrepo replication , /Med/Low tiers ...

#### Content Summary

- **Total Lines:** 174
- **Non-Empty Lines:** 142
- **Empty Line Ratio:** 18.39%
- **Avg Line Length:** 71.8 chars
- **Max Line Length:** 226 chars

---

### `DATA_PRESENCE_AUDIT.md`

- **Extension:** .md
- **Size:** 58.14 KB (59,535 bytes)
- **MIME Type:** unknown
- **Encoding:** utf-8
- **Lines:** 962
- **Characters:** 58,604
- **Words:** 7,671
- **MD5:** `9df1695de9e9ec7f322a67e4fe7929ac`
- **SHA256:** `3f5fcd92ba20f5cab6aac3343231c5e34bfe46a0540d8f86544aad06173725d8`

#### Markdown Structure

- **Headers:** 46 (H1: 1, H2: 4, H3: 41)
- **Links:** 0
- **Images:** 0
- **Code Blocks:** 1
- **Tables:** 775
- **Lists:** 9
- **Word Count:** 7,671

**Table of Contents:**
- Data Presence Audit: Maximum Data Requirements vs. Available Data Collection
  - Executive Summary
  - Detailed Section-by-Section Audit
    - 1. Entity Master Data (§1 Appendix)
    - 2. Company Universe Data (§2)
    - 3. Historical Dot-com Comparison Data (§3)
    - 4. Valuation Data (§4)
    - 5. Financial Statement Data (§5)
    - 6. Revenue Quality Data (§6)
    - 7. IPO Quality Data (§7)
    - 8. AI Adoption Data (§8)
    - 9. Token Usage and AI Workload Data (§9)
    - 10. AI Pricing Data (§10)
    - 11. AI Efficiency Data (§11)
    - 12. Jevons Paradox and Demand Elasticity Data (§12)
    - 13. Training Demand Data (§13)
    - 14. Inference Demand Data (§14)
    - 15. CapEx Data (§15)
    - 16. Data Center Infrastructure Data (§16)
    - 17. Physical Infrastructure Constraint Data (§17)

#### Extracted Data Patterns

- **Dates Iso (1):** 2026-07-15
- **File Paths (20):** /EO 14110, /telecom fiber/cloud/smartphone/DRAM/NAND cycles, /availability targets. Only growth multipliers., /subscription/cloud pricing , /ai_efficiency.csv, /E, /reserved/secondary GPU prices, /sector_rotation.csv, /reskilling/management/compliance cost, /unit compute...

#### Content Summary

- **Total Lines:** 962
- **Non-Empty Lines:** 711
- **Empty Line Ratio:** 26.09%
- **Avg Line Length:** 59.9 chars
- **Max Line Length:** 899 chars

---

### `DATA_SOURCES_AND_LINEAGE.md`

- **Extension:** .md
- **Size:** 49.61 KB (50,799 bytes)
- **MIME Type:** unknown
- **Encoding:** utf-8
- **Lines:** 804
- **Characters:** 50,531
- **Words:** 7,063
- **MD5:** `c9b48396dd576a5f921a486c08d6ada7`
- **SHA256:** `ccd3347487049b986f6811d9187f7a36e42d6263df3b94214831b8c907459980`

#### Markdown Structure

- **Headers:** 62 (H1: 1, H2: 18, H3: 43)
- **Links:** 13
- **Images:** 0
- **Code Blocks:** 0
- **Tables:** 1035
- **Lists:** 47
- **Word Count:** 7,063

**Table of Contents:**
- Comprehensive Data Sources & Lineage Registry
  - Table of Contents
  - 1. Core Financial & Market Data Sources
    - 1.1 SEC EDGAR / DERA Financial Statements
    - 1.2 Equity Market Data (CRSP / Refinitiv / Bloomberg)
    - 1.3 Private Market Data (AI Pure-Plays)
    - 1.4 IPO Prospectus Database (S-1 / F-1 Filings)
  - 2. Data Center Infrastructure Data
    - 2.1 Master Global Data Centers Dataset (Compiled)
    - 2.2 Enriched Hyperscale Facility Dataset (Phase 1-4)
  - 3. Grid & Power Infrastructure Data
    - 3.1 LBNL Interconnection Queue Database
    - 3.2 ISO/RTO Queue Data (Direct)
    - 3.3 FERC Form 715 (Transmission Planning)
    - 3.4 EIA Forms (Generation & Capacity)
    - 3.5 NREL Models
  - 4. Semiconductor Supply Chain Data
    - 4.1 Public Filings & Earnings
    - 4.2 Subscription Research (Required for Production)
    - 4.3 USITC Trade Data (Semiconductor Imports)

#### Extracted Data Patterns

- **Urls (20):** https://platform.moonshot.cn/, https://dcbyte.com/, https://www.misoenergy.org/planning/generator-interconnection/, https://www.eia.gov/electricity/data/eia860/, https://investor.nvidia.com/, https://cloud.tencent.com/, https://www.bis.org/statistics/, https://www.iso-ne.com/ws/document, https://www.ercot.com/gridinfo/resource, https://www.volcengine.com/...
- **Dates Iso (1):** 2026-07-15
- **File Paths (20):** s://elibrary.ferc.gov/ , s://dataweb.usitc.gov/  , /blue, / DRAMeXchange, /facility DCF , s://www.gridpath.io/ , / SEC 13F filings , /kWh , /module_3_ipo_quality.csv, s://www.ercot.com/gridinfo/resource ...

#### Content Summary

- **Total Lines:** 804
- **Non-Empty Lines:** 645
- **Empty Line Ratio:** 19.78%
- **Avg Line Length:** 61.9 chars
- **Max Line Length:** 468 chars

---

### `DEEP_RESEARCH_PLAN.md`

- **Extension:** .md
- **Size:** 11.31 KB (11,581 bytes)
- **MIME Type:** unknown
- **Encoding:** utf-8
- **Lines:** 293
- **Characters:** 11,561
- **Words:** 1,601
- **MD5:** `1aac150035a9b669a8324ab7d36cdbda`
- **SHA256:** `f1b8b5218f6d8a1263ae923f2d421c21c13674676809117840b74ea15f127c1b`

#### Markdown Structure

- **Headers:** 46 (H1: 1, H2: 12, H3: 33)
- **Links:** 0
- **Images:** 0
- **Code Blocks:** 0
- **Tables:** 10
- **Lists:** 85
- **Word Count:** 1,601

**Table of Contents:**
- Deep Research Plan: New Data Sources for TESM Model Enhancement
  - Phase 1: AI Adoption & Usage Telemetry (Priority: P0)
    - Target Data
    - Research Queries
    - Expected Outputs
  - Phase 2: Chinese AI Ecosystem Data (Priority: P0)
    - Target Data
    - Research Queries
    - Expected Outputs
  - Phase 3: Productivity Studies Meta-Analysis (Priority: P0)
    - Target Data
    - Research Queries
    - Expected Outputs
  - Phase 4: Cloud Revenue Quality & Contract Mapping (Priority: P0)
    - Target Data
    - Research Queries
    - Expected Outputs
  - Phase 5: Macro & Financial Market Data (Priority: P1)
    - Target Data
    - Research Queries

#### Extracted Data Patterns

- **File Paths (20):** /china/model_benchmarks.csv, /TCO case studies from vendors and enterprises, /labor/displaced_worker_outcomes.csv, /macro/fred_core_series.parquet, /labor/reskilling_outcomes.csv, /macro/etf_flows.csv, /regulatory/export_controls.csv, /revenue_quality/contract_taxonomy.csv, /advanced packaging capacity, /investor days...

#### Content Summary

- **Total Lines:** 293
- **Non-Empty Lines:** 234
- **Empty Line Ratio:** 20.14%
- **Avg Line Length:** 38.5 chars
- **Max Line Length:** 159 chars

---

### `FINAL_REPORT.md`

- **Extension:** .md
- **Size:** 6.82 KB (6,979 bytes)
- **MIME Type:** unknown
- **Encoding:** utf-8
- **Lines:** 101
- **Characters:** 6,979
- **Words:** 945
- **MD5:** `b34913e74e2f05b1242146d55cae5f29`
- **SHA256:** `0ae3f16d8f3073c632f26238597d36784aff668be9ee1b36fe01b96490548626`

#### Markdown Structure

- **Headers:** 15 (H1: 1, H2: 1, H3: 5)
- **Links:** 0
- **Images:** 0
- **Code Blocks:** 2
- **Tables:** 20
- **Lists:** 25
- **Word Count:** 945

**Table of Contents:**
- Techno-Economic Systems Model (TESM)
  - Phase 6: Final Report & Investment Recommendations
    - 1. Executive Summary
      - 1.1 Empirical Scope
      - 1.2 Key Quantitative Findings
    - 2. Investment Thesis by Sector
      - 2.1 Hyperscaler Cloud Providers (Meta, Microsoft, Google, AWS, Oracle)
      - 2.2 Specialized Colocation Providers (Equinix, Digital Realty, QTS, Vantage)
      - 2.3 Pure-Play GPU Cloud and Capacity Developers (Bitzero, Nscale, Fermi America)
      - 2.4 Repurposed Crypto Miners (IREN, Hut 8, Core Scientific)
    - 3. Risk Mitigation Strategies
      - 3.1 Onsite Generation Defection
      - 3.2 Overcapacity and Price Compression Hedging
    - 4. Leading Indicator Dashboard Design
    - 5. Quarterly Refresh Methodology

#### Extracted Data Patterns

- **File Paths (16):** /hr H100 rental equivalents, /1K tokens blended pricing, / Hour , / Revenue Ratio , /Ohio queue delays, /MWh, /Fiber overbuild, /E multiples , /MWh., / 5.00 ...

#### Content Summary

- **Total Lines:** 101
- **Non-Empty Lines:** 75
- **Empty Line Ratio:** 25.74%
- **Avg Line Length:** 68.1 chars
- **Max Line Length:** 355 chars

---

### `financial_modeling.py`

- **Extension:** .py
- **Size:** 27.76 KB (28,431 bytes)
- **MIME Type:** text/x-python
- **Encoding:** utf-8
- **Lines:** 768
- **Characters:** 28,431
- **Words:** 2,583
- **MD5:** `e4d444d89dda434b4cc5cbf0bb575e86`
- **SHA256:** `84b7524e25274d85f7f52ca7326f9b65aaedf0017a710f66ad130ae944974420`

#### Code Structure Analysis

- **Imports (9):** import json, import csv, import numpy as np, import pandas as pd, from datetime import datetime, timedelta, from collections import defaultdict, from dataclasses import dataclass, field, from typing import Dict, List, Optional, Tuple, import warnings
- **Classes (3):** FacilityFinancials, HyperscalerFinancials, ScenarioEngine
- **Functions (16):** load_facility_data, load_global_datacenters, annual_ebitda, roic, payback_years, total_capex, total_capacity_mw, total_gpus, weighted_avg_roic, aggregate_payback...
- **Constants (3):** DOTCOM_BENCHMARKS, AI_CURRENT_METRICS, SCENARIOS
- **Complexity:** 768 lines, 9 imports, 3 classes, 16 functions

#### Extracted Data Patterns

- **File Paths (20):** \n, / Current Demand, \nWeighted Score, /E, /1e12, /CoWoS/power constraints limit overbuild speed, /cancelled , / sum, / ebitda if ebitda , /S...

#### Content Summary

- **Total Lines:** 768
- **Non-Empty Lines:** 656
- **Empty Line Ratio:** 14.58%
- **Avg Line Length:** 36.0 chars
- **Max Line Length:** 265 chars

---
