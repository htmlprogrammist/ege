"""
(№ 2305) (А. Куканова)
Рассматривается множество целых чисел, принадлежащих числовому отрезку [1221; 9763],
которые делятся на 7 и не делятся на 2, 5, 11, 49. Найдите количество таких чисел и максимальное из них.

380 9737
"""
counter = 0
max_i = 0

for i in range(1221, 9763 + 1):
    if i % 7 == 0 and i % 2 != 0 and i % 5 != 0 and i % 11 != 0 and i % 49 != 0:
        counter += 1
        max_i = i

print(counter, max_i)
