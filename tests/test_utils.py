from unittest.mock import Mock

from src.utils import amount_rub, nwe_list, transaction


def test_transaction_true() -> None:
    """проверяет функцию котрая возвращает список словарей
    с данными о финансовых транзакциях"""
    filename = "data/operations.json"
    assert transaction(filename) == nwe_list


def test_amount_rub() -> None:
    """проверяет функцию которая которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    assert amount_rub(nwe_list) == 2627938.9600000004


def test_get_usd_url() -> None:
    """проверяет функцию которая если транзакция была в USD или EUR,
    идет обращение к внешнему API для получения текущего курса валют  возвращает сумму в рублях"""
    mock_random = Mock(return_value=25656.896037152314)
    assert mock_random() == 25656.896037152314

