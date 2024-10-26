#gibt das zurück, was im Aufruf steht. Bsp: n=n-1, cur = cur, prev = cur+prev
def recur(*args, **kwargs) -> (callable, any):
    return recur, args, kwargs
def loop(f: callable):
    a = f()
    while isinstance(a, tuple) and a[0] is recur: #Die Schleife läuft, solange a ein Tupel ist und das erste Element von a die Funktion recur ist.
        a = f(*a[1], **a[2])
        #Die Schleife endet, wenn a kein Tupel mehr ist, dessen erstes Element recur ist.
    return a

def fibonacci_recursiv_11(n):
    def fibonacci(n, cur=0, prev=1 ):
        if n == 0:
            return cur
        else:
            return recur(n-1, cur+prev, cur)
    return loop(lambda n=n, cur=0, prev=1: fibonacci(n, cur, prev))


print(fibonacci_recursiv_11(10000))


