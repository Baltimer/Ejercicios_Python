# Escribe un programa que visualice los n-primeros múltiplos de 2, 
# siendo n un valor leído por teclado.
#
# Autor: Luis Cifre
#
# Casos tipo:
#
# Valor = 5, Imprimirá: 2, 4, 6, 8, 10

Valor = int(input("Introduce un valor: "))

print "Los ", Valor, " primeros múltiplos de 2 son:"

for i in range(Valor*2+1):
	if i==0:
	  continue
	elif i%2 == 0:
		print i