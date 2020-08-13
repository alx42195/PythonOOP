# Задание 1
# Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе
# издания и жанре. Создайте несколько разных книг. Определите для него операции проверки на
# равенство и неравенство, методы __repr__ и __str__.

class Book:
    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

# Не совсем понятна разница между __repr__ и __str__
    def __repr__(self):
        return f"Book: {self.name}, Author: {self.author}, Year of publish: {self.year}, Genre: {self.genre}"

    def __str__(self):
        return f"Book: {self.name}, Author: {self.author}, Year of publish: {self.year}, Genre: {self.genre}"

    def book_analysis(self):    # при вызове данной функции - ошибка, как же просматривать аттрибуты циклом?
        for self.item in Book:
            print(self.item)

    def compare_to_another_book(self,another_book):  # хотел сделать функцию сравнения книг, но не пойму
        self.another_book = another_book             # как добавить все аттрибуты второго объекта для сравнения

# Функция проверки на идентичность. Не знаю как перебирать циклом в объекте, поэтому влоб проверяю все аттрибуты
def books_compare(book1, book2):
    if book1.name == book2.name and book1.author == book2.author \
            and book1.year == book2.year and book1.genre == book2.genre:
        print("Books are the same")
    else:
        print("Books are different")

book1 = Book("M.Bulgakov", "Dog's Heart", "1938", "Historical Fiction")
print(book1)
print(book1.__str__())
book2 = Book("M.Bulgakov", "Dog's Heart", "2020", "Historical Fiction")  # Различие в годе издания


print(book1 == book2)   # Результат выдает False, подразумеваю, что сравнивает не содержимое, а объекты

print(book1.name == book2.name)
# book2.book_analysis()
books_compare(book1,book2)  # Выдает корректный результат





