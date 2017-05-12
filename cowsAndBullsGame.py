#!/usr/bin/python
import random
#this program is to create the cows and bulls game for user

def game(userInput):
    numbers=range(0000,9999)
    randomNum=random.choice(numbers)
    randomNum=str(randomNum)
    randomNum=list(randomNum.split())
    #userInput=int(userInput)
    userInput=list(userInput)
    countCow=0
    countBull=0
    for i in range(len(randomNum)):
        for j in range(len(userInput)):
            if randomNum[i]==userInput[j]:
                countCow=countCow+1
            else:
                countBull=countBull+1

    print 'random num :' , ' '.join(randomNum)
    print 'Cow count :', countCow
    print 'Bull count :' ,countBull

    return countCow,countBull;

num=raw_input('Please guess 4 digit number :')

game(num)
               
