from objects.board import Board
from algorithms.simulated_annealing import simulatedAnnealing

b = Board()
b.readExternalFile()
b.show()

simulatedAnnealing(b)
