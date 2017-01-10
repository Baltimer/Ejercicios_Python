# Lee por teclado 5 números enteros positivos, 
# y escribe cuál es el mayor de los números introducidos.  
#
# Autor: Luis Cifre
#
# Casos tipo:
#
# Valor = 5, Imprimirá: 2, 4, 6, 8, 10

num1 = int(input("Introduce el primer número positivo: "))
num2 = int(input("Introduce el segundo número positivo: "))
num3 = int(input("Introduce el tercer número positivo: "))
num4 = int(input("Introduce el cuarto número positivo: "))
num5 = int(input("Introduce el quinto número positivo: "))

if num1 > num2:
	if num1 > num3:
		if num1 > num4:
			if num1 > num5:
				print "El ", num1, " es el mayor."
			else:
				print "El ", num5, " es el mayor."
		elif num4 > num5:
			print "El ", num4, " es el mayor."
		else:
			print "El ", num5, " es el mayor."
	elif num3 > num4:
		if num3 > num5:
			print "El ", num3, " es el mayor."
		else:
			print "El ", num5, " es el mayor."
	elif num4 > num5:
		print "El ", num4, " es el mayor."
	else:
		print "El ", num5, " es el mayor."
else:
	if num2 > num3:
		if num2 > num4:
			if num2 > num5:
				print "El ", num2, " es el mayor."
			else:
				print "El ", num5, " es el mayor."
		elif num4 > num5:
			print "El ", num4, " es el mayor."
		else:
			print "El ", num5, " es el mayor."
	elif num3 > num4:
		if num3 > num5:
			print "El ", num3, " es el mayor."
		else:
			print "El ", num5, " es el mayor."
	elif num4 > num5:
		print "El ", num4, " es el mayor."
	else:
		print "El ", num5, " es el mayor."