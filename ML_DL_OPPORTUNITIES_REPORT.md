# Machine Learning & Deep Learning Opportunities Report
## Techno-Economic Systems Model (TESM) — AI vs. Dot-com Projection Engine

**Project**: TESM Projection Engine  
**Date**: 2026-07-17  
**Codebase**: `C:\Users\NITHING\Desktop\projections\`  
**Primary Engine**: `engine/tesm_simulation.py` (445 lines)  
**Calibration Pipeline**: `engine/calibrate.py` (1,057 lines)  
**Historical Validation**: `engine/historical_validation.py` (370 lines)  
**Sensitivity Analysis**: `engine/sensitivity_analysis.py` (186 lines)  
**Data Assets**: 54-table DuckDB (`databases/master_consolidated.duckdb`), 13-quarter SEC DERA panel, LBNL grid queues, USITC semiconductor trade, productivity meta-analysis, China benchmarks, enterprise contracts

---

## Executive Summary

The TESM is a **rule-based systems dynamics model** calibrated on real-world financial, infrastructure, and productivity data. It simulates 80-quarter trajectories across compute supply, power constraints, revenue dynamics, ROIC, and valuation indices. The current approach uses:
- **Deterministic simulation** with 100+ calibrated parameters
- **Grid-search optimization** for historical calibration (7 crises)
- **Monte Carlo** (500 trials) for uncertainty quantification
- **Sobol/OAT sensitivity analysis** for parameter importance

**ML/DL does not replace the mechanistic core** — it amplifies it. The highest-value applications are **surrogate modeling**, **Bayesian calibration**, **generative scenario design**, and **hybrid neural-mechanistic residuals**.

---

## 1. Surrogate Modeling / Emulation (Highest ROI)

### 1.1 Problem Statement
- `run_simulation()` executes 80 quarters × 500 Monte Carlo trials = **40,000 forward passes** per scenario matrix
- Scenario matrix evaluates 31 combinations (powerset of 5 dimensions) → **1.24M simulation runs**
- Each run: ~50-100ms → **minutes to hours** for full uncertainty quantification

### 1.2 ML Solution: Neural Surrogate
Train a neural network to emulate `run_simulation(params) → trajectory[80]` for key outputs.

| Approach | Architecture | Training Data | Inference Speedup |
|----------|--------------|---------------|-------------------|
| **MLP** | 4-layer (128-256-256-128) | 50k Latin Hypercube samples | ~1000x (μs vs ms) |
| **DeepONet** | Branch (params) + Trunk (time) | 20k trajectories | Continuous-time queries |
| **FNO** | Fourier Neural Operator | 10k trajectories | Resolution-invariant |
| **Transformer** | Encoder(params) + Decoder(time) | 30k trajectories | Attention over quarters |

### 1.3 Target Outputs to Emulate (Priority Order)
```python
# From tesm_simulation.py:178-207
PRIMARY_TARGETS = [
    "indexVal",        # Asset price index (primary validation metric)
    "cloudRevenue",    # Monetized AI spend
    "roic",            # Enterprise ROIC
    "computeSupply",   # Compute capacity
    "activePower",     # Grid power consumption
    "strandedCapacity" # Overbuild metric
]
SECONDARY_TARGETS = [
    "softwareRevenues", "netEnterpriseROI", "marketValuation",
    "multipleSales", "revenueQualityHigh", "revenueQualityLow",
    "gdpBoost", "siliconSupply"
]
```

### 1.4 Training Pipeline Design
```python
# Pseudocode: surrogate_training.py
import numpy as np
import torch
from torch.utils.data import DataLoader, TensorDataset
from tesm_simulation import run_simulation, DEFAULT_PARAMS

# 1. Define parameter space (from SENSITIVITY_PARAMS + calibrated overrides)
PARAM_BOUNDS = {
    "elasticityCoefficient": [0.5, 2.0],
    "priceCompression": [0.2, 0.8],
    "capitalReflexivity": [0.0, 0.9],
    "tcoMultiplier": [1.0, 2.5],
    "downsizingRatio": [0.1, 0.8],
    "powerGrowthCap": [0.03, 0.25],
    "chinaConvergenceRate": [0.01, 0.05],
    "chinaPriceCompressionVelocity": [0.02, 0.15],
    # ... 15-20 total calibrated parameters
}

# 2. Generate training data (Latin Hypercube Sampling)
from scipy.stats import qmc
sampler = qmc.LatinHypercube(d=len(PARAM_BOUNDS))
n_samples = 50000
param_samples = sampler.random(n=n_samples)
# Scale to bounds
for i, (_, bounds) in enumerate(PARAM_BOUNDS.items()):
    param_samples[:, i] = bounds[0] + param_samples[:, i] * (bounds[1] - bounds[0])

# 3. Run simulations (parallelizable, embarrassingly parallel)
trajectories = []
for params in param_samples:
    param_dict = dict(zip(PARAM_BOUNDS.keys(), params))
    merged = {**DEFAULT_PARAMS, **param_dict}
    history = run_simulation(merged)
    # Stack target trajectories: [n_targets, 80]
    target_trajectory = np.stack([history[t] for t in PRIMARY_TARGETS])
    trajectories.append(target_trajectory)

trajectories = np.array(trajectories)  # [50000, 6, 80]

# 4. Train surrogate
# Option A: MLP per target (simplest)
# Option B: Multi-output DeepONet (continuous time)
# Option C: Transformer encoder-decoder

# 5. Validate: RMSE < 2% of trajectory std, R² > 0.98
```

### 1.5 Integration Points
- **Replace Monte Carlo inner loop** in `tesm_simulation.py:256-308` → 500 trials in milliseconds
- **Enable real-time dashboard** with interactive parameter sliders
- **Nested optimization**: Bayesian optimization over surrogate for calibration
- **Global sensitivity**: Sobol indices via surrogate (10k evals in seconds)

---

## 2. Bayesian Calibration & Parameter Inference

### 2.1 Current Approach (Analytical / Grid Search)
```python
# calibrate.py:372-375 — Point estimates from formulas
downsizing_ratio = round(min(0.90, max(0.25, (overall_capex_sum / overall_rpo_sum) * 1.0)), 2)
capital_reflexivity = round(min(0.80, max(0.10, (overall_capex_sum / overall_rev_sum) * 1.5)), 2)

