import pattern
import wingame
import os

def player(winner,play):
    i=0
    pattern.pattern(winner)
    print("PLAYER 1: O")
    print("PLAYER 2: x")
    while(i!=9):
        if(play%2!=0):
            if(i%2==0):
                print("\nPLAYER 1: ")
            else:
                print("\nPLAYER 2: ")
        else:
            if(i%2==0):
                print("\nPLAYER 2: ")
            else:
                print("\nPLAYER 1: ")
                    
                    
        enter=int(input())
            
        if(winner[enter]!=enter):
            print("\nTry again\n")
        else:
            if(play%2!=0):
                if(i%2==0):
                    winner[enter]="O"
                else:
                    winner[enter]="X"
            else:
                if(i%2==0):
                    winner[enter]="X"
                else:
                    winner[enter]="O"
                    
            os.system('cls')        
            pattern.pattern(winner)

            win=wingame.check_winner(winner)

            if(win):
                return win             
            
        i+=1
