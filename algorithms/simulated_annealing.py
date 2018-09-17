from math import exp
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

    # else (ei >= e)
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
def SAdecreaseTemp(method, initial_temp, rate):
    if method == 1:
        return initial_temp - rate
    elif method == 2':
        return initial_temp*(100-rate)/100


"""
function to do movement for piece in simulated annealing
@board: Board
@piece: chess piece
"""
def SAMove(board, piece):
    piece_char = board.maps[piece.y][piece.x]   # get char from maps
    self.maps[piece.y][piece.x] = '.'   # delete piece from maps
    move = numpy.random.choice([0, 1, 2, 3, 4])
    try:
        if move == 1:
            


"""
function to solve nything-problem using simulated annealing
@board: Board
"""
def simulatedAnnealing(board):
    # choose decreasing method
    print('Decreasing method:')
    print('1. linear')
    print('2. log')
    method = input('Choose decreasing method (e.g. 1):')

    # input initial temperature
    print('Initial in degree (e.g. 1000):')

    # decreasing rate
    if method == 1:
        print('Decreasing rate in degree (e.g. 0.1):')
    else: # method == 2
        print('Decreasing rate in % (e.g. 0.1):')

    # start loop for solving nything
    while(True):
        temp_board = board.copy()   # save current board

        # move pieces
        for piece in board.pieces:
            
            
