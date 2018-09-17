import copy
import random as rnd
import numpy as np

def countHeatMap(board,piece, pieceChar,tempPieces):
        mapsTemp =  np.zeros((8,8), dtype=np.int)
        for i in range(8):
            for j in range(8):
                if board.maps[i][j] != ".":
                    # dummy for imposible move
                    mapsTemp[i][j] = 999
                else:
                    # insert pieceChart(Q,B,R,K) to maps
                    board.maps[i][j] = pieceChar
                    piece.x = j
                    piece.y = i
                    # insert new piece with new i and j to tempPieces
                    tempPieces.append(piece)
                    mapsTemp[i][j] = board.countConflictsSameColor(tempPieces)
                    # remove again the new piece
                    tempPieces.remove(piece)
                    board.maps[i][j] = '.'
        return mapsTemp


def hillClimbing(board):
        tempPieces = board.pieces[:]
        isPieceMove = False
        while(not isPieceMove):
            # countMove counts move that happen on each iteration
            countMove = 0
            for piece in board.pieces:
                # delete piece from tempPieces list
                tempPieces.remove(piece)
                # get pieceChar from maps
                pieceChar = board.maps[piece.y][piece.x]
                # delete piece from maps
                board.maps[piece.y][piece.x] = '.'
                tempPiece = copy.deepcopy(piece)
                # create heat map
                heatMap = countHeatMap(board, tempPiece, pieceChar, tempPieces)
                # get minimum value
                minValue = heatMap.min()
                minIdx = []
                # find minimum index
                for i in range(8):
                    for j in range(8):
                        if(heatMap[i][j] == minValue):
                            minIdx.append((j,i))
                if not((piece.x, piece.y) in minIdx):
                    # choice index from list of minimum index
                    newIdx = rnd.choice(minIdx)
                    # place piece on minimum index
                    piece.x = newIdx[0]
                    piece.y = newIdx[1]
                    isPieceMove = True
                board.maps[piece.y][piece.x] = pieceChar
                tempPieces = board.pieces[:]
                # board.show()
        print("Hill Climbing")
        print("Solution:")
        board.show()