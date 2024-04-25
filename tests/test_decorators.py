import os
from typing import Generator

import pytest

from src.decorators import my_function


@pytest.fixture
def log_output_filename() -> Generator:
    yield "mylog.txt"


def test_file_or_console(log_output_filename: str) -> None:
    """проверяет создался ли специальны файл, если же нет, то выводит в консоль"""
    assert os.path.isfile(log_output_filename)
    if not os.path.isfile(log_output_filename):
        print()


@pytest.mark.parametrize("x, y, expected_result", [(1, 2, 3)])
def test_log_decorator_file(log_output_filename: str, x: int, y: int, expected_result: int) -> None:
    """проверяет наличие выполнения декоратора в файле"""
    my_function(x, y)
    with open(log_output_filename, "r") as f:
        result = f.read()
    assert f"{'my_function ok'}\n" in result


@pytest.mark.parametrize("x, y, expected_result", [(1, 2, 3), (1, 2, None)])
def test_log_decorator_file_mistake(log_output_filename: str, x: int, y: int, expected_result: int) -> None:
    """проверяет если возникла ошибка наличие сообщения об ошибке в файле"""
    my_function(x, y)
    try:
        with open(log_output_filename, "r") as f:
            result = f.read()
        assert f"{'my_function ok'}\n" in result
    except Exception as e:
        with open(log_output_filename, "r") as f:
            result = f.read()
        assert f"my_function error:{type(e).__name__} Inputs:  ({x}, {y})\n" in result
