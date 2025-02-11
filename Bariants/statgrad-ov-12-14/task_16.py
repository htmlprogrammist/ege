"""
Обозначим через 𝑎 mod 𝑏 остаток от деления натурального числа 𝑎 на натуральное число 𝑏.
Алгоритм вычисления значения функции 𝐹(𝑛), где 𝑛 – целое неотрицательное число, задан следующими соотношениями:
𝐹(0)=0;
𝐹(𝑛)=𝑛+𝐹(𝑛–3), если 𝑛>0 и при этом 𝑛 mod 3=0;
𝐹(𝑛)=𝑛+𝐹(𝑛 – (𝑛 mod 3)), если 𝑛 mod 3>0.
Чему равно значение функции 𝐹(26)?
"""


def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 3 == 0:
        return n + F(n - 3)
    if n % 3 > 0:
        return n + F(n - (n % 3))


print(F(26))
