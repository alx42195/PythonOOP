# Создайте иерархию классов транспортных средств. В общем классе опишите общие для всех
# транспортных средств поля, в наследниках – специфичные для них. Создайте несколько экземпляров.
# Выведите информацию о каждом транспортном средстве.

class Vehicle:
    def __init__(self, transport_method, engine, usage, seats):
        self.transport_method = transport_method
        self.engine = engine
        self.usage = usage
        self.seats = seats

# Создание декоратора property и примеры ниже для проверки работоспособности
    @property
    def description(self):
        return f"{self.transport_method} vehicle for {self.usage} usage"

    @description.setter
    def description(self, sentence):
        _method, and1, and2, _usage, and3 = sentence.split(" ")
        self.transport_method = _method
        self.usage = _usage

    def __str__(self):
        return f" This is {self.transport_method} vehicle with {self.engine} type of engine for {self.usage} usage \
        with {self.seats} seats"

    @staticmethod
    def beeping():
        print("Beep..! Beep!")


class Car(Vehicle):
    def __init__(self, transport_method, engine, usage, seats, body_type, color):
        super().__init__(transport_method, engine, usage, seats)
        self.body_type = body_type
        self.color = color

    def __str__(self):
        return f" This is {self.transport_method} vehicle with {self.engine} type of engine for {self.usage} usage \
                with {self.seats} seats. It has {self.body_type} body and {self.color} color"

class Sport_car(Car):
    def __init__(self, transport_method, engine, usage, seats, body_type, color, upgrades):
        # super(Sport_car, self).__init__(transport_method, engine, usage, seats, body_type, color)
        super().__init__(transport_method, engine, usage, seats, body_type, color)
        self.upgrades = upgrades

    def __str__(self):
        return f" This is sport {self.transport_method} vehicle with {self.engine} type of engine for {self.usage} usage \
                   with {self.seats} seats. It has {self.body_type} body and {self.color} color. \
                   As a sport car is has {self.upgrades}."

# Сделать классовые методы для разных видов спортивных машин из upgrages

class Aircraft(Vehicle):
    flag = "UA"
    def __init__(self,transport_method, engine, usage, seats, jet_type, engines_number):
        super().__init__(transport_method, engine, usage, seats)
        self.jet_type = jet_type
        self.engines_number = engines_number

    def __str__(self):
        return f" This is {self.jet_type}  with {self.engines_number} engines for {self.usage} usage \
        with {self.seats} seats"

# Дописать
    @classmethod
    def from_vehicle(cls, vehicle):
        pass
        return cls(transport_method, engine, usage, seats, jet_type, engines_number)

class Ship(Vehicle):
    pass

class Amfibia(Vehicle,Aircraft,Ship):
    pass


car1 = Vehicle("road", "diesel", "civil", 4)
car2 = Car("road", "diesel", "civil", 4, "sedan", "black")
car3 = Sport_car("road", "petrol", "civil", 2, "coupe", "red", "enforced engine")
print(car1, car2, car3, sep="\n")
car1.beeping()
print()
car4 = Vehicle("road", "diesel", "military", 8)
print(car4.description)
print(car3.description)
print()
car4.transport_method = "sea"
print(car4.description)
print(car3.description)
print()
car3.description = "air vehicle for civil usage"
print(car4.description)
print(car3.description)
print()
vehicle5 = Aircraft("air", "gasoline", "military", 12, "helicopter", 2)
print(vehicle5)
print()
vehicle5.from_vehicle("small jet",2)
print(vehicle5)

