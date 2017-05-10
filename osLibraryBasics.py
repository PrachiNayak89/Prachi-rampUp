#!/usr/bin/python
import os

#Introductory program for python OS library/module

print os.getcwd() #get current working directory data

print 'Files in current directory: %s ' % (os.listdir(os.getcwd()))

os.mkdir("newFolder") #create new directory

print 'Files in current directory after creating new dir newFolder: %s '%(os.listdir(os.getcwd()))

os.chdir("/home/prachi/gitHub/Prachi-rampUp/newFolder") #change current directory to new directory

print os.getcwd() 

os.chdir("/home/prachi/gitHub/Prachi-rampUp") #change to previous directory

os.rmdir("newFolder") #remove new directory

print 'Files in current directory after deleting the newly created dir newFolder: %s '%(os.listdir(os.getcwd()))


