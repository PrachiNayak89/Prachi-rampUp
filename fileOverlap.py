#!/usr/bin/python

#Happy number generator

happy=[]

for i in range(1,1001):
    num=i
    l=[]
    s=0
    while not (s in l[:-1]) and s!=1:
        s=0
        for j in str(num):
            s+=int(j)**2

        l.append(s)
        num=s

    if l[-1]==1:
        happy.append(i)
#print happy 

#import happy number to file

#happyFile=open("happyFile.txt","w+")
#happyFile.write(str(happy))

#Prime number generator

prime=[]
for x in range(2,1001):
    if x>1:
        for y in range(2,x):
            if x%y==0:
                break
        else:
            prime.append(x)

#print prime

#import prime number to file

#primeFile=open("primeFile.txt","w+")
#primeFile.write(str(prime))


def listFromFile(fileName):
    fetchedList=[]

    with open(fileName) as f:
        fetchedList=f.read().split(',')

    return fetchedList;

primeList=listFromFile('primeFile.txt')
happyList=listFromFile('happyFile.txt')

#print primeList
#print happyList

overLapList=[]

for element in happyList:
    if element in primeList:
        overLapList.append(element)

print 'Overlap list result :', overLapList



