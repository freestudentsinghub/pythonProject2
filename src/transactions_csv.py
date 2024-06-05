from typing import Any

import pandas as pd


def read_csv(filename: str) -> list[Any]:
    """считывает финансовые операции с файла csv"""
    csv_file = pd.read_csv(filename, sep=";")
    return csv_file.to_dict(orient="records")


# print(read_csv("../data/transactions.csv"))
