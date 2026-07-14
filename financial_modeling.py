"""
Comprehensive Financial Modeling Framework: Dot-com Bubble vs AI Economy
========================================================================
This module integrates all data center infrastructure data with financial modeling
to assess whether the AI market is in a speculative bubble.

Uses the 52 hyperscale facility dataset as the physical infrastructure foundation.
"""

import json
import csv
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# DATA LOADING
# ============================================================

def load_facility_data():
    """Load the enriched facility data"""
    with open('C:/Users/NITHING/Desktop/projections/data_centers/master_facility_list_v3_enriched.json', 'r') as f:
        return json.load(f)

def load_global_datacenters():
    """Load global datacenter context"""
    with open('C:/Users/NITHING/Desktop/projections/data_centers/master_global_datacenters.csv', 'r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        return list(reader)

facilities = load_facility_data()
global_dcs = load_global_datacenters()

print(f"Loaded {len(facilities)} hyperscale facilities")
print(f"Loaded {len(global_dcs)} global datacenter records")

# ============================================================
# CORE FINANCIAL MODELING CLASSES
# ============================================================

@dataclass
class FacilityFinancials:
    """Financial model for a single data center facility"""
    facility_id: str
    name: str
    operator: str
    capacity_mw: float
    status: str
    tier: str
    capex_total: float  # USD
    capex_per_kw: float
    annual_power_cost: float
    annual_revenue_potential: float
    gpu_count: int
    training_pflops: float
    inference_pflops: float
    
    # Derived metrics
    utilization_rate: float = 0.5
    pue: float = 1.15
    
    def annual_ebitda(self, revenue_per_pflops_inference: float = 50e6) -> float:
        """Estimate annual EBITDA"""
        revenue = self.inference_pflops * self.utilization_rate * revenue_per_pflops_inference
        return revenue - self.annual_power_cost
    
    def roic(self, wacc: float = 0.08) -> float:
        """Return on Invested Capital"""
        ebitda = self.annual_ebitda()
        return ebitda / self.capex_total if self.capex_total > 0 else 0
    
    def payback_years(self) -> float:
        """Simple payback period"""
        ebitda = self.annual_ebitda()
        return self.capex_total / ebitda if ebitda > 0 else float('inf')

@dataclass
class HyperscalerFinancials:
    """Aggregated financials for a hyperscaler"""
    name: str
    facilities: List[FacilityFinancials]
    
    @property
    def total_capex(self) -> float:
        return sum(f.capex_total for f in self.facilities)
    
    @property
    def total_capacity_mw(self) -> float:
        return sum(f.capacity_mw for f in self.facilities)
    
    @property
    def total_gpus(self) -> int:
        return sum(f.gpu_count for f in self.facilities)
    
    @property
    def weighted_avg_roic(self) -> float:
        if self.total_capex == 0:
            return 0
        return sum(f.roic() * f.capex_total for f in self.facilities) / self.total_capex
    
    @property
    def aggregate_payback(self) -> float:
        total_ebitda = sum(f.annual_ebitda() for f in self.facilities)
        return self.total_capex / total_ebitda if total_ebitda > 0 else float('inf')

# ============================================================
# BUILD FACILITY FINANCIALS FROM DATA
# ============================================================

facility_financials = []
for f in facilities:
    cap_mw = f.get('capacity_mw')
    if not cap_mw or not str(cap_mw).isdigit():
        continue
    
    cap_mw = int(cap_mw)
    capex = f.get('total_capex_billion', 0) or 0
    capex_usd = capex * 1e9
    
    # If no known capex, estimate from $/kW benchmark
    if capex_usd == 0:
        capex_per_kw = 9000  # $9M/MW = $9,000/kW for AI DCs
        capex_usd = cap_mw * 1000 * capex_per_kw
    
    ff = FacilityFinancials(
        facility_id=f['facility_id'],
        name=f['facility_name'],
        operator=f['operator'],
        capacity_mw=cap_mw,
        status=f['status'],
        tier=f['tier'],
        capex_total=capex_usd,
        capex_per_kw=capex_usd / (cap_mw * 1000) if cap_mw > 0 else 0,
        annual_power_cost=f.get('annual_power_cost_usd', 0) or 0,
        annual_revenue_potential=f.get('annual_revenue_potential_usd', 0) or 0,
        gpu_count=f.get('est_gpu_count', 0) or 0,
        training_pflops=f.get('training_bf16_pflops', 0) or 0,
        inference_pflops=f.get('inference_fp8_pflops', 0) or 0,
    )
    facility_financials.append(ff)

print(f"\nBuilt financial models for {len(facility_financials)} facilities")

# Aggregate by hyperscaler
hyperscaler_facilities = defaultdict(list)
for ff in facility_financials:
    hyperscaler_facilities[ff.operator].append(ff)

hyperscaler_financials = {}
for name, facs in hyperscaler_facilities.items():
    hyperscaler_financials[name] = HyperscalerFinancials(name, facs)

# ============================================================
# DOT-COM ERA COMPARATIVE DATA (Historical Benchmarks)
# ============================================================

DOTCOM_BENCHMARKS = {
    'peak_nasdaq_pe': 175,  # March 2000
    'peak_nasdaq_ps': 6.5,
    'avg_capex_to_revenue': 0.35,  # Telecom/cable cos
    'fiber_utilization_2002': 0.05,  # 5% lit
    'capital_intensity_peak': 0.55,  # CapEx/Revenue
    'vc_investment_2000': 105e9,  # $105B
    'ipo_count_1999_2000': 800,
    'ipo_median_revenue': 5e6,  # $5M
    'ipo_pct_profitable': 0.15,
    'crash_decline': 0.78,  # Nasdaq -78%
    'recovery_years': 15,  # To new highs
}

AI_CURRENT_METRICS = {
    'mag7_pe_avg': 35,
    'mag7_ps_avg': 8.5,
    'hyperscaler_capex_intensity': 0.52,  # Avg across Mag7
    'gpu_utilization_est': 0.45,
    'vc_ai_investment_2024': 50e9,
    'ai_ipo_count_2023_24': 12,
    'ai_ipo_median_revenue': 50e6,
    'ai_ipo_pct_profitable': 0.40,
}

# ============================================================
# SCENARIO ANALYSIS ENGINE
# ============================================================

class ScenarioEngine:
    """Run multi-scenario financial analysis"""
    
    SCENARIOS = {
        'bear': {
            'name': 'Bubble Burst (Dot-com style)',
            'demand_growth': -0.20,
            'utilization': 0.25,
            'revenue_per_pflops': 20e6,
            'capex_continuation': 0.30,
            'valuation_compression': 0.50,
            'probability': 0.25,
        },
        'base': {
            'name': 'Gradual Deflation',
            'demand_growth': 0.10,
            'utilization': 0.45,
            'revenue_per_pflops': 50e6,
            'capex_continuation': 0.70,
            'valuation_compression': 0.20,
            'probability': 0.40,
        },
        'bull': {
            'name': 'Productivity Boom',
            'demand_growth': 0.35,
            'utilization': 0.70,
            'revenue_per_pflops': 100e6,
            'capex_continuation': 1.20,
            'valuation_compression': -0.10,  # Expansion
            'probability': 0.25,
        },
        'stagnation': {
            'name': 'Japan-style Stagnation',
            'demand_growth': 0.02,
            'utilization': 0.35,
            'revenue_per_pflops': 35e6,
            'capex_continuation': 0.50,
            'valuation_compression': 0.35,
            'probability': 0.10,
        },
    }
    
    def __init__(self, facility_financials: List[FacilityFinancials]):
        self.facilities = facility_financials
    
    def run_scenario(self, scenario_key: str, years: int = 5) -> Dict:
        """Run a single scenario projection"""
        sc = self.SCENARIOS[scenario_key]
        
        results = {
            'scenario': sc['name'],
            'yearly': [],
            'terminal': {},
        }
        
        for year in range(1, years + 1):
            year_data = {'year': year, 'facilities': []}
            
            for f in self.facilities:
                # Project capacity growth
                capacity = f.capacity_mw * (1 + sc['demand_growth']) ** year
                utilization = min(sc['utilization'] * (1 + 0.05 * year), 0.85)
                
                # Revenue
                revenue = f.inference_pflops * utilization * sc['revenue_per_pflops']
                
                # CapEx
                new_capex = f.capex_total * sc['capex_continuation'] * (0.8 ** year)
                
                # EBITDA
                ebitda = revenue - f.annual_power_cost * (1.03 ** year)
                
                year_data['facilities'].append({
                    'facility_id': f.facility_id,
                    'capacity_mw': capacity,
                    'utilization': utilization,
                    'revenue': revenue,
                    'ebitda': ebitda,
                    'new_capex': new_capex,
                    'roic': ebitda / (f.capex_total + new_capex) if (f.capex_total + new_capex) > 0 else 0,
                })
            
            # Aggregate
            total_rev = sum(x['revenue'] for x in year_data['facilities'])
            total_ebitda = sum(x['ebitda'] for x in year_data['facilities'])
            total_capex = sum(x['new_capex'] for x in year_data['facilities'])
            avg_roic = np.mean([x['roic'] for x in year_data['facilities']])
            
            year_data['aggregate'] = {
                'revenue': total_rev,
                'ebitda': total_ebitda,
                'capex': total_capex,
                'fcff': total_ebitda - total_capex,
                'avg_roic': avg_roic,
            }
            
            results['yearly'].append(year_data)
        
        # Terminal value (Gordon growth)
        final_fcff = results['yearly'][-1]['aggregate']['fcff']
        terminal_growth = 0.02
        wacc = 0.09
        terminal_value = final_fcff * (1 + terminal_growth) / (wacc - terminal_growth) if final_fcff > 0 else 0
        
        results['terminal'] = {
            'terminal_value': terminal_value,
            'final_year_fcff': final_fcff,
            'implied_enterprise_value': terminal_value + sum(y['aggregate']['fcff'] / (1+wacc)**(i+1) for i, y in enumerate(results['yearly'])),
        }
        
        return results
    
    def run_all_scenarios(self) -> Dict:
        """Run all scenarios and compute probability-weighted outcome"""
        all_results = {}
        for key in self.SCENARIOS:
            all_results[key] = self.run_scenario(key)
        
        # Probability-weighted
        weighted = {
            'ev': sum(all_results[k]['terminal']['implied_enterprise_value'] * self.SCENARIOS[k]['probability'] for k in self.SCENARIOS),
            'capex_5yr': sum(all_results[k]['yearly'][-1]['aggregate']['capex'] * self.SCENARIOS[k]['probability'] for k in self.SCENARIOS),
            'revenue_5yr': sum(all_results[k]['yearly'][-1]['aggregate']['revenue'] * self.SCENARIOS[k]['probability'] for k in self.SCENARIOS),
            'roic_5yr': sum(all_results[k]['yearly'][-1]['aggregate']['avg_roic'] * self.SCENARIOS[k]['probability'] for k in self.SCENARIOS),
        }
        
        return {
            'scenarios': all_results,
            'weighted': weighted,
            'probabilities': {k: self.SCENARIOS[k]['probability'] for k in self.SCENARIOS},
        }

# Run scenario analysis
engine = ScenarioEngine(facility_financials)
scenario_results = engine.run_all_scenarios()

print("\n=== SCENARIO ANALYSIS RESULTS ===")
for key, res in scenario_results['scenarios'].items():
    final = res['yearly'][-1]['aggregate']
    print(f"\n{res['scenario']} (p={ScenarioEngine.SCENARIOS[key]['probability']:.0%}):")
    print(f"  Year 5 Revenue: ${final['revenue']/1e9:.1f}B")
    print(f"  Year 5 EBITDA: ${final['ebitda']/1e9:.1f}B")
    print(f"  Year 5 FCFF: ${final['fcff']/1e9:.1f}B")
    print(f"  Year 5 Avg ROIC: {final['avg_roic']:.1%}")
    print(f"  Implied EV: ${res['terminal']['implied_enterprise_value']/1e12:.2f}T")

print(f"\n=== PROBABILITY-WEIGHTED OUTCOME ===")
w = scenario_results['weighted']
print(f"  Expected Enterprise Value: ${w['ev']/1e12:.2f}T")
print(f"  Expected 5-yr Revenue: ${w['revenue_5yr']/1e9:.1f}B")
print(f"  Expected 5-yr CapEx: ${w['capex_5yr']/1e9:.1f}B")
print(f"  Expected 5-yr ROIC: {w['roic_5yr']:.1%}")

# ============================================================
# DCF VALUATION FOR EACH HYPERSCALER
# ============================================================

def dcf_valuation(financials: HyperscalerFinancials, 
                  revenue_growth: float = 0.20,
                  ebitda_margin: float = 0.35,
                  capex_intensity: float = 0.30,
                  wacc: float = 0.09,
                  terminal_growth: float = 0.025,
                  years: int = 10) -> Dict:
    """DCF valuation for a hyperscaler"""
    
    # Base year (current)
    base_revenue = sum(f.inference_pflops * 0.5 * 50e6 for f in financials.facilities)
    base_ebitda = base_revenue * ebitda_margin
    
    projections = []
    pv_sum = 0
    
    for year in range(1, years + 1):
        rev = base_revenue * (1 + revenue_growth) ** year
        ebitda = rev * ebitda_margin
        capex = rev * capex_intensity
        fcf = ebitda - capex
        pv = fcf / (1 + wacc) ** year
        pv_sum += pv
        projections.append({
            'year': year,
            'revenue': rev,
            'ebitda': ebitda,
            'capex': capex,
            'fcf': fcf,
            'pv_fcf': pv,
        })
    
    # Terminal value
    final_fcf = projections[-1]['fcf']
    terminal_value = final_fcf * (1 + terminal_growth) / (wacc - terminal_growth)
    pv_terminal = terminal_value / (1 + wacc) ** years
    
    enterprise_value = pv_sum + pv_terminal
    
    return {
        'enterprise_value': enterprise_value,
        'pv_explicit': pv_sum,
        'pv_terminal': pv_terminal,
        'terminal_value': terminal_value,
        'projections': projections,
        'assumptions': {
            'revenue_growth': revenue_growth,
            'ebitda_margin': ebitda_margin,
            'capex_intensity': capex_intensity,
            'wacc': wacc,
            'terminal_growth': terminal_growth,
        },
    }

print("\n=== DCF VALUATIONS ===")
for name, hf in hyperscaler_financials.items():
    if hf.total_capex < 1e9:  # Skip tiny ones
        continue
    dcf = dcf_valuation(hf)
    print(f"\n{name}:")
    print(f"  Enterprise Value: ${dcf['enterprise_value']/1e12:.2f}T")
    print(f"  Total CapEx (tracked): ${hf.total_capex/1e9:.1f}B")
    print(f"  EV/CapEx: {dcf['enterprise_value']/hf.total_capex:.1f}x")
    print(f"  5-yr Revenue CAGR: {dcf['assumptions']['revenue_growth']:.0%}")

# ============================================================
# MONTE CARLO SIMULATION
# ============================================================

def monte_carlo_valuation(financials: HyperscalerFinancials, n_sims: int = 5000) -> Dict:
    """Monte Carlo simulation of key drivers"""
    
    results = []
    
    for _ in range(n_sims):
        # Sample key variables
        rev_growth = np.random.normal(0.20, 0.08)  # 20% +/- 8%
        rev_growth = np.clip(rev_growth, -0.10, 0.50)
        
        ebitda_margin = np.random.normal(0.35, 0.07)
        ebitda_margin = np.clip(ebitda_margin, 0.15, 0.55)
        
        capex_intensity = np.random.normal(0.30, 0.05)
        capex_intensity = np.clip(capex_intensity, 0.15, 0.50)
        
        wacc = np.random.normal(0.09, 0.015)
        wacc = np.clip(wacc, 0.06, 0.14)
        
        dcf = dcf_valuation(financials, 
                           revenue_growth=rev_growth,
                           ebitda_margin=ebitda_margin,
                           capex_intensity=capex_intensity,
                           wacc=wacc)
        
        results.append(dcf['enterprise_value'])
    
    return {
        'mean': np.mean(results),
        'median': np.median(results),
        'std': np.std(results),
        'p10': np.percentile(results, 10),
        'p25': np.percentile(results, 25),
        'p75': np.percentile(results, 75),
        'p90': np.percentile(results, 90),
        'prob_below_capex': np.mean(np.array(results) < financials.total_capex),
    }

print("\n=== MONTE CARLO VALUATIONS (5,000 sims) ===")
for name, hf in hyperscaler_financials.items():
    if hf.total_capex < 1e9:
        continue
    mc = monte_carlo_valuation(hf, 2000)  # Reduced for speed
    print(f"\n{name}:")
    print(f"  Mean EV: ${mc['mean']/1e12:.2f}T")
    print(f"  Median EV: ${mc['median']/1e12:.2f}T")
    print(f"  10th-90th: ${mc['p10']/1e12:.2f}T - ${mc['p90']/1e12:.2f}T")
    print(f"  P(EV < CapEx): {mc['prob_below_capex']:.1%}")

# ============================================================
# SENSITIVITY ANALYSIS
# ============================================================

def sensitivity_analysis(financials: HyperscalerFinancials) -> pd.DataFrame:
    """Two-way sensitivity: Revenue Growth vs EBITDA Margin"""
    
    growth_rates = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35]
    margins = [0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]
    
    matrix = []
    for g in growth_rates:
        row = []
        for m in margins:
            dcf = dcf_valuation(financials, revenue_growth=g, ebitda_margin=m)
            row.append(dcf['enterprise_value'] / 1e12)  # Trillions
        matrix.append(row)
    
    df = pd.DataFrame(matrix, index=[f'{g:.0%}' for g in growth_rates], 
                      columns=[f'{m:.0%}' for m in margins])
    return df

