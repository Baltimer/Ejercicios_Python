# Diseña un programa que calcule el importe final de una venta considerando 
# que sobre el valor bruto se hace un descuento según la siguiente tabla:
# Valores <=20 implican un descuento del 0%
# Valores >20 y <=100 implican un descuento descuento del 5%
# Valores >100 implican un descuento 10%
#
# Autor: Luis Cifre
#
# Casos tipo:
#
# importe = 10, total = 10
# importe = 50, total = 47'5
# importe = 200, total = 180

importe = int(input("Introduc el valor de la venta: "))

if importe <= 20:
	print "El importe total es: ", importe
elif importe > 20 and importe <=100:
	print "El importe total es: ", importe*0.95
else:
	print "El importe total es: ", importe*0.9