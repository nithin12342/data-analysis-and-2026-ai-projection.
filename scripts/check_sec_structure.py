import zipfile
import json

with zipfile.ZipFile('DATA/not preprocessed/more data/companyfacts.zip', 'r') as zf:
    json_files = [f for f in zf.namelist() if f.endswith('.json')]
    print(f'Total JSON files: {len(json_files)}')
    print(f'First 5 files: {json_files[:5]}')
    
    with zf.open(json_files[0]) as f:
        data = json.load(f)
        print(f'Keys: {list(data.keys())[:10]}')
        print(f'cik: {data.get("cik", "NOT FOUND")}')
        print(f'ticker: {data.get("ticker", "NOT FOUND")}')
        
        facts = data.get('facts', {})
        print(f'Number of fact tags: {len(facts)}')
        if facts:
            first_tag = list(facts.keys())[0]
            print(f'First tag: {first_tag}')
            units = facts[first_tag].get('units', {})
            if units:
                first_unit = list(units.keys())[0]
                print(f'First unit: {first_unit}')
                print(f'Number of items: {len(units[first_unit])}')
                if units[first_unit]:
                    print(f'First item: {units[first_unit][0]}')