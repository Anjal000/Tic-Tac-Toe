import os
import pattern
import computer
import wingame
import players
import computegame
    
choice=1
play=0
playcomp=0
win1=0
win2=0
winn=0
comp=0
while(choice!=0):
    winner={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
    if(playcomp>0):
            print("Game played: ",playcomp)
            print("Player won: ",winn)
            print("Computer won: ",comp)
    if(play>0):
            print("Game played: ",play)
            print("Player 1 won: ",win1)
            print("Player 2 won: ",win2)
    
    if(play>0 or playcomp>0):
        print("\nWant to play(Yes(1)/No(0))")
        choice=int(input())
        
    if(choice):
        print("1.PLAYER V/S PLAYER")
        print("2.PLAYER V/S COMPUTER")
        choice=int(input())
        
        
    if(choice==1):
        playcomp=0
        play+=1
        win=players.player(winner,play)
        if(win):
            if(win=='X'):
                print("Player 2 wins")
                win2+=1
            elif(win=='O'):
                print("Player 1 wins")
                win1+=1
        if wingame.draw(winner):
            print("It's a draw!")
    
    elif(choice==2):
        playcomp+=1
        play=0
        win=computegame.compute(winner,playcomp)
        if win:
            if(win=='X'):
                comp+=1
                print("Computer wins!")
            elif(win=='O'):
                winn+=1
                print("Player wins!")
        
        if wingame.draw(winner):
            print("It's a draw!")
        
            


print("\nThank you for playing")
