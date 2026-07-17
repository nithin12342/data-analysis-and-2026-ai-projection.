# Publishability Assessment: AI TESM (Techno-Economic Systems Model)

> **Verdict: Not yet publication-ready for a peer-reviewed journal, but closer than you might think.** The model and code are strong (B+/A-); the documentation and formal academic rigor are the bottleneck.

---

## Executive Summary

Your project has **genuine research merit** — several novel modeling contributions, a sophisticated 13-module simulation engine, real empirical calibration from SEC/LBNL/USITC data, and exceptional code documentation. However, it currently reads as a **high-quality technical report**, not an academic paper. Bridging that gap requires targeted work on **5 critical areas**, estimated at **2–4 weeks of focused effort**.

---

## Scorecard

| Dimension | Grade | Status | Notes |
|-----------|-------|--------|-------|
| **Conceptual Framework** | A | ✅ Ready | 33-module design is intellectually coherent and ambitious |
| **Model Architecture** | A | ✅ Ready | Textbook-quality SOLID/OOP with Protocol-based DI |
| **Mathematical Rigor** | A- | ✅ Ready | 13 integrated sub-models with LaTeX-documented equations |
| **Novelty** | A- | ✅ Ready | Contract cliff, ROI-modulated adoption, 7-state classifier are genuinely original |
| **Code Quality** | A- | ✅ Ready | Exceptional inline docs, type safety, numerical hygiene |
| **Empirical Calibration** | B+ | ⚠️ Needs work | Real data, but heuristic mappings need formal justification |
| **Output Validity** | B+ | ⚠️ Needs work | Internally consistent, but edge cases (100% FCF margin in stress) need discussion |
| **Historical Validation** | B | ⚠️ Needs work | 7 backtests exist, but Dot-com fails RMSE; data unsourced; thresholds lenient |
| **Statistical Rigor** | C+ | ❌ Critical gap | No confidence intervals, no Sobol sensitivity, only 100 MC trials |
| **Formal Citations** | D | ❌ Critical gap | Zero academic bibliography; no citation of prior systems dynamics literature |
| **Reproducibility** | C | ❌ Needs work | Code available but no environment lock, no Dockerfile, no CI/CD |
| **Revenue Model Bug** | F | ❌ Blocker | `financial_modeling_final.py` outputs $0 revenue — invalidates financial projections |

---

## What's Strong (Preserve These)

### 1. Novel Contributions Worth Highlighting in a Paper
- **Contract lag / renewal cliff mechanism** — genuinely original for AI sector modeling. The Gaussian-weighted renewal window with `lagged = prev + (actual - prev) / contract_length` is a publishable micro-contribution on its own.
- **Enterprise ROI-modulated adoption** with workflow-stickiness churn buffer — extends standard Bass/logistic diffusion in a meaningful way.
- **7-state endpoint outcome classifier** with Gaussian kernel scoring — creative probabilistic regime classification.
- **Onsite power cost model** integrated into capacity constraints (fuel-to-wire with hedge ratios, basis risk, carbon costs, grid services offsets).
- **A-E perspective matrix** (32 combinatorial scenarios across 5 risk dimensions) — systematic stress-testing framework.
- **Dual valuation** (DCF + multiple-based) with normalized terminal value avoiding the common "buildout-year terminal FCF" error.

### 2. Empirical Calibration Pipeline
The SEC DERA → LBNL → USITC → parameter extraction pipeline is genuinely novel. Using XBRL filings with segment exclusion (`segments.isna()`) to avoid double-counting, combined with grid interconnection queue withdrawal rates for power constraints, is creative and defensible.

