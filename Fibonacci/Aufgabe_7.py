def fibonacci_generator(limit = None):
    a, b = 0, 1
    cnt = 0
    while limit is None or cnt < limit:
        yield a
        a, b = b, a + b
        cnt += 1


def fib_sum_1(n: int) -> int:
    sum_ = 0
    for i, f in enumerate(fibonacci_generator()):
        sum_ += f
        if i == n:
            break
    return sum_
def fib_sum_2(n: int) -> int:
    return sum(fibonacci_generator(n))


print("Summe 2:", fib_sum_2(1000))
