"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [210235; 210300],
числа, имеющие ровно четыре различных натуральных делителя, не считая единицы и самого числа.
Для каждого найденного числа запишите эти четыре делителя в четыре соседних столбца на экране с новой строки.
Делители в строке должны следовать в порядке возрастания.

Например, в диапазоне [10; 16] ровно четыре различных натуральных делителя имеет число 12,
поэтому для этого диапазона вывод на экране должна содержать следующие значения: 2 3 4 6

Ответ:
2 4 52561 105122
2 4 52567 105134
2 4 52571 105142
"""
max_divider = 1
a = []
for i in range(210235, 210300):
    divider = 0
    a = []
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            divider += 1
            a.append(j)
    if divider == 4:
        print(a)
