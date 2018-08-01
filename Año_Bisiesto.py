#Año bisiesto

x=int(input("Ingresa el año: "))

a = x % 4
b = x % 100
c = x % 400

if c == 0:
    print("Año bisiesto.")

elif a == 0 and b != 0:
    print("Año bisiesto.")

else:
    print("No es bisiesto.")

        
    
