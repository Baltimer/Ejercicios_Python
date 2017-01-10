# Escribe un programa que nos pida por teclado dos números 
# enteros y que a continuación muestre en pantalla la suma 
# de los dos números solamente si son los dos positivos.
#
# Autor: Luis Cifre
#
# Casos tipo:
#
# numA = 4, numB = 5, suma = 9 ==> numA = -3, numB = 4, no son positivos

numA = int(input("Introduce el primer número: "))
numB = int(input("Introduce el segundo número: "))

if numA >= 0 and numB >= 0:
	print "La suma de los dos números es: ", numA+numB
else:
	print "Alguno de los números no es positivo!"
