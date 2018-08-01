#Funciones

#Escibir el cubo de un numero

def cubo(x):
	y= x * x * x
	return y

a = int(input("Ingresa el valor: "))
b = cubo(a)

print("el cubo es: ", b)