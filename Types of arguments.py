# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 08:49:46 2020

@author: johan
"""

#Pass/Call by value  => only for immuteable data type-->except(list,dictionary)

#Pass by value
#Positional Argument
def fun1(x,y): #function definition with formal parameter/argument
    x=10
    print("Inside function x={} and y={}".format(x,y))
    
a=20 ; b=30  #local to main
fun1(a,b)   #function call with actual parameter/argument
print("Outside function x={} and y={}".format(a,b))




#Pass by value
#Keyword Argument - order of variable in func call doesnt matter
def fun1(y,x):
    print("Inside function x={} and y={}".format(x,y))
x=20 ; y=30  #local to main
fun1(x=100,y=300)   #function call(use same variable name as func def)
fun1(y=300,x=100)   #order does not matter
print("Outside function x={} and y={}".format(x,y))




#Pass by value
#Default Argument  - order of variable matters
def fun1(x,y=10): #function definition with formal parameter/argument
    print("Inside function x={} and y={}".format(x,y))
    
a=20 ; b=30  #local to main
fun1(a)   #function call
fun1(a,b)
print("Outside function x={} and y={}".format(a,b))
