from Grafo import *
from GrafoPesado import *
from math import factorial
import random


def obtener_vertices(numeros_de_linea):  
    if len(numeros_de_linea) < 3:
        print("No todas las posiciones fueron dadas. Se completa con lineas elegidas al azar")
        with open('mapa.coords') as f:
            cant_lineas = len(f.readlines())
        while len(numeros_de_linea) < 3:
            numeros_de_linea.append(random.randint(0,cant_lineas-1))
    return lineas_a_vertices(numeros_de_linea)

def lineas_a_vertices(numeros_de_linea):
    vertices = []
    numeros_de_linea = sorted([int(x) for x in numeros_de_linea])
    with open('mapa.coords') as file:
        lineas_file = file.readlines()
        for i in numeros_de_linea:
            linea = lineas_file[i]
            v1,_ = stringADosVertices(linea)
            vertices.append(v1)
    return vertices

def stringADosVertices(linea):
    datos = linea.split()
    datos.pop(2) #Sacar el guion
    datos = [int (x) for x in datos]
    x1,y1,x2,y2 = datos
    return ( (x1, y1) , (x2,y2) )

def generarArchivo(dimensionX, dimensionY, porcentajeCargado):
    """Crea el archivo 'mapa.coords' que es un grafo representado con una matriz de dimension dada
    donde las lineas especifican una conexion entre puntos de la ciudad"""
    if porcentajeCargado > 100:
        porcentajeCargado = 100
    cantidadPuntos = porcentajeCargado/100 * dimensionX*dimensionY
    conexiones = set()
    while len(conexiones) < cantidadPuntos:
        punto1 = ( random.randint(0,dimensionX-1) , random.randint(0,dimensionY-1) )
        punto2 = ( random.randint(0,dimensionX-1) , random.randint(0,dimensionY-1) )
        if punto1 == punto2: continue
        tuplaordenada = (punto1,punto2) if punto1 < punto2 else (punto2,punto1)
        conexiones.add( tuplaordenada )
    conexiones = sorted(conexiones)
    with open('mapa.coords','w') as file:
        for p1,p2 in conexiones:
            linea = "{} {} - {} {}\n".format(*p1, *p2)
            file.write(linea)

def crearGrafoDesdeArchivo(archivo='mapa.coords', pesado=False):
    """Recibe un archivo de texto.
    El archivo de texto debe tener en cada linea las coordenadas en la forma 'x1 y1 - x2 y2' representando
    la union de dos vertices.
    Devuelve un grafo"""
    grafo = GrafoPesado() if pesado else Grafo()
    with open(archivo, "r") as archivo:
        for linea in archivo:
            v1,v2 = stringADosVertices(linea)
            grafo.add(v1)
            grafo.add(v2)
            grafo.agregarArista(v1, v2)
    return grafo

if __name__ == '__main__':
	generarArchivo(50,50,70)