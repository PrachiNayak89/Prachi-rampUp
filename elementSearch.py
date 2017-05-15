#!/usr/bin/python

#this program is for better understanding for binary search

a=[100,65,2,1,6,8,23,50,34,59]
a.sort()
print a

#binary serach logic

def binSearch(a_list,element):
    minimum=0
    maximum=len(a_list)-1

    while minimum<=maximum:
        middle=(minimum+maximum)//2

        if a_list[middle]==element:
            return True
        elif a_list[middle]<element:
            minimum=middle+1
        else:
            maximum=middle-1
    return False

print binSearch(a,9)
print binSearch(a,8)
