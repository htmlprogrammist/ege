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

15 954387771
"""
document = open('26.txt')
n = int(document.readline())
# a = []
even = []
odd = []
for i in range(n):
    # a.append(int(document.readline()))
    a = int(document.readline())
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)
# a.sort()  # все числа различны
counter = 0
summa = 0
chet = set(even)
nechet = set(odd)

for i in range(len(even)):
    for j in range(len(odd)):
        s = even[i] + odd[j]
        if s in chet or s in nechet:
            counter += 1
            if s > summa:
                summa = s
            break
print(counter, summa)
