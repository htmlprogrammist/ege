"""
Р-35  (демо-2021). Обозначим через ДЕЛ(n,m) утверждение «натуральное число n делится без
остатка на натуральное число m».
Для какого наибольшего натурального числа А формула
¬ДЕЛ(x,А) => (ДЕЛ(x,6) => ¬ДЕЛ(x,9))
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?
"""


def Del(x, D):  # Проверяет делимость первого аргумента x на второй аргумент D (если x делится на D, возвращается True)
    return x % D == 0


def F(x, A):  # Функция по заданию
    return (not Del(x, A)) <= (Del(x, 6) <= (not Del(x, 9)))


# Перебор
for A in range(1, 1000):
    OK = True
    for x in range(1, 1000):
        if not F(x, A):
            OK = False
            break
    if OK:
        print(A)
