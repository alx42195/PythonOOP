# Задание 3
# Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год
# поступления на работу. Конструктор должен генерировать исключение, если заданы неправильные
# данные. Введите список работников с клавиатуры. Выведите всех сотрудников, которые были приняты
# после заданного года.

class Employee:
    _list = []
    def __init__(self, firstname, lastname, department, year):
        self._list.append(self)
        self.firstname = firstname
        self.lastname = lastname
        self.department = department
        self.year = year

        try:
            if not type(self.firstname) == str or not type(self.lastname) == str or not type(self.year) == int:
                raise ValueError("Check whether names are strings and year is integer")
        except ValueError as err:
            print(f"Something went wrong. {err}")

    def __str__(self):
        return f"Employee name: {self.firstname} {self.lastname}, dep: {self.department}, start year: {self.year}"

emp1 = Employee("John", "Smith", "logistics", 2010)
print(type(emp1.firstname), type(emp1.year))
emp2 = Employee("Bob", "Dilan", "logistics", 2012)
emp3 = Employee("Mary", "Rose", "Accounting", 2015)
emp4 = Employee("Lucy", "Black", "Accounting", 2017)
emp5 = Employee("Miko", "Winterspoon", "Marketing", 2008)

check_year = 2012

for e in Employee._list:
    if e.year >= check_year:
        print(e)
