cnt = 0
def fibonacci_rec(n: int) -> int:
    global cnt
    cnt += 1
    return n if n <= 1 else fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
print(fibonacci_rec(10), "count", cnt)
