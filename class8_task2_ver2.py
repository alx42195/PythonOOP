# Задание 2
# Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте
# так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.

class Book:
    def __init__(self, name):
        self.name = name
        self.review_list = []

    def review_add(self, review):
        self.review = review
        self.review_list.append(self.review)

# Как можно более умно вывести через return список без вызова цикла?  Хотел сделать print(*list),
#     но выдает ошибку, как неподдерживаемый тип в __str__
    def __repr__(self):
        print(f"Book name is {self.name}, Here are the reviews:")
        for item in self.review_list:
            print(item)


book1 = Book("White Fang")
book1.review_add("Very good book")
book1.review_add("Too boring for me!")
book1.review_add("Not bad!")

print(book1.__dict__)

print(book1)
# Результат выводит, но в конце пишет TypeError:

# Traceback (most recent call last):
#   File "C:/Users/Alx/Desktop/class8_task2_ver2.py", line 26, in <module>
#     print(book1)
# TypeError: __str__ returned non-string (type NoneType)
#
# Process finished with exit code 1





