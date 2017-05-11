#!/usr/bin/python

#This program is to find whether the entered string is pelindrome or not

inputString=raw_input('Please enter the string to check :')

reverseString=str(inputString[::-1])

print 'Reversed String :', reverseString

if inputString== reverseString:
    print 'Input is pelindrome'
else:
    print 'Input is not pelindrome'

