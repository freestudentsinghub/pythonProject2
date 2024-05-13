import json
from typing import Any, Dict, List

import requests


def list_of_the_transaction(filename: str) -> List[dict]:
    """функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
     функция возвращает пустой список."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


filename = "../data/operations.json"
nwe_list = list_of_the_transaction(filename)


def transaction_amount_in_rubles(transactions: Dict) -> Any:
    """функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    возвращает тип float. Если транзакция была в USD или EUR,
    идет обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли."""
    if transactions["operationAmount"]["currency"]["code"] == "RUB":
        return transactions["operationAmount"]["amount"]
    elif transactions["operationAmount"]["currency"]["code"] != "RUB":
        code = transactions["operationAmount"]["currency"]["code"]

        currency_exchange_rate = requests.get(
            f"https://v6.exchangerate-api.com/v6/04fed55e4543c3c22311996f/latest/{code}"
        )
        data = currency_exchange_rate.json()

        with open("../currency.json", "w", encoding="utf-8") as f:
            json.dump(data, f)

        with open("../currency.json", "r", encoding="utf-8") as f:
            read_text = json.load(f)

            for currency, rates in read_text["conversion_rates"].items():
                if currency == "RUB":
                    get_rub = float(rates)

            if transactions["operationAmount"]["currency"]["code"] == "USD":
                rub_to_usd = float(transactions["operationAmount"]["amount"]) * get_rub

    return rub_to_usd


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
