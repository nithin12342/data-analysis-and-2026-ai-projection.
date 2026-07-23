@echo off
setlocal enabledelayedexpansion

echo ==============================================================
echo   BULK DATA DOWNLOAD SCRIPT
echo   Date: %date% %time%
echo ==============================================================

set "DATA_DIR=DATA\bulk_downloads"
if not exist "%DATA_DIR%" mkdir "%DATA_DIR%"

echo.
echo [1/7] SEC Company Facts...
set "SEC_URL=https://www.sec.gov/files/companyfacts.zip"
set "SEC_FILE=%DATA_DIR%\companyfacts.zip"
curl.exe -L -H "User-Agent: Kilo-Data-Collector/1.0" -o "%SEC_FILE%" "%SEC_URL%" 2>NUL
if exist "%SEC_FILE%" (
    for %%A in ("%SEC_FILE%") do (
        set "SIZE=%%~zA"
    )
    if !SIZE! gtr 1000000 (
        echo   Downloaded: !SIZE! bytes
    ) else (
        echo   Download incomplete or rate limited
        del "%SEC_FILE%"
    )
)

echo.
echo [2/7] EIA Form 860 (2024)...
set "EIA_URL=https://www.eia.gov/electricity/data/eia860/xls/eia860_2024.xlsx"
set "EIA_FILE=%DATA_DIR%\eia860_2024.xlsx"
curl.exe -L -H "User-Agent: Kilo-Data-Collector/1.0" -o "%EIA_FILE%" "%EIA_URL%" 2>NUL
if exist "%EIA_FILE%" (
    for %%A in ("%EIA_FILE%") do set "SIZE=%%~zA"
    if !SIZE! gtr 1000000 (
        echo   Downloaded: !SIZE! bytes
    ) else (
        echo   Download incomplete
        del "%EIA_FILE%"
    )
)

echo.
echo [3/7] EIA Form 923 (2024)...
set "EIA923_URL=https://www.eia.gov/electricity/data/eia923/xls/eia923_2024.xlsx"
set "EIA923_FILE=%DATA_DIR%\eia923_2024.xlsx"
curl.exe -L -H "User-Agent: Kilo-Data-Collector/1.0" -o "%EIA923_FILE%" "%EIA923_URL%" 2>NUL
if exist "%EIA923_FILE%" (
    for %%A in ("%EIA923_FILE%") do set "SIZE=%%~zA"
    if !SIZE! gtr 1000000 (
        echo   Downloaded: !SIZE! bytes
    ) else (
        echo   Download incomplete
    )
)

echo.
echo [4/7] FRED Economic Series...
for %%I in (FDXFIPS GDP FEDFUNDS DGS10 DGS30 BAMLH0A0HYM2 T10Y2Y) do (
    set "FRED_URL=https://fred.stlouisfed.org/graph/fredgraph.csv?id=%%I"
    set "FRED_FILE=%DATA_DIR%\fred_%%I.csv"
    curl.exe -L -H "User-Agent: Kilo-Data-Collector/1.0" -o "!FRED_FILE!" "!FRED_URL!" 2>NUL
    if exist "!FRED_FILE!" (
        for %%A in ("!FRED_FILE!") do set "SIZE=%%~zA"
        if !SIZE! gtr 1000 (
            echo   %%I: !SIZE! bytes
        ) else (
            del "!FRED_FILE!"
        )
    )
)

echo.
echo [5/7] LBNL Grid Interconnection...
set "LBNL_URL=https://emp.lbl.gov/sites/default/files/LBNL_Ix_Queue_Data_File_thru2025.xlsx"
set "LBNL_FILE=%DATA_DIR%\LBNL_Ix_Queue_Data_File_thru2025.xlsx"
curl.exe -L -H "User-Agent: Kilo-Data-Collector/1.0" -o "%LBNL_FILE%" "%LBNL_URL%" 2>NUL
if exist "%LBNL_FILE%" (
    for %%A in ("%LBNL_FILE%") do set "SIZE=%%~zA"
    if !SIZE! gtr 1000000 (
        echo   Downloaded: !SIZE! bytes
    ) else (
        echo   Download incomplete
    )
)

echo.
echo [6/7] SEC Company Tickers...
set "TICKER_URL=https://www.sec.gov/files/company_tickers.json"
set "TICKER_FILE=%DATA_DIR%\company_tickers.json"
curl.exe -L -H "User-Agent: Kilo-Data-Collector/1.0" -o "%TICKER_FILE%" "%TICKER_URL%" 2>NUL
if exist "%TICKER_FILE%" (
    for %%A in ("%TICKER_FILE%") do set "SIZE=%%~zA"
    echo   Downloaded: !SIZE! bytes
)

echo.
echo [7/7] OpenRouter Models...
set "OR_URL=https://openrouter.ai/api/v1/models"
set "OR_FILE=%DATA_DIR%\openrouter_models.json"
curl.exe -L -H "User-Agent: Kilo-Data-Collector/1.0" -o "%OR_FILE%" "%OR_URL%" 2>NUL
if exist "%OR_FILE%" (
    for %%A in ("%OR_FILE%") do set "SIZE=%%~zA"
    echo   Downloaded: !SIZE! bytes
)

echo.
echo ==============================================================
echo   DOWNLOAD SUMMARY
echo ==============================================================
dir /b /a:-d "%DATA_DIR%" 2>NUL
echo ==============================================================

endlocal