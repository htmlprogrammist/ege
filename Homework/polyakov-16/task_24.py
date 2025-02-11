"""
(№ 2543) (К. Амеличев)
Текстовый файл 24-5.txt содержит последовательность из символов «(»и «)», всего не более 106 символов.
Определите, с какого по счёту символа от начала файла начинается 10000-я пара скобок «()»
(нумерация символов начинается с 1).

40451
"""
document = open('24-5.txt')
a = document.read()
counter = 0
# print(a[0])  => ')' => можно так и вести нумерацию с единицы, не заморачиваясь
for i in range(len(a)):
    if a[i] == '(' and a[i + 1] == ')':
        counter += 1
    if counter == 10000:
        print(i)
# Выводит 40450 и 40451. В другом файле вывело мне вот такую красоту:
# print(a[40449], a[40450], a[40451], a[40452]) => ) ( ) (
# Ну, начинается же с 40450, как по условию надо, а ответ 40451, когда пара скобок уже зафиксирована.
# Видимо, начинается 10000-я пара скобок «()» имеется в виду, что вот дальше уже 10001-я, то есть это начало
# Поэтому надо эту скобку учитывать целиком

