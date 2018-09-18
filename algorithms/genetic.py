import random as rnd
import copy as cpy
from objects.board import Board


def maxFitnessFunction(board):
    knightPossibleMoves = 8
    queenPossibleMoves = 8
    bishopPossibleMoves = 4
    rookPossibleMoves = 4
    return (board.whiteKnight + board.blackKnight) * knightPossibleMoves + (board.whiteQueen + board.blackQueen) * queenPossibleMoves + (board.whiteBishop + board.blackBishop) * bishopPossibleMoves + (board.whiteRook + board.blackRook) * rookPossibleMoves

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
    return selectionPieces
            

def crossOver(pieces1,pieces2):
    idxSelection = rnd.randint(1, len(pieces1) - 1)
    part1 = selection(pieces1, 'left', idxSelection)
    part2 = selection(pieces2, 'right', idxSelection)
    result = []
    for leftSide in part1:
        result.append(leftSide)
    for rightSide in part2:
        result.append(rightSide)
    for leftSide in part1:
        for rightSide in part2:
            if (leftSide.x == rightSide.x and leftSide.y == rightSide.y):
                return []
    # print(result)
    return result

def mutation(pieces, maps):
    idxSelection = rnd.randint(0, len(pieces))
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
    tempMaps = cpy.deepcopy(maps)
    for piece in pieces:
        newX = rnd.randint(0,7)
        newY = rnd.randint(0,7)
        while(tempMaps[7 - newY][newX] != '.'):
            newX = rnd.randint(0,7)
            newY = rnd.randint(0,7)
        newY = 7 - newY
        piece.x = newX
        piece.y = newY
        tempMaps[piece.y][piece.x] = piece.getChar()
    return pieces

def genetic(board):
    nPopulation = 100
    population = []
    # print("temp")
    for i in range (nPopulation):
        temp = cpy.deepcopy(randAllPiece(board.pieces, board.maps))
        population.append([temp, countFitnessFunction(board, temp)])
    cleanPopulation = []
    population.sort(key=lambda x:x[1])
    # for i in range(len(population)):
    #     print("count")
    #     print(population[i][1])
    for individual in population:
        if (individual[1] > maxFitnessFunction(board)/2):
            cleanPopulation.append(individual)
    # print(cleanPopulation)
    cleanPopulation.sort(key=lambda x:x[1], reverse=True)
    # print("test")
    # print(cleanPopulation)
    nCleanPopulation = len(cleanPopulation)
    # child = [cleanPopulation[0][0]]
    for j in range(1000):
        if(cleanPopulation[0][1] != maxFitnessFunction(board)):
            # print("clean")
            for i in range(len(cleanPopulation)-1):
                if (i+1 < len(cleanPopulation)):
                    child = crossOver(cleanPopulation[i][0],cleanPopulation[i+1][0])
                    # print("anak",i)
                # else:
                #     child = crossOver(cleanPopulation[0][0],cleanPopulation[i][0])
                if (child != []):
                    board.update(child)
                    # board.show()
                    cleanPopulation.append([child, countFitnessFunction(board, child)])
            cleanPopulation.sort(key=lambda x:x[1], reverse=True)
            cleanPopulation = cleanPopulation[:nCleanPopulation]
            # cleanPopulation = cleanPopulation[:nCleanPopulation]
            # print("LIST POPULATION")
            # print(cleanPopulation)
        else:
            break
    print("Genetic Algorithm")
    board.update(cleanPopulation[0][0])
    print("Solution")
    board.show()    
