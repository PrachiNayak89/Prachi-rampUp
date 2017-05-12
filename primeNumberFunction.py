#!/usr/bin/python

#Practice the function for reusable functions and modularity of program

#defining the prime number function

def primeNumber(num):
    for i in range(2,num):
        if num%i==0:
            j=num/i
            print ('%d * %d is %d, hence %d is not prime number!') % (i,j,num,num)
            break
    else:
        print ('%d is prime number!') % (num)
    return num;

#calling the function
userInput=None
while userInput!="exit":
    try:
        userInput=raw_input('Enter number to check the primality:, enter exit to quit :')
        if userInput=="exit":
            break
        
        userInput=int(userInput) #converting the input type from string to integer

        primeNumber(userInput) #calling the prime logic function

    except ValueError:
        print '\nPlease enter valid integer value!'

