"""
Задание 25 (№1206).
Напишите программу, которая ищет среди целых чисел, превышающих 350300, первые шесть чисел, 
удовлетворяющих условию: сумма всех различных делителей числа, отличных от 1 и самого числа, кратна 13.
В ответе запишите эти шесть пар чисел в порядке возрастания первого числа в паре: число, 
для каждого такого числа частное от деления на 13 суммы его различных делителей (исключая 1 и само число).
Количество строк в таблице для ответа избыточно.

350308 26951
350321 630
350333 138
350345 6198
350347 0
350351 0

NB!
350308 26951
350321 630
350333 138
350345 6198
350355 16172
350367 8984
"""
# NB!
# Алексей Кабанов в комментариях на YouTube:
# Есть важные ответы ФИПИ по двум заданиям (спасибо неравнодушным ребятам!)
# - В 10 задании слова из заголовка УЧИТЫВАЮТСЯ в ответе, насчёт падежей и числа заморачиваться не нужно
# - В 25 задании отсутствие искомых делителей означает НУЛЕВУЮ сумму.
# А значит простые числа с нулевой суммой ДОЛЖНЫ присутствовать в ответе #ужаскошмар.

# ПРЕВЫШАЮЩИХ 350300, поэтому 350301
for i in range(350301, 351000):
    sq = int(i ** 0.5)  # нужно для range для фора с j
    d = set()  # это нужно, чтобы если корень из числа получится достать, то добавится он всё равно только 1 раз
    # Преимущество множества над массивом в этом плане
    # А так, я бы писал "частный случай"
    # if int(i ** 0.5) == i ** 0.5:
    #   d.add(i ** 0.5)
    for j in range(2, sq + 1):
        if i % j == 0:
            d.add(j)
            d.add(i // j)
    # if sum(d) != 0 and sum(d) % 13 == 0:  # Неправильно! Оставил только чтобы побургутить на составителей
    #     print(i, sum(d) // 13)
    if sum(d) % 13 == 0:
        print(i, sum(d) // 13)
# Из всего выведенного многообразия берём только первые 6 чисел - ответ