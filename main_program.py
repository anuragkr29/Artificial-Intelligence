import functions as fun
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
print("Result : " ,MiniMax('WxxxxxxxBxxxxxxxxxxxx',3,True))