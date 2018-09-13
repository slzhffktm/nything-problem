from rook import Rook

class Board:
    
    def check(self, i, j):
        if (i == 5 and j == 3) or (i == 5 and j == 4):
            return True
        return False

board = Board()
bishop = Rook(5, 5)

print(bishop.attack(board))
