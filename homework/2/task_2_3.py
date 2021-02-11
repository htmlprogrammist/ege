"""
Задание 2 (№739).
Логическая функция F задаётся выражением (z ∨ y) → (x ≡ z).
На рисунке приведён частично заполненный фрагмент таблицы истинности функции F,
содержащий неповторяющиеся строки. Определите, какому столбцу таблицы истинности
функции F соответствует каждая из переменных x, y, z.
      F
0   0 0
    0 0
"""
r = 0, 1
print('x y z F')
for x in r:
    for y in r:
        for z in r:
            F = (z or y) <= (x == z)
            if not F:
                print(x, y, z, F)
