from .piece import Piece

class Queen(Piece):

    # constructor
    def __init__(self, x, y, color):        
        Piece.__init__(self, x, y, color)


    # return how many conflicts occured
    def attack(self, board):
        conflicts = 0

        # diagonal
        # left-down
        j = self.y
        for i in range(self.x-1, -1, -1):
            if j - 1 < 0:
                break
            else:
                j = j - 1
                if board.check(i, j):
                    conflicts += 1
                    break
        
        # left-up
        j = self.y
        for i in range(self.x-1, -1, -1):
            if j + 1 > 7:
                break
            else:
                j = j + 1
                if board.check(i, j):
                    conflicts += 1
                    break

        # right-up
        j = self.y
        for i in range(self.x+1, 8):
            if j + 1 > 7:
                break
            else:
                j = j + 1
                if board.check(i, j):
                    conflicts += 1
                    break

        # right-down
        j = self.y
        for i in range(self.x+1, 8):
            if j - 1 < 0:
                break
            else:
                j = j - 1
                if board.check(i, j):
                    conflicts += 1
                    break

        # vertical and horizontal
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


    def getChar(self):
        if self.color == 'w':
            return 'Q'
        else:   # color == 'b'
            return 'q'