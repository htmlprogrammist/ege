"""
Логическая функция 𝐹 задаётся выражением: (y→z)/\¬((y\/𝑤)→(z/\𝑥)).
Дан частично заполненный фрагмент,
содержащий неповторяющиеся строки таблицы истинности функции 𝐹
Определите, какому столбцу таблицы истинности соответствует каждая из
переменных 𝑤,𝑥,𝑦,𝑧
"""
print('x y z w F')
k = 0, 1
for x in k:
    for y in k:
        for w in k:
            for z in k:
                F = (y <= z) and not((y or w) <= (z and x))
                if F:
                    print(x, y, z, w, F)
