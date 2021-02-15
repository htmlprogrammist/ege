"""
Задание 12 (№95).
Дана программа для исполнителя Редактор:
НАЧАЛО
ПОКА нашлось (4444) ИЛИ нашлось (777)
 ЕСЛИ нашлось (4444)
  ТО заменить (4444, 77)
  ИНАЧЕ заменить (777, 4)
 КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой выше программы к строке,
состоящей из 204 идущих подряд цифр 4? В ответе запишите полученную строку.
"""
s = 204 * '4'
while '4444' in s or '777' in s:
    if '4444' in s:
        s = s.replace('4444', '77', 1)
    else:
        s = s.replace('777', '4', 1)
print(s)