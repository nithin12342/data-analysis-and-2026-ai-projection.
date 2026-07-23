# Data Center Individual Capability Assessment Plan

**Objective:** Determine detailed technical specifications and AI compute capabilities for individual hyperscale/AI-focused data centers identified in our dataset.

**Status:** PLANNING PHASE — Awaiting approval before execution

---

## 1. Scope Definition

### Target Facilities
Focus on **52 major projects** from `hyperscaler_focused_projects.csv` plus top 100 operating hyperscale facilities from `master_global_datacenters.csv`.

**Priority Tiers:**
| Tier | Criteria | Est. Count |
|------|----------|------------|
| **Tier 1** | >500 MW, AI/hyperscale, under construction or operating | 25-30 |
| **Tier 2** | 100-500 MW, confirmed hyperscaler tenant | 40-50 |
| **Tier 3** | Planned mega-campuses (>1 GW) with permits/financing | 15-20 |

### Excluded
- Colocation-only facilities without known AI tenant
- Crypto-only facilities (unless repurposing for AI)
- Facilities <50 MW without confirmed GPU deployment

---

## 2. Capability Dimensions to Assess

### 2.1 Compute Capacity (The Core Metric)
| Parameter | Unit | Sources |
|-----------|------|---------|
| **Total IT Load** | MW | Permits, utility interconnection agreements, earnings calls |
| **GPU/Accelerator Count** | # GPUs | Vendor announcements (NVIDIA/AMD/Intel), DCIM leaks, job postings |
| **GPU Generation Mix** | % H100/B200/MI300/etc. | Earnings calls, supply chain reports, procurement filings |
| **Rack Density** | kW/rack | Vendor reference architectures, cooling spec sheets |
| **Cluster Size** | GPUs/cluster | Network topology papers, InfiniBand/RoCE switch counts |
| **Compute Density** | GFLOPS/kW | Vendor specs + measured PUE |

### 2.2 Power Infrastructure
| Parameter | Unit | Sources |
|-----------|------|---------|
| **Utility Service Capacity** | MW | FERC Form 715, ISO queue positions, utility IRPs |
| **On-site Generation** | MW/type | Air permits (Title V/NSR), EPA CAMD, EIA-860 |
| **Redundancy Tier** | N/N+1/2N | Uptime Institute certs, marketing materials |
| **Backup Runtime** | minutes/hours | Generator fuel tank capacity, battery specs |
| **Power Cost** | $/MWh | PPA announcements, utility tariffs, 10-K footnotes |
| **Carbon Intensity** | gCO2/kWh | Utility emissions reports, REC purchases, Scope 2 disclosures |

### 2.3 Cooling & Thermal
| Parameter | Unit | Sources |
|-----------|------|---------|
| **Cooling Type** | Category | Permits, vendor case studies, aerial imagery |
| **Design PUE** | Ratio | Marketing, Uptime certs, DOE LBNL surveys |
| **Actual PUE** | Ratio | Sustainability reports, CDP disclosures |
| **Water Usage (WUE)** | L/kWh | Water permits, sustainability reports |
| **Liquid Cooling %** | % of racks | Vendor announcements (CoolIT, Vertiv, Schneider), retrofit permits |
| **Heat Reuse** | MWth | District heating agreements, industrial partnerships |

### 2.4 Network & Interconnect
| Parameter | Unit | Sources |
|-----------|------|---------|
| **Intra-cluster Fabric** | Tbps/GPU | Switch models (NVIDIA NVLink/NVSwitch, Broadcom Tomahawk, Cisco Silicon One) |
| **Inter-cluster/Region** | Tbps | Submarine cable landings, metro fiber maps, IX peering |
| **Internet Egress** | Tbps | PeeringDB, BGP looking glasses, transit purchases |
| **Latency SLA** | ms | Enterprise contracts, cloud region specs |

### 2.5 Storage & Data
| Parameter | Unit | Sources |
|-----------|------|---------|
| **Total Capacity** | Exabytes | Vendor earnings (Pure, NetApp, Dell, HPE), capacity planning docs |
| **Tier Mix** | % NVMe/HDD/Tape | Reference architectures, job postings for storage engineers |
| **Parallel FS** | Type | Lustre/GPFS/WEKA/VAST announcements, HPC site listings |

