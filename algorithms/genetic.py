import random as rnd

global knightPossibleMoves = 8
global queenPossibleMoves = 8
global bishopPossibleMoves = 4
global rookPossibleMoves = 4



def countFitnessFunction(board):
    maxFitnessFunction = (board.whiteKnight + board.blackKnight) * knightPossibleMoves +
                            (board.whiteQueen + board.blackQueen) * queenPossibleMoves +
                            (board.whiteBishop + board.blackBishop) * bishopPossibleMoves +
                            (board.whiteRook + board.blackRook) * rookPossibleMoves
    conflict = board.countConflictsSameColor()
    return maxFitnessFunction - conflict

def selection(board, side):
    idxSelection = rnd.randint(1,6)
    selectionBoard = []
    selection
    if(side == 'left'):
        for piece in board.pieces:
            if piece.x <= idxSelection:
                selectionPieces.append(piece)
            else:

    elif(side == 'right'):
         for piece in board.pieces:
            if piece.x > idxSelection:
                selectionPieces.append(piece)
            

def crossOver():

def mutation():