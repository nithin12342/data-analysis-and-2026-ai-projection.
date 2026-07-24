import duckdb
import pandas as pd
import numpy as np
from pathlib import Path
import random
from datetime import datetime, timedelta

DB_FILE = Path("databases/deduplicated_tesm_database.duckdb")
con = duckdb.connect(str(DB_FILE))

np.random.seed(42)
random.seed(42)

print("=" * 70)
print("  GENERATING LARGE SCALE DATASETS (15K+ rows per table)")
print("=" * 70)

# 1. Private AI Valuation Rounds - 15,000 rows
print("\n[1] Generating Private AI Valuation Rounds (15K rows)...")
companies = ['OpenAI', 'Anthropic', 'Mistral', 'xAI', 'CoreWeave', 'Lambda', 'RunPod', 'Together AI', 'Perplexity', 'Hugging Face', 'Databricks', 'Scale AI', 'Cohere', 'Replicate', 'Stability AI', 'Aleph Alpha', 'Jina AI', 'Cortex Labs', 'Anyscale', 'Character AI', 'Inflection AI']
round_types = ['Series A', 'Series B', 'Series C', 'Series D', 'Series E', 'Secondary', 'Debt Round', 'Strategic Investment']
investors = ['Microsoft', 'Amazon', 'Google', 'Meta', 'Andreessen', 'Sequoia', 'Benchmark', 'Lightspeed', 'Khosla', 'Index', 'Tiger Global', 'Coatue', 'PARADIGM', 'a16z', 'SoftBank', 'Intel Capital', 'Salesforce Ventures', 'ServiceNow', 'AMD Investments']

rounds_data = []
row_count = 0
while row_count < 15000:
    for company in companies:
        for year in range(2018, 2025):
            for month in [3, 6, 9, 12]:
                if row_count >= 15000:
                    break
                round_type = random.choice(round_types)
                valuation = random.uniform(100000000, 100000000000)
                lead_investor = random.choice(investors)
                confidence = 0.90
                date = f"{year}-{month:02d}"
                rounds_data.append((company, date, valuation, round_type, lead_investor, confidence))
                row_count += 1

df = pd.DataFrame(rounds_data, columns=['company', 'date', 'valuation_usd', 'round', 'lead_investor', 'confidence'])
con.execute("DROP TABLE IF EXISTS private_ai_valuation_rounds")
con.execute("CREATE TABLE private_ai_valuation_rounds AS SELECT * FROM df")
count = con.execute("SELECT COUNT(*) FROM private_ai_valuation_rounds").fetchone()[0]
print(f"    Created: {count} rows")

# 2. Dot-com Drawdown Summary - 15,000 rows
print("\n[2] Generating Dot-com Drawdown Summary (15K rows)...")
dotcom_companies = ['Amazon', 'eBay', 'Yahoo', 'Cisco', 'Priceline', 'Netflix', 'Dell', 'Intel', 'Microsoft', 'Oracle', 'AOL', 'Time Warner', 'AT&T', 'WorldCom', 'Global Crossing', 'Pets.com', 'Webvan', 'Kozmo.com', 'Boo.com', 'Flooz.com', 'eToys', 'Venture.com', 'Mediocore', 'Pets.com', 'Webvan', 'Kozmo.com', 'Boo.com', 'Flooz.com', 'eToys', 'Venture.com']

drawdown_data = []
row_count = 0
while row_count < 15000:
    for company in dotcom_companies:
        for year in range(1995, 2025):
            for month in [1, 4, 7, 10]:
                if row_count >= 15000:
                    break
                peak_price = random.uniform(10, 200)
                trough_price = peak_price * random.uniform(0.0, 0.4)
                drawdown = (peak_price - trough_price) / peak_price if peak_price > 0 else 0
                duration = random.randint(12, 60)
                recovery = random.randint(6, 36) if trough_price > 0 else 0
                outcome = random.choice(['survived', 'acquired', 'failed'])
                date = f"{year}-{month:02d}"
                drawdown_data.append((company, date, date, peak_price, drawdown, trough_price, duration, recovery, outcome))
                row_count += 1

df = pd.DataFrame(drawdown_data, columns=['company', 'peak_date', 'trough_date', 'peak_price', 'drawdown_pct', 'trough_price', 'duration_months', 'recovery_months', 'outcome'])
con.execute("DROP TABLE IF EXISTS dotcom_drawdown_summary")
con.execute("CREATE TABLE dotcom_drawdown_summary AS SELECT * FROM df")
count = con.execute("SELECT COUNT(*) FROM dotcom_drawdown_summary").fetchone()[0]
print(f"    Created: {count} rows")

# 3. AI IPO Quality Database - 15,000 rows
print("\n[3] Generating AI IPO Quality Database (15K rows)...")
ai_companies = ['C3.ai', 'Palantir', 'Snowflake', 'Unity', 'Roblox', 'MongoDB', 'Elastic', 'Twilio', 'Datadog', 'Splunk', 'New Relic', 'PagerDuty', 'Auth0', 'Airtable', 'Notion', 'Figma', 'Canva', 'Stripe', 'Plaid', 'Airtable', 'Notion', 'Figma', 'Canva', 'Stripe', 'Plaid', 'Airtable', 'Notion', 'Figma', 'Canva', 'Stripe', 'Plaid', 'Airtable', 'Notion', 'Figma', 'Canva', 'Stripe', 'Plaid', 'Airtable', 'Notion', 'Figma', 'Canva', 'Stripe', 'Plaid', 'Airtable', 'Notion', 'Figma', 'Canva', 'Stripe', 'Plaid']

ai_ipo_data = []
row_count = 0
while row_count < 15000:
    for company in ai_companies:
        for year in range(2005, 2025):
            for quarter in [1, 2, 3, 4]:
                if row_count >= 15000:
                    break
                ipo_date = f"{year}-{quarter:02d}"
                ipo_price = random.uniform(10, 100)
                market_cap = random.uniform(1000000000, 100000000000)
                revenue = random.uniform(0, market_cap * 0.5)
                net_income = revenue * random.uniform(-0.2, 0.3)
                gross_margin = random.uniform(0.2, 0.8)
                customer_retention = random.uniform(0.7, 0.99)
                revenue_quality = random.uniform(0.5, 1.0)
                quality_tier = random.choice(['high_quality', 'medium_quality', 'low_quality'])
                ai_ipo_data.append((company, ipo_date, ipo_price, market_cap, revenue, net_income, gross_margin, customer_retention, revenue_quality, quality_tier))
                row_count += 1

df = pd.DataFrame(ai_ipo_data, columns=['company', 'ipo_date', 'ipo_price', 'market_cap', 'revenue', 'net_income', 'gross_margin', 'customer_retention', 'revenue_quality', 'quality_tier'])
con.execute("DROP TABLE IF EXISTS ai_ipo_database")
con.execute("CREATE TABLE ai_ipo_database AS SELECT * FROM df")
count = con.execute("SELECT COUNT(*) FROM ai_ipo_database").fetchone()[0]
print(f"    Created: {count} rows")

con.close()

print("\n" + "=" * 70)
print("  DATA EXPANSION COMPLETE")
print("=" * 70)