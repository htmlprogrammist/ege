"""
№ 60, Джобс 31.08.2020
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(0) = 1, F(1) = 1
F(n) = 3*F(n–1) - F(n-2), при n > 1
Чему равно значение функции F(6)? В ответе запишите только целое число.
"""


def F(n):
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return 3 * F(n - 1) - F(n - 2)


print(F(20))