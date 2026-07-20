"""
AI TESM - OOP / SOLID implementation
------------------------------------
This file refactors the original core mathematical financial model into a more
maintainable object-oriented architecture.

SOLID mapping
    S - Single Responsibility:
        Each class owns one model function: ROI, adoption, pricing, demand,
        power, capacity, sector financials, valuation, outcomes, reporting.
    O - Open/Closed:
        New pricing/adoption/capacity/outcome logic can be added by implementing
        the small Protocol interfaces without editing the simulation engine.
    L - Liskov Substitution:
        Any implementation of the Protocols can replace the defaults.
    I - Interface Segregation:
        Components depend on small, specific Protocols rather than one giant API.
    D - Dependency Inversion:
        TESMSimulationEngine depends on abstractions injected at construction.

Run
    python3 ai_tesm_solid_oop_model.py

Outputs
    ./tesm_solid_outputs/scenario_summary.csv
    ./tesm_solid_outputs/sector_financials_baseline.csv
    ./tesm_solid_outputs/global_metrics_baseline.csv
    ./tesm_solid_outputs/dcf_baseline.csv
    ./tesm_solid_outputs/sector_endpoint_matrix.csv
    ./tesm_solid_outputs/sector_endpoint_pivot_10y.csv
    ./tesm_solid_outputs/sector_endpoint_probability_weighted.csv
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional, Protocol, Sequence, Tuple

import math
import numpy as np
import pandas as pd

# Reuse the domain dataclasses/default assumptions from the existing model.
# The OOP/SOLID implementation below does not call TESMModel; it composes its
# own components around these domain objects.
from ai_tesm_core_financial_model import (  # noqa: E402
    EPS,
    ModelConfig,
    Scenario,
    SectorParams,
    OUTCOME_DEGREE_SCORE,
    OUTCOME_LABEL_SHORT,
    OUTCOME_ORDER,
    cagr,
    clip,
    default_sectors,
    gaussian_score,
    named_scenarios,
    pv_factor,
    sigmoid,
    softmax,
)


# -----------------------------------------------------------------------------
# Repository abstractions - DIP: engine/reporting load data through interfaces
# -----------------------------------------------------------------------------

class SectorRepository(Protocol):
    def load_sectors(self) -> Dict[str, SectorParams]:
        """Return sector parameter objects keyed by sector name."""


class ScenarioRepository(Protocol):
    def load_scenarios(self) -> Dict[str, Scenario]:
        """Return scenario objects keyed by scenario name."""


class ConfigRepository(Protocol):
    def load_config(self) -> ModelConfig:
        """Return model configuration."""


class DefaultSectorRepository:
    def load_sectors(self) -> Dict[str, SectorParams]:
        return default_sectors()


class DefaultScenarioRepository:
    def load_scenarios(self) -> Dict[str, Scenario]:
        return named_scenarios()


class DefaultConfigRepository:
    def load_config(self) -> ModelConfig:
        return ModelConfig()


class DuckDBConfigRepository:
    def __init__(self, db_path: str = "databases/master_consolidated.duckdb"):
        self.db_path = db_path

    def load_config(self) -> ModelConfig:
        import duckdb
        conn = duckdb.connect(self.db_path, read_only=True)
        rows = conn.execute("SELECT parameter_name, calibrated_value FROM calibration_parameters").fetchall()
        params = {r[0]: float(r[1]) for r in rows}
        conn.close()
        
        return ModelConfig(
            horizon_years=int(params.get("horizon", 20)),
            default_power_growth_cap=params.get("powerGrowthCap", 0.32),
            grid_delay_years=params.get("gridConnectionDelay", 8.0) / 4.0,
            avg_contract_length_years=params.get("averageContractLength", 12.0) / 4.0,
            contract_mix=params.get("contractMix3yr", 0.70),
            onsite_gen_capacity_mw=params.get("onsiteGenCapacityMW", 2500.0),
            onsite_capacity_factor=params.get("onsiteCapacityFactor", 0.75),
            onsite_hedge_ratio=params.get("hedgeRatio", 0.65),
            grid_services_revenue_per_mw_year=params.get("gridServicesRevenue", 25000.0),
            grid_power_price_per_mwh=51.33,
            gas_emissions_ton_per_mwh=params.get("carbonIntensityTonCO2perMWh", 0.40)
        )


class DuckDBSectorRepository:
    def __init__(self, db_path: str = "databases/master_consolidated.duckdb"):
        self.db_path = db_path

    def load_sectors(self) -> Dict[str, SectorParams]:
        import duckdb
        sectors = default_sectors()
        
        conn = duckdb.connect(self.db_path, read_only=True)
        rows = conn.execute("SELECT parameter_name, calibrated_value FROM calibration_parameters").fetchall()
        params = {r[0]: float(r[1]) for r in rows}
        conn.close()
        
        wacc_val = params.get("wacc", 0.085)
        multiple_val = params.get("baseMultipleSales", 8.0)
        
        for name in list(sectors.keys()):
            s = sectors[name]
            sectors[name] = replace(
                s,
                wacc=wacc_val if name != "frontier_model_providers" else wacc_val + 0.035,
                base_ev_sales_multiple=multiple_val if name in ["enterprise_ai_software", "ai_cloud_rental"] else s.base_ev_sales_multiple
            )
        return sectors


# -----------------------------------------------------------------------------
# Data transfer objects
# -----------------------------------------------------------------------------

@dataclass(frozen=True)
class RoiResult:
    gross_productivity_benefit_ratio: float
    ai_cost_ratio: float
    governance_cost_ratio: float
    net_productivity_benefit_ratio: float
    enterprise_roi: float


@dataclass(frozen=True)
class AdoptionSnapshot:
    enterprise: float
    consumer: float
    adoption_index: float


@dataclass(frozen=True)
class DemandSnapshot:
    token_volume: float
    price_index: float
    compute_per_token: float
    training_compute: float
    compute_demand: float
    actual_cloud_demand_index: float
    monetized_ai_spend_index: float
    adoption_index: float
    token_growth: float = 0.0
    price_decline: float = 0.0


@dataclass(frozen=True)
class CapacitySnapshot:
    compute_capacity: float
    utilization: float
    overcapacity_ratio: float
    global_capacity_capex: float
    allowed_capacity_growth: float


@dataclass(frozen=True)
class OnsitePowerResult:
    onsite_energy_mwh: float
    onsite_fuel_cost_bn: float
    onsite_carbon_cost_bn: float
    onsite_grid_services_revenue_bn: float
    onsite_grid_equivalent_cost_bn: float
    onsite_net_delta_vs_grid_bn: float
    onsite_power_growth_bonus: float

    def as_dict(self) -> Dict[str, float]:
        return self.__dict__.copy()


@dataclass(frozen=True)
class SectorState:
    actual_revenue: float
    reported_revenue: float
    revenue_growth: float
    ebit_margin: float
    ebit: float
    tax: float
    nopat: float
    capex: float
    depreciation: float
    fcf: float
    invested_capital: float
    roic: float
    ev_sales_multiple: float
    multiple_based_value: float


@dataclass(frozen=True)
class StepDrivers:
    year: int
    year_index: int
    scenario: Scenario
    price_decline: float
    competition_pressure: float
    regulated_cost_ratio: float
    net_productivity_benefit: float
    overcapacity_ratio: float
    global_capacity_capex: float
    capacity_growth_rate: float
    capex_growth: float
    cloud_demand_growth: float
    compute_growth: float
    monetized_demand_growth: float
    adoption_growth: float
    allowed_capacity_growth: float
    utilization: float
    power_margin_drag: float
    enterprise_roi: float


@dataclass(frozen=True)
class SimulationResult:
    scenario: Scenario
    global_df: pd.DataFrame
    sector_df: pd.DataFrame
    dcf_df: pd.DataFrame
    summary: Dict[str, float]
    outcome_probabilities: Dict[str, float]


# -----------------------------------------------------------------------------
# Component protocols - ISP: small interfaces for replaceable components
# -----------------------------------------------------------------------------

class EnterpriseRoiModel(Protocol):
    def compute(self, scenario: Scenario, enterprise_adoption_prev: float, price_index_prev: float) -> RoiResult:
        ...


class AdoptionModel(Protocol):
    def update(
        self,
        scenario: Scenario,
        enterprise_prev: float,
        consumer_prev: float,
        enterprise_roi: float,
        price_decline_rate: float,
    ) -> AdoptionSnapshot:
        ...


class PricingModel(Protocol):
    def annual_price_decline_rate(self, scenario: Scenario, year_index: int) -> float:
        ...


class DemandModel(Protocol):
    def next_demand(
        self,
        scenario: Scenario,
        previous: DemandSnapshot,
        previous_adoption: AdoptionSnapshot,
        current_adoption: AdoptionSnapshot,
        price_decline: float,
    ) -> DemandSnapshot:
        ...


class OnsitePowerModel(Protocol):
    def compute(self, scenario: Scenario) -> OnsitePowerResult:
        ...


class CapacityModel(Protocol):
    def initial_capacity(self) -> CapacitySnapshot:
        ...

    def next_capacity(
        self,
        scenario: Scenario,
        year_index: int,
        previous_capacity: CapacitySnapshot,
        compute_demand: float,
        token_growth: float,
        onsite_power_bonus: float,
    ) -> CapacitySnapshot:
        ...


class ContractLagPolicy(Protocol):
    def apply(
        self,
        year: int,
        prev_reported: float,
        actual_revenue: float,
        scenario: Scenario,
        enterprise_roi: float,
    ) -> float:
        ...


class SectorFinancialProjector(Protocol):
    def initial_state(self, sector: SectorParams) -> SectorState:
        ...

    def project(self, sector: SectorParams, previous: SectorState, drivers: StepDrivers) -> SectorState:
        ...


class ValuationModel(Protocol):
    def value(self, sector_df: pd.DataFrame, sectors: Mapping[str, SectorParams], scenario: Scenario) -> pd.DataFrame:
        ...


class SummaryModel(Protocol):
    def summarize(
        self,
        global_df: pd.DataFrame,
        sector_df: pd.DataFrame,
        dcf_df: pd.DataFrame,
        sectors: Mapping[str, SectorParams],
        scenario: Scenario,
    ) -> Dict[str, float]:
        ...


class AggregateOutcomeClassifier(Protocol):
    def probabilities(self, summary: Mapping[str, float], scenario: Scenario) -> Dict[str, float]:
        ...


class EndpointOutcomeClassifier(Protocol):
    def probabilities(
        self,
        value_ratio: float,
        revenue_cagr: float,
        fcf_margin: float,
        roic_spread: float,
        capex_to_revenue: float,
    ) -> Dict[str, float]:
        ...

    def label_from_degree(self, degree: float) -> str:
        ...


# -----------------------------------------------------------------------------
# Concrete model components
# -----------------------------------------------------------------------------

class DefaultEnterpriseRoiModel:
    """Enterprise ROI = productivity benefit less AI and governance cost."""

    def __init__(self, config: ModelConfig):
        self.config = config

    def compute(self, scenario: Scenario, enterprise_adoption_prev: float, price_index_prev: float) -> RoiResult:
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
        return RoiResult(
            gross_productivity_benefit_ratio=gross_benefit,
            ai_cost_ratio=ai_cost,
            governance_cost_ratio=governance_cost,
            net_productivity_benefit_ratio=net_benefit,
            enterprise_roi=roi,
        )


class LogisticAdoptionModel:
    """Logistic consumer/enterprise adoption with ROI and price feedback."""

    def __init__(self, config: ModelConfig):
        self.config = config

    def update(
        self,
        scenario: Scenario,
        enterprise_prev: float,
        consumer_prev: float,
        enterprise_roi: float,
        price_decline_rate: float,
    ) -> AdoptionSnapshot:
        cfg = self.config
        roi_multiplier = 1.50 * sigmoid(enterprise_roi) - 0.20
        churn_buffer = cfg.workflow_stickiness * enterprise_prev
        enterprise_delta = (
            cfg.adoption_speed_enterprise
            * enterprise_prev
            * max(0.0, 1.0 - enterprise_prev / cfg.max_enterprise_penetration)
            * roi_multiplier
        )
        if enterprise_delta < 0:
            enterprise_delta *= 1.0 - churn_buffer
        enterprise = clip(enterprise_prev + enterprise_delta, 0.01, cfg.max_enterprise_penetration)

        price_multiplier = 0.75 + 1.50 * clip(price_decline_rate, 0.0, 0.70)
        consumer_delta = (
            cfg.adoption_speed_consumer
            * consumer_prev
            * max(0.0, 1.0 - consumer_prev / cfg.max_consumer_penetration)
            * price_multiplier
        )
        consumer = clip(consumer_prev + consumer_delta, 0.01, cfg.max_consumer_penetration)
        return AdoptionSnapshot(
            enterprise=enterprise,
            consumer=consumer,
            adoption_index=0.70 * enterprise + 0.30 * consumer,
        )


class CompetitivePricingModel:
    """Price decline from efficiency pass-through and competitive pressure."""

    def annual_price_decline_rate(self, scenario: Scenario, year_index: int) -> float:
        frontier_premium_decay = scenario.frontier_quality_premium * math.exp(-0.25 * year_index)
        competition_pressure = (
            0.55 * scenario.china_price_compression * (1.0 + 0.50 * scenario.ppp_cost_advantage)
            + 0.45 * scenario.open_source_pressure
        ) / 5.0
        premium_offset = 0.35 * frontier_premium_decay / 5.0
        decline = scenario.price_pass_through * scenario.inference_cost_decline + competition_pressure - premium_offset
        return clip(decline, 0.0, 0.75)


class JevonsDemandModel:
    """Elastic demand response to AI price declines plus adoption/agent usage."""

    def __init__(self, config: ModelConfig):
        self.config = config

    def initial_demand(self) -> DemandSnapshot:
        cfg = self.config
        token_volume = cfg.initial_token_volume
        price_index = cfg.initial_price_index
        compute_per_token = cfg.initial_compute_per_token
        training_compute = 0.18
        compute_demand = token_volume * compute_per_token + training_compute
        adoption_index = 0.70 * cfg.initial_enterprise_adoption + 0.30 * cfg.initial_consumer_adoption
        return DemandSnapshot(
            token_volume=token_volume,
            price_index=price_index,
            compute_per_token=compute_per_token,
            training_compute=training_compute,
            compute_demand=compute_demand,
            actual_cloud_demand_index=compute_demand * price_index,
            monetized_ai_spend_index=token_volume * price_index,
            adoption_index=adoption_index,
            token_growth=0.0,
            price_decline=0.0,
        )

    def next_demand(
        self,
        scenario: Scenario,
        previous: DemandSnapshot,
        previous_adoption: AdoptionSnapshot,
        current_adoption: AdoptionSnapshot,
        price_decline: float,
    ) -> DemandSnapshot:
        price_index = previous.price_index * (1.0 - price_decline)
        price_ratio = price_index / max(previous.price_index, EPS)
        price_elastic_growth = price_ratio ** (-scenario.demand_elasticity) - 1.0
        enterprise_delta = current_adoption.enterprise - previous_adoption.enterprise
        consumer_delta = current_adoption.consumer - previous_adoption.consumer
        adoption_usage_growth = 2.20 * enterprise_delta + 0.90 * consumer_delta
        agent_usage_growth = 0.06 * scenario.enterprise_agent_intensity * current_adoption.enterprise
        raw_token_growth = (
            scenario.organic_token_growth
            + scenario.demand_shock
            + scenario.recession_shock
            + price_elastic_growth
            + adoption_usage_growth
            + agent_usage_growth
        )
        token_growth = clip(raw_token_growth, -0.60, 2.50)
        token_volume = previous.token_volume * (1.0 + token_growth)
        compute_per_token = previous.compute_per_token * (1.0 - clip(scenario.compute_per_token_decline, 0.0, 0.85))
        training_compute = 0.18 * (token_volume ** 0.65) * (1.0 - 0.25 * scenario.open_source_pressure)
        compute_demand = token_volume * compute_per_token + training_compute
        return DemandSnapshot(
            token_volume=token_volume,
            price_index=price_index,
            compute_per_token=compute_per_token,
            training_compute=training_compute,
            compute_demand=compute_demand,
            actual_cloud_demand_index=compute_demand * price_index,
            monetized_ai_spend_index=token_volume * price_index,
            adoption_index=current_adoption.adoption_index,
            token_growth=token_growth,
            price_decline=price_decline,
        )


class DefaultOnsitePowerModel:
    """Onsite generation fuel/carbon/grid-services economics."""

    def __init__(self, config: ModelConfig):
        self.config = config

    def compute(self, scenario: Scenario) -> OnsitePowerResult:
        cfg = self.config
        energy_mwh = cfg.onsite_gen_capacity_mw * cfg.onsite_capacity_factor * 8760.0
        heat_rate = cfg.onsite_heat_rate_btu_per_kwh / 1000.0
        effective_fuel_price = scenario.gas_price_per_mmbtu * (
            cfg.onsite_hedge_ratio + (1.0 - cfg.onsite_hedge_ratio) * (1.0 + cfg.onsite_basis_risk)
        )
        fuel_cost_bn = energy_mwh * heat_rate * effective_fuel_price / 1e9
        carbon_cost_bn = energy_mwh * cfg.gas_emissions_ton_per_mwh * scenario.carbon_price_per_ton / 1e9
        grid_services_bn = cfg.onsite_gen_capacity_mw * cfg.grid_services_revenue_per_mw_year / 1e9
        grid_equivalent_bn = energy_mwh * cfg.grid_power_price_per_mwh / 1e9
        net_delta_bn = fuel_cost_bn + carbon_cost_bn - grid_services_bn - grid_equivalent_bn
        onsite_share = cfg.onsite_gen_capacity_mw / max(cfg.total_dc_power_mw0, EPS)
        return OnsitePowerResult(
            onsite_energy_mwh=energy_mwh,
            onsite_fuel_cost_bn=fuel_cost_bn,
            onsite_carbon_cost_bn=carbon_cost_bn,
            onsite_grid_services_revenue_bn=grid_services_bn,
            onsite_grid_equivalent_cost_bn=grid_equivalent_bn,
            onsite_net_delta_vs_grid_bn=net_delta_bn,
            onsite_power_growth_bonus=0.50 * onsite_share,
        )


class ConstrainedCapacityModel:
    """Capacity growth constrained by silicon, power, construction, and sentiment."""

    def __init__(self, config: ModelConfig):
        self.config = config

    def initial_capacity(self) -> CapacitySnapshot:
        cfg = self.config
        compute_capacity = cfg.initial_compute_capacity
        compute_demand0 = cfg.initial_token_volume * cfg.initial_compute_per_token + 0.18
        utilization = min(1.0, compute_demand0 / max(compute_capacity, EPS))
        overcapacity = max(0.0, compute_capacity / max(compute_demand0, EPS) - 1.0 / cfg.target_utilization)
        initial_capex = compute_capacity * cfg.maintenance_capex_per_capacity_unit + 0.15 * cfg.capex_per_capacity_unit
        return CapacitySnapshot(
            compute_capacity=compute_capacity,
            utilization=utilization,
            overcapacity_ratio=overcapacity,
            global_capacity_capex=initial_capex,
            allowed_capacity_growth=0.0,
        )

    def next_capacity(
        self,
        scenario: Scenario,
        year_index: int,
        previous_capacity: CapacitySnapshot,
        compute_demand: float,
        token_growth: float,
        onsite_power_bonus: float,
    ) -> CapacitySnapshot:
        cfg = self.config
        silicon_cap = scenario.silicon_growth_cap if scenario.silicon_growth_cap is not None else cfg.default_silicon_growth_cap
        power_cap = scenario.power_growth_cap if scenario.power_growth_cap is not None else cfg.default_power_growth_cap
        construction_cap = scenario.construction_growth_cap if scenario.construction_growth_cap is not None else cfg.default_construction_growth_cap
        power_cap_effective = power_cap + onsite_power_bonus
        base_allowed_growth = min(silicon_cap, power_cap_effective, construction_cap) * scenario.infrastructure_speed
        delay_drag = cfg.grid_delay_years / (cfg.grid_delay_years + year_index + 1.0)
        allowed_growth = clip(base_allowed_growth * (1.0 - 0.35 * delay_drag), 0.02, 1.20)

        existing_after_obsolescence = previous_capacity.compute_capacity * (1.0 - cfg.capacity_obsolescence_rate)
        desired_capacity = compute_demand / cfg.target_utilization
        demand_gap_addition = max(0.0, desired_capacity - existing_after_obsolescence)
        reflexive_addition = (
            previous_capacity.compute_capacity
            * scenario.capex_reflexivity
            * max(token_growth, 0.0)
            * max(scenario.valuation_multiple_multiplier, 0.20)
            * math.exp(-scenario.sentiment_decay * year_index)
        )
        committed_addition = previous_capacity.compute_capacity * scenario.committed_capex_overbuild * max(0.0, 1.0 - year_index / 6.0)
        planned_addition = demand_gap_addition + reflexive_addition + committed_addition
        max_physical_addition = previous_capacity.compute_capacity * allowed_growth
        capacity_addition = min(planned_addition, max_physical_addition)
        compute_capacity = existing_after_obsolescence + capacity_addition
        utilization = min(1.0, compute_demand / max(compute_capacity, EPS))
        overcapacity = max(0.0, compute_capacity / max(compute_demand, EPS) - 1.0 / cfg.target_utilization)
        global_capex = capacity_addition * cfg.capex_per_capacity_unit + compute_capacity * cfg.maintenance_capex_per_capacity_unit
        return CapacitySnapshot(
            compute_capacity=compute_capacity,
            utilization=utilization,
            overcapacity_ratio=overcapacity,
            global_capacity_capex=global_capex,
            allowed_capacity_growth=allowed_growth,
        )


class MultiYearContractLagPolicy:
    """Enterprise multi-year contracts delay reported revenue adjustment."""

    def __init__(self, config: ModelConfig):
        self.config = config

    def apply(
        self,
        year: int,
        prev_reported: float,
        actual_revenue: float,
        scenario: Scenario,
        enterprise_roi: float,
    ) -> float:
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
            reported *= 1.0 - clip(downsize, 0.0, 0.70)
        return max(0.01, reported)


class DefaultSectorFinancialProjector:
    """Sector-level financial projection, including margins, FCF, ROIC, multiples."""

    def __init__(self, config: ModelConfig, contract_lag_policy: ContractLagPolicy):
        self.config = config
        self.contract_lag_policy = contract_lag_policy

    def initial_state(self, sector: SectorParams) -> SectorState:
        cfg = self.config
        ebit = sector.revenue0 * sector.ebit_margin0
        tax = max(0.0, ebit * cfg.tax_rate)
        nopat = ebit - tax
        capex = sector.revenue0 * sector.capex_intensity0
        depreciation = sector.invested_capital0 / sector.asset_life_years
        fcf = nopat + depreciation - capex
        roic = nopat / max(sector.invested_capital0, EPS)
        return SectorState(
            actual_revenue=sector.revenue0,
            reported_revenue=sector.revenue0,
            revenue_growth=0.0,
            ebit_margin=sector.ebit_margin0,
            ebit=ebit,
            tax=tax,
            nopat=nopat,
            capex=capex,
            depreciation=depreciation,
            fcf=fcf,
            invested_capital=sector.invested_capital0,
            roic=roic,
            ev_sales_multiple=sector.base_ev_sales_multiple,
            multiple_based_value=sector.revenue0 * sector.base_ev_sales_multiple,
        )

    def _sector_driver_growth(self, sector: SectorParams, d: StepDrivers) -> float:
        if sector.semiconductor_supplier:
            return 0.45 * d.compute_growth + 0.55 * d.capex_growth
        if sector.infrastructure_supplier:
            return 0.20 * d.compute_growth + 0.80 * d.capex_growth
        if "cloud" in sector.name or "rental" in sector.name:
            return d.cloud_demand_growth
        if "enterprise" in sector.name:
            return 0.75 * d.adoption_growth + 0.25 * d.monetized_demand_growth
        if "frontier_model" in sector.name:
            return 0.75 * d.monetized_demand_growth + 0.25 * d.adoption_growth
        return d.monetized_demand_growth

    def project(self, sector: SectorParams, previous: SectorState, drivers: StepDrivers) -> SectorState:
        cfg = self.config
        s = drivers.scenario
        growth_fade = math.exp(-0.15 * drivers.year_index)
        driver_fade = math.exp(-0.10 * max(0, drivers.year_index - 4))
        base_growth_t = sector.terminal_growth + (sector.base_growth - sector.terminal_growth) * growth_fade
        sector_driver_g = self._sector_driver_growth(sector, drivers)
        growth = (
            base_growth_t
            + driver_fade * sector.ai_demand_beta * sector_driver_g
            + driver_fade * sector.capex_cycle_beta * drivers.capex_growth
            - sector.price_pressure_beta * (drivers.price_decline + drivers.competition_pressure)
            + sector.productivity_beta * drivers.net_productivity_benefit
            - sector.compliance_beta * drivers.regulated_cost_ratio
            - sector.overcapacity_beta * drivers.overcapacity_ratio * 0.14
            + s.recession_shock
        )

        if sector.contract_lag_sensitive and ("cloud" in sector.name or "rental" in sector.name):
            growth = 0.35 * growth + 0.65 * drivers.cloud_demand_growth

        if sector.semiconductor_supplier:
            if drivers.utilization < 0.70:
                growth -= 0.35 * (0.70 - drivers.utilization) / 0.70
            if drivers.overcapacity_ratio > 0.30:
                growth -= 0.15 * drivers.overcapacity_ratio
        if sector.infrastructure_supplier:
            growth += 0.10 * drivers.allowed_capacity_growth
            if drivers.year_index > 4 and drivers.utilization < 0.65:
                growth -= 0.18 * (0.65 - drivers.utilization) / 0.65

        growth = clip(growth, -0.65, 0.55)
        actual_revenue = max(0.01, previous.actual_revenue * (1.0 + growth))
        if sector.contract_lag_sensitive:
            reported_revenue = self.contract_lag_policy.apply(
                year=drivers.year,
                prev_reported=previous.reported_revenue,
                actual_revenue=actual_revenue,
                scenario=s,
                enterprise_roi=drivers.enterprise_roi,
            )
        else:
            reported_revenue = actual_revenue
        revenue_growth = reported_revenue / max(previous.reported_revenue, EPS) - 1.0

        margin = (
            sector.ebit_margin0
            + sector.margin_efficiency_beta * s.inference_cost_decline * 0.25
            + sector.productivity_beta * drivers.net_productivity_benefit * 0.60
            - sector.margin_price_pressure_beta * drivers.competition_pressure
            - sector.compliance_beta * drivers.regulated_cost_ratio
            - sector.overcapacity_beta * drivers.overcapacity_ratio * 0.08
            - s.stranded_asset_penalty * max(0.0, 0.75 - drivers.utilization)
        )
        if sector.semiconductor_supplier and drivers.utilization < 0.75:
            margin -= 0.45 * (0.75 - drivers.utilization)
        if sector.buyer_capex_share > 0.10 or "cloud" in sector.name or "datacenter" in sector.name:
            margin -= drivers.power_margin_drag
        if "frontier_model" in sector.name:
            margin += 0.35 * s.inference_cost_decline
            margin -= 0.45 * drivers.competition_pressure
        margin = clip(margin, -0.60, 0.60)

        ebit = reported_revenue * margin
        tax = max(0.0, ebit * cfg.tax_rate)
        nopat = ebit - tax
        depreciation = previous.invested_capital / sector.asset_life_years
        capex_intensity = sector.capex_intensity0 + sector.capex_sensitivity * max(0.0, drivers.capacity_growth_rate)
        capex_intensity = clip(capex_intensity, 0.0, 0.90)
        capex = reported_revenue * capex_intensity + sector.buyer_capex_share * drivers.global_capacity_capex
        delta_nwc = sector.nwc_intensity * (reported_revenue - previous.reported_revenue)
        fcf = nopat + depreciation - capex - delta_nwc
        invested_capital = max(0.01, previous.invested_capital + capex - depreciation)
        roic = nopat / max(previous.invested_capital, EPS)

        forward_cagr_proxy = clip(0.50 * revenue_growth + 0.50 * sector.base_growth, -0.20, 0.80)
        roic_spread = roic - (sector.wacc + s.wacc_spread_add)
        quality_adj = 0.65 + 0.55 * sector.quality_score
        growth_adj = clip(1.0 + 2.2 * (forward_cagr_proxy - 0.08), 0.30, 2.50)
        roic_adj = clip(1.0 + 3.0 * roic_spread, 0.25, 2.20)
        compression_adj = clip(1.0 - 0.35 * (s.china_price_compression + s.open_source_pressure), 0.25, 1.10)
        sentiment_adj = s.valuation_multiple_multiplier * math.exp(-s.sentiment_decay * drivers.year_index)
        ev_sales_multiple = clip(
            sector.base_ev_sales_multiple * quality_adj * growth_adj * roic_adj * compression_adj * sentiment_adj,
            0.20,
            60.0,
        )
        multiple_value = reported_revenue * ev_sales_multiple
        return SectorState(
            actual_revenue=actual_revenue,
            reported_revenue=reported_revenue,
            revenue_growth=revenue_growth,
            ebit_margin=margin,
            ebit=ebit,
            tax=tax,
            nopat=nopat,
            capex=capex,
            depreciation=depreciation,
            fcf=fcf,
            invested_capital=invested_capital,
            roic=roic,
            ev_sales_multiple=ev_sales_multiple,
            multiple_based_value=multiple_value,
        )


class NormalizedDcfValuationModel:
    """DCF valuation with normalized terminal FCF rather than final-year buildout FCF."""

    def __init__(self, config: ModelConfig):
        self.config = config

    def value(self, sector_df: pd.DataFrame, sectors: Mapping[str, SectorParams], scenario: Scenario) -> pd.DataFrame:
        cfg = self.config
        rows = []
        for key, sec in sectors.items():
            sdf = sector_df[sector_df["sector"] == key].sort_values("year").reset_index(drop=True)
            fcf = sdf["fcf_bn"].to_numpy()
            revenue = sdf["reported_revenue_bn"].to_numpy()
            wacc = max(0.02, sec.wacc + scenario.wacc_spread_add)
            terminal_growth = min(sec.terminal_growth + scenario.terminal_growth_adjustment, cfg.terminal_growth_cap, wacc - 0.01)
            pv_fcf = sum(fcf[t] * pv_factor(wacc, t) for t in range(1, len(fcf)))
            forecast_cagr = cagr(revenue[0], revenue[-1], len(revenue) - 1)
            avg_roic_5y = float(sdf.tail(5)["roic"].mean())
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
                "market_to_fair_value": sec.market_cap0 / dcf_ev if dcf_ev > EPS else 10.0,
                "wacc": wacc,
                "terminal_growth": terminal_growth,
                "forecast_revenue_cagr": forecast_cagr,
                "avg_roic_last5y": avg_roic_5y,
                "terminal_fcf_bn": normalized_terminal_fcf,
                "explicit_year_terminal_fcf_bn": fcf[-1],
                "terminal_revenue_bn": revenue[-1],
            })
        return pd.DataFrame(rows)


class DefaultSummaryModel:
    def __init__(self, config: ModelConfig):
        self.config = config

    def summarize(
        self,
        global_df: pd.DataFrame,
        sector_df: pd.DataFrame,
        dcf_df: pd.DataFrame,
        sectors: Mapping[str, SectorParams],
        scenario: Scenario,
    ) -> Dict[str, float]:
        cfg = self.config
        start_year = cfg.start_year
        end_year = cfg.start_year + cfg.horizon_years

        def totals_at(year: int) -> pd.Series:
            return sector_df[sector_df["year"] == year].sum(numeric_only=True)

        start_totals = totals_at(start_year)
        y5 = totals_at(min(start_year + 5, end_year))
        y10 = totals_at(min(start_year + 10, end_year))
        y20 = totals_at(end_year)
        total_market0 = sum(sec.market_cap0 for sec in sectors.values())
        total_dcf = float(dcf_df["dcf_ev_bn"].sum())
        aggregate_fair = total_dcf / max(total_market0, EPS)
        aggregate_market_to_fair = total_market0 / total_dcf if total_dcf > EPS else 10.0
        total_revenue0 = float(start_totals["reported_revenue_bn"])
        total_revenue5 = float(y5["reported_revenue_bn"])
        total_revenue10 = float(y10["reported_revenue_bn"])
        total_revenue20 = float(y20["reported_revenue_bn"])
        total_fcf5 = float(y5["fcf_bn"])
        total_fcf10 = float(y10["fcf_bn"])
        total_fcf20 = float(y20["fcf_bn"])
        total_capex5 = float(y5["capex_bn"])
        total_nopat20 = float(y20["nopat_bn"])
        total_ic20 = float(y20["invested_capital_bn"])
        initial_sector = sector_df[sector_df["year"] == start_year]
        quality_weighted = float(np.average(initial_sector["quality_score"], weights=np.maximum(initial_sector["reported_revenue_bn"], EPS)))
        low_quality_weighted = float(np.average(initial_sector["quality_low"], weights=np.maximum(initial_sector["reported_revenue_bn"], EPS)))
        cloud_like = sector_df[sector_df["sector"].isin(["ai_cloud_rental", "hyperscaler_cloud_ai", "enterprise_ai_software"])]
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
            "aggregate_fair_value_to_market": aggregate_fair,
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
            "multiple_value_y5_bn": float(y5["multiple_based_value_bn"]),
            "multiple_value_y10_bn": float(y10["multiple_based_value_bn"]),
            "price_target_ratio_5y_vs_market0": float(y5["multiple_based_value_bn"]) / max(total_market0, EPS),
            "price_target_ratio_10y_vs_market0": float(y10["multiple_based_value_bn"]) / max(total_market0, EPS),
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


class ReducedFormAggregateOutcomeClassifier:
    """Aggregate scenario classifier: burst / deflation / stagnation / expansion."""

    def __init__(self, config: ModelConfig):
        self.config = config

    def _bubble_score(self, summary: Mapping[str, float], scenario: Scenario) -> float:
        cfg = self.config
        valuation_excess = min(max(0.0, summary["aggregate_market_to_fair_value"] - 1.0), 5.0)
        overbuild = max(0.0, summary["avg_overcapacity_5y"])
        low_quality = summary["initial_low_quality_revenue_share_weighted"]
        fcf_penalty = max(0.0, -summary["fcf_margin5"])
        rate_penalty = max(0.0, (cfg.risk_free_rate + scenario.wacc_spread_add) - 0.035) / 0.05
        reflexivity = scenario.capex_reflexivity * scenario.valuation_multiple_multiplier
        return float(
            cfg.bubble_weight_valuation * valuation_excess
            + cfg.bubble_weight_overbuild * overbuild
            + cfg.bubble_weight_revenue_quality * low_quality
            + cfg.bubble_weight_fcf * fcf_penalty
            + cfg.bubble_weight_rates * rate_penalty
            + cfg.bubble_weight_reflexivity * reflexivity
        )

    def probabilities(self, summary: Mapping[str, float], scenario: Scenario) -> Dict[str, float]:
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
            "rapid_dotcom_style_burst": 0.30 + 1.80 * valuation_excess + 1.25 * overbuild + 0.70 * max(0.0, -fcf_margin) + 0.45 * price_comp - 1.20 * productivity - 0.35 * adoption,
            "gradual_valuation_deflation": 0.65 + 0.80 * bubble + 0.65 * price_comp + 0.55 * contract_lag + 0.35 * max(0.0, fcf_margin) - 0.45 * max(0.0, -fcf_margin),
            "japan_style_prolonged_stagnation": 0.20 + 0.90 * overbuild + 0.55 * max(0.0, -roic_spread) + 0.45 * scenario.stranded_asset_penalty + 0.40 * max(0.0, -summary["revenue_cagr_10y"]) - 0.55 * productivity,
            "productivity_led_expansion": 0.25 + 1.60 * productivity + 0.70 * elasticity_bonus + 0.55 * adoption + 0.35 * max(0.0, fcf_margin) - 0.55 * price_comp - 0.60 * overbuild,
        }
        probs = softmax(scores)
        probs["bubble_score_diagnostic"] = bubble
        return probs


class ReducedFormEndpointOutcomeClassifier:
    """Sector endpoint crash-to-boom probability classifier."""

    def label_from_degree(self, degree: float) -> str:
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

    def probabilities(
        self,
        value_ratio: float,
        revenue_cagr: float,
        fcf_margin: float,
        roic_spread: float,
        capex_to_revenue: float,
    ) -> Dict[str, float]:
        vr = clip(value_ratio, 0.01, 8.0)
        log_v = math.log(vr)
        g = clip(revenue_cagr, -0.50, 0.80)
        f = clip(fcf_margin, -1.00, 1.00)
        r = clip(roic_spread, -0.50, 0.50)
        k = clip(capex_to_revenue, 0.00, 2.00)
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
        for outcome, (vc, gc, fc, vw, gw, fw) in centers.items():
            scores[outcome] = gaussian_score(log_v, math.log(vc), vw) + gaussian_score(g, gc, gw) + 0.55 * gaussian_score(f, fc, fw)
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
        if r < 0:
            neg = min(abs(r) / 0.10, 3.0)
            scores["complete_severe_crash"] += 0.40 * neg
            scores["severe_crash"] += 0.35 * neg
            scores["prolonged_stagnation"] += 0.45 * neg
            scores["resilient_compounding"] -= 0.50 * neg
            scores["booming_expansion"] -= 0.80 * neg
        else:
            pos = min(r / 0.10, 3.0)
            scores["resilient_compounding"] += 0.30 * pos
            scores["booming_expansion"] += 0.35 * pos
        if k > 0.35 and f < 0:
            overbuild_penalty = min((k - 0.35) / 0.30, 3.0)
            scores["complete_severe_crash"] += 0.35 * overbuild_penalty
            scores["severe_crash"] += 0.45 * overbuild_penalty
            scores["valuation_deflation"] += 0.25 * overbuild_penalty
            scores["booming_expansion"] -= 0.50 * overbuild_penalty
        return softmax(scores)


# -----------------------------------------------------------------------------
# Simulation engine - orchestration only; business logic lives in components
# -----------------------------------------------------------------------------

class TESMSimulationEngine:
    """OOP orchestration engine with components injected through Protocols."""

    def __init__(
        self,
        config: ModelConfig,
        sectors: Mapping[str, SectorParams],
        roi_model: EnterpriseRoiModel,
        adoption_model: AdoptionModel,
        pricing_model: PricingModel,
        demand_model: JevonsDemandModel,
        power_model: OnsitePowerModel,
        capacity_model: CapacityModel,
        financial_projector: SectorFinancialProjector,
        valuation_model: ValuationModel,
        summary_model: SummaryModel,
        outcome_classifier: AggregateOutcomeClassifier,
    ):
        self.config = config
        self.sectors = dict(sectors)
        self.roi_model = roi_model
        self.adoption_model = adoption_model
        self.pricing_model = pricing_model
        self.demand_model = demand_model
        self.power_model = power_model
        self.capacity_model = capacity_model
        self.financial_projector = financial_projector
        self.valuation_model = valuation_model
        self.summary_model = summary_model
        self.outcome_classifier = outcome_classifier

    @classmethod
    def default(cls) -> "TESMSimulationEngine":
        cfg = DefaultConfigRepository().load_config()
        sectors = DefaultSectorRepository().load_sectors()
        contract_policy = MultiYearContractLagPolicy(cfg)
        return cls(
            config=cfg,
            sectors=sectors,
            roi_model=DefaultEnterpriseRoiModel(cfg),
            adoption_model=LogisticAdoptionModel(cfg),
            pricing_model=CompetitivePricingModel(),
            demand_model=JevonsDemandModel(cfg),
            power_model=DefaultOnsitePowerModel(cfg),
            capacity_model=ConstrainedCapacityModel(cfg),
            financial_projector=DefaultSectorFinancialProjector(cfg, contract_policy),
            valuation_model=NormalizedDcfValuationModel(cfg),
            summary_model=DefaultSummaryModel(cfg),
            outcome_classifier=ReducedFormAggregateOutcomeClassifier(cfg),
        )

    @classmethod
    def from_duckdb(cls, db_path: str = "databases/master_consolidated.duckdb") -> "TESMSimulationEngine":
        cfg = DuckDBConfigRepository(db_path).load_config()
        sectors = DuckDBSectorRepository(db_path).load_sectors()
        contract_policy = MultiYearContractLagPolicy(cfg)
        return cls(
            config=cfg,
            sectors=sectors,
            roi_model=DefaultEnterpriseRoiModel(cfg),
            adoption_model=LogisticAdoptionModel(cfg),
            pricing_model=CompetitivePricingModel(),
            demand_model=JevonsDemandModel(cfg),
            power_model=DefaultOnsitePowerModel(cfg),
            capacity_model=ConstrainedCapacityModel(cfg),
            financial_projector=DefaultSectorFinancialProjector(cfg, contract_policy),
            valuation_model=NormalizedDcfValuationModel(cfg),
            summary_model=DefaultSummaryModel(cfg),
            outcome_classifier=ReducedFormAggregateOutcomeClassifier(cfg),
        )

    def simulate(self, scenario: Scenario) -> SimulationResult:
        cfg = self.config
        years = list(range(cfg.start_year, cfg.start_year + cfg.horizon_years + 1))
        onsite = self.power_model.compute(scenario)

        current_adoption = AdoptionSnapshot(
            enterprise=cfg.initial_enterprise_adoption,
            consumer=cfg.initial_consumer_adoption,
            adoption_index=0.70 * cfg.initial_enterprise_adoption + 0.30 * cfg.initial_consumer_adoption,
        )
        current_demand = self.demand_model.initial_demand()
        current_capacity = self.capacity_model.initial_capacity()
        sector_states: Dict[str, SectorState] = {k: self.financial_projector.initial_state(s) for k, s in self.sectors.items()}

        global_rows: List[Dict[str, float]] = []
        sector_rows: List[Dict[str, float]] = []

        def append_global(year: int, year_index: int, roi_result: Optional[RoiResult]) -> None:
            row = {
                "year": year,
                "enterprise_adoption": current_adoption.enterprise,
                "consumer_adoption": current_adoption.consumer,
                "token_volume_index": current_demand.token_volume,
                "price_index": current_demand.price_index,
                "price_decline": current_demand.price_decline,
                "compute_per_token_index": current_demand.compute_per_token,
                "training_compute_index": current_demand.training_compute,
                "compute_demand_index": current_demand.compute_demand,
                "compute_capacity_index": current_capacity.compute_capacity,
                "utilization": current_capacity.utilization,
                "overcapacity_ratio": current_capacity.overcapacity_ratio,
                "allowed_capacity_growth": current_capacity.allowed_capacity_growth,
                "global_capacity_capex_bn": current_capacity.global_capacity_capex,
                "token_growth": current_demand.token_growth,
                "net_productivity_benefit_ratio": 0.0 if roi_result is None else roi_result.net_productivity_benefit_ratio,
                "enterprise_roi": 0.0 if roi_result is None else roi_result.enterprise_roi,
                "governance_cost_ratio": 0.0 if roi_result is None else roi_result.governance_cost_ratio,
                "actual_cloud_demand_index": current_demand.actual_cloud_demand_index,
                "monetized_ai_spend_index": current_demand.monetized_ai_spend_index,
                "adoption_index": current_demand.adoption_index,
            }
            row.update(onsite.as_dict())
            global_rows.append(row)

        def append_sector_rows(year: int) -> None:
            for key, sec in self.sectors.items():
                st = sector_states[key]
                sector_rows.append({
                    "scenario": scenario.name,
                    "year": year,
                    "sector": key,
                    "actual_revenue_bn": st.actual_revenue,
                    "reported_revenue_bn": st.reported_revenue,
                    "revenue_growth": st.revenue_growth,
                    "ebit_margin": st.ebit_margin,
                    "ebit_bn": st.ebit,
                    "tax_bn": st.tax,
                    "nopat_bn": st.nopat,
                    "capex_bn": st.capex,
                    "depreciation_bn": st.depreciation,
                    "fcf_bn": st.fcf,
                    "invested_capital_bn": st.invested_capital,
                    "roic": st.roic,
                    "ev_sales_multiple": st.ev_sales_multiple,
                    "multiple_based_value_bn": st.multiple_based_value,
                    "quality_score": sec.quality_score,
                    "quality_low": sec.quality_low,
                })

        append_global(years[0], 0, roi_result=None)
        append_sector_rows(years[0])

        for t, year in enumerate(years[1:], start=1):
            previous_adoption = current_adoption
            previous_demand = current_demand
            previous_capacity = current_capacity
            previous_capex = previous_capacity.global_capacity_capex

            roi_result = self.roi_model.compute(scenario, previous_adoption.enterprise, previous_demand.price_index)
            price_decline = self.pricing_model.annual_price_decline_rate(scenario, t)
            current_adoption = self.adoption_model.update(
                scenario,
                previous_adoption.enterprise,
                previous_adoption.consumer,
                roi_result.enterprise_roi,
                price_decline,
            )
            current_demand = self.demand_model.next_demand(
                scenario,
                previous_demand,
                previous_adoption,
                current_adoption,
                price_decline,
            )
            current_capacity = self.capacity_model.next_capacity(
                scenario,
                t,
                previous_capacity,
                current_demand.compute_demand,
                current_demand.token_growth,
                onsite.onsite_power_growth_bonus,
            )

            compute_growth = current_demand.compute_demand / max(previous_demand.compute_demand, EPS) - 1.0
            capex_growth = current_capacity.global_capacity_capex / max(previous_capex, EPS) - 1.0
            cloud_demand_growth = current_demand.actual_cloud_demand_index / max(previous_demand.actual_cloud_demand_index, EPS) - 1.0
            monetized_demand_growth = current_demand.monetized_ai_spend_index / max(previous_demand.monetized_ai_spend_index, EPS) - 1.0
            adoption_growth = current_adoption.adoption_index / max(previous_adoption.adoption_index, EPS) - 1.0
            capacity_growth_rate = current_capacity.compute_capacity / max(previous_capacity.compute_capacity, EPS) - 1.0
            competition_pressure = (scenario.china_price_compression + scenario.open_source_pressure) / 5.0
            regulated_cost_ratio = roi_result.governance_cost_ratio * scenario.regulated_compliance_multiplier
            cloud_like_revenue_prev = sum(
                st.reported_revenue
                for key, st in sector_states.items()
                if self.sectors[key].buyer_capex_share > 0.10 or "cloud" in self.sectors[key].name or "datacenter" in self.sectors[key].name
            )
            power_margin_drag = max(0.0, onsite.onsite_net_delta_vs_grid_bn) / max(cloud_like_revenue_prev, EPS)
            drivers = StepDrivers(
                year=year,
                year_index=t,
                scenario=scenario,
                price_decline=price_decline,
                competition_pressure=competition_pressure,
                regulated_cost_ratio=regulated_cost_ratio,
                net_productivity_benefit=roi_result.net_productivity_benefit_ratio,
                overcapacity_ratio=current_capacity.overcapacity_ratio,
                global_capacity_capex=current_capacity.global_capacity_capex,
                capacity_growth_rate=capacity_growth_rate,
                capex_growth=capex_growth,
                cloud_demand_growth=cloud_demand_growth,
                compute_growth=compute_growth,
                monetized_demand_growth=monetized_demand_growth,
                adoption_growth=adoption_growth,
                allowed_capacity_growth=current_capacity.allowed_capacity_growth,
                utilization=current_capacity.utilization,
                power_margin_drag=power_margin_drag,
                enterprise_roi=roi_result.enterprise_roi,
            )
            sector_states = {
                key: self.financial_projector.project(sec, sector_states[key], drivers)
                for key, sec in self.sectors.items()
            }
            append_global(year, t, roi_result)
            append_sector_rows(year)

        global_df = pd.DataFrame(global_rows)
        sector_df = pd.DataFrame(sector_rows)
        dcf_df = self.valuation_model.value(sector_df, self.sectors, scenario)
        summary = self.summary_model.summarize(global_df, sector_df, dcf_df, self.sectors, scenario)
        probs = self.outcome_classifier.probabilities(summary, scenario)
        summary.update({f"prob_{k}": v for k, v in probs.items()})
        return SimulationResult(scenario, global_df, sector_df, dcf_df, summary, probs)


# -----------------------------------------------------------------------------
# Endpoint matrix builder
# -----------------------------------------------------------------------------

class SectorEndpointMatrixBuilder:
    def __init__(self, config: ModelConfig, sectors: Mapping[str, SectorParams], classifier: EndpointOutcomeClassifier):
        self.config = config
        self.sectors = dict(sectors)
        self.classifier = classifier

    def build_for_results(self, results: Iterable[SimulationResult], horizons: Sequence[int] = (5, 10, 20)) -> pd.DataFrame:
        rows: List[Dict[str, float]] = []
        for result in results:
            scen = result.scenario
            sector_df = result.sector_df
            for horizon in horizons:
                year = self.config.start_year + horizon
                if year > self.config.start_year + self.config.horizon_years:
                    continue
                target = sector_df[sector_df["year"] == year]
                for _, row in target.iterrows():
                    sec = self.sectors[str(row["sector"])]
                    revenue = float(row["reported_revenue_bn"])
                    value_ratio = float(row["multiple_based_value_bn"] / max(sec.market_cap0, EPS))
                    revenue_cagr = cagr(sec.revenue0, revenue, horizon)
                    fcf_margin = float(row["fcf_bn"] / max(revenue, EPS))
                    roic_spread = float(row["roic"] - (sec.wacc + scen.wacc_spread_add))
                    capex_to_revenue = float(row["capex_bn"] / max(revenue, EPS))
                    sales_multiple_change = float(row["ev_sales_multiple"] / max(sec.base_ev_sales_multiple, EPS) - 1.0)
                    probs = self.classifier.probabilities(value_ratio, revenue_cagr, fcf_margin, roic_spread, capex_to_revenue)
                    degree = sum(probs[k] * OUTCOME_DEGREE_SCORE[k] for k in OUTCOME_ORDER)
                    final_label = self.classifier.label_from_degree(degree)
                    highest_prob_label = max(OUTCOME_ORDER, key=lambda k: probs[k])
                    outrow = {
                        "scenario": scen.name,
                        "scenario_probability_weight": scen.probability_weight,
                        "horizon_years": horizon,
                        "endpoint_year": year,
                        "sector": sec.name,
                        "endpoint_label_highest_probability": highest_prob_label,
                        "endpoint_label_final": final_label,
                        "endpoint_label_short": OUTCOME_LABEL_SHORT[final_label],
                        "endpoint_degree_index": degree,
                        "endpoint_cell": f"{OUTCOME_LABEL_SHORT[final_label]} ({degree:+.0f})",
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

    def pivot(self, endpoint_df: pd.DataFrame, horizon: int = 10) -> pd.DataFrame:
        matrix = endpoint_df[endpoint_df["horizon_years"] == horizon]
        return matrix.pivot(index="sector", columns="scenario", values="endpoint_cell").reset_index()

    def probability_weighted(self, endpoint_df: pd.DataFrame) -> pd.DataFrame:
        rows = []
        for (sector, horizon), grp in endpoint_df.groupby(["sector", "horizon_years"]):
            w = grp["scenario_probability_weight"].to_numpy(float)
            wsum = float(w.sum()) if float(w.sum()) > 0 else 1.0
            weighted_probs = {
                f"weighted_prob_{outcome}": float((grp[f"prob_{outcome}"].to_numpy(float) * w).sum() / wsum)
                for outcome in OUTCOME_ORDER
            }
            expected_degree = float((grp["endpoint_degree_index"].to_numpy(float) * w).sum() / wsum)
            degree_label = self.classifier.label_from_degree(expected_degree)
            highest_prob_label = max(OUTCOME_ORDER, key=lambda k: weighted_probs[f"weighted_prob_{k}"])
            rows.append({
                "sector": sector,
                "horizon_years": int(horizon),
                "endpoint_label_highest_probability_weighted": highest_prob_label,
                "endpoint_label_final_weighted": degree_label,
                "endpoint_label_short": OUTCOME_LABEL_SHORT[degree_label],
                "endpoint_degree_index_weighted": expected_degree,
                "endpoint_cell_weighted": f"{OUTCOME_LABEL_SHORT[degree_label]} ({expected_degree:+.0f})",
                "weighted_value_ratio_vs_start": float((grp["endpoint_value_ratio_vs_start"].to_numpy(float) * w).sum() / wsum),
                "weighted_revenue_cagr": float((grp["endpoint_revenue_cagr"].to_numpy(float) * w).sum() / wsum),
                "weighted_fcf_margin": float((grp["endpoint_fcf_margin"].to_numpy(float) * w).sum() / wsum),
                **weighted_probs,
            })
        return pd.DataFrame(rows)


# -----------------------------------------------------------------------------
# Reporting and Monte Carlo
# -----------------------------------------------------------------------------

class CsvReportWriter:
    """SRP: only writes model outputs; does not contain modeling logic."""

    def __init__(self, output_dir: str | Path):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def write(self, engine: TESMSimulationEngine, scenarios: Mapping[str, Scenario]) -> None:
        results = [engine.simulate(s) for s in scenarios.values()]
        scenario_summary = pd.DataFrame([r.summary for r in results])
        scenario_summary.to_csv(self.output_dir / "scenario_summary.csv", index=False)

        baseline = next((r for r in results if r.scenario.name == "baseline_gradual_deflation"), results[0])
        baseline.sector_df.to_csv(self.output_dir / "sector_financials_baseline.csv", index=False)
        baseline.global_df.to_csv(self.output_dir / "global_metrics_baseline.csv", index=False)
        baseline.dcf_df.to_csv(self.output_dir / "dcf_baseline.csv", index=False)

        endpoint_builder = SectorEndpointMatrixBuilder(engine.config, engine.sectors, ReducedFormEndpointOutcomeClassifier())
        endpoint_df = endpoint_builder.build_for_results(results, horizons=(5, 10, 20))
        endpoint_df.to_csv(self.output_dir / "sector_endpoint_matrix.csv", index=False)
        endpoint_builder.pivot(endpoint_df, horizon=10).to_csv(self.output_dir / "sector_endpoint_pivot_10y.csv", index=False)
        endpoint_builder.probability_weighted(endpoint_df).to_csv(self.output_dir / "sector_endpoint_probability_weighted.csv", index=False)

        readme = """# TESM SOLID/OOP Outputs

Generated by `ai_tesm_solid_oop_model.py`.

This is the OOP/SOLID refactor of the core AI financial model.

Important files:
- scenario_summary.csv
- sector_financials_baseline.csv
- global_metrics_baseline.csv
- dcf_baseline.csv
- sector_endpoint_matrix.csv
- sector_endpoint_pivot_10y.csv
- sector_endpoint_probability_weighted.csv
"""
        (self.output_dir / "README.md").write_text(readme, encoding="utf-8")

        print(f"Wrote SOLID/OOP outputs to {self.output_dir.resolve()}")
        display_cols = [
            "scenario",
            "aggregate_fair_value_to_market",
            "revenue_cagr_10y",
            "fcf_margin10",
            "capex_to_revenue5",
            "prob_rapid_dotcom_style_burst",
            "prob_gradual_valuation_deflation",
            "prob_japan_style_prolonged_stagnation",
            "prob_productivity_led_expansion",
        ]
        print("\nScenario summary:")
        print(scenario_summary[[c for c in display_cols if c in scenario_summary.columns]].to_string(index=False))
        print("\n10-year endpoint matrix:")
        print(endpoint_builder.pivot(endpoint_df, horizon=10).to_string(index=False))


class MonteCarloScenarioFactory:
    """Creates randomized scenarios; replaceable without changing the engine."""

    def __init__(self, base: Scenario, seed: int = 42):
        self.base = base
        self.rng = np.random.default_rng(seed)

    def make(self, i: int) -> Scenario:
        rng = self.rng
        recession_draw = rng.choice([0.0, -0.05, -0.12], p=[0.74, 0.20, 0.06])
        return replace(
            self.base,
            name=f"mc_solid_{i:04d}",
            organic_token_growth=clip(rng.normal(0.22, 0.10), -0.05, 0.55),
            demand_elasticity=clip(rng.normal(1.05, 0.30), 0.25, 1.90),
            inference_cost_decline=clip(rng.normal(0.28, 0.08), 0.05, 0.55),
            compute_per_token_decline=clip(rng.normal(0.25, 0.08), 0.03, 0.55),
            price_pass_through=clip(rng.normal(0.65, 0.15), 0.20, 0.95),
            productivity_gross_gain=clip(rng.normal(0.09, 0.04), 0.00, 0.22),
            productivity_capture=clip(rng.normal(0.30, 0.10), 0.05, 0.60),
            tco_multiplier=clip(rng.triangular(1.0, 1.45, 3.0), 1.0, 3.5),
            china_price_compression=clip(rng.beta(2.0, 3.0), 0.02, 0.90),
            open_source_pressure=clip(rng.beta(2.0, 3.0), 0.02, 0.90),
            silicon_growth_cap=clip(rng.normal(0.45, 0.10), 0.12, 0.75),
            power_growth_cap=clip(rng.normal(0.32, 0.09), 0.08, 0.65),
            construction_growth_cap=clip(rng.normal(0.35, 0.10), 0.10, 0.75),
            valuation_multiple_multiplier=clip(rng.lognormal(mean=math.log(0.85), sigma=0.35), 0.25, 1.80),
            wacc_spread_add=clip(rng.normal(0.0, 0.012), -0.020, 0.040),
            recession_shock=recession_draw,
        )


class MonteCarloRunner:
    def __init__(self, engine: TESMSimulationEngine, factory: MonteCarloScenarioFactory):
        self.engine = engine
        self.factory = factory

    def run(self, n: int = 100) -> pd.DataFrame:
        rows = []
        for i in range(n):
            scen = self.factory.make(i)
            summary = self.engine.simulate(scen).summary
            summary["path"] = i
            rows.append(summary)
        return pd.DataFrame(rows)


# -----------------------------------------------------------------------------
# Composition root
# -----------------------------------------------------------------------------

def build_default_solid_model() -> Tuple[TESMSimulationEngine, Dict[str, Scenario]]:
    engine = TESMSimulationEngine.from_duckdb()
    scenarios = DefaultScenarioRepository().load_scenarios()
    return engine, scenarios


def main() -> None:
    engine, scenarios = build_default_solid_model()
    CsvReportWriter("tesm_solid_outputs").write(engine, scenarios)


if __name__ == "__main__":
    main()
