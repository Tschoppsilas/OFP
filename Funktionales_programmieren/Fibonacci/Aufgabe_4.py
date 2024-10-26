def fibonacci_rec_3(n: int, memo=None, cnt=0) -> (int, int):
    # Initialisiere das Dictionary, wenn es nicht bereits existiert
    if memo is None:
        memo = {}

    # Überprüfen, ob der Wert bereits im Dictionary gespeichert ist
    if n in memo:
        return memo[n], cnt

    # Berechnung der Fibonacci-Zahl
    if n <= 1:
        cnt += 1
        return n, cnt
    else:
        fib1, cnt1 = fibonacci_rec_3(n - 1, memo, cnt)
        fib2, cnt2 = fibonacci_rec_3(n - 2, memo, cnt1)
        resultat = fib1 + fib2
        cnt = cnt2 + 1

    # Ergebnis im Dictionary speichern
    memo[n] = resultat
    return resultat, cnt

print(fibonacci_rec_3(20))
print(fibonacci_rec_3(10))
print(fibonacci_rec_3(20))
