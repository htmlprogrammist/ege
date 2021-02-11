"""
Задание 2 (№614).
Логическая функция F задаётся выражением
((¬y → w) → (x → z)) → (x → w).
На рисунке приведён частично заполненный фрагмент таблицы истинности функции F,
содержащий неповторяющиеся строки. Определите, какому столбцу таблицы истинности
функции F соответствует каждая из переменных x, y, z, w.
        F
0 0 0   0
0 0     0
0       0
"""
print('x y z w F')
r = 0, 1
for x in r:
    for y in r:
        for z in r:
            for w in r:
                F = ((not y <= w) <= (x <= z)) <= (x <= w)
                if not F:
                    # print(x, y, z, w, F)
                    print(w, y, z, x, F)
