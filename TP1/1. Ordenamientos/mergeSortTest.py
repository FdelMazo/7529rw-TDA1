import unittest
import random

from mergeSort import mergeSort

def generarArrayRandom(n, low, high):
	return [int(n*random.random()) for i in range(low, high)]


class TestListaVacia(unittest.TestCase):

	def test001OrdenarListaVaciaSort(self):
		array = []
		result = []
		arrayOrdenado = mergeSort(array)
		self.assertEqual(result, arrayOrdenado)

class TestListaUno(unittest.TestCase):

	def test001OrdenarListaUnoSort(self):
		array = [1]
		result = [1]
		arrayOrdenado = mergeSort(array)
		self.assertEqual(result, arrayOrdenado)


class TestListaDe2Elementos(unittest.TestCase):

	def test001OrdenarLista2ElementosSort(self):
		array = [2, 1]
		result = [1, 2]
		arrayOrdenado = mergeSort(array)
		self.assertEqual(result, arrayOrdenado)

class TestListaDe500Elementos(unittest.TestCase):

	def test001OrdenarListaDe500ElementosSort(self):
		array = generarArrayRandom(500, 0, 1000)
		result = sorted(array)
		arrayOrdenado = mergeSort(array)
		self.assertEqual(result, arrayOrdenado)

class TestListaDe1000Elementos(unittest.TestCase):

	def test001OrdenarListaDe1000ElementosSort(self):
		array = generarArrayRandom(1000, 0, 10000)
		result = sorted(array)
		arrayOrdenado = mergeSort(array)
		self.assertEqual(result, arrayOrdenado)

class TestListaDe10000Elementos(unittest.TestCase):

	def test001OrdenarListaDe10000ElementosSort(self):
		array = generarArrayRandom(10000, 0, 10000)
		result = sorted(array)
		arrayOrdenado = mergeSort(array)
		self.assertEqual(result, arrayOrdenado)

class TestListaOrdenada(unittest.TestCase):

	def test001OrdenarListaOrdenadaSort(self):
		array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		result = sorted(array)
		arrayOrdenado = mergeSort(array)
		self.assertEqual(result, arrayOrdenado)

if __name__ == '__main__':
	unittest.main()
