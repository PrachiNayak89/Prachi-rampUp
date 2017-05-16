#!/usr/bin/python
import random

#This program is to better understand the concepts of file read write and random module

listToStore=[]
with open("sowpodsDictionary.txt","r") as fileToRead:
    line=fileToRead.readline().strip()
    while line:
        words=line
        listToStore.append(words)
        line=fileToRead.readline().strip()

    print 'Random string from SOWPODS Dictionary is :',random.choice(listToStore)
