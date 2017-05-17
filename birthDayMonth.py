#!/usr/bin/python
import json
from collections import Counter

#This program is for better understanding for json read and python Counter module

def readFromJson():
    with open("birthdayInfo.json","r") as fileJson:
        jsonData=fileJson.read()
        birthDayDict=json.loads(jsonData)
    return birthDayDict  

def createMonthList():
	bDict=readFromJson()
	months=[]
	for names in bDict:
		bdate=bDict[names]
		bdate=bdate.split('/')
		if int(bdate[0])==1:
			month="Jan"
		elif int(bdate[0])==2:
			month="Feb"
		elif int(bdate[0])==3:
			month="Mar"
		elif int(bdate[0])==4:
			month="Apr"
		elif int(bdate[0])==5:
			month="May"
		elif int(bdate[0])==6:
			month="June"
		elif int(bdate[0])==7:
			month="July"
		elif int(bdate[0])==8:
			month="Aug"
		elif int(bdate[0])==9:
			month="Sep"
		elif int(bdate[0])==10:
			month="Oct"
		elif int(bdate[0])==11:
			month="Nov"
		elif int(bdate[0])==12:
			month="Dec"
		months.append(month)
	#print months
        c=Counter(months)
        print 'Number of names born in particular months are :',c

if __name__=="__main__":
	createMonthList()


