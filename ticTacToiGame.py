#!/usr/bin/python

#This program is to check the tic tac toe game logic implementation

def ticTacToe(game):

    for r in range(0,3):
        row=set([game[r][0],game[r][1],game[r][2]])

        if len(row)==1 and game[r][0]!=0:
            return game[r][0]

    for c in range(0,3):
        col=set([game[0][c],game[1][c],game[2][c]])

        if len(col)==1 and game[0][c]!=0:
            return game[0][c]

    diagonal1=set([game[0][0],game[1][1],game[2][2]])
    diagonal2=set([game[0][2],game[1][1],game[2][0]])

    if len(diagonal1)==1 or len(diagonal2)==1 and game[1][1]!=0:
        return game[1][1]

    return 0

#Different combinations

winner_is_1=[[1,2,0],
             [2,1,0],
             [2,1,1]]

winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]

#Calling the function

print 'Winner is player :', (ticTacToe(winner_is_1))
print 'Winner is player :', (ticTacToe(winner_is_2))
print 'Winner is player :', (ticTacToe(winner_is_also_1))
print 'Winner is player :', (ticTacToe(no_winner))
print 'Winner is player :', (ticTacToe(also_no_winner))
