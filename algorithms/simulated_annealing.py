from math import exp
from copy import deepcopy
import numpy
# from objects.board import Board

# function that returns acceptance probability of simulated annealing
def SAProbability(e, ei, ti):
    return exp(-(e-ei)/ti)


"""
function that returns boolean:  acceptance of simulated annealing step
@board: new board that has been moved
@old_board: board before moved
@ti: temperature
"""
def SAAccept(board, old_board, ti):
    # count conflicts
    new_conf_same_color, new_conf_diff_color = board.countConflicts(board.pieces)
    old_conf_same_color, old_conf_diff_color = old_board.countConflicts(old_board.pieces)

    delta_same_color = old_conf_same_color - new_conf_same_color
    delta_diff_color = new_conf_diff_color - old_conf_diff_color

    if delta_same_color > delta_diff_color:
        if old_conf_same_color < new_conf_same_color:
            # count probability
            probs = SAProbability(new_conf_same_color, old_conf_same_color, ti)
        else:
            return True

    else:
        if old_conf_diff_color > new_conf_diff_color:
            # count probability
            probs = SAProbability(old_conf_diff_color, new_conf_diff_color, ti)
        else:
            return True
        
    return numpy.random.choice([False, True], p=[1-probs, probs])


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
            if not board.check(piece.x+1, piece.y, 'w') and not board.check(piece.x+1, piece.y, 'b'):
                piece.x = piece.x + 1
        elif move == 2:     # move left
            if not board.check(piece.x-1, piece.y, 'w') and not board.check(piece.x-1, piece.y, 'b'):
                piece.x = piece.x - 1
        elif move == 3:     # move up
            if not board.check(piece.x, piece.y+1, 'w') and not board.check(piece.x, piece.y+1, 'b'):
                piece.y = piece.y + 1
        elif move == 4:     # move down
            if not board.check(piece.x, piece.y-1, 'w') and not board.check(piece.x, piece.y-1, 'b'):
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
    attempt = 0     # count stucked attempt
    best_conf = deepcopy(board)
    while(True):
        old_board = deepcopy(board)

        # move pieces
        for i in range(len(board.pieces)):
            SAMove(board, board.pieces[i])

        accept = SAAccept(board, old_board, temperature)

        # save best board        
        new_conf_same_color, new_conf_diff_color = board.countConflicts(board.pieces)
        best_conf_same_color, best_conf_diff_color = best_conf.countConflicts(best_conf.pieces)

        if new_conf_diff_color-new_conf_same_color > best_conf_diff_color-best_conf_same_color:
            best_conf = deepcopy(board)

        if not accept:
            board = old_board
            attempt += 1
        else:
            attempt = 0

        if attempt == 10:
            board = best_conf
            break

        # decrease temperature
        temperature = SADecreaseTemp(method, temperature, rate)
    
        if temperature <= 0:
            board = best_conf
            break

    board.show()
