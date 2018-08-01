#escribir numero del 1 al 100 y casa 5 bajar de renglon

for i in range(100):
	a = i % 5
	if a == 0:
		print('\n')
	print(i)