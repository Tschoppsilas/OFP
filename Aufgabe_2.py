from typing import Callable


def curry(func: Callable, *x):
    def plus(*y: int) -> int:
        result = x + y
        return func(*result)
    return plus


