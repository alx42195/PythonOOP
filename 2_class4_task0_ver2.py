'''
Дополнительное Задание
Напишите функцию-генератор для получения n первых простых чисел
'''

# number = 20
# print(
#     [
#     item for item in range(1, number + 1)
#         if number % item != 0
#     ]
#         )

def prime_number_generator(number):
    return [item for item in range(1, number + 1) if number % item != 0]

print(prime_number_generator(20))