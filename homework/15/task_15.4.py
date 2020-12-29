"""
Р-25. Введём выражение M & K, обозначающее поразрядную конъюнкцию M и K
(логическое «И» между соответствующими битами двоичной записи).
Определите наименьшее натуральное число a, такое что выражение
(x & 125 != 1) ∨ ((x & 34 = 2) => (x & a = 0))
тождественно истинно (то есть принимает значение 1 при любом натуральном значении переменной x)?
"""


def F(x, A):
    return (x & 125 != 1) or ((x & 34 == 2) <= (x & A == 0))


for A in range(1, 1000):
    allowance = True
    for x in range(1, 1000):
        if not F(x, A):
            allowance = False
            break
    if allowance:
        print(A)
        break
