#!/usr/bin/python
#This program is to verify the input number is prime or not

num =int(raw_input('Please enter the number :')) #take input from user

for i in range(2,num): #iterate factors for number to check not a prime number
    if num%i==0: #check first factor
        j=num/i  #check second factor
        print '%d equals %d*%d Hence %d is not a prime number' % (num,i,j,num)
        break

else:
    print num, 'is a prime number'
