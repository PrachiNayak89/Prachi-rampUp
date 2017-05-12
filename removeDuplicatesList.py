#!/usr/bin/python

#This program is for better understanding of list and set

#defining the remove duplicate function

def removeDuplicates(inputList):
    inputList=list(inputList.split())
    resultSet=set(inputList)
    resultSet=list(resultSet)
    print 'Output without duplicates :',resultSet
    return resultSet;

userInput=raw_input('Please enter list elements with space :')

removeDuplicates(userInput)  #calling the remove duplicates function

