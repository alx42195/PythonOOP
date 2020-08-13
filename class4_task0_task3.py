# Дополнительное задание
# Создайте программу, которая рисует на экране прямоугольник из звёздочек заданной
# пользователем ширины и высоты.

# Задание 3
# Используя вложенные циклы и функции print(‘*’, end=’’), print(‘ ‘, end=’’) и print() выведите на
# экран прямоугольный треугольник.

hight=int(input("Enter rectangular hight > "))
width=int(input("Enter rectangular width > "))

for i in range(hight):
    for j in range(width):
        if i==0 or j==0 or i==hight-1 or j==width-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
