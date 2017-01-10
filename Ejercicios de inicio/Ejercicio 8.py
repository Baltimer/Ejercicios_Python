# Escribe    un programa que pida por teclado dos números y que muestre en
# pantalla uno de los dos mensajes siguientes en función de los números leídos: 
# a) el primer número (valor) es mayor que el segundo (valor)
#	(introduciendo el valor de los números en el mensaje); 
# b) el primer número (valor) es menor que el segundo (valor; 
# c) los dos números son iguales (valor).
#
# Autor: Luis Cifre
#
# Casos tipo:
#
# a) numA = 5, numB = 4, A>B
# b) numA = 4, numB = 5, A<B
# c) numA = 3, numB = 3, A=B

numA = int(input("Introduce el primer número: "))
numB = int(input("Introduce el segundo número: "))

if numA>numB:
	print "El primer número ", numA, " es mayor que el segundo ", numB
elif numA<numB:
	print "El primer número ", numA, " es menor que el segundo ", numB
else:
	print "Los dos números son iguales"