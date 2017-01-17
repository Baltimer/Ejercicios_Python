# coding = utf-8

class Cliente:
	def __init__(self, nombre, apellidos, direccion, telefono, nif, saldo=0):
		self.nombre = nombre
		self.apellidos = apellidos
		self.direccion = direccion
		self.telefono = telefono
		self.nif = nif
		self.saldo = saldo

	def __repr__(self):
		return self.nombre + " " + self.apellidos + ", " + self.direccion + ", " + str(self.telefono) + ", " + str(self.nif) + ", " + str(self.saldo)

	def setNombre(self, nombre):
		self.nombre = nombre
	def getNombre(self):
		return self.nombre

	def setApellidos(self, apellidos):
		self.apellidos = apellidos
	def getApellidos(self):
		return self.apellidos

	def setDireccion(self, direccion):
		self.direccion = direccion
	def getDireccion(self):
		return self.direccion

	def setTelefono(self, telefono):
		self.telefono = telefono
	def getTelefono(self):
		return self.telefono

	def setNif(self, nif):
		self.nif = nif
	def getNif(self):
		return self.nif

	def setSaldo(self, saldo):
		self.saldo = self.saldo
	def getSaldo(self):
		return saldo

	def retirarDinero(self, cantidad):
		if cantidad <= self.saldo:
			self.saldo -= cantidad
		else:
			print("No dispones de suficiente Saldo")

	def ingresarDinero(self, cantidad):
		self.saldo += cantidad

	def consultarCuenta(self):
		return print(self)

	def saldoNegativo(self):
		if self.saldo < 0:
			return True
		return False



def crearCliente():
	nombre = input("Introduce el nombre del Cliente\n")
	apellidos = input("Introduce los apellidos del Cliente\n")
	direccion = input("Introduce la dirección del Cliente\n")
	telefono = input("Introduce el teléfono del Cliente\n")
	nif = input("Introduce el NIF del Cliente\n")
	saldo = input("Introduce el saldo del Cliente\n")

	cliente = Cliente(nombre, apellidos, direccion, telefono, nif, saldo)

	return cliente

def almacenarCliente(cliente, nif):
	clientes[nif] = cliente

clientes = {}
def nuevoCliente():
	cliente = crearCliente()
	almacenarCliente(cliente, cliente.getNif())

#class CuentaCorriente:
	#def __init__(self)

#guille = Cliente("Guille", "Cirer", "casa", 123456, 43215678)
#lluis = Cliente("Lluis", "Cifre Font", "casa", 123456, 43215678, 100)
numeroClientes = input("Cuantos nuevos clientes quieres introducir")
for numCliente in range(0, numeroCliente, 1)
	nuevoCliente()	