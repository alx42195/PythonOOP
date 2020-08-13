# Задание 2
# Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте
# так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.

class Book:
    def __init__(self, name, review):
        self.name = name
        self.review = review

    def __repr__(self):
        return f"Book: {self.name}, Review: {self.review}"

book1 = Book("White Fang", "Very interesting book")
print(book1)






