import os
import matplotlib.pyplot as plt
import numpy as np
from tesm_simulation import generate_scenario_matrix, DEFAULT_PARAMS

def plot_scenario_matrix():
    print("Running 32 Scenario Matrix combinations...")
    matrix = generate_scenario_matrix(DEFAULT_PARAMS)
    
    # Sort scenarios by final index value
    outcomes = []
    for name, sim in matrix.items():
        final_idx = sim['indexVal'][-1]
        final_roic = sim['roic'][-1]
        
        # Classification logic (same as JS frontend)
        overall_cagr = (final_idx / 100.0) ** (1/20) - 1
        
        if final_idx < 50:
            status = "Severe Crash"
            color = "#ff3366"  # Red
        elif final_idx < 100:
            status = "Deflationary"
            color = "#ffb300"  # Yellow
        elif overall_cagr < 0.04 or final_roic < DEFAULT_PARAMS['wacc']:
            status = "Stagnant / Flat"
            color = "#a29bfe"  # Purple
        else:
            status = "Stable Growth"
            color = "#00e676"  # Green
            
        outcomes.append({
            "name": name,
            "index": final_idx,
            "status": status,
            "color": color
        })
        
    outcomes = sorted(outcomes, key=lambda x: x['index'])
    
    names = [x['name'] for x in outcomes]
    indices = [x['index'] for x in outcomes]
    colors = [x['color'] for x in outcomes]
    
    # Create horizontal bar chart
    plt.figure(figsize=(12, 10))
    bars = plt.barh(names, indices, color=colors, height=0.6)
    
    # Add values on the bars
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 2, bar.get_y() + bar.get_height()/2, f"{width:.1f}", 
                 va='center', ha='left', color='white', fontweight='bold', fontsize=9)
                 
    plt.title("TESM Scenario Matrix Outturns (Sorted by Q80 Index Value)", fontsize=14, fontweight="bold", color="white")
    plt.xlabel("Q80 Tech Index Value (Base = 100)", fontsize=12, color="white")
    plt.ylabel("Scenario Parameters Combinations", fontsize=12, color="white")
    
    # Dark mode styling
    ax = plt.gca()
    ax.set_facecolor("#121212")
    ax.spines['bottom'].set_color('#555555')
    ax.spines['top'].set_color('#555555')
    ax.spines['right'].set_color('#555555')
    ax.spines['left'].set_color('#555555')
    ax.tick_params(colors='#cccccc', labelsize=9)
    ax.yaxis.label.set_color('#cccccc')
    ax.xaxis.label.set_color('#cccccc')
    
    # Custom legend for classifications
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#ff3366', label='Severe Crash (<50)'),
        Patch(facecolor='#ffb300', label='Deflationary (50-100)'),
        Patch(facecolor='#a29bfe', label='Stagnant / Flat (overall CAGR <4%)'),
        Patch(facecolor='#00e676', label='Stable Growth (overall CAGR >=4%)')
    ]
    plt.legend(handles=legend_elements, facecolor='#1e1e1e', edgecolor='#333333', labelcolor='white')
    
    plt.grid(True, axis='x', color='#2c2c2c', alpha=0.5)
    
    fig = plt.gcf()
    fig.patch.set_facecolor('#1e1e1e')
    
    artifacts_dir = "C:/Users/NITHING/.gemini/antigravity/brain/60e8d70e-69ee-4ab6-a08d-332834a5ddce"
    if not os.path.exists(artifacts_dir):
        os.makedirs(artifacts_dir)
        
    out_path = os.path.join(artifacts_dir, "scenario_matrix_outcomes.png")
    plt.tight_layout()
    plt.savefig(out_path, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    
    print(f"Generated Scenario Matrix plot saved to: {out_path}")

if __name__ == "__main__":
    plot_scenario_matrix()
