#!/usr/bin/python

#This program is for better understanding of dictionary objects 

birthDayDictionary={"Prachi":"11/03/1991",
                    "Mitul":"05/03/1990"}

print 'Welcome to Birthday dictionary! We know the birthdays of:'
for names in birthDayDictionary:
    print names

print 'Who\'s birthday fo you want to know?'

userInput=raw_input('Name :')

if userInput in birthDayDictionary:
    print ('{} \'s birthday is {}.'.format(userInput,birthDayDictionary[userInput]))

else:
    print ('Sorry we don\'t have {} \'s birthday in Birthday Dictionary.'.format(userInput))
