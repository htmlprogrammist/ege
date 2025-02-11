""" OV
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [210 235; 210 300],
числа, имеющие ровно четыре различных натуральных делителя, не считая единицы и самого числа. Для каждого
найденного числа запишите эти четыре делителя в четыре соседних столбца на экране с новой строки. Делители в
строке должны следовать в порядке возрастания.
Например, в диапазоне [10; 16] ровно четыре различных натуральных делителя имеет число 12, поэтому для этого
диапазона вывод на экране должна содержать следующие значения:
2 3 4 6

2 4 52561 105122
2 4 52567 105134
2 4 52571 105142
"""
import math


dividers = []

for i in range(210235, 210300 + 1):
    dividers = []
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            dividers.append(j)
            dividers.append(i // j)
    if len(dividers) == 4:
        # print(dividers[0], dividers[1], dividers[2], dividers[3])
        print(dividers[0], dividers[2], dividers[3], dividers[1])
