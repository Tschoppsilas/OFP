from functools import cache
import time
@cache
def fibonacci_rec_5(n: int) -> int:
    return n if n <= 1 else fibonacci_rec_5(n - 1) + fibonacci_rec_5(n - 2)

print(fibonacci_rec_5(1000))
