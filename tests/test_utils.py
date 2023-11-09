from utils.utils import sort_only_dates, sort_by_date, get_reformat_dates, get_reform_numbers, get_executed


def test_sort_only_dates():
    assert sort_only_dates([{'date': 2}, {'date': 1}, {'date': 3}]) == [3, 2, 1]


def test_sort_by_date():
    assert sort_by_date([{'date': "2"}, {'date': "1"}, {'date': "3"}]) == [{'date': "3"}, {'date': "2"}, {'date': "1"}]


def test_get_reformat_dates():
    assert get_reformat_dates([{'date': '2023-11-08'}, {'date': '2023-09-07'}, {'date': '2023-10-06'}]) == [{'date': '08.11.2023'}, {'date': '06.10.2023'}, {'date': '07.09.2023'}]


def test_get_reform_numbers():
    assert get_reform_numbers([{'date': '2023-11-08', 'from': 'Счет 00000000000000000000', 'to': 'МИР 0000000000000000'}]) == [{'date': '08.11.2023', 'from': 'Счет **0000', 'to': 'МИР 0000 00** **** 0000'}]


def test_get_executed():
    assert get_executed([{'state': 'CANCELED', 'date': '2023-08-11', 'from': 'МИР 0000000000000000', 'to': 'Счет 00000000000000000000'}, {'state': 'EXECUTED', 'date': '2023-10-09', 'from': 'Счет 00000000000000000000', 'to': 'МИР 0000000000000000'}]) == [{'state': 'EXECUTED', 'date': '09.10.2023', 'from': 'Счет **0000', 'to': 'МИР 0000 00** **** 0000'}]