#numero romanosdel 1 al 3999

# -*- coding: utf-8 -*-

import math

numero=int(input("Ingresa el valor a convertir: "))

if numero<=0:
	print("No existe ningun simbolo para representar el ", numero)

#Unidad de millar
um = math.trunc(numero / 1000)

for i in range (um):
	print("M")

#Centena	
numero = math.trunc(numero % 1000)
c = math.trunc (numero / 100)

if c==9:
	print("CM")

elif c==4: 
	print("CD")
	f=c-5
	for i in range(f):
		print ("C")

elif c==5:
	print ("D")

elif c>=5:
	print ("D")
	f=c-5
	for i in range(f):
		print ("C")
else:
	for i in range(c):
		print ("C")

#Decenas
numero = math.trunc(numero % 100)
d = math.trunc(numero/10)

if d==9:
	print("XC")

elif d==4: 
	print("LX")
	f=d-5
	for i in range(f):
		print ("X")

elif d==5:
	print ("L")

elif d>=5:
	print ("L")
	f=d-5
	for i in range(f):
		print ("X")

else:
	for i in range(d):
		print ("X")

#Unidad
numero = math.trunc(numero % 10)
u = math.trunc(numero)

if u==9:
	print("IX")

elif u==4: 
	print("IV")
	f=u-5
	for i in range(f):
		print ("I")

elif u==5:
	print ("V")

elif u>=5:
	print ("V")
	f=u-5
	for i in range(f):
		print ("I")

else:
	for i in range(u):
		print ("I")