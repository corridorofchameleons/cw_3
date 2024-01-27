from utils.functions import get_data
from utils.view_formats import encrypt_source, format_date


def main():
    client_data = get_data()
    print()

    for op in client_data:
        print(format_date(op.get('date')), op.get('description'))
        print(f"{encrypt_source(op.get('from'))} -> {encrypt_source(op.get('to'))}")
        print(op.get('operationAmount').get('amount'), op.get('operationAmount').get('currency').get('name'))
        print()


if __name__ == '__main__':
    main()
