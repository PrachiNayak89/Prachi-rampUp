#!/usr/bin/python

#this is loop example program

#while loop

num=int(raw_input("Kindly enter number :")) #ask input from user

count=1 #initialize the counter

while(count<=num):  #while condition
    print "Count is: ",count
    count+=1

print("Out from the loop")

#while loop with else 
count=0 #initialize counter again for another while loop
while(count<=num):
    print "Count is: ", count
    count+=2
else:
    print("you are out of the loop now!")

print("End of program!")

#for loop examples

print "\n\n"
print 'This is for loop example'
for letter in 'Python':
    print 'Current letter :', letter

fruitsList= ['mango','banana','avacado'] #make fruit list

for fruit in fruitsList:
    print 'Current fruit :',fruit
#iterating for by sequence index

print '\nIterating for loop by index'

for index in range(len(fruitsList)):
    print 'Current fruit :', fruitsList[index]

print 'End of Program!'
