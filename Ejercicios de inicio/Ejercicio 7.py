# Escribe un programa que pida por teclado un número y que a continuación muestre 
# el mensaje el número leído es positivo o bien el número leído es negativo 
# dependiendo de que el número introducido por teclado sea positivo o negativo. 
# Consideramos al número 0 positivo.
#
# Autor: Luis Cifre
#
# Casos tipo:
#
# numero = 5, Positivo ==> numero = -4, Negativo

numero = int(input("Introduce un número y te diré si es positivo o negativo: "))

if numero >= 0:
	print "El número introducido es positivo"
else:
	print "El número introducido es negativo"