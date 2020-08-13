# Задание 2
# Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать
# нажатия мыши. Опишите класс кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите
# метод нажатия на кнопку.

class Rectangular:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self):
        return f"Rectangular: side a = {self.side_a}, side b = {self.side_b}"

class Graph_object:
    def mouse_click(self):
        return True
# Добавить логику если Истина, то объект меняет цвет и запускает программу пуска ракеты по цели

class Mouse(Graph_object):
    pass
    # def __init__(self):

obj1 = Rectangular(2,3)
print(obj1)

obj2 = Graph_object()
print(obj2.mouse_click())


