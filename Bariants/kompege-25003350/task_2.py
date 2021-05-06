"""
Задание 2 (№419).
Логическая функция F задаётся выражением (a → d) ∧ ¬ (b → c)
На рисунке приведён фрагмент таблицы истинности функции F,
содержащий все наборы аргументов, при которых функция F истинна.
Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных a, b, c, d.
"""
k = 0, 1
print('a b c d F')
for a in k:
    for b in k:
        for c in k:
            for d in k:
                F = (a <= d) and not(b <= c)
                if F:
                    print(a, b, c, d)