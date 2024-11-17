import pytest


@pytest.fixture
def lst_for_tests_csv_xlsx() -> list:
    """Функция выдает список словарей транзакций для тестов"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
            "description": "Перевод организации"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "amount": "79114.93",
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
            "description": "Перевод со счета на счет"}
            ]
