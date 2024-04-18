import pytest

from src import widget


@pytest.mark.parametrize(
    "name_card_and_name_account, expected",
    [
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Maestro 1596837868705199", "Maestro  1596 83** **** 5199"),
        ("Visa Platinum 8990922113665229", "Visa Platinum  8990 92** **** 5229"),
    ],
)
def test_mask_kard_and_mask_account(name_card_and_name_account: str, expected: str) -> None:
    """проверяет первую функцию из widget"""
    assert widget.mask_kard_and_mask_account(name_card_and_name_account) == expected


def test_data_mask() -> None:
    """Проверяет функцию data_mask() без parametrize потому, что принемаем только одно значение"""
    assert widget.data_mask("2018-07-11T02:26:18.671407") == "11.07.2018"
