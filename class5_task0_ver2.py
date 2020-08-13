# Задание
# Создайте программу, которая состоит из функции, которая принимает три числа и возвращает
# их среднее арифметическое, и главного цикла, спрашивающего у пользователя числа и
# вычисляющего их средние значения при помощи созданной функции.

def give_me_numbers():
    numbers_list = []
    numbers_list = input("Please enter numbers via space > ").split(" ")

    return numbers_list


def list_convert(list_input):
    for index, item in enumerate(list_input):
        list_input[index] = float(item)

    return list_input


def average_calculation(list_input):
    n = 0
    total = 0
    for item in list_input:
        total = total+item
        n += 1

    if n == 0:
        print("You have not entered any numbers, please try again!")
    else:
        return {
                   "total_sum": total,
                   "num_number": n,
                   "average": total/n
        }

user_input=give_me_numbers()
user_input = list_convert(user_input)
result=average_calculation(user_input)
print("Your average is ",result["average"])
print("Your total is ",result["total_sum"])
print("You have entered ",result["num_number"], " numbers", sep="")

#############    Вопрос Леониду   ########################
# В данном примере пытаюсь возвращать из функции несколько результатов
# и потом их использовать в других функциях.
# Мне показалось, что dictionary наиболее для этого подошло,
# т.к. можно присвоить названия результатам, а потом к ним
# обращаться.
# Как на практике реализуются такие вещи?
# Т.е. как выводится несколько значений в функции, и как потом это использовать?


