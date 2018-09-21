from .piece import Piece

class Rook(Piece):
    def __init__(self, x, y, color):
        Piece.__init__(self, x, y, color)

    def attack(self, board):
        conflictsSameColor = 0 
        conflictsDifferentColor = 0
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
                    conflictsSameColor += 1
                    north = False
                if (board.check(self.x, self.y + i, opponent)):
                    conflictsDifferentColor += 1
                    north = False
            else:
                north = False

            #Checking down
            if (south and (self.y - i >= 0)):
                if (board.check(self.x, self.y - i, self.color)):
                    conflictsSameColor += 1
                    south = False
                if (board.check(self.x, self.y - i, opponent)):
                    conflictsDifferentColor += 1
                    south = False
            else:
                south = False

            #Checking right
            if (west and (self.x + i <= 7)):
                if (board.check(self.x + i, self.y, self.color)):
                    conflictsSameColor += 1
                    west = False
                if (board.check(self.x + i, self.y, opponent)):
                    conflictsDifferentColor += 1
                    west = False
            else:
                west = False
            
            #Checking left
            if (east and (self.x - i >= 0)):
                if (board.check(self.x - i, self.y, self.color)):
                    conflictsSameColor += 1
                    east = False
                if (board.check(self.x - i, self.y, opponent)):
                    conflictsDifferentColor += 1
                    east = False
            else:
                east = False
            #If every direction already found other piece then break out iteration
            if ((not north) and (not south) and (not west) and (not east)):
                break
        return conflictsSameColor, conflictsDifferentColor


    def getChar(self):
        if self.color == 'w':
            return 'R'
        else:   # color == 'b'
            return 'r'