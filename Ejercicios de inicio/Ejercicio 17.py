# Escribe un programa que calcule y escriba la suma de los 
# números pares por un lado, y de los impares por otro, de los 
# números comprendidos entre dos número introducidos por teclado.
#
# Autor: Luis Cifre
#
# Casos tipo:
#
# NumA = 3, NumB = 10
# SumaNumPares = 28, SumaNumImpares = 24

numA = int(input("Introduce el primer número: "))
numB = int(input("Introduce el segundo número: "))
SumaNumPares = 0;
SumaNumImpares = 0;

for i in range(numA, numB+1):
	if i%2 == 0:
		SumaNumPares = SumaNumPares + i
	else:
		SumaNumImpares = SumaNumImpares + i

print "La suma de los números Pares es: ", SumaNumPares
print "La suma de los números Impares es: ", SumaNumImpares