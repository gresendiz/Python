#leer dos numeros entre -20 y 20 y determinar si son de signos iguales

x=int(input("Ingresa el primero valor: "))
y=int(input("Ingresa el segundo valor: "))

z=x*y

if z == 0:
	print("Uno de los dos valores es igual a cero")
elif z > 0:
	print("Signo iguales")
else:
	print("Sginos opuestos")