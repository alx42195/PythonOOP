"""
Дополнительное задание

Создайте модуль для получения простых чисел. Импортируйте его из другого модуля. Импортируйте
отдельные его имена.
"""

from prime_number import prime_number as prinum, prime_generator as prigen

def main():
    number = 20
    print(prinum(number))
    for _ in prigen(number):
        print(_)

if __name__ == '__main__':
    main()
