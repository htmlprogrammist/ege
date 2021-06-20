"""
Задание 26 (№1232).
Системный администратор раз в неделю создаёт архив пользовательских файлов. Однако объём диска, куда он помещает архив,
может быть меньше, чем суммарный объём архивируемых файлов. Известно, какой объём занимает файл каждого пользователя.
По заданной информации об объёме файлов пользователей и свободном объёме на архивном диске определите
максимальное число пользователей, чьи файлы можно сохранить в архиве, а также максимальный размер имеющегося файла,
который может быть сохранён в архиве, при условии, что сохранены файлы максимально возможного числа пользователей.

Входные данные.
В первой строке входного файла находятся два числа:
S – размер свободного места на диске (натуральное число, не превышающее 10 000) и
N – количество пользователей (натуральное число, не превышающее 1000).
В следующих N строках находятся значения объёмов файлов каждого пользователя
(все числа натуральные, не превышающие 100), каждое в отдельной строке.
Запишите в ответе два числа: сначала наибольшее число пользователей, чьи файлы могут быть помещены в архив,
затем максимальный размер имеющегося файла, который может быть сохранён в архиве, при условии,
что сохранены файлы максимально возможного числа пользователей.
"""
f = open('26.txt')
string = f.readline()
s = int(string.split()[0])
n = int(string.split()[1])
a = []
for _ in range(n):
    a.append(int(f.readline()))
a.sort()
total = 0

for i in range(n):
    if total + a[i] > s:
        break
    total += a[i]

print(i)
delta = s - total
candidates = [x for x in a if x - a[i] <= delta]
print(max(candidates))