from typing import List
from unittest.mock import Mock

import pytest

from src.utils import list_of_the_transaction


def test_transaction_true() -> List[dict]:
    """проверяет функцию котрая возвращает список словарей
    с данными о финансовых транзакциях"""
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        },
    ]


@pytest.fixture
def test_list_of_the_transaction(test_transaction_true: List[dict], filename: str) -> None:
    get_list = list_of_the_transaction(filename)
    assert test_transaction_true in get_list


def test_transaction_amount_in_rubles() -> None:
    mock_random = Mock(return_value=8275817.395122)
    assert mock_random() == 8275817.395122


def test_transaction_amount_in_rubles_rubl() -> None:
    mock_random = Mock(return_value=96995.73)
    assert mock_random() == 96995.73
