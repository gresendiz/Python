#Ecuacion cuadratica

import math

a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))
c = int(input("Ingresa el valor de c: "))

x = b * b
y = 4 * a * c

D = x - y

if D < 0:
	print("No hay solucion")
elif D == 0:
	x = -b / (2 * a)
	print ("Raiz doble en x = ", x)
else:
	x1 = (-b + math.sqrt(D)) /2
	x2 = (-b - math.sqrt(D)) /2
	y1 = round(x1,2)
	y2 = round(x2,2)
	print("Una raiz en x1 = ", y1, "y la otra raiz en x2 = ", y2)