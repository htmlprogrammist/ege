"""
Задание 12 (№1292).
Исполнитель Редактор получает на вход строку цифр и преобразовывает её.
Какая строка получится в результате применения приведённой ниже программы к строке,
состоящей из 81 идущей подряд цифры 1? В ответе запишите полученную строку.
"""
s = '1' * 81

while '1111' in s or '88888' in s:
    if '1111' in s:
        s = s.replace('1111', '888', 1)
    else:
        s = s.replace('88888', '888', 1)

print(s)
