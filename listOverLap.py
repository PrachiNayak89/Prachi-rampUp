#!/usr/bin/python


#This program is to find the overlap elements from two lists

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 13, 8, 9, 10, 11, 12, 13] 


resultList=[]
finalResult=[]

for i in a:
    for k in b:
        if i==k:
            resultList.append(i)
print 'Result list with duplicate values' , resultList

for j in resultList:
    if j not in finalResult:
        finalResult.append(j)
print 'Result list without duplicate values', finalResult

