# Escribe un programa que pida por teclado una cantidad de dinero y 
# que a continuación muestre la descomposición de dicho importe en el 
# menor número de billetes y monedas de 100, 50, 20, 10, 5, 2 y 1 euro.
#
# Autor: Luis Cifre
#
# Casos tipo:
#
# Valor = 2364
# Billetes100 = 23, Billetes50 = 1, Billetes20 = 0, Billetes10 = 1
# Billetes5 = 0, Monedas2 = 2, Monedas1 = 0

Valor = int(input("Escribe una cantidad de euros: "))

Billetes100 = Valor//100
Valor = Valor%100

Billetes50 = Valor//50
Valor = Valor%50

Billetes20 = Valor//20
Valor = Valor%20

Billetes10 = Valor//10
Valor = Valor%10

Billetes5 = Valor//5
Valor = Valor%5

Monedas2 = Valor//2
Valor = Valor%2

Monedas1 = Valor//1
Valor = Valor%1

print ("Billetes de 100: ", Billetes100, "\nBilletes de 50: ", Billetes50, 
	"\nBilletes de 20: ", Billetes20, "\nBilletes de 10: ", Billetes10,
	"\nBilletes de 5: ", Billetes5, "\nMonedas de 2: ", Monedas2,
	"\nMonedas de 1: ", Monedas1)