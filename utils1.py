import json
from typing import List, Any

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
        print("file not found")
        return []
    except json.JSONDecodeError:
        print("Wrong format")
        return []


filename = "data/operations.json"
nwe_list = transaction(filename)


def amount_rub(nwe_list: List[dict]) -> Any:
    """функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    rub_list = []
    for amount in nwe_list:
        if (
            "operationAmount" in amount
            and "currency" in amount["operationAmount"]
            and amount["operationAmount"]["currency"]["code"] == "RUB"
        ):
            rub_list.append(amount["operationAmount"]["amount"])
    return rub_list


rub_a_l = amount_rub(nwe_list)

count = sum(float(amount) for amount in rub_a_l)
#print(count)



def get_usd_url(nwe_list: List[dict]) -> List[float]:
    """Функция которая если транзакция была в USD или EUR,
    идет обращение к внешнему API для получения текущего курса валют"""
    currency_exchange_rate = requests.get("https://v6.exchangerate-api.com/v6/04fed55e4543c3c22311996f/latest/USD")
    data = currency_exchange_rate.json()
    with open("cout.json", "w", encoding="utf-8") as f:
        json.dump(data, f)

    with open("cout.json", "r", encoding="utf-8") as f:
        read_text = json.load(f)
        for currency, rates in read_text["conversion_rates"].items():
            if currency == "RUB":
                get_rub = float(rates)
        results = []
        for rub in nwe_list:
            if (
                "operationAmount" in rub
                and "currency" in rub["operationAmount"]
                and rub["operationAmount"]["currency"]["code"] == "USD"
            ):
                rub_to_usd = float(rub["operationAmount"]["amount"]) / get_rub
                results.append(rub_to_usd)
    return results


results = get_usd_url(nwe_list)
count_usd = sum(float(amount) for amount in results)
#print(count_usd)

all_sum = count_usd + count
print(all_sum)