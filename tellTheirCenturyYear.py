#!/usr/bin/python
import datetime

#This is example program to tell the user to their century year by taking name and age as input


name=raw_input('Please enter your name :') #input name from user
age=int(input('How old are you? :')) #input age from user

now=datetime.datetime.now() #current date 
birthYear=int(now.year)-(age+1) #calculate birth year

centuryYear=birthYear+100 #calculate the year in which user will turn 100

print '%s birthyear is : %d' %(name,birthYear) #print user's birth year

print '%s will turn 100 in year %d' % (name,centuryYear) #print user's century year
