import random as rnd
from .bishop import Bishop
from .knight import Knight
from .rook import Rook
from .queen import Queen
import numpy as np
import copy

class Board:
    # Class Attribute
    maps = []
    pieces = []
    # Initializer / Instance Attributes
    def __init__(self):
        for i in range(8):
            self.maps.append(['.', '.', '.', '.', '.', '.', '.', '.'])
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
                        self.pieces.append(k)
                    elif(data[1] == "BISHOP"):
                        self.maps[y][x] = "B"
                        b = Bishop(x,y,'w')
                        self.pieces.append(b)
                    elif(data[1] == "ROOK"):
                        self.maps[y][x] = "R"
                        r = Rook(x,y,'w')
                        self.pieces.append(r)
                    elif(data[1] == "QUEEN"):
                        self.maps[y][x] = "Q"
                        q = Queen(x,y,'w')
                        self.pieces.append(q)
                elif(data[0] == "BLACK"):
                    if(data[1] == "KNIGHT"):
                        self.maps[y][x] = "k"
                        k = Knight(x,y,'b')
                        self.pieces.append(k)
                    elif(data[1] == "BISHOP"):
                        self.maps[y][x] = "b"
                        b = Bishop(x,y,'b')
                        self.pieces.append(b)
                    elif(data[1] == "ROOK"):
                        self.maps[y][x] = "r"
                        r = Rook(x,y,'b')
                        self.pieces.append(r)
                    elif(data[1] == "QUEEN"):
                        self.maps[y][x] = "q"
                        q = Queen(x,y,'b')
                        self.pieces.append(q)

    # instance method
    def show(self):
        for i in range(7,-1,-1):
            for j in range(8):
                print(self.maps[i][j], end = " ")
            print()
        self.countConflicts()

    def countConflictsSameColor(self, pieces):
        count = 0
        for piece in pieces:
            # print(piece.__class__.__name__, piece.x, piece.y, "att", piece.attack(self))
            count += piece.attack(self)
        return count
    
    def countConflicts(self):
        sameColor = self.countConflictsSameColor(self.pieces)
        difColor = 0
        print(sameColor," ",difColor)
    
    def check(self, j, i):
        if(self.maps[i][j] != "."):
            return True
        else:
            return False

    def countHeatMap(self,piece, pieceChar,tempPieces):
        mapsTemp =  np.zeros((8,8), dtype=np.int)
        for i in range(8):
            for j in range(8):
                if self.maps[i][j] != ".":
                    mapsTemp[i][j] = 99
                else:
                    self.maps[i][j] = pieceChar
                    piece.x = j
                    piece.y = i
                    tempPieces.append(piece)
                    mapsTemp[i][j] = self.countConflictsSameColor(tempPieces)
                    tempPieces.remove(piece)
                    self.maps[i][j] = '.'
        return mapsTemp

    def hillClimbing(self):
        tempPieces = self.pieces[:]
        while(True):
            countMove = 0
            for piece in self.pieces:
                tempPieces.remove(piece)
                pieceChar = self.maps[piece.y][piece.x]
                self.maps[piece.y][piece.x] = '.'
                # print(piece.__class__.__name__)
                # print(piece.x," ",piece.y)
                tempPiece = copy.deepcopy(piece)
                heatMap = self.countHeatMap(tempPiece,pieceChar,tempPieces)
                minValue = heatMap.min()
                # find minimum index
                minIdx = []
                for i in range(8):
                    for j in range(8):
                        if(heatMap[i][j] == minValue):
                            minIdx.append((j,i))
                if not((piece.x, piece.y) in minIdx):
                    newIdx = rnd.choice(minIdx)
                    # print(newIdx)
                    # place piece on minimum index
                    piece.x = newIdx[0]
                    piece.y = newIdx[1]
                    countMove += 1
                self.maps[piece.y][piece.x] = pieceChar
                tempPieces = self.pieces[:]
                # self.show()
            if(countMove == 0):
                break
        print("Hill Climbing")
        print("Solution:")
        self.show()
