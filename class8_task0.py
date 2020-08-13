# Дополнительное задание
# Задание
# Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список
# автомобилей, доступных для продажи, и функцию продажи заданного автомобиля.

class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    @staticmethod
    def advertisement():
        print("Your car is the best car")

mycar = Car("Tesla","2020","red")
print(mycar.model)
print(mycar.advertisement())

class Car_showroom:
    def __init__(self):
        self.available_cars = ["Mercedes", "Ford", "Tesla", "Ferrari", "Bugatti"]

    def selling_a_car(self, model):
        if model in self.available_cars:
            self.available_cars.remove(model)

showroom1 = Car_showroom()
showroom1.selling_a_car("Ford")

print(showroom1.available_cars)




