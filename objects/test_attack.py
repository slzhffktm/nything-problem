class Board:
    
    def check(self, i, j):
        if (i == 8 and j == 8) or (i == 6 and j == 4):
            return True
        return False

board = Board()
# bishop = Bishop(5, 5)

# print(bishop.attack(board))
