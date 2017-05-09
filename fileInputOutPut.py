#!/usr/bin/python

import os

#print os.getcwd()

try:
    fTest=open("test.txt","r+")  #open a new file 

    print 'Permissions for file :', fTest.mode
    print 'File name :', fTest.name
    print 'Closed or not :',fTest.closed
    print 'Softspace flag :' , fTest.softspace

    #write in the file 

    fTest.write("This is the first line of the file \n This is second line of the file")

    fTest.seek(0,0); #changing position to initial

    #Read from file
    str=fTest.read(10);

    print "Read string from file :", str

    fTest.close() #close the file

    print 'Closed or not: ' , fTest.closed

except IOError:
    print "You have no permissions to read the file"

finally:
    print "Finally runs everytime errespective of exception"

