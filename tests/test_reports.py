import json

import pandas as pd

from src.reports import decorator_with_args, spending_by_category


# def test_decorator_with_args():
#     @decorator_with_args('logs/decorators_mistakes.json')
def test_spending_by_category(lst_for_tests_csv_xlsx):
    data = {
        "Супермаркеты": -753.68,
        "Tuesday": -549.29,
        "Monday": -1356.3,
        "Sunday": -1303.8,
        "Saturday": -311.52,
        "Friday": -2358.73,
        "Thursday": -435.24,
    }
    data = json.dumps(data)
    assert spending_by_category(pd.DataFrame(lst_for_tests_csv_xlsx),"Супермаркеты", "14.10.2021").to_dict("records") == data
    # return spending_by_category(df_file,"Супермаркеты", "14.10.2020")

    # result = test_spending_by_category()
    # with open('logs/decorators_mistakes.json', encoding="utf-8") as file:
    #     data_json = json.load(file)
    # assert result == data_json