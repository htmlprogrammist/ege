"""
Задание 7 (№1416).
Автоматическая камера производит растровые изображения размером 3900x2160 пикселей.
Для кодирования цвета каждого пикселя используется одинаковое количество бит,
коды пикселей записываются в файл один за другим без промежутков.
Объём файлов с изображением не может превышать 13 Мбайт без учёта размера заголовка файла.
Какое максимальное количество цветов можно использовать в палитре?
"""
k = 3900 * 2160
volume = 13 * 2 ** 23
i = volume / k  # <= 12.945382716049382 => i = 12
print(2 ** 12)  # 4096
