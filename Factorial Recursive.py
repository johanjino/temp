# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 08:23:44 2020

@author: johan
"""


#program calculate the factorial of a number using recursive call

def fact(n):
    if n>=0:
        if n<=1:
            return 1
        else:
            return n*fact(n-1)
    else:
        return ("invalid input")
#main starts here
n=int(input("Enter number:"))
print(fact(n))