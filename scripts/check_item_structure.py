import zipfile
import json

with zipfile.ZipFile('DATA/not preprocessed/more data/companyfacts.zip', 'r') as zf:
    json_files = [f for f in zf.namelist() if f.endswith('.json')]
    
    with zf.open(json_files[0]) as f:
        data = json.load(f)
        
        found = False
        for cat_name, cat_data in data.get('facts', {}).items():
            for tag, tag_data in cat_data.items():
                units = tag_data.get('units', {})
                for unit_name, unit_data in units.items():
                    if unit_data:
                        print(f'Category: {cat_name}')
                        print(f'Tag: {tag}')
                        print(f'Unit: {unit_name}')
                        print(f'Number of items: {len(unit_data)}')
                        print(f'First item: {unit_data[0]}')
                        print(f'Item keys: {list(unit_data[0].keys())}')
                        print(f'Item value: {unit_data[0].get("value")}')
                        found = True
                        break
                if found:
                    break
            if found:
                break