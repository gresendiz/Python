#calcular area de un triangulo

b = float(input("Ingresa el valor de base: ")) 
a = float(input("Ingresa el valor de altura: "))

z = (b * a) / 2

w = "{0:.2f}".format(z)

print("El valor de area es:", w)