import math
a1 = int(input("Первая координата точки A: "))
a2 = int(input("Вторая координата точки A: "))
b1 = int(input("Первая координата точки B: "))
b2 = int(input("Вторая координата точки B: "))
print(round((math.sqrt((b1 - a1)**2 + (b2 - a2)**2)), 2))
