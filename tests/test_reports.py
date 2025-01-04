import json
from math import nan

import pandas as pd

from src.reports import decorator_with_args, spending_by_category


def test_decorator_with_args(lst_for_tests_csv_xlsx):
    @decorator_with_args('logs/decorators_mistakes.json')
    def test_spending_by_category():
        data = [{'Дата операции': '2021-12-30 22:22:03', 'Номер карты': nan, 'Статус': 'OK', 'Сумма операции': -20000.0,
                'Валюта операции': 'RUB', 'Сумма платежа': -20000.0, 'Валюта платежа': 'RUB', 'Категория': 'Переводы',
                'Описание': 'Константин Л.'}]
        data = json.dumps(data, ensure_ascii=False)
        assert spending_by_category(pd.DataFrame(lst_for_tests_csv_xlsx),'Переводы', "31.10.2021").to_dict("records") == data
        return spending_by_category(pd.DataFrame(lst_for_tests_csv_xlsx),'Переводы', "31.10.2021")
    result = test_spending_by_category()
    with open('logs/decorators_mistakes.json', encoding="utf-8") as file:
        data_json = json.load(file)
    assert result.to_dict('records') == data_json
