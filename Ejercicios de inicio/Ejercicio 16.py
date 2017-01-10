# Escribe un programa que escriba en pantalla los 30 primeros 
# números naturales (del 1 al 30), así como su media aritmética.
#
# Autor: Luis Cifre
#
# Casos tipo:
#
# imrimir los 30 primeros números naturales
# MediaAritmética = (1+2+3...) / 30

suma = 0

for i in range(30):
	print i
	suma = suma + i

print "La suma de todos los números del 1 al 30 es: ", suma