# historical_validation.py:192-267 — Grid search over 3 params only
e_range = np.arange(0.2, 2.3, 0.1)      # 21 values
pc_range = np.arange(0.05, 0.95, 0.05)  # 18 values
r_range = np.arange(0.1, 1.05, 0.05)    # 19 values
# 21 × 18 × 19 = 7,182 simulations per crisis × 7 crises = 50k runs
```

### 2.2 Limitations
- **Point estimates only** — no uncertainty quantification
- **Formulas are heuristic** (e.g., `* 1.0`, `* 1.5` scaling factors)
- **Grid search scales exponentially** — only 3 params optimized
- **No parameter correlations** captured
- **No propagation of data uncertainty** (SEC filing noise, LBNL sampling error)

### 2.3 Bayesian Solution: Hierarchical Probabilistic Model

```python
# bayesian_calibration.py
import pymc as pm
import pytensor.tensor as pt
from tesm_simulation import run_simulation, DEFAULT_PARAMS
import numpy as np

# Observed data from calibrate.py outputs
observed = {
    "quarterly_capex": quarterly_ts_data["capexSumB"],      # 13 quarters
    "quarterly_rpo": quarterly_ts_data["rpoSumB"],
    "quarterly_revenue": quarterly_ts_data["revSumB"],
    "historical_indices": {crisis: REAL_HISTORICAL_TRAILS[crisis]["actualIndex"] 
                          for crisis in ["dotcom", "telecom", "cloud", "smartphone"]}
}

with pm.Model() as calibration_model:
    # --- Priors from calibrate.py analytical formulas (as informative priors) ---
    
    # Downsizing ratio: calibrated formula gives ~0.35, allow ±0.15
    downsizing_ratio = pm.Beta("downsizing_ratio", alpha=12, beta=22)  # mean≈0.35
    
    # Capital reflexivity: calibrated formula gives ~0.30, allow ±0.15
    capital_reflexivity = pm.Beta("capital_reflexivity", alpha=10, beta=23)  # mean≈0.30
    
    # Elasticity: meta-analysis gives 1.25, range [0.8, 1.8]
    elasticity_coefficient = pm.Normal("elasticity_coefficient", mu=1.25, sigma=0.25)
    
    # Price compression: calibrated 0.45, range [0.2, 0.7]
    price_compression = pm.Beta("price_compression", alpha=9, beta=11)  # mean≈0.45
    
    # China convergence rate: calibrated 0.025, range [0.01, 0.05]
    china_convergence_rate = pm.Beta("china_convergence_rate", alpha=5, beta=195)  # mean≈0.025
    
    # China price compression velocity: calibrated 0.08, range [0.03, 0.15]
    china_price_compression_velocity = pm.Beta("china_pcv", alpha=8, beta=92)  # mean≈0.08
    
    # Power growth cap: LBNL-derived, range [0.03, 0.15]
    power_growth_cap = pm.Beta("power_growth_cap", alpha=4, beta=26)  # mean≈0.12
    
    # ... 15-20 total parameters with domain-informed priors
    
    # --- Likelihood: Simulator as probabilistic forward model ---
    
    # For each historical crisis, simulate and compare to actual index
    for crisis_name, actual_index in observed["historical_indices"].items():
        n_quarters = len(actual_index)
        
        # Crisis-specific base params (from get_crisis_params)
        crisis_base = get_crisis_params(crisis_name, n_quarters)
        
        # Override with inferred params
        sim_params = {**crisis_base, 
                      "downsizingRatio": downsizing_ratio,
                      "capitalReflexivity": capital_reflexivity,
                      "elasticityCoefficient": elasticity_coefficient,
                      "priceCompression": price_compression}
        
        # Run simulator (deterministic given params)
        # Note: Use surrogate for speed in production
        sim_output = run_simulation(sim_params)
        simulated_index = sim_output["indexVal"][:n_quarters]
        
        # Observation noise: heteroscedastic (larger near peaks)
        sigma = pm.HalfNormal(f"sigma_{crisis_name}", sigma=50)
        
        # Weighted likelihood (emphasize peak periods as in historical_validation.py:233)
        weights = (np.array(actual_index) / 100.0) ** 2
        
        pm.Normal(f"obs_{crisis_name}", 
                  mu=simulated_index, 
                  sigma=sigma / weights,  # Weight by importance
                  observed=actual_index)
    
    # SEC quarterly financials likelihood
    for q_idx, (capex, rpo, rev) in enumerate(zip(
        observed["quarterly_capex"], 
        observed["quarterly_rpo"], 
        observed["quarterly_revenue"])):
        
        # Simulate single quarter (or use steady-state approximation)
        # ... likelihood terms linking params to observed financials
        
        pm.Normal(f"capex_q{q_idx}", mu=model_capex, sigma=5, observed=capex)
        pm.Normal(f"rpo_q{q_idx}", mu=model_rpo, sigma=3, observed=rpo)
        pm.Normal(f"rev_q{q_idx}", mu=model_rev, sigma=5, observed=rev)

# Inference
with calibration_model:
    # Use NUTS (Hamiltonian Monte Carlo) for efficient sampling
    trace = pm.sample(2000, tune=1000, chains=4, target_accept=0.9)
    
    # Posterior summaries
    summary = pm.summary(trace, var_names=[
        "downsizing_ratio", "capital_reflexivity", "elasticity_coefficient",
        "price_compression", "china_convergence_rate", "power_growth_cap"
    ])
    print(summary)
    
    # Posterior predictive checks
    ppc = pm.sample_posterior_predictive(trace, var_names=[f"obs_{c}" for c in observed["historical_indices"]])
