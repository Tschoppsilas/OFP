def fibonacci_rec(n: int, memo:dict = None) -> int:
    if memo is None: #Memo erstellen, falls keines angegeben
        memo = {}
    if n in memo: #vor berechnung kontrollieren, ob es nicht bereits berechnet wurde
        return memo[n]
    if n <= 1:
        resultat = n
    else: #normale fibonacci schlaufe
        resultat = fibonacci_rec(n - 1, memo)+fibonacci_rec(n - 2, memo)
    memo[n] = resultat
    return resultat

print(fibonacci_rec(10))