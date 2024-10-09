def fibonacci_recursiv_9(n, cur = 0, prev = 1):
    if n == 0:
        return cur
    else:
        return fibonacci_recursiv_9(n-1, cur+prev, cur)

print(fibonacci_recursiv_9(10000))
