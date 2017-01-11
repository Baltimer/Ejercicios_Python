## Verificar si una cadena de texto leída por teclado es un  
## DNI correcto o no. Suponer que los DNI tienen 8 dígitos y 
## a continuación una letra mayúscula.


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

DNIIntroducido = input("Introduce tu DNI:\n")
print (esCorrecto(DNIIntroducido))