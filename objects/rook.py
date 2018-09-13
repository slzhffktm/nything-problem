from piece import Piece

class Rook(Piece):
    def __init__(self, x, y):
        super.__init__(x,y)

    def attack(self, board):
        conflicts = 0
        northwest = true
        southwest = true
        southeast = true
        northeast = true
        for i in range (1,7):
            if (northwest and (self.x + i <= 7) and (self.y + i <= 7)):
                if (board.check(self.x + i, self.y + i)):
                    conflicts += 1
            else:
                northwest = false
            
            if (southwest and (self.x + i <= 7) and (self.y - i <= 7)):
                if (board.check(self.x + i, self.y + i)):
                    conflicts += 1
            else:
                southwest = false
            
            if (southeast and (self.x - i <= 7) and (self.y - i <= 7)):
                if (board.check(self.x + i, self.y + i)):
                    conflicts += 1
            else:
                southeast = false
            
            if (northeast and (self.x - i <= 7) and (self.y + i <= 7)):
                if (board.check(self.x + i, self.y + i)):
                    conflicts += 1
            else:
                northeast = false
        return conflicts