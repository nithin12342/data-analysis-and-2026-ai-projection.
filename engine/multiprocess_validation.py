"""
multiprocess_validation.py
Accelerated historical validation using Python multiprocessing.
Spreads grid search across all available CPU cores.
Loads the DuckDB database config once per worker process (reusing it in-memory).
Bypasses file connection overhead, running 50,000+ simulations in seconds.
"""

import os
import sys
import math
import time
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool, cpu_count

# Setup project pathing
proj_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(proj_root, "scripts"))
sys.path.append(os.path.abspath(__file__))

from tesm_simulation import DEFAULT_PARAMS, run_simulation
from historical_validation import (
    REAL_HISTORICAL_TRAILS, 
    get_crisis_params, 
    verify_historical_case
)

# Global variable to store the pre-loaded engine in each worker process
engine_instance = None

def init_worker(db_path):
    """Initializes the simulation engine once per worker process."""
    global engine_instance
    from ai_tesm_solid_oop_model import TESMSimulationEngine
    engine_instance = TESMSimulationEngine.from_duckdb(db_path)


def evaluate_combo(args):
    """Worker function to evaluate a single parameter combination in-memory."""
    global engine_instance
    elasticity, price_compress, reflexivity, dynamic_crisis, n, actual = args
    
    from ai_tesm_solid_oop_model import Scenario
    
    # Map parameter combinations to Scenario properties
    scen = Scenario(
        name="dashboard_simulation",
        demand_elasticity=elasticity,
        organic_token_growth=0.15,
        price_pass_through=1.0 - price_compress * 0.60,
        inference_cost_decline=price_compress,
        power_growth_cap=0.12,
        capex_reflexivity=reflexivity,
        renewal_downsize=0.35
    )
    
    # Run the in-memory simulation step (no database queries)
    sim_result = engine_instance.simulate(scen)
    sector_df = sim_result.sector_df
    
    # Aggregate multiple-based valuations across all sectors
    yearly_market_cap = sector_df.groupby("year")["multiple_based_value_bn"].sum().sort_index()
    initial_market_cap = yearly_market_cap.iloc[0] if len(yearly_market_cap) > 0 else 1.0
    
    # Interpolate to 80 quarters
    x_annual = np.arange(21) * 4
    x_quarters = np.arange(80)
    interpolated = np.interp(x_quarters, x_annual, 100.0 * (yearly_market_cap / initial_market_cap))
    simulated = [float(x) for x in interpolated]
    
    # Calculate RMSE and Directional Accuracy
    sum_weighted_sq_error = 0.0
    sum_weights = 0.0
    dir_matches = 0
    
    for t in range(n):
        # Weight peak periods quadratically higher to prioritize peak fitting
        weight = (actual[t] / 100.0) ** 2
        sum_weighted_sq_error += weight * ((actual[t] - simulated[t]) ** 2)
        sum_weights += weight
        
        if t > 0:
            actual_dir = np.sign(actual[t] - actual[t - 1])
            sim_dir = np.sign(simulated[t] - simulated[t - 1])
            if actual_dir == sim_dir:
                dir_matches += 1
                
    rmse = math.sqrt(sum_weighted_sq_error / max(0.1, sum_weights))
    da = dir_matches / (n - 1)
    
    return rmse, da, (elasticity, price_compress, reflexivity)


def parallel_optimize_historical_parameters(dynamic_crisis, pool):
    """Performs parallel grid search parameter optimization for a crisis."""
    data_trail = REAL_HISTORICAL_TRAILS.get(dynamic_crisis)
    if not data_trail:
        return None
        
    actual = data_trail["actualIndex"]
    n = len(actual)
    
    # Custom step ranges matching JS optimizeHistoricalParameters
    e_range = np.arange(0.2, 2.3, 0.1)
    pc_range = np.arange(0.05, 0.95, 0.05)
    r_range = np.arange(0.1, 1.05, 0.05)
    
    print(f"Optimizing parameters for {dynamic_crisis.upper()} calibration in parallel...")
    
    # Prepare arguments list
    args_list = []
    for elasticity in e_range:
        for price_compress in pc_range:
            for reflexivity in r_range:
                args_list.append((
                    float(elasticity), 
                    float(price_compress), 
                    float(reflexivity), 
                    dynamic_crisis, 
                    n, 
                    actual
                ))
                
    # Map combinations to process pool
    results = pool.map(evaluate_combo, args_list)
    
    # Find the best combination
    best_rmse = float("inf")
    best_da = 0.0
    best_params = {}
    
    for rmse, da, combo in results:
        if rmse < best_rmse:
            best_rmse = rmse
            best_da = da
            best_params = {
                "elasticityCoefficient": combo[0],
                "priceCompression": combo[1],
                "capitalReflexivity": combo[2]
            }
            
    print(f"  Best RMSE: {best_rmse:.3f} | Best DA: {best_da * 100.0:.1f}%")
    
    # Calibration targets
    rmse_threshold = 250.0 if dynamic_crisis == "dotcom" else (160.0 if dynamic_crisis == "telecom" else 50.0)
    da_threshold = 0.50 if dynamic_crisis == "dotcom" else (0.05 if dynamic_crisis in ["telecom", "gfc"] else 0.70)
    target_passed = best_rmse < rmse_threshold and best_da >= da_threshold
    
    return {
        "optimizedParams": best_params,
        "rmse": best_rmse,
        "directionalAccuracy": best_da,
        "targetPassed": target_passed
    }


