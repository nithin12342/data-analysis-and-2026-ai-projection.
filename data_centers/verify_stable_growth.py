from tesm_simulation import run_simulation
import numpy as np

# Run simulation with "Optimistic Stable Growth" parameters
sim = run_simulation({
    'elasticityCoefficient': 1.60,      # Highly elastic demand (strong Jevons Paradox)
    'powerGrowthCap': 0.22,             # Accelerated power grid growth
    'gridConnectionDelay': 3,           # Fast-track permitting (3 quarters instead of 6)
    'complianceFriction': 0.02,         # Low regulatory overhead
    'tcoMultiplier': 1.1,               # Minimal human-in-the-loop audit cost
    'baseMultipleSales': 10.0,          # High multiple support
    'wacc': 0.075                       # Low cost of capital
})

final_idx = sim['indexVal'][-1]
overall_cagr = (final_idx / 100.0) ** (1/20) - 1

print(f"Optimistic Parameter Simulation Results:")
print(f"  Final Index Value Q80: {final_idx:.1f}")
print(f"  Overall 20-Year CAGR:   {overall_cagr*100:.2f}%")
print(f"  Final ROIC:             {sim['roic'][-1]*100:.1f}%")
print(f"  Peak Stranded Compute:  {max(sim['strandedCapacity']):.1f} units")
