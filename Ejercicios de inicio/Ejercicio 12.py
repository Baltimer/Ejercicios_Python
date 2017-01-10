# Escribe un programa que pida por teclado dos números y que calcule 
# y muestre su suma solamente si:
# a) los dos son pares 
# b) el primero es menor que cincuenta 
# c) el segundo está dentro del intervalo cerrado 100-500. 
#
# Autor: Luis Cifre
#
# Casos tipo:
#
# numA = 2, numB = 4, NO
# numA = 2, numB = 5, NO
# numA = 2, numB = 200, OK

numA = int(input("Introduce el primer número :"))
numB = int(input("Introduce el segundo número :"))

if numA%2 == 0 and numB%2 == 0:
	if numA <50:
		if numB>=100 and numB<=500:
			print "La suma de los dos números es: ", numA + numB
		else:
			print "El segundo número no está comprendido entre 100 y 500."
	else:
		print "El primer número es 50 o más"
else:
	print "Alguno de los dos números no es par."