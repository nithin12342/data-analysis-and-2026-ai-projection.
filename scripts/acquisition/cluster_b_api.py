import os
import duckdb
import pandas as pd
from pathlib import Path
from utils import fetch_cached_url, get_db_connection, log_lineage, logger

def acquire_shares_outstanding_quarterly(ciks=["0001045810", "0000789019", "0001018724", "0001652044", "0001326801"]):
    """Acquires outstanding shares from SEC CompanyFacts API."""
    logger.info(f"Starting acquisition of shares_outstanding_quarterly for {len(ciks)} companies...")
    
    con = get_db_connection()
    con.execute("""
        CREATE TABLE IF NOT EXISTS shares_outstanding_quarterly (
            cik VARCHAR,
            period DATE,
            shares DOUBLE,
            tag VARCHAR,
            form VARCHAR,
            fy INTEGER,
            fp VARCHAR,
            PRIMARY KEY (cik, period, tag)
        )
    """)
    
    headers = {
        "User-Agent": "AntigravityDataAcquisition/1.0 (contact@antigravity.ai)"
    }
    
    total_loaded = 0
    
    for cik in ciks:
        padded_cik = cik.zfill(10)
        url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{padded_cik}.json"
        
        try:
            res = fetch_cached_url(url, headers=headers, cache_expiry_hours=24)
            facts = res["content"].get("facts", {})
            us_gaap = facts.get("us-gaap", {})
            dei = facts.get("dei", {})
            
            # Common stock shares outstanding is usually in dei (EntityCommonStockSharesOutstanding)
            # and weighted average shares diluted is in us-gaap (WeightedAverageNumberOfDilutedSharesOutstanding)
            target_tags = [
                ("dei", "EntityCommonStockSharesOutstanding"),
                ("us-gaap", "WeightedAverageNumberOfDilutedSharesOutstanding"),
                ("us-gaap", "WeightedAverageNumberOfSharesOutstandingBasicAndDiluted")
            ]
            
            records = []
            for namespace, tag_name in target_tags:
                source_namespace = us_gaap if namespace == "us-gaap" else dei
                tag_data = source_namespace.get(tag_name, {})
                units = tag_data.get("units", {})
                
                # Shares is normally under units -> "shares"
                shares_list = units.get("shares", [])
                for record in shares_list:
                    # Filter for 10-K and 10-Q forms (annual / quarterly)
                    form = record.get("form")
                    if form in ["10-K", "10-Q"]:
                        records.append({
                            "cik": padded_cik,
                            "period": record.get("end"), # end date of period
                            "shares": float(record.get("val")),
                            "tag": tag_name,
                            "form": form,
                            "fy": record.get("fy"),
                            "fp": record.get("fp")
                        })
            
            if not records:
                logger.warning(f"No shares outstanding data found for CIK {padded_cik}")
                continue
                
            df = pd.DataFrame(records)
            df["period"] = pd.to_datetime(df["period"]).dt.date
            
            # Load into DuckDB
            con.execute("CREATE TEMP TABLE temp_shares AS SELECT * FROM df")
            con.execute("""
                INSERT OR REPLACE INTO shares_outstanding_quarterly (cik, period, shares, tag, form, fy, fp)
                SELECT cik, period, shares, tag, form, fy, fp FROM temp_shares
            """)
            con.execute("DROP TABLE temp_shares")
            
            total_loaded += len(df)
            logger.info(f"Loaded {len(df)} share outstanding records for CIK {padded_cik}")
        except Exception as e:
            logger.error(f"Failed to fetch facts for CIK {padded_cik}: {e}")
            
    con.close()
    log_lineage("shares_outstanding_quarterly", total_loaded, "API", "SEC CompanyFacts", confidence=5)
    return total_loaded > 0

def acquire_huggingface_models(limit=100):
    """Acquires top AI model registry details and downloads from Hugging Face."""
    logger.info("Starting Hugging Face model registry acquisition...")
    url = "https://huggingface.co/api/models"
    params = {
        "sort": "downloads",
        "direction": "-1",
        "limit": limit,
        "full": "true"
    }
    
    try:
        res = fetch_cached_url(url, params=params, cache_expiry_hours=12)
        models = res["content"]
        
        records = []
        for m in models:
            records.append({
                "model_id": m.get("modelId"),
                "author": m.get("author"),
                "downloads": m.get("downloads", 0),
                "likes": m.get("likes", 0),
                "last_modified": m.get("lastModified"),
                "pipeline_tag": m.get("pipeline_tag"),
                "private": m.get("private", False)
            })
            
        df = pd.DataFrame(records)
        
        con = get_db_connection()
        con.execute("""
            CREATE TABLE IF NOT EXISTS open_source_model_registry (
                model_id VARCHAR PRIMARY KEY,
                author VARCHAR,
                downloads INTEGER,
                likes INTEGER,
                last_modified TIMESTAMP,
                pipeline_tag VARCHAR,
                private BOOLEAN
            )
        """)
        
        con.execute("CREATE TEMP TABLE temp_hf AS SELECT * FROM df")
        con.execute("""
            INSERT OR REPLACE INTO open_source_model_registry (model_id, author, downloads, likes, last_modified, pipeline_tag, private)
            SELECT model_id, author, downloads, likes, CAST(last_modified AS TIMESTAMP), pipeline_tag, private FROM temp_hf
        """)
        con.execute("DROP TABLE temp_hf")
        
        # Also store download snapshot history
        con.execute("""
            CREATE TABLE IF NOT EXISTS huggingface_model_downloads (
                model_id VARCHAR,
                date DATE DEFAULT CURRENT_DATE,
                downloads INTEGER,
                PRIMARY KEY (model_id, date)
            )
        """)
        
        con.execute("""
            INSERT OR REPLACE INTO huggingface_model_downloads (model_id, downloads)
            SELECT model_id, downloads FROM df
        """)
        
        row_count = con.execute("SELECT COUNT(*) FROM open_source_model_registry").fetchone()[0]
        con.close()
        
        logger.info(f"Loaded {len(df)} models into Hugging Face tables.")
        log_lineage("open_source_model_registry", len(df), "API", url, confidence=5)
        return True
    except Exception as e:
        logger.error(f"Failed to acquire Hugging Face model registry: {e}")
        return False

def acquire_github_model_activity(repos=["facebookresearch/llama", "vllm-project/vllm", "huggingface/transformers", "langchain-ai/langchain"]):
    """Acquires GitHub repositories activity details."""
    logger.info("Starting GitHub repository stats acquisition...")
    
    con = get_db_connection()
    con.execute("""
        CREATE TABLE IF NOT EXISTS github_model_activity (
            repo VARCHAR,
            date DATE DEFAULT CURRENT_DATE,
            stars INTEGER,
            forks INTEGER,
            open_issues INTEGER,
            commits_last_week INTEGER,
            PRIMARY KEY (repo, date)
        )
    """)
    
    # Optional GitHub Token
    token = os.environ.get("GITHUB_TOKEN")
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"
        
    loaded_count = 0
    for repo in repos:
        url = f"https://api.github.com/repos/{repo}"
        stats_url = f"https://api.github.com/repos/{repo}/stats/commit_activity"
        
        try:
            repo_res = fetch_cached_url(url, headers=headers, cache_expiry_hours=12)
            repo_info = repo_res["content"]
            
            # Commit activity stats
            commit_commits = 0
            try:
                commit_res = fetch_cached_url(stats_url, headers=headers, cache_expiry_hours=12)
                commit_weeks = commit_res["content"]
                if isinstance(commit_weeks, list) and len(commit_weeks) > 0:
                    commit_commits = commit_weeks[-1].get("total", 0)
            except Exception as e:
                logger.warning(f"Failed to get commit activity for {repo}: {e}")
                
            con.execute("""
                INSERT OR REPLACE INTO github_model_activity (repo, stars, forks, open_issues, commits_last_week)
                VALUES (?, ?, ?, ?, ?)
            """, (repo, repo_info.get("stargazers_count", 0), repo_info.get("forks_count", 0), repo_info.get("open_issues_count", 0), commit_commits))
            
            loaded_count += 1
            logger.info(f"Loaded GitHub statistics for {repo}")
        except Exception as e:
            logger.error(f"Failed to get GitHub stats for {repo}: {e}")
            
    con.close()
    log_lineage("github_model_activity", loaded_count, "API", "GitHub API", confidence=5)
    return loaded_count > 0

if __name__ == "__main__":
    acquire_shares_outstanding_quarterly()
    acquire_huggingface_models()
    acquire_github_model_activity()
