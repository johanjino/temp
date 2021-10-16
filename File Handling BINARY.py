# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:04:03 2020

@author: Jino
"""


import pickle
#using binary modes


print("FILE OPERATIONS IN BINARY FILES:")
with open ('FILE READ AND WRITE BINARY','wb+') as f:
    data="Python is an interative language\n Python is user frinedly\n"
    pickle.dump(data,f)
    f.seek(0)
    print("File content as follows:\n {}".format(pickle.load(f)))
    f.seek(0)
    print(type(pickle.load(f)))


