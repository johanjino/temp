# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:32:04 2020

@author: johan
"""


# global variable has scope only for that function 
# Rule--> Name Resolution (1st checks for local in function block)(lifetime of var)
#                         order--- local,enclosed,global,built in

#Global for fun1()
x=200
def fun1():
    global x
    x=x+200
    print("Inside fun1(), before calling fun2(): ",x)
    def fun2():
        #x=x+200 #gives error since x is only global for fun1 UnboundLocalError 
        print("Inside fun2(): ",x)
    fun2()
    print("Inside fun1(), after calling fun2(): ",x)

#main starts here
print("Before fun1() ",x)
fun1()
print("Outside function after calling fun1(): ",x)



#Global for fun2()
x=200
def fun1():
    #x=x+200     #gives error since x is only global for fun1 UnboundLocalError 
    print("Inside fun1(), before calling fun2(): ",x)
    def fun2():
        global x
        x=x+200 
        print("Inside fun2(): ",x)
    fun2()
    print("Inside fun1(), after calling fun2(): ",x)

#main starts here
print("Before fun1() ",x)
fun1()
print("Outside function after calling fun1(): ",x)



#Global for fun1() and fun2()
x=200
def fun1():
    global x
    x=x+200
    print("Inside fun1(), before calling fun2(): ",x)
    def fun2():
        global x
        x=x+200 
        print("Inside fun2(): ",x)
    fun2()
    print("Inside fun1(), after calling fun2(): ",x)

#main starts here
print("Before fun1() ",x)
fun1()
print("Outside function after calling fun1(): ",x)



#very important---->
#Example:
x=200
def fun1():
    x=10
    print("Inside fun1(), before calling fun2(): ",x)
    def fun2():
        global x
        x=x+200 # global x will be used, i.e. x=200
        print("Inside fun2(): ",x)
    fun2()
    x=90
    print("Inside fun1(), after calling fun2(): ",x) #global x is changed, here local x is printed

#main starts here
print("Before fun1() ",x)
fun1()
print("Outside function after calling fun1(): ",x)