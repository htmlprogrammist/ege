"""
№ 316, Джобс 28.09.2020
Для уменьшения аварий на центральной дороге в городе X дорожная служба решила выровнять ямы.
Новая яма будет иметь второй по величине объем (в литрах) среди её самой и двух соседних ям.
При этом размеры первой и последней ямы решили не менять.
Ночью перед ремонтом дороги в городе X прошел проливной дождь, поэтому все ямы до краев заполнены водой.
Сколько литров воды выльется обратно на дорогу после проведения ремонта?
Входные данные.
В первой строке входного файла находятся два числа:
N – количество ям на дороге (натуральное число, не превышающее 10 000).
В следующих N строках находятся значения объемов ям (все числа натуральные, не превышающие 25),
каждое в отдельной строке.
Запишите в ответе два числа: количество ям с наименьшим объемом и общий объем воды,
вылившейся из ям обратно на дорогу.

Пример входного файла:
8
10
12
8
6
20
12
16
10
При таких исходных данных после ремонта объем ям будет выглядеть следующим образом 10, 10, 8, 8, 12, 16, 12, 10.
Следовательно в ответе необходимо указать два числа – 2 и 14.

72 17730
"""
document = open("task_26_6_example.txt")
data = document.readlines()
n = int(data[0])
del data[0]
data = sorted(list(map(int, data)))
print(n, data)
