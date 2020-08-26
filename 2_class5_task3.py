"""
Задание 3
Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова
данного текста.

Задание 4
Ознакомьтесь при помощи документации с классами namedtuple и deque модуля collections. -- ОЗНАКОМИЛСЯ
"""

def sequence_request():
    seq = input("Please enter your words > ").split(" ")
    return [_.lower() for _ in seq]

# Первый способ, используем функцию sorted
print(sorted(sequence_request()))

# Второй способ, используем метод sort, но т.к. он возвращает None, то нужно использовать дополнительную строчку кода
unsorted = sequence_request()
unsorted.sort()
print(unsorted)