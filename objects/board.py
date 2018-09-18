import random as rnd
from .bishop import Bishop
from .knight import Knight
from .rook import Rook
from .queen import Queen

class Board:

    # Initializer / Instance Attributes
    def __init__(self):
        self.maps = []
        for i in range(8):
            self.maps.append(['.', '.', '.', '.', '.', '.', '.', '.'])
        self.pieces = []
        self.whiteRook = 0
        self.whiteQueen = 0
        self.whiteBishop = 0
        self.whiteKnight = 0
        self.blackQueen = 0
        self.blackRook = 0
        self.blackBishop = 0
        self.blackKnight = 0
        

    # instance method
    def readExternalFile(self):
        f = open("test.txt","r")
        inputPieces = f.read().split("\n")
        for data in inputPieces:
            data = data.split(" ")
            for j in range(int(data[2])):
                x = rnd.randint(0,7)
                y = rnd.randint(0,7)
                while(self.maps[7 - y][x] != '.'):
                    x = rnd.randint(0,7)
                    y = rnd.randint(0,7)
                y = 7 - y
                if(data[0] == "WHITE"):
                    if(data[1] == "KNIGHT"):
                        self.maps[y][x] = "K"
                        k = Knight(x,y,'w')
                        self.whiteKnight += 1
                        self.pieces.append(k)
                    elif(data[1] == "BISHOP"):
                        self.maps[y][x] = "B"
                        b = Bishop(x,y,'w')
                        self.whiteBishop += 1
                        self.pieces.append(b)
                    elif(data[1] == "ROOK"):
                        self.maps[y][x] = "R"
                        r = Rook(x,y,'w')
                        self.whiteRook += 1
                        self.pieces.append(r)
                    elif(data[1] == "QUEEN"):
                        self.maps[y][x] = "Q"
                        q = Queen(x,y,'w')
                        self.whiteQueen += 1
                        self.pieces.append(q)
                elif(data[0] == "BLACK"):
                    if(data[1] == "KNIGHT"):
                        self.maps[y][x] = "k"
                        k = Knight(x,y,'b')
                        self.blackKnight += 1
                        self.pieces.append(k)
                    elif(data[1] == "BISHOP"):
                        self.maps[y][x] = "b"
                        b = Bishop(x,y,'b')
                        self.blackBishop += 1
                        self.pieces.append(b)
                    elif(data[1] == "ROOK"):
                        self.maps[y][x] = "r"
                        r = Rook(x,y,'b')
                        self.blackRook += 1
                        self.pieces.append(r)
                    elif(data[1] == "QUEEN"):
                        self.maps[y][x] = "q"
                        q = Queen(x,y,'b')
                        self.blackQueen += 1
                        self.pieces.append(q)

    def show(self):
        for i in range(7,-1,-1):
            for j in range(8):
                print(self.maps[i][j], end = " ")
            print()
        self.countConflicts()

    def countConflictsSameColor(self):
        count = 0
        for piece in self.pieces:
            # print(piece.__class__.__name__, piece.x, piece.y, "att", piece.attack(self))
            count += piece.attack(self)
        return count
    
    def countConflicts(self):
        sameColor = self.countConflictsSameColor()
        difColor = 0
        print(sameColor," ",difColor)
    
    def check(self, j, i):
        if(self.maps[i][j] != "."):
            return True
        else:
            return False