# class Bishop
from .piece import Piece

class Bishop(Piece):

    # constructor
    def __init__(self, x, y, color):
        Piece.__init__(self, x, y, color)


    # return how many pieces can be attacked by bishop
    def attack(self, board):
        friendly_attack = 0  # count how many friend pieces can be attacked
        enemy_attack = 0     # count how many enemy pieces can be attacked

        # declare enemy color
        if self.color == 'w':
            enemy_color = 'b'
        else:
            enemy_color = 'w'

        # left-down
        j = self.y
        for i in range(self.x-1, -1, -1):
            if j - 1 < 0:
                break
            else:
                j = j - 1
                if board.check(i, j, self.color):
                    friendly_attack += 1
                    break
                elif board.check(i, j, enemy_color):
                    enemy_attack += 1
                    break

        # left-up
        j = self.y
        for i in range(self.x-1, -1, -1):
            if j + 1 > 7:
                break
            else:
                j = j + 1
                if board.check(i, j, self.color):
                    friendly_attack += 1
                    break
                elif board.check(i, j, enemy_color):
                    enemy_attack += 1
                    break

        # right-up
        j = self.y
        for i in range(self.x+1, 8):
            if j + 1 > 7:
                break
            else:
                j = j + 1
                if board.check(i, j, self.color):
                    friendly_attack += 1
                    break
                elif board.check(i, j, enemy_color):
                    enemy_attack += 1
                    break

        # right-down
        j = self.y
        for i in range(self.x+1, 8):
            if j - 1 < 0:
                break
            else:
                j = j - 1
                if board.check(i, j, self.color):
                    friendly_attack += 1
                    break
                elif board.check(i, j, enemy_color):
                    enemy_attack += 1
                    break

        return friendly_attack, enemy_attack


    def getChar(self):
        if self.color == 'w':
            return 'B'
        else:
            return 'b'
