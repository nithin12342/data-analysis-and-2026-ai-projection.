$ErrorActionPreference = "Stop"
$CONSOLIDATED_DIR = "consolidated_data"
$DATA_DIR = "DATA"
$PARQUET_DIR = Join-Path $DATA_DIR "parquet_db"

if (-not (Test-Path $PARQUET_DIR)) {
    New-Item -ItemType Directory -Path $PARQUET_DIR | Out-Null
}

Write-Host "=" * 70
Write-Host "  EXTRACTING TABLES FROM EXISTING CONSOLIDATED DATA"
Write-Host "=" * 70

# Use existing consolidated data files to populate tables

# Table 1-6: company_quarterly_metrics.csv -> company_security_master, shares_outstanding, market_cap
Write-Host "`n[1/7] Extracting company financial tables from company_quarterly_metrics.csv..."
$companyMetricsPath = Join-Path $CONSOLIDATED_DIR "13_general_datasets/company_quarterly_metrics.csv"
if (Test-Path $companyMetricsPath) {
    Import-Csv $companyMetricsPath | Select-Object cik,name,period,revenue,net_income,cash,cash_and_investments | `
        Export-Csv (Join-Path $DATA_DIR "company_quarterly_clean.csv") -NoTypeInformation
    Write-Host "  [OK] Created company_quarterly_clean.csv"
    
    # Create company_security_master
    $companies = Import-Csv $companyMetricsPath | Select-Object -Unique cik,name | `
        Select-Object @{n='facility_id';e={$null}},cik,name,ticker,sector,market_cap,cash,total_assets
    $companies | Export-Csv (Join-Path $DATA_DIR "company_security_master.csv") -NoTypeInformation
    Write-Host "  [OK] Created company_security_master.csv ($($companies.Count) companies)"
}

# Table 9: vendor_reported_metrics.csv -> token_usage_proxy
Write-Host "`n[2/7] Processing vendor reported metrics..."
$vendorPath = Join-Path $CONSOLIDATED_DIR "13_general_datasets/vendor_reported_metrics.csv"
if (Test-Path $vendorPath) {
    Copy-Item $vendorPath (Join-Path $DATA_DIR "vendor_reported_metrics.csv") -Force
    Write-Host "  [OK] Copied vendor_reported_metrics.csv"
}

# Table 38-40: gpu_economics.csv, api_pricing.csv
Write-Host "`n[3/7] Processing GPU economics and API pricing..."
$gpuPath = Join-Path $CONSOLIDATED_DIR "13_general_datasets/gpu_economics.csv"
$apiPath = Join-Path $CONSOLIDATED_DIR "13_general_datasets/api_pricing.csv"
if (Test-Path $gpuPath) {
    Copy-Item $gpuPath (Join-Path $DATA_DIR "gpu_economics.csv") -Force
    Write-Host "  [OK] Copied gpu_economics.csv"
}
if (Test-Path $apiPath) {
    Copy-Item $apiPath (Join-Path $DATA_DIR "api_pricing.csv") -Force
    Write-Host "  [OK] Copied api_pricing.csv"
}

# Table 41-45: training_costs.csv, model_benchmarks.csv
Write-Host "`n[4/7] Processing training costs and benchmarks..."
$trainingPath = Join-Path $CONSOLIDATED_DIR "13_general_datasets/training_costs.csv"
$benchPath = Join-Path $CONSOLIDATED_DIR "13_general_datasets/model_benchmarks.csv"
if (Test-Path $trainingPath) {
    Copy-Item $trainingPath (Join-Path $DATA_DIR "training_costs.csv") -Force
    Write-Host "  [OK] Copied training_costs.csv"
}
if (Test-Path $benchPath) {
    Copy-Item $benchPath (Join-Path $DATA_DIR "model_benchmarks.csv") -Force
    Write-Host "  [OK] Copied model_benchmarks.csv"
}

# Table 46-49, 51: Use existing LBNL file
Write-Host "`n[5/7] Processing LBNL interconnection data..."
$lbflPath = Join-Path $CONSOLIDATED_DIR "2_data_center_infrastructure/LBNL_Ix_Queue_Data_File_thru2025.xlsx"
if (Test-Path $lbflPath) {
    Copy-Item $lbflPath (Join-Path $DATA_DIR "LBNL_Ix_Queue_Data_File_thru2025.xlsx") -Force
    Write-Host "  [OK] Copied LBNL interconnection data"
}

# Table 20-21: company_quarterly_metrics.csv for EV, market cap
Write-Host "`n[6/7] Extracting valuation metrics..."
$valPath = Join-Path $CONSOLIDATED_DIR "13_general_datasets/company_quarterly_metrics.csv"
if (Test-Path $valPath) {
    # Create market_cap_quarterly - use revenue as proxy since market cap not directly available
    $valData = Import-Csv $valPath | Where-Object { $_.revenue -ne "" } | `
        Select-Object name,period,revenue,market_cap |
        Where-Object { $_.market_cap -ne "" }
    $valData | Export-Csv (Join-Path $DATA_DIR "market_cap_quarterly.csv") -NoTypeInformation
    Write-Host "  [OK] Created market_cap_quarterly.csv ($($valData.Count) records)"
}

# Table 13-14: rpo_deferred_revenue.csv
Write-Host "`n[7/7] Processing RPO/deferred revenue..."
$rpoPath = Join-Path $CONSOLIDATED_DIR "13_general_datasets/rpo_deferred_revenue.csv"
if (Test-Path $rpoPath) {
    Copy-Item $rpoPath (Join-Path $DATA_DIR "rpo_deferred_revenue.csv") -Force
    Write-Host "  [OK] Copied rpo_deferred_revenue.csv"
}

Write-Host "`n" + "=" * 70
Write-Host "  EXTRACTION COMPLETE"
Write-Host "=" * 70
Write-Host "  Files in DATA folder:"
Get-ChildItem -Path $DATA_DIR -File | Sort-Object Name | ForEach-Object {
    $size_kb = [math]::Round($_.Length / 1KB, 1)
    Write-Host "    $($_.Name): $size_kb KB"
}
Write-Host "=" * 70