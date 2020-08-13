# Задание 3
# Создайте программу-калькулятор, которая поддерживает четыре операции: сложение,
# вычитание, умножение, деление. Все данные должны вводиться в цикле, пока пользователь не
# укажет, что хочет завершить выполнение программы. Каждая операция должна быть
# реализована в виде отдельной функции. Функция деления должна проверять данные на
# корректность и выдавать сообщение об ошибке в случае попытки деления на ноль.

# Функция преобразования текстового списка в float
def list_convertion(user_list):
    for index, item in enumerate(user_list):
        user_list[index]=float(item)

    return user_list

# Умножение
def multiplication(user_list):
    multnum=1
    for item in user_list:
        multnum*=item

    return multnum

# Деление. Здесь долго мучился, т.к. нужно первое число оставть и делить его на второе, т.е цикл со второго индекса
# пока не нашел в Интернете запись через slice напр.: for i in collection[1:]
def division(user_list):
    divnum=user_list[0]
    for item in user_list[1:]:
        divnum/=item

    return divnum

# Сложение
def adding(user_list):
    sumnum=0
    for item in user_list:
        sumnum+=item

    return sumnum

# Вычитание. Логика та же, что и в делении
def subtraction(user_list):
    subtractnum=user_list[0]
    for item in user_list[1:]:
        subtractnum-=item

    return subtractnum

# Записвываем знаки разрешенных операций в список, для облегчения проверки в будущем через "in'
allowed=["*", "-", "/", "+"]

while True:
    operation = input("Enter operation sign, please (*), (/), (+), (-) > ")
    if operation.lower() == "done":  # Ключевым словом выхода из цикла будет done
        print("Thank you for using the program!")
        break
    elif operation not in allowed: # Возврат к началу цикла, если неподдерживаемый знак операции
        print("Unsupported operation, please try again!")
        continue
    else:
        numbers_list = [] # Контейнер для сбора чисел от пользователя
        numbers_list = input("Enter the numbers separated by space > ").split(" ")
        numbers_list = list_convertion(numbers_list) # Конвертация списка из str в float
        if "*" in operation: # Защита от ввода типа "*" или (*), т.е. проверяем есть ли во всей строке операция
            print(f"Your multiplication result is {multiplication(numbers_list)}")
        elif "-" in operation:
            print(f"Your subtraction result is {subtraction(numbers_list)}")
        elif "+" in operation:
            print(f"Your sum result is {adding(numbers_list)}")
        elif "/" in operation:
            if 0 in numbers_list: # проверка деления на ноль
                print("You have division by zero, please try again!")
                continue
            else:
                print(f"Your division result is {division(numbers_list)}")
        else: # вывод в случае каких-либо иных непредвиденных ошибок ввода
            print("There is an error, please try again!")
            continue





