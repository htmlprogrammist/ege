"""
Задание 6 (№536).
(М.В. Кузнецова) Найдите максимальное значение s,
при котором в результате работы программы на экране будет напечатано число 256.
Для Вашего удобства программа представлена на четырех языках программирования.
"""
s = int(input())
n = 1
while s <= 45:
    s += 4
    n *= 2
print(n)

number = 0
mx = 0
while number < 100:
    s = number
    n = 1
    while s <= 45:
        s += 4
        n *= 2
    if n == 256:
        mx = number
    number += 1
print(mx)
