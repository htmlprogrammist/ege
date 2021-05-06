"""
Задание 5 (№351).
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число следующим образом.
1) Строится двоичная запись числа N.
К этой записи дописываются справа ещё два разряда по следующему правилу:
2) Если число чётное, в конец числа (справа) дописывается 1, в противном случае справа дописывается 0.
3) Предыдущий пункт повторяется для записи с добавленной цифрой.
Например, двоичная запись 1001 числа 9 будет преобразована в 100101.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью числа – результата работы данного алгоритма.
Укажите максимальное число N, для которого результат работы алгоритма будет меньше 171.
В ответе это число запишите в десятичной системе счисления.
"""
mx = 0
# for n in range(42, 43):
for n in range(16, 256):
    binary = bin(n)[2:]
    if n % 2 == 0:
        binary += '1'
    else:
        binary += '0'
    if int(binary, 2) % 2 == 0:
        binary += '1'
    else:
        binary += '0'
    # print(int(binary, 2), binary)
    if int(binary, 2) < 171:
        mx = n
print(mx)