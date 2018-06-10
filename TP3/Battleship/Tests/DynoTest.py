import unittest
from Greedo import Greedo
from Dyno import Dyno
from Partida import Partida
from Barco import Barco

class MismasPruebasGreedoTestUnaLanzaderaGree(unittest.TestCase):
	def testUnaLanzaderaUnBarcoUnicaOpcionPosibleDerribarlo(self):
		dyno = Dyno()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[100, 40, 30, 10]]
		partida = Partida(matriz, [barco], 1, dyno)
		targets = dyno.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(barco.estaDerribado())

	def testUnaLanzaderaUnBarcoUnicaOpcionPosibleNoDerribarlo(self):
		dyno = Dyno()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[10, 40, 30, 10]]
		partida = Partida(matriz, [barco], 1, dyno)
		targets = dyno.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(barco.estaDerribado())

	def testUnaLanzaderaDosBarcosSacaLaMayorCantidadPosible(self):
		dyno = Dyno()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0,1)
		matriz = [[80, 40, 30, 10], [50, 30, 80, 100]]
		partida = Partida(matriz, [A,B], 1, dyno)
		targets = dyno.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())
		self.assertTrue(A.getVida() < B.getVida())

	def testUnaLanzaderaDosBarcosDerribaAlQuePuede(self):
		dyno = Dyno()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0,1)
		matriz = [[100, 40, 30, 10], [50, 30, 80, 100]]
		partida = Partida(matriz, [A,B], 1, dyno)
		targets = dyno.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

	def testUnaLanzaderaDosBarcosDerribaAlQuePuedeInvertido(self):
		dyno = Dyno()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0,1)
		matriz = [[50, 40, 30, 10], [100, 30, 80, 100]]
		partida = Partida(matriz, [A,B], 1, dyno)
		targets = dyno.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertTrue(B.estaDerribado())

	def testUnaLanzaderaDosBarcosDerribaIgualesDerribaAlPrimero(self):
		dyno = Dyno()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[100, 40, 30, 10], [100, 30, 80, 100]]
		partida = Partida(matriz, [A,B], 1, dyno)
		targets = dyno.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

class MismasPruebasGreedoTestTresLanzaderas(unittest.TestCase):
	def testTresLanzaderasUnBarcoDerribado(self):
		dyno = Dyno()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[50, 40, 30, 10]]
		partida = Partida(matriz, [barco], 3, dyno)
		targets = dyno.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(barco.estaDerribado())

	def testTresLanzaderasUnBarcoNoDerribado(self):
		dyno = Dyno()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[10, 40, 30, 10]]
		partida = Partida(matriz, [barco], 3, dyno)
		targets = dyno.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(barco.estaDerribado())

	def testTresLanzaderasDosBarcoUnoDerribado(self):
		dyno = Dyno()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[50, 40, 30, 10], [40, 30, 80, 100]]
		partida = Partida(matriz, [A, B], 3, dyno)
		targets = dyno.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

	def testTresLanzaderasDosBarcoUnoDerribadoInvertido(self):
		dyno = Dyno()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[10, 40, 30, 10], [50, 30, 80, 100]]
		partida = Partida(matriz, [A, B], 3, dyno)
		targets = dyno.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertTrue(B.estaDerribado())

	def testTresLanzaderasDosBarcoAmbosDerribados(self):
		dyno = Dyno()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[50, 40, 30, 10], [100, 30, 80, 100]]
		partida = Partida(matriz, [A, B], 3, dyno)
		targets = dyno.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(A.estaDerribado())
		self.assertTrue(B.estaDerribado())

	def testTresLanzaderasDosBarcoNingunoDerribado(self):
		dyno = Dyno()
		A = Barco(1000)
		B = Barco(1000)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[50, 40, 30, 10], [100, 30, 80, 100]]
		partida = Partida(matriz, [A, B], 3, dyno)
		targets = dyno.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

	def testTresLanzaderasDosBarcoNingunoDerribado2(self):
		dyno = Dyno()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[1, 1000, 30, 10], [2, 1000, 80, 100]]
		partida = Partida(matriz, [A, B], 3, dyno)
		targets = dyno.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

class TestsDiferenciasGreedoBrutoGreedo(unittest.TestCase):
	def testGreeedoBrutoEligeElMejorTurnoPosible(self):
		dyno = Dyno()
		A = Barco(300)
		B = Barco(200)
		C = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		C.setPosicion(0,2)
		matriz = [[60],[50],[50]]
		partida = Partida(matriz, [A, B, C], 2, dyno)
		targets = dyno.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(C.estaDerribado())
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

	def testGreedoBrutoElijeMejorTurnoQueGreedo(self):
		dyno = Dyno()
		A = Barco(300)
		B = Barco(200)
		C = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		C.setPosicion(0, 2)
		matriz = [[60], [50], [50]]
		partida = Partida(matriz, [A, B, C], 2, dyno)
		targets = dyno.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(C.estaDerribado())
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

		greedo = Greedo()
		A = Barco(300)
		B = Barco(200)
		C = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		C.setPosicion(0, 2)
		partidaG = Partida(matriz, [A, B, C], 2, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partidaG)
		partidaG.setTargetDelTurno(targets[0])
		partidaG.jugarTurno()
		self.assertFalse(C.estaDerribado())
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())


if __name__ == '__main__':
	unittest.main()