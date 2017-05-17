#!/usr/bin/python
import json

#This program is for better understanding of the import from json file and export into json file

def readFromJson():
    with open("birthdayInfo.json","r") as fileJson:
        jsonData=fileJson.read()
        birthDayDict=json.loads(jsonData)
    return birthDayDict                


def writeToJson(birthdayDict):
    with open("birthdayInfo.json","w") as fileJson:
        json.dump(birthdayDict,fileJson)


def displayBirthday():

    #Read from json file and store dictionary object into the variiable
    birthDayDictionary=readFromJson()

    print 'Welcome to Birthday dictionary! We know the birthdays of:'
    for names in birthDayDictionary:
    	print names

    print 'Who\'s birthday fo you want to know?'
    userIn=raw_input('Name :')


    if userIn in birthDayDictionary:
    	print ('{}\'s birthday is {}.'.format(userIn,birthDayDictionary[userIn]))

    else:
	print ('Sorry we don\'t have {}\'s birthday in Birthday Dictionary.'.format(userIn))
        userInput=raw_input('\nDo you want to add the name and birthday of this person? enter yes or no :')

        if userInput=="no" or userInput=="No":
            return False

        if userInput=="yes" or "Yes":
            day=raw_input('Please enter date in mm/dd/yyyy format :')
            birthDayDictionary[userIn]=day
	    print birthDayDictionary
            #Write to json file and store the new key value entry into the json file format
            writeToJson(birthDayDictionary)

                 
if __name__=="__main__":
    answer="continue"
    while True and answer!="exit":
        displayBirthday()
        answer=raw_input('Do you want to continue Dictionary program? Enter continue or exit :')
        if answer=="continue":
            continue
        if answer=="exit":
            break
