import random as rnd
from objects.board import Board

global knightPossibleMoves = 8
global queenPossibleMoves = 8
global bishopPossibleMoves = 4
global rookPossibleMoves = 4

def maxFitnessFunction(board):
    return maxFitnessFunction = (board.whiteKnight + board.blackKnight) * knightPossibleMoves +
                                    (board.whiteQueen + board.blackQueen) * queenPossibleMoves +
                                    (board.whiteBishop + board.blackBishop) * bishopPossibleMoves +
                                    (board.whiteRook + board.blackRook) * rookPossibleMoves

def countFitnessFunction(board, pieces):
    conflict = board.countConflictsSameColor(pieces)
    return maxFitnessFunction(board) - conflict

def selection(pieces, side, idxSelection):
    selectionPieces = []
    if(side == 'left'):
        for i in range(idxSelection):
            selectionPieces.append(pieces[i])
    elif(side == 'right'):
        for i in range(idxSelection, len(pieces)):
            selectionPieces.append(pieces[i])
    return selectionBoard
            

def crossOver(pieces1,pieces2):
    idxSelection = rnd.randint(1, len(pieces1) - 1)
    part1 = selection(pieces1, 'left', idxSelection)
    part2 = selection(pieces2, 'right', idxSelection)
    result = []
    result.append(part1)
    result.append(part2)
    return result

def mutation(pieces, maps):
    idxSelection = rnd.randint(0, len(pieces1))
    newX = rnd.randint(0,7)
    newY = rnd.randint(0,7)
    while(maps[7 - newY][newX] != '.'):
        newX = rnd.randint(0,7)
        newY = rnd.randint(0,7)
    newY = 7 - newY
    pieces[idxSelection].x = newX
    pieces[idxSelection].y = newY
    return pieces

def randAllPiece(pieces, maps):
    for piece in pieces:
        newX = rnd.randint(0,7)
        newY = rnd.randint(0,7)
        while(maps[7 - newY][newX] != '.'):
            newX = rnd.randint(0,7)
            newY = rnd.randint(0,7)
        newY = 7 - newY
        piece.x = newX
        piece.y = newY
    return pieces

def genetic(board):
    nPopulation = 4
    population = []
    for i in range (nPopulation):
        temp = randAllPiece(board.pieces, board.maps)
        population.append([temp, countFitnessFunction(board, temp)])
    cleanPopulation = []
    for individual in population:
        if (individual[1] > maxFitnessFunction(board)/4):
            cleanPopulation.append(individual)
    cleanPopulation.sort(key=lambda x:x[1])
    for 
    
