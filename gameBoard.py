#!/usr/bin/python

#This program is to create game board graphics as per user's input number

num=int(input('What size of gameboard you need? :'))

for index in range(num):
    print (" --- " * num)
    print ("|    " * (num+1))
print (" --- " * num) 
