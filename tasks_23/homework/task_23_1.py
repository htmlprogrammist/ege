"""
№ 473, Джобс 12.10.2020
Исполнитель Простачок преобразует число, записанное на экране.
У исполнителя есть три команды, которым присвоены номера:
1.      Прибавить 2
2.      Прибавить предыдущее
3.      Прибавить следующее
Первая команда увеличивает число на 2, вторая – на предыдущее
(например, число 5 будет преобразовано по правилу 5 + 4),
третья – на следующее (аналогично, 5 по правилу 5 + 6 = 11)
Сколько существует таких программ, которые исходное число 7 преобразуют в число 63,
при этом траектория вычислений не содержит число 43?

116
"""
s = [0] * 64
s[7] = 1
s[9] = 1

for i in range(11, 64):
    s[i] = s[i - 2]
    if i % 2 != 0:
        s[i] += s[i // 2] + s[i // 2 + 1]
    if i == 43:
        s[i] = 0
print(s[63])
# print(s)

d = {}
for i in range(64):
    if s[i] != 0:
        d["№"+str(i)] = s[i]
    # d[str(i)] = s[i]
print(d)
