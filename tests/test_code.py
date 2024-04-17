import pytest

from src import masks, processing, widget


def test_masks():
    """Проверяет функциииз модуля masks"""
    assert masks.mask_card("7000792289606361") == "7000 79** **** 6361"
    assert masks.mask_account("73654108430135874305") == "**4305"


# widget с картами и счетами
@pytest.mark.parametrize(
    "name_card_and_name_account, expected",
    [
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Maestro 1596837868705199", "Maestro  1596 83** **** 5199"),
        ("Visa Platinum 8990922113665229", "Visa Platinum  8990 92** **** 5229"),
    ],
)
def test_mask_kard_and_mask_account(name_card_and_name_account, expected):
    assert widget.mask_kard_and_mask_account(name_card_and_name_account) == expected


def test_data_mask():
    """Проверяет функцию data_mask() без parametrize потому, что принемаем только одно значение"""
    assert widget.data_mask("2018-07-11T02:26:18.671407") == "11.07.2018"


@pytest.fixture
def test_sorted_by_datetime():
    """Функция проверки сортировки по времени"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_test_sorted_by_datetime(test_sorted_by_datetime):
    """Функция проверки сортировки по времени"""
    assert processing.sorted_by_datetime(test_sorted_by_datetime) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def test_filter_by_state():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_test_filter_by_state_EXECUTED(test_filter_by_state):
    """Проверяет обычное условие"""
    assert processing.filter_by_state(test_filter_by_state) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_test_filter_by_state_CANCELED(test_filter_by_state):
    """Проверяет когда в state передается CANCELED"""
    assert processing.filter_by_state(test_filter_by_state, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
