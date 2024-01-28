from utils.functions import get_data, FILE_PATH
from utils.view_formats import encrypt_source, format_date


def main():
    '''
    Shows latest 5 successful bank operations
    :return: None
    '''
    client_data = get_data(FILE_PATH)
    print()

    for op in client_data:
        print(format_date(op.get('date')), op.get('description'))
        print(f"{encrypt_source(op.get('from'))} -> {encrypt_source(op.get('to'))}")
        print(op.get('operationAmount').get('amount'), op.get('operationAmount').get('currency').get('name'))
        print()


if __name__ == '__main__':
    main()
