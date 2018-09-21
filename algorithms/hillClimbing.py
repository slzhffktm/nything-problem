import copy
import random as rnd
import numpy as np

def countHeatMap(board,piece, pieceChar,tempPieces):
        mapsMin =  np.zeros((8,8), dtype=np.int)
        mapsMax =  np.zeros((8,8), dtype=np.int)
        for i in range(8):
            for j in range(8):
                if board.maps[i][j] != ".":
                    # dummy for imposible move
                    mapsMin[i][j] = 999
                    mapsMax[i][j] = -999
                else:
                    # insert pieceChart(Q,B,R,K) to maps
                    board.maps[i][j] = pieceChar
                    piece.x = j
                    piece.y = i
                    # insert new piece with new i and j to tempPieces
                    tempPieces.append(piece)
                    mapsMin[i][j], mapsMax[i][j] = board.countConflicts(tempPieces)
                    # remove again the new piece
                    tempPieces.remove(piece)
                    board.maps[i][j] = '.'
        return mapsMin, mapsMax


def hillClimbing(board):
        tempPieces = board.pieces[:]
        isPieceMove = True
        while(isPieceMove):
            # countMove counts move that happen on each iteration
            countMove = 0
            piecesMovement = []
            sameColor, difColor = board.countConflicts(board.pieces)
            for piece in board.pieces:
                # delete piece from tempPieces list
                tempPieces.remove(piece)
                # get pieceChar from maps
                pieceChar = board.maps[piece.y][piece.x]
                # delete piece from maps
                board.maps[piece.y][piece.x] = '.'
                tempPiece = copy.deepcopy(piece)
                # create heat map for minimum and maximum
                minHeatMap, maxHeatMap = countHeatMap(board, tempPiece, pieceChar, tempPieces)
                # get minimum value and maximum
                minValue = minHeatMap.min()
                maxValue = maxHeatMap.max()
                # compare minValue and maxValue and choose the more benefit
                if((sameColor - minValue) > (difColor - maxValue)):
                    moveToMin = True
                    moveToMax = False
                    maxValue = -999
                else:
                    moveToMax = True
                    moveToMin = False
                    minValue = 999
                minIdx = []
                maxIdx = []
                # find minimum index or maximum index
                for i in range(8):
                    for j in range(8):
                        if(moveToMin and minHeatMap[i][j] == minValue):
                            minIdx.append((j,i))
                        if(moveToMax and maxHeatMap[i][j] == maxValue):
                            maxIdx.append((j,i))
                if not(minValue == sameColor or maxValue == difColor):
                    # choice index from list of minimum index
                    # append minimum minimum value and index to be compared with other pieces
                    if(moveToMin):
                        newIdx = rnd.choice(minIdx)
                        piecesMovement.append([sameColor - minValue,newIdx,piece])
                    else:
                        newIdx = rnd.choice(maxIdx)
                        piecesMovement.append([difColor - maxValue,newIdx,piece])                  
                    isPieceMove = True
                board.maps[piece.y][piece.x] = pieceChar
                tempPieces = board.pieces[:]
                
            #choosing the best piece movement
            if (piecesMovement != []):
                piecesMovement.sort(key=lambda x:x[0], reverse = True)
                piecePosition = piecesMovement[0][1]
                pieceIndex = board.pieces.index(piecesMovement[0][2])
                board.pieces[pieceIndex].x = piecePosition[0]
                board.pieces[pieceIndex].y = piecePosition[1]
                board.update(board.pieces)
            else:
                isPieceMove = False
        print("Hill Climbing")
        print("Solution:")
        board.show()