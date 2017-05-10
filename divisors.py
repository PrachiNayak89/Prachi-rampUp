#!/usr/bin/python


#This program is to give list output for divisors for user input number
try:
    num =int(input('Please enter the number :'))

    result=[]

    for i in range(1,num+1):
        if num%i==0:
            result.append(i)

    print result

except NameError:
    print 'You have entered invalid input, kindly enter number next time'




