#!/usr/bin/python
import random

#This program is for better understanding for binary search where user will tell the system correct guessed number which has been guessed by system 

minimumNum=0
maximumNum=100

sysNumber=random.randint(minimumNum,maximumNum)
count=1
answer=None

while True and answer!="exit":
    print "Is Guessed Num %d ?"% sysNumber
    answer=raw_input('Answer :')
    if answer=="exit":
        break

    if "lower" in answer.lower():
        sysNumber=sysNumber-random.randint(1,4)
    elif "higher" in answer.lower():
        sysNumber=sysNumber+random.randint(1,4)
    elif answer.lower()=="no":
        answer=raw_input('higher or lower? :')

        if answer.lower()=="higher":
            sysNumber=sysNumber+random.randint(1,4)
        elif answer.lower()=="lower":
            sysNumber=sysNumber-random.randint(1,4)
    elif answer.lower()=="yes":
        print "System took %d tries to find correct guessed number"%count
        break
    count+=1

