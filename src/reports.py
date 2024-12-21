from datetime import datetime
from typing import Optional
import json
import pandas as pd
from dateutil.relativedelta import relativedelta


def decorator_with_args(file):
    def my_big_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                with open(file, "w", encoding="utf-8") as file_2:
                    json.dump(result.to_dict("records"), file_2)
                return result
            except FileNotFoundError:
                print("Не получилось записать информацию в файл")
        return wrapper
    return my_big_decorator


@decorator_with_args('logs/decorators_mistakes.json')
def spending_by_category(transactions: pd.DataFrame,
                         category: str,
                         date: Optional[str] = str(datetime.now())) -> pd.DataFrame:
    transactions['Дата операции'] = pd.to_datetime(transactions['Дата операции'], dayfirst=True)
    """Функция, которая возвращает датафрейм с тратами по заданной категории за последние три месяца (от переданной даты)."""
    transactions_by_category = transactions[(transactions['Дата операции'] >= pd.to_datetime(date, dayfirst=True) - relativedelta(months=2))
                 & (transactions['Дата операции'] <= pd.to_datetime(date, dayfirst=True))
                 & (transactions['Категория'].str.upper() == category.upper())]
    transactions_by_category['Дата операции'] = transactions_by_category['Дата операции'].astype(str)
    return transactions_by_category
