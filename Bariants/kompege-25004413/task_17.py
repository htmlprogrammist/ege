"""
Задание 17 (№1297). Рассматривается множество целых чисел, принадлежащих числовому отрезку [16 015; 48 989],
которые делятся на 7 или 11 и не делятся на 9, 12, 13.
Найдите количество таких чисел и минимальное из них. В ответе запишите два целых числа: сначала количество,
затем минимальное число.
Для выполнения этого задания можно написать программу или воспользоваться редактором электронных таблиц.
"""
a = []

for i in range(16015, 48989 + 1):
    if i % 7 == 0 or i % 11 == 0:
        if i % 9 != 0 and i % 12 != 0 and i % 13 != 0:
            a.append(i)

print(len(a), min(a))
