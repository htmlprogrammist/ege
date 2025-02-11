""" OV
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [245690;245756]
простые числа. Выведите на экран все найденные простые числа в порядке возрастания,
слева от каждого числа выведите его порядковый номер в последовательности.
Каждая пара чисел должна быть выведена в отдельной строке.
Например, в диапазоне [5; 9] ровно два различных натуральных простых числа - это числа 5 и 7,
поэтому для этого диапазона вывод на экране должна содержать следующие значения:
1 5
3 7
Примечание. Простое число - натуральное число, имеющее ровно два различных
натуральных делителя - единицу и самого себя.

22 245711
30 245719
34 245723
52 245741
58 245747
64 245753
"""
import math

order_number = 0
dividers = []

# for i in range(245690, 245756 + 1):
#     dividers = []
#     order_number += 1
#     for j in range(2, i // 2 + 1):
#         if i % j == 0:
#             k = 0
#             for d in range(2, j // 2 + 1):
#                 if j % d == 0:
#                     k += 1
#             if k == 0:
#                 print(order_number, i)

# for i in range(245690, 245756 + 1):
#     order_number += 1
#     for j in range(2, int(math.sqrt(i)) + 1):
#         if i % j == 0:
#             k = 0
#             for d in range(2, int(math.sqrt(j)) + 1):
#                 if j % d == 0:
#                     k += 1
#             if k == 0:
#                 print(order_number, i)

for i in range(245690, 245756 + 1):
    order_number += 1
    counter = 0
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            counter += 1
    if counter == 0:
        print(order_number, i)
