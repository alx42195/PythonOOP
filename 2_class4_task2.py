'''
Задание 2
Перепишите решение первого задания с помощью генератора.
'''

def my_reversed(seq):
    return [item for item in seq[::-1]]

def my_reversed_2(seq):
    index = len(seq)-1
    while index > 0:
        yield seq[index]
        index -= 1


my_seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_reversed(my_seq))
print()
for _ in my_reversed_2(my_seq):
    print(_)
