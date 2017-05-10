#!/usr/bin/python
import json

#This is to practice the JSON library operations with python

#Reading the json and converting the data into python object with loads() function

jsonData = '{"name":"Prachi", "age":25}'  #JSON data in simple text format
jsonToPython = json.loads(jsonData)       #convert the JSON data into python object jsonToPython

print 'Print the json data to python dictionary :', jsonToPython
print 'Print the python object from jason file :',jsonToPython['name']

#Converting python dictionary data to json format
pythonDictionary = {'name':'Mitul', 'age':27}   #Pyhton dictionary data
dictionaryToJson = json.dumps(pythonDictionary) #convert python dictionary object to json format

print 'Print the python dictionary to json format :',dictionaryToJson

#try defining the default method with type conversion default method

class User(object): #create a class to store the python dictionary for username and passwords
    def __init__(self,name,password):  #defining function for class
        self.name=name
        self.password=password

#Defining the default method to convert data into json format
def jsonDefault(o):
    return o.__dict__

prachi=User('Prachi','wontTell1')
mitul=User('Mitul','willNotTell2')

print json.dumps(prachi, default=jsonDefault) #print the user prachi's data into json format
print json.dumps(mitul, default=jsonDefault) #print the user mitul's data into json fromat









