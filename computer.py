import wingame


def minimax(winner, is_maximizing):
    win = wingame.check_winner(winner)
    
    if win == 'X':
        return 1
    elif win == 'O':
        return -1
    elif wingame.draw(winner):
        return 0
    
    if is_maximizing:
        best_score = -100
        for i in range(1,10):
            if winner[i]==i:
                winner[i] = 'X'
                score = minimax(winner, False)
                winner[i]=i
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 100
        for i in range(1,10):
            if winner[i]==i:
                winner[i] = 'O'
                score = minimax(winner, True)
                winner[i]=i
                best_score = min(score, best_score)
        return best_score


def find_best_move(winner):
    best_score = -100
    best_move = 0
    
    for i in range(1,10):
        if (winner[i]==i):
            winner[i] = 'X'
            score = minimax(winner, False)
            winner[i]=i
            if score > best_score:
                best_score = score
                best_move = i
    
    return best_move
