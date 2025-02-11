"""
№ 23, Демоверсия 2020
Имеется набор данных, состоящий из пар положительных целых чисел.
Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма всех выбранных чисел не делилась на 3
и при этом была максимально возможной. Гарантируется, что искомую сумму получить можно.
Программа должна напечатать одно число – максимально возможную сумму, соответствующую условиям задачи.
Входные данные.
Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество пар N (1 ≤ N ≤ 100000).
Каждая из следующих N строк содержит два натуральных числа, не превышающих 10 000.
Пример организации исходных данных во входном файле:
6
1 3
5 12
6 9
5 4
3 3
1 1
Для указанных входных данных значением искомой суммы должно быть число 32. В ответе укажите два числа:
сначала значение искомой суммы для файла А, затем для файла B.
Предупреждение: для обработки файла B не следует использовать переборный алгоритм,
вычисляющий сумму для всех возможных вариантов, поскольку написанная по такому алгоритму программа
будет выполняться слишком долго.

127127 399762080
"""
f = open('txt/27-B-23.txt')
n = int(f.readline())
# начальное значение S - это самая первая пара
s = list(map(int, f.readline().split()))

for i in range(n - 1):  # делаем -1, потому что первую строку мы уже прочитали
    pair = list(map(int, f.readline().split()))
    cmb = [a + b for a in s for b in pair]
    s1 = [0] * 3
    for x in cmb:
        # эта штука находит максимальный элемент с остатками 0, 1, 2
        s1[x % 3] = max(s1[x % 3], x)
        # аналог
        # if x > s1[x % 3]:
        #     s1[x % 3] = x
    s = [x for x in s1 if x != 0]  # ноль переводить не надо, поэтому мы в s будем заносить только те числа,
    # которые не равны 0

m = 0
for x in s:
    if x % 3 != 0 and x > m:
        m = x
print(m)
