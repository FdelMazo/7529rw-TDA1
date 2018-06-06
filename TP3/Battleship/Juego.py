from Barco import Barco

class Juego():
    def __init__(self, matriz, barcos, cantidadLanzaderas, jugador):
        self.matriz = matriz
        self.barcos = barcos
        self.cantidadLanzaderas = cantidadLanzaderas
        self.turno = 0
        self.puntos = 0
        self.jugador = jugador
        self.targets = [None] * self.cantidadLanzaderas

    def terminado(self):
        return not self.getBarcosVivos()

    def setPosicionesIniciales(self):
        for i, barco in enumerate(self.barcos):
            barco.setPosicion(0,i)

    def avanzarBarcos(self):
        for barco in self.barcos:
            x, y = barco.getPosicion()
            if x == len(self.matriz[y]) - 1:
                barco.setPosicion(0,y)
            else:
                barco.setPosicion(x + 1, y)

    def getBarcosVivos(self):
        return [b for b in self.barcos if not b.estaDerribado()]

    def getBarcos(self):
        return self.barcos
        
    def getDanioCasillero(self, x, y):
        return self.matriz[y][x]

    def getCantidadLanzaderas(self):
        return self.cantidadLanzaderas

    def elegirTargets(self):
        self.targets = self.jugador.elegirTargets(self)
        self.barcosAtacados = [i.getPosicion()[1] if i != None else None for i in self.targets ]

    def jugarTurno(self):
        self.jugador.addPuntos(len(self.getBarcosVivos()))
        for barco in self.targets:
            if barco: barco.recibirDanio(self.getDanioCasillero(*barco.getPosicion()))
        self.avanzarBarcos()
        self.turno += 1

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