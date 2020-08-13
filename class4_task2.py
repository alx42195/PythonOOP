# Задание 2
# Факториалом числа n называется число 㨹ί ᩛ ڵ  ڶ  ڷ    㨹. Создайте программу, которая
# вычисляет факториал введённого пользователем числа.Задание 2
# Факториалом числа n называется число n! = 1*2*3*...*n. Создайте программу, которая
# вычисляет факториал введённого пользователем числа.

try:
    n = int(input("Please enter the factorial > "))
except ValueError:
    print("Oh no, you have entered non valid value, please enter an integer")
else:
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    print(f"Factorial of {n} is {factorial}")

