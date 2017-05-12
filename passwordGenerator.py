#!/usr/bin/python
import random
import string
#This program will generate the strong password

def passwordGenerator(size):
    char=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
    generatedPw=(''.join((random.choice(char) for x in range(size))))

    print 'Generated password :', generatedPw
    return generatedPw;
userInput=None

while userInput!="exit":
    try:
        userInput=raw_input('Enter length of the password to be generated :')
        
        if userInput=='exit':
            break
        userInput=int(userInput)
        
        passwordGenerator(userInput) #calling the funcion
    
    except ValueError:
        print 'Please enter valid input!'



