def fibonacci_rec_3(n: int, memo=None) -> int:
    # Initialisiere das Dictionary, wenn es nicht bereits existiert
    if memo is None:
        memo = {}

    # Überprüfen, ob der Wert bereits im Dictionary gespeichert ist
    if n in memo:
        return memo[n]

    # Berechnung der Fibonacci-Zahl
    if n <= 1:
        resultat = n
    else:
        resultat = fibonacci_rec_3(n - 1, memo) + fibonacci_rec_3(n - 2, memo)
        # fibonacci_rec(n - 1, memo), Ruft die Fibonacci-Zahl für n-1 ab und nutzt das memo-Dictionary, um bereits
        # berechnete Werte zu finden und die Effizienz zu steigern. Es ergibt sich also quasi einen Rattenschwanz
        # bis n = 0 ist.

    # Ergebnis im Dictionary speichern
    memo[n] = resultat
    return resultat



print("Fibonacci 1'000:", fibonacci_rec_3(1000))



