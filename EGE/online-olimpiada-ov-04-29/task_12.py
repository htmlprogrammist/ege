"""
Дана программа для редактора:
НАЧАЛО
ПОКА НЕ нашлось (00)
заменить (01, 210)
заменить (02, 320)
заменить (03, 3012)
КОНЕЦ ПОКА
КОНЕЦ
Известно, что исходная строка начиналась с нуля и заканчивалась нулём,
а между ними содержала только единицы, двойки и тройки.
После выполнения данной программы получилась строка, содержащая 23 единицы, 48 двоек и 41 тройку.
Сколько цифр было в исходной строке?
"""
for units in range(2, 60):
    for twos in range(2, 60):
        for threes in range(2, 60):
            s = '0' + units * '1' + twos * '2' + threes * '3' + '0'
            while not('00' in s):
                s = s.replace('01', '210', 1)
                s = s.replace('02', '320', 1)
                s = s.replace('03', '3012', 1)
            if s.count('1') == 23 and s.count('2') == 48 and s.count('3') == 41:
                print(units + twos + threes + 2)
# надо ли учитывать 2 нуля, которые в строке изначально?
# "Сколько цифр было в исходной строке?"