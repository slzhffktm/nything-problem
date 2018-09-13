from queen import Queen

class Board:
    
    def check(self, i, j):
        if (i == 6 and j == 6) or (i == 5 and j == 3) or (i == 7 and j == 7):
            return True
        return False

board = Board()
bishop = Queen(5, 5, "red")

print(bishop.attack(board))
