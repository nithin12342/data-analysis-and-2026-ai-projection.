$ErrorActionPreference = "Continue"
$DataDir = "DATA\bulk_downloads"

Write-Host "=============================================================="
Write-Host "  BULK DATA DOWNLOAD SCRIPT"
Write-Host "  Date: $(Get-Date)"
Write-Host "=============================================================="

# 1. SEC Company Facts (may be rate limited)
Write-Host "`n[1/7] SEC Company Facts..."
$secUrl = "https://www.sec.gov/files/companyfacts.zip"
$secPath = Join-Path $DataDir "companyfacts.zip"
try {
    $headers = @{
        'User-Agent' = 'Kilo-Data-Collector/1.0 (contact@example.com)'
        'Accept-Encoding' = 'gzip, deflate'
        'Connection' = 'keep-alive'
    }
    Invoke-WebRequest -Uri $secUrl -OutFile $secPath -Headers $headers -TimeoutSec 600
    $size = (Get-Item $secPath).Length
    if ($size -gt 1000000) {
        Write-Host "  Downloaded: $([math]::Round($size/1GB, 2)) GB"
    } else {
        Write-Host "  Download incomplete or rate limited"
        Remove-Item $secPath -ErrorAction SilentlyContinue
    }
} catch {
    Write-Host "  Error: $($_.Exception.Message)"
}

# 2. EIA Form 860
Write-Host "`n[2/7] EIA Form 860 (2024)..."
$eiaUrl = "https://www.eia.gov/electricity/data/eia860/xls/eia860_2024.xlsx"
$eiaPath = Join-Path $DataDir "eia860_2024.xlsx"
try {
    $headers = @{ 'User-Agent' = 'Kilo-Data-Collector/1.0' }
    Invoke-WebRequest -Uri $eiaUrl -OutFile $eiaPath -Headers $headers -TimeoutSec 120
    $size = (Get-Item $eiaPath).Length
    if ($size -gt 1000000) {
        Write-Host "  Downloaded: $([math]::Round($size/1MB, 1)) MB"
    } else {
        Write-Host "  Download incomplete"
        Remove-Item $eiaPath -ErrorAction SilentlyContinue
    }
} catch {
    Write-Host "  Error: $($_.Exception.Message)"
}

# 3. EIA Form 923
Write-Host "`n[3/7] EIA Form 923 (2024)..."
$eia923Url = "https://www.eia.gov/electricity/data/eia923/xls/eia923_2024.xlsx"
$eia923Path = Join-Path $DataDir "eia923_2024.xlsx"
try {
    $headers = @{ 'User-Agent' = 'Kilo-Data-Collector/1.0' }
    Invoke-WebRequest -Uri $eia923Url -OutFile $eia923Path -Headers $headers -TimeoutSec 120
    $size = (Get-Item $eia923Path).Length
    if ($size -gt 1000000) {
        Write-Host "  Downloaded: $([math]::Round($size/1MB, 1)) MB"
    } else {
        Write-Host "  Download incomplete"
    }
} catch {
    Write-Host "  Error: $($_.Exception.Message)"
}

# 4. FRED Core Series
Write-Host "`n[4/7] FRED Economic Series..."
$fredIds = @("FDXFIPS","GDP","FEDFUNDS","DGS10","DGS30","BAMLH0A0HYM2","T10Y2Y")
foreach ($id in $fredIds) {
    $fredUrl = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=$id"
    $fredPath = Join-Path $DataDir "fred_$id.csv"
    try {
        $headers = @{ 'User-Agent' = 'Kilo-Data-Collector/1.0' }
        Invoke-WebRequest -Uri $fredUrl -OutFile $fredPath -Headers $headers -TimeoutSec 30
        $size = (Get-Item $fredPath).Length
        if ($size -gt 1000) {
            Write-Host ("  {0}: {1} KB" -f $id, [math]::Round($size/1KB, 1))
        } else {
            Remove-Item $fredPath -ErrorAction SilentlyContinue
        }
    } catch {
        Write-Host ("  {0}: Error" -f $id)
    }
}

# 5. LBNL Interconnection Data
Write-Host "`n[5/7] LBNL Grid Interconnection..."
$lbnlUrl = "https://emp.lbl.gov/sites/default/files/LBNL_Ix_Queue_Data_File_thru2025.xlsx"
$lbnlPath = Join-Path $DataDir "LBNL_Ix_Queue_Data_File_thru2025.xlsx"
try {
    $headers = @{ 'User-Agent' = 'Kilo-Data-Collector/1.0' }
    Invoke-WebRequest -Uri $lbnlUrl -OutFile $lbnlPath -Headers $headers -TimeoutSec 120
    $size = (Get-Item $lbnlPath).Length
    if ($size -gt 1000000) {
        Write-Host "  Downloaded: $([math]::Round($size/1MB, 1)) MB"
    } else {
        Write-Host "  Download incomplete"
    }
} catch {
    Write-Host "  Error: $($_.Exception.Message)"
}

# 6. Company Tickers JSON
Write-Host "`n[6/7] SEC Company Tickers..."
$tickerUrl = "https://www.sec.gov/files/company_tickers.json"
$tickerPath = Join-Path $DataDir "company_tickers.json"
try {
    $headers = @{ 'User-Agent' = 'Kilo-Data-Collector/1.0' }
    Invoke-WebRequest -Uri $tickerUrl -OutFile $tickerPath -Headers $headers -TimeoutSec 30
    $size = (Get-Item $tickerPath).Length
    Write-Host "  Downloaded: $([math]::Round($size/1KB, 1)) KB"
} catch {
    Write-Host "  Error: $($_.Exception.Message)"
}

# 7. OpenRouter Models API
Write-Host "`n[7/7] OpenRouter Models..."
$orUrl = "https://openrouter.ai/api/v1/models"
$orPath = Join-Path $DataDir "openrouter_models.json"
try {
    $headers = @{ 'User-Agent' = 'Kilo-Data-Collector/1.0' }
    $resp = Invoke-WebRequest -Uri $orUrl -Headers $headers -TimeoutSec 30
    $resp.Content | Out-File $orPath -Encoding utf8
    $size = (Get-Item $orPath).Length
    Write-Host "  Downloaded: $([math]::Round($size/1KB, 1)) KB"
} catch {
    Write-Host "  Error: $($_.Exception.Message)"
}

Write-Host "`n=============================================================="
Write-Host "  DOWNLOAD SUMMARY"
Write-Host "=============================================================="
Get-ChildItem -Path $DataDir -File | Sort-Object Name | ForEach-Object {
    $size = $_.Length
    if ($size -gt 1048576) { 
        Write-Host ("  {0}: {1} MB" -f $_.Name, [math]::Round($size/1MB, 2))
    } else { 
        Write-Host ("  {0}: {1} KB" -f $_.Name, [math]::Round($size/1KB, 1))
    }
}
Write-Host "=============================================================="