"""
Задание 23 (№933).
Исполнитель Кампухтер преобразует число на экране.
У исполнителя есть две команды, которым присвоены номера:
1. Прибавить 3
2. Умножить на 3
Сколько положительных четных чисел, меньших 100,
может получить исполнитель из числа 3?

16
"""
counter = 0
for n in range(3, 100, 3):
    if n % 2 == 0:
        counter += 1

print(counter)
