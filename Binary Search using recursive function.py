# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:26:42 2020

@author: Jino
"""

#3) Binary Search using recursive function
def bubblesort(l):
    l=[2,10,-3,8,6]
    length=len(l)
    for i in range(0,length-1):
        for j in range(0,length-1-i):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    print(l,"list after sorting through bubble sort")
    return l
def binarysearchR(L,s,low,high):      
    if low>=0 and high>=low:
        mid=(low+high)//2 #low+(high-low)//2
        if L[mid]==s:
            return mid
        elif s<L[mid]:
            return binarysearchR(L,s,low,mid-1)
        else:
            return binarysearchR(L,s,mid+1,high)
    else:
        return -1
#main starts here
L=[2,10,-3,8,6]
list_sorted=bubblesort(L)
s=int(input("Enter number to be searched: "))
out = binarysearchR( list_sorted , s , 0 , len(list_sorted)-1 )

if out==-1:
    print("Element searched is absent")
else:
    print("Element searched present at index", out)
    