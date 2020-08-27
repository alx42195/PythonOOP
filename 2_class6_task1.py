"""
Задание 1
Даны две строки. Выведите на экран символы, которые есть в обоих строках.
"""

txt_1 = "Happy New Year !"
txt_2 = "Happy Birthday !"

set_1 = set(txt_1)
set_2 = set(txt_2)

print(set_1 & set_2)
