"""
№ 632, Джобс 02.11.2020
Ниже приведён алгоритм. Получив на вход число x, этот алгоритм печатает число S.
Укажите наибольшее число x, при вводе которого алгоритм печатает 82.
"""

# x = int(input())
# P = 90
# S = 6 * (x - x % 22)
# K = 0
# while P < 181:
#     K += 1
#     P += K
#     S = S - 2 * K
# print(S)

number = 0
mx = 0
while number < 1000:
    x = number
    P = 90
    S = 6 * (x - x % 22)
    K = 0
    while P < 181:
        K += 1
        P += K
        S = S - 2 * K
    if S == 82:
        mx = number
    number += 1
print(mx)