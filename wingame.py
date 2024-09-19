def check_winner(winner):
    for i in range(1,10,3):
        if(winner[i]==winner[i+1]==winner[i+2]):
            return winner[i]
    for i in range(1,4):
        if(winner[i]==winner[i+3]==winner[i+6]):
            return winner[i]
    if(winner[1]==winner[5]==winner[9]):
        return winner[1]
    elif(winner[3]==winner[5]==winner[7]):
        return winner[3]
    return 0

def draw(winner):
    for i in range(1,10):
        if(winner[i]==i):
            return 0
    return 1
