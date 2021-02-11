from itertools import count
from math import factorial
def generator(n):
    for el in range(1, n + 1):
        yield factorial(el)
for item in generator(int(input('Введите количество чисел '))): print(item)