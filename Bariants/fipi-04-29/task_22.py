"""
Задание 22 (№1300).
Ниже на четырёх языках программирования записан алгоритм. Получив на вход число x, этот алгоритм печатает два числа:
L и M. Укажите наименьшее число x, при вводе которого алгоритм печатает сначала 5, а потом 8.
"""
x = int(input())
L = 0
M = 0
while x > 0:
    M += 1
    if x % 2 != 0:
        L += 1
    x //= 2
print(L)  # 5
print(M)  # 8

number = 1
while number < 1000:
    x = number
    L = 0
    M = 0
    while x > 0:
        M += 1
        if x % 2 != 0:
            L += 1
        x //= 2
    if L == 5 and M == 8:
        print(number)
        break
    number += 1
