# Implementation Plan - Google Colab Data Ingestion

This updated plan details the strategy to run the data acquisition pipeline inside a **Google Colab (Free Tier with GPU)** environment. 

Executing in Colab resolves local firewall/proxy timeouts (like the ones encountered with FRED and iShares) and utilizes Colab's high-speed cloud backbone.

---

## User Review Required

> [!IMPORTANT]
> **Colab Setup & Execution Flow**
> The pipeline will be packaged as a single self-contained Python script `colab_pipeline.py`.
> The user will:
> 1. Open a new Google Colab notebook (free GPU tier).
> 2. Upload `colab_pipeline.py` to the Colab environment.
> 3. Run a single cell to install requirements and execute the pipeline.
> 4. Download the resulting `master_consolidated.duckdb` and logs.

---

## Open Questions

> [!NOTE]
> 1. **Google Drive Integration**: Should the script automatically mount Google Drive and save the DuckDB database directly to the user's Drive folder (e.g., `/content/drive/MyDrive/projections/`)? This is highly recommended for persistence.

---

## Colab Notebook Setup

To execute the pipeline, the user will create a Colab notebook with two cells:

### Cell 1: Environment Setup
```python
# Install required libraries
!pip install duckdb pandas requests beautifulsoup4 python-dotenv
```

### Cell 2: Run Pipeline
```python
# Run the pipeline script
!python colab_pipeline.py --mount-drive
```

---

## Proposed Changes

### [Acquisition Engine]

#### [NEW] [colab_pipeline.py](file:///c:/Users/NITHING/Desktop/projections/scripts/acquisition/colab_pipeline.py)
A self-contained Python script combining all cluster scripts (A, B, D, E) to run seamlessly on Google Colab. If `--mount-drive` is specified, it will save the DuckDB database to Google Drive for persistent storage.

---

## Verification Plan

### Manual Verification
1. Run the `colab_pipeline.py` script locally to verify syntax.
2. Provide the step-by-step notebook execution instructions.
3. Validate output row counts and check for complete data ingestion.
