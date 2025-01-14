"""
Задание 16 (№1296).
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = 1 при n = 1;
F(n) = n + F(n − 1), если n чётно;
F(n) = 2 x F(n − 2), если n > 1 и при этом n нечётно.
Чему равно значение функции F(24)?
"""
from functools import lru_cache


@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + F(n - 1)
    if n > 1 and n % 2 != 0:
        return 2 * F(n - 2)


print(F(24))
