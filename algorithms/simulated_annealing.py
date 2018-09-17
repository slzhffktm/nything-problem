from math import exp
from copy import deepcopy
import numpy
from objects.board import Board

# function that returns acceptance probability of simulated annealing
def SAProbability(e, ei, ti):
    return exp(-(e-ei)/ti)


# function that returns boolean:  acceptance of simulated annealing step
def SAAccept(e, ei, ti):
    if ei < e:
        # count probabilty
        probs = SAProbability(e, ei, ti)
        print(probs)
        return numpy.random.choice([False, True], p=[1-probs, probs])

    else: # (ei >= e)
        return True


"""
function to decrease temperature for simulated annealing
@method: decreasing method (1 == linear, 2 == log)
@initial_temp: initial temperature
@rate: decreasing rate
        linear: in degree
        log: in %
@return: final temperature
"""
def SADecreaseTemp(method, initial_temp, rate):
    if method == 1:
        return initial_temp - rate
    else:
        return initial_temp*(100-rate)/100


"""
function to do movement for piece in simulated annealing
@board: Board
@piece: chess piece
"""
def SAMove(board, piece):
    piece_char = board.maps[piece.y][piece.x]   # get char from maps
    board.maps[piece.y][piece.x] = '.'   # delete piece from maps
    move = numpy.random.choice([0, 1, 2, 3, 4])
    try:
        if move == 1:       # move right
            if not board.check(piece.x+1, piece.y):
                piece.x = piece.x + 1
        elif move == 2:     # move left
            if not board.check(piece.x-1, piece.y):
                piece.x = piece.x - 1
        elif move == 3:     # move up
            if not board.check(piece.x, piece.y+1):
                piece.y = piece.y + 1
        elif move == 4:     # move down
            if not board.check(piece.x, piece.y-1):
                piece.y = piece.y - 1
    except:
        pass
    board.maps[piece.y][piece.x] = piece_char


"""
function to solve nything-problem using simulated annealing
@board: Board
"""
def simulatedAnnealing(board):
    # choose decreasing method
    print('Decreasing method:')
    print('1. linear')
    print('2. log')
    method = int(input('Choose decreasing method (e.g. 1): '))

    # input initial temperature
    temperature = float(input('Initial in degree (e.g. 1000): '))

    # decreasing rate
    if method == 1:
        rate = float(input('Decreasing rate in degree (e.g. 0.1): '))
    else: # method == 2
        rate = float(input('Decreasing rate in % (e.g. 0.1): '))

    # start loop for solving nything
    while(True):
        old_pieces = deepcopy(board.pieces)
        old_maps = deepcopy(board.maps)

        # move pieces
        for i in range(len(board.pieces)):
            SAMove(board, board.pieces[i])
        
        e = board.countConflictsSameColor(board.pieces)
        print(e)
        ei = board.countConflictsSameColor(old_pieces)
        print(ei)
        accept = SAAccept(e, ei, temperature)
        
        if not accept:
            board.pieces = old_pieces
            board.maps = old_maps

        # decrease temperature
        temperature = SADecreaseTemp(method, temperature, rate)
        print(temperature)
        if temperature == 0:
            break

    board.show()