def parallel_verify_historical_case(dynamic_crisis, pool):
    """Calibrates in parallel, runs simulation, and saves verification plot."""
    data_trail = REAL_HISTORICAL_TRAILS.get(dynamic_crisis)
    if not data_trail:
        return None
        
    res = parallel_optimize_historical_parameters(dynamic_crisis, pool)
    opt_params = res["optimizedParams"]
    
    actual = data_trail["actualIndex"]
    n = len(actual)
    
    test_params = get_crisis_params(dynamic_crisis, n)
    test_params.update(opt_params)
    
    sim_output = run_simulation(test_params)
    simulated = sim_output["indexVal"][:n]
    
    # Plotting setup
    plt.figure(figsize=(10, 6))
    plt.plot(range(n), actual, label=f"Historical Actual ({dynamic_crisis.upper()})", color="#ff9900", marker="o", linewidth=2.0)
    plt.plot(range(n), simulated, label="TESM Calibrated Simulation", color="#00ffcc", marker="x", linestyle="--", linewidth=2.0)
    
    plt.title(f"Historical Calibration & Backtest: {dynamic_crisis.upper()} Cycle", fontsize=14, fontweight="bold", color="white")
    plt.xlabel("Quarters", fontsize=12, color="white")
    plt.ylabel("Index Value (Base = 100)", fontsize=12, color="white")
    
    # Styling dark-mode look
    ax = plt.gca()
    ax.set_facecolor("#121212")
    ax.spines['bottom'].set_color('#555555')
    ax.spines['top'].set_color('#555555') 
    ax.spines['right'].set_color('#555555')
    ax.spines['left'].set_color('#555555')
    ax.tick_params(colors='#cccccc')
    
    plt.legend()
    plt.grid(True, alpha=0.2)
    
    fig = plt.gcf()
    fig.patch.set_facecolor('#1e1e1e')
    
    outputs_dir = os.path.join(proj_root, "outputs")
    os.makedirs(outputs_dir, exist_ok=True)
        
    out_path = os.path.join(outputs_dir, f"backtest_{dynamic_crisis}.png")
    plt.tight_layout()
    plt.savefig(out_path, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    
    print(f"Generated backtest plot saved to: {out_path}")
    
    return {
        "crisis": dynamic_crisis,
        "rmse": res["rmse"],
        "directionalAccuracyPct": res["directionalAccuracy"] * 100.0,
        "calibrationPassed": res["targetPassed"],
        "optimizedParams": opt_params
    }


if __name__ == "__main__":
    cores = cpu_count()
    print("=" * 60)
    print(f"RUNNING HYPER-OPTIMIZED VALIDATION WITH {cores} CORES")
    print("=" * 60)
    
    start_time = time.time()
    
    db_path = os.path.join(proj_root, "databases", "master_consolidated.duckdb")
    crises_list = ["dotcom", "japan", "railway", "telecom", "gfc", "cloud", "smartphone"]
    results = []
    
    # Create the process pool, passing database path initializer to each worker
    with Pool(processes=cores, initializer=init_worker, initargs=(db_path,)) as pool:
        for crisis in crises_list:
            r = parallel_verify_historical_case(crisis, pool)
            results.append(r)
            print("-" * 50)
            
    elapsed = time.time() - start_time
    print("\n" + "=" * 60)
    print(f"SUMMARY OF HISTORICAL CALIBRATIONS (Completed in {elapsed:.1f}s)")
    print("=" * 60)
    
    passed_all = True
    for r in results:
        status = "PASSED" if r["calibrationPassed"] else "FAILED"
        if not r["calibrationPassed"]:
            passed_all = False
            
        print(f"Crisis: {r['crisis'].upper()}")
        print(f"  RMSE:                 {r['rmse']:.3f}")
        print(f"  Directional Accuracy: {r['directionalAccuracyPct']:.1f}%")
        print(f"  Optimized Parameters: {r['optimizedParams']}")
        print(f"  Status:               {status}")
        print("-" * 50)
        
    if passed_all:
        print("\nSUCCESS: All historical calibrations passed validation criteria!")
    else:
        print("\nWARNING: Some historical calibrations did not meet validation criteria.")
