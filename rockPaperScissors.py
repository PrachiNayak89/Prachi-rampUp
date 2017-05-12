#!/usr/bin/python

#This program is to create a rock-paper-scissors game logic
user1Input=None
user2Input=None

def game(u1,u2): #defining the function

    if u1==u2:
        print 'Both made same choice, please enter again!'
    elif u1=='r' and u2=='s':
        print 'User 1 wins!'
    elif u1=='s' and u2=='r':
        print 'User 2 wins!'
    elif u1=='s' and u2=='p':
        print 'User 1 wins!'
    elif u1=='p' and u2=='s':
        print 'User 2 wins!'
    elif u1=='p' and u2=='r':
        print 'User 1 wins!'
    elif u1=='r' and u2=='p':
        print 'User 2 wins!'
    else:
        print 'Something wend wrong! Please enter valid input!'
    return u1,u2;

while user1Input!="exit" and user2Input!="exit":
    print '\nNote: r for Rock, s for scissors and p for paper. exit to quit game\n'

    user1Input=raw_input('Please enter choice for user 1 :')

    if user1Input=="exit":
        break

    user2Input=raw_input('Please enter choice for user 2 :')

    if user1Input=="exit":
        break

    game(user1Input,user2Input) #calling the function

