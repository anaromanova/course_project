from typing import Any
from utils import df_to_transactions
import pandas as pd


def investment_bank(month: str, transactions: list[dict[str, Any]], limit: int) -> float:
    """Функция, которая возвращает json с сервисом по Выгодным категориям повышенного кешбэка."""
    num = 0
    for i in transactions:
        if str(pd.to_datetime(i['Дата операции']).strftime('%Y-%m')) < month:
            num += abs(i['Сумма операции'])

    return num

print(investment_bank('2018-10',df_to_transactions('data/operations.xlsx'), 10))