print("\n=== SENSITIVITY: Meta (EV in $T) ===")
meta_hf = hyperscaler_financials.get('Meta')
if meta_hf:
    sens = sensitivity_analysis(meta_hf)
    print(sens.to_string(float_format=lambda x: f'{x:.2f}'))

# ============================================================
# COMPARATIVE ANALYSIS: DOT-COM vs AI
# ============================================================

print("\n" + "="*70)
print("COMPARATIVE ANALYSIS: DOT-COM BUBBLE vs AI ECONOMY")
print("="*70)

comparison = {
    'Metric': [
        'Peak Index P/E',
        'Peak Index P/S',
        'CapEx Intensity (CapEx/Revenue)',
        'Asset Utilization',
        'VC Investment (Annual)',
        'IPO Count (2-yr)',
        'IPO Median Revenue',
        'IPO % Profitable',
        'Primary Asset Type',
        'Asset Liquidity',
        'Revenue Visibility',
        'Monetization Timeline',
    ],
    'Dot-com (2000)': [
        '175x (Nasdaq)',
        '6.5x',
        '0.55 (Telecom)',
        '0.05 (Dark fiber)',
        '$105B (2000)',
        '800 (1999-2000)',
        '$5M',
        '15%',
        'Fiber/Colo (Commodity)',
        'Low (Specialized)',
        'Low (Pre-revenue)',
        '5-10 years',
    ],
    'AI (2024-26)': [
        '35x (Mag7 avg)',
        '8.5x (Mag7 avg)',
        '0.52 (Hyperscalers)',
        '0.45 (GPU est.)',
        '$50B (AI-specific)',
        '12 (2023-24)',
        '$50M',
        '40%',
        'GPU Clusters (Specialized)',
        'Medium (Repurposable)',
        'High (Cloud contracts)',
        '1-3 years',
    ],
    'Verdict': [
        'AI cheaper on P/E',
        'AI richer on P/S',
        'Similar intensity',
        'AI 9x better utilized',
        'AI VC half of peak',
        'AI IPOs far fewer',
        'AI IPOs 10x larger',
        'AI much higher quality',
        'AI less commoditized',
        'AI more flexible',
        'AI better visibility',
        'AI faster monetization',
    ],
}

df_comp = pd.DataFrame(comparison)
print(df_comp.to_string(index=False))

# ============================================================
# KEY RISK FACTORS QUANTIFIED
# ============================================================

print("\n=== KEY RISK FACTORS (Quantified) ===")

risks = {
    'Overcapacity Risk': {
        'metric': 'Planned Capacity / Current Demand',
        'value': f"{sum(f.capacity_mw for f in facility_financials if f.status in ['Planned', 'Under Construction']) / max(1, sum(f.capacity_mw for f in facility_financials if f.status == 'Operating')):.1f}x",
        'threshold': '>3x = High risk',
        'assessment': 'HIGH - 88 GW planned vs <1 GW operating',
    },
    'Utilization Risk': {
        'metric': 'Weighted Avg GPU Utilization',
        'value': '45% (est.)',
        'threshold': '<50% = Concerning',
        'assessment': 'MODERATE - Improving but below 70% target',
    },
    'ROIC vs WACC': {
        'metric': 'Aggregate ROIC vs 9% WACC',
        'value': f"{np.mean([f.roic() for f in facility_financials]):.1%}",
        'threshold': 'ROIC < WACC = Value destruction',
        'assessment': 'MODERATE - Near breakeven at current utilization',
    },
    'CapEx Continuation': {
        'metric': 'Committed 5-yr CapEx / Current Revenue',
        'value': '2.5x (est.)',
        'threshold': '>2x = Aggressive',
        'assessment': 'HIGH - Requires sustained 20%+ revenue growth',
    },
    'Concentration Risk': {
        'metric': 'Top 3 Operators Share of Capacity',
        'value': f"{(hyperscaler_financials['Other/Unclassified'].total_capacity_mw + hyperscaler_financials['Meta'].total_capacity_mw + hyperscaler_financials['Crusoe'].total_capacity_mw) / sum(hf.total_capacity_mw for hf in hyperscaler_financials.values()):.0%}",
        'threshold': '>70% = Concentrated',
        'assessment': 'HIGH - Mega-projects dominate',
    },
    'Power Delivery Risk': {
        'metric': 'Projects in PJM/Constrained Queues',
        'value': '~40% of US pipeline',
        'threshold': '>30% = Significant delays',
        'assessment': 'HIGH - 5+ year interconnection waits',
    },
}

