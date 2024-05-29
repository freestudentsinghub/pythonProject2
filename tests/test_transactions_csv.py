import csv
from unittest.mock import mock_open, patch

csv_data = (
    "id;state;date;amount;currency_name;currency_code;from;to;description\n"
    "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol"
)

mock_csv_file = mock_open(read_data=csv_data)


@patch("builtins.open", mock_csv_file)
def test_read_csv() -> None:
    """тест для функции которая считывает финансовые операции с файла csv"""
    rows = []
    with open("../data/transactions.csv") as csv_file:
        for row in csv.reader(csv_file):
            rows.append(row)

    assert rows != [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]
