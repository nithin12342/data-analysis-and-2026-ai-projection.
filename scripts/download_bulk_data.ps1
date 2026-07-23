$ErrorActionPreference = "Stop"
$DATA_DIR = "DATA"

if (-not (Test-Path $DATA_DIR)) {
    New-Item -ItemType Directory -Path $DATA_DIR | Out-Null
}

Write-Host "=" * 70
Write-Host "  BULK DATA DOWNLOAD SCRIPT FOR 54 TABLES"
Write-Host "=" * 70

# 1. SEC EDGAR Company Facts Bulk Dataset
Write-Host "`n[1/5] SEC EDGAR Company Facts..."
$sec_url = "https://www.sec.gov/files/companyfacts.zip"
$sec_path = Join-Path $DATA_DIR "companyfacts.zip"
if (-not (Test-Path $sec_path)) {
    try {
        curl.exe -L --max-time 600 `
            -H "User-Agent: Kilo-Data-Collector/1.0 (contact@example.com)" `
            -H "Accept: application/zip" `
            -o $sec_path $sec_url
        $fileSize = (Get-Item $sec_path).Length
        if ($fileSize -gt 100000000) {
            Write-Host "  Downloaded $(Split-Path $sec_path -Leaf) ($([math]::Round($fileSize/1GB, 1)) GB)"
        } else {
            Write-Host "  Download incomplete or redirected. Manual download needed:"
            Write-Host "  https://www.sec.gov/files/companyfacts.zip"
            Remove-Item $sec_path -ErrorAction SilentlyContinue
        }
    } catch {
        Write-Host "  Error downloading SEC data: $_"
        Write-Host "  Manual download: https://www.sec.gov/files/companyfacts.zip"
    }
} else {
    $fileSize = (Get-Item $sec_path).Length
    Write-Host "  Already exists ($(Split-Path $sec_path -Leaf)): $([math]::Round($fileSize/1MB, 1)) MB"
}

# 2. EIA Form 860 - Annual Data
Write-Host "`n[2/5] EIA Form 860 (Power Plant Generator Data)..."
$eia_url = "https://www.eia.gov/electricity/data/eia860/mf/eia860_mf_2024.xlsx"
$eia_path = Join-Path $DATA_DIR "eia_form860_2024.xlsx"
if (-not (Test-Path $eia_path)) {
    try {
        curl.exe -L --max-time 120 `
            -H "User-Agent: Kilo-Data-Collector/1.0 (contact@example.com)" `
            -o $eia_path $eia_url
        $fileSize = (Get-Item $eia_path).Length
        if ($fileSize -gt 1000000) {
            Write-Host "  Downloaded $(Split-Path $eia_path -Leaf) ($([math]::Round($fileSize/1MB, 1)) MB)"
        } else {
            Write-Host "  Download may be incomplete. Manual download:"
            Write-Host "  https://www.eia.gov/electricity/data/eia860/"
            Remove-Item $eia_path -ErrorAction SilentlyContinue
        }
    } catch {
        Write-Host "  Manual download required: https://www.eia.gov/electricity/data/eia860/"
    }
} else {
    $fileSize = (Get-Item $eia_path).Length
    Write-Host "  Already exists: $(Split-Path $eia_path -Leaf) ($([math]::Round($fileSize/1MB, 1)) MB)"
}

# 3. USGS NWIS Water Use Data
Write-Host "`n[3/5] USGS NWIS Water Use Data..."
$usgs_path = Join-Path $DATA_DIR "usgs_nwis_sample.txt"
if (-not (Test-Path $usgs_path)) {
    Write-Host "  Note: USGS bulk requires site-specific queries"
    Write-Host "  Access: https://waterdata.usgs.gov/nwis/wu"
    Write-Host "  Sample query: https://waterdata.usgs.gov/nwis/dvplugis?format=rdb&site_no=08075500"
} else {
    $fileSize = (Get-Item $usgs_path).Length
    Write-Host "  Already exists: $(Split-Path $usgs_path -Leaf)"
}

# 4. LMSYS Chatbot Arena Conversations
Write-Host "`n[4/5] LMSYS Chatbot Arena Conversations..."
Write-Host "  Note: HuggingFace datasets require authentication"
Write-Host "  Download via: datasets-cli download lmsys/chatbot_arena_conversations"
Write-Host "  Manual: https://huggingface.co/datasets/lmsys/chatbot_arena_conversations"

# 5. arXiv Metadata
Write-Host "`n[5/5] arXiv Metadata Snapshot..."
$arxiv_url = "https://arxiv.org/help/bulk_data_s3"
Write-Host "  Access via AWS S3: $arxiv_url"
Write-Host "  Alternative: https://data.cornell.edu/api/1/dataset/download/arxiv-metadata-oai-snapshot.json"

Write-Host "`n" + "=" * 70
Write-Host "  DOWNLOAD SUMMARY"
Write-Host "=" * 70
Write-Host "  Files in DATA folder:"
Get-ChildItem -Path $DATA_DIR -File | ForEach-Object {
    $size_mb = [math]::Round($_.Length / 1MB, 1)
    Write-Host "    $($_.Name): $size_mb MB"
}
Write-Host "=" * 70
Write-Host "`n  MANUAL DOWNLOADS REQUIRED:"
Write-Host "    1. SEC companyfacts.zip: https://www.sec.gov/files/companyfacts.zip"
Write-Host "    2. EIA Form 860: https://www.eia.gov/electricity/data/eia860/"
Write-Host "    3. arXiv metadata: https://arxiv.org/help/bulk_data_s3"
Write-Host "    4. LMSYS Chatbot Arena: huggingface.co/datasets/lmsys/chatbot_arena_conversations"
Write-Host "=" * 70