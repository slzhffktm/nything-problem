import random as rnd
from objects.board import Board

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
    selectionBoard = Board()
    if(side == 'left'):
        for piece in board.pieces:
            if piece.x <= idxSelection:
                selectionBoard.pieces.append(piece)
                selectionBoard.maps[piece.y][piece.x]
    elif(side == 'right'):
         for piece in board.pieces:
            if piece.x > idxSelection:
                selectionBoard.pieces.append(piece)
                selectionBoard.maps[piece.y][piece.x]
    return board
            

def crossOver():

def mutation():