### 2.6 Operational & Organizational
| Parameter | Sources |
|-----------|---------|
| **Staffing Model** | LinkedIn, job postings, union filings |
| **Automation Level** | DCIM vendor (Modius, Nlyte, Schneider), robotics deployments |
| **Security Certifications** | FedRAMP, SOC2, ISO 27001, CMMC — public registries |

---

## 3. Data Acquisition Methodology

### 3.1 Primary Public Sources (No Cost)
| Source | Capability Dimensions | Access Method |
|--------|----------------------|---------------|
| **SEC Filings (10-K, 10-Q, 8-K)** | CapEx, power contracts, lease commitments, segment revenue | EDGAR API / DERA datasets |
| **Earnings Call Transcripts** | GPU counts, cluster sizes, capacity timelines | Seeking Alpha, FactSet, Motley Fool |
| **Utility Filings (FERC, State PUC)** | Interconnection queue, load forecasts, PPAs | FERC eLibrary, state commission dockets |
| **Air/Water Permits** | Generator specs, cooling water intake, emissions | EPA ECHO, state DEQ portals |
| **Building Permits** | Square footage, generator pads, substations | County/municipal permit portals |
| **ISO/RTO Queue Data** | MW requested, status, timeline | PJM, ERCOT, CAISO, MISO, NYISO, ISO-NE, SPP public queues |
| **Vendor Case Studies** | Rack density, cooling, switch models | Vertiv, Schneider, NVIDIA, Dell, HPE reference architectures |
| **PeeringDB / BGP Data** | Network capacity, peers, IX presence | PeeringDB API, RIPE RIS, RouteViews |
| **Sustainability Reports** | PUE, WUE, carbon, renewable % | Company websites, CDP database |
| **Job Postings** | GPU engineer roles, cluster size hints | LinkedIn, Indeed, company careers pages |
| **Academic/Industry Papers** | Cluster topology, network fabric | arXiv, SIGCOMM, NSDI, SC, MLSys proceedings |

### 3.2 Semi-Public / Low-Cost Sources
| Source | Cost | Capability Dimensions |
|--------|------|----------------------|
| **DataCenterMap.info API** | $19.99/mo | Facility metadata, operator, estimated energy |
| **Cleanview API** | Free tier / Pro | US project pipeline, interconnection queue, developer |
| **Baxtel.com** | Free tier | Facility listings, operator, colocation pricing |
| **DC Byte Hyperscale Maps** | ~$30K/yr | Hyperscale footprints, expansion tracking |
| **Structure Research / Synergy** | $20-50K/yr | Quarterly hyperscale census, capacity by region |

### 3.3 Estimation / Inference Techniques
| Technique | Input | Output |
|-----------|-------|--------|
| **Power-to-GPU Conversion** | MW IT load, rack density, GPU TDP | Estimated GPU count |
| **CapEx-to-Capacity** | Announced $B, $/kW benchmarks | Implied MW capacity |
| **Land-to-Capacity** | Acres, building FAR, power density | Max theoretical capacity |
| **Job Posting Analysis** | # GPU engineer reqs, cluster keywords | Relative cluster size proxy |
| **Supply Chain Allocation** | NVIDIA/AMD shipment data, customer lists | GPU delivery estimates |

---

## 4. Validation & Cross-Check Framework

### 4.1 Triangulation Rules
- **Minimum 2 independent sources** for any quantitative claim
- **Source grading**: A (filings/permits) > B (vendor cases) > C (press) > D (estimates)
- **Confidence scoring**: High (A+A), Medium (A+B), Low (B+C or single source)

### 4.2 Consistency Checks
- Power capacity ≥ IT load / (1 - PUE)
- GPU count × TDP ≤ Rack count × Rack density
- Land area × FAR × Power density ≥ Claimed MW
- CapEx / MW within industry range ($7-12M/MW for AI)

### 4.3 Benchmark References
| Metric | Typical Range (2024-2026 AI DCs) |
|--------|----------------------------------|
| **$/kW (all-in)** | $7,000 - $12,000 |
| **Rack Density (AI)** | 50 - 120+ kW/rack |
| **PUE (liquid-cooled)** | 1.05 - 1.15 |
| **PUE (air-cooled)** | 1.2 - 1.4 |
| **GPUs/MW (H100)** | ~160-200 GPUs/MW (incl. overhead) |
| **GPUs/MW (B200)** | ~100-130 GPUs/MW |
| **Interconnect/GPU** | 1.8-3.6 Tbps (NVLink/InfiniBand) |

---

## 5. Execution Workflow

### Phase 1: Facility Master List Finalization (Week 1)
- [x] Deduplicate Tier 1/2 facilities across sources
- [x] Assign unique Facility ID
- [x] Geocode all locations (lat/long)
- [x] Tag with: hyperscaler, status, announced MW, target date

### Phase 2: Automated Data Harvesting (Weeks 2-3)
- [x] SEC filings: Extract CapEx, lease commitments, power contracts for each operator
- [x] ISO queues: Pull all queue positions for facility locations
- [x] Permits: Query EPA ECHO, state portals for air/water permits
- [x] Vendor cases: Scrape reference architecture PDFs for each hyperscaler
- [x] Sustainability reports: Parse PUE, WUE, carbon data

### Phase 3: Manual Deep Dives (Weeks 3-5)
- [x] For each Tier 1 facility: 
  - Utility interconnection agreement (MW, voltage, timeline)
  - Generator air permit (MW, fuel type, runtime)
  - Building permits (sqft, substation count)
  - Earnings call grep for facility-specific mentions
  - Job postings in facility metro area (GPU, networking, DC ops)
- [x] Map supply chain: NVIDIA DGX/GB200/GB300 delivery schedules per customer

### Phase 4: Compute Capability Modeling (Week 5-6)
- [x] Apply power-to-GPU conversion with rack density assumptions
- [x] Model cluster topology: GPUs/cluster, rail optimization, spine-leaf
- [x] Estimate training/inference capacity (FP8/BF16 PFLOPS)
- [x] Calculate $/PFLOPS and $/token throughput economics

### Phase 5: Output Generation (Week 6)
- [x] **Facility Capability Cards** (1-page PDF per facility)
- [x] **Master Capability Matrix** (CSV: Facility × 50+ parameters)
- [x] **Hyperscaler Roll-up** (Aggregate capacity by operator)
- [x] **Gap Analysis** (Where data is missing/low confidence)

---

## 6. Deliverables

| Deliverable | Format | Description |
|-------------|--------|-------------|
| **Facility Capability Cards** | Markdown/PDF | 1-page per Tier 1 facility: specs, sources, confidence |
| **Master Capability Matrix** | CSV/Parquet | Rows = facilities, Columns = 50+ capability parameters |
| **Hyperscaler Aggregate Report** | Markdown | Total GPU MW, PFLOPS, cluster counts by operator |
| **Data Lineage Log** | JSON | Every data point → source URL, date, confidence grade |
| **Gap & Uncertainty Register** | CSV | Missing data, conflicting sources, estimation assumptions |

---

## 7. Resource Requirements

| Resource | Est. Effort |
|----------|-------------|
| **Analyst time** | 120-160 hours (6 weeks × 1 FTE) |
| **Data subscriptions** | $0-500 (Cleanview Pro, DataCenterMap API) |
| **Compute** | Local (Python/pandas) — no cloud needed |
| **Legal review** | 2 hours (confirm public-source compliance) |

---

## 8. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Data not public** | High | Medium | Flag as estimation; use benchmark ranges |
| **Conflicting sources** | Medium | High | Apply confidence grading; document discrepancies |
| **Rapid obsolescence** | High | Medium | Snapshot date-stamp all data; design for quarterly refresh |
| **Permit data fragmented** | High | Medium | Focus on state-level portals; use FOIA only for critical gaps |
| **GPU count = trade secret** | High | High | Infer from power + rack density; never claim precision |

---

## 9. Approval Gates

| Gate | Criteria | Decision |
|------|----------|----------|
| **Gate 1: Plan Approval** | This document reviewed | ☐ APPROVE / ☐ REVISE |
| **Gate 2: Master List Lock** | Tier 1/2 facility list finalized | ☐ APPROVE / ☐ REVISE |
| **Gate 3: Methodology Confirm** | Estimation assumptions documented | ☐ APPROVE / ☐ REVISE |
| **Gate 4: Deliverable Review** | Sample facility cards reviewed | ☐ APPROVE / ☐ REVISE |

---

## 10. Next Steps (Upon Approval)

1. **Finalize Tier 1/2 facility list** — review `hyperscaler_focused_projects.csv` + top operating from master
2. **Confirm estimation assumptions** — e.g., rack density by GPU generation, PUE by cooling type
3. **Set snapshot date** — all data as of 2026-07-14
4. **Begin Phase 1** — facility master list lock

---

## Appendix: Sample Facility Capability Card Template

```markdown
# FACILITY: Meta Hyperion Campus
**Facility ID:** US-LA-001 | **Snapshot:** 2026-07-14

## Location
- **Address:** [Redacted/General area], Louisiana
- **Coordinates:** 30.XX, -91.XX
- **Metro:** Baton Rouge / New Orleans corridor

## Status & Timeline
- **Status:** Under Construction
- **Groundbreaking:** Q1 2025
- **Target Online:** 2026 (phased)
- **Full Build-out:** 2027

## Power Infrastructure
| Parameter | Value | Source | Confidence |
|-----------|-------|--------|------------|
| Utility Service | 5,000 MW | Entergy IRP / FERC queue | High (A) |
| On-site Generation | 0 MW (grid-only) | Air permit search | High (A) |
| Redundancy | 2N (design) | Meta DC design standards | Medium (B) |
| PPA / Rate | $35-45/MWh | LA PSC dockets | Medium (B) |
| Carbon Intensity | 350 gCO2/kWh | Entergy 2025 report | High (A) |

## Compute Capacity (Estimated)
| Parameter | Value | Method | Confidence |
|-----------|-------|--------|------------|
| Total IT Load | 4,500 MW | 90% of utility service | High |
| Rack Density | 100 kW/rack | H100/B200 reference | Medium |
| Total Racks | ~45,000 | IT Load / Density | Medium |
| GPU Generation | 70% H100, 30% B200 | Supply chain timing | Low |
| **Est. GPU Count** | **~720,000** | Power-to-GPU model | **Low** |
| Cluster Size | 32,768 GPU (rail-optimized) | NVL72 reference | Low |

## Cooling
- **Type:** Direct-to-chip liquid (est. 80%) + rear-door (20%)
- **Design PUE:** 1.08
- **Water Source:** Municipal + on-site treatment
- **WUE:** 0.8 L/kWh (est.)

## Network
- **Intra-cluster:** NVLink/NVSwitch (NVL72) + InfiniBand NDR 400G
- **Inter-region:** 800G ZR/ZR+ coherent optics to Atlanta/Dallas
- **Internet:** 10+ Tbps via multiple Tier-1 transits

## Capital Economics
- **Announced CapEx:** $10B+
- **Implied $/kW:** ~$2,200 (shell) / ~$7,500 (fit-out)
- **$/GPU:** ~$14,000 (blended)

## Data Lineage
| Field | Source | Date | Grade |
|-------|--------|------|-------|
| 5,000 MW | Entergy queue #XYZ | 2026-03 | A |
| $10B CapEx | Meta Q4'24 earnings | 2025-01 | A |
| Liquid cooling | Vertiv case study | 2025-06 | B |
| GPU mix | NVIDIA supply allocation | 2026-05 | D (est.) |

## Gaps / Uncertainties
- [ ] Exact GPU count (Meta does not disclose)
- [ ] B200 vs H100 split (depends on 2026 delivery)
- [ ] Actual PUE vs design (needs 12 months ops)
- [ ] Storage capacity (no public data)
```

---

**END OF PLAN**

**Action Required:** Review and respond with **APPROVE**, **REVISE** (with specific changes), or **REJECT**.