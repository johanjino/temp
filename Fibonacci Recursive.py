# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:30:30 2020

@author: johan
"""



def fib(x):
    if x<=1:
        return x
    else:
        y=fib(x-1)+fib(x-2)
        return y

#main starts here
        
n=int(input("enter number of values: "))
if n>0:
    for i in range(n):
        print(fib(i))
else:
    print("invalid input")
    
    
#-----------

x=0
for i in range(n):
    x=x+fib(i)
print(x)

def fibsum(x):
    x=0
    for i in range(n):
        x=x+fib(i)
    return x
print(fibsum(n))
        
    