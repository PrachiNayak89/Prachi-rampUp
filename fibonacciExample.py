#!/usr/bin/python

#This is a program to generate the fibonacci series upto user input number

#defining the fibonac function

def fibonac(num):
    n1=0
    n2=1
    n3=0
    resultList=[]
    while num>n3:
        n3=n1+n2
        n1=n2
        n2=n3
        resultList.append(n1)
    print 'Fibonacci series upto', num,' number is :', resultList

userInputNumber=int(input('Please enter number to generate fibonacci series output :'))

fibonac(userInputNumber)  #calling the fibonac function
