"""
№ 441, Джобс 05.10.2020
Системный администратор раз в неделю создаёт архив пользовательских файлов.
Известно, какой объём занимает файл каждого пользователя. Сохраняются файлы всех пользователей.
Каждый файл в архиве может быть либо сжат, либо сохранен в исходном состоянии.
Сжатый файл занимает в памяти 80% от исходного. Для архива выделяется объем,
равный 90% от общего объема файлов пользователей до сжатия.
Для ускорения процесса создания архива как можно большее количество файлов сохраняется без сжатия.
Определите максимально возможное количество файлов, которое может быть сохранено без сжатия и
максимально возможный размер такого файла.

Входные данные.
В первой строке входного файла находятся два числа:
N – количество пользователей (натуральное число, 20 ≤ N ≤ 10000).
В следующих N строках находятся значения объёмов файлов каждого пользователя
(все числа натуральные, не превышающие 100), каждое в отдельной строке.

Запишите в ответе два числа: сначала количество не сжатых файлов,
затем наибольший размер сохраненного без сжатия файла.

Пример входного файла:
7
13
17
5
55
61
9
10

При таких исходных данных ответ должен содержать 2 числа – 5 и 13.

6808 99
"""
document = open("txt/task_26_8.txt")
data = document.readlines()
n = int(data[0])
del data[0]
data = sorted(list(map(int, data)))

k = n - 1

while sum(data[:k]) + sum(data[k:]) * 0.8 >= sum(data) * 0.9:
    k -= 1

print(len(data) - len(data[k:]), max(data[:k]))
