import json

FILE_PATH = 'data/operations.json'


def get_data(file_path=FILE_PATH):
    try:
        with open(file_path) as file:
            data = json.load(file)
    except FileNotFoundError:
        return []

    data_filtered = [d for d in data if d.get('state') == 'EXECUTED']
    data_filtered.sort(key=lambda k: k.get('date'), reverse=True)
    return data_filtered[:5]
