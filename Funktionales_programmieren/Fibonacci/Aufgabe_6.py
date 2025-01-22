import time
def my_cache(func: callable) -> callable: #kreeirt den wrapper
    memo = {}

    def wrapper(*args):
        if args in memo: #gibt direkt die fibo zahl aus, falls sie bereits berechnet wurde
            result = memo[args]
        else:
            result = func(*args) #Führt die Funktion hier aus also in result wird die fibo zahl gespeichert
            memo[args] = result#speichert das resultat der berechneten fibo zahl im speicher

        return result
    return wrapper

@my_cache
def fibonacci_6(n: int) -> int:
    if n <= 1:
        resultat = n
    else: #normale fibonacci schlaufe
        resultat = fibonacci_6(n - 1)+fibonacci_6(n - 2)
    return resultat
start_time = time.time()
print(fibonacci_6(5))
end_time = time.time()
duration = end_time - start_time
print(duration)
start_time = time.time()
print(fibonacci_6(160))
end_time = time.time()
duration = end_time - start_time
print(duration)
start_time = time.time()
print(fibonacci_6(140))#in diesem Beispiel muss dies hier 0.0 Sekunden dauern, da diese bereits zuvor berechnet wurde
end_time = time.time()
duration = end_time - start_time
print(duration)
