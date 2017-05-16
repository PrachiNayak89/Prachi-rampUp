#!/usr/bin/python

#This program is to find the maximum out of three numbers which has been input by user

def maxOfThree(userInput):

    nums=userInput.split(" ")
    num1=int(nums[0])
    num2=int(nums[1])
    num3=int(nums[2])

    if num1>num2:
        if num1>num3:
            print 'Max num is :',num1
        else:
            print 'Max num is :',num3

    else:
        if num2>num3:
            print 'Max num is :',num2
        else:
            print 'Max num is :',num3

if __name__=='__main__':
    inputFromUser=None
    while True and inputFromUser!="exit":
        try:
            inputFromUser=raw_input('Please enter three numbers with <space> to check max out of them. Enter exit to quit :')
            if inputFromUser=="exit":
                break
            maxOfThree(inputFromUser)
        except ValueError:
            print 'Invalid input! Please enter integer values only.'
            continue
