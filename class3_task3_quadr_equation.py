# Задание 3
# Напишите программу, которая решает квадратное уравнение по формулам.
# Значения a, b и c вводятся с клавиатуры. Для извлечения корня используйте
# оператор возведения в степень, а не функцию math.sqrt, чтобы получить комплексные числа в
# случае, если подкоренное выражение отрицательно.
coefficients=[]

print("Let's solve quadratic equation!")

# asking user to enter arguments for the equation within 1 input
# arguments should be split by space
coefficients=input("Please enter 3 coefficients via space > ").split(" ")

# looping through coefficient list to covert string values into float type
for index,item in enumerate(coefficients):
    coefficients[index]=float(item)

# assigning list values to separate variables, to simplify readability of the code
# e.g. instead of using coefficients[0], coefficient[1], etc, it is easier to use a,b,c
[a,b,c]=coefficients

# showing the equation view to the user
print(f"Here is your equation: {a}x^2+{b}x+{c}=0\nLet's solve it!\n\n")

# Finding discriminant
D=b**2-4*a*c
print(f"D={D}")

# Finding x0 (when D=0) and x1,2 (when D>0)
x0=-b/(2*a)
x1=(-b+(pow(D,(1/2))))/(2*a)
x2=(-b-(pow(D,(1/2))))/(2*a)

if D>0:
    print(f"Here we go! x1={x1} and x2={x2}")
elif D==0:
    print(f"Since D=0, you have only one solution x={x0}")
else:
    print(f"Since D<0, there is no solution within rational numbers")


