from Partida import Partida
from Barco import Barco


class Juego():
	def __init__(self, matriz, barcos, cantidadLanzaderas):
		self.jugadores = []
		self.matriz = matriz
		self.barcos = barcos
		self.cantidadLanzaderas = cantidadLanzaderas

	def agregarJugador(self, jugador):
		self.jugadores.append(jugador)

	def nuevaPartidaCon(self, jugador, posicionesDefault = True):
		partida = Partida(self.matriz, self.barcos, self.cantidadLanzaderas, jugador)
		if posicionesDefault: partida.setPosicionesIniciales()
		return partida

	@staticmethod
	def ArchivoToBarcos(archivo):
		vida_barcos = []
		with open(archivo, 'r') as f:
			for linea in f:
				linea = linea.split()
				vida = int(linea[0])
				vida_barcos.append(vida)
		barcos = []
		for vida in vida_barcos:
			barcos.append(Barco(vida))
		return barcos

	@staticmethod
	def ArchivoToMatriz(archivo):
		matriz = []
		with open(archivo, 'r') as f:
			for linea in f:
				linea = linea.split()
				linea = linea[1:] #El primer valor es un barco
				linea = [int(x) for x in linea]
				matriz.append(linea)
		return matriz