import functions as fun
import sys
def MiniMax(root, depth, isMaxStep):
    children = fun.GenerateMovesOpening(root)
    if depth == 0 or len(children) ==0 :
        return fun.SEOpening(root)
    elif isMaxStep:
        v = float("-inf")
        for child in children:
            v = max(v,MiniMax(child, depth-1, False))
        return v
    elif not isMaxStep:
        v = float("inf")
        for child in children:
            v = min(v,MiniMax(child, depth-1, True))
        return v
def alphabeta(root, depth, alpha, beta, isMaxStep):
    children = GenerateMovesOpening(root)
    if depth == 0 or len(children) ==0 :
        return SEOpening(root)
    elif isMaxStep:
        for child in children:
            alpha = max(alpha,alphabeta(child, depth-1,alpha, beta, False))
            if alpha>= beta:
                break
        return alpha
    elif not isMaxStep:
        for child in children:
            beta = min(beta,alphabeta(child, depth-1,alpha, beta, True))
            if alpha>= beta:
                break
        return beta

def main():
    args = (sys.argv)
    inputFile= str(args[1])
    outputFile= str(args[2])
    depth = int(args[3])
    try:
        root = fun.getFileContent(inputFile)
        child_branch= MiniMax(root,depth,True)
        children = fun.GenerateMovesOpening(root)
        fun.writeToFile(outputFile,children[child_branch])
    except Exception as e:
        print("An Error occured :",e)

if __name__ == "__main__":
	main()
