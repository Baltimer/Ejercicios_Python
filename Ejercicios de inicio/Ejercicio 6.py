# Escribe un programa que pida por teclado dos valores de tipo 
# numérico que se han de guardar en sendas variables y se intercambien.
#
# Autor: Luis Cifre
#
# Casos tipo:
#
# varA = 4, varB = 5 ==> varA = 5, varB = 4

varA = int(input("Introduce el primer número: "))
varB = int(input("Introduce el segundo número: "))

varC = varA
varA = varB
varB = varC

print "Los números intercambiados son: \nPrimero: ", varA, "\nSegundo: ", VarB