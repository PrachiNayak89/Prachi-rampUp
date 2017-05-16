#!/usr/bin/python

#This program is to take the user input for the game 

#default board

game=[[0,0,0],
      [0,0,0],
      [0,0,0]]

print game
count=1
#1 for player 1 and 2 for player 2
userInput1=None
userInput2=None
while True and userInput1!="exit" and userInput2!="exit":
    
    if count%2!=0:
        userInput1=raw_input('Player 1 please enter row <space> col for number in position :')
        if userInput1=="exit":
            break
        rowCol=userInput1.split(" ")
        row=int(rowCol[0])
        col=int(rowCol[1])
        row-=1
        col-=1
    
        if game[row][col]==0:
            game[row][col]=1
        else:
            print 'Already filled position!'
            continue
        print game
        count+=1
    
    if count==10:
        break

    if count%2==0:
        userInput2=raw_input('Player 2 please enter row <space> col for number in position :')
        if userInput2=="exit":
            break
        rowCol=userInput2.split(" ")
        row=int(rowCol[0])
        col=int(rowCol[1])
        row-=1
        col-=1

        if game[row][col]==0:
            game[row][col]=2
        else:
            print 'Already filled position!'
            continue
        print game
        count+=1

