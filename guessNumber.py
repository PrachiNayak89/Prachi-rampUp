#!/usr/bin/python
import random

#This program is to find the guess number from user and give output

num = random.randint(1,9)
count=0
userInput=None

while userInput != num and userInput != "exit":
    try:
        userInput= raw_input('Please guess the number between 1 to 9 :')
        count+=1        
        if count==3:
            print 'Maximum 3 tries allowed! Correct number was: ', num
            break

        if userInput=="exit":
            break
        #print 'Random number :', num
        #print 'Guessed number :' , userInput

        userInput=int(userInput)

        if userInput>num:
            print 'You have guessed higher value,Try again!'
        elif userInput<num:
            print 'You have guessed lower value, Try again!'
        elif userInput==num:
            print 'Wow! You have guessed exact number! Bravo!'
        else:
            print 'Invalid input! Please try again'


    except ValueError:
        print 'Invalid input! Please enter numeber between 1 to 9'

#print 'You have guessed number exact %d times!'% (count)




