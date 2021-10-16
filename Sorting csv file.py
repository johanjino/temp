# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:28:13 2020

@author: johan
"""


#to sort elements

import csv

newline=[]
found=0
with open("student1.csv",'r') as csvfile:
    csvobj = csv.reader(csvfile)
    L=[]
    for i in csvobj:
        L.append(i)
    for i in range(len(L)):          #insertion sort 
        m=L[i]                   
        j=i-1
        while j>=0 and m[1]<L[j][1]:   #int(m[1])<int(L[j][1]) for roll number
            L[j+1]=L[j]                #float(m[1])<float(L[j][1]) for marks
            j=j-1
        else:
            L[j+1]=m
            
csvfile=open("student1 copy.csv","w",newline='')
csvobj=csv.writer(csvfile)
csvobj.writerows(L)
csvfile.close()