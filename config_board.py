neighbor_positions = {
    'a0': ['a3','b1','g0'],'g0': ['a0','g3'],
    'b1': ['a0','b3','f1','c2'],'f1': ['b1','f3'],
    'c2': ['b1','c3','e2'],'e2': ['c2','e3'],
    'a3': ['a0','a6','b3'],'b3': ['a3','b1','b5','c3'],'c3': ['b3','c2','c4'],'e3': ['e2','e4','f3'],'f3': ['e3','f1','f5','g3'],'g3': ['f3','g0','g6'],
    'c4': ['c3','d4'],'d4': ['c4','d5','e4'],'e4': ['d4','e3'],
    'b5': ['b3','d5'],'d5': ['b5','d4','d6','f5'],'f5': ['d5','f3'],
    'a6': ['a3','d6'],'d6': ['a6','d5','g6'],'g6': ['d6','g3']
}
board_position = dict(enumerate(neighbor_positions.keys()))
position_to_num = dict((v,k) for k,v in board_position.items())
