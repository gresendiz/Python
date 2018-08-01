#Leer numero de 3 sifras e indicar cual de las sifras es la menor

import math

x = int(input("ingresa el numero de 3 sifras: "))

um = math.trunc(x / 1000)
if um > 0:
	print("No es un valor de tres sifras.")

else:
	c = math.trunc(x / 100)

	x = x % 100


	e = x / 10
	d = int(e)

	n = x % 10
	u = int(n)


	if u < d:
		if u < c:
			print(u, " es menor")
		else:
			print(c, " es menor")
	elif d < c:
		print(d, " es menor")
	else:
		print(c, " es menor")
 