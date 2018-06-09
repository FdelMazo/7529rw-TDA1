from Terminal import Terminal
from VistaPartida import VistaPartida


class VistaJuego():
	def __init__(self, juego, no_input):
		self.juego = juego
		self.terminal = Terminal(no_input)

	def titulo(self):
		string = "\n*******************************\n" \
				 "Battleship: La Batalla Final! \n\n" \
				 "En esta esquina, el memorizador Dyno! El mejor programador de la historia desde Thomas Cormen \n" \
				 "En esta otra, el goloso Greedo! El sucesor al creador de la programacion greedy, John Greedy \n" \
		         "Oh no! Que es esa cosa monstruosa allí? Esta entrando un nuevo participante! La horrorosa abominación, hija de nadie, GreedoBruto \n" \
				 "*******************************\n"
		print(self.terminal.pretty_string(string, 'TITLE'))
		self.terminal.print_command()
		self.terminal.clear()

	def cambioDeTurno(self):
		string = "*******************************\n" \
				 "Cambio de turno!!!\n" \
				 "*******************************\n"
		print(self.terminal.pretty_string(string, 'TITLE'))
		self.terminal.clear()

	def imprimirGanador(self):
		string = "*******************************\n"
		if self.juego.getLeaderboard()[0].getPuntos() == self.juego.getLeaderboard()[1].getPuntos():
			ganadorString = "Empataron!!!\n\n"
		else:
			ganadorString = "El ganador es {}!!!\n\n".format(self.juego.getLeaderboard()[0])
		string += ganadorString
		for j in self.juego.getLeaderboard():
			string += "{}: {} Puntos\n".format(j, j.getPuntos())
		string += "*******************************\n"
		print(self.terminal.pretty_string(string, 'TITLE'))

	def nuevaVistaPartida(self, partida):
		vistaPartida = VistaPartida(partida, self.terminal)
		return vistaPartida


