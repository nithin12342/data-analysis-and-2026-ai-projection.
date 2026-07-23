import zipfile
import json

with zipfile.ZipFile('DATA/not preprocessed/more data/companyfacts.zip', 'r') as zf:
    json_files = [f for f in zf.namelist() if f.endswith('.json')]
    
    with zf.open(json_files[0]) as f:
        data = json.load(f)
        print(f'Keys: {list(data.keys())}')
        print(f'cik: {data.get("cik", "NOT FOUND")}')
        print(f'entityName: {data.get("entityName", "NOT FOUND")}')
        
        facts = data.get('facts', {})
        print(f'Number of fact categories: {len(facts)}')
        print(f'Fact categories: {list(facts.keys())}')
        
        # Check first category
        for cat_name, cat_data in facts.items():
            print(f'\nCategory: {cat_name}')
            print(f'  Keys: {list(cat_data.keys())}')
            if 'units' in cat_data:
                units = cat_data['units']
                print(f'  Number of units: {len(units)}')
                for unit_name, unit_data in units.items():
                    print(f'  Unit: {unit_name}, items: {len(unit_data)}')
                    if unit_data:
                        print(f'  First item: {unit_data[0]}')
            break  # Only check first category