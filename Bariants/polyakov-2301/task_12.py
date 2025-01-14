"""
Задание 12
Исполнитель Редактор получает на вход строку цифр и преобразовывает её.
Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки цифр.
1. заменить (v, w)
2. нашлось (v)
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w,
вторая проверяет, встречается ли цепочка v в строке исполнителя Редактор.
Если она встречается, то команда возвращает логическое значение «истина»,
в противном случае возвращает значение «ложь». Дана программа для исполнителя Редактор:
НАЧАЛО
  ПОКА нашлось (21)
    заменить (21, 5)
  КОНЕЦ ПОКА
КОНЕЦ
Исходная строка содержит десять единиц и некоторое количество двоек,
других цифр нет, точный порядок расположения единиц и двоек неизвестен.
После выполнения программы получилась строка с суммой цифр 34.
Какое наименьшее количество двоек могло быть в исходной строке?
"""

for n in range(1, 100):
    result = 0
    s = '1' * 10 + '2' * n

    while '21' in s:
        s = s.replace('21', '5', 1)

    for i in range(len(s)):
        result += int(s[i])

    if result == 34:
        print(n)
        break