```

### 2.4 Outputs
| Output | Use Case |
|--------|----------|
| **Posterior distributions** for all 15-20 params | Uncertainty-aware projections |
| **Parameter correlations** (e.g., elasticity ↔ price compression) | Identify identifiability issues |
| **Posterior predictive checks** | Validate model fit to historical crises |
| **Prior-to-posterior shrinkage** | Quantify information gain from data |
| **Leave-one-crisis-out cross-validation** | Test generalization to unseen regimes |

### 2.5 Computational Strategy
- **Phase 1**: Use surrogate model (Section 1) for likelihood evaluation → minutes per chain
- **Phase 2**: Full simulator for final validation samples only
- **Phase 3**: Sequential Bayesian updating as new SEC quarters arrive

---

## 3. Generative Scenario Design

### 3.1 Current Approach (Manual Powerset)
```python
# tesm_simulation.py:217-253
scenario_defs = {
    "baseline": {},
    "A": {"tcoMultiplier": 3.0, "complianceFriction": 0.60},
    "B": {"pppAdjustment": 0.40, "priceCompression": 0.85, "openSourcePower": 0.90},
    "C": {"powerGrowthCap": 0.04, "gridConnectionDelay": 12, ...},
    "D": {"averageContractLength": 16, "downsizingRatio": 0.65, ...},
    "E": {"baseMultipleSales": 12.0, "targetMultipleSales": 2.0}
}
# Generates 2^5 - 1 = 31 combinations via powerset
```

### 3.2 Limitations
- **Human-defined extremes** — may miss plausible but non-obvious combinations
- **No probability weighting** — all 31 scenarios treated equally
- **Fixed dimensions** — cannot discover new risk dimensions
- **No adversarial stress testing** — doesn't actively seek worst cases

### 3.3 Generative ML Solutions

#### 3.3.1 Normalizing Flow for Plausible Scenario Generation
```python
# generative_scenarios.py
import torch
import torch.nn as nn
from torch.distributions import Normal, Transform, constraints
from nflows.flows import Flow
from nflows.distributions import StandardNormal
from nflows.transforms import CompositeTransform, MaskedAffineAutoregressiveTransform

# Training data: Historical crisis parameter sets + calibrated baseline + expert scenarios
# Each scenario = 20-dim parameter vector
historical_params = np.array([
    # dotcom crisis params (from optimize_historical_parameters)
    [1.8, 0.7, 0.6, 1.0, 0.85, 0.12, ...],
    # telecom crisis params
    [1.6, 0.6, 0.5, 1.0, 0.80, 0.10, ...],
    # ... 7 historical crises
    # + 31 manual scenario combinations
    # + 1000 samples from calibrated posterior (Section 2)
])

# Normalizing Flow: learns p(params) over plausible scenario space
base_dist = StandardNormal(shape=[20])
transforms = []
for _ in range(6):  # 6 flow layers
    transforms.append(MaskedAffineAutoregressiveTransform(features=20, hidden_features=128))
    transforms.append(ReversePermutation(features=20))

flow = Flow(CompositeTransform(transforms), base_dist)

# Train via maximum likelihood
optimizer = torch.optim.Adam(flow.parameters(), lr=1e-3)
for epoch in range(500):
    optimizer.zero_grad()
    loss = -flow.log_prob(torch.tensor(historical_params, dtype=torch.float32)).mean()
    loss.backward()
    optimizer.step()

# Generate novel plausible scenarios
novel_scenarios = flow.sample(1000)  # 1000 new 20-dim parameter vectors
# These are statistically consistent with historical crises + expert knowledge
```

#### 3.3.2 Adversarial Scenario Generation (Worst-Case Search)
```python
# adversarial_scenarios.py
import torch
from tesm_simulation import run_simulation
# Use differentiable surrogate from Section 1

class AdversarialScenarioFinder:
    def __init__(self, surrogate_model, param_bounds):
        self.surrogate = surrogate_model
        self.bounds = param_bounds
        
    def find_worst_case(self, target_metric="indexVal", 
                        objective="minimize",  # or "maximize_stranded"
                        n_restarts=50):
        """Find parameter combinations that extremize target metric."""
        best_params = None
        best_value = float('inf') if objective == "minimize" else -float('inf')
        
        for _ in range(n_restarts):
            # Random initialization within bounds
            params = torch.rand(len(self.bounds), requires_grad=True)
            params.data = params.data * (bounds[:,1] - bounds[:,0]) + bounds[:,0]
            
            optimizer = torch.optim.Adam([params], lr=0.1)
            
            for step in range(200):
                optimizer.zero_grad()
                # Surrogate predicts full trajectory
                trajectory = self.surrogate(params.unsqueeze(0))  # [1, n_targets, 80]
                metric_trajectory = trajectory[0, target_idx]  # [80]
                
                # Objective: minimize final value, or maximize peak stranded, etc.
                if objective == "minimize":
                    loss = metric_trajectory[-1]  # Year 20 index
                elif objective == "maximize_stranded":
                    loss = -trajectory[0, stranded_idx].max()
                elif objective == "maximize_volatility":
                    loss = -metric_trajectory.std()
                
                loss.backward()
                optimizer.step()
                
                # Project to bounds
                with torch.no_grad():
                    params.clamp_(bounds[:,0], bounds[:,1])
            
            final_value = loss.item()
            if (objective == "minimize" and final_value < best_value) or \
               (objective != "minimize" and final_value > best_value):
                best_value = final_value
                best_params = params.detach().clone()
        
        return best_params, best_value

# Usage: Find scenarios that crash the index most severely
finder = AdversarialScenarioFinder(surrogate, PARAM_BOUNDS)
worst_params, worst_index = finder.find_worst_case("indexVal", "minimize", n_restarts=100)
print(f"Worst-case Year 20 Index: {worst_index:.1f} (vs baseline ~100)")
```

#### 3.3.3 Conditional Generation for "What-If" Analysis
```python
# conditional_scenarios.py
# CVAE: Condition on partial scenario (e.g., "China converges fast") → complete scenario

