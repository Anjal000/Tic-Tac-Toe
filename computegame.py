import pattern
import wingame
import os
import computer

def compute(winner,playcomp):
    pattern.pattern(winner)
    i=0
    if(playcomp%2==0):
        current_player = 'X'
    else:
        current_player = 'O'
    
    while i!=9:
        win = wingame.check_winner(winner)
        if(win or wingame.draw(winner)):
            return win
        elif(not wingame.draw(winner)):
            if current_player == 'X':
                print("Computer's turn (X):")
                enter = computer.find_best_move(winner)
            else:
                print("Your turn (O):")
                enter=int(input())
        
            if (enter in range(1,10) and winner[enter]==enter):
                winner[enter] = current_player
                os.system('cls')
                pattern.pattern(winner)
                current_player = 'O' if current_player == 'X' else 'X'
                i+=1
            else:
                print("Invalid move! Try again.")
