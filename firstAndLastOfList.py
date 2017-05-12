#!/usr/bin/python

#This program is to find the first and last element of the list from the user input elements
def inputList(bufferInput):
    listInput= list(bufferInput.split())
    newList=[]
    for elements in listInput:
        elements=int(elements)
        newList.append(elements)
    print 'Entered input list befor converting to integer :',listInput
    print 'Input list after converting into integer numbers :',newList

    print 'First element of list is :',newList[0]
    print 'Last element of List is :',newList[-1]
    return newList;
try:
    inputListInput=raw_input('Please enter series of numbers using the space :')
    inputList(inputListInput) #calling the function
except ValueError:
    print 'Not a valid input for list. Kindly add numbers only'


