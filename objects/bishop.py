from .piece import Piece

class Bishop(Piece):

    # constructor
    def __init__(self, x, y, color):        
        Piece.__init__(self, x, y, color)


    # return how many pieces can be attacked by bishop
    def attack(self, board):
        attacked = 0    # count how many pieces can be attacked by bishop

        # left-down
        j = self.y
        for i in range(self.x-1, -1, -1):
            if j - 1 < 0:
                break
            else:
                j = j - 1
                if board.check(i, j):
                    attacked += 1
                    break
        
        # left-up
        j = self.y
        for i in range(self.x-1, -1, -1):
            if j + 1 > 7:
                break
            else:
                j = j + 1
                if board.check(i, j):
                    attacked += 1
                    break

        # right-up
        j = self.y
        for i in range(self.x+1, 8):
            if j + 1 > 7:
                break
            else:
                j = j + 1
                if board.check(i, j):
                    attacked += 1
                    break

        # right-down
        j = self.y
        for i in range(self.x+1, 8):
            if j - 1 < 0:
                break
            else:
                j = j - 1
                if board.check(i, j):
                    attacked += 1
                    break

        return attacked

    def getChar(self):
        if self.color == 'w':
            return 'B'
        else:   # color == 'b'
            return 'b'