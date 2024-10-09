def fibonacci_rec_2(n: int) -> int:

    def fibonacci(n: int, cnt: int) -> int:
        print(n)
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1, cnt) + fibonacci(n - 2, cnt)

    return fibonacci(n, 0) #da ich hier die cnt Variable definiere, kann sie von aussn nicht angepasst werden, was bedeutet, dass die funktion pure ist


print(fibonacci_rec_2(1000))



