'''
Задание 1
Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог
reversed).
'''

class My_Iterator:
    """ Пробуем простой итератор """

    def __init__(self, example):
        self.example = example
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.example) - 1:
            raise StopIteration

        item_value = self.example[self.index]
        self.index += 1

        return item_value

class My_IteratorReversed:
    """ Теперь обратный итератор """

    def __init__(self, example):
        self.example = example
        self.index = len(example) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        item_value = self.example[self.index]
        self.index -= 1

        return item_value



test = [1,2,3,5,6,7,8]
for _ in My_Iterator(test):
    print(_)

print(" Reversed ".center(50,"*"))

for _ in My_IteratorReversed(test):
    print(_)

