# Задание 2
# Создайте две функции, вычисляющие значения определённых алгебраических выражений.
# Выведите на экран таблицу значений этих функций от -5 до 5 с шагом 0.5.

def quadratic_function(x):
    return x**2


def cubic_function(x):
    return x**3


n = -5
while n <= 5:
    print(f"{n : 5} | {quadratic_function(n) : 8} | {cubic_function(n): 8}")
    n += .5

#############    Вопрос Леониду   ########################
# взял двоеточия из Вашего примера в online уроке.
# Какие правила форматирования через двоеточие? Есть какие-нибудь ссылки для чтения?