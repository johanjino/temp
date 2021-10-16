# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:01:07 2020

@author: johan
"""


#global and local scope of variable

def func(a):
    a=a+1    #local a
    print("Inside function:",a)
a=10      #global a
func(a)
print("Outside function after calling:",a)  #local a will not reflect outside function

# using global variable in function

a=10
def func():
    global a
    a=a+1    #global a
    print("Inside function:",a)

func()
print("Outside function after calling:",a)  #global a in function will reflect outside


