# coding = utf-8

class Hora:
	def __init__(self, hora=0, minutos=0, segundos=0):
		self.hora = hora
		self.minutos = minutos
		self.segundos = segundos

	def __repr__(self):
		return self.hora + ":" + self.minutos + ":" + self.segundos

	def setHora(self, hora):
		self.hora = hora
	def getHora(self, hora):
		return self.hora

	def setMinutos(self, minutos):
		self.minutos = minutos
	def getHora(self, minutos):
		return self.minutos

	def setHora(self, segundos):
		self.segundos = segundos
	def getHora(self, segundos):
		return self.segundos

	def establecerHora(self, hora, minutos, segundos):
		self.hora = hora
		self.minutos = minutos
		self.segundos = segundos

	def devolverHora(self):
		return self.hora + ":" + self.minutos + ":" + self.segundos

	def imprimirHora(self):
		return self.hora + ":" + self.minutos + ":" + self.segundos

def definirHora():
	horaActual = input("Que hora es? ")
	minutosActual = input("Cuantos minutos? ")
	segundosActual = input("Cuantos segundos? ")

	hora = Hora(horaActual, minutosActual, segundosActual)

	hora.imprimirHora()

definirHora()