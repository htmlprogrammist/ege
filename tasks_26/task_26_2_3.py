"""
№ 68, Джобс 31.08.2020
Задача робота заполнить как можно большее количество ящиков монетами в количестве 100 штук.
Роботу по конвейеру поступают корзины с монетами. В каждой корзине может быть от 1 до 99 монет.
Известно, что робот может высыпать в каждый ящик один раз содержимое не более двух корзин.
Необходимо написать программу, которая определяет, сколько ящиков можно заполнить ровно 100 монетами.
Входные данные представлены в файле следующим образом.
В первой строке записано число 1 < N < 10000 – количество корзин,
в каждой из последующих N строк целое число 0 < K < 100 – количество монет в каждой корзине.
В качестве ответа дать одно число – количество ящиков, заполненных 100 монетами.

Пример организации исходных данных во входном файле:
7
10
44
66
90
65
47
34
При таких исходных данных можно заполнить только 2 ящика по 100 монет 10 + 90 и 66 + 34.

3845
"""
document = open("txt/task_26_2.txt")
data = document.readlines()
n1 = int(data[0])
counter = 0
del data[0]
# data = sorted(list(map(int, data)))
data = list(map(int, data))

# file = open("task_26_2.txt")
# n = int(file.readline())
# c = []
#
# for i in range(n):
#     c.append(int(file.readline()))
#
# print(data == c)
# print(data)
# print(c)

for i in range(len(data)):
    for j in range(len(data) - 1, i, -1):
        if data[i] + data[j] == 100:
            data[i] = data[j] = 0
            counter += 1
            break
print(counter)
