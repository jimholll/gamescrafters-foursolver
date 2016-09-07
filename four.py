initial_position = 4

def primitive(pos):
    if pos == 0:
        return "L"
    else:
        return "U"

def do_move(action, pos):
    return pos - action

def gen_moves(pos):
    if pos == 0:
        return []
    elif pos == 1:
        return [1]
    elif pos > 1:
        return [1,2]
    else:
        return "?"


    
