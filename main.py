from objects.board import Board
from algorithms.genetic import genetic

b = Board()
b.readExternalFile()
b.show()

genetic(b)
