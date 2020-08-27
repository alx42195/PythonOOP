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