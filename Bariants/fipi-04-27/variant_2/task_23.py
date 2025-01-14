"""
Задание 23 (№1229).
Исполнитель Май преобразует число на экране. У исполнителя есть две команды, которым присвоены номера:
1. Прибавить 1
2. Умножить на 2
Первая команда увеличивает число на экране на 1, вторая умножает его на 2.
Программа для исполнителя Май — это последовательность команд.
Сколько существует программ, для которых при исходном числе 2 результатом является число 45
и при этом траектория вычислений содержит числа 9 и 20?
"""
k = [0] * 46
k[2] = 1

for n in range(2, 9 + 1):
    if n + 1 <= 9:
        k[n + 1] += k[n]
    if n * 2 <= 9:
        k[n * 2] += k[n]

for n in range(9, 20 + 1):
    if n + 1 <= 20:
        k[n + 1] += k[n]
    if n * 2 <= 20:
        k[n * 2] += k[n]

for n in range(20, 45 + 1):
    if n + 1 <= 45:
        k[n + 1] += k[n]
    if n * 2 <= 45:
        k[n * 2] += k[n]
print(k[45])
