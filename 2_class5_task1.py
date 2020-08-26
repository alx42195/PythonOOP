"""
Задание 1
Создайте функцию от произвольного количества аргументов, которая вычисляет среднее
арифметическое данных чисел. Вычислите при помощи неё среднее арифметическое двух заданных
чисел и среднее арифметическое чисел из заданного диапазона.

Задание 2
Используя документацию, ознакомьтесь с методами класса str. -- ОЗНАКОМИЛСЯ
"""

def my_average(sequence, first_index=None, second_index=None):
    """
    Функция вычисляет среднее арифметическое, если заданы два числа,
    в противном случае вычисляется среднее арифметическое всей последовательности
    :param sequence: последовательность
    :param first_index: индекс первого числа
    :param second_index: индекс второго числа
    :return:
    """
    if first_index != None and second_index != None:
        return f"Average for specified 2 numbers is {(sequence[first_index] + sequence[second_index]) / 2} \
        and average for the range between these numbers \
        is {sum(sequence[first_index:second_index+1])/len(sequence[first_index:second_index+1])}"
    else:
        return f"Average for the whole sequence is {sum(sequence)/len(sequence)}"

my_numbers = 1, 11, 3, 4, 5

print(my_average(my_numbers, 0, 2))
print(my_average(my_numbers))


