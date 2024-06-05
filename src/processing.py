from datetime import datetime


def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """Функция, которая принимает на вход список словарей и значение для ключа state
    (опциональный параметр со значением по умолчанию
    EXECUTED) и возвращает новый список, содержащий только те словари, у которых ключ"""
    function_output = []
    for check in data:
        if check.get("state") == state:
            function_output.append(check)

    return function_output


def sorted_by_datetime(data: list[dict], order: str = "descending") -> list:
    """Функция, которая принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты (ключ date)."""
    sorted_data = sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=(order == "descending"))
    return sorted_data

#
# print(
#     sorted_by_datetime(
#         data=[
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
# )

# print(
#     filter_by_state(
#         data=[
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
# )

# print(
#     filter_by_state(
#         data=[
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ],
#         state="CANCELED",
#     )
# )
