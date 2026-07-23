# Global Data Centers Master Dataset - Summary

**Generated:** 2026-07-14  
**Total Records:** 19,694 unique facilities  
**File:** `master_global_datacenters.csv` (3.07 MB)

---

## Data Sources Combined

| Source | Records | Description |
|--------|---------|-------------|
| **GitHub Global-Data-Center-Map** | 18,089 | 18,110 facilities across 116 countries, 4,181 operators (ATLAS dataset) |
| **FracTracker US Tracker** | 1,579 | US facilities with detailed pipeline status (Operating, Planned, Under Construction, Cancelled, Suspended, Expanding) |
| **DCMap.us Pipeline** | 11 | Major US hyperscale pipeline projects (250,993 MW total pipeline) |
| **DataCenterMap.info** | 15 | Country-level aggregate statistics (11,873 facilities across 179 countries) |

---

## Status Breakdown

| Status | Count | Description |
|--------|-------|-------------|
| **Operating** | 18,607 | Currently operational facilities |
| **Planned** | 728 | Proposed/announced projects |
| **Under Construction** | 159 | Actively building |
| **Cancelled** | 64 | Cancelled/postponed projects |
| **Expanding** | 60 | Existing facilities adding capacity |
| **Suspended** | 59 | On hold |
| **Reference** | 15 | Country-level stats rows |
| **Pre-proposal** | 2 | Very early stage |

---

## Top 20 Countries by Facility Count

| Rank | Country | Facilities |
|------|---------|------------|
| 1 | United States | 10,406 |
| 2 | United Kingdom | 748 |
| 3 | Germany | 582 |
| 4 | France | 558 |
| 5 | China | 549 |
| 6 | Netherlands | 443 |
| 7 | Canada | 416 |
| 8 | Australia | 397 |
| 9 | India | 343 |
| 10 | Brazil | 299 |
| 11 | Italy | 251 |
| 12 | Japan | 237 |
| 13 | Spain | 221 |
| 14 | Indonesia | 193 |
| 15 | Switzerland | 175 |
| 16 | Sweden | 145 |
| 17 | Russia | 136 |
| 18 | Singapore | 130 |
| 19 | South Africa | 130 |

---

## Key US Pipeline Insights (from DCMap.us & FracTracker)

### DCMap.us Pipeline (July 2026)
- **1,063 facilities** in pipeline
- **250,993 MW** total planned capacity
- **162 under construction** (31,021 MW)
- **901 planned/approved** (219,972 MW)

### Top States by Pipeline Capacity
| State | Projects | Capacity (MW) |
|-------|----------|---------------|
| Texas | 157 | 67,803 |
| Virginia | 183 | 23,222 |
| Georgia | 97 | 8,810 |
| Arizona | 44 | 13,372 |
| Pennsylvania | 41 | 13,376 |
| Ohio | 53 | 6,579 |
| Indiana | 38 | 9,463 |
| Illinois | 34 | 8,506 |

### Largest Announced Projects
| Project | Operator | State | Capacity (MW) | Status | Target |
|---------|----------|-------|---------------|--------|--------|
| Stratos Hyperscale Campus | Bitzero | Utah | 9,000 | Planned | — |
| Monarch Compute Campus | Nscale | West Virginia | 8,000 | Planned | 2027 |
| GW Ranch | Pacifico Energy | Texas | 7,650 | Planned | 2027 |
| New Era Lea Data Center | New Era Energy | New Mexico | 7,000 | Planned | 2028 |
| Meta Hyperion Campus | Meta | Louisiana | 5,000 | Under Construction | 2026 |

---

## CSV Columns

| Column | Description |
|--------|-------------|
| `source` | Data source identifier |
| `facility_name` | Name of the data center facility |
| `operator` | Operating company/owner |
| `city` | City location |
| `state_province` | State/province (normalized to full names for US) |
| `country` | Country |
| `address` | Street address |
| `status` | Operating / Planned / Under Construction / Cancelled / Suspended / Expanding / Reference |
| `capacity_mw` | Power capacity in megawatts (where available) |
| `capacity_category` | Size classification (Small/Medium/Large/Hyperscale/Mega campus) |
| `facility_size_sqft` | Building square footage |
| `property_size_acres` | Land area in acres |
| `project_cost_usd` | Announced project cost |
| `expected_online_date` | Target completion year |
| `latitude` | Latitude coordinate |
| `longitude` | Longitude coordinate |
| `cooling_type` | Cooling method (air, water, closed loop, hybrid) |
| `power_source` | Primary power source |
| `tenant` | Known anchor tenant |
| `purpose` | AI/Cloud/Crypto/Enterprise/Telecom |
| `community_pushback` | Known community opposition |
| `notes` | Additional details |
| `source_url` | Primary source URL |
| `date_added` | Date added to tracker |
| `last_updated` | Last update date |

---

## Known Limitations

1. **GitHub GlobalMap**: Primarily operating facilities; limited capacity/power data
2. **FracTracker**: US-focused; community-sourced; may have duplicates with GitHub data
3. **DCMap.us**: Pipeline projects only; no international coverage
4. **DataCenterMap**: Country aggregates only; no facility-level detail in this export
5. **No single source** has complete global coverage of all planned/under-construction facilities
6. **Commercial databases** (Synergy Research, Structure Research, DC Byte, Baxtel) have more comprehensive data but require paid subscriptions ($20K-50K+/year)

---

## Recommended Next Steps

1. **For investment analysis**: Subscribe to DC Byte, Synergy Research, or Structure Research
2. **For US permitting tracking**: Use FracTracker API or Cleanview API (requires key)
3. **For hyperscale tracking**: Monitor DCMap.us pipeline page and ValueAddVC AI Buildout Tracker
4. **For international**: Use DataCenterMap.info API or Baxtel.com
5. **For power infrastructure**: Cross-reference with ISO/RTO interconnection queues (PJM, ERCOT, CAISO, MISO)

---

## License & Attribution

- **GitHub GlobalMap**: ATLAS dataset (OpenStreetMap ODbL, public sources)
- **FracTracker**: Creative Commons / public compilation from media monitoring
- **DCMap.us**: Public pipeline tracker
- **DataCenterMap**: CC-BY-4.0 / public statistics

This compiled dataset is for research purposes. Verify critical data with primary sources before making investment decisions.