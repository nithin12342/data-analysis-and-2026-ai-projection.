import os
import matplotlib.pyplot as plt
import numpy as np
from tesm_simulation import run_monte_carlo, DEFAULT_PARAMS

def plot_monte_carlo():
    print("Running Monte Carlo simulation (500 trials)...")
    mc = run_monte_carlo(DEFAULT_PARAMS, trials=500)
    
    n = len(mc['indexVal']['p50'])
    quarters = np.arange(n)
    
    # Create dark-mode style plot
    plt.figure(figsize=(10, 6))
    
    p90 = np.array(mc['indexVal']['p90'])
    p50 = np.array(mc['indexVal']['p50'])
    p10 = np.array(mc['indexVal']['p10'])
    
    # Fill between P10 and P90
    plt.fill_between(quarters, p10, p90, color='#4facfe', alpha=0.15, label='10th - 90th Percentile Range')
    
    plt.plot(quarters, p90, color='#00f2fe', alpha=0.4, linestyle='--', linewidth=1.5, label='P90 (Optimistic Expansion)')
    plt.plot(quarters, p50, color='#4facfe', linewidth=3.0, label='P50 (Expected Stagnation Path)')
    plt.plot(quarters, p10, color='#ff3366', linestyle='--', linewidth=1.5, label='P10 (Severe Crash/Downside)')
    
    plt.title("TESM Monte Carlo Range Forecast: 20-Year Horizon", fontsize=14, fontweight="bold", color="white")
    plt.xlabel("Quarters", fontsize=12, color="white")
    plt.ylabel("TESM Tech Index Value (Base = 100)", fontsize=12, color="white")
    
    # Dark mode styling
    ax = plt.gca()
    ax.set_facecolor("#121212")
    ax.spines['bottom'].set_color('#555555')
    ax.spines['top'].set_color('#555555')
    ax.spines['right'].set_color('#555555')
    ax.spines['left'].set_color('#555555')
    ax.tick_params(colors='#cccccc')
    ax.yaxis.label.set_color('#cccccc')
    ax.xaxis.label.set_color('#cccccc')
    
    plt.legend(facecolor='#1e1e1e', edgecolor='#333333', labelcolor='white')
    plt.grid(True, color='#2c2c2c', alpha=0.5)
    
    fig = plt.gcf()
    fig.patch.set_facecolor('#1e1e1e')
    
    artifacts_dir = "C:/Users/NITHING/.gemini/antigravity/brain/60e8d70e-69ee-4ab6-a08d-332834a5ddce"
    if not os.path.exists(artifacts_dir):
        os.makedirs(artifacts_dir)
        
    out_path = os.path.join(artifacts_dir, "monte_carlo_trajectories.png")
    plt.tight_layout()
    plt.savefig(out_path, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    
    print(f"Generated Monte Carlo plot saved to: {out_path}")

if __name__ == "__main__":
    plot_monte_carlo()
