"""
Алгоритм получает на вход натуральное число 𝑁>1 и строит по нему новое число 𝑅 следующим образом:
1. Если исходное число кратно 2, оно делится на 2, в противном случае из него вычитается 1.
2. Если полученное на предыдущем шаге число кратно 3, оно делится на 3, в противном случае из него вычитается 1.
3. Если полученное на предыдущем шаге число кратно 7, оно делится на 7, в противном случае из него вычитается 1.
4. Число, полученное на шаге 3, считается результатом работы алгоритма.

Пример. Дано число 𝑁=44. Алгоритм работает следующим образом:
1. Число 44 кратно 2, оно делится на 2, получается 22.
2. Число 22 не кратно 3, из него вычитается 1, получается 21.
3. Число 21 кратно 7, оно делится на 7, получается 3.
4. Результат работы алгоритма 𝑅=3.
Сколько существует различных натуральных чисел 𝑁, при обработке которых получится 𝑅=1?

5
"""
counter = 0

for n in range(1, 2560):
    number = n
    if n % 2 == 0:
        number //= 2
    else:
        number -= 1
    if number % 3 == 0:
        number //= 3
    else:
        number -= 1
    if number % 7 == 0:
        number //= 7
    else:
        number -= 1
    if number == 1:
        counter += 1

print(counter)
