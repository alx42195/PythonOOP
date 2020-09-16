"""
Задание 1
Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных
действительных чисел. Создайте ещё один скрипт, который читает числа из файла и выводит на экран их
сумму.
"""

import random
import pickle

def random_float():
    return [random.random() for _ in range(10000)]

with open("random.txt", "w") as file:
    file.write(f"{random_float()}")

with open("random.txt") as file:
    txt = file.read()
    txt_stripped = txt.strip('[]')
    container = txt_stripped.split(", ")
    sum_calculation = sum([float(i) for i in container])

print(sum_calculation)
