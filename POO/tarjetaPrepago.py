#coding = utf-8

class tarjetaPrepago:
	def __init__(self, numeroTelefono, nif, saldo, consumo):
		self.numeroTelefono = numeroTelefono
		self.nif = nif
		self.saldo = saldo
		self.consumo = consumo

	def __repr__(self):
		return self.numeroTelefono + ", " + self.nif + ", " + self.saldo + ", " + self.consumo

	def setNumeroTelefono(self):
		self.numeroTelefono = numeroTelefono
	def getNumeroTelefono(self):
		return self.numeroTelefono

	def setNif(self):
		self.nif = nif
	def getNif(self):
		return self.nif

	def setSaldo(self):
		self.saldo = saldo
	def getSaldo(self):
		return self.saldo

	def setConsumo(self):
		self.consumo = consumo
	def getConsumo(self):
		return self.consumo

	def ingresarSaldo(self, saldo):
		self.saldo += saldo

	def enviarMensaje(self, mensajes):
		if self.saldo >= mensajes*0.09:
			self.saldo -= mensajes*0.09
		else:
			print("No dispones de suficiente saldo.")

	def realizarLlamada(self, segundos):
		self.saldo -= 0.15 + segundos*0.01
		## PENDIENTE ACTALIZAR CONSUMO

	def consultarTarjeta(self):
		return print (self)