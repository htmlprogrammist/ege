"""
Задание 27 (№1396).
Имеется набор данных, состоящий из троек положительных целых чисел.
Необходимо выбрать из каждой тройки ровно одно число так, чтобы сумма всех выбранных чисел не делилась на k = 123,
при этом была чётной и минимально возможной. Гарантируется, что искомую сумму получить можно.
Программа должна напечатать одно число – минимально возможную сумму, соответствующую условиям задачи.

Входные данные.
Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество троек N
(1 ≤ N ≤ 1 000 000). Каждая из следующих N строк содержит три натуральных числа, не превышающих 10 000.
Пример организации исходных данных во входном файле:
6
1 3 7
5 12 6
6 9 11
5 4 8
3 5 4
1 1 1
Для указанных входных данных, в случае, если k = 7, значением искомой суммы является число 20.
В ответе укажите два числа: сначала значение искомой суммы для файла А, затем для файла B.
Предупреждение: для обработки файла B не следует использовать переборный алгоритм,
вычисляющий сумму для всех возможных вариантов, поскольку написанная по такому алгоритму программа будет
выполняться слишком долго.

4246 2553076396
"""
f = open('27-B.txt')
n = int(f.readline())
s = [0]
for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    cmb = [a + b for a in s for b in pair]
    # s = {x % 123: x for x in sorted(cmb, reverse=True)}.values() (1)
    s = {x % 246: x for x in sorted(cmb, reverse=True)}.values()

m = min(x for x in s if x % 123 != 0 and x % 2 == 0)
print(m)
# (1) по нечетному остатку нельзя судить о четности числа

# ну типо при делении по модулю на нечетное число нельзя точно сказать делимое число четное или нет,
# поэтому делитель надо домножить на 2, и тогда уже можно судить о четности делимого

# 4 % 3 == 1 6 % 3 == 0  оба четные, разные остатки
