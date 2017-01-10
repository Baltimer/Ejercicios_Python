# Escribe un programa que pida por teclado tres valores de tipo entero, 
# y que calcule si se cumple que la suma de dos de ellos es igual al tercero.
#
# Autor: Luis Cifre
#
# Casos tipo:
#
# numA = 1, numB = 2, numC = 3, numC = numA + numB
# numA = 3, numB = 2, numC = 1, numA = numB + numC
# numA = 1, numB = 3, numC = 2, numB = numA + numC
# numA = 2, numB = 5, numC = 4, No se puede

numA = int(input("Introduce el primer número :"))
numB = int(input("Introduce el segundo número :"))
numC = int(input("Introduce el tercer número :"))

print "Números introducidos: ", numA, "\t", numB, "\t", numC

if numA == numB + numC:
	print "Se cumple que N1 = N2 + N3"
elif numB == numA + numC:
	print "Se cumple que N2 = N1 + N3"
elif numC == numA + numB:
	print "Se cumple que N3 = N1 + N2"
else:
	print "Los números no cumplen la condición"