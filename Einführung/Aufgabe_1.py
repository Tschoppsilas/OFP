from functools import reduce
def anzahl_gerade_filter(x: list[int]) -> int:
    return len(list(filter(lambda x: x % 2 == 0, x)))

def anzahl_gerade_reduce(x: list[int]) -> int:
    def summe(acc: int, num: int) -> int:
        return acc + (1 if num % 2 == 0 else 0)
    return reduce(summe, x, 0)
