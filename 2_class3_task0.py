# Дополнительное задание
# Задание
# Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
# если пользователь введёт определённое значение, и перехватите это исключение при вызове функции.

class MyException:
    def division_by_zero(self):
        return f"Division by zero"
x = 5
y = 0
try:
    result = x/y
    if y == 0:
        err = MyException()
        raise err.division_by_zero()
except Exception as e:
    print(f"We have an error - {e}")
finally:
    print("Exceptions handling".center(70,"*"))

