# Escribe un programa que calcule el área de una finca rectangular en 
# metros cuadrados, así como su perímetro exterior, también en metros.
#
# Autor: Luis Cifre
#
# Casos tipo:
#
# ladoA = 3, ladoB = 4, area = 12, perimetro = 14

ladoA = int(input("Introduce el lado corto de la finca: "))
ladoB = int(input("Introduce el lado largo de la finca: "))

print "El área de la finca es: ", ladoA*ladoB
print "El perímetro de la finca es: ", (ladoA*2)+(ladoB*2)