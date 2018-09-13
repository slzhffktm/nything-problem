from .piece import Piece

class Rook(Piece):
    def __init__(self, x, y, color):
        Piece.__init__(self, x, y, color)

    def attack(self, board):
        conflicts = 0
        north = True
        south = True
        west = True
        east = True
        for i in range (1,7):
            if (north and (self.y + i <= 7)):
                if (board.check(self.x, self.y + i)):
                    conflicts += 1
                    north = False
            else:
                north = False

            if (south and (self.y - i >= 0)):
                if (board.check(self.x, self.y - i)):
                    conflicts += 1
                    south = False
            else:
                south = False

            if (west and (self.x + i <= 7)):
                if (board.check(self.x + i, self.y)):
                    conflicts += 1
                    west = False
            else:
                west = False
            
            if (east and (self.x - i >= 0)):
                if (board.check(self.x - i, self.y)):
                    conflicts += 1
                    east = False
            else:
                east = False
        return conflicts