"""
№ 281, Джобс 21.09.2020
Системный администратор раз в неделю создаёт архив пользовательских файлов.
Выделяемый объем памяти рассчитывается, как общий объем файлов за вычетом количественно 10% файлов –
5% составляют самые мелкие файлы и 5% составляют самые крупные файлы.
Известно, какой объём занимает файл каждого пользователя.
Определите объем выделенного дискового пространства и размер самого крупного из сохраненных файлов.
В случае, если 5% является нецелым числом, берется целая часть от деления количества файлов на 20.

Входные данные.
В первой строке входного файла находятся два числа:
N – количество пользователей (натуральное число, 20 ≤ N ≤ 10000).
В следующих N строках находятся значения объёмов файлов каждого пользователя
(все числа натуральные, не превышающие 100), каждое в отдельной строке.

Запишите в ответе два числа: сначала объем сохраненных файлов, затем размер наибольшего сохраненного файла.

Пример входного файла (для вычета 20% файлов):
10
50
33
44
17
92
58
42
10
52
88
При таких исходных данных можно сохранить 8 файлов – 50, 33, 44, 17, 58, 42, 52, 88.
Поэтому ответ должен содержать два числа – 384 и 88.

496209 96
"""
document = open("txt/task_26_5.txt")
data = document.readlines()
n = int(data[0])
del data[0]
answers = []

data = sorted(list(map(int, data)))
five_percent = n * 0.05
length = len(data)

if five_percent.is_integer():
    five_percent = int(five_percent)
    data = data[five_percent:]
    data = data[:(length - five_percent * 2)]
else:
    five_percent = n // 20
    data = data[five_percent:]
    data = data[:(length - five_percent * 2)]

print(sum(data), max(data))
