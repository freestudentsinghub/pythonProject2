import json

import pytest

from utils1 import transaction


def test_transaction(filename):
    file_path = filename/'data/operations.json'
    file_path.write_text("")
    assert transaction(str(file_path)) == []






def test_amount_rub():
    pass


def test_get_usd_url():
    pass
