from typing import Callable
from functools import reduce

def mein_filter(func: Callable[[int], bool], x:list[int]) -> list[int]:
    def filtern(acc:list[int], num:int)->list[int]:
        print([num])
        if func(num):
            return acc + [num]
        else:
            return acc
    return reduce(filtern, x, [])