class ConditionalScenarioVAE(nn.Module):
    def __init__(self, param_dim=20, condition_dim=5, latent_dim=16):
        super().__init__()
        # Encoder: p(z | params, condition)
        self.encoder = nn.Sequential(
            nn.Linear(param_dim + condition_dim, 128), nn.ReLU(),
            nn.Linear(128, 128), nn.ReLU()
        )
        self.mu = nn.Linear(128, latent_dim)
        self.logvar = nn.Linear(128, latent_dim)
        
        # Decoder: p(params | z, condition)
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim + condition_dim, 128), nn.ReLU(),
            nn.Linear(128, 128), nn.ReLU(),
            nn.Linear(128, param_dim)
        )
    
    def forward(self, params, condition):
        x = torch.cat([params, condition], dim=-1)
        h = self.encoder(x)
        mu, logvar = self.mu(h), self.logvar(h)
        z = mu + torch.exp(0.5 * logvar) * torch.randn_like(mu)
        recon = self.decoder(torch.cat([z, condition], dim=-1))
        return recon, mu, logvar, z

# Conditions: ["china_fast_convergence", "power_crisis", "regulation_heavy", ...]
# Train on historical + calibrated scenarios with condition labels
# Generate: condition = "china_fast_convergence" → sample full scenario
```

### 3.4 Scenario Quality Metrics
| Metric | Method | Threshold |
|--------|--------|-----------|
| **Plausibility** | Log-prob under normalizing flow | > 5th percentile of training data |
| **Diversity** | Pairwise parameter distance | Mean pairwise L2 > 0.3 × bound range |
| **Coverage** | Convex hull volume in param space | > 80% of expert-defined bounds |
| **Adversarial severity** | Surrogate-predicted metric extremum | > 2σ from baseline distribution |

---

## 4. Hybrid Neural-Mechanistic Modeling (Neural ODEs / SDEs)

### 4.1 Motivation
The rule-based engine encodes **known physics/economics** (power constraints, contract renewal dynamics, CapEx reflexivity). But some dynamics are **poorly understood or data-driven**:
- China model convergence trajectory (Elo gap closure rate)
- Open-source adoption diffusion curves
- Enterprise AI ROI realization lag distribution
- Regulatory regime shift dynamics

### 4.2 Neural ODE Residual Learning
```python
# neural_ode_residual.py
import torch
import torch.nn as nn
from torchdiffeq import odeint_adjoint as odeint
from tesm_simulation import run_simulation, DEFAULT_PARAMS

class TESMNeuralODE(nn.Module):
    """
    Hybrid model: dz/dt = f_mechanistic(z, t, params) + f_neural(z, t, params)
    where f_mechanistic = differentiable version of TESM step function
    and f_neural = learned residual dynamics
    """
    def __init__(self, state_dim=12, param_dim=20, hidden_dim=128):
        super().__init__()
        self.state_dim = state_dim
        self.param_dim = param_dim
        
        # Neural residual network
        self.residual_net = nn.Sequential(
            nn.Linear(state_dim + param_dim + 1, hidden_dim),  # +1 for time
            nn.Softplus(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.Softplus(),
            nn.Linear(hidden_dim, state_dim)
        )
        
        # Learnable initial condition correction
        self.ic_correction = nn.Parameter(torch.zeros(state_dim))
    
    def mechanistic_step(self, state, params, t):
        """
        Differentiable approximation of one TESM quarter step.
        This is a simplified physics-informed layer.
        In practice: use surrogate gradient or differentiable simulator.
        """
        # Key mechanistic relationships (differentiable):
        # computeSupply growth = f(siliconSupply, capex, powerGrowthCap)
        # activePower = min(computeSupply * power_per_compute, grid_capacity(t))
        # cloudRevenue = f(computeSupply, priceCompression, elasticity)
        # roic = f(cloudRevenue, capex, wacc)
        # indexVal = f(roic, multipleSales, sentiment)
        # ... implement as differentiable PyTorch operations
        return mechanistic_derivatives
    
    def forward(self, t, state, params):
        # Mechanistic derivatives
        mech_deriv = self.mechanistic_step(state, params, t)
        # Neural residual
        nn_input = torch.cat([state, params, t.expand(state.shape[0], 1)], dim=-1)
        neural_deriv = self.residual_net(nn_input)
        return mech_deriv + neural_deriv
    
    def simulate(self, params, t_span=torch.linspace(0, 80, 81)):
        # Initial state from DEFAULT_PARAMS
        init_state = self.get_initial_state(params) + self.ic_correction
        # Integrate
        trajectory = odeint(self.forward, init_state, t_span, args=(params,))
        return trajectory  # [81, state_dim]

# Training: Fit to historical crises + calibration data
def train_hybrid_model():
    model = TESMNeuralODE()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    
    for epoch in range(1000):
        # Sample crisis + params
        crisis = np.random.choice(list(REAL_HISTORICAL_TRAILS.keys()))
        actual = REAL_HISTORICAL_TRAILS[crisis]["actualIndex"]
        n = len(actual)
        t_span = torch.linspace(0, n, n+1)
        
        # Get crisis base params + sample from posterior
        crisis_params = get_crisis_params(crisis, n)
        params = sample_from_posterior(crisis_params)  # From Bayesian calibration
        params_tensor = torch.tensor(params, dtype=torch.float32)
        
        # Simulate
        pred_trajectory = model.simulate(params_tensor, t_span)
        pred_index = pred_trajectory[:, index_state_idx]
        
        # Loss: Weighted MSE (emphasize peaks)
        weights = (torch.tensor(actual) / 100.0) ** 2
        loss = (weights * (pred_index - torch.tensor(actual))**2).mean()
        
        # Regularization: Keep neural residual small (prefer mechanistic)
        reg = 0.01 * sum(p.pow(2).sum() for p in model.residual_net.parameters())
        
        total_loss = loss + reg
        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()
```

### 4.3 Neural SDE for Stochastic Dynamics
```python
# neural_sde.py
import torchsde

class TESMNeuralSDE(nn.Module):
    """
    dz = f_mechanistic(z, t) dt + g_neural(z, t) dW
    Learns both drift residual and diffusion (volatility) structure
    """
    def __init__(self, state_dim, param_dim, noise_dim=6, hidden_dim=128):
        super().__init__()
        self.drift_net = nn.Sequential(  # Residual drift
            nn.Linear(state_dim + param_dim + 1, hidden_dim),
            nn.Softplus(),
            nn.Linear(hidden_dim, state_dim)
        )
        self.diffusion_net = nn.Sequential(  # State-dependent volatility
            nn.Linear(state_dim + param_dim + 1, hidden_dim),
            nn.Softplus(),
            nn.Linear(hidden_dim, state_dim * noise_dim)
        )
    
    def f(self, t, y, params):
        mech_drift = mechanistic_step(y, params, t)
        nn_input = torch.cat([y, params, t.expand(y.shape[0], 1)], dim=-1)
        return mech_drift + self.drift_net(nn_input)
    
    def g(self, t, y, params):
        nn_input = torch.cat([y, params, t.expand(y.shape[0], 1)], dim=-1)
        return self.diffusion_net(nn_input).view(y.shape[0], self.state_dim, self.noise_dim)

# Train via maximum likelihood (Euler-Maruyama) or score matching
# Generates calibrated uncertainty bands matching historical volatility
```

### 4.4 Benefits Over Pure Mechanistic or Pure ML
| Aspect | Pure Mechanistic | Pure ML (Black Box) | Hybrid Neural-Mechanistic |
|--------|------------------|---------------------|---------------------------|
| **Extrapolation** | ✓ Physics-guaranteed | ✗ Unreliable | ✓ Constrained by physics |
| **Interpretability** | ✓ Full | ✗ None | ✓ Mechanistic core visible |
| **Data Efficiency** | ✗ Needs full specification | ✗ Needs massive data | ✓ Learns only residuals |
| **Calibration** | Manual grid search | End-to-end gradient | Gradient-based + physics |
| **Uncertainty** | Monte Carlo only | Epistemic only | Both aleatoric + epistemic |

---

## 5. Time-Series Forecasting for Boundary Conditions

### 5.1 Current State
- SEC quarterly data: 13 quarters (2023q1–2026q1) for 6 hyperscalers
- Used only for **calibration** (point estimates of CapEx, RPO, Revenue)
- Not used for **forward forecasting** of boundary conditions

### 5.2 Forecasting Targets (Feed into Simulator)
| Boundary Condition | Current Treatment | ML Forecasting Value |
|-------------------|-------------------|---------------------|
| Hyperscaler CapEx trajectory | Constant / heuristic growth | Transformer on 13-qtr panel |
| Silicon supply (semiconductor trade) | Fixed quarterly baseline | FNO on USITC monthly flows |
| Grid connection delays | LBNL mean (static) | Survival analysis on queue data |
| Chinese API pricing | Static discount factor | Time-series on 50+ model prices |
| Enterprise contract renewals | Fixed length/downsizing | Cox proportional hazards on contract data |
| Carbon price trajectory | Fixed $0 | ETS auction data + policy scenarios |

### 5.3 Architecture: Multi-Horizon Transformer
```python
# boundary_forecasting.py
import torch
import torch.nn as nn
from gluonts.torch import TransformerEstimator
from gluonts.dataset.common import ListDataset

# Prepare panel dataset: [entity, time, features]
# Entities: 6 hyperscalers + regional aggregates
# Features: capex, rpo, revenue, capex/rpo, capex/rev, stock_return, ...
# Target: Next 20 quarters (5 years) of each feature

class BoundaryConditionForecaster:
    def __init__(self, context_length=13, prediction_length=20):
        self.estimator = TransformerEstimator(
            context_length=context_length,
            prediction_length=prediction_length,
            freq="Q",  # Quarterly
            num_layers=4,
            hidden_size=128,
            num_heads=8,
            scaling=True,
            # Covariates: known future (policy dates, chip roadmaps)
            use_feat_static_cat=True,  # Entity ID
            cardinality=[10],  # Number of entities
        )
    
    def train(self, panel_data):
        # panel_data: List of dicts with "target", "start", "feat_static_cat"
        dataset = ListDataset(panel_data, freq="Q")
        self.predictor = self.estimator.train(dataset)
    
    def forecast_boundary_conditions(self, n_samples=100):
        """Returns [n_samples, 20 quarters, n_features] for each entity"""
        forecasts = self.predictor.predict(dataset, num_samples=n_samples)
        return forecasts

# Integration: Sample boundary conditions → feed into TESM simulator
# Enables "conditional projection": Given CapEx forecast distribution, what's index distribution?
```

### 5.4 Survival Analysis for Grid Queue Delays
```python
# grid_queue_survival.py
from lifelines import CoxPHFitter
import pandas as pd

# LBNL data: grid_delays from calibrate.py:75-102
# Features: project_type, region, capacity_mw, technology, interconnection_study_status
# Target: Time from Interconnection Request (IR) to Commercial Operation Date (COD)
# Censoring: Projects still in queue / withdrawn

cph = CoxPHFitter(penalizer=0.1)
cph.fit(lbnl_data, duration_col='months_ir_to_cod', event_col='completed')

# Predict distribution of delays for NEW projects with given characteristics
new_projects = pd.DataFrame({
    'project_type': ['data_center'] * 100,
    'capacity_mw': np.random.lognormal(6, 0.5, 100),  # 100-1000 MW
    'region': np.random.choice(['PJM', 'CAISO', 'ERCOT', 'MISO', 'SPP'], 100),
    'technology': np.random.choice(['battery', 'solar', 'wind', 'gas'], 100)
})

delay_distributions = cph.predict_percentile(new_projects, p=[0.1, 0.5, 0.9])
# Feed delay distributions into TESM powerGrowthCap and gridConnectionDelay params
```

---

## 6. China Competition Dynamics Modeling

### 6.1 Current Heuristic Parameters (calibrate.py:536-574)
```python
elo_gap = 40                          # US vs China frontier Elo gap
china_convergence_rate = 0.025        # 2.5% gap closure per quarter
china_price_discount = 0.94           # 94% cheaper than GPT-4o
china_price_compression_velocity = 0.08  # 8% additional compression per quarter
china_open_weight_share = 0.65        # 65% open-weight
china_frontier_lag = 2                # Quarters to reach US frontier
```

### 6.2 ML Enhancements

#### 6.2.1 Competitive RL Environment
```python
# china_competition_rl.py
import gymnasium as gym
from gymnasium import spaces
import numpy as np

class AICompetitionEnv(gym.Env):
    """
    Two-agent RL: US Frontier Lab vs Chinese Lab Consortium
    State: [US_elo, CN_elo, US_price, CN_price, US_open_weight_share, CN_open_weight_share,
            US_compute_budget, CN_compute_budget, regulation_level, ...]
    Actions: [R&D_investment, price_change, open_source_release, compute_allocation, ...]
    Reward: Market share × margin (or strategic objective)
    """
    def __init__(self):
        self.observation_space = spaces.Box(low=0, high=1, shape=(15,), dtype=np.float32)
        self.action_space = spaces.Box(low=-1, high=1, shape=(8,), dtype=np.float32)
        
        # Calibrated transition dynamics from historical benchmark data
        self.transition_model = self._build_transition_model()
    
    def step(self, actions):
        us_action, cn_action = actions[:4], actions[4:]
        
        # Elo dynamics: R&D → capability improvement
        # Price dynamics: Cost reduction + strategic pricing
        # Open-source dynamics: Release decisions → adoption → talent attraction
        # Compute dynamics: Budget allocation → training runs → Elo gains
        
        next_state = self.transition_model(self.state, us_action, cn_action)
        us_reward = self._compute_reward(next_state, "US")
        cn_reward = self._compute_reward(next_state, "CN")
        
        self.state = next_state
        return next_state, (us_reward, cn_reward), False, False, {}
    
    def _build_transition_model(self):
        # Train on china_benchmarks + china_api_pricing time series
        # Use neural ODE or transformer to learn state transitions
        pass

# Train via self-play (PPO, SAC) → emergent competitive dynamics
# Extract: Convergence rate distributions, price war probabilities, 
#          open-source tipping points, compute arms race equilibria
```

#### 6.2.2 Transformer Forecasting on Benchmark Data
```python
# china_benchmark_forecasting.py
# china_benchmarks table: [model, organization, date, score, model_type, params, ...]
# Monthly frequency from 2023-present

from gluonts.torch import TemporalFusionTransformerEstimator

# Multivariate forecast: Elo scores + API prices + open-weight indicators
# For top-10 Chinese labs + US frontier
estimator = TemporalFusionTransformerEstimator(
    freq="M",
    prediction_length=12,  # 12 months ahead
    context_length=24,
    hidden_size=64,
    num_heads=4,
    dropout_rate=0.1,
    # Static covariates: org_type (big_tech, startup, academic), funding, compute_access
    use_feat_static_cat=True,
    cardinality=[3, 10],  # org_type, lab_id
)

# Outputs: Distribution over future Elo gaps, price discounts, open-weight shares
# Directly feeds into TESM china_* parameters with uncertainty
```

---

## 7. Sensitivity Analysis Acceleration

### 7.1 Current State (sensitivity_analysis.py)
- **Sobol**: 768 simulations (64 Saltelli samples × 12 params) — requires SALib
- **OAT fallback**: 10 steps × 5 params × 3 metrics = 150 simulations
- Both use full simulator → slow

### 7.2 ML-Accelerated Sensitivity

#### 7.2.1 Active Subspace Detection
```python
# active_subspace.py
import numpy as np
from scipy.linalg import eigh

def compute_active_subspace(surrogate, param_bounds, n_samples=10000):
    """
    Identify linear combinations of parameters that drive output variance.
    Reduces 20-dim sensitivity to 2-3 active directions.
    """
    # Sample parameters
    X = np.random.uniform(param_bounds[:,0], param_bounds[:,1], (n_samples, 20))
    
    # Gradient of output w.r.t parameters (via autodiff on surrogate)
    gradients = []
    for x in X:
        x_tensor = torch.tensor(x, requires_grad=True, dtype=torch.float32)
        y = surrogate(x_tensor.unsqueeze(0))[:, 0, -1]  # Year 20 index
        grad = torch.autograd.grad(y, x_tensor)[0].detach().numpy()
        gradients.append(grad)
    
    G = np.array(gradients)  # [n_samples, 20]
    
    # Covariance of gradients
    C = G.T @ G / n_samples
    
    # Eigendecomposition
    eigenvalues, eigenvectors = eigh(C)
    
    # Active subspace: top-k eigenvectors
    k = np.sum(eigenvalues > 0.01 * eigenvalues[-1])  # Eigenvalue threshold
    W1 = eigenvectors[:, -k:]  # Active directions
    W2 = eigenvectors[:, :-k]  # Inactive directions
    
    return W1, W2, eigenvalues

# Usage: Project Sobol analysis onto active subspace only
# Reduces effective dimensionality from 20 → 3-5
```

#### 7.2.2 Shapley Value Estimation via Surrogate
```python
# shapley_sensitivity.py
import shap

def compute_shapley_sensitivity(surrogate, param_bounds, baseline_params, n_samples=2000):
    """
    Global sensitivity via Shapley values (game-theoretic attribution).
    Works with any surrogate model.
    """
    # Background dataset for SHAP
    background = np.random.uniform(param_bounds[:,0], param_bounds[:,1], (500, 20))
    
    # Explain Year 20 index
    def model_fn(X):
        return surrogate(torch.tensor(X, dtype=torch.float32))[:, 0, -1].detach().numpy()
    
    explainer = shap.KernelExplainer(model_fn, background)
    shap_values = explainer.shap_values(baseline_params.reshape(1, -1), nsamples=n_samples)
    
    # shap_values[0] = [20] array of attributions
    # Sum = f(baseline) - E[f(X)]
    return shap_values[0]

# Advantages over Sobol:
# - Handles correlated parameters naturally
# - Local + global interpretability
# - Model-agnostic (works with any surrogate)
# - O(n_samples × n_params) vs Sobol's O(n_samples × 2^n_params)
```

---

## 8. Anomaly Detection & Regime Change Monitoring

### 8.1 Motivation
- New SEC quarters arrive every 3 months
- Structural breaks: Policy shifts (CHIPS Act, export controls), breakthroughs (new architecture), crises
- Current: Manual recalibration when "things look different"

### 8.2 Online Changepoint Detection
```python
# regime_detection.py
from ruptures import Binseg, Pelt
import numpy as np

class RegimeMonitor:
    def __init__(self, window_size=8, min_segment=4):
        self.window_size = window_size
        self.min_segment = min_segment
        self.history = []  # Stores [quarter, capex, rpo, revenue, ...] for each hyperscaler
        
    def add_quarter(self, quarter_data):
        """quarter_data: dict with keys for each hyperscaler's metrics"""
        self.history.append(quarter_data)
        if len(self.history) > self.window_size:
            self.history.pop(0)
    
    def detect_changepoints(self):
        if len(self.history) < self.min_segment * 2:
            return []
        
        # Aggregate signal: CapEx/Revenue ratio (capital_reflexivity proxy)
        signal = np.array([h['aggregate_capex'] / h['aggregate_revenue'] 
                          for h in self.history])
        
        # PELT algorithm for changepoint detection
        model = "rbf"  # or "linear", "ar"
        algo = Pelt(model=model, min_size=self.min_segment).fit(signal)
        changepoints = algo.predict(pen=10)  # Penalty tuned on historical breaks
        
        # Map to quarters
        return [self.history[i]['quarter'] for i in changepoints if i < len(self.history)]
    
    def trigger_recalibration(self):
        """Called when changepoint detected with high confidence"""
        # 1. Re-run Bayesian calibration (Section 2) with updated data
        # 2. Update prior distributions for affected parameters
        # 3. Re-generate scenario set (Section 3) with new regime
        # 4. Alert dashboard users
        pass

# Integration: Run after each SEC quarter ingestion in calibrate.py
```

### 8.3 Multivariate Anomaly Detection on Full Panel
```python
# multivariate_anomaly.py
from pyod.models.ecod import ECOD
from pyod.models.deep_svdd import DeepSVDD

class PanelAnomalyDetector:
    def __init__(self):
        # Features per quarter: 6 hyperscalers × 5 metrics = 30-dim
        self.detector = DeepSVDD(epochs=100, batch_size=32)
        self.scaler = StandardScaler()
        self.trained = False
    
    def train_baseline(self, historical_panel):
        """historical_panel: [n_quarters, 30]"""
        X = self.scaler.fit_transform(historical_panel)
        self.detector.fit(X)
        self.trained = True
    
    def score_quarter(self, quarter_panel):
        """Returns anomaly score; high = potential regime shift"""
        if not self.trained:
            return 0.0
        X = self.scaler.transform(quarter_panel.reshape(1, -1))
        return self.detector.decision_function(X)[0]
```

---

## 9. Implementation Roadmap

### Phase 1: Foundation (Weeks 1-4)
| Task | Deliverable | Effort |
|------|-------------|--------|
| 1.1 Build training data generator for surrogate | `generate_surrogate_data.py` (50k samples) | 1 week |
| 1.2 Train MLP surrogate for 6 primary targets | `surrogate_model.pt` + validation report | 1 week |
| 1.3 Integrate surrogate into Monte Carlo loop | Modified `tesm_simulation.py:256-308` | 3 days |
| 1.4 Benchmark: 500 trials in <1s vs 30s | Performance report | 2 days |

### Phase 2: Bayesian Calibration (Weeks 5-8)
| Task | Deliverable | Effort |
|------|-------------|--------|
| 2.1 Define PyMC model with 15-20 parameters | `bayesian_calibration.py` | 1 week |
| 2.2 Run NUTS inference with surrogate likelihood | Posterior samples (4 chains × 2000) | 1 week |
| 2.3 Posterior predictive checks on 7 crises | Validation plots + LOO-CV scores | 3 days |
| 2.4 Replace point estimates in `calibrate.py` | Updated param_overrides.json with distributions | 2 days |

### Phase 3: Generative Scenarios (Weeks 9-12)
| Task | Deliverable | Effort |
|------|-------------|--------|
| 3.1 Train normalizing flow on historical + posterior scenarios | `scenario_flow.pt` | 1 week |
| 3.2 Implement adversarial scenario finder | `adversarial_scenarios.py` | 1 week |
| 3.3 Generate 1000 novel scenarios + quality filtering | `generated_scenarios.json` | 3 days |
| 3.4 Replace manual powerset in scenario matrix | Modified `tesm_simulation.py:217-253` | 2 days |

### Phase 4: Hybrid Neural-Mechanistic (Weeks 13-20)
| Task | Deliverable | Effort |
|------|-------------|--------|
| 4.1 Build differentiable mechanistic layer | `mechanistic_step_torch.py` | 2 weeks |
| 4.2 Train Neural ODE residual on crises | `neural_ode_residual.pt` | 2 weeks |
| 4.3 Train Neural SDE for volatility | `neural_sde.pt` | 1 week |
| 4.4 Validate extrapolation beyond training regimes | Stress test report | 1 week |

### Phase 5: Forecasting & Monitoring (Weeks 21-28)
| Task | Deliverable | Effort |
|------|-------------|--------|
| 5.1 Multi-horizon Transformer for boundary conditions | `boundary_forecaster.pt` | 2 weeks |
| 5.2 Survival analysis for grid queues | `grid_survival_model.pkl` | 1 week |
| 5.3 RL environment for China competition | `china_competition_env.py` | 2 weeks |
| 5.4 Online changepoint detector + alerting | `regime_monitor.py` | 1 week |
| 5.5 End-to-end integration testing | Full pipeline validation | 2 weeks |

---

## 10. Risk Assessment & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Surrogate extrapolation failure** | Medium | High | Active learning: flag low-density regions, fall back to full simulator |
| **Bayesian calibration non-identifiability** | High | Medium | Prior sensitivity analysis; fix non-identified params to calibrated values |
| **Generative scenarios implausible** | Medium | Medium | Plausibility filter (flow log-prob); expert review loop |
| **Neural ODE training instability** | High | High | Gradient clipping; adjoint method; mechanistic regularization |
| **Data scarcity for China RL** | High | Medium | Transfer learning from US lab dynamics; synthetic pre-training |
| **Regulatory/compliance on ML models** | Low | High | Document all ML components; maintain mechanistic audit trail |
| **Computational cost of full pipeline** | Low | Medium | Surrogate-first design; incremental training; cloud burst capability |

---

## 11. Tooling & Infrastructure Requirements

### 11.1 Python Packages (Add to requirements.txt)
```txt
# Core ML
torch>=2.3
pymc>=5.16
pytensor>=2.10
numpyro>=0.13  # Alternative to PyMC

# Surrogate & Neural ODE
torchdiffeq>=0.2.3
torchsde>=0.2.5
nflows>=0.14  # Normalizing flows

# Forecasting
gluonts>=0.14
torchmetrics>=1.4

# Sensitivity & Interpretability
shap>=0.44
SALib>=1.5

# Anomaly Detection
ruptures>=1.2
pyod>=1.1

# RL
gymnasium>=0.29
stable-baselines3>=2.0

# Utilities
optuna>=3.6  # Bayesian optimization
hydra-core>=1.3  # Config management
wandb>=0.17  # Experiment tracking
```

### 11.2 Compute Requirements
| Component | Training Compute | Inference Compute |
|-----------|-----------------|-------------------|
| Surrogate (MLP) | 1 GPU-hour (RTX 3080) | <1ms per batch |
| Bayesian Calibration | 4 CPU-hours (surrogate likelihood) | N/A |
| Normalizing Flow | 2 GPU-hours | <1ms per sample |
| Neural ODE | 8 GPU-hours | ~10ms per trajectory |
| Transformer Forecaster | 4 GPU-hours | ~50ms per forecast |
| China RL | 50+ GPU-hours (self-play) | N/A (offline policy) |

**Recommendation**: Start with CPU-only (surrogate + PyMC) — no GPU required for Phases 1-3.

---

## 12. Success Metrics

| Metric | Baseline (Current) | Target (With ML/DL) |
|--------|-------------------|---------------------|
| Monte Carlo 500 trials runtime | ~30 seconds | **<500 ms** (surrogate) |
| Calibration parameters with uncertainty | 3 (grid search) | **15-20** (Bayesian posterior) |
| Historical crisis RMSE (dotcom) | ~200-300 | **<150** (hybrid neural-mechanistic) |
| Scenario coverage (parameter space volume) | 31 fixed points | **1000+ plausible + adversarial** |
| Sensitivity analysis runtime | 768 sims (Sobol) | **<10 seconds** (Shapley on surrogate) |
| Regime detection latency | Manual (quarterly) | **Automated (per quarter ingest)** |
| China convergence forecast horizon | Heuristic (2 qtr lag) | **12-month probabilistic forecast** |

---

## 13. Appendix: File Map for ML Integration

```
projections/
├── engine/
│   ├── tesm_simulation.py          # ← Integrate surrogate Monte Carlo
│   ├── calibrate.py                # ← Replace point estimates with Bayesian posteriors
│   ├── historical_validation.py    # ← Use hybrid model for calibration
│   ├── sensitivity_analysis.py     # ← Shapley/active subspace on surrogate
│   ├── surrogate_model.py          # NEW: Neural surrogate training/inference
│   ├── bayesian_calibration.py     # NEW: PyMC calibration pipeline
│   ├── generative_scenarios.py     # NEW: Normalizing flow + adversarial
│   ├── neural_ode_residual.py      # NEW: Hybrid neural-mechanistic
│   ├── boundary_forecasting.py     # NEW: Transformer forecaster
│   ├── regime_monitor.py           # NEW: Changepoint detection
│   └── china_competition_rl.py     # NEW: Competitive RL environment
├── databases/
│   └── master_consolidated.duckdb  # ← Source for all ML training data
├── ml_models/                      # NEW: Trained model artifacts
│   ├── surrogate_model.pt
│   ├── bayesian_posterior.nc
│   ├── scenario_flow.pt
│   ├── neural_ode_residual.pt
│   ├── boundary_forecaster.pt
│   └── china_competition_policy.zip
├── scripts/
│   ├── train_surrogate.py
│   ├── run_bayesian_calibration.py
│   ├── generate_scenarios.py
│   ├── train_neural_ode.py
│   └── forecast_boundaries.py
└── ML_DL_OPPORTUNITIES_REPORT.md   # ← This document
```

---

## 14. Conclusion

The TESM codebase is **exceptionally well-positioned** for ML/DL augmentation:

1. **Rich, structured data** (54 tables, 13-quarter panel, 7 historical crises)
2. **Clear mechanistic core** with differentiable structure (power laws, renewal dynamics, CapEx reflexivity)
3. **Well-defined calibration targets** (historical indices, SEC financials)
4. **Explicit uncertainty sources** (parameter, structural, scenario, data)

**Start with the surrogate model (Phase 1)** — it unlocks all downstream capabilities (Bayesian calibration, generative scenarios, fast sensitivity, real-time dashboards) with minimal risk and immediate ROI.

The hybrid neural-mechanistic approach (Phase 4) is the **long-term differentiator**: it preserves the TESM's interpretability and extrapolation guarantees while learning the "dark matter" dynamics that pure mechanistic models miss.

---

*End of Report*