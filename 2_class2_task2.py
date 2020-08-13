# Задание 2
# Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать
# нажатия мыши. Опишите класс кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите
# метод нажатия на кнопку.
#
# Замена // графический объект - это наземная цель на экране монитора = Target_on_the_ground
# Замена // Вместо прямоугольника - BattleField - зона боевых действий

x1 = 0
x2 = 0
y1 = 0
y2 = 0
target_status = False
weapon = None
missile_status = False

class BattleField:

    def __init__(self, user_x1, user_x2, user_y1, user_y2):
        global x1
        global x2
        global y1
        global y2
        self.user_x1 = user_x1
        self.user_x2 = user_x2
        self.user_y1 = user_y1
        self.user_y2 = user_y2
        x1 = self.user_x1
        x2 = self.user_x2
        y1 = self.user_y1
        y2 = self.user_y2

    def __str__(self):
        return f"Balltefield area is from {self.user_x1} to {self.user_x2} and from {self.user_y1} to {self.user_y2}"

# Следующий объект - цель на земле. Обработка события, если указатель мыши над целью, то возврат значения Истина и
# разрешение на выбор ракеты для нанесения удара
class Target_on_the_ground:

    def __init__(self, target_x, target_y, target_engage=False):
        self.target_x = target_x
        self.target_y = target_y
        self.target_engage = target_engage

    def __str__(self):
        f"Target is at x={self.target_x} and at y={self.target_y}, target status is: {self.target_engage}"


    missile_1 = "HellFire"
    missile_2 = "Griffin"
    missile_3 = "Maverick"

# Обработка события, мышка над целью, если да - то Истина. Также проверка входит ли объект в зону боевых действий,
# если нет, то возврат Ложь и сообщения
    def mouse_hover(self):
        global x1
        global x2
        global y1
        global y2

        if x1 <= self.target_x <= x2 and y1 <= self.target_y <= y2:
            return True
        else:
            print("You are outside of the war area. You are not allowed to engage peaceful targets!")
            return False

# Если мыка над целью истина, то подготовка ракеты к запуску, выбор какой ракеты. Возврат - захват цели Истина.
# Если мышка не над целью, то Ложь

    def missile_engage(self):
        global target_status
        global weapon
        if self.mouse_hover():
            weapon = input(f"Select missile type: {self.missile_1} , {self.missile_2}, {self.missile_3} > ")
            self.target_engage = True
            target_status = self.target_engage
            return target_status


class MissileLaunch_by_Mouse:
    def __init__(self, left_button_click_status=False, right_button_click_status=False):
        self.left_button_click_status = left_button_click_status
        self.right_button_click_status = right_button_click_status

    def left_button_click(self):
        global target_status
        if target_status:
            self.left_button_click_status = True
            return self.left_button_click_status
        else:
            print("Target is not engaged. Please select the target and weapon!")

    def missile_launch(self):
        global weapon
        global missile_status
        if self.left_button_click_status:
            missile_status = True
            return f"{weapon} has been launched, the target is destroyed!"
        else:
            return f"Missile has not been launched"

    def __str__(self):
        if missile_status:
            return f"{weapon} has been launched, the target is destroyed!"
        else:
            return f"Mission aborted!"

# Проверка работоспособности объекта класса BattleField  ---> (+)
print()
print("  War area object creation  ".center(70,"*"))
field_1 = BattleField(1,10,1,20)
print(field_1)
print(type(field_1.user_x1), type(field_1.user_y1))
print(x1,x2,y1,y2)
print()


# Проверка работоспособности объекта класса Target_on_the_ground  ---> (+)
      # Если выбранный объект вне зоны боевых действий
print("  Outside war zone  ".center(70,"*"))
target_1 = Target_on_the_ground(100,500)
# print(target_1)
print(target_1.target_x, target_1.target_y, target_1.target_engage)
print(type(target_1.target_x))
print()

# Проверка работоспособности объекта класса Target_on_the_ground  ---> (+)
      # Если выбранный объект внутри зоны боевых действий
print("  Within war zone  ".center(70,"*"))
target_1 = Target_on_the_ground(3,5)
# print(target_1)
print(target_1.target_x, target_1.target_y, target_1.target_engage)
print(type(target_1.target_x))
print()

# Проверка метода mouse_hover объекта класса Target_on_the_ground  ---> (+)
print("  Mouse hoover test  ".center(70,"*"))
target_1.mouse_hover()
print(target_1.mouse_hover())

# Проверка метода missile_engage объекта класса Target_on_the_ground  ---> (+)
print("  Missile engage test  ".center(70,"*"))
target_1.missile_engage()
print(f"Chosen weapon = {weapon}")
print(f"Target engage status = {target_status}")
print()

# Проверка работоспособности объекта класса MissileLaunch_by_Mouse - создание объекта action   ---> (+)
print("  object action  ".center(70,"*"))
action1 = MissileLaunch_by_Mouse()
print(action1)
print(f"Left button > {action1.left_button_click_status} | Right button > {action1.right_button_click_status}")
print()

# Проверка работоспособности метода нажатия на кнопку мышки класса MissileLaunch_by_Mouse   ---> (+)
print("  Mouse click test  ".center(70,"*"))
action1.left_button_click()
print(f"Left button pressed? > {action1.left_button_click_status}")
print()

# Проверка работоспособности метода запуска ракеты класса MissileLaunch_by_Mouse   ---> (+)
print("  Missile Launch Test  ".center(70,"*"))
action1.missile_launch()
print(action1.missile_launch())
print(f"Missile status > {missile_status}")


# Вопросы
# Почему при выводе print(target_1) выводится ошибка __str__  NonType объект (строки кода 42-43)
#
#
# Вопросы
# Что думаете по поводу использдования глобальных переменных в коде для передачи статусов объектов?
# Так используетя на практике? Или есть более умное решение?
#
