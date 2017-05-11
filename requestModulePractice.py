#!/usr/bin/python

import requests

req=requests.get('https://github.com/timeline.json')
print req.text
print req.json
print'\n'
print type(req)
print req.status_code

#Store the website source code into simple text file

test=requests.get('https://www.hipstercode.com') #get the http page response

testFile= open("testSourceCode.txt","w+") #open the file to store the source code

test.encoding='ISO-8859-1'

testFile.write(str(test.text.encode('utf-8')))

testFile.close()

