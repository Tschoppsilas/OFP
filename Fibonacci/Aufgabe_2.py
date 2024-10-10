def fibonacci_rec_2(n: int, cnt=0) -> (int, int):
    def fibonacci(n: int, cnt) -> (int, int):
        if n <= 1:
            cnt+=1
            return n, cnt
        else:
            fib1, cnt1 = fibonacci(n - 1, cnt)
            fib2, cnt2 = fibonacci(n - 2, cnt1)
            return fib1 + fib2, cnt2 + 1

    result, cnt = fibonacci(n, cnt)
    return (result, cnt)


print(fibonacci_rec_2(10))
print(fibonacci_rec_2(10))
