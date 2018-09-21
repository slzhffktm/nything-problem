from .piece import Piece

class Knight(Piece):
    def __init__(self,_x,_y,color):
        Piece.__init__(self,_x,_y,color)

    def attack(self, board):
        friendly_attack = 0  # count how many friend pieces can be attacked
        enemy_attack = 0     # count how many enemy pieces can be attacked

        # declare enemy color
        if self.color == 'w':
            enemy_color = 'b'
        else:
            enemy_color = 'w'

        if (self.x + 2 <= 7):
            if (self.y + 1 <= 7):
                if(board.check(self.x + 2, self.y + 1, self.color)):
                    friendly_attack += 1
                elif(board.check(self.x + 2, self.y + 1, enemy_color)):
                    enemy_attack += 1
            if(self.y - 1 >= 0):
                if(board.check(self.x + 2, self.y - 1, self.color)):
                    friendly_attack += 1
                elif(board.check(self.x + 2, self.y - 1, enemy_color)):
                    enemy_attack += 1
                
        if (self.x + 1 <= 7):
            if (self.y + 2 <= 7):
                if(board.check(self.x + 1, self.y + 2, self.color)):
                    friendly_attack += 1
                elif(board.check(self.x + 1, self.y + 2, enemy_color)):
                    enemy_attack += 1
            if(self.y - 2 >= 0):
                if(board.check(self.x + 1, self.y - 2, self.color)):
                    friendly_attack += 1
                elif(board.check(self.x + 1, self.y - 2, enemy_color)):
                    enemy_attack += 1
            
        if (self.x - 2 >= 0):
            if (self.y + 1 <= 7):
                if(board.check(self.x - 2, self.y + 1, self.color)):
                    friendly_attack += 1
                elif(board.check(self.x - 2, self.y + 1, enemy_color)):
                    enemy_attack += 1
            if(self.y - 1 >= 0):
                if(board.check(self.x - 2, self.y - 1, self.color)):
                    friendly_attack += 1
                elif(board.check(self.x - 2, self.y - 1, enemy_color)):
                    enemy_attack += 1
        if (self.x - 1 >= 0):
            if (self.y + 2 <= 7):
                if(board.check(self.x - 1, self.y + 2, self.color)):
                    friendly_attack += 1
                elif(board.check(self.x - 1, self.y + 2, enemy_color)):
                    enemy_attack += 1
            if(self.y - 2 >= 0):
                if(board.check(self.x - 1, self.y - 2, self.color)):
                    friendly_attack += 1
                if(board.check(self.x - 1, self.y - 2, enemy_color)):
                    enemy_attack += 1
        
        return friendly_attack, enemy_attack    


    def getChar(self):
        if self.color == 'w':
            return 'K'
        else:   # color == 'b'
            return 'k'