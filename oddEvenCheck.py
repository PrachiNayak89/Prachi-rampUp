#!/usr/bin/python

#This program is to check whether the input number is odd or even

num=int(input('Please enter number to check if it is even or odd :'))

checkeven=num%2
checkFour=num%4

if checkeven==0:
    print '%d is even' % (num)
else:
    print '%d is odd' % (num)

if checkFour==0:
    print '%d is multiple of 4' % (num)
else:
    print '%d is not multiple of 4' % (num)

