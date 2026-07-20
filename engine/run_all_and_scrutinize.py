import os
import subprocess
import shutil
import sys

def main():
    proj_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    scrutinize_dir = os.path.join(proj_root, "scrutinize")
    outputs_dir = os.path.join(proj_root, "outputs")
    engine_dir = os.path.join(proj_root, "engine")
    
    # 1. Create scrutinize directory if it doesn't exist
    if not os.path.exists(scrutinize_dir):
        os.makedirs(scrutinize_dir)
        print(f"Created scrutinize directory: {scrutinize_dir}")
    else:
        print(f"Scrutinize directory already exists: {scrutinize_dir}")
        
    # 2. Run Baseline Simulation
    print("\n--- Running Baseline Systems Dynamics Simulation ---")
    sim_script = os.path.join(engine_dir, "tesm_simulation.py")
    try:
        res = subprocess.run([sys.executable, sim_script], capture_output=True, text=True, check=True)
        log_path = os.path.join(scrutinize_dir, "baseline_simulation_log.txt")
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(res.stdout)
            if res.stderr:
                f.write("\n\n=== STDERR ===\n")
                f.write(res.stderr)
        print(f"  Baseline simulation complete. Log saved to scrutinize/baseline_simulation_log.txt")
    except subprocess.CalledProcessError as e:
        print(f"  Error running baseline simulation: {e}")
        print(e.stdout)
        print(e.stderr)
        
    # 3. Run Historical Validation Sweep
    print("\n--- Running Historical Validation (7 Crises) Sweep ---")
    val_script = os.path.join(engine_dir, "multiprocess_validation.py")
    try:
        res = subprocess.run([sys.executable, val_script], capture_output=True, text=True, check=True)
        log_path = os.path.join(scrutinize_dir, "validation_summary.txt")
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(res.stdout)
            if res.stderr:
                f.write("\n\n=== STDERR ===\n")
                f.write(res.stderr)
        print(f"  Validation sweep complete. Summary saved to scrutinize/validation_summary.txt")
    except subprocess.CalledProcessError as e:
        print(f"  Error running validation sweep: {e}")
        print(e.stdout)
        print(e.stderr)
        
    # 4. Run Sensitivity Analysis (Sobol & OAT Sweeps)
    print("\n--- Running Global Parameter Sensitivity Analysis ---")
    sens_script = os.path.join(engine_dir, "sensitivity_analysis.py")
    try:
        res = subprocess.run([sys.executable, sens_script], capture_output=True, text=True, check=True)
        log_path = os.path.join(scrutinize_dir, "sensitivity_analysis_log.txt")
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(res.stdout)
            if res.stderr:
                f.write("\n\n=== STDERR ===\n")
                f.write(res.stderr)
        print(f"  Sensitivity analysis complete. Log saved to scrutinize/sensitivity_analysis_log.txt")
    except subprocess.CalledProcessError as e:
        print(f"  Error running sensitivity analysis: {e}")
        print(e.stdout)
        print(e.stderr)
        
    # 5. Copy all files from outputs/ to scrutinize/
    print("\n--- Copying generated charts and reports to scrutinize/ ---")
    if os.path.exists(outputs_dir):
        files = os.listdir(outputs_dir)
        copied_count = 0
        for filename in files:
            src = os.path.join(outputs_dir, filename)
            dst = os.path.join(scrutinize_dir, filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)
                copied_count += 1
        print(f"  Copied {copied_count} files from outputs/ to scrutinize/")
    else:
        print("  Warning: outputs directory not found.")
        
    # 6. Copy legacy path tesm_trajectories.png if generated
    legacy_dir = "C:/Users/NITHING/.gemini/antigravity/brain/60e8d70e-69ee-4ab6-a08d-332834a5ddce"
    legacy_img = os.path.join(legacy_dir, "tesm_trajectories.png")
    if os.path.exists(legacy_img):
        dst_img = os.path.join(scrutinize_dir, "tesm_trajectories.png")
        shutil.copy2(legacy_img, dst_img)
        print(f"  Copied tesm_trajectories.png to scrutinize/")
        
    print("\nExecution and scrutiny organization completed successfully!")

if __name__ == "__main__":
    main()
