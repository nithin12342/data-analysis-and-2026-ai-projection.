from tesm_simulation import run_simulation, generate_scenario_matrix

matrix = generate_scenario_matrix()

print("Onsite Power Generation Capacity Q80:")
print(f"{'Scenario':<15} | {'Onsite Capacity (MW)':<20} | {'Active Power (GW)':<18}")
print("-" * 60)

for name in ["baseline", "C", "E", "C+E"]:
    sim = matrix[name]
    print(f"{name:<15} | {sim['onsiteGenCapacityMW'][-1]:<20.1f} | {sim['activePower'][-1]:<18.2f}")
