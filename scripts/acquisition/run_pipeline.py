#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

# Add current folder to sys.path to allow absolute imports
sys.path.append(str(Path(__file__).resolve().parent))

from utils import logger, get_db_connection
import cluster_a_bulk
import cluster_b_api
import cluster_d_scrape
import cluster_e_agent

def main():
    parser = argparse.ArgumentParser(description="Automated Data Ingestion & Acquisition Pipeline")
    parser.add_argument(
        "--cluster", 
        type=str, 
        choices=["A", "B", "D", "E", "all"], 
        default="all",
        help="Specify which cluster of the acquisition matrix to execute."
    )
    
    args = parser.parse_args()
    cluster = args.cluster.upper()
    
    logger.info("=" * 60)
    logger.info(f"STARTING DATA ACQUISITION PIPELINE FOR CLUSTER: {cluster}")
    logger.info("=" * 60)
    
    success = True
    
    if cluster in ["A", "ALL"]:
        logger.info("\n--- EXECUTING CLUSTER A: BULK DOWNLOADS & DERIVED TABLES ---")
        try:
            r1 = cluster_a_bulk.acquire_company_security_master()
            r2 = cluster_a_bulk.acquire_equity_prices_daily()
            r3 = cluster_a_bulk.acquire_macro_timeseries_fred()
            if not (r1 and r2 and r3):
                success = False
                logger.warning("Some Cluster A acquisitions failed.")
        except Exception as e:
            logger.error(f"Cluster A execution failed: {e}")
            success = False

    if cluster in ["B", "ALL"]:
        logger.info("\n--- EXECUTING CLUSTER B: PUBLIC APIS ---")
        try:
            r1 = cluster_b_api.acquire_shares_outstanding_quarterly()
            r2 = cluster_b_api.acquire_huggingface_models()
            r3 = cluster_b_api.acquire_github_model_activity()
            if not (r1 and r2 and r3):
                success = False
                logger.warning("Some Cluster B acquisitions failed.")
        except Exception as e:
            logger.error(f"Cluster B execution failed: {e}")
            success = False

    if cluster in ["D", "ALL"]:
        logger.info("\n--- EXECUTING CLUSTER D: WEB SCRAPING ---")
        try:
            r1 = cluster_d_scrape.scrape_sector_etf_holdings()
            r2 = cluster_d_scrape.scrape_epoch_ai_training_runs()
            if not (r1 and r2):
                success = False
                logger.warning("Some Cluster D acquisitions failed.")
        except Exception as e:
            logger.error(f"Cluster D execution failed: {e}")
            success = False

    if cluster in ["E", "ALL"]:
        logger.info("\n--- EXECUTING CLUSTER E: AGENTIC EXTRACTION ---")
        try:
            r1 = cluster_e_agent.run_agentic_research()
            if not r1:
                success = False
                logger.warning("Cluster E acquisition failed.")
        except Exception as e:
            logger.error(f"Cluster E execution failed: {e}")
            success = False
            
    if success:
        logger.info("\n✅ DATA ACQUISITION PIPELINE COMPLETED SUCCESSFULLY.")
    else:
        logger.error("\n❌ DATA ACQUISITION PIPELINE COMPLETED WITH ERRORS.")
        sys.exit(1)

if __name__ == "__main__":
    main()
