"""
Задание 14 (№879).
Значение арифметического выражения: 64**150 + 4**300 – 32
записали в системе счисления с основанием 8.
Сколько цифр «7» в этой записи?
"""
x = 64**150 + 4**300 - 32
print(oct(x).count('7'))  # 198
