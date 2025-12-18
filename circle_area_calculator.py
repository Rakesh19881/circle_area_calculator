import math as m
r = int(input(("Enter Radius: ")))


circle = round(m.pi * r * r, 2)
print("Area of circular garden", circle)


circumference = round(2 * m.pi * r, 2)
f = 21.70
n = circumference * f
print("The fencing cost will be: ₹ ", n)