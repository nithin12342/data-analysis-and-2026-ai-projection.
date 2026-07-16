#!/usr/bin/env python3
"""
Python script to consolidate scattered CSV and Excel (spreadsheet) files
into a structured folder 'consolidated_data' categorized by data domain.
"""

import os
import shutil
from pathlib import Path

def get_category(file_path: Path) -> str:
    name = file_path.name.lower()
    path_str = str(file_path).lower()
    
    # 7. Macroeconomic & Financial Market Data
    if 'fred_' in name or '\\macro\\' in path_str or '/macro/' in path_str:
        return '7_macroeconomic_data'
        
    # 6. Chinese AI Ecosystem Data
    if 'china' in name or 'china_' in name:
        return '6_chinese_ai_ecosystem'
        
    # 4. Semiconductor Supply Chain Data
    if 'dataweb' in name or 'semiconductor' in name or 'supply_chain' in name:
        return '4_semiconductor_supply_chain'
        
    # 9. Black Swan & Stress Scenario Parameters
    if 'stress' in name or 'backtest' in name or 'scenario_matrix' in name:
        return '9_stress_scenarios'
        
    # 8. Regulatory & Policy Data
    if 'regulatory' in path_str or 'jurisdiction' in name:
        return '8_regulatory_policy'
        
    # 5. AI Adoption & Productivity Research
    if 'productivity' in name or 'adoption' in name or 'agent' in name or 'deployment_count' in name:
        return '5_ai_adoption_productivity'
        
    # 10. Onsite Power Generation Data
    if '\\power\\' in path_str or '/power/' in path_str or 'onsite_gen' in name or name in ['fuel_prices.csv', 'heat_rates.csv', 'hedge_ratios.csv']:
        return '10_onsite_power_generation'
        
    # 11. Model Calibration & Validation Data
    if name in ['calibration_parameters.csv', 'technology_parameters.csv']:
        return '11_model_calibration'
        
    # 12. Derived/Computed Datasets & Modules
    if name.startswith('module_') or name in ['data_lineage_log.csv', 'gap_uncertainty_register.csv', 'master_capability_matrix.csv']:
        return '12_derived_system_modules'
        
    # 3. Grid & Power Infrastructure Data
    if 'lbnl_' in name or 'grid_connection' in name or 'grid_services' in name or 'wholesale_electricity' in name or 'transformer_shortage' in name or 'regional_infrastructure' in name:
        return '3_grid_power_infrastructure'
        
    # 1. Core Financial & Market Data Sources
    if 'facility_financials' in name or 'enterprise_contracts' in name:
        return '1_financial_market_data'
        
    # 2. Data Center Infrastructure Data
    if 'datacenter' in name or 'facility_list' in name or 'global_datacenters' in name or 'focused_projects' in name or 'key_hyperscale' in name or 'master_global_datacenters' in name:
        return '2_data_center_infrastructure'
        
    # Fallback categorizations
    if 'capacity' in name or 'generation' in name:
        return '10_onsite_power_generation'
    if 'project' in name or 'facility' in name:
        return '2_data_center_infrastructure'
        
    return '13_general_datasets'


def main():
    workspace = Path(r"C:\Users\NITHING\Desktop\projections")
    dest_root = workspace / "consolidated_data"
    
    # Clean and recreate consolidated_data folder
    if dest_root.exists():
        print(f"Cleaning existing directory: {dest_root}")
        shutil.rmtree(dest_root)
    dest_root.mkdir(parents=True, exist_ok=True)
    
    # Keep track of files copied to avoid name collisions
    copied_counts = {}
    
    exclude_dirs = {'.git', '.gemini', '.agents', 'scratch', 'consolidated_data'}
    
    all_files = []
    for root, dirs, files in os.walk(workspace):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for f in files:
            file_path = Path(root) / f
            ext = file_path.suffix.lower()
            if ext in ['.csv', '.xlsx', '.xls']:
                all_files.append(file_path)
                
    print(f"Found {len(all_files)} data files to process.")
    
    for src_path in sorted(all_files):
        category = get_category(src_path)
        dest_dir = dest_root / category
        dest_dir.mkdir(parents=True, exist_ok=True)
        
        # Name preservation logic
        dest_name = src_path.name
        dest_path = dest_dir / dest_name
        
        # Resolve collisions by prefixing with parent folder name
        if dest_path.exists():
            parent_name = src_path.parent.name
            dest_name = f"{parent_name}_{src_path.name}"
            dest_path = dest_dir / dest_name
            
        print(f"Copying: {src_path.relative_to(workspace)} -> {category}/{dest_name}")
        shutil.copy2(src_path, dest_path)
        copied_counts[category] = copied_counts.get(category, 0) + 1
        
    print("\n--- Consolidation Summary ---")
    for cat, count in sorted(copied_counts.items()):
        print(f"  {cat}: {count} files")
        
    print(f"\nAll files successfully consolidated under: {dest_root}")


if __name__ == "__main__":
    main()
