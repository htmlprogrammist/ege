"""
Задание 16 (№610).
Алгоритм вычисления функции F(n) задан следующими соотношениями:
F(n) = 1+2n при n < 5
F(n) = 2·(n + 1)·F(n–2), если n ≥ 5 и n делится на 3,
F(n) = 2·n + 1 + F(n–1) + 2·F(n–2), если n ≥ 5 и n не делится на 3.
Чему равно значение функции F(15)?
"""


def F(n):
    if n < 5:
        return 1 + 2 * n
    if n >= 5 and n % 3 == 0:
        return 2 * (n + 1) * F(n - 2)
    if n >= 5 and n % 3 != 0:
        return 2 * n + 1 + F(n - 1) + 2 * F(n - 2)


print(F(15))
