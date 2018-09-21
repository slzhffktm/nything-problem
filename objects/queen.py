from .piece import Piece

class Queen(Piece):

    # constructor
    def __init__(self, x, y, color):        
        Piece.__init__(self, x, y, color)


    # return how many conflicts occured
    def attack(self, board):
        friendly_attack = 0  # count how many friend pieces can be attacked
        enemy_attack = 0     # count how many enemy pieces can be attacked

        # declare enemy color
        if self.color == 'w':
            enemy_color = 'b'
        else:
            enemy_color = 'w'

        # diagonal
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

        # vertical and horizontal
        north = True
        south = True
        west = True
        east = True
        #Determining opponent color
        if (self.color == 'w'):
            opponent = 'b'
        else:
            opponent = 'w'
        #iteration to check conflicts
        for i in range (1,7):
            #checking up
            if (north and (self.y + i <= 7)):
                if (board.check(self.x, self.y + i, self.color)):
                    friendly_attack += 1
                    north = False
                if (board.check(self.x, self.y + i, opponent)):
                    enemy_attack += 1
                    north = False
            else:
                north = False

            #Checking down
            if (south and (self.y - i >= 0)):
                if (board.check(self.x, self.y - i, self.color)):
                    friendly_attack += 1
                    south = False
                if (board.check(self.x, self.y - i, opponent)):
                    enemy_attack += 1
                    south = False
            else:
                south = False

            #Checking right
            if (west and (self.x + i <= 7)):
                if (board.check(self.x + i, self.y, self.color)):
                    friendly_attack += 1
                    west = False
                if (board.check(self.x + i, self.y, opponent)):
                    enemy_attack += 1
                    west = False
            else:
                west = False
            
            #Checking left
            if (east and (self.x - i >= 0)):
                if (board.check(self.x - i, self.y, self.color)):
                    friendly_attack += 1
                    east = False
                if (board.check(self.x - i, self.y, opponent)):
                    enemy_attack += 1
                    east = False
            else:
                east = False
            #If every direction already found other piece then break out iteration
            if ((not north) and (not south) and (not west) and (not east)):
                break

        return friendly_attack, enemy_attack


    def getChar(self):
        if self.color == 'w':
            return 'Q'
        else:   # color == 'b'
            return 'q'