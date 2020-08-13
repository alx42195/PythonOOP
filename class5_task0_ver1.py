# Задание
# Создайте программу, которая состоит из функции, которая принимает три числа и возвращает
# их среднее арифметическое, и главного цикла, спрашивающего у пользователя числа и
# вычисляющего их средние значения при помощи созданной функции.


# Функция преобразования текстового списка в float
def list_convert(list_input):
    for index, item in enumerate(list_input):
        list_input[index] = float(item)

    return list_input

# Функция среднего арифметического
def average_calculation(list_input):
    total = 0
    for item in list_input:
        total += item
        # print(item,total,sep=" | ")
    if len(list_input) == 0:
        print("You have not entered any numbers, please try again!")
    else:
        # print(len(list_input), total)
        return total / len(list_input)


numbers_list=[] # Контейнер для чисел
while True:
    print("  Welcome to Average Function Calculation  ".center(60, "#"))
    numbers_list = input("Enter your numbers separated by space > ").split(" ") # Вводим в одну строку через пробел
    if "done" in numbers_list:  # Ключевое слово "done" - вывод из цикла
        print("Thank you and good bye!")
        break
    else:
        user_input = list_convert(numbers_list)  # Преобразование списка в float
        print(f"Your average is {average_calculation(user_input)} ")


