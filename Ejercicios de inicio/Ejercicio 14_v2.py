dinero = int(input("Introduce una cantidad de dinero: "))

def contarDinero(cantidad, valor):
	if valor <= cantidad & cantidad > 4:
		contador = cantidad // valor
		cantidad = cantidad % valor
		print("Hay ", contador, " billetes de ", valor, "€")
		return cantidad
	elif valor <= cantidad & cantidad > 0 & cantidad < 4:
		contador = cantidad // valor
		cantidad = cantidad % valor
		print ("Hay ", contador, " monedas de ", valor, "€")
		return cantidad
	else:
		return cantidad
		
tipos = [500, 200, 100, 50, 20, 10, 5, 2, 1]
for x in tipos: dinero = contarDinero(dinero, x)