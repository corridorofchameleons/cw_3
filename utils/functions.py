import json

# path to fake db from root
FILE_PATH = 'data/operations.json'


def get_data(file_path):
    '''
    SELECT * FROM operations
    WHERE state='EXECUTED'
    ORDER BY date DESC
    LIMIT 5
    '''

    try:
        with open(file_path) as file:
            data = json.load(file)
    except FileNotFoundError:
        return []

    data_filtered = [d for d in data if d.get('state') == 'EXECUTED']
    data_filtered.sort(key=lambda k: k.get('date'), reverse=True)
    return data_filtered[:5]
