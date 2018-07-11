import copy
from config_board import neighbor_positions,board_position, position_to_num
import os
import sys

def run(state, method, *args):
    if state == 'opening':
        if method == 'minimax':
            print('calling GenerateMovesOpening with Minimax');
            return MiniMax(GenerateMovesOpening, SEOpening, *args),GenerateMovesOpening(args[0])
        else :
            print('calling GenerateMovesOpening with AlphaBeta');
            return AlphaBeta(GenerateMovesOpening, SEOpening,*args),GenerateMovesOpening(args[0])
    elif state == 'midgame' or state == 'endgame':
        if method == 'minimax':
            print('calling GenerateMovesMidgameEndgame with Minimax');
            return MiniMax(GenerateMovesMidgameEndgame, StaticEstimate,*args),GenerateMovesMidgameEndgame(args[0])
        else :
            print('calling GenerateMovesMidgameEndgame with AlphaBeta');
            return AlphaBeta(GenerateMovesMidgameEndgame, StaticEstimate, *args),GenerateMovesMidgameEndgame(args[0])
    else :
        raise Exception('Enter a correct state and method');
def MiniMax(successor, staticFun, root, depth, isMaxStep):
    children = successor(root)
    if depth == 0 or len(children) ==0 :
        return staticFun(root),root
    elif isMaxStep:
        v = float("-inf")
        for child in children:
            v = max(v,MiniMax(successor, staticFun,child, depth-1, False)[0])
        return v,child
    elif not isMaxStep:
        v = float("inf")
        for child in children:
            v = min(v,MiniMax(successor, staticFun,child, depth-1, True)[0])
        return v,child
def AlphaBeta(successor, staticFun, root, depth, isMaxStep, alpha=None, beta=None):
    if alpha is None :
        alpha = float('-inf')
    if beta is None:
        beta = float('inf')
    children = successor(root)
    if depth == 0 or len(children) ==0 :
        val= staticFun(root,children)
        return (val,root)
    elif isMaxStep:
        for child in children:
            alpha = max(alpha, AlphaBeta(successor, staticFun, child, depth-1, False, alpha, beta)[0])
            if alpha>= beta:
                break
        return (alpha,child)
    elif not isMaxStep:
        for child in children:
            beta = min(beta, AlphaBeta(successor, staticFun, child, depth-1, True, alpha, beta)[0])
            if alpha>= beta:
                break
        return (beta,child)
def getFileContent(fName):
    if os.path.exists(fName):
        with open(fName, 'r') as f:
            try:
                file_content = f.read()
                print("Input position   : {}".format(file_content))
                return file_content
            except : 
                print('Error opening the file')
                sys.exit()
            finally:
                f.close()

def writeToFile(fOut, file_content):
    try:
        with open(fOut, 'w') as dest:
            dest.write(file_content)
            print("Output position  : {}".format(file_content))
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        sys.exit()
    finally:
        dest.close()

class Node:
    def __init__(self):
        self.position = None
        self.ply = 0
        self.minmax = ''
class morrisGame:
    def __init__(self):
        self.state = 'xxxxxxxxxxxxxxxxxxxxx'
def StaticEstimate(state,children):
    def SE_MidgameEndgamePos(numBlackPieces, numWhitePieces, numBlackMoves):
        if numBlackPieces <= 2:
            return 10000
        elif numWhitePieces <= 2:
            return -10000
        elif numBlackMoves== 0:
            return 10000
        else :
            return (1000*(numWhitePieces-numBlackPieces)-numBlackMoves)
    if state is None or state == '':
        return 0
    else:
        numWhitePieces = state.count('W')
        numBlackPieces = state.count('B')
        L = children
        numBlackMoves = len(L)
        return SE_MidgameEndgamePos(numBlackPieces, numWhitePieces, numBlackMoves)



def SEOpening(board):
    numWhitePieces = board.count('W')
    numBlackPieces = board.count('B')
    return numWhitePieces - numBlackPieces

