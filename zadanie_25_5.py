"""
Задание 25 (№315).

Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [326496; 649632],
числа, у которых количество четных делителей равно количеству нечетных делителей.
При этом в каждой из таких групп делителей не менее 70 элементов.
Для каждого найденного числа запишите само число и минимальный делитель, больший 1000.

Например, для числа 2018 имеем следующие делители 2 и 1009.
Поэтому результатом (не принимая во внимание количества делителей) будет пара чисел 2018 1009
"""
import math

a = []
counter1 = 0
counter2 = 0
for i in range(326496, 649632 + 1):
    sqrt_i = int(math.sqrt(i))
    k = 0
    counter1 = 0
    counter2 = 0
    if sqrt_i ** 2 == i:
        k += 1
    for j in range(2, int(math.sqrt(i)) + 1 - k):
        if counter1 >= 70:
            # print('Наше число', i)  # ! Выводит каждое число
            break
        # for j in range(2, int(i // 2) + 1):
        if i % j == 0:
            if j % 2 == 0:
                counter1 += 1
            else:
                counter2 += 1
            if i // j % 2 == 0:
                counter1 += 1
            if i // j % 2 != 0:
                counter2 += 1
    if counter1 == counter2 and counter1 >= 70:
        print(i)
