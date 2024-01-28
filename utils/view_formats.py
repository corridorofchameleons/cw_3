from _datetime import datetime


def encrypt_source(source):
    '''
    Chooses an encryption function depending on a source
    :param source: str; Acc No or Card No
    :return: 'undefined' if source does not exist
    '''
    if source:
        data = source.split()
        if data[0] == 'Счет':
            return encrypt_acc(data)
        else:
            return encrypt_card(data)
    return 'undefined'


def encrypt_acc(data):
    '''
    Returns encrypted acc no
    '''
    enc_acc_no = '*' + data[-1][-4:]
    return data[0] + ' ' + enc_acc_no


def encrypt_card(data) -> str:
    '''
    Returns encrypted card no
    '''
    paym_sys = ' '.join(data[:-1]) + ' '
    card_no = data[-1]

    enc_card_no = 'XXXX XX' + card_no[6:8] + ' ' + card_no[8:12] + ' XXXX'
    return paym_sys + enc_card_no


def format_date(source_date):
    '''
    Transfoms ISO datetime format into Russian date format
    :param source_date: str ISO format
    :return: str readable format
    '''
    try:
        dt = datetime.fromisoformat(source_date)
        return dt.strftime('%d.%m.%Y')
    except ValueError:
        return '<invalid date format>'
