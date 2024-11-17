from typing import Any
from src.utils import df_to_transactions
import pandas as pd
import math


def investment_bank(month: str, transactions: list[dict[str, Any]], limit: int)-> float:
    """Функция, которая позволяет задавать комфортный порог округления: 10, 50 или 100 ₽.
     Траты будут округляться, и разница между фактической суммой трат по карте
      и суммой округления будет попадать на счет «Инвесткопилки»."""
    num = 0
    transactions = df_to_transactions(transactions)
    for i in transactions:
        if pd.to_datetime(i['Дата операции']) < pd.to_datetime(month, format='%Y-%m'):
            num += math.ceil(abs(i['Сумма операции']) / limit) * limit - abs(i['Сумма операции'])
    return num
