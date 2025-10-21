import json

def convert_csv_to_json(filepath):
    with open(f'{filepath}.csv', mode='r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    with open(f'{filepath}.json', mode='w', encoding='utf-8') as jsonfile:
        json.dump(list(content.split(',')), jsonfile, indent=4)
