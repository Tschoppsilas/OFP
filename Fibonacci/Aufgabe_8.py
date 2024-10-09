import sys
sys.path.append(r"C:\Users\silas\PycharmProjects\OFP\Fibonacci")
from Aufgabe_7 import fibonacci_generator

def squares_of_even_fibonacci(n: int) -> int:
    even = []
    for i in fibonacci_generator(n):
        if i%2 == 0:
            even.append(i)
    return sum(even)

print(squares_of_even_fibonacci(10))

