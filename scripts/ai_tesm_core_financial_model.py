"""
AI Techno-Economic Systems Model (TESM) - Core Mathematical Financial Model
----------------------------------------------------------------------------
Purpose
    A reproducible Python model skeleton for comparing the dot-com bubble with
    the current AI economy and for simulating AI-sector outcomes under demand,
    efficiency, capex, infrastructure, contract-lag, compliance, China/PPP,
    open-source, productivity, valuation, and power/fuel scenarios.

What this file is
    * Core equations and a runnable model engine.
    * Uses illustrative default parameters that should be replaced with public
      data from filings, company reports, macro datasets, benchmarks, etc.
    * No scraping, no external APIs, no proprietary datasets.

What this file is not
    * Not investment advice.
    * Not a fully calibrated publication-grade empirical model.
    * Not a claim that the default assumptions are exact current market facts.

Units
    * Money values are USD billions unless explicitly stated otherwise.
    * Annual time step.
    * Global AI compute capacity and demand are normalized indices.

Run
    python ai_tesm_core_financial_model.py

Outputs
    ./tesm_outputs/scenario_summary.csv
    ./tesm_outputs/perspective_matrix.csv
    ./tesm_outputs/monte_carlo_summary.csv
    ./tesm_outputs/sector_financials_baseline.csv
    ./tesm_outputs/global_metrics_baseline.csv

Core formulas included
    1. Logistic AI adoption with ROI feedback.
    2. Jevons paradox / elastic demand: quantity response to price decline.
    3. AI efficiency: compute-per-token declines over time.
    4. Physical capacity growth constrained by silicon, power, construction.
    5. CapEx overbuild and utilization dynamics.
    6. Enterprise contract-lag / renewal-cliff dynamics.
    7. Agentic AI TCO and compliance costs.
    8. Open-source + China/PPP pricing compression.
    9. Onsite power fuel-price exposure.
    10. Sector financial statements: revenue, EBIT, NOPAT, CapEx, D&A, FCF, ROIC.
    11. DCF valuation and multiple-based price target paths.
    12. Bubble-score and outcome-probability model.
    13. Monte Carlo uncertainty and A-E scenario matrix.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import combinations
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

import math
import numpy as np
import pandas as pd

EPS = 1e-9

# Endpoint outcome states used for sector-level terminal matrices. The degree
# score gives an ordered crash-to-boom scale from -100 to +80.
OUTCOME_ORDER = [
    "complete_severe_crash",
    "severe_crash",
    "moderate_crash",
    "valuation_deflation",
    "prolonged_stagnation",
    "resilient_compounding",
    "booming_expansion",
]

OUTCOME_DEGREE_SCORE = {
    "complete_severe_crash": -100.0,
    "severe_crash": -80.0,
    "moderate_crash": -55.0,
    "valuation_deflation": -25.0,
    "prolonged_stagnation": 0.0,
    "resilient_compounding": 35.0,
    "booming_expansion": 80.0,
}

OUTCOME_LABEL_SHORT = {
    "complete_severe_crash": "complete crash",
    "severe_crash": "severe crash",
    "moderate_crash": "moderate crash",
    "valuation_deflation": "valuation deflation",
    "prolonged_stagnation": "stagnation",
    "resilient_compounding": "resilient",
    "booming_expansion": "booming",
}


# -----------------------------------------------------------------------------
# Utility math
# -----------------------------------------------------------------------------

def clip(x: float, lo: float, hi: float) -> float:
    return float(max(lo, min(hi, x)))


def sigmoid(x: float) -> float:
    if x >= 0:
        z = math.exp(-x)
        return 1.0 / (1.0 + z)
    z = math.exp(x)
    return z / (1.0 + z)


def safe_growth(now: float, prev: float) -> float:
    return float(now / max(prev, EPS) - 1.0)


def cagr(start: float, end: float, years: int) -> float:
    if start <= 0 or end <= 0 or years <= 0:
        return 0.0
    return float((end / start) ** (1.0 / years) - 1.0)


def softmax(scores: Mapping[str, float]) -> Dict[str, float]:
    m = max(scores.values())
    exps = {k: math.exp(v - m) for k, v in scores.items()}
    s = sum(exps.values())
    return {k: v / s for k, v in exps.items()}


def pv_factor(rate: float, year: int) -> float:
    return 1.0 / ((1.0 + rate) ** year)


def gaussian_score(x: float, center: float, width: float) -> float:
    """Log-likelihood-like score; higher means closer to center."""
    return -0.5 * ((x - center) / max(width, EPS)) ** 2


# -----------------------------------------------------------------------------
# Parameter classes
# -----------------------------------------------------------------------------

@dataclass(frozen=True)
class SectorParams:
    """Financial and economic parameters for a sector/category."""

    name: str
    revenue0: float                  # USD bn
    market_cap0: float               # USD bn, example starting equity/EV proxy
    ebit_margin0: float
    gross_margin0: float
    capex_intensity0: float          # sector organic capex / revenue
    nwc_intensity: float             # incremental working capital / revenue change
    invested_capital0: float         # USD bn
    asset_life_years: float
    wacc: float
    terminal_growth: float
    base_growth: float
    base_ev_sales_multiple: float

    # Revenue quality shares, sum should be approximately 1.
    quality_high: float
    quality_medium: float
    quality_low: float

    # Sensitivities to model drivers.
    ai_demand_beta: float
    capex_cycle_beta: float
    price_pressure_beta: float
    productivity_beta: float
    compliance_beta: float
    overcapacity_beta: float

    # Financial operating sensitivities.
    buyer_capex_share: float = 0.0       # share of global AI capacity capex spent by this sector
    capex_sensitivity: float = 0.0       # incremental capex intensity per capacity-growth point
    margin_efficiency_beta: float = 0.2
    margin_price_pressure_beta: float = 0.4
    regulated_share: float = 0.2
    contract_lag_sensitive: bool = False
    infrastructure_supplier: bool = False
    semiconductor_supplier: bool = False

    @property
    def quality_score(self) -> float:
        # High quality revenue gets 1.0, medium 0.55, low 0.15.
        return self.quality_high + 0.55 * self.quality_medium + 0.15 * self.quality_low


@dataclass(frozen=True)
class ModelConfig:
    """Global non-scenario constants."""

    start_year: int = 2026
    horizon_years: int = 20
    tax_rate: float = 0.20
    risk_free_rate: float = 0.045
    equity_risk_premium: float = 0.045
    terminal_growth_cap: float = 0.035

    # Adoption and enterprise ROI.
    initial_enterprise_adoption: float = 0.18
    initial_consumer_adoption: float = 0.35
    max_enterprise_penetration: float = 0.90
    max_consumer_penetration: float = 0.85
    adoption_speed_enterprise: float = 0.32
    adoption_speed_consumer: float = 0.22
    labor_share_enterprise_revenue: float = 0.45
    ai_exposed_labor_share: float = 0.35
    ai_spend_per_enterprise_revenue0: float = 0.015
    base_governance_cost_ratio: float = 0.003
    workflow_stickiness: float = 0.15

    # Compute demand and capacity.
    initial_token_volume: float = 1.0
    initial_price_index: float = 1.0
    initial_compute_per_token: float = 1.0
    initial_compute_capacity: float = 1.25
    target_utilization: float = 0.82
    capacity_obsolescence_rate: float = 0.08
    capex_per_capacity_unit: float = 350.0       # USD bn per normalized capacity unit
    maintenance_capex_per_capacity_unit: float = 18.0
    default_silicon_growth_cap: float = 0.45
    default_power_growth_cap: float = 0.32
    default_construction_growth_cap: float = 0.35
    grid_delay_years: float = 2.0

    # Contract lag.
    contract_mix: float = 0.60
    five_year_contract_mix: float = 0.20
    avg_contract_length_years: float = 3.0
    renewal_cliff_start_year: int = 2027
    renewal_cliff_peak_year: int = 2028
    renewal_cliff_end_year: int = 2030

    # Onsite power defaults, based on user-provided module structure.
    onsite_gen_capacity_mw: float = 2500.0
    total_dc_power_mw0: float = 50000.0
    onsite_capacity_factor: float = 0.75
    onsite_heat_rate_btu_per_kwh: float = 9500.0
    onsite_hedge_ratio: float = 0.65
    onsite_basis_risk: float = 0.15
    grid_services_revenue_per_mw_year: float = 25000.0
    grid_power_price_per_mwh: float = 70.0
    gas_emissions_ton_per_mwh: float = 0.40

    # Bubble-score calibration weights. These are transparent knobs, not facts.
    bubble_weight_valuation: float = 0.30
    bubble_weight_overbuild: float = 0.20
    bubble_weight_revenue_quality: float = 0.15
    bubble_weight_fcf: float = 0.15
    bubble_weight_rates: float = 0.10
    bubble_weight_reflexivity: float = 0.10


@dataclass(frozen=True)
class Scenario:
    """Scenario levers. All rates are annual unless noted."""

    name: str

    # Demand/adoption/efficiency.
    organic_token_growth: float = 0.22
    demand_elasticity: float = 1.05
    inference_cost_decline: float = 0.28       # cost/token decline
    compute_per_token_decline: float = 0.25    # physical compute/token decline
    price_pass_through: float = 0.65
    demand_shock: float = 0.0

    # Productivity and enterprise agents.
    productivity_gross_gain: float = 0.09
    productivity_capture: float = 0.30
    enterprise_agent_intensity: float = 0.25
    agent_autonomy_risk: float = 0.35
    tco_multiplier: float = 1.35
    regulated_compliance_multiplier: float = 1.0

    # Competition and PPP.
    china_price_compression: float = 0.20      # cumulative-ish five-year pressure
    open_source_pressure: float = 0.20         # cumulative-ish five-year pressure
    frontier_quality_premium: float = 0.15
    ppp_cost_advantage: float = 0.35           # lower cost competitors, 0=no advantage, 1=extreme

    # Infrastructure and capex.
    silicon_growth_cap: Optional[float] = None
    power_growth_cap: Optional[float] = None
    construction_growth_cap: Optional[float] = None
    infrastructure_speed: float = 1.0
    capex_reflexivity: float = 0.50
    committed_capex_overbuild: float = 0.03
    stranded_asset_penalty: float = 0.0

    # Enterprise contract renewal cliff.
    renewal_downsize: float = 0.12
    renewal_rate: float = 0.82
    contract_mix_override: Optional[float] = None

    # Valuation / rates / macro.
    valuation_multiple_multiplier: float = 0.85
    wacc_spread_add: float = 0.0
    sentiment_decay: float = 0.03
    recession_shock: float = 0.0
    terminal_growth_adjustment: float = 0.0

    # Onsite power / fuel.
    gas_price_per_mmbtu: float = 4.0
    carbon_price_per_ton: float = 0.0

    # Optional probability weight when using scenario mixtures.
    probability_weight: float = 1.0


# -----------------------------------------------------------------------------
# Default sector universe
# -----------------------------------------------------------------------------

def default_sectors() -> Dict[str, SectorParams]:
    """
    Illustrative sector-level starting values.

    Replace these with public-data calibrated values:
      * SEC/annual report revenues and margins.
      * Segment revenues for cloud, semiconductors, networking, infra.
      * Market caps/enterprise values.
      * CapEx, D&A, RPO/deferred revenue, NRR, etc.
    """
    sectors = {
        "frontier_model_providers": SectorParams(
            name="frontier_model_providers",
            revenue0=30.0,
            market_cap0=500.0,
            ebit_margin0=-0.15,
            gross_margin0=0.55,
            capex_intensity0=0.08,
            nwc_intensity=0.02,
            invested_capital0=60.0,
            asset_life_years=4.0,
            wacc=0.12,
            terminal_growth=0.035,
            base_growth=0.28,
            base_ev_sales_multiple=15.0,
            quality_high=0.20,
            quality_medium=0.50,
            quality_low=0.30,
            ai_demand_beta=0.85,
            capex_cycle_beta=0.10,
            price_pressure_beta=0.85,
            productivity_beta=0.30,
            compliance_beta=0.60,
            overcapacity_beta=0.30,
            buyer_capex_share=0.02,
            capex_sensitivity=0.02,
            margin_efficiency_beta=0.50,
            margin_price_pressure_beta=0.80,
            regulated_share=0.25,
            contract_lag_sensitive=False,
        ),
        "ai_cloud_rental": SectorParams(
            name="ai_cloud_rental",
            revenue0=20.0,
            market_cap0=120.0,
            ebit_margin0=0.05,
            gross_margin0=0.42,
            capex_intensity0=0.42,
            nwc_intensity=0.01,
            invested_capital0=55.0,
            asset_life_years=4.0,
            wacc=0.11,
            terminal_growth=0.030,
            base_growth=0.32,
            base_ev_sales_multiple=8.0,
            quality_high=0.35,
            quality_medium=0.45,
            quality_low=0.20,
            ai_demand_beta=0.90,
            capex_cycle_beta=0.35,
            price_pressure_beta=0.60,
            productivity_beta=0.15,
            compliance_beta=0.20,
            overcapacity_beta=0.85,
            buyer_capex_share=0.15,
            capex_sensitivity=0.20,
            margin_efficiency_beta=0.25,
            margin_price_pressure_beta=0.60,
            regulated_share=0.15,
            contract_lag_sensitive=True,
        ),
        "hyperscaler_cloud_ai": SectorParams(
            name="hyperscaler_cloud_ai",
            revenue0=300.0,
            market_cap0=3500.0,
            ebit_margin0=0.28,
            gross_margin0=0.62,
            capex_intensity0=0.18,
            nwc_intensity=0.015,
            invested_capital0=700.0,
            asset_life_years=5.0,
            wacc=0.085,
            terminal_growth=0.030,
            base_growth=0.17,
            base_ev_sales_multiple=8.5,
            quality_high=0.65,
            quality_medium=0.25,
            quality_low=0.10,
            ai_demand_beta=0.55,
            capex_cycle_beta=0.15,
            price_pressure_beta=0.35,
            productivity_beta=0.20,
            compliance_beta=0.15,
            overcapacity_beta=0.35,
            buyer_capex_share=0.45,
            capex_sensitivity=0.12,
            margin_efficiency_beta=0.20,
            margin_price_pressure_beta=0.30,
            regulated_share=0.30,
            contract_lag_sensitive=True,
        ),
        "ai_semiconductors": SectorParams(
            name="ai_semiconductors",
            revenue0=180.0,
            market_cap0=4000.0,
            ebit_margin0=0.35,
            gross_margin0=0.70,
            capex_intensity0=0.09,
            nwc_intensity=0.03,
            invested_capital0=360.0,
            asset_life_years=6.0,
            wacc=0.095,
            terminal_growth=0.030,
            base_growth=0.20,
            base_ev_sales_multiple=14.0,
            quality_high=0.50,
            quality_medium=0.40,
            quality_low=0.10,
            ai_demand_beta=0.30,
            capex_cycle_beta=1.10,
            price_pressure_beta=0.30,
            productivity_beta=0.10,
            compliance_beta=0.10,
            overcapacity_beta=0.90,
            buyer_capex_share=0.00,
            capex_sensitivity=0.05,
            margin_efficiency_beta=0.10,
            margin_price_pressure_beta=0.25,
            regulated_share=0.05,
            infrastructure_supplier=True,
            semiconductor_supplier=True,
        ),
        "networking_storage_infra": SectorParams(
            name="networking_storage_infra",
            revenue0=100.0,
            market_cap0=500.0,
            ebit_margin0=0.22,
            gross_margin0=0.58,
            capex_intensity0=0.06,
            nwc_intensity=0.025,
            invested_capital0=180.0,
            asset_life_years=7.0,
            wacc=0.095,
            terminal_growth=0.028,
            base_growth=0.16,
            base_ev_sales_multiple=5.0,
            quality_high=0.45,
            quality_medium=0.40,
            quality_low=0.15,
            ai_demand_beta=0.25,
            capex_cycle_beta=0.85,
            price_pressure_beta=0.25,
            productivity_beta=0.08,
            compliance_beta=0.08,
            overcapacity_beta=0.55,
            buyer_capex_share=0.00,
            capex_sensitivity=0.03,
            margin_efficiency_beta=0.08,
            margin_price_pressure_beta=0.20,
            regulated_share=0.05,
            infrastructure_supplier=True,
        ),
        "datacenter_power_cooling": SectorParams(
            name="datacenter_power_cooling",
            revenue0=90.0,
            market_cap0=600.0,
            ebit_margin0=0.15,
            gross_margin0=0.45,
            capex_intensity0=0.30,
            nwc_intensity=0.02,
            invested_capital0=260.0,
            asset_life_years=12.0,
            wacc=0.090,
            terminal_growth=0.027,
            base_growth=0.18,
            base_ev_sales_multiple=6.0,
            quality_high=0.55,
            quality_medium=0.35,
            quality_low=0.10,
            ai_demand_beta=0.20,
            capex_cycle_beta=0.70,
            price_pressure_beta=0.10,
            productivity_beta=0.05,
            compliance_beta=0.10,
            overcapacity_beta=0.55,
            buyer_capex_share=0.10,
            capex_sensitivity=0.10,
            margin_efficiency_beta=0.05,
            margin_price_pressure_beta=0.10,
            regulated_share=0.25,
            infrastructure_supplier=True,
        ),
        "enterprise_ai_software": SectorParams(
            name="enterprise_ai_software",
            revenue0=160.0,
            market_cap0=1400.0,
            ebit_margin0=0.20,
            gross_margin0=0.75,
            capex_intensity0=0.04,
            nwc_intensity=0.015,
            invested_capital0=260.0,
            asset_life_years=5.0,
            wacc=0.095,
            terminal_growth=0.032,
            base_growth=0.18,
            base_ev_sales_multiple=9.0,
            quality_high=0.70,
            quality_medium=0.22,
            quality_low=0.08,
            ai_demand_beta=0.50,
            capex_cycle_beta=0.05,
            price_pressure_beta=0.25,
            productivity_beta=0.55,
            compliance_beta=0.45,
            overcapacity_beta=0.10,
            buyer_capex_share=0.00,
            capex_sensitivity=0.01,
            margin_efficiency_beta=0.15,
            margin_price_pressure_beta=0.25,
            regulated_share=0.45,
            contract_lag_sensitive=True,
        ),
    }
    return sectors


# -----------------------------------------------------------------------------
# Default scenarios
# -----------------------------------------------------------------------------

def named_scenarios() -> Dict[str, Scenario]:
    return {
        "optimistic_productivity": Scenario(
            name="optimistic_productivity",
            organic_token_growth=0.35,
            demand_elasticity=1.35,
            inference_cost_decline=0.35,
            compute_per_token_decline=0.25,
            price_pass_through=0.30,
            productivity_gross_gain=0.15,
            productivity_capture=0.40,
            enterprise_agent_intensity=0.45,
            agent_autonomy_risk=0.25,
            tco_multiplier=1.10,
            china_price_compression=0.05,
            open_source_pressure=0.06,
            frontier_quality_premium=0.35,
            ppp_cost_advantage=0.25,
            silicon_growth_cap=0.55,
            power_growth_cap=0.45,
            construction_growth_cap=0.50,
            infrastructure_speed=1.25,
            capex_reflexivity=0.20,
            committed_capex_overbuild=0.00,
            renewal_downsize=0.05,
            renewal_rate=0.92,
            valuation_multiple_multiplier=1.10,
            wacc_spread_add=-0.005,
            sentiment_decay=0.01,
            gas_price_per_mmbtu=3.5,
            probability_weight=0.20,
        ),
        "baseline_gradual_deflation": Scenario(
            name="baseline_gradual_deflation",
            organic_token_growth=0.22,
            demand_elasticity=1.05,
            inference_cost_decline=0.28,
            compute_per_token_decline=0.25,
            price_pass_through=0.65,
            productivity_gross_gain=0.09,
            productivity_capture=0.30,
            enterprise_agent_intensity=0.25,
            agent_autonomy_risk=0.35,
            tco_multiplier=1.35,
            china_price_compression=0.20,
            open_source_pressure=0.20,
            ppp_cost_advantage=0.35,
            silicon_growth_cap=0.45,
            power_growth_cap=0.32,
            construction_growth_cap=0.35,
            infrastructure_speed=1.0,
            capex_reflexivity=0.50,
            committed_capex_overbuild=0.03,
            renewal_downsize=0.12,
            renewal_rate=0.82,
            valuation_multiple_multiplier=0.85,
            sentiment_decay=0.03,
            gas_price_per_mmbtu=4.0,
            probability_weight=0.45,
        ),
        "pessimistic_renewal_compression": Scenario(
            name="pessimistic_renewal_compression",
            organic_token_growth=0.10,
            demand_elasticity=0.75,
            inference_cost_decline=0.32,
            compute_per_token_decline=0.30,
            price_pass_through=0.80,
            demand_shock=-0.04,
            productivity_gross_gain=0.05,
            productivity_capture=0.22,
            enterprise_agent_intensity=0.15,
            agent_autonomy_risk=0.55,
            tco_multiplier=2.00,
            regulated_compliance_multiplier=1.35,
            china_price_compression=0.45,
            open_source_pressure=0.35,
            ppp_cost_advantage=0.50,
            silicon_growth_cap=0.35,
            power_growth_cap=0.25,
            construction_growth_cap=0.25,
            infrastructure_speed=0.80,
            capex_reflexivity=0.65,
            committed_capex_overbuild=0.06,
            stranded_asset_penalty=0.05,
            renewal_downsize=0.25,
            renewal_rate=0.68,
            valuation_multiple_multiplier=0.60,
            wacc_spread_add=0.010,
            sentiment_decay=0.06,
            recession_shock=-0.03,
            gas_price_per_mmbtu=5.0,
            probability_weight=0.25,
        ),
        "stress_dotcom_like_burst": Scenario(
            name="stress_dotcom_like_burst",
            organic_token_growth=0.00,
            demand_elasticity=0.45,
            inference_cost_decline=0.35,
            compute_per_token_decline=0.35,
            price_pass_through=0.90,
            demand_shock=-0.12,
            productivity_gross_gain=0.02,
            productivity_capture=0.15,
            enterprise_agent_intensity=0.05,
            agent_autonomy_risk=0.80,
            tco_multiplier=2.80,
            regulated_compliance_multiplier=1.75,
            china_price_compression=0.70,
            open_source_pressure=0.60,
            ppp_cost_advantage=0.65,
            silicon_growth_cap=0.25,
            power_growth_cap=0.18,
            construction_growth_cap=0.18,
            infrastructure_speed=0.65,
            capex_reflexivity=0.85,
            committed_capex_overbuild=0.08,
            stranded_asset_penalty=0.12,
            renewal_downsize=0.40,
            renewal_rate=0.55,
            valuation_multiple_multiplier=0.40,
            wacc_spread_add=0.020,
            sentiment_decay=0.10,
            recession_shock=-0.08,
            gas_price_per_mmbtu=7.0,
            carbon_price_per_ton=35.0,
            probability_weight=0.10,
        ),
    }


# -----------------------------------------------------------------------------
# Core model engine
# -----------------------------------------------------------------------------

class TESMModel:
    """Core mathematical engine."""

    def __init__(self, config: Optional[ModelConfig] = None, sectors: Optional[Dict[str, SectorParams]] = None):
        self.config = config or ModelConfig()
        self.sectors = sectors or default_sectors()
        self._validate()

    def _validate(self) -> None:
        for sec in self.sectors.values():
            qsum = sec.quality_high + sec.quality_medium + sec.quality_low
            if not (0.80 <= qsum <= 1.20):
                raise ValueError(f"Revenue quality shares for {sec.name} sum to {qsum:.2f}, expected near 1.")
            if sec.wacc <= sec.terminal_growth:
                raise ValueError(f"WACC must exceed terminal growth for {sec.name}.")

    # ------------------------- Adoption and ROI ------------------------------

    def enterprise_roi_components(
        self,
        scenario: Scenario,
        enterprise_adoption_prev: float,
        price_index_prev: float,
    ) -> Dict[str, float]:
        """
        Enterprise ROI model.

        Gross productivity benefit as % of enterprise revenue:
            gross_benefit = labor_share * AI_exposed_labor_share
                            * productivity_gross_gain * productivity_capture
                            * adoption_effect

        Costs as % of enterprise revenue:
            ai_cost = base_ai_spend * price_index * agent_intensity_factor
            governance_cost = base_governance_cost * TCO_multiplier
                              * autonomy_risk_factor * regulated_multiplier

        ROI:
            roi = (gross_benefit - ai_cost - governance_cost) / (ai_cost + governance_cost)
        """
        cfg = self.config
        adoption_effect = 0.35 + 0.65 * enterprise_adoption_prev
        gross_benefit = (
            cfg.labor_share_enterprise_revenue
            * cfg.ai_exposed_labor_share
            * scenario.productivity_gross_gain
            * scenario.productivity_capture
            * adoption_effect
        )
        ai_cost = (
            cfg.ai_spend_per_enterprise_revenue0
            * price_index_prev
            * (1.0 + 0.60 * scenario.enterprise_agent_intensity)
        )
        governance_cost = (
            cfg.base_governance_cost_ratio
            * scenario.tco_multiplier
            * (1.0 + scenario.agent_autonomy_risk)
            * scenario.regulated_compliance_multiplier
        )
        net_benefit = gross_benefit - ai_cost - governance_cost
        roi = net_benefit / max(ai_cost + governance_cost, EPS)
        return {
            "gross_productivity_benefit_ratio": gross_benefit,
            "ai_cost_ratio": ai_cost,
            "governance_cost_ratio": governance_cost,
            "net_productivity_benefit_ratio": net_benefit,
            "enterprise_roi": roi,
        }

    def update_adoption(
        self,
        scenario: Scenario,
        enterprise_prev: float,
        consumer_prev: float,
        enterprise_roi: float,
        price_decline_rate: float,
    ) -> Tuple[float, float]:
        """
        Logistic diffusion with ROI feedback.

        enterprise_delta = speed * p * (1 - p/K) * roi_multiplier
        consumer_delta   = speed * p * (1 - p/K) * price_multiplier

        Negative ROI can slow adoption or cause mild churn, but workflow
        stickiness reduces reversal once embedded.
        """
        cfg = self.config
        # ROI multiplier ranges roughly from -0.20 to 1.30.
        roi_multiplier = 1.50 * sigmoid(enterprise_roi) - 0.20
        churn_buffer = cfg.workflow_stickiness * enterprise_prev
        enterprise_delta = (
            cfg.adoption_speed_enterprise
            * enterprise_prev
            * max(0.0, 1.0 - enterprise_prev / cfg.max_enterprise_penetration)
            * roi_multiplier
        )
        if enterprise_delta < 0:
            enterprise_delta *= (1.0 - churn_buffer)
        enterprise = clip(enterprise_prev + enterprise_delta, 0.01, cfg.max_enterprise_penetration)

        price_multiplier = 0.75 + 1.50 * clip(price_decline_rate, 0.0, 0.70)
        consumer_delta = (
            cfg.adoption_speed_consumer
            * consumer_prev
            * max(0.0, 1.0 - consumer_prev / cfg.max_consumer_penetration)
            * price_multiplier
        )
        consumer = clip(consumer_prev + consumer_delta, 0.01, cfg.max_consumer_penetration)
        return enterprise, consumer

    # ----------------------- Price, efficiency, demand ------------------------

    def annual_price_decline_rate(self, scenario: Scenario, year_index: int) -> float:
        """
        AI price decline combines:
          * pass-through of inference cost decline;
          * China/PPP competition;
          * open-source commoditization;
          * decaying frontier quality premium.

        We interpret china_price_compression and open_source_pressure as medium-
        run pressure variables, annualized across roughly five years.
        """
        frontier_premium_decay = scenario.frontier_quality_premium * math.exp(-0.25 * year_index)
        competition_pressure = (
            0.55 * scenario.china_price_compression * (1.0 + 0.50 * scenario.ppp_cost_advantage)
            + 0.45 * scenario.open_source_pressure
        ) / 5.0
        premium_offset = 0.35 * frontier_premium_decay / 5.0
        decline = scenario.price_pass_through * scenario.inference_cost_decline + competition_pressure - premium_offset
        return clip(decline, 0.00, 0.75)

    def onsite_power_economics(self, scenario: Scenario) -> Dict[str, float]:
        """
        Onsite fuel exposure.

        energy_mwh = MW * capacity_factor * 8760
        heat_rate_mmbtu_per_mwh = Btu/kWh / 1000
        effective_fuel_price = gas_price * [hedge + (1-hedge)*(1+basis_risk)]
        fuel_cost = energy_mwh * heat_rate * fuel_price
        carbon_cost = energy_mwh * emissions_rate * carbon_price
        grid_services = MW * grid_services_revenue_per_mw_year
        grid_equivalent = energy_mwh * grid_power_price
        net_delta_vs_grid = fuel_cost + carbon_cost - grid_services - grid_equivalent
        """
        cfg = self.config
        energy_mwh = cfg.onsite_gen_capacity_mw * cfg.onsite_capacity_factor * 8760.0
        heat_rate = cfg.onsite_heat_rate_btu_per_kwh / 1000.0  # MMBtu/MWh
        effective_fuel_price = scenario.gas_price_per_mmbtu * (
            cfg.onsite_hedge_ratio + (1.0 - cfg.onsite_hedge_ratio) * (1.0 + cfg.onsite_basis_risk)
        )
        fuel_cost_bn = energy_mwh * heat_rate * effective_fuel_price / 1e9
        carbon_cost_bn = energy_mwh * cfg.gas_emissions_ton_per_mwh * scenario.carbon_price_per_ton / 1e9
        grid_services_bn = cfg.onsite_gen_capacity_mw * cfg.grid_services_revenue_per_mw_year / 1e9
        grid_equivalent_bn = energy_mwh * cfg.grid_power_price_per_mwh / 1e9
        net_delta_bn = fuel_cost_bn + carbon_cost_bn - grid_services_bn - grid_equivalent_bn
        onsite_share = cfg.onsite_gen_capacity_mw / max(cfg.total_dc_power_mw0, EPS)
        power_growth_bonus = 0.50 * onsite_share
        return {
            "onsite_energy_mwh": energy_mwh,
            "onsite_fuel_cost_bn": fuel_cost_bn,
            "onsite_carbon_cost_bn": carbon_cost_bn,
            "onsite_grid_services_revenue_bn": grid_services_bn,
            "onsite_grid_equivalent_cost_bn": grid_equivalent_bn,
            "onsite_net_delta_vs_grid_bn": net_delta_bn,
            "onsite_power_growth_bonus": power_growth_bonus,
        }

    # -------------------------- Simulation engine -----------------------------

    def simulate(self, scenario: Scenario) -> Dict[str, object]:
        cfg = self.config
        years = np.arange(cfg.start_year, cfg.start_year + cfg.horizon_years + 1)
        n = len(years)

        # Global state arrays.
        enterprise_adoption = np.zeros(n)
        consumer_adoption = np.zeros(n)
        token_volume = np.zeros(n)
        price_index = np.zeros(n)
        compute_per_token = np.zeros(n)
        compute_demand = np.zeros(n)
        training_compute = np.zeros(n)
        compute_capacity = np.zeros(n)
        utilization = np.zeros(n)
        overcapacity_ratio = np.zeros(n)
        global_capacity_capex = np.zeros(n)
        allowed_capacity_growth = np.zeros(n)
        price_decline = np.zeros(n)
        token_growth = np.zeros(n)
        net_productivity_benefit = np.zeros(n)
        enterprise_roi = np.zeros(n)
        governance_cost_ratio = np.zeros(n)
        actual_cloud_demand_index = np.zeros(n)
        monetized_ai_spend_index = np.zeros(n)
        adoption_index = np.zeros(n)

        enterprise_adoption[0] = cfg.initial_enterprise_adoption
        consumer_adoption[0] = cfg.initial_consumer_adoption
        token_volume[0] = cfg.initial_token_volume
        price_index[0] = cfg.initial_price_index
        compute_per_token[0] = cfg.initial_compute_per_token
        training_compute[0] = 0.18
        compute_demand[0] = token_volume[0] * compute_per_token[0] + training_compute[0]
        compute_capacity[0] = cfg.initial_compute_capacity
        utilization[0] = min(1.0, compute_demand[0] / max(compute_capacity[0], EPS))
        overcapacity_ratio[0] = max(0.0, compute_capacity[0] / max(compute_demand[0], EPS) - 1.0 / cfg.target_utilization)
        actual_cloud_demand_index[0] = compute_demand[0] * price_index[0]
        monetized_ai_spend_index[0] = token_volume[0] * price_index[0]
        adoption_index[0] = 0.70 * enterprise_adoption[0] + 0.30 * consumer_adoption[0]
        # Initialize capacity capex so first-year capex-cycle growth is not
        # mechanically inflated by comparing against zero.
        global_capacity_capex[0] = (
            cfg.initial_compute_capacity * cfg.maintenance_capex_per_capacity_unit
            + 0.15 * cfg.capex_per_capacity_unit
        )

        onsite = self.onsite_power_economics(scenario)
        silicon_cap = scenario.silicon_growth_cap if scenario.silicon_growth_cap is not None else cfg.default_silicon_growth_cap
        power_cap = scenario.power_growth_cap if scenario.power_growth_cap is not None else cfg.default_power_growth_cap
        construction_cap = scenario.construction_growth_cap if scenario.construction_growth_cap is not None else cfg.default_construction_growth_cap
        power_cap_effective = power_cap + onsite["onsite_power_growth_bonus"]

        # Sector-level arrays.
        sector_data: Dict[str, Dict[str, np.ndarray]] = {}
        for key, sec in self.sectors.items():
            sector_data[key] = {
                "actual_revenue": np.zeros(n),
                "reported_revenue": np.zeros(n),
                "revenue_growth": np.zeros(n),
                "ebit_margin": np.zeros(n),
                "ebit": np.zeros(n),
                "tax": np.zeros(n),
                "nopat": np.zeros(n),
                "capex": np.zeros(n),
                "depreciation": np.zeros(n),
                "fcf": np.zeros(n),
                "invested_capital": np.zeros(n),
                "roic": np.zeros(n),
                "ev_sales_multiple": np.zeros(n),
                "multiple_based_value": np.zeros(n),
            }
            sector_data[key]["actual_revenue"][0] = sec.revenue0
            sector_data[key]["reported_revenue"][0] = sec.revenue0
            sector_data[key]["ebit_margin"][0] = sec.ebit_margin0
            sector_data[key]["ebit"][0] = sec.revenue0 * sec.ebit_margin0
            sector_data[key]["tax"][0] = max(0.0, sector_data[key]["ebit"][0] * cfg.tax_rate)
            sector_data[key]["nopat"][0] = sector_data[key]["ebit"][0] - sector_data[key]["tax"][0]
            sector_data[key]["capex"][0] = sec.revenue0 * sec.capex_intensity0
            sector_data[key]["depreciation"][0] = sec.invested_capital0 / sec.asset_life_years
            sector_data[key]["fcf"][0] = (
                sector_data[key]["nopat"][0]
                + sector_data[key]["depreciation"][0]
                - sector_data[key]["capex"][0]
            )
            sector_data[key]["invested_capital"][0] = sec.invested_capital0
            sector_data[key]["roic"][0] = sector_data[key]["nopat"][0] / max(sec.invested_capital0, EPS)
            sector_data[key]["ev_sales_multiple"][0] = sec.base_ev_sales_multiple
            sector_data[key]["multiple_based_value"][0] = sec.revenue0 * sec.base_ev_sales_multiple

        # Annual simulation.
        for t in range(1, n):
            year = int(years[t])
            # Enterprise ROI based on prior price/adoption.
            roi_parts = self.enterprise_roi_components(scenario, enterprise_adoption[t - 1], price_index[t - 1])
            net_productivity_benefit[t] = roi_parts["net_productivity_benefit_ratio"]
            enterprise_roi[t] = roi_parts["enterprise_roi"]
            governance_cost_ratio[t] = roi_parts["governance_cost_ratio"]

            # Price and adoption.
            price_decline[t] = self.annual_price_decline_rate(scenario, t)
            price_index[t] = price_index[t - 1] * (1.0 - price_decline[t])
            enterprise_adoption[t], consumer_adoption[t] = self.update_adoption(
                scenario,
                enterprise_adoption[t - 1],
                consumer_adoption[t - 1],
                enterprise_roi[t],
                price_decline[t],
            )

            # Jevons / elastic demand.
            price_ratio = price_index[t] / max(price_index[t - 1], EPS)
            price_elastic_growth = price_ratio ** (-scenario.demand_elasticity) - 1.0
            enterprise_adoption_delta = enterprise_adoption[t] - enterprise_adoption[t - 1]
            consumer_adoption_delta = consumer_adoption[t] - consumer_adoption[t - 1]
            adoption_usage_growth = 2.20 * enterprise_adoption_delta + 0.90 * consumer_adoption_delta
            agent_usage_growth = 0.06 * scenario.enterprise_agent_intensity * enterprise_adoption[t]
            raw_token_growth = (
                scenario.organic_token_growth
                + scenario.demand_shock
                + scenario.recession_shock
                + price_elastic_growth
                + adoption_usage_growth
                + agent_usage_growth
            )
            token_growth[t] = clip(raw_token_growth, -0.60, 2.50)
            token_volume[t] = token_volume[t - 1] * (1.0 + token_growth[t])

            # Efficiency and compute demand.
            compute_per_token[t] = compute_per_token[t - 1] * (1.0 - clip(scenario.compute_per_token_decline, 0.0, 0.85))
            # Training demand grows sublinearly with total usage and is reduced by open-source reuse/distillation.
            training_compute[t] = 0.18 * (token_volume[t] ** 0.65) * (1.0 - 0.25 * scenario.open_source_pressure)
            compute_demand[t] = token_volume[t] * compute_per_token[t] + training_compute[t]
            actual_cloud_demand_index[t] = compute_demand[t] * price_index[t]
            # Monetized AI spend is volume times price. It prevents the model
            # from treating free/near-free token explosions as equal to revenue.
            monetized_ai_spend_index[t] = token_volume[t] * price_index[t]
            adoption_index[t] = 0.70 * enterprise_adoption[t] + 0.30 * consumer_adoption[t]

            # Physical constraints.
            base_allowed_growth = min(silicon_cap, power_cap_effective, construction_cap) * scenario.infrastructure_speed
            # Grid delay dampens near-term deployment; effect fades as infrastructure adapts.
            delay_drag = cfg.grid_delay_years / (cfg.grid_delay_years + t + 1.0)
            allowed_capacity_growth[t] = clip(base_allowed_growth * (1.0 - 0.35 * delay_drag), 0.02, 1.20)

            existing_after_obsolescence = compute_capacity[t - 1] * (1.0 - cfg.capacity_obsolescence_rate)
            desired_capacity = compute_demand[t] / cfg.target_utilization
            demand_gap_addition = max(0.0, desired_capacity - existing_after_obsolescence)
            reflexive_addition = (
                compute_capacity[t - 1]
                * scenario.capex_reflexivity
                * max(token_growth[t], 0.0)
                * max(scenario.valuation_multiple_multiplier, 0.20)
                * math.exp(-scenario.sentiment_decay * t)
            )
            committed_addition = (
                compute_capacity[t - 1]
                * scenario.committed_capex_overbuild
                * max(0.0, 1.0 - t / 6.0)
            )
            planned_addition = demand_gap_addition + reflexive_addition + committed_addition
            max_physical_addition = compute_capacity[t - 1] * allowed_capacity_growth[t]
            capacity_addition = min(planned_addition, max_physical_addition)
            compute_capacity[t] = existing_after_obsolescence + capacity_addition
            utilization[t] = min(1.0, compute_demand[t] / max(compute_capacity[t], EPS))
            overcapacity_ratio[t] = max(0.0, compute_capacity[t] / max(compute_demand[t], EPS) - 1.0 / cfg.target_utilization)
            global_capacity_capex[t] = (
                capacity_addition * cfg.capex_per_capacity_unit
                + compute_capacity[t] * cfg.maintenance_capex_per_capacity_unit
            )

            raw_token_g = safe_growth(token_volume[t], token_volume[t - 1])
            monetized_demand_g = safe_growth(monetized_ai_spend_index[t], monetized_ai_spend_index[t - 1])
            adoption_g = safe_growth(adoption_index[t], adoption_index[t - 1])
            compute_g = safe_growth(compute_demand[t], compute_demand[t - 1])
            capex_g = safe_growth(global_capacity_capex[t], max(global_capacity_capex[t - 1], 0.01))
            cloud_demand_g = safe_growth(actual_cloud_demand_index[t], actual_cloud_demand_index[t - 1])
            competition_pressure = (scenario.china_price_compression + scenario.open_source_pressure) / 5.0
            regulated_cost_ratio = governance_cost_ratio[t] * scenario.regulated_compliance_multiplier
            # Financial growth must fade toward maturity; token volume can grow
            # very rapidly as price falls, but revenue cannot compound at raw
            # token growth forever. This is a saturation guard, not a data claim.
            growth_fade = math.exp(-0.15 * t)
            driver_fade = math.exp(-0.10 * max(0, t - 4))

            # Margin impact of onsite power relative to grid, allocated to cloud/DC buyers.
            # Positive net_delta means onsite more expensive than grid equivalent.
            total_cloud_like_revenue_prev = sum(
                sector_data[k]["reported_revenue"][t - 1]
                for k, s in self.sectors.items()
                if s.buyer_capex_share > 0.10 or "cloud" in s.name or "datacenter" in s.name
            )
            power_margin_drag = max(0.0, onsite["onsite_net_delta_vs_grid_bn"]) / max(total_cloud_like_revenue_prev, EPS)

            for key, sec in self.sectors.items():
                prev_actual_rev = sector_data[key]["actual_revenue"][t - 1]
                prev_reported_rev = sector_data[key]["reported_revenue"][t - 1]

                # Revenue growth driver. Supplier sectors benefit from capex
                # cycle; model/API sectors benefit from monetized AI spend;
                # enterprise software benefits more from adoption/workflow
                # integration than from raw token volume.
                base_growth_t = sec.terminal_growth + (sec.base_growth - sec.terminal_growth) * growth_fade
                if sec.semiconductor_supplier:
                    sector_driver_g = 0.45 * compute_g + 0.55 * capex_g
                elif sec.infrastructure_supplier:
                    sector_driver_g = 0.20 * compute_g + 0.80 * capex_g
                elif "cloud" in sec.name or "rental" in sec.name:
                    sector_driver_g = cloud_demand_g
                elif "enterprise" in sec.name:
                    sector_driver_g = 0.75 * adoption_g + 0.25 * monetized_demand_g
                elif "frontier_model" in sec.name:
                    sector_driver_g = 0.75 * monetized_demand_g + 0.25 * adoption_g
                else:
                    sector_driver_g = monetized_demand_g

                growth = (
                    base_growth_t
                    + driver_fade * sec.ai_demand_beta * sector_driver_g
                    + driver_fade * sec.capex_cycle_beta * capex_g
                    - sec.price_pressure_beta * (price_decline[t] + competition_pressure)
                    + sec.productivity_beta * net_productivity_benefit[t]
                    - sec.compliance_beta * regulated_cost_ratio
                    - sec.overcapacity_beta * overcapacity_ratio[t] * 0.14
                    + scenario.recession_shock
                )

                # Cloud revenue is more tied to cloud demand index than generic sector growth.
                if sec.contract_lag_sensitive and ("cloud" in sec.name or "rental" in sec.name):
                    growth = 0.35 * growth + 0.65 * cloud_demand_g

                # Semiconductor/infrastructure cycles can reverse sharply when capacity is idle.
                if sec.semiconductor_supplier:
                    if utilization[t] < 0.70:
                        growth -= 0.35 * (0.70 - utilization[t]) / 0.70
                    if overcapacity_ratio[t] > 0.30:
                        growth -= 0.15 * overcapacity_ratio[t]
                if sec.infrastructure_supplier:
                    growth += 0.10 * allowed_capacity_growth[t]
                    if t > 4 and utilization[t] < 0.65:
                        growth -= 0.18 * (0.65 - utilization[t]) / 0.65

                growth = clip(growth, -0.65, 0.55)
                actual_revenue = max(0.01, prev_actual_rev * (1.0 + growth))

                # Contract lag / renewal cliff.
                if sec.contract_lag_sensitive:
                    reported_revenue = self._apply_contract_lag(
                        year=year,
                        prev_reported=prev_reported_rev,
                        actual_revenue=actual_revenue,
                        scenario=scenario,
                        enterprise_roi=enterprise_roi[t],
                    )
                else:
                    reported_revenue = actual_revenue

                sector_data[key]["actual_revenue"][t] = actual_revenue
                sector_data[key]["reported_revenue"][t] = reported_revenue
                sector_data[key]["revenue_growth"][t] = safe_growth(reported_revenue, prev_reported_rev)

                # Margin model.
                margin = (
                    sec.ebit_margin0
                    + sec.margin_efficiency_beta * scenario.inference_cost_decline * 0.25
                    + sec.productivity_beta * net_productivity_benefit[t] * 0.60
                    - sec.margin_price_pressure_beta * competition_pressure
                    - sec.compliance_beta * regulated_cost_ratio
                    - sec.overcapacity_beta * overcapacity_ratio[t] * 0.08
                    - scenario.stranded_asset_penalty * max(0.0, 0.75 - utilization[t])
                )
                if sec.semiconductor_supplier and utilization[t] < 0.75:
                    margin -= 0.45 * (0.75 - utilization[t])
                if sec.buyer_capex_share > 0.10 or "cloud" in sec.name or "datacenter" in sec.name:
                    margin -= power_margin_drag
                # Frontier providers face the strongest price compression but gain from inference efficiency.
                if "frontier_model" in sec.name:
                    margin += 0.35 * scenario.inference_cost_decline
                    margin -= 0.45 * competition_pressure
                margin = clip(margin, -0.60, 0.60)
                sector_data[key]["ebit_margin"][t] = margin

                ebit = reported_revenue * margin
                tax = max(0.0, ebit * cfg.tax_rate)
                nopat = ebit - tax
                prev_ic = sector_data[key]["invested_capital"][t - 1]
                depreciation = prev_ic / sec.asset_life_years

                capacity_growth_rate = safe_growth(compute_capacity[t], compute_capacity[t - 1])
                capex_intensity = sec.capex_intensity0 + sec.capex_sensitivity * max(0.0, capacity_growth_rate)
                capex_intensity = clip(capex_intensity, 0.00, 0.90)
                capex = reported_revenue * capex_intensity + sec.buyer_capex_share * global_capacity_capex[t]
                delta_nwc = sec.nwc_intensity * (reported_revenue - prev_reported_rev)
                fcf = nopat + depreciation - capex - delta_nwc
                invested_capital = max(0.01, prev_ic + capex - depreciation)
                roic = nopat / max(prev_ic, EPS)

                sector_data[key]["ebit"][t] = ebit
                sector_data[key]["tax"][t] = tax
                sector_data[key]["nopat"][t] = nopat
                sector_data[key]["depreciation"][t] = depreciation
                sector_data[key]["capex"][t] = capex
                sector_data[key]["fcf"][t] = fcf
                sector_data[key]["invested_capital"][t] = invested_capital
                sector_data[key]["roic"][t] = roic

                # Multiple-based valuation path.
                forward_cagr_proxy = clip(0.50 * sector_data[key]["revenue_growth"][t] + 0.50 * sec.base_growth, -0.20, 0.80)
                roic_spread = roic - (sec.wacc + scenario.wacc_spread_add)
                quality_adj = 0.65 + 0.55 * sec.quality_score
                growth_adj = clip(1.0 + 2.2 * (forward_cagr_proxy - 0.08), 0.30, 2.50)
                roic_adj = clip(1.0 + 3.0 * roic_spread, 0.25, 2.20)
                compression_adj = clip(1.0 - 0.35 * (scenario.china_price_compression + scenario.open_source_pressure), 0.25, 1.10)
                sentiment_adj = scenario.valuation_multiple_multiplier * math.exp(-scenario.sentiment_decay * t)
                ev_sales_multiple = sec.base_ev_sales_multiple * quality_adj * growth_adj * roic_adj * compression_adj * sentiment_adj
                ev_sales_multiple = clip(ev_sales_multiple, 0.20, 60.0)
                sector_data[key]["ev_sales_multiple"][t] = ev_sales_multiple
                sector_data[key]["multiple_based_value"][t] = reported_revenue * ev_sales_multiple

        global_df = pd.DataFrame({
            "year": years,
            "enterprise_adoption": enterprise_adoption,
            "consumer_adoption": consumer_adoption,
            "token_volume_index": token_volume,
            "price_index": price_index,
            "price_decline": price_decline,
            "compute_per_token_index": compute_per_token,
            "training_compute_index": training_compute,
            "compute_demand_index": compute_demand,
            "compute_capacity_index": compute_capacity,
            "utilization": utilization,
            "overcapacity_ratio": overcapacity_ratio,
            "allowed_capacity_growth": allowed_capacity_growth,
            "global_capacity_capex_bn": global_capacity_capex,
            "token_growth": token_growth,
            "net_productivity_benefit_ratio": net_productivity_benefit,
            "enterprise_roi": enterprise_roi,
            "governance_cost_ratio": governance_cost_ratio,
            "actual_cloud_demand_index": actual_cloud_demand_index,
            "monetized_ai_spend_index": monetized_ai_spend_index,
            "adoption_index": adoption_index,
            **{k: v for k, v in onsite.items() if isinstance(v, (int, float))},
        })

        sector_rows = []
        for key, sec in self.sectors.items():
            arrays = sector_data[key]
            for i, year in enumerate(years):
                sector_rows.append({
                    "scenario": scenario.name,
                    "year": int(year),
                    "sector": key,
                    "actual_revenue_bn": arrays["actual_revenue"][i],
                    "reported_revenue_bn": arrays["reported_revenue"][i],
                    "revenue_growth": arrays["revenue_growth"][i],
                    "ebit_margin": arrays["ebit_margin"][i],
                    "ebit_bn": arrays["ebit"][i],
                    "tax_bn": arrays["tax"][i],
                    "nopat_bn": arrays["nopat"][i],
                    "capex_bn": arrays["capex"][i],
                    "depreciation_bn": arrays["depreciation"][i],
                    "fcf_bn": arrays["fcf"][i],
                    "invested_capital_bn": arrays["invested_capital"][i],
                    "roic": arrays["roic"][i],
                    "ev_sales_multiple": arrays["ev_sales_multiple"][i],
                    "multiple_based_value_bn": arrays["multiple_based_value"][i],
                    "quality_score": sec.quality_score,
                    "quality_low": sec.quality_low,
                })
        sector_df = pd.DataFrame(sector_rows)

        dcf_df = self._dcf(sector_df, scenario)
        summary = self._summary(global_df, sector_df, dcf_df, scenario)
        outcome_probs = self._outcome_probabilities(global_df, sector_df, dcf_df, scenario, summary)
        summary.update({f"prob_{k}": v for k, v in outcome_probs.items()})

        return {
            "global": global_df,
            "sector": sector_df,
            "dcf": dcf_df,
            "summary": summary,
            "outcome_probabilities": outcome_probs,
        }

    def _apply_contract_lag(
        self,
        year: int,
        prev_reported: float,
        actual_revenue: float,
        scenario: Scenario,
        enterprise_roi: float,
    ) -> float:
        """
        Multi-year contracts delay revenue response.

        contracted revenue moves gradually toward actual demand:
            lagged = previous_reported + (actual - previous_reported) / contract_length

        reported = contract_mix * lagged + (1-contract_mix) * actual

        During renewal cliff window, a fraction of contracts is downsized:
            downsize = renewal_downsize * (1-renewal_rate) * renewal_weight * ROI_modifier
        """
        cfg = self.config
        contract_mix = scenario.contract_mix_override if scenario.contract_mix_override is not None else cfg.contract_mix
        contract_mix = clip(contract_mix + cfg.five_year_contract_mix * 0.50, 0.0, 0.95)
        lagged = prev_reported + (actual_revenue - prev_reported) / max(cfg.avg_contract_length_years, 1.0)
        reported = contract_mix * lagged + (1.0 - contract_mix) * actual_revenue

        if cfg.renewal_cliff_start_year <= year <= cfg.renewal_cliff_end_year:
            sigma = max(0.75, (cfg.renewal_cliff_end_year - cfg.renewal_cliff_start_year) / 3.0)
            renewal_weight = math.exp(-0.5 * ((year - cfg.renewal_cliff_peak_year) / sigma) ** 2)
            roi_modifier = clip(1.0 - max(enterprise_roi, -1.0) / 2.0, 0.10, 1.75)
            downsize = scenario.renewal_downsize * (1.0 - scenario.renewal_rate) * renewal_weight * roi_modifier * contract_mix
            reported *= (1.0 - clip(downsize, 0.0, 0.70))
        return max(0.01, reported)

    # ----------------------------- Valuation ---------------------------------

    def _dcf(self, sector_df: pd.DataFrame, scenario: Scenario) -> pd.DataFrame:
        rows = []
        cfg = self.config
        for key, sec in self.sectors.items():
            sdf = sector_df[sector_df["sector"] == key].sort_values("year").reset_index(drop=True)
            fcf = sdf["fcf_bn"].to_numpy()
            revenue = sdf["reported_revenue_bn"].to_numpy()
            wacc = max(0.02, sec.wacc + scenario.wacc_spread_add)
            terminal_growth = min(sec.terminal_growth + scenario.terminal_growth_adjustment, cfg.terminal_growth_cap, wacc - 0.01)
            # Use years 1..N for explicit DCF; year 0 is starting year.
            pv_fcf = 0.0
            for t in range(1, len(fcf)):
                pv_fcf += fcf[t] * pv_factor(wacc, t)

            forecast_cagr = cagr(revenue[0], revenue[-1], len(revenue) - 1)
            avg_roic_5y = float(sdf.tail(5)["roic"].mean())
            # Terminal value should represent a stable-growth state. The final
            # explicit forecast year may include temporary buildout CapEx or
            # stranded-asset charges. Normalize terminal FCF from NOPAT and a
            # sustainable reinvestment rate: reinvestment ~= g / ROIC.
            terminal_ebit_margin = float(sdf.tail(5)["ebit_margin"].mean())
            terminal_nopat = revenue[-1] * terminal_ebit_margin * (1.0 - cfg.tax_rate if terminal_ebit_margin > 0 else 1.0)
            stable_roic = max(abs(avg_roic_5y), wacc + 0.01)
            reinvestment_rate = clip(terminal_growth / stable_roic, 0.05, 0.85) if terminal_nopat > 0 else 0.0
            normalized_terminal_fcf = terminal_nopat * (1.0 - reinvestment_rate)
            terminal_fcf = normalized_terminal_fcf * (1.0 + terminal_growth)
            terminal_value = terminal_fcf / max(wacc - terminal_growth, EPS)
            pv_terminal = terminal_value * pv_factor(wacc, len(fcf) - 1)
            dcf_ev = pv_fcf + pv_terminal
            rows.append({
                "scenario": scenario.name,
                "sector": key,
                "dcf_ev_bn": dcf_ev,
                "market_cap0_bn": sec.market_cap0,
                "fair_value_to_market": dcf_ev / max(sec.market_cap0, EPS),
                "market_to_fair_value": sec.market_cap0 / max(dcf_ev, EPS),
                "wacc": wacc,
                "terminal_growth": terminal_growth,
                "forecast_revenue_cagr": forecast_cagr,
                "avg_roic_last5y": avg_roic_5y,
                "terminal_fcf_bn": normalized_terminal_fcf,
                "explicit_year_terminal_fcf_bn": fcf[-1],
                "terminal_revenue_bn": revenue[-1],
            })
        return pd.DataFrame(rows)

    def _summary(
        self,
        global_df: pd.DataFrame,
        sector_df: pd.DataFrame,
        dcf_df: pd.DataFrame,
        scenario: Scenario,
    ) -> Dict[str, float]:
        cfg = self.config
        start_year = cfg.start_year
        horizon_end = cfg.start_year + cfg.horizon_years

        def totals_at(year: int) -> pd.Series:
            return sector_df[sector_df["year"] == year].sum(numeric_only=True)

        start_totals = totals_at(start_year)
        y5_totals = totals_at(min(start_year + 5, horizon_end))
        y10_totals = totals_at(min(start_year + 10, horizon_end))
        y20_totals = totals_at(horizon_end)

        total_market0 = sum(sec.market_cap0 for sec in self.sectors.values())
        total_dcf = float(dcf_df["dcf_ev_bn"].sum())
        aggregate_fair_value_to_market = total_dcf / max(total_market0, EPS)
        # If fair value is negative, market/fair is not economically meaningful;
        # use a capped distress diagnostic instead of an infinite ratio.
        aggregate_market_to_fair = total_market0 / total_dcf if total_dcf > EPS else 10.0
        total_multiple_value_y5 = float(y5_totals["multiple_based_value_bn"])
        total_multiple_value_y10 = float(y10_totals["multiple_based_value_bn"])
        total_revenue0 = float(start_totals["reported_revenue_bn"])
        total_revenue5 = float(y5_totals["reported_revenue_bn"])
        total_revenue10 = float(y10_totals["reported_revenue_bn"])
        total_revenue20 = float(y20_totals["reported_revenue_bn"])
        total_fcf5 = float(y5_totals["fcf_bn"])
        total_fcf10 = float(y10_totals["fcf_bn"])
        total_fcf20 = float(y20_totals["fcf_bn"])
        total_capex5 = float(y5_totals["capex_bn"])
        total_nopat20 = float(y20_totals["nopat_bn"])
        total_ic20 = float(y20_totals["invested_capital_bn"])

        # Revenue-quality weighted average.
        initial_sector = sector_df[sector_df["year"] == start_year]
        quality_weighted = float(np.average(
            initial_sector["quality_score"],
            weights=np.maximum(initial_sector["reported_revenue_bn"], EPS),
        ))
        low_quality_weighted = float(np.average(
            initial_sector["quality_low"],
            weights=np.maximum(initial_sector["reported_revenue_bn"], EPS),
        ))

        # Contract lag indicator: reported cloud-like revenue minus actual demand-linked revenue.
        cloud_like = sector_df[
            sector_df["sector"].isin(["ai_cloud_rental", "hyperscaler_cloud_ai", "enterprise_ai_software"])
        ]
        lag_df = cloud_like.groupby("year")[["reported_revenue_bn", "actual_revenue_bn"]].sum()
        contract_lag_ratio_y3 = 0.0
        if start_year + 3 in lag_df.index:
            contract_lag_ratio_y3 = float(
                (lag_df.loc[start_year + 3, "reported_revenue_bn"] - lag_df.loc[start_year + 3, "actual_revenue_bn"])
                / max(lag_df.loc[start_year + 3, "actual_revenue_bn"], EPS)
            )

        return {
            "scenario": scenario.name,
            "total_market_cap0_bn": total_market0,
            "total_dcf_ev_bn": total_dcf,
            "aggregate_fair_value_to_market": aggregate_fair_value_to_market,
            "aggregate_market_to_fair_value": aggregate_market_to_fair,
            "total_revenue0_bn": total_revenue0,
            "total_revenue5_bn": total_revenue5,
            "total_revenue10_bn": total_revenue10,
            "total_revenue20_bn": total_revenue20,
            "revenue_cagr_5y": cagr(total_revenue0, total_revenue5, 5),
            "revenue_cagr_10y": cagr(total_revenue0, total_revenue10, 10),
            "revenue_cagr_20y": cagr(total_revenue0, total_revenue20, 20),
            "total_fcf5_bn": total_fcf5,
            "total_fcf10_bn": total_fcf10,
            "total_fcf20_bn": total_fcf20,
            "fcf_margin5": total_fcf5 / max(total_revenue5, EPS),
            "fcf_margin10": total_fcf10 / max(total_revenue10, EPS),
            "fcf_margin20": total_fcf20 / max(total_revenue20, EPS),
            "total_capex5_bn": total_capex5,
            "capex_to_revenue5": total_capex5 / max(total_revenue5, EPS),
            "roic20": total_nopat20 / max(total_ic20, EPS),
            "multiple_value_y5_bn": total_multiple_value_y5,
            "multiple_value_y10_bn": total_multiple_value_y10,
            "price_target_ratio_5y_vs_market0": total_multiple_value_y5 / max(total_market0, EPS),
            "price_target_ratio_10y_vs_market0": total_multiple_value_y10 / max(total_market0, EPS),
            "terminal_compute_utilization": float(global_df.iloc[-1]["utilization"]),
            "avg_utilization_5y": float(global_df.tail(5)["utilization"].mean()),
            "avg_overcapacity_5y": float(global_df.tail(5)["overcapacity_ratio"].mean()),
            "terminal_enterprise_adoption": float(global_df.iloc[-1]["enterprise_adoption"]),
            "terminal_consumer_adoption": float(global_df.iloc[-1]["consumer_adoption"]),
            "terminal_token_volume_index": float(global_df.iloc[-1]["token_volume_index"]),
            "terminal_price_index": float(global_df.iloc[-1]["price_index"]),
            "terminal_compute_demand_index": float(global_df.iloc[-1]["compute_demand_index"]),
            "terminal_compute_capacity_index": float(global_df.iloc[-1]["compute_capacity_index"]),
            "avg_net_productivity_benefit_5y": float(global_df.tail(5)["net_productivity_benefit_ratio"].mean()),
            "terminal_enterprise_roi": float(global_df.iloc[-1]["enterprise_roi"]),
            "initial_quality_score_weighted": quality_weighted,
            "initial_low_quality_revenue_share_weighted": low_quality_weighted,
            "contract_lag_ratio_y3": contract_lag_ratio_y3,
            "onsite_net_delta_vs_grid_bn": float(global_df.iloc[0]["onsite_net_delta_vs_grid_bn"]),
        }

    def _bubble_score(
        self,
        summary: Mapping[str, float],
        scenario: Scenario,
    ) -> float:
        cfg = self.config
        valuation_excess = min(max(0.0, summary["aggregate_market_to_fair_value"] - 1.0), 5.0)
        overbuild = max(0.0, summary["avg_overcapacity_5y"])
        low_quality = summary["initial_low_quality_revenue_share_weighted"]
        fcf_penalty = max(0.0, -summary["fcf_margin5"])
        rate_penalty = max(0.0, (cfg.risk_free_rate + scenario.wacc_spread_add) - 0.035) / 0.05
        reflexivity = scenario.capex_reflexivity * scenario.valuation_multiple_multiplier
        score = (
            cfg.bubble_weight_valuation * valuation_excess
            + cfg.bubble_weight_overbuild * overbuild
            + cfg.bubble_weight_revenue_quality * low_quality
            + cfg.bubble_weight_fcf * fcf_penalty
            + cfg.bubble_weight_rates * rate_penalty
            + cfg.bubble_weight_reflexivity * reflexivity
        )
        return float(score)

    def _outcome_probabilities(
        self,
        global_df: pd.DataFrame,
        sector_df: pd.DataFrame,
        dcf_df: pd.DataFrame,
        scenario: Scenario,
        summary: Mapping[str, float],
    ) -> Dict[str, float]:
        """
        Reduced-form outcome classifier.

        This is intentionally transparent and calibratable. It maps financial
        state variables into probabilities for four broad regimes.
        """
        bubble = self._bubble_score(summary, scenario)
        valuation_excess = min(max(0.0, summary["aggregate_market_to_fair_value"] - 1.0), 5.0)
        overbuild = summary["avg_overcapacity_5y"]
        fcf_margin = summary["fcf_margin5"]
        productivity = summary["avg_net_productivity_benefit_5y"]
        adoption = summary["terminal_enterprise_adoption"]
        contract_lag = max(0.0, summary["contract_lag_ratio_y3"])
        price_comp = scenario.china_price_compression + scenario.open_source_pressure
        elasticity_bonus = max(0.0, scenario.demand_elasticity - 1.0)
        roic_spread = summary["roic20"] - 0.09

        scores = {
            "rapid_dotcom_style_burst": (
                0.30
                + 1.80 * valuation_excess
                + 1.25 * overbuild
                + 0.70 * max(0.0, -fcf_margin)
                + 0.45 * price_comp
                - 1.20 * productivity
                - 0.35 * adoption
            ),
            "gradual_valuation_deflation": (
                0.65
                + 0.80 * bubble
                + 0.65 * price_comp
                + 0.55 * contract_lag
                + 0.35 * max(0.0, fcf_margin)
                - 0.45 * max(0.0, -fcf_margin)
            ),
            "japan_style_prolonged_stagnation": (
                0.20
                + 0.90 * overbuild
                + 0.55 * max(0.0, -roic_spread)
                + 0.45 * scenario.stranded_asset_penalty
                + 0.40 * max(0.0, -summary["revenue_cagr_10y"])
                - 0.55 * productivity
            ),
            "productivity_led_expansion": (
                0.25
                + 1.60 * productivity
                + 0.70 * elasticity_bonus
                + 0.55 * adoption
                + 0.35 * max(0.0, fcf_margin)
                - 0.55 * price_comp
                - 0.60 * overbuild
            ),
        }
        probs = softmax(scores)
        # Keep the bubble score available as a pseudo-probability-like diagnostic.
        probs["bubble_score_diagnostic"] = bubble
        return probs

    # ---------------- Sector endpoint outcome matrix tools -------------------

    def _degree_to_outcome(self, degree: float) -> str:
        """Map the continuous crash-to-boom degree index to an ordered label."""
        if degree <= -90:
            return "complete_severe_crash"
        if degree <= -65:
            return "severe_crash"
        if degree <= -40:
            return "moderate_crash"
        if degree <= -10:
            return "valuation_deflation"
        if degree <= 15:
            return "prolonged_stagnation"
        if degree <= 55:
            return "resilient_compounding"
        return "booming_expansion"

    def endpoint_outcome_probabilities(
        self,
        value_ratio: float,
        revenue_cagr: float,
        fcf_margin: float,
        roic_spread: float,
        capex_to_revenue: float,
    ) -> Dict[str, float]:
        """
        Convert sector terminal metrics into a probability distribution across
        ordered endpoint states.

        Inputs:
          value_ratio     = endpoint multiple-based sector value / starting market value
          revenue_cagr    = revenue CAGR from start year to endpoint horizon
          fcf_margin      = endpoint FCF / endpoint revenue
          roic_spread     = endpoint ROIC - WACC
          capex_to_revenue= endpoint CapEx / endpoint revenue

        This is a transparent reduced-form classifier, not a trained model.
        Replace centers/widths with calibrated historical data if available.
        """
        vr = clip(value_ratio, 0.01, 8.0)
        log_v = math.log(vr)
        g = clip(revenue_cagr, -0.50, 0.80)
        f = clip(fcf_margin, -1.00, 1.00)
        r = clip(roic_spread, -0.50, 0.50)
        k = clip(capex_to_revenue, 0.00, 2.00)

        # Centers: (value ratio, revenue CAGR, FCF margin, log-value width, growth width, FCF width).
        centers = {
            "complete_severe_crash": (0.05, -0.20, -0.20, 0.70, 0.18, 0.35),
            "severe_crash": (0.25, -0.10, -0.05, 0.60, 0.14, 0.25),
            "moderate_crash": (0.55, -0.03, 0.00, 0.45, 0.10, 0.18),
            "valuation_deflation": (0.82, 0.04, 0.04, 0.35, 0.08, 0.16),
            "prolonged_stagnation": (1.00, 0.01, 0.03, 0.40, 0.05, 0.14),
            "resilient_compounding": (1.35, 0.08, 0.08, 0.45, 0.08, 0.15),
            "booming_expansion": (2.50, 0.18, 0.12, 0.70, 0.15, 0.18),
        }
        scores: Dict[str, float] = {}
        for outcome, (v_center, g_center, f_center, v_width, g_width, f_width) in centers.items():
            scores[outcome] = (
                gaussian_score(log_v, math.log(v_center), v_width)
                + gaussian_score(g, g_center, g_width)
                + 0.55 * gaussian_score(f, f_center, f_width)
            )

        # Fundamental modifiers.
        if vr < 0.15 or (g < -0.10 and f < 0):
            scores["complete_severe_crash"] += 1.50
        if vr < 0.40 or g < -0.05:
            scores["severe_crash"] += 0.95
        if vr < 0.70:
            scores["moderate_crash"] += 0.55
        if 0.60 <= vr <= 1.05 and g > 0.00:
            scores["valuation_deflation"] += 0.75
        if abs(g) < 0.035 and 0.65 <= vr <= 1.30:
            scores["prolonged_stagnation"] += 0.90
        if vr > 1.05 and g > 0.035 and f > 0.00:
            scores["resilient_compounding"] += 0.85
        if vr > 2.00 and g > 0.10 and f > 0.00:
            scores["booming_expansion"] += 1.25

        # ROIC/WACC and overbuild modifiers.
        if r < 0:
            scores["complete_severe_crash"] += 0.40 * min(abs(r) / 0.10, 3.0)
            scores["severe_crash"] += 0.35 * min(abs(r) / 0.10, 3.0)
            scores["prolonged_stagnation"] += 0.45 * min(abs(r) / 0.10, 3.0)
            scores["resilient_compounding"] -= 0.50 * min(abs(r) / 0.10, 3.0)
            scores["booming_expansion"] -= 0.80 * min(abs(r) / 0.10, 3.0)
        else:
            scores["resilient_compounding"] += 0.30 * min(r / 0.10, 3.0)
            scores["booming_expansion"] += 0.35 * min(r / 0.10, 3.0)

        if k > 0.35 and f < 0:
            overbuild_penalty = min((k - 0.35) / 0.30, 3.0)
            scores["complete_severe_crash"] += 0.35 * overbuild_penalty
            scores["severe_crash"] += 0.45 * overbuild_penalty
            scores["valuation_deflation"] += 0.25 * overbuild_penalty
            scores["booming_expansion"] -= 0.50 * overbuild_penalty

        return softmax(scores)

    def _endpoint_rule_label(
        self,
        value_ratio: float,
        revenue_cagr: float,
        fcf_margin: float,
        roic_spread: float,
        capex_to_revenue: float,
    ) -> str:
        """Deterministic rule label to accompany probabilistic endpoint scores."""
        if value_ratio <= 0.15 or (revenue_cagr <= -0.10 and fcf_margin < 0):
            return "complete_severe_crash"
        if value_ratio <= 0.40 or revenue_cagr <= -0.05 or (fcf_margin < -0.15 and capex_to_revenue > 0.50):
            return "severe_crash"
        if value_ratio <= 0.70:
            return "moderate_crash"
        if value_ratio <= 0.95:
            return "valuation_deflation"
        if (abs(revenue_cagr) <= 0.03 and value_ratio <= 1.20) or (roic_spread < 0 and revenue_cagr < 0.05):
            return "prolonged_stagnation"
        if value_ratio >= 2.00 and revenue_cagr >= 0.10 and fcf_margin >= 0:
            return "booming_expansion"
        if value_ratio >= 1.05 and revenue_cagr >= 0.03 and fcf_margin >= 0:
            return "resilient_compounding"
        return "prolonged_stagnation"

    def sector_endpoint_matrix(
        self,
        scenarios: Optional[Iterable[Scenario]] = None,
        horizons: Sequence[int] = (5, 10, 20),
    ) -> pd.DataFrame:
        """
        Build the requested sector endpoint matrix.

        Rows contain one sector x scenario x horizon endpoint with:
          * rule label;
          * probability label;
          * crash-to-boom degree score;
          * probabilities for all endpoint outcomes;
          * underlying financial metrics.
        """
        scenario_list = list(scenarios) if scenarios is not None else list(named_scenarios().values())
        rows: List[Dict[str, float]] = []
        for scen in scenario_list:
            result = self.simulate(scen)
            sector_df = result["sector"]
            for horizon in horizons:
                target_year = self.config.start_year + horizon
                if target_year > self.config.start_year + self.config.horizon_years:
                    continue
                target = sector_df[sector_df["year"] == target_year]
                for _, row in target.iterrows():
                    sec = self.sectors[str(row["sector"])]
                    revenue = float(row["reported_revenue_bn"])
                    value_ratio = float(row["multiple_based_value_bn"] / max(sec.market_cap0, EPS))
                    revenue_cagr = cagr(sec.revenue0, revenue, horizon)
                    fcf_margin = float(row["fcf_bn"] / max(revenue, EPS))
                    roic_spread = float(row["roic"] - (sec.wacc + scen.wacc_spread_add))
                    capex_to_revenue = float(row["capex_bn"] / max(revenue, EPS))
                    sales_multiple_change = float(row["ev_sales_multiple"] / max(sec.base_ev_sales_multiple, EPS) - 1.0)
                    probs = self.endpoint_outcome_probabilities(
                        value_ratio=value_ratio,
                        revenue_cagr=revenue_cagr,
                        fcf_margin=fcf_margin,
                        roic_spread=roic_spread,
                        capex_to_revenue=capex_to_revenue,
                    )
                    probabilistic_label = max(OUTCOME_ORDER, key=lambda k: probs[k])
                    rule_label = self._endpoint_rule_label(
                        value_ratio=value_ratio,
                        revenue_cagr=revenue_cagr,
                        fcf_margin=fcf_margin,
                        roic_spread=roic_spread,
                        capex_to_revenue=capex_to_revenue,
                    )
                    degree = sum(probs[k] * OUTCOME_DEGREE_SCORE[k] for k in OUTCOME_ORDER)
                    degree_label = self._degree_to_outcome(degree)
                    outrow = {
                        "scenario": scen.name,
                        "scenario_probability_weight": scen.probability_weight,
                        "horizon_years": horizon,
                        "endpoint_year": target_year,
                        "sector": sec.name,
                        "endpoint_label_rule": rule_label,
                        "endpoint_label_probability": probabilistic_label,
                        "endpoint_label_final": degree_label,
                        "endpoint_label_short": OUTCOME_LABEL_SHORT[degree_label],
                        "endpoint_degree_index": degree,
                        "endpoint_cell": f"{OUTCOME_LABEL_SHORT[degree_label]} ({degree:+.0f})",
                        "endpoint_value_ratio_vs_start": value_ratio,
                        "endpoint_drawdown_pct_if_below_start": max(0.0, 1.0 - value_ratio),
                        "endpoint_upside_pct_if_above_start": max(0.0, value_ratio - 1.0),
                        "endpoint_revenue_cagr": revenue_cagr,
                        "endpoint_reported_revenue_bn": revenue,
                        "endpoint_fcf_bn": float(row["fcf_bn"]),
                        "endpoint_fcf_margin": fcf_margin,
                        "endpoint_roic": float(row["roic"]),
                        "endpoint_roic_spread_vs_wacc": roic_spread,
                        "endpoint_capex_to_revenue": capex_to_revenue,
                        "endpoint_ev_sales_multiple": float(row["ev_sales_multiple"]),
                        "endpoint_sales_multiple_change": sales_multiple_change,
                    }
                    for k in OUTCOME_ORDER:
                        outrow[f"prob_{k}"] = probs[k]
                    rows.append(outrow)
        return pd.DataFrame(rows)

    def probability_weighted_sector_endpoint_matrix(
        self,
        horizons: Sequence[int] = (5, 10, 20),
    ) -> pd.DataFrame:
        """
        Probability-weighted sector matrix using named_scenarios() weights.

        Output rows are sector x horizon. Columns contain weighted probabilities
        for complete crash, severe crash, stagnation, deflation, and boom states.
        """
        endpoints = self.sector_endpoint_matrix(horizons=horizons)
        rows: List[Dict[str, float]] = []
        for (sector, horizon), grp in endpoints.groupby(["sector", "horizon_years"]):
            w = grp["scenario_probability_weight"].to_numpy(dtype=float)
            wsum = float(w.sum()) if float(w.sum()) > 0 else 1.0
            weighted_probs = {}
            for outcome in OUTCOME_ORDER:
                weighted_probs[f"weighted_prob_{outcome}"] = float((grp[f"prob_{outcome}"].to_numpy(dtype=float) * w).sum() / wsum)
            expected_degree = float((grp["endpoint_degree_index"].to_numpy(dtype=float) * w).sum() / wsum)
            weighted_value_ratio = float((grp["endpoint_value_ratio_vs_start"].to_numpy(dtype=float) * w).sum() / wsum)
            weighted_revenue_cagr = float((grp["endpoint_revenue_cagr"].to_numpy(dtype=float) * w).sum() / wsum)
            weighted_fcf_margin = float((grp["endpoint_fcf_margin"].to_numpy(dtype=float) * w).sum() / wsum)
            highest_probability_label = max(OUTCOME_ORDER, key=lambda k: weighted_probs[f"weighted_prob_{k}"])
            degree_label = self._degree_to_outcome(expected_degree)
            row = {
                "sector": sector,
                "horizon_years": int(horizon),
                "endpoint_label_highest_probability_weighted": highest_probability_label,
                "endpoint_label_final_weighted": degree_label,
                "endpoint_label_short": OUTCOME_LABEL_SHORT[degree_label],
                "endpoint_degree_index_weighted": expected_degree,
                "endpoint_cell_weighted": f"{OUTCOME_LABEL_SHORT[degree_label]} ({expected_degree:+.0f})",
                "weighted_value_ratio_vs_start": weighted_value_ratio,
                "weighted_revenue_cagr": weighted_revenue_cagr,
                "weighted_fcf_margin": weighted_fcf_margin,
            }
            row.update(weighted_probs)
            rows.append(row)
        return pd.DataFrame(rows)

    def sector_endpoint_pivot(
        self,
        horizon: int = 10,
        scenarios: Optional[Iterable[Scenario]] = None,
    ) -> pd.DataFrame:
        """Readable sector x scenario matrix for a single endpoint horizon."""
        endpoints = self.sector_endpoint_matrix(scenarios=scenarios, horizons=(horizon,))
        pivot = endpoints.pivot(index="sector", columns="scenario", values="endpoint_cell").reset_index()
        return pivot

    # ---------------------- Scenario / sensitivity tools ----------------------

    def run_named_scenarios(self) -> pd.DataFrame:
        rows = []
        for scen in named_scenarios().values():
            result = self.simulate(scen)
            rows.append(result["summary"])
        return pd.DataFrame(rows)

    def make_perspective_scenario(self, flags: Sequence[str]) -> Scenario:
        """
        Build scenarios for Perspective A-E combinations.

        A: Agentic TCO/regulatory friction.
        B: PPP/global pricing competition.
        C: Physical infrastructure stranding.
        D: Enterprise contract renewal cliff.
        E: Valuation multiple compression.
        """
        scen = named_scenarios()["baseline_gradual_deflation"]
        name_parts = list(flags) if flags else ["none"]
        scen = replace(scen, name="perspective_" + "+".join(name_parts))

        if "A" in flags:
            scen = replace(
                scen,
                tco_multiplier=max(scen.tco_multiplier, 2.20),
                regulated_compliance_multiplier=max(scen.regulated_compliance_multiplier, 1.45),
                agent_autonomy_risk=max(scen.agent_autonomy_risk, 0.60),
                productivity_capture=max(0.10, scen.productivity_capture - 0.06),
            )
        if "B" in flags:
            scen = replace(
                scen,
                china_price_compression=max(scen.china_price_compression, 0.55),
                open_source_pressure=max(scen.open_source_pressure, 0.50),
                ppp_cost_advantage=max(scen.ppp_cost_advantage, 0.60),
                valuation_multiple_multiplier=scen.valuation_multiple_multiplier * 0.90,
            )
        if "C" in flags:
            scen = replace(
                scen,
                power_growth_cap=min(scen.power_growth_cap or 0.32, 0.22),
                construction_growth_cap=min(scen.construction_growth_cap or 0.35, 0.24),
                silicon_growth_cap=min(scen.silicon_growth_cap or 0.45, 0.34),
                infrastructure_speed=min(scen.infrastructure_speed, 0.75),
                committed_capex_overbuild=max(scen.committed_capex_overbuild, 0.08),
                stranded_asset_penalty=max(scen.stranded_asset_penalty, 0.07),
                gas_price_per_mmbtu=max(scen.gas_price_per_mmbtu, 5.5),
            )
        if "D" in flags:
            scen = replace(
                scen,
                renewal_downsize=max(scen.renewal_downsize, 0.34),
                renewal_rate=min(scen.renewal_rate, 0.62),
                contract_mix_override=0.78,
                demand_shock=min(scen.demand_shock, -0.03),
            )
        if "E" in flags:
            scen = replace(
                scen,
                valuation_multiple_multiplier=scen.valuation_multiple_multiplier * 0.58,
                wacc_spread_add=scen.wacc_spread_add + 0.015,
                sentiment_decay=max(scen.sentiment_decay, 0.08),
            )
        return scen

    def run_perspective_matrix(self) -> pd.DataFrame:
        flags_all = ["A", "B", "C", "D", "E"]
        flag_sets: List[Tuple[str, ...]] = [tuple()]
        for r in range(1, len(flags_all) + 1):
            flag_sets.extend(list(combinations(flags_all, r)))

        rows = []
        for flags in flag_sets:
            scen = self.make_perspective_scenario(flags)
            res = self.simulate(scen)
            row = dict(res["summary"])
            row["flags"] = "+".join(flags) if flags else "none"
            rows.append(row)
        return pd.DataFrame(rows)

    def monte_carlo(self, n: int = 500, seed: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Monte Carlo uncertainty around core levers.

        The distributions below are deliberately simple and editable. Replace
        them with calibrated priors/posteriors from empirical data.
        """
        rng = np.random.default_rng(seed)
        rows = []
        outcome_rows = []
        base = named_scenarios()["baseline_gradual_deflation"]

        for i in range(n):
            recession_draw = rng.choice([0.0, -0.05, -0.12], p=[0.74, 0.20, 0.06])
            scen = replace(
                base,
                name=f"mc_{i:04d}",
                organic_token_growth=clip(rng.normal(0.22, 0.10), -0.05, 0.55),
                demand_elasticity=clip(rng.normal(1.05, 0.30), 0.25, 1.90),
                inference_cost_decline=clip(rng.normal(0.28, 0.08), 0.05, 0.55),
                compute_per_token_decline=clip(rng.normal(0.25, 0.08), 0.03, 0.55),
                price_pass_through=clip(rng.normal(0.65, 0.15), 0.20, 0.95),
                productivity_gross_gain=clip(rng.normal(0.09, 0.04), 0.00, 0.22),
                productivity_capture=clip(rng.normal(0.30, 0.10), 0.05, 0.60),
                enterprise_agent_intensity=clip(rng.normal(0.25, 0.15), 0.00, 0.70),
                tco_multiplier=clip(rng.triangular(1.0, 1.45, 3.0), 1.0, 3.5),
                regulated_compliance_multiplier=clip(rng.normal(1.0, 0.25), 0.70, 1.90),
                china_price_compression=clip(rng.beta(2.0, 3.0), 0.02, 0.90),
                open_source_pressure=clip(rng.beta(2.0, 3.0), 0.02, 0.90),
                ppp_cost_advantage=clip(rng.normal(0.35, 0.15), 0.0, 0.80),
                silicon_growth_cap=clip(rng.normal(0.45, 0.10), 0.12, 0.75),
                power_growth_cap=clip(rng.normal(0.32, 0.09), 0.08, 0.65),
                construction_growth_cap=clip(rng.normal(0.35, 0.10), 0.10, 0.75),
                infrastructure_speed=clip(rng.normal(1.0, 0.20), 0.45, 1.55),
                capex_reflexivity=clip(rng.normal(0.50, 0.20), 0.05, 1.10),
                committed_capex_overbuild=clip(rng.normal(0.03, 0.03), 0.00, 0.14),
                renewal_downsize=clip(rng.beta(2.0, 5.0), 0.00, 0.70),
                renewal_rate=clip(rng.normal(0.82, 0.12), 0.35, 0.98),
                valuation_multiple_multiplier=clip(rng.lognormal(mean=math.log(0.85), sigma=0.35), 0.25, 1.80),
                wacc_spread_add=clip(rng.normal(0.0, 0.012), -0.020, 0.040),
                sentiment_decay=clip(rng.normal(0.03, 0.03), 0.0, 0.15),
                recession_shock=recession_draw,
                gas_price_per_mmbtu=clip(rng.lognormal(mean=math.log(4.0), sigma=0.35), 1.5, 12.0),
                carbon_price_per_ton=clip(rng.normal(10.0, 20.0), 0.0, 100.0),
            )
            res = self.simulate(scen)
            summary = dict(res["summary"])
            summary["path"] = i
            rows.append(summary)
            probs = dict(res["outcome_probabilities"])
            probs["path"] = i
            outcome_rows.append(probs)

        mc_df = pd.DataFrame(rows)
        probs_df = pd.DataFrame(outcome_rows)

        quantile_cols = [
            "aggregate_fair_value_to_market",
            "revenue_cagr_10y",
            "fcf_margin10",
            "capex_to_revenue5",
            "avg_overcapacity_5y",
            "terminal_enterprise_adoption",
            "terminal_token_volume_index",
            "terminal_compute_utilization",
            "price_target_ratio_5y_vs_market0",
            "price_target_ratio_10y_vs_market0",
            "prob_rapid_dotcom_style_burst",
            "prob_gradual_valuation_deflation",
            "prob_japan_style_prolonged_stagnation",
            "prob_productivity_led_expansion",
        ]
        quantile_cols = [c for c in quantile_cols if c in mc_df.columns]
        q = mc_df[quantile_cols].quantile([0.05, 0.25, 0.50, 0.75, 0.95]).T.reset_index()
        q.columns = ["metric", "p05", "p25", "p50", "p75", "p95"]
        return mc_df, q

    def sensitivity_table(
        self,
        parameter: str,
        values: Sequence[float],
        base_scenario: Optional[Scenario] = None,
    ) -> pd.DataFrame:
        """One-way sensitivity table for any Scenario field."""
        base = base_scenario or named_scenarios()["baseline_gradual_deflation"]
        rows = []
        if not hasattr(base, parameter):
            raise AttributeError(f"Scenario has no field {parameter!r}")
        for v in values:
            scen = replace(base, **{parameter: v}, name=f"sens_{parameter}_{v}")
            rows.append(self.simulate(scen)["summary"])
        return pd.DataFrame(rows)

    def dotcom_comparison_scorecard(self, scenario: Scenario) -> pd.DataFrame:
        """
        Stylized dot-com vs AI scorecard.

        For rigorous use, replace dotcom_benchmark values with historical cohort
        data: IPO revenue/profitability, P/S, FCF margins, VC financing, rates,
        capex/fiber overbuild, market concentration, etc.
        """
        res = self.simulate(scenario)
        summary = res["summary"]
        sector = res["sector"]
        dcf = res["dcf"]
        start_sector = sector[sector["year"] == self.config.start_year]

        ai_metrics = {
            "market_to_fair_value": summary["aggregate_market_to_fair_value"],
            "weighted_low_quality_revenue_share": summary["initial_low_quality_revenue_share_weighted"],
            "fcf_margin_5y": summary["fcf_margin5"],
            "capex_to_revenue_5y": summary["capex_to_revenue5"],
            "avg_overcapacity_5y": summary["avg_overcapacity_5y"],
            "revenue_cagr_5y": summary["revenue_cagr_5y"],
            "market_concentration_top3_share": self._top_n_revenue_share(start_sector, n=3),
            "profitable_revenue_share_start": self._profitable_revenue_share(start_sector),
        }
        # Stylized normalized dot-com benchmark placeholders.
        dotcom_benchmark = {
            "market_to_fair_value": 2.20,
            "weighted_low_quality_revenue_share": 0.45,
            "fcf_margin_5y": -0.12,
            "capex_to_revenue_5y": 0.35,
            "avg_overcapacity_5y": 0.40,
            "revenue_cagr_5y": 0.10,
            "market_concentration_top3_share": 0.28,
            "profitable_revenue_share_start": 0.25,
        }
        rows = []
        for metric, ai_value in ai_metrics.items():
            dot_value = dotcom_benchmark[metric]
            if abs(dot_value) < EPS:
                ratio = np.nan
            else:
                ratio = ai_value / dot_value
            rows.append({
                "metric": metric,
                "ai_model_value": ai_value,
                "stylized_dotcom_benchmark": dot_value,
                "ai_to_dotcom_ratio": ratio,
            })
        return pd.DataFrame(rows)

    @staticmethod
    def _top_n_revenue_share(sector_start_df: pd.DataFrame, n: int = 3) -> float:
        rev = sector_start_df["reported_revenue_bn"].sort_values(ascending=False)
        return float(rev.head(n).sum() / max(rev.sum(), EPS))

    @staticmethod
    def _profitable_revenue_share(sector_start_df: pd.DataFrame) -> float:
        profitable = sector_start_df[sector_start_df["ebit_bn"] > 0]
        return float(profitable["reported_revenue_bn"].sum() / max(sector_start_df["reported_revenue_bn"].sum(), EPS))


# -----------------------------------------------------------------------------
# Reporting helpers
# -----------------------------------------------------------------------------

def write_outputs(output_dir: str = "tesm_outputs", monte_carlo_paths: int = 500) -> None:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    model = TESMModel()

    scenario_rows = []
    baseline_result = None
    for scen in named_scenarios().values():
        result = model.simulate(scen)
        scenario_rows.append(result["summary"])
        if scen.name == "baseline_gradual_deflation":
            baseline_result = result
    scenario_summary = pd.DataFrame(scenario_rows)
    scenario_summary.to_csv(out / "scenario_summary.csv", index=False)

    if baseline_result is not None:
        baseline_result["sector"].to_csv(out / "sector_financials_baseline.csv", index=False)
        baseline_result["global"].to_csv(out / "global_metrics_baseline.csv", index=False)
        baseline_result["dcf"].to_csv(out / "dcf_baseline.csv", index=False)
        scorecard = model.dotcom_comparison_scorecard(named_scenarios()["baseline_gradual_deflation"])
        scorecard.to_csv(out / "dotcom_comparison_scorecard.csv", index=False)

    # Endpoint sector matrices: complete crash -> severe crash -> deflation ->
    # stagnation -> resilient/booming outcomes by sector and scenario.
    sector_endpoint_matrix = model.sector_endpoint_matrix(horizons=(5, 10, 20))
    sector_endpoint_matrix.to_csv(out / "sector_endpoint_matrix.csv", index=False)
    sector_endpoint_pivot_10y = model.sector_endpoint_pivot(horizon=10)
    sector_endpoint_pivot_10y.to_csv(out / "sector_endpoint_pivot_10y.csv", index=False)
    weighted_sector_endpoint = model.probability_weighted_sector_endpoint_matrix(horizons=(5, 10, 20))
    weighted_sector_endpoint.to_csv(out / "sector_endpoint_probability_weighted.csv", index=False)

    perspective_matrix = model.run_perspective_matrix()
    perspective_matrix.to_csv(out / "perspective_matrix.csv", index=False)

    mc_paths, mc_summary = model.monte_carlo(n=monte_carlo_paths)
    mc_summary.to_csv(out / "monte_carlo_summary.csv", index=False)
    # Save only essential MC path values to keep file compact.
    keep_cols = [
        "path",
        "aggregate_fair_value_to_market",
        "aggregate_market_to_fair_value",
        "revenue_cagr_10y",
        "fcf_margin10",
        "capex_to_revenue5",
        "avg_overcapacity_5y",
        "terminal_enterprise_adoption",
        "terminal_token_volume_index",
        "terminal_compute_utilization",
        "price_target_ratio_5y_vs_market0",
        "price_target_ratio_10y_vs_market0",
        "prob_rapid_dotcom_style_burst",
        "prob_gradual_valuation_deflation",
        "prob_japan_style_prolonged_stagnation",
        "prob_productivity_led_expansion",
    ]
    keep_cols = [c for c in keep_cols if c in mc_paths.columns]
    mc_paths[keep_cols].to_csv(out / "monte_carlo_paths_compact.csv", index=False)

    # Sensitivity examples.
    model.sensitivity_table(
        "demand_elasticity", values=[0.40, 0.70, 1.00, 1.30, 1.60]
    ).to_csv(out / "sensitivity_demand_elasticity.csv", index=False)
    model.sensitivity_table(
        "tco_multiplier", values=[1.0, 1.5, 2.0, 2.5, 3.0]
    ).to_csv(out / "sensitivity_tco_multiplier.csv", index=False)
    model.sensitivity_table(
        "china_price_compression", values=[0.10, 0.25, 0.40, 0.60, 0.80]
    ).to_csv(out / "sensitivity_china_price_compression.csv", index=False)

    readme = f"""# AI TESM Core Financial Model Outputs

Generated by `ai_tesm_core_financial_model.py`.

## Important
These outputs use illustrative default assumptions embedded in the Python file.
Replace default sector values and scenario parameters with calibrated public data
before treating results as empirical forecasts.

## Files
- `scenario_summary.csv`: optimistic, baseline, pessimistic, stress scenarios.
- `sector_financials_baseline.csv`: sector-level annual financial statements for baseline.
- `global_metrics_baseline.csv`: adoption, token demand, efficiency, capex, utilization for baseline.
- `dcf_baseline.csv`: baseline sector DCF valuation.
- `perspective_matrix.csv`: all A-E perspective combinations.
- `monte_carlo_summary.csv`: p05/p25/p50/p75/p95 uncertainty bands.
- `monte_carlo_paths_compact.csv`: path-level compact MC outputs.
- `dotcom_comparison_scorecard.csv`: stylized dot-com comparison placeholders.
- `sector_endpoint_matrix.csv`: sector x scenario x horizon endpoint outcomes, from complete crash to boom.
- `sector_endpoint_pivot_10y.csv`: readable 10-year sector x scenario outcome matrix.
- `sector_endpoint_probability_weighted.csv`: probability-weighted sector endpoint probabilities using scenario weights.
- `sensitivity_*.csv`: one-way sensitivity examples.

## Core equations
```text
Enterprise gross benefit = labor_share * exposed_labor_share * productivity_gain * capture * adoption_effect
Enterprise ROI = (gross_benefit - AI_cost - governance_cost) / (AI_cost + governance_cost)
Adoption[t+1] = adoption[t] + speed * adoption[t] * (1 - adoption[t]/max_penetration) * ROI_multiplier
Price decline = pass_through * inference_cost_decline + China/PPP pressure + open-source pressure - frontier premium
Token growth = organic + demand_shock + price_ratio^(-elasticity)-1 + adoption_growth + agent_growth
Compute demand = token_volume * compute_per_token + training_compute
Capacity growth <= min(silicon cap, power cap + onsite bonus, construction cap) * infrastructure_speed
Utilization = min(1, compute_demand / compute_capacity)
FCF = NOPAT + depreciation - capex - change_in_working_capital
DCF EV = sum(FCF_t/(1+WACC)^t) + terminal_FCF/(WACC-g)/(1+WACC)^T
```
"""
    (out / "README.md").write_text(readme, encoding="utf-8")

    print(f"Wrote outputs to {out.resolve()}")
    print("\nScenario summary:")
    display_cols = [
        "scenario",
        "aggregate_fair_value_to_market",
        "revenue_cagr_10y",
        "fcf_margin10",
        "capex_to_revenue5",
        "avg_overcapacity_5y",
        "prob_rapid_dotcom_style_burst",
        "prob_gradual_valuation_deflation",
        "prob_japan_style_prolonged_stagnation",
        "prob_productivity_led_expansion",
    ]
    display_cols = [c for c in display_cols if c in scenario_summary.columns]
    print(scenario_summary[display_cols].to_string(index=False))
    print("\n10-year sector endpoint matrix:")
    print(sector_endpoint_pivot_10y.to_string(index=False))


if __name__ == "__main__":
    write_outputs(monte_carlo_paths=500)
