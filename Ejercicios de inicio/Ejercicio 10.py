# Modifica el programa anterior para que en vez de mostrar un mensaje 
# genérico en el caso de que alguno o los dos números sean negativos, 
# escriba una salida diferenciada para cada una de las situaciones 
# que se puedan producir.
#
# Autor: Luis Cifre
#
# Casos tipo:
#
# numA = 4, numB = 5, suma = 9 ==> numA = -3, numB = 4, numA negativo
# numA = 4, numB = -3, numV negativo ==> numA = -3, numB = -4, Negativos

numA = int(input("Introduce el primer número :"))
numB = int(input("Introduce el segundo número :"))

if numA >= 0 and numB >= 0:
	print "La suma de los dos números es: ", numA+numB
elif numA < 0 and numB >= 0:
	print "No se calcula la suma porque el primer número es negativo."
elif numA >= 0 and numB < 0:
	print "No se calcula la suma porque el segundo número es negativo."
else:
	print "Los dos números son negativos!"