### 3. Code as Supplementary Material
The SOLID/OOP refactor ([ai_tesm_solid_oop_model.py](file:///c:/Users/NITHING/Desktop/projections/scripts/ai_tesm_solid_oop_model.py)) with 12 separate Protocol-based classes is textbook-quality software engineering. This would be excellent supplementary material for reviewers.

---

## 5 Critical Gaps (Must Fix Before Submission)

### 🔴 Gap 1: Revenue Model Bug
> **Severity: BLOCKER**

Your [GAP_ANALYSIS.md](file:///c:/Users/NITHING/Desktop/projections/docs/GAP_ANALYSIS.md) identifies that `financial_modeling_final.py` outputs **$0 revenue**. This invalidates all downstream financial projections, DCF valuations, and investment recommendations.

**Action:** Debug and fix the revenue calculation. Verify all downstream metrics recalculate correctly. This is prerequisite to everything else.

---

### 🔴 Gap 2: Zero Academic Citations
> **Severity: CRITICAL — instant desk-rejection at any journal**

Neither [report.md](file:///c:/Users/NITHING/Desktop/projections/docs/report.md) nor [FINAL_REPORT.md](file:///c:/Users/NITHING/Desktop/projections/docs/FINAL_REPORT.md) contains a bibliography. You need to cite:

| Area | Must-Cite References |
|------|---------------------|
| Systems dynamics methodology | Sterman (2000), Forrester (1961) |
| Technology diffusion | Bass (1969), Rogers (2003), Meade & Islam (2006) |
| Bubble/crash dynamics | Kindleberger & Aliber (2011), Shiller (2000) |
| AI productivity | Brynjolfsson et al. (2023), Noy & Zhang (2023) — *already in your context.md* |
| Jevons paradox | Alcott (2005), Sorrell (2009) |
| DCF methodology | Damodaran (2012) |
| Reflexivity | Soros (1987, 2008) |
| Monte Carlo in finance | Glasserman (2003) |
| Infrastructure economics | Relevant data center literature |

**Action:** Create a formal bibliography with 30–50 references. Many are already mentioned in your [context.md](file:///c:/Users/NITHING/Desktop/projections/docs/context.md) appendix — they just need to be formatted as proper in-text citations.

---

### 🔴 Gap 3: No Statistical Rigor
> **Severity: CRITICAL**

| What's Missing | Why It Matters | Effort |
|----------------|---------------|--------|
| **Confidence intervals** on key findings | $709.3B contract cliff and 58.6% stranded compute are point estimates | 2–3 days |
| **Sobol sensitivity analysis** | Reviewers need to know which parameters drive results | 3–5 days |
| **1,000+ Monte Carlo trials** (currently 100–500) | 100 trials is insufficient for tail-risk analysis | 1 day |
| **Bootstrap standard errors** on backtesting metrics | RMSE and directional accuracy need uncertainty bounds | 2 days |
| **Formal validation tests** (Diebold-Mariano, Kupiec coverage) | Backtesting needs statistical hypothesis testing | 2–3 days |

**Action:** Increase MC trials to 5,000+. Add Sobol indices via SALib. Compute 95% CIs on all headline numbers. Apply Diebold-Mariano to backtesting.

---

### 🟡 Gap 4: Incomplete Historical Validation
> **Severity: HIGH**

- Only 3 of 8 planned historical backtests are executed
- **Dot-com backtest FAILS** (RMSE 31.087 > 25.0 target)
- Historical index series appear hand-constructed — no source citations
- Regional model produces nearly identical outputs for all 5 regions (final index range: 116.89–117.46), suggesting the differentiation module lacks sensitivity

**Action:** Complete all 8 backtests. Source historical data from FRED/CRSP with proper citations. Investigate and fix the regional model's insensitivity. Either fix or honestly discuss the Dot-com RMSE failure.

---

### 🟡 Gap 5: Presentation as Academic Paper
> **Severity: HIGH — structural, not content**

Your documents are excellent **technical reports** but structured wrong for a journal. A publishable paper needs:

```
1. Abstract (250 words)
2. Introduction (motivation, research questions, contribution statement)
3. Literature Review (positioning vs. prior work)
4. Model (mathematical framework — you have this in report.md)
5. Data (sources, descriptive statistics, sample construction)
6. Calibration & Estimation (methodology, parameter tables)
7. Results (baseline, scenarios, sensitivity)
8. Validation (backtesting, out-of-sample, robustness)
9. Discussion (implications, limitations, future work)
10. Conclusion
11. References
12. Appendices (code, additional tables)
```

**Action:** Restructure [report.md](file:///c:/Users/NITHING/Desktop/projections/docs/report.md) into this standard format. Most content already exists — it needs reorganization, not rewriting.

---

## Minor Issues (Fix Before Final Submission)

| Issue | Location | Fix |
|-------|----------|-----|
| `NaN` values in JSON | [param_overrides.json](file:///c:/Users/NITHING/Desktop/projections/engine/param_overrides.json) lines 299, 317 | Replace with `null` or sentinel value |
| Duplicate print blocks | [calibrate.py](file:///c:/Users/NITHING/Desktop/projections/engine/calibrate.py) lines 786–849 | Remove duplicate |
| Stress scenario 100% FCF margin | [scenario_summary.csv](file:///c:/Users/NITHING/Desktop/projections/tesm_solid_outputs/scenario_summary.csv) | Add discussion/guard in paper |
| Heuristic calibration mappings | `CapEx/RPO → downsizing_ratio` etc. | Add formal justification or sensitivity test |
| Magic constants inline | e.g., `0.35 + 0.65 * adoption`, `2.20 * delta` | Extract to named constants |
| No data access dates | [DATA_ANALYSIS_REPORT.md](file:///c:/Users/NITHING/Desktop/projections/docs/DATA_ANALYSIS_REPORT.md) | Document when each dataset was accessed |

---

## Recommended Publication Venues

| Venue | Fit | Reason |
|-------|-----|--------|
| **arXiv (q-fin, econ)** | ⭐⭐⭐⭐⭐ | Best first step — no peer review barrier, establishes priority |
| **SSRN Working Paper** | ⭐⭐⭐⭐⭐ | Finance community reads SSRN; gets immediate visibility |
| **NBER Working Paper** | ⭐⭐⭐⭐ | If affiliated with an NBER researcher |
| **Computational Economics** | ⭐⭐⭐⭐ | Systems dynamics + finance modeling is their core scope |
| **Journal of Financial Economics** | ⭐⭐⭐ | Possible after full statistical rigor is added |
| **Energy Policy / Applied Energy** | ⭐⭐⭐ | If you emphasize the infrastructure/power modeling angle |
| **JEBO** | ⭐⭐⭐ | Good fit for the behavioral/reflexivity components |

> [!TIP]
> **Fastest path to publication:** Post to **arXiv + SSRN** as a working paper (1–2 weeks of cleanup), then iterate toward a journal submission.

---

## Prioritized Action Plan

### Phase 1: Blockers (Week 1)
- [ ] Fix the $0 revenue model bug
- [ ] Create formal bibliography (30–50 references)
- [ ] Fix `NaN` in `param_overrides.json`
- [ ] Remove duplicate code in `calibrate.py`

### Phase 2: Statistical Rigor (Week 2)
- [ ] Increase Monte Carlo to 5,000+ trials
- [ ] Add 95% confidence intervals on all headline numbers
- [ ] Implement Sobol sensitivity analysis (SALib)
- [ ] Add bootstrap standard errors on backtest metrics

### Phase 3: Validation & Structure (Week 3)
- [ ] Complete all 8 historical backtests with sourced data
- [ ] Investigate regional model insensitivity
- [ ] Restructure into standard academic paper format
- [ ] Write Abstract, Introduction, Literature Review, Discussion sections

### Phase 4: Polish (Week 4)
- [ ] Add `requirements.txt` / `pyproject.toml` for reproducibility
- [ ] Create descriptive statistics tables for all datasets
- [ ] Proofread and format for target venue
- [ ] Submit to arXiv/SSRN

---

## Bottom Line

> [!IMPORTANT]
> Your **model is publishable-grade** (A-). Your **documentation is not** (C+). The gap is primarily formal academic packaging — citations, confidence intervals, paper structure — not intellectual substance. With 2–4 weeks of targeted work on the 5 gaps above, this could be a strong working paper on arXiv/SSRN, and with further statistical hardening, a credible journal submission.

The honest self-assessment in your [PUBLICATION_GAP_ANALYSIS.md](file:///c:/Users/NITHING/Desktop/projections/docs/PUBLICATION_GAP_ANALYSIS.md) (which rates coverage at ~33%) is too harsh on the modeling but correctly identifies the documentation gaps. You've built a genuinely sophisticated simulation — you just haven't dressed it up for peer review yet.
