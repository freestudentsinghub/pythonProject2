import json
from unittest.mock import MagicMock, patch

from src.utils import list_of_the_transaction, transaction_amount_in_rubles


def test_transaction_amount() -> None:
    """тест проверяет функцию, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    возвращает тип float. Если транзакция была в USD или EUR,
    идет обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли."""
    with patch("src.utils.requests.get") as mock_get:
        mock_response = {"conversion_rates": {"RUB": 92.591}}
        mock_get.return_value.json.return_value = mock_response

        result = transaction_amount_in_rubles(
            {
                "id": 542678139,
                "state": "EXECUTED",
                "date": "2018-10-14T22:27:25.205631",
                "operationAmount": {"amount": "90582.51", "currency": {"name": "USD", "code": "USD"}},
            }
        )
        assert result == 8387125.183409999
        mock_get.assert_called_once_with("https://v6.exchangerate-api.com/v6/04fed55e4543c3c22311996f/latest/USD")


@patch("builtins.open")
@patch("json.load")
def test_list_of_the_transaction(mock_json_load: MagicMock, mock_open: MagicMock) -> None:
    """тест проверяет функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
     функция возвращает пустой список."""
    filename = "../data/operations.json"
    mock_data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]

    mock_open.return_value.__enter__.return_value = json.dumps(mock_data)
    mock_json_load.return_value = mock_data

    new_list = list_of_the_transaction(filename)

    assert new_list == mock_data
    mock_open.assert_called_once_with(filename, "r", encoding="utf-8")
    mock_json_load.assert_called_once()
