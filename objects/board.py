import random as rnd
from .bishop import Bishop
from .knight import Knight
from .rook import Rook
from .queen import Queen

class Board:
    # Class Attribute
    maps = []
    pieces = []
    # Initializer / Instance Attributes
    def __init__(self):
        for i in range(8):
            self.maps.append(['.', '.', '.', '.', '.', '.', '.', '.'])
        f = open("../test.txt","r")
        inputPieces = f.read().split("\n")
        for data in inputPieces:
            data = data.split(" ")
            for j in range(int(data[2])):
                x = rnd.randint(0,7)
                y = rnd.randint(0,7)
                while(self.maps[x][y] != '.'):
                    x = rnd.randint(0,7)
                    y = rnd.randint(0,7)
                if(data[0] == "WHITE"):
                    if(data[1] == "KNIGHT"):
                        self.maps[x][y] = "K"
                        k = Knight(x,y,'w')
                        self.pieces.append(k)
                    elif(data[1] == "BISHOP"):
                        self.maps[x][y] = "B"
                        b = Bishop(x,y,'w')
                        self.pieces.append(b)
                    elif(data[1] == "ROOK"):
                        self.maps[x][y] = "R"
                        r = Rook(x,y,'w')
                        self.pieces.append(r)
                    elif(data[1] == "QUEEN"):
                        self.maps[x][y] = "Q"
                        q = Queen(x,y,'w')
                        self.pieces.append(q)
                elif(data[0] == "BLACK"):
                    if(data[1] == "KNIGHT"):
                        self.maps[x][y] = "k"
                        k = Knight(x,y,'b')
                        self.pieces.append(k)
                    elif(data[1] == "BISHOP"):
                        self.maps[x][y] = "b"
                        b = Bishop(x,y,'b')
                        self.pieces.append(b)
                    elif(data[1] == "ROOK"):
                        self.maps[x][y] = "r"
                        r = Rook(x,y,'b')
                        self.pieces.append(r)
                    elif(data[1] == "QUEEN"):
                        self.maps[x][y] = "q"
                        q = Queen(x,y,'b')
                        self.pieces.append(q)
    # instance method
    def show(self):
        for i in range(8):
            for j in range(7,-1,-1):
                print(self.maps[i][j], end = " ")
            print()

    def countConflictsSameColor(self):
        count = 0
        for piece in self.pieces:
            count += piece.attack(self)
        return count
    def countConflicts(self):
        sameColor = self.countConflictsSameColor()
        difColor = 0
        print(sameColor," ",difColor)
    def check(self,i,j):
        if(self.maps[i][j] != "."):
            return True
        else:
            return False
