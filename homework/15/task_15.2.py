"""
Р-34.  (С.С. Поляков) Укажите наименьшее целое значение А, при котором выражение
(5k + 6n > 57) ∨ ((k ≤ A) ⋀ (n < A))
истинно для любых целых положительных значений k и n.
"""


def F(k, n, A):
    return (5*k + 6*n > 57) or ((k <= A) and (n < A))


for A in range(1, 1000):
    OK = True
    for k in range(1, 1000):
        for n in range(1, 1000):
            if not F(k, n, A):
                OK = False
                break
    if OK:
        print(A)
        break  # BREAK НЕОБХОДИМ! Нам нужно искать наименьшее, поэтому break позволит получить лишь одно значение
        # Если убрать break, то значения А поползут ещё дальше
