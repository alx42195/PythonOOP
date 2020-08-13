# Задание 1
# Даны числа a и b (a < b). Выведите сумму всех натуральных чисел от a до b (включительно).

a = input("Enter integer a > ")
b = input("Enter integer b > ")

try:
    if not a.isdigit() or not b.isdigit():
        raise ValueError("You have entered non-digit values, please try again!")
    else:
        if a > b:
            raise ValueError("Your A is greater then B, please try again!")
        else:
            a, b = int(a), int(b)
            for number in range(a, b+1):
                print(number)

except ValueError as err:
    print(f"We have an issue. {err}")


