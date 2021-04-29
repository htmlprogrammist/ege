"""
Найдите все натуральные числа, 𝑁, принадлежащие отрезку [400 000 000; 600 000 000],
которые можно представить в виде 𝑁 = 2**m * 3**n, где 𝑚 – чётное число, 𝑛 – нечётное число.
В ответе запишите все найденные числа в порядке возрастания.
"""
# import math

for n in range(400000000, 600000000 + 1):
    counter_even = 0
    counter_odd = 0
    number = n
    while number % 2 == 0:
        number //= 2  # отбрасываю все степени двойки
        counter_even += 1
    # math.log(number, 3)
    # там есть число-нюанс, которое при логарифме выводит 12.9999999999998, хотя подходит (3 ** 13)
    # https://colab.research.google.com/drive/1ZuBfkGIYGs6CzR7LG9gnwy8eBR3gL4XR?authuser=2#scrollTo=5vjZqcu57RiL&line=1&uniqifier=1
    while number % 3 == 0:
        number //= 3  # отбрасываю все степени двойки
        counter_odd += 1
    if counter_odd % 2 != 0 and counter_even % 2 == 0 and counter_even != 0:
        if 2 ** counter_even * 3 ** counter_odd == n:
            print(n)
