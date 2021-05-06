"""
В текстовом файле записан набор натуральных чисел, не превышающих 10 ** 9.
Гарантируется, что все числа различны. Необходимо определить, сколько в наборе таких пар чисел,
что числа в паре имеют разную чётность, а их сумма тоже присутствует в файле,
и чему равна наибольшая из сумм таких пар.

Входные данные
Первая строка входного файла содержит целое число 𝑁 – общее количество чисел в наборе.
Каждая из следующих 𝑁 строк содержит одно число.

Пример входного файла
6
3
8
14
11
22
17

В данном случае есть две подходящие пары: 3 и 8 (сумма 11), 3 и 14 (сумма 17). В ответе надо записать числа 2 и 17.
"""
document = open('26_example.txt')
n = int(document.readline())
a = []
for i in range(n):
    a.append(int(document.readline()))
a.sort()  # все числа различны
counter = 0
summa = 0

for i in range(n - 1):
    for j in range(1, n):
        if (a[i] + a[j]) % 2 != 0:  # числа в паре имеют разную чётность (1, 2; 3, 4 - все в сумме дают нечетное)
            # for number in a:
            for k in range(i, len(a)):
                if a[i] + a[j] == a[k]:
                    counter += 1
                    if a[i] + a[j] > summa:
                        summa = a[i] + a[j]
print(counter, summa)
