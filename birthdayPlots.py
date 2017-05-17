#!/usr/bin/python

import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

with open("birthdayInfo.json", "r") as fileJson:
    fileData = json.load(fileJson)

months = []

for i in fileData:
    months.append(fileData[i].split("/")[0])

c = Counter(months)            #c is list containing the counts of birthdays in each month

data = {}

data["jan"]=c['01']
data["feb"]=c['02']
data["mar"]=c['03']
data["apr"]=c['04']
data["may"]=c['05']
data["jun"]=c['06']
data["jul"]=c['07']
data["aug"]=c['08']
data["sep"]=c['09']
data["oct"]=c['10']
data["nov"]=c['11']
data["dec"]=c['12']

output_file("birthdayPlot.html")

categories = []
count = []
for j in data.keys():
    categories.append(j)            #to store all month
    count.append(data[j])             #to store count in every month
    
x = categories
y = count

p = figure(x_range=categories)

p.vbar(x=x, top=y, width=0.5)

show(p)


