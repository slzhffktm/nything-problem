import copy
import random as rnd
import numpy as np

def countHeatMap(board,piece, pieceChar,tempPieces):
        mapsDiiference =  np.zeros((8,8), dtype=np.int)
        # mapsMax =  np.zeros((8,8), dtype=np.int)
        for i in range(8):
            for j in range(8):
                if board.maps[i][j] != ".":
                    # dummy for imposible move
                    # mapsMin[i][j] = 999
                    # mapsMax[i][j] = -999
                    mapsDiiference[i][j] = 999
                else:
                    # insert pieceChart(Q,B,R,K) to maps
                    board.maps[i][j] = pieceChar
                    piece.x = j
                    piece.y = i
                    # insert new piece with new i and j to tempPieces
                    tempPieces.append(piece)
                    minValue, maxValue = board.countConflicts(tempPieces)
                    mapsDiiference[i][j] = minValue - maxValue
                    # remove again the new piece
                    tempPieces.remove(piece)
                    board.maps[i][j] = '.'
        return mapsDiiference


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
                # minHeatMap, maxHeatMap = countHeatMap(board, tempPiece, pieceChar, tempPieces)
                differenceHeatMap = countHeatMap(board, tempPiece, pieceChar, tempPieces)
                # get minimum value and maximum
                # minValue = minHeatMap.min()
                # maxValue = maxHeatMap.max()
                minValue = differenceHeatMap.min()
                # compare minValue and maxValue and choose the more benefit
                if((minValue) < (sameColor - difColor)):
                    moveToMin = True
                else:
                    moveToMin = False
                minIdx = []
                # maxIdx = []
                # find minimum index or maximum index
                for i in range(8):
                    for j in range(8):
                        if(moveToMin and differenceHeatMap[i][j] == minValue):
                            minIdx.append((j,i))
                            
                if not(minValue == sameColor):
                    # choice index from list of minimum index
                    # append minimum minimum value and index to be compared with other pieces
                    if(moveToMin):
                        newIdx = rnd.choice(minIdx)
                        piecesMovement.append([minValue,newIdx,piece])
                    # else:
                    #     newIdx = rnd.choice(maxIdx)
                    #     piecesMovement.append([maxValue - difColor,newIdx,piece])                  
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