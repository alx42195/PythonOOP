import math
x=float(input("Enter X > "))

if -math.pi<=x<=math.pi:
    y=math.cos(3*x)
else:
    y=x

print(f"Your result is {y}")
