import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str) -> Callable[[Callable], Callable]:
    """декоратор log, который будет логировать вызов функции и ее результат в файл или в консоль.
    Декоратор log принимает один необязательный аргумент filename,
    который определяет имя файла, в который будут записываться логи.
    Если filename не задан, то логи будут выводиться в консоль.
    Если вызов функции закончился ошибкой, то записывается сообщение об ошибке и входные параметры функции."""
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')} my_function ok\n"
            except Exception as e:
                result = None
                message = (
                    f"{datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')} "
                    f"my_function error:{type(e).__name__} Inputs: {args}, {kwargs}\n"
                )
            if filename:
                with open(filename, "a") as f:
                    f.write(message)
            else:
                print(message)
            return result

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """основная функция считает сумму двух чисел"""
    return x + y


my_function(1, 2)
