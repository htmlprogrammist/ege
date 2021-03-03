"""
№ 670, Джобс 09.11.2020
Значение арифметического выражения: 5∙36^7 + 6^10 – 36
записали в системе счисления с основанием 6.
Сколько цифр «5» содержится в этой записи?

9
"""
x = 5*36**7 + 6**10 - 36
counter = 0

while x > 0:
    if x % 6 == 5:
        counter += 1
    x //= 6
print(counter)