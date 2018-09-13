from piece import Piece

class Knight(Piece):
    def __init__(self,_x,_y,color):
        Piece.__init__(self,_x,_y,color)

    def attack(self, board):
        conflicts = 0
        if (self.x + 2 <= 7):
            if (self.y + 1 <= 7):
                if(board.check(self.x + 2, self.y + 1)):
                    conflicts += 1
            if(self.y - 1 >= 0):
                if(board.check(self.x + 2, self.y - 1)):
                    conflicts += 1
        if (self.x + 1 <= 7):
            if (self.y + 2 <= 7):
                if(board.check(self.x + 1, self.y + 2)):
                    conflicts += 1
            if(self.y - 2 >= 0):
                if(board.check(self.x + 1, self.y - 2)):
                    conflicts += 1
            
        if (self.x - 2 >= 0):
            if (self.y + 1 <= 7):
                if(board.check(self.x - 2, self.y + 1)):
                    conflicts += 1
            if(self.y - 1 >= 0):
                if(board.check(self.x - 2, self.y - 1)):
                    conflicts += 1
        if (self.x - 1 >= 0):
            if (self.y + 2 <= 7):
                if(board.check(self.x - 1, self.y + 2)):
                    conflicts += 1
            if(self.y - 2 >= 0):
                if(board.check(self.x - 1, self.y - 2)):
                    conflicts += 1
        
        return conflicts     
