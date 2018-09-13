import random as rnd
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
                    elif(data[1] == "BISHOP"):
                        self.maps[x][y] = "B"
                    elif(data[1] == "ROOK"):
                        self.maps[x][y] = "R"
                    elif(data[1] == "QUEEN"):
                        self.maps[x][y] = "Q"
                elif(data[0] == "BLACK"):
                    if(data[1] == "KNIGHT"):
                        self.maps[x][y] = "k"
                    elif(data[1] == "BISHOP"):
                        self.maps[x][y] = "b"
                    elif(data[1] == "ROOK"):
                        self.maps[x][y] = "r"
                    elif(data[1] == "QUEEN"):
                        self.maps[x][y] = "q"
    # instance method
    def show(self):
        for i in range(8):
            for j in range(7,-1,-1):
                print(self.maps[i][j], end = "")
            print()

    def check(i,j):
        if(self.maps(i,j) != '.'):
            return true
        else
            return false
