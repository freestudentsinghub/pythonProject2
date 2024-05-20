import json
from typing import Any, Dict, List

import requests

from src.logger import setup_logger

# вызов логера
logger = setup_logger("utils", "utils.log")


def list_of_the_transaction(filename: str) -> List[dict]:
    """функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
     функция возвращает пустой список."""
    logger.info(f"check filename {filename}")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info("file correct")
                return data
            else:
                logger.info("file not correct")
                return []
    except FileNotFoundError:
        logger.info("file not correct")
        return []
    except json.JSONDecodeError:
        logger.info("file not correct")
        return []


filename = "../data/operations.json"
nwe_list = list_of_the_transaction(filename)


def transaction_amount_in_rubles(transactions: Dict) -> Any:
    """функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    возвращает тип float. Если транзакция была в USD или EUR,
    идет обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли."""
    logger.info("start transaction_amount_in_rubles")
    if transactions["operationAmount"]["currency"]["code"] == "RUB":
        logger.info(f'result in RUB {transactions["operationAmount"]["amount"]}')
        return transactions["operationAmount"]["amount"]
    elif transactions["operationAmount"]["currency"]["code"] != "RUB":
        logger.info("get APL code USD or EUR")
        code = transactions["operationAmount"]["currency"]["code"]

        currency_exchange_rate = requests.get(
            f"https://v6.exchangerate-api.com/v6/04fed55e4543c3c22311996f/latest/{code}"
        )
        data = currency_exchange_rate.json()
        conversion_rates = data.get("conversion_rates")
        if conversion_rates and "RUB" in conversion_rates:
            exchange_rate = conversion_rates["RUB"]
            amount_in_rubles = float(transactions["operationAmount"]["amount"]) * exchange_rate
            logger.info(f"result in EUR or USD {amount_in_rubles}")
            return amount_in_rubles


print(nwe_list)
print(
    transaction_amount_in_rubles(
        {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {"amount": "90582.51", "currency": {"name": "USD", "code": "USD"}},
        }
    )
)

print(
    transaction_amount_in_rubles(
        {
            "id": 649467725,
            "state": "EXECUTED",
            "date": "2018-04-14T19:35:28.978265",
            "operationAmount": {"amount": "96995.73", "currency": {"name": "руб.", "code": "RUB"}},
        }
    )
)
