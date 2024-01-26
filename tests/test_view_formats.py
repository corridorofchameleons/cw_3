import pytest

from utils.view_formats import encrypt_source, format_date


def test_encrypt_source():
    assert encrypt_source('Arch 1234567887654321') == 'Arch XXXX XX78 8765 XXXX'
    assert encrypt_source('Счет 1234567890') == 'Счет *7890'


def test_format_date():
    assert format_date('2019-04-11T23:10:21.514616') == '11.04.2019'
    assert format_date('error') == '<invalid date format>'
