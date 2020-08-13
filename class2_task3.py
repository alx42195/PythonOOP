# Задание 3
# Напишите программу, которая решает квадратное уравнение по формулам.
# Значения a, b и c вводятся с клавиатуры. Для извлечения корня используйте
# оператор возведения в степень, а не функцию math.sqrt, чтобы получить комплексные числа в
# случае, если подкоренное выражение отрицательно.

print("Let's solve quadratic equation!")
a=float(input("Please enter coefficient A > "))
b=float(input("Please enter coefficient B > "))
c=float(input("Please enter coefficient C > "))
print(f"Here is your equation: {a}x^2+{b}x+{c}=0\nLet's solve it!\n\n")

# Finding discriminant
D=b**2-4*a*c
print(f"D={D}")

# Finding x1,2
x1=(-b+(pow(D,(1/2))))/(2*a)
x2=(-b-(pow(D,(1/2))))/(2*a)

if D>0:
    print(f"Here we go! x1={x1} and x2={x2}")
else:
    print(f"Here we go! Since you had Discriminant <0,\nyou have answers as complex numbers:\nx1={x1} and x2={x2}")


