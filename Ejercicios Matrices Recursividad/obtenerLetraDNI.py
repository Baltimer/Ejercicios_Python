## Hacer un programa que dado un número de DNI obtenga la letra del NIF. 
## La letra correspondiente a un número de DNI se calcula mediante el 
## siguiente algoritmo: 
## 		a) Se obtiene el resto de dividir el número de DNI entre 23. 
## 		b) El número resultante nos indica la posición de la letra 
##		correspondiente a ese DNI, en la siguiente cadena:
##		(Mirar lista/diccionario de Asignación)

diccionarioAsignacion={	 0:"T",
						 1:"R",
						 2:"W",
						 3:"A",
						 4:"G",
						 5:"M",
						 6:"Y",
						 7:"F",
						 8:"P",
						 9:"D",
						 10:"X",
						 11:"B",
						 12:"N",
						 13:"J",
						 14:"Z",
						 15:"S",
						 16:"Q",
						 17:"V",
						 18:"H",
						 19:"L",
						 20:"C",
						 21:"K",
						 22:"E"
						}

listaAsignacion=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

def calcularLetraNIF(dni):
	for numero in dni:

def esCorrecto(DNI):
	if len(DNI) != 9:
		print("No has introducido un DNI")
		return False

	for posicion in DNI:
		if 0 <= DNI.index(posicion) <= 7 and posicion.isdigit() != True:
			return False
		else DNI.index(posicion) == 8 and posicion.islower() and (posicion.isalpha() or posicion.isdigit()):
			return False
	return True