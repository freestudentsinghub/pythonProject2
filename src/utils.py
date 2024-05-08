import json
from typing import List

import requests


def transaction(filename: str) -> List[dict]:
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
nwe_list = transaction(filename)


def amount_rub(transac: List[dict]) -> float:
    """функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    rub_list = []
    for amount in transac:
        if amount["operationAmount"]["currency"]["code"] == "RUB":
            rub_list.append(amount["operationAmount"]["amount"])

        elif amount["operationAmount"]["currency"]["code"] != "RUB":
            code = amount["operationAmount"]["currency"]["code"]

            currency_exchange_rate = requests.get(
                f"https://v6.exchangerate-api.com/v6/04fed55e4543c3c22311996f/latest/{code}"
            )
            data = currency_exchange_rate.json()

            with open("../cout.json", "w", encoding="utf-8") as f:
                json.dump(data, f)

            with open("../cout.json", "r", encoding="utf-8") as f:
                read_text = json.load(f)

                for currency, rates in read_text["conversion_rates"].items():
                    if currency == "RUB":
                        get_rub = float(rates)

                for rub in transac:
                    if rub["operationAmount"]["currency"]["code"] == "USD":
                        rub_to_usd = float(rub["operationAmount"]["amount"]) * get_rub

    return rub_to_usd


print(
    amount_rub(
        [
            {
                "id": 542678139,
                "state": "EXECUTED",
                "date": "2018-10-14T22:27:25.205631",
                "operationAmount": {"amount": "90582.51", "currency": {"name": "USD", "code": "USD"}},
            }
        ]
    )
)
