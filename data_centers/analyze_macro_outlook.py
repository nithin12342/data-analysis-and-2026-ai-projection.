from tesm_simulation import run_simulation
import numpy as np

# Run baseline scenario
h_base = run_simulation()

# Run stress scenario (High WACC, low elasticity, high grid delay, high compression)
h_stress = run_simulation({
    'wacc': 0.12,
    'elasticityCoefficient': 0.85,          # Low demand elasticity (does not trigger Jevons Paradox)
    'gridConnectionDelay': 12,              # Long utility queues
    'priceCompression': 0.90,               # Rapid commoditization of API tokens
    'capitalReflexivity': 0.70              # High capital market feedback
})

def analyze_trajectory(history, name):
    index = np.array(history['indexVal'])
    quarters = np.array(history['quarters'])
    roic = np.array(history['roic'])
    stranded = np.array(history['strandedCapacity'])
    
    peak_idx = np.argmax(index)
    peak_val = index[peak_idx]
    peak_q = quarters[peak_idx]
    
    trough_val = np.min(index[peak_idx:])
    trough_idx = peak_idx + np.argmin(index[peak_idx:])
    trough_q = quarters[trough_idx]
    
    drop_pct = (peak_val - trough_val) / peak_val * 100.0 if peak_val > 0 else 0.0
    
    # Check if index stabilizes or keeps dropping
    final_val = index[-1]
    recovery_pct = (final_val - trough_val) / trough_val * 100.0 if trough_val > 0 else 0.0
    
    print(f"Scenario: {name.upper()}")
    print(f"  Peak Index Value:   {peak_val:.1f} (Quarter {peak_q})")
    print(f"  Trough Index Value: {trough_val:.1f} (Quarter {trough_q})")
    print(f"  Peak-to-Trough Drop: {drop_pct:.1f}%")
    print(f"  Final Y20 Index:    {final_val:.1f} (Recovery from Trough: {recovery_pct:.1f}%)")
    print(f"  Peak Stranded:      {max(stranded):.1f} capacity units")
    print(f"  Final ROIC:         {roic[-1]*100.0:.1f}%")
    print("-" * 50)

print("=" * 60)
print("TESM SYSTEM DYNAMICS FORECAST ANALYSIS")
print("=" * 60)
analyze_trajectory(h_base, "Baseline (Onsite Power Enabled)")
analyze_trajectory(h_stress, "Stress Scenario (Hype Burst / Deleveraging)")
