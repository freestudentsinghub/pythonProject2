import os.path

from unittest.mock import Mock

from src.transactions_excel import read_excel

from pandas import DataFrame
from unittest.mock import patch
import os


@patch('pandas.read_excel')
def test_read_excel(mock_open: Mock) -> None:
    mock_open.return_value = DataFrame(
        {'id': [650703.0],
         'state': ['EXECUTED'],
         'date': ['2023-09-05T11:30:32Z'],
         'amount': [16210.0],
         'currency_name': ['Sol'],
         'currency_code': ['PEN'],
         'from': ['Счет 58803664561298323391'],
         'to': ['Счет 39745660563456619397'],
         'description': ['Перевод организации']}
    )

    assert read_excel(os.path.join("../data/transactions_excel.xlsx")) == [{'id': 650703.0,
                                                                                         'state': 'EXECUTED',
                                                                                         'date': '2023-09-05T11:30:32Z',
                                                                                         'amount': 16210.0,
                                                                                         'currency_name': 'Sol',
                                                                                         'currency_code': 'PEN',
                                                                                         'from': 'Счет 58803664561298323391',
                                                                                         'to': 'Счет 39745660563456619397',
                                                                                         'description': 'Перевод организации'}]
