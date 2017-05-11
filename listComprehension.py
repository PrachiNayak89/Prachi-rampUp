#!/usr/bin/python

#This program is to know more about List Comprehension

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print a

resultList=[element for element in a if element%2==0]

print resultList
