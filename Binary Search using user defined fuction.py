# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:05:36 2020

@author: Jino
"""

#2) Binary Search using user defined fuction
    
def bubblesort(l):
    length=len(l)
    for i in range(0,length-1):
        for j in range(0,length-1-i):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    print(l,"list after sorting through bubble sort")
    return l

def binarysearch(l):
    s=int(input("Enter number to be searched: "))
    low=0
    found=0
    high=len(l)-1
    for i in range(len(l)):
        mid=(low+high)//2
        if s>l[mid]:
            low=mid+1
        elif s<l[mid]:
            high=mid
        else:
            found+=1
            break
    if found>0:
        print("{} is present in list at index {} and position {}".format(s,mid,mid+1))
    else:
        print("{} not present in list".format(s)) 

l=[2,10,-3,8,6]
binarysearch(bubblesort(l))