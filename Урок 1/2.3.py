import math
a = int(input ("Введиде а"))
b = int(input ("Введиде b"))
c = int(input ("Введиде c"))

D = 0
D = b**2 - 4*a*c
if D < 0:
	print ("Корней нет")
elif D == 0:
	x = -b / (2*a)
	print ("Один корень уровнения х= ", x)
else:
	x1 = (-b + math.sqrt(D)) / (2*a)
	x2 = (-b - math.sqrt(D)) / (2*a)
	print ("Корень x1 = ", x1)
	print ("Корень x2 = ", x2)