from tesm_simulation import run_simulation, generate_scenario_matrix
import numpy as np

matrix = generate_scenario_matrix()

print("Scenario Matrix Late-Stage Growth Rates:")
print(f"{'Scenario':<15} | {'Q60 Index':<10} | {'Q80 Index':<10} | {'Ann. Growth':<12}")
print("-" * 55)

for name, sim in matrix.items():
    idx_q60 = sim['indexVal'][60]
    idx_q80 = sim['indexVal'][79]
    ann_growth = (idx_q80 / max(0.1, idx_q60)) ** (1/5) - 1
    print(f"{name:<15} | {idx_q60:<10.1f} | {idx_q80:<10.1f} | {ann_growth*100:.1f}%")
