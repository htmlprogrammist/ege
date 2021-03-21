"""
НАЧАЛО
ПОКА нашлось (01) ИЛИ нашлось (02) ИЛИ нашлось (03)
заменить (01, 2302)
заменить (02, 10)
заменить (03, 201)
КОНЕЦ ПОКА
КОНЕЦ

Известно, что исходная строка начиналась с нуля,
а далее содержала только единицы, двойки и тройки.
После выполнения данной программы получилась строка,
содержащая 50 единиц, 12 двоек и 7 троек.
Сколько единиц было в исходной строке?
"""
for units in range(2, 100):
    for deuce in range(2, 100):
        for troika in range(2, 100):
            s = '0' + '1' * units + '2' * deuce + '3' * troika
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '2302', 1)
                s = s.replace('02', '10', 1)
                s = s.replace('03', '201', 1)
            if s.count('1') == 50 and s.count('2') == 12 and s.count('3') == 7:
                print(units)
