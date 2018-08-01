#Leer una cantidad determinada de numeros y obtener el promedio

suma = 0

n = int(input("Numero de datos que quiere ingresar: "))

for i in range(n):
    num = int(input("Ingresa datos: "))
    suma = suma + num

p = suma / n
print("El promedio es: ", p)
