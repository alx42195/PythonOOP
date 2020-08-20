# Дополнительное задание
# Задание
# Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список
# автомобилей, доступных для продажи, и функцию продажи заданного автомобиля.

class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f"Car: {self.model}, Year: {self.year}, Color: {self.color}"

class Car_showroom:
    available_cars = []

# Хороший пример, если не добавить статический декоратор, и не убрать self,
# то будет выдавать ошибку, что не хватает аргумента self
    @staticmethod
    def car_list():
        return [(item.model, item.year, item.color) for item in Car_showroom.available_cars]

    def adding_car(self, *object_car):
        for car in object_car:
            self.available_cars.append(car)
            print(f"{car} -- added")

    def selling_car(self, selected_model):
        self.selected_model = selected_model
        for item in Car_showroom.available_cars:
            if item.model == self.selected_model:
                print(f"{item} -- sold")
                return self.available_cars.remove(item)

    def __str__(self):
        return f"{[(item.model, item.year, item.color) for item in Car_showroom.available_cars]}"

obj1 = Car("Tesla",2020,"red")
obj2 = Car("BMW", 2010, "black")
obj3 = Car("Ford", 2015, "white")
obj4 = Car("Mercedes", 2019, "grey")
selected_cars = obj1, obj2, obj3, obj4

showroom1 = Car_showroom()

showroom1.adding_car(*selected_cars)
print()
print(f"Showroom cars: {showroom1.car_list()}")
print()
showroom1.selling_car("Tesla")
print()
print(showroom1.car_list())
print()
showroom1.selling_car("Ford")
print()
print(showroom1.car_list())
print()
print(obj4)
print()
print(showroom1)






