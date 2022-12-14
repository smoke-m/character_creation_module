from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Возвращаем Ответ."""
    if your_number <= 0:
        return
    elif your_number > 0:
        sqrt_number = calculate_square_root(your_number)
        return print(f'Мы вычислили квадратный корень из введённого вами '
                     f'числа. Это будет: {sqrt_number}')


calc(25.5)
