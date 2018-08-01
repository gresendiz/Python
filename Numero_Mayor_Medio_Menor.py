#leer tres numeros e indicar cual es el mayor, intermedio y menor

a=int(input("Ingresa el valor de A: "))
b=int(input("Ingresa el valor de B: "))
c=int(input("Ingresa el valor de C: "))

if a == b:
	print("A es iguale a B")
if a == c:
	print("A es igual a C")
if b == c:
	print("B es igual a C")


if a > b:
	if b > c:
		print("A es mayor, B es intermedio y C es menor")
	elif a > c:
		print("A es mayor, C es intermedio y B es menor")
	else:
		print("C es mayor, A es intermedio y B es menor")
elif b > c:
	if c > a:
		print("B es mayor, C es intermedio y A es menor")
	else:
		print("B es mayor, A es intermedio y C es menor")
else:
	print("C es mayor, B es intermedio y A es menor")
