# Escribe un programa que pida por teclado el radio de una circunferencia, y que a continuación 
# calcule y escriba en pantalla la longitud de la circunferencia y del área del círculo.
#
# Autor: Luis Cifre
#
# Casos tipo:
#
# Radio = 5, Longuitud = 2·pi·Radio, Área = pi·Radio^2

import math

radio = int(input("Escribe el radio de una circunferencia: "))

print "La longuitud de la circunferencia es: ", radio*2*math.pi
print "El área de la circunferencia es: ", math.pi*radio**2