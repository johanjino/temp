# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:33:06 2020

@author: Jino
"""
#1) Binary Search

l=[1,1,1,1,1,4,32,4,9,5,9]
length=len(l)
for i in range(0,length-1):
    for j in range(0,length-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l,"list after sorting through bubble sort")

s=int(input("Enter number to be searched: "))
low=0
found=0
high=len(l)-1
for i in range(len(l)):
    mid=(low+high)//2
    if s==l[mid]:            #Good to check l[mid]=s first
        found+=1
        break
    elif s>l[mid]:           
        low=mid+1
    elif s<l[mid]:
        high=mid

if found>0:
    print("{} is present in list at index {} and position {}".format(s,mid,mid+1))
else:
    print("{} not present in list".format(s))
    
