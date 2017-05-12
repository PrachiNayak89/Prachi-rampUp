#!/usr/bin/python

#This program is to reverse the sentance input by user


def reverseInputFun(userInput):
    userInput=list(userInput.split()) #converting string input to list
    reverseInput=userInput[::-1] #reverse the list elements
    reverseInput=" ".join(reverseInput) #converting reversed list elements into joint string output
    print 'Reverse sentence :',reverseInput
    return reverseInput;

inputSentence=raw_input('Please enter an sentence to reverse :')

reverseInputFun(inputSentence)  #calling the function
