import copy
from config_board import neighbor_positions,board_position, position_to_num
import os
import sys


class morrisGame:
    def __init__(self):
        self.numberOfPositionEvaluated = 0

    def run(self, state, method, *args):
        if state == 'opening':
            if method == 'minimax':
                #print('calling GenerateMovesOpening with Minimax')
                return self.MiniMax(self.GenerateMovesOpening, self.SEOpening, *args)
            else:
                #print('calling GenerateMovesOpening with AlphaBeta')
                return self.AlphaBeta(self.GenerateMovesOpening, self.SEOpening, *args)
        elif state == 'midgame' or state == 'endgame':
            if method == 'minimax':
                #print('calling GenerateMovesMidgameEndgame with Minimax')
                return self.MiniMax(self.GenerateMovesMidgameEndgame, self.StaticEstimate,*args)
            else:
                #print('calling GenerateMovesMidgameEndgame with AlphaBeta')
                return self.AlphaBeta(self.GenerateMovesMidgameEndgame, self.StaticEstimate, *args)
        else :
            raise Exception('Enter a correct state and method')

    def MiniMax(self, successor, staticFun, root, depth, isMaxStep):
        children = successor(root)
        bestchild = ''
        if depth == 0 or len(children) ==0 :
            return staticFun(root, children), root
        elif isMaxStep:
            v = float("-inf")
            for child in children:
                val, tempchild = self.MiniMax(successor, staticFun,child, depth-1, False)
                if val > v:
                    v = val
                    bestchild=child
            return v, bestchild
        elif not isMaxStep:
            v = float("inf")
            for child in children:
                val, tempchild = self.MiniMax(successor, staticFun,child, depth-1, True)
                if val < v:
                    v = val
                    bestchild=child
            return v, bestchild

    def blackMove(self, board):
        board = board.replace('B', '$')
        board = board.replace('W', 'B')
        board = board.replace('$', 'W')
        return board

    def AlphaBeta(self, successor, staticFun, root, depth, isMaxStep, alpha=None, beta=None):
        if alpha is None :
            alpha = float('-inf')
        if beta is None:
            beta = float('inf')
        bestchild = ''
        children = successor(root)
        if depth == 0 or len(children) == 0:
            val = staticFun(root, children)
            return val, root
        elif isMaxStep:
            for child in children:
                val, tempchild = self.AlphaBeta(successor, staticFun, child, depth-1, False, alpha, beta)
                if alpha < val:
                    alpha = val
                    bestchild = child
                if alpha >= beta:
                    break
            return alpha, bestchild
        elif not isMaxStep:
            for child in children:
                val, tempchild = self.AlphaBeta(successor, staticFun, child, depth-1, True, alpha, beta)
                if beta > val:
                    beta = val
                    bestchild = child
                if alpha >= beta:
                    break
            return beta, bestchild

    def printOutput(self, estimate, method):
        print("Positions evaluated by static estimation : {}".format(self.numberOfPositionEvaluated))
        print("{} Estimate : {}".format(method, estimate))

    def getBumberOfStaticEvaluation(self):
        return self.numberOfPositionEvaluated

    class Node:
        def __init__(self):
            self.position = None
            self.ply = 0
            self.minmax = ''

    def StaticEstimate(self, state, children):
        def SE_MidgameEndgamePos(numBlackPieces, numWhitePieces, numBlackMoves):
            if numBlackPieces <= 2:
                return 10000
            elif numWhitePieces <= 2:
                return -10000
            elif numBlackMoves== 0:
                return 10000
            else:
                return (1000*(numWhitePieces-numBlackPieces)-numBlackMoves)
        if state is None or state == '':
            return 0
        else:
            self.numberOfPositionEvaluated += 1
            numWhitePieces = state.count('W')
            numBlackPieces = state.count('B')
            L = children
            numBlackMoves = len(L)
            return SE_MidgameEndgamePos(numBlackPieces, numWhitePieces, numBlackMoves)

    def SEOpening(self, board, *args):
        self.numberOfPositionEvaluated += 1
        numWhitePieces = board.count('W')
        numBlackPieces = board.count('B')
        return numWhitePieces - numBlackPieces

    def GetNeighbors(self, position):
        if 0 <= position < 21:
            neighbors = neighbor_positions[board_position[position]]
            return [position_to_num[k] for k in neighbors]

    def closeMill(self, position,board):
        if 0 <= position < 21:
            return self.checkMill(position,board)

    def checkMill(self, position, b):
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

    def GenerateMove(self, board):
        L = []
        for index, value in enumerate(board):
            if value == 'W':
                n = self.GetNeighbors(index)
                for j in n:
                    if board[j] == 'x':
                        b = list(board)
                        b[index] = 'x'
                        b[j] = 'W'
                        if self.closeMill(j,b):
                            self.GenerateRemove(''.join(b),L)
                        else:
                            L.append(''.join(b))
        return L

    def GenerateRemove(self, board, List):
        for index, value in enumerate(board):
            if value == 'B':
                if not self.closeMill(index,board):
                    b = list(board)
                    b[index] = 'x'
                    List.append(''.join(b))
        if not List:
            List.append(board)

    def GenerateAdd(self, board):
        L = []
        for index, value in enumerate(board):
            if value == 'x':
                b = list(board)
                b[index] = 'W'
                if self.closeMill(index,b):
                    self.GenerateRemove(''.join(b),L)
                else:
                    L.append(''.join(b))
        return L

    def GenerateHopping(self, board):
        L = []
        for index, value in enumerate(board):
            if value == 'W':
                for index1, value1 in enumerate(board):
                    if value1 == 'x':
                        b = list(board)
                        b[index] = 'x'
                        b[index1] = 'W'
                        if self.closeMill(index1, b):
                            self.GenerateRemove(b, L)
                        else:
                            L.append(''.join(b))
        return L

    def GenerateMovesMidgameEndgame(self, board):
        if board.count('W') == 3:
            return self.GenerateHopping(board)
        else:
            return self.GenerateMove(board)


    def GenerateMovesOpening(self, board):
        return self.GenerateAdd(board)

