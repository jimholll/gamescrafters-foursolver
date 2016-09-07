import four

def other(player):
    return 1 - player

def traverse(pos, player=0):
    #check to see if you've won/lost
    if four.primitive(pos) != "U" and player == 0:
        return "Win!"
    if four.primitive(pos) != "U" and player == 1:
        return -1
    
    #cycle through possible moves
    for i in four.gen_moves(pos):
        next_pos = four.do_move(i, pos)
        player = other(player)
        if traverse(next_pos, player) == -1:
            continue
        else:
            return traverse(next_pos,player)
        
    return "Lose"


            
            
            
            
        
    
