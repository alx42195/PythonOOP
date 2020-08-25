'''
Дополнительное Задание
Напишите функцию-генератор для получения n первых простых чисел
'''

# def simple_gen():
#     index = 0
#     while True:
#         yield index
#         index += 1
#
# def main():
#     for i in simple_gen():
#         print(i)

def prime_number(number):
    count = 0
    for item in range(1, number + 1):
        if number % item == 0:
            count += 1
    if number < 2 or count > 2:
        return False
    else:
        return True

def prime_generator(n):
    index = 0
    while index <= n:
        if prime_number(index):
            yield index
        index += 1

def main():
    number = 20
    for i in prime_generator(number):
        print(i)

if __name__ == "__main__":
    main()

