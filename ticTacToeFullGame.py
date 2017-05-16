#!/usr/bin/python

#Full implementation of tic tac toe game

def drawBoard(gameBoard):
    print (' ' + str(gameBoard[0][0]) + ' | '+str(gameBoard[0][1])+ ' | '+str(gameBoard[0][2])+' ')
    print ('-'*11)
    print (' ' + str(gameBoard[1][0]) + ' | '+str(gameBoard[1][1])+ ' | '+str(gameBoard[1][2])+' ')
    print ('-'*11)
    print (' ' + str(gameBoard[2][0]) + ' | '+str(gameBoard[2][1])+ ' | '+str(gameBoard[2][2])+' ')

game=[[0,0,0],
      [0,0,0],
      [0,0,0]]

def userInput():
    game=[[0,0,0],
          [0,0,0],
          [0,0,0]]

    count=1
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
            drawBoard(game)
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
            drawBoard(game)
            count+=1

    return game;

def checkTheWinner(gameToBeChecked):
    for r in range(0,3):
        row=set([gameToBeChecked[r][0],gameToBeChecked[r][1],gameToBeChecked[r][2]])

        if len(row)==1 and gameToBeChecked[r][0]!=0:
            return gameToBeChecked[r][0]

    for c in range(0,3):
        col=set([gameToBeChecked[0][c],gameToBeChecked[1][c],gameToBeChecked[2][c]])

        if len(col)==1 and gameToBeChecked[0][c]!=0:
            return gameToBeChecked[0][c]

    diagonal1=set([gameToBeChecked[0][0],gameToBeChecked[1][1],gameToBeChecked[2][2]])
    diagonal2=set([gameToBeChecked[0][2],gameToBeChecked[1][1],gameToBeChecked[2][0]])

    if len(diagonal1)==1 or len(diagonal2)==1 and gameToBeChecked[1][1]!=0:
        return gameToBeChecked[1][1]


#Writing the main function
def main():
    user1count=0
    user2count=0
    answer="yes"
    while answer=="yes":
        try:
            game1=userInput()
            
            if checkTheWinner(game1)==1:
                print 'Player 1 won!'
                user1count+=1
            elif checkTheWinner(game1)==2:
                print 'Player 2 won!'
                user2count+=1

        except IndexError:
            print 'Please enter position index rows and col in 1 to 3 range'
            continue

        answer=raw_input('Do you want to play more? yes or no?')

    print 'Player 1 wins :'+str(user1count)+' matches and Player 2 wins :'+str(user2count)+' matches'

if __name__=='__main__':
    main()

