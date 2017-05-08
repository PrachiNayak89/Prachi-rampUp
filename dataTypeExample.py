#!/usr/bin/python

#this program is all about better understanding for Python data types

#variable declaration

var1= 10 #this is integer type
var2= 10.008 #this is float type
var3= 18656L #this is long type
var4= 'string' #this is string type

#string data type examples
str="Hello World!"
print "String operations"
print str #print str
print str[0] # print str 1st location letter
print str[2:7] #print str 3rd to 7th location letters
print str[3:] #print str from 4th to end location letters
print str *2  #repeat the string twice
print str + "Test"  #concatinate the str with Test

#list datatype example

list=["string",10,100.87,"sentence check",'name'] #similar to arrayList
tinyList = [123,'word']
print("\n\n")
print "List operations"
print list[1] #print second element of list
print list[2:] #print from third to last element
print list[0:2] #print from first to second element
print tinyList *2 #print tinyList twice
print list + tinyList #concate list and tinyList

#tuples datatype example

tuple = ('abcd',123,"check sentence",1345L) #similar to array
tinyTuple= (987,'test')
print("\n\n")
print "Tuples operations"
print tuple #prints tuple
print tuple[0] #prints first element
print tuple[2:] #prints third to last elements
print tuple[1:3] #prints second to third elements
print tinyTuple *2 #prints tinyTuples twice
print tuple + tinyTuple  #concate tuples with tinyTuple

#Dictionary datatype example

dict = {} #create dictionary object
dict['one'] = "This is value for key one" #assign string key to value 
dict[2]="This is value for key 2" #assign integer key to value

tinyDict = {'name':'prachi','code':112157,'dept':"QA Automation"} #create dictionary

print("\n\n")
print "Dictionary operations"
print dict['one']  #prints dict for key 'one'
print dict[2] #prints dict for key 2
print tinyDict #prints tinyDict dictionary
print tinyDict['dept'] #prints value assigned to key dept
print tinyDict.keys() #prints keys for tinyDict dictionary
print tinyDict.values() #prints values for tinyDict dictionary


