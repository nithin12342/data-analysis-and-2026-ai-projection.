"""
sensitivity_analysis.py
Performs global parameter sensitivity sweeps for the TESM model.
Supports two modes:
1. Standard One-At-a-Time (OAT) parameter sweeps (fallback with zero dependencies).
2. High-fidelity Sobol Sensitivity Analysis (activates if SALib is installed).
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from tesm_simulation import DEFAULT_PARAMS, run_simulation

# Parameter configurations
SENSITIVITY_PARAMS = {
    "elasticityCoefficient": {"default": 1.25, "bounds": [0.5, 2.0], "label": "Demand Elasticity"},
    "priceCompression": {"default": 0.45, "bounds": [0.2, 0.8], "label": "Price Compression / Churn"},
    "capitalReflexivity": {"default": 0.30, "bounds": [0.0, 0.9], "label": "Capital Reflexivity"},
    "tcoMultiplier": {"default": 1.5, "bounds": [1.0, 2.5], "label": "TCO Multiplier"},
    "downsizingRatio": {"default": 0.35, "bounds": [0.1, 0.8], "label": "Downsizing Churn Ratio"}
}

TARGET_METRICS = {
    "indexVal": "Year 20 Index Value (Asset Price Index)",
    "cloudRevenue": "Year 10 Cloud Revenue (monetized AI Spend)",
    "roic": "Year 10 Enterprise ROIC"
}

def run_oat_analysis(artifacts_dir):
    """Runs a standard One-At-a-Time parameter sensitivity analysis."""
    print("Running standard One-At-a-Time (OAT) parameter sweep...")
    steps = 10
    
    for metric_key, metric_label in TARGET_METRICS.items():
        plt.figure(figsize=(10, 6))
        
        for param_name, param_info in SENSITIVITY_PARAMS.items():
            param_range = np.linspace(param_info["bounds"][0], param_info["bounds"][1], steps)
            metric_outputs = []
            
            for val in param_range:
                test_params = dict(DEFAULT_PARAMS)
                test_params[param_name] = float(val)
                sim_res = run_simulation(test_params)
                
                # Fetch target metric value at index 40 (Year 10) or 79 (Year 20)
                if metric_key == "indexVal":
                    metric_val = sim_res["indexVal"][-1]  # Y20
                else:
                    metric_val = sim_res[metric_key][40]  # Y10
                metric_outputs.append(metric_val)
                
            plt.plot(param_range, metric_outputs, label=param_info["label"], marker='o', linewidth=2)
            
        plt.title(f"OAT Sensitivity Analysis: {metric_label}", fontsize=14, fontweight="bold", color="white")
        plt.xlabel("Normalized Parameter Range", fontsize=12, color="white")
        plt.ylabel("Output Metric Value", fontsize=12, color="white")
        
        # Dark styling
        ax = plt.gca()
        ax.set_facecolor("#121212")
        ax.spines['bottom'].set_color('#555555')
        ax.spines['top'].set_color('#555555')
        ax.spines['right'].set_color('#555555')
        ax.spines['left'].set_color('#555555')
        ax.tick_params(colors='#cccccc')
        plt.legend(facecolor='#1e1e1e', labelcolor='white')
        plt.grid(True, alpha=0.15)
        
        fig = plt.gcf()
        fig.patch.set_facecolor('#1e1e1e')
        plt.tight_layout()
        
        out_path = os.path.join(artifacts_dir, f"sensitivity_oat_{metric_key}.png")
        plt.savefig(out_path, facecolor=fig.get_facecolor(), edgecolor='none')
        plt.close()
        print(f"  Saved OAT sensitivity plot to: {out_path}")


def run_sobol_analysis(artifacts_dir):
    """Runs a formal Sobol Sensitivity Analysis using SALib."""
    from SALib.sample import saltelli
    from SALib.analyze import sobol
    
    print("Running high-fidelity Sobol Sensitivity Analysis...")
    
    # 1. Define problem definition for SALib
    names = list(SENSITIVITY_PARAMS.keys())
    bounds = [SENSITIVITY_PARAMS[name]["bounds"] for name in names]
    
    problem = {
        'num_vars': len(names),
        'names': names,
        'bounds': bounds
    }
    
    # 2. Sample parameter space (Saltelli method)
    # N=64 results in N * (2D + 2) = 64 * 12 = 768 simulations
    param_values = saltelli.sample(problem, 64)
    print(f"  Generated {len(param_values)} parameter combinations for Sobol sample.")
    
    # 3. Evaluate models
    y_index = []
    y_revenue = []
    
    for i, params_subset in enumerate(param_values):
        test_params = dict(DEFAULT_PARAMS)
        for idx, param_name in enumerate(names):
            test_params[param_name] = float(params_subset[idx])
            
        sim_res = run_simulation(test_params)
        y_index.append(sim_res["indexVal"][-1])
        y_revenue.append(sim_res["cloudRevenue"][40])
        
    y_index = np.array(y_index)
    y_revenue = np.array(y_revenue)
    
    # 4. Perform Sobol analysis
    si_index = sobol.analyze(problem, y_index)
    si_rev = sobol.analyze(problem, y_revenue)
    
    # 5. Plot first-order (S1) and total-order (ST) indices
    plt.figure(figsize=(12, 6))
    x = np.arange(len(names))
    width = 0.35
    
    plt.bar(x - width/2, si_index['S1'], width, label='First Order (S1) - Price Index', color='#00ffcc')
    plt.bar(x + width/2, si_index['ST'], width, label='Total Effect (ST) - Price Index', color='#ff9900', alpha=0.7)
    
    labels = [SENSITIVITY_PARAMS[n]["label"] for n in names]
    plt.xticks(x, labels, rotation=15, ha='right', color='white')
    plt.title("Sobol Global Sensitivity Analysis (Asset Price Index)", fontsize=14, fontweight="bold", color="white")
    plt.ylabel("Sensitivity Index", fontsize=12, color="white")
    
    # Styling
    ax = plt.gca()
    ax.set_facecolor("#121212")
    ax.spines['bottom'].set_color('#555555')
    ax.spines['top'].set_color('#555555')
    ax.spines['right'].set_color('#555555')
    ax.spines['left'].set_color('#555555')
    ax.tick_params(colors='#cccccc')
    plt.legend(facecolor='#1e1e1e', labelcolor='white')
    plt.grid(True, alpha=0.15)
    
    fig = plt.gcf()
    fig.patch.set_facecolor('#1e1e1e')
    plt.tight_layout()
    
    out_path = os.path.join(artifacts_dir, "sensitivity_sobol_price_index.png")
    plt.savefig(out_path, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"  Saved Sobol sensitivity plot to: {out_path}")
    
    # Write statistical summary report
    rep_path = os.path.join(artifacts_dir, "sensitivity_analysis_report.md")
    with open(rep_path, 'w') as f:
        f.write("# Global Sensitivity Analysis Report (Sobol Indices)\n\n")
        f.write("A Sobol variance-based sensitivity analysis was conducted to quantify parameter contributions to output variance.\n\n")
        f.write("| Parameter | First-Order Index ($S_1$) | Total-Effect Index ($S_T$) |\n")
        f.write("|---|---|---|\n")
        for idx, name in enumerate(names):
            f.write(f"| {SENSITIVITY_PARAMS[name]['label']} | {si_index['S1'][idx]:.4f} | {si_index['ST'][idx]:.4f} |\n")
    print(f"  Saved sensitivity markdown report to: {rep_path}")


if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING GLOBAL PARAMETER SENSITIVITY ANALYSIS")
    print("=" * 60)
    
    # Setup outputs folder
    proj_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    outputs_dir = os.path.join(proj_root, "outputs")
    os.makedirs(outputs_dir, exist_ok=True)
    
    # Try running Sobol; fallback to OAT if SALib is missing
    try:
        import SALib
        run_sobol_analysis(outputs_dir)
    except ImportError:
        print("SALib not detected. Install via 'pip install SALib' for publication-grade Sobol analysis.")
        run_oat_analysis(outputs_dir)
        
    print("\nSensitivity analysis runs completed successfully!")
