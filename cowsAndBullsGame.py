#!/usr/bin/python
import random
#this program is to create the cows and bulls game for user

def game(userInput,randomNum):
    randomNum=str(randomNum)
    userInput=str(userInput)
    countCowBull=[0,0]

    for i in range(len(randomNum)):
        if userInput[i] in randomNum:
            if randomNum[i]==userInput[i]:
                countCowBull[0]+=1
            else:
                countCowBull[1]+=1
    
    return countCowBull;

#generating random number
numbers=range(1000,9999)
randomNumber=random.choice(numbers)
print 'Random Numer',randomNumber
num=None
tries=0
while num!="exit":
    num=raw_input('Please guess 4 digit number :')

    if num=="exit":
        break
    tries+=1
    numConverted=int(num)

    if numConverted==randomNumber:
        print 'Whoohaa! you have guessed the correct number! You have tried ',tries,' times'
        break
    
    cowBull= game(num,randomNumber)

    print 'Cows :', cowBull[0]
    print 'Bulls :', cowBull[1]

