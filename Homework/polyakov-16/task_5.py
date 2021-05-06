"""
(№ 1773) На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1. Строится двоичная запись числа N.
2. К этой записи дописывается (дублируется) последняя цифра.
3. Затем справа дописывается бит чётности: 0, если в двоичном коде полученного числа чётное число единиц,
и 1, если нечётное.
4. К полученному результату дописывается ещё один бит чётности.
Полученная таким образом запись (в ней на три разряда больше, чем в записи исходного числа N)
является двоичной записью искомого числа R.
Укажите минимальное число N, после обработки которого автомат получает число, большее 130.

17
"""
for n in range(10, 300):
    binary = bin(n)[2:]  # 1.
    binary += binary[-1]  # 2.
    if binary.count('1') % 2 == 0:  # 3.
        binary += '0'
    else:
        binary += '1'
    if binary.count('1') % 2 == 0:  # 4.
        binary += '0'
    else:
        binary += '1'
    R = int(binary, 2)
    if R > 130:
        print(n)
        break