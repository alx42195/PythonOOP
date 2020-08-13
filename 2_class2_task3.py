# Задание 3
# Создайте иерархию классов с использованием множественного наследования. Выведите на экран
# порядок разрешения методов для каждого из классов. Объясните, почему линеаризации данных
# классов выглядят именно так.

class A:
    def __init__(self,value):
        self.value = value

class B(A):
    def test(self):
        pass

class C(B):
    def checking(self):
        pass

class D(C):
    def new_test(self):
        pass

obj_A = A(5)
obj_B = B(6)
obj_C = C(7)
obj_D = D(8)

# print(help(obj_A))
print(help(obj_D))
print(obj_C.__mro__)   # Почему выдает ошибку? Ведь такой же аттрибут существует....