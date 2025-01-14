"""
Задание 23 (№1418).
Исполнитель Счётчик преобразует число на экране:
У исполнителя есть две команды, которым присвоены номера:
1. Прибавить 5
2. Умножить на 5
Первая команда увеличивает число на экране на 5, вторая умножает его на 5.
Программа для исполнителя Счётчик - это последовательность команд.
Сколько существует программ, для которых при исходном числе 5 результатом является число 280
и при этом траектория вычислений содержит число 30 и не содержит числа 60?
Траектория вычислений программы - это последовательность результатов выполнения всех команд программы.
"""
k = [0] * 281
k[5] = 1
for n in range(5, 30 + 1):
    if n + 5 <= 30:
        k[n + 5] += k[n]
    if n * 5 <= 30:
        k[n * 5] += k[n]

for n in range(30, 280 + 1):
    if n == 60:
        continue
    if n + 5 <= 280:
        k[n + 5] += k[n]
    if n * 5 <= 280:
        k[n * 5] += k[n]
print(k[280])