def GetNeighbors(position):
    if position >=0 and position <21:
        neighbors = neighbor_positions[board_position[position]]
        return [position_to_num[k] for k in neighbors]
def closeMill(position,board):
    if position >=0 and position <21:
        return checkMill(position,board)
def checkMill(position,b):
    C = b[position]
    if C=='x':
        return False
    return {
         0: (True if (b[6]==C and b[18]==C) or (b[2]==C and b[4]==C) else False),
         1: (True if (b[11]==C and b[20]==C) else False),
         2: (True if (b[0]==C  and b[4]==C) or (b[7]==C and b[15]==C) else False),
         3: (True if (b[10]==C and b[17]==C) else False),
         4: (True if (b[2]==C and b[0]==C) or (b[8]==C and b[12]==C) else False),
         5: (True if (b[9]==C and b[14]==C) else False),
         6: (True if (b[0]==C and b[18]==C) or (b[7]==C and b[8]==C) else False),
         7: (True if (b[6]==C and b[8]==C) or (b[2]==C and b[15]==C) else False),
         8: (True if (b[6]==C and b[7]==C) or (b[12]==C and b[4]==C)else False),
         9: (True if (b[5]==C and b[14]==C) or (b[10]==C and b[11]==C) else False),
        10: (True if (b[9]==C and b[1]==C) or (b[3]==C and b[17]==C) else False),
        11: (True if (b[10]==C and b[9]==C) or (b[1]==C and b[20]==C) else False),
        12: (True if (b[4]==C and b[8]==C) or (b[13]==C and b[14]==C) else False),
        13: (True if (b[12]==C and b[14]==C) or (b[16]==C and b[19]==C) else False),
        14: (True if (b[5]==C and b[9]==C) or (b[12]==C and b[13]==C) else False),
        15: (True if (b[2]==C and b[7]==C) or (b[16]==C and b[17]==C) else False),
        16: (True if (b[13]==C and b[19]==C) or (b[15]==C and b[17]==C) else False),
        17: (True if (b[3]==C and b[10]==C) or (b[15]==C and b[16]==C) else False),
        18: (True if (b[0]==C and b[6]==C) or (b[19]==C and b[20]==C) else False),
        19: (True if (b[13]==C and b[16]==C) or (b[18]==C and b[20]==C) else False),
        20: (True if (b[1]==C and b[11]==C) or (b[18]==C and b[19]==C) else False)
    }[position]   
def GenerateMove(board):
    L = []
    for index, value in enumerate(board):
        if value == 'W':
            n = GetNeighbors(index)
            for j in n:
                if board[j] == 'x':
                    b = list(board)
                    b[index] = 'x'
                    b[j] = 'W'
                    if closeMill(j,b):
                        GenerateRemove(''.join(b),L)
                    else:
                        L.append(''.join(b))
    return L
def GenerateRemove(board,List):
    for index, value in enumerate(board):
        if value == 'B':
            if not closeMill(index,board):
                b = list(board)
                b[index] = 'x'
                List.append(''.join(b))
    if not List:
        List.append(board)
def GenerateAdd(board):
    L = []
    for index, value in enumerate(board):
        if value == 'x':
            b = list(board)
            b[index] = 'W'
            if closeMill(index,b):
                GenerateRemove(''.join(b),L)
            else:
                L.append(''.join(b))
    return L
def GenerateHopping(board):
    L = []
    for index, value in enumerate(board):
        if value == 'W':
            for index1, value1 in enumerate(board):
                if value1 == 'x':
                    b = list(board)
                    b[index] = 'x'
                    b[index1] = 'W'
                    if closeMill(index1, b):
                        GenerateRemove(b, L)
                    else:
                        L.append(''.join(b))
    return L

def GenerateMovesMidgameEndgame(board):
    if board.count('W') == 3:
        return GenerateHopping(board)
    else:
        return GenerateMove(board)

def GenerateMovesOpening(board):
    return GenerateAdd(board)
    
