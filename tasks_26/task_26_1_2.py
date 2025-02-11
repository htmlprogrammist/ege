# Автор: А.Н. Носкин
""" Идея:
считываем все объемы в массив, сортируем их по возрастанию.
На каждом шаге суммируем очередной объем, пока не достигнем
заданного объема диска и подсчитываем количество пользователей.
Если сумма объемов совпала, то задача решена, иначе нужно
убрать последний суммированный объем и прибавить следующий за ним объем.
Так выполнять пока не достигним нужного объема
"""
with open("26-1.txt") as f:
    s, n = map(int, f.readline().split())
    a = []
    for i in range(n):
        a.append(int(f.readline()))

    a.sort()
    summa = 0
    k = 0
    Max = 0
    for i in range(n):
        if s >= summa + a[i]:
            summa += a[i]
            k += 1
            Max = a[i]
        else:
            summa = summa - Max + a[i]
            if s >= summa:
                Max = a[i]

    print(k, Max)
