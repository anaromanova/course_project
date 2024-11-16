from datetime import datetime
from typing import Optional
from dateutil.relativedelta import relativedelta
import pandas as pd


def spending_by_category(transactions: pd.DataFrame,
                         category: str,
                         date: Optional[str] = str(datetime.now())) -> pd.DataFrame:
    """Функция, которая возвращает датафрейм с тратами по заданной категории за последние три месяца (от переданной даты)."""
    return transactions[(transactions['Дата операции'] <= pd.to_datetime(date, dayfirst=True) + relativedelta(months=2)) &\
                 (transactions['Дата операции'] >= pd.to_datetime(date, dayfirst=True)) &\
                 (transactions['Категория'] == category)]
