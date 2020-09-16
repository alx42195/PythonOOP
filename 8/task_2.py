"""
Задание 1
Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных
действительных чисел. Создайте ещё один скрипт, который читает числа из файла и выводит на экран их
сумму.
Задание 2
Модифицируйте решение предыдущего задания так, чтобы оно работало не с текстовыми, а бинарными
файлами.
"""

import random
from array import array
import os.path


numbers = [random.random() for _ in range(100)]
num_array = array('d', numbers)

with open("random.bin", "wb") as file:
    file.write(num_array)

filesize = os.path.getsize("random.bin")
item_len = array("d").itemsize
read_array = ('d', (0 for _ in range(filesize // item_len)))

with open("random.bin", "rb") as rbfile:
    rbfile.readinto(read_array)

print(read_array)