"""
Задание 26 (№1275).
Системный администратор раз в неделю создаёт архив пользовательских файлов.
Однако объём диска, куда он помещает архив, может быть меньше, чем суммарный объём архивируемых файлов.
Известно, какой объём занимает файл каждого пользователя. Администратор отбирает файлы в архив таким образом,
что в него будут сохранены файлы наибольшего возможного количества пользователей.
По заданной информации об объёме файлов пользователей и
свободном объёме на архивном диске определите максимально возможный суммарный объём файлов в архиве,
а также количество файлов, которые ни при каких условиях не могут попасть в архив.

Входные данные.
В первой строке входного файла находятся два числа:
S – размер свободного места на диске (натуральное число, не превышающее 10 000) и
N – количество пользователей (натуральное число, не превышающее 1000).
В следующих N строках находятся значения объёмов файлов каждого пользователя
(все числа натуральные, не превышающие 100), каждое в отдельной строке.
Запишите в ответе два числа: сначала максимально возможный суммарный объём файлов в архиве,
затем количество файлов, которые ни при каких условиях не могут попасть в архив, при условии,
что сохранены файлы максимально возможного числа пользователей.

Пример организации исходных данных во входном файле:
100 7
10
44
66
90
65
47
34
При таких исходных данных в архив можно записать файлы максимум 3 пользователей.
При этом максимально возможная сумма будет из файлов размером 10, 34, 47.
А файлы размером 65, 66, 90 не смогут попасть в архив ни при каких условиях.
Ответ к приведённому примеру входных данных
91 3

7100 220
"""
document = open('26.txt')
a = document.readlines()
s = int(a[0].split()[0])
n = int(a[0].split()[1])
del a[0]
a = sorted(list(map(int, a)))

total = 0

for i in range(n):
    if total + a[i] > s:
        break
    total += a[i]

print(total, len(a[i:]))
