#!/usr/bin/pyhton

#This program is for better understanging on lists comprehensive operations

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

bufferList= [i for i in a if i in b]

resultList= []

for j in bufferList:
    if j not in resultList:
        resultList.append(j)

print resultList
