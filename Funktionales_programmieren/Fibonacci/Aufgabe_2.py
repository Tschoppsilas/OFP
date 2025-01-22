def fibonacci(n: int) -> int:
    cnt = 0
    def fibonacci_rec(cnt: int, n:int) -> [int, int]:
        cnt+=1

        if n <= 1: #Sicherheit, dass n nicht unter 1 geht, da es nur von pos Zahlen berechnet wird
            return n,cnt
        fibo2, cnt2 = fibonacci_rec(cnt, n - 2) #berrechnugn der kleineren
        fibo1, cnt = fibonacci_rec(cnt, n - 1)  # berechnen der grösseren fibonacci Zahl
        return fibo1 + fibo2, cnt2
    return fibonacci_rec(cnt,n)


print(fibonacci(10))
print(fibonacci(10))
