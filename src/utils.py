import json
import logging
import os

import requests
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/utils.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def reading_json_file(path: str) -> list[dict]:
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с пользовательскими параметрами"""
    try:
        logger.info('Попытка открыть JSON-файл')
        with open(path, encoding='utf-8') as f:
            lst = json.load(f)
        if not isinstance(lst, list) or not lst:
            logger.warning('Проблема с содержимым JSON-файла')
            return []
        else:
            return lst
    except FileNotFoundError:
        logger.warning('Возможна проблема с путем до JSON-файла')
        return []


def external_api_marketstack() -> list[dict]:
    """Функция для получения последних имеющихся цен на акции"""
    load_dotenv()
    apikey = os.getenv('API_KEY_MARKETSTACK')
    user_stocks = reading_json_file("user_settings.json")[0]['user_stocks']
    lst = []
    try:
        logger.info('Попытка подключения через API к сайту со стоимостью акций')
        for i in user_stocks:
            url = f"http://api.marketstack.com/v1/intraday?access_key={apikey}&symbols={i}&sort=DESC&limit=1"
            response = requests.get(url)
            dct = {"stock": i, "price": response.json()['data'][0]['close']}
            logger.info('Успешное подключение через API к сайту со стоимостью акций')
            lst.append(dct)
        return lst
    except requests.exceptions.RequestException:
        logger.warning('Возможна проблема с подключением через API к сайту со стоимостью акций')


def external_api_currency() -> list[dict]:
    """Функция для получения текущего курса валют"""
    load_dotenv()
    apikey = os.getenv('API_KEY_CURRENCY')
    headers = {
        "apikey": f"{apikey}"
    }
    user_currencies = reading_json_file("user_settings.json")[0]['user_currencies']
    lst = []
    try:
        for i in user_currencies:
            logger.info('Попытка подключения через API к сайту с курсом валют')
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={i}&amount=1"
            response = requests.get(url, headers=headers)
            dct = {"currency": i, "rate": response.json()['info']['rate']}
            lst.append(dct)
            logger.info('Успешное подключение через API к сайту с курсом валют')
        return lst
    except requests.exceptions.RequestException:
        logger.warning('Возможна проблема с подключением через API к сайту с курсом валют')
