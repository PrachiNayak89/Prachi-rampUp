#!/usr/bin/python

myList = [1,1,16,8,9,67,100,5,4,2,9,4,3,7,10]

num= int(input('Choose a number :'))

updatedList = [] #create empty list to store the result

for elements in myList:
    if elements<=num:
        updatedList.append(elements)

print updatedList #print results 


