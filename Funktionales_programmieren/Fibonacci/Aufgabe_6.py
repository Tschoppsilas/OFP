def my_cache(func:callable) -> callable:
    memo = {}
    def wrapper(*args):
        if args in memo:
            result = memo[args]
        else:
            result = func(*args)
            memo[args] = result
        return result
    return wrapper

@my_cache
def fibonacci_6(n:int) -> int:
    if n <= 1:
        resultat = n
    else:
        resultat = fibonacci_6(n - 1) + fibonacci_6(n - 2)
    return resultat

print(fibonacci_6(1000))
