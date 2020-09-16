"""
Задание 1
Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных
действительных чисел. Создайте ещё один скрипт, который читает числа из файла и выводит на экран их
сумму.
"""

import random
from array import array

with open("random.txt", "w") as file:
    for i in range(10000):
        file.write(f"{random.random()}\n")

with open("random.txt") as file:
    sum_calculation = sum([float(line) for line in file.readlines()])

print(sum_calculation)