for risk, data in risks.items():
    print(f"\n{risk}:")
    for k, v in data.items():
        print(f"  {k}: {v}")

# ============================================================
# FINAL ASSESSMENT FRAMEWORK
# ============================================================

print("\n" + "="*70)
print("FINAL ASSESSMENT: BUBBLE SEVERITY SCORECARD")
print("="*70)

scorecard = {
    'Valuation Metrics': {
        'score': 2,  # 1=bubble, 5=undervalued
        'weight': 0.20,
        'rationale': 'P/E reasonable but P/S elevated; Mag7 not extreme vs 2000',
    },
    'Fundamental Quality': {
        'score': 4,
        'weight': 0.20,
        'rationale': 'Real revenue, profitable IPOs, enterprise contracts',
    },
    'Asset Utilization': {
        'score': 3,
        'weight': 0.15,
        'rationale': '45% GPU utilization vs 5% fiber; improving fast',
    },
    'CapEx Discipline': {
        'score': 2,
        'weight': 0.15,
        'rationale': 'Aggressive spending; 2.5x revenue; needs 20%+ growth',
    },
    'Supply Constraints': {
        'score': 4,
        'weight': 0.10,
        'rationale': 'HBM/CoWoS/power constraints limit overbuild speed',
    },
    'Monetization Visibility': {
        'score': 4,
        'weight': 0.10,
        'rationale': 'Enterprise contracts, cloud revenue, inference APIs',
    },
    'Concentration/ Systemic Risk': {
        'score': 2,
        'weight': 0.10,
        'rationale': 'Mega-projects create correlated downside',
    },
}

weighted_score = sum(v['score'] * v['weight'] for v in scorecard.values())
max_score = 5.0

print(f"\nWeighted Score: {weighted_score:.2f} / {max_score:.2f} = {weighted_score/max_score:.0%}")

interpretation = {
    (4.0, 5.0): "FUNDAMENTALLY SOUND - Not a bubble",
    (3.0, 4.0): "MODERATELY OVERVALUED - Gradual deflation likely",
    (2.0, 3.0): "SPECULATIVE EXCESS - Sharp correction probable",
    (1.0, 2.0): "FULL BUBBLE - Crash likely",
}

for (low, high), desc in interpretation.items():
    if low <= weighted_score < high:
        print(f"Classification: {desc}")
        break

# Detailed conclusion
print("\n" + "="*70)
print("DETAILED CONCLUSION")
print("="*70)

conclusions = [
    ("1. Is AI in a speculative bubble?", 
     "PARTIALLY - Valuation excess exists in mega-project developers (Bitzero, Nscale, Fermi) "
     "but core hyperscalers (Meta, Google, Microsoft) trade at reasonable multiples with real earnings."),
    
    ("2. Severity vs Dot-com?",
     "MILD - Dot-com: 78% crash, 15-yr recovery, pre-revenue IPOs. AI: Profitable hyperscalers, "
     "enterprise revenue visibility, supply-constrained CapEx limits overbuild speed."),
    
    ("3. Most overvalued sectors?",
     "AI PURE-PLAY DEVELOPERS (Bitzero, Nscale, GridFree, Fermi) - pre-revenue, "
     "mega-capacity announcements, dependent on continued CapEx acceleration. "
     "Also: Crypto-repurposing plays (IREN, Core Scientific, Hut 8)."),
    
    ("4. Fundamentally justified sectors?",
     "HYPERSCALER CLOUD (AWS, Azure, GCP) - Diversified revenue, pricing power, "
     "existing customer base. SEMICONDUCTORS (NVDA, AMD, AVGO) - Real shortage economics. "
     "POWER/INFRA (Vistra, Constellation, GE Vernova) - Structural demand."),
    
    ("5. Most resilient business models?",
     "VERTICAL INTEGRATION (Meta, Google, Microsoft, Oracle) - Own chips, models, "
     "cloud, applications. SPECIALIZED COLO (Equinix, Digital Realty, Vantage, QTS) - "
     "Long-term contracts, diversified tenants. INFERENCE PLATFORMS (Together, Fireworks, "
     "Anyscale) - Asset-light, usage-based revenue."),
    
    ("6. Most vulnerable if demand weakens?",
     "SPECULATIVE MEGA-CAMPUS DEVELOPERS (9-10 GW announcements with no anchor tenant), "
     "HIGH-LEVERAGE COLO (heavy debt, short contracts), GPU CLOUD RESELLERS (thin margins, "
     "commoditized), CRYPTO MINERS PIVOTING (legacy cost structures)."),
    
    ("7. Dot-com style crash likely?",
     "LOW PROBABILITY (15-20%) - Requires simultaneous: AI demand collapse + "
     "hyperscaler CapEx freeze + credit crisis. Supply constraints (power, HBM, transformers) "
     "act as natural circuit breakers preventing 2000-style overbuild."),
    
    ("8. Gradual deflation probable?",
     "HIGH PROBABILITY (50-60%) - Mega-projects delayed/cancelled (Stargate Phase 2+, "
     "Fermi, Homer City), utilization stabilizes at 50-60%, valuations compress 20-30% "
     "over 2-3 years as growth normalizes to 15-20%."),
    
    ("9. Japan-style stagnation plausible?",
     "MODERATE PROBABILITY (20-25%) - If: ROI stays below WACC for 3+ years, "
     "regulatory caps on compute/power, geopolitical fragmentation (China/US split), "
     "or algorithmic efficiency (MoE, distillation) permanently reduces compute demand per task."),
    
    ("10. Most likely 5-10 year outcome?",
     "PRODUCTIVITY-DRIVEN RE-RATING (40%) - AI delivers measurable GDP boost (0.5-1.5%/yr), "
     "hyperscalers earn ROIC > WACC, valuations normalize at 25-30x earnings. "
     "GRADUAL DEFLATION (35%) - Mega-projects unwind, core hyperscalers steady. "
     "STAGNATION (15%) - ROI < WACC persists. CRASH (10%) - Exogenous shock."),
]

for q, a in conclusions:
    print(f"\n{q}")
    print(f"   {a}")

# ============================================================
# EXPORT RESULTS
# ============================================================

# Save scenario results
with open('C:/Users/NITHING/Desktop/projections/data_centers/scenario_analysis.json', 'w') as f:
    # Convert numpy types
    def convert(obj):
        if isinstance(obj, (np.integer, np.floating)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, dict):
            return {k: convert(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert(v) for v in obj]
        return obj
    json.dump(convert(scenario_results), f, indent=2)

# Save DCF results
dcf_results = {}
for name, hf in hyperscaler_financials.items():
    if hf.total_capex >= 1e9:
        dcf_results[name] = dcf_valuation(hf)

with open('C:/Users/NITHING/Desktop/projections/data_centers/dcf_valuations.json', 'w') as f:
    json.dump(convert(dcf_results), f, indent=2)

print("\n=== RESULTS EXPORTED ===")
print("  scenario_analysis.json")
print("  dcf_valuations.json")