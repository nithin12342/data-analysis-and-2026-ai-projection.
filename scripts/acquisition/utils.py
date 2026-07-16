import os
import time
import logging
import json
import hashlib
import requests
import duckdb
from pathlib import Path

# Paths
WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
DB_PATH = WORKSPACE_ROOT / "databases" / "master_consolidated.duckdb"
CACHE_DIR = WORKSPACE_ROOT / "DATA" / "cache"
LOG_DIR = WORKSPACE_ROOT / "logs"

# Ensure directories exist
CACHE_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "acquisition.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("acquisition")

def get_db_connection():
    """Returns a connection to the master DuckDB database."""
    return duckdb.connect(str(DB_PATH))

def get_cache_filename(url, params=None):
    """Generates a stable cache filename based on URL and query params."""
    key = f"{url}_{json.dumps(params, sort_keys=True)}"
    h = hashlib.md5(key.encode("utf-8")).hexdigest()
    return CACHE_DIR / f"{h}.json"

def fetch_cached_url(url, params=None, headers=None, cache_expiry_hours=24, use_cache=True):
    """
    Fetches URL content, caching it locally to prevent duplicate requests.
    Enforces a rate limit of 1 second between live calls.
    """
    cache_file = get_cache_filename(url, params)
    
    if use_cache and cache_file.exists():
        # Check expiry
        mtime = cache_file.stat().st_mtime
        age_hours = (time.time() - mtime) / 3600
        if age_hours < cache_expiry_hours:
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    logger.debug(f"Cache hit: {url}")
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Error reading cache file {cache_file}: {e}")

    # Enforce politeness rate limit before calling
    time.sleep(1.0)
    
    default_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    if headers:
        default_headers.update(headers)
        
    logger.info(f"Fetching: {url}")
    try:
        response = requests.get(url, params=params, headers=default_headers, timeout=30)
        response.raise_for_status()
        
        # Try to parse as JSON first, otherwise store as text
        try:
            data = {"type": "json", "content": response.json()}
        except ValueError:
            data = {"type": "text", "content": response.text}
            
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        return data
    except Exception as e:
        logger.error(f"Error fetching {url}: {e}")
        # Try loading expired cache if request failed
        if cache_file.exists():
            logger.warning(f"Returning expired cache for {url} due to request failure.")
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        raise e

def log_lineage(table_name, row_count, source_type, primary_source, confidence=5):
    """Logs data lineage record into the database."""
    con = get_db_connection()
    try:
        con.execute("""
            CREATE TABLE IF NOT EXISTS data_acquisition_log (
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                table_name VARCHAR,
                row_count INTEGER,
                source_type VARCHAR,
                primary_source VARCHAR,
                confidence INTEGER
            )
        """)
        con.execute("""
            INSERT INTO data_acquisition_log (table_name, row_count, source_type, primary_source, confidence)
            VALUES (?, ?, ?, ?, ?)
        """, (table_name, row_count, source_type, primary_source, confidence))
    except Exception as e:
        logger.error(f"Failed to log lineage for {table_name}: {e}")
    finally:
        con.close()
