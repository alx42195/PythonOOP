"""
Дополнительное задание

Напишите программу, которая вводит с клавиатуры последовательность чисел и выводит её
отсортированной в порядке возрастания.
"""

def sequence_request():
    seq = input("Please enter your numbers separated by space > ").split(" ")
    return [float(_) for _ in seq]

# Первый способ, используем функцию sorted
print(sorted(sequence_request()))

# Второй способ, используем метод sort, но т.к. он возвращает None, то нужно использовать дополнительную строчку кода
unsorted = sequence_request()
unsorted.sort()
print(unsorted)
