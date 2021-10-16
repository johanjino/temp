# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:48:53 2020

@author: johan
"""

import pickle

#dictionary in files


#1) USING DICTIONARY IN TEXT FILE
    
with open('FILE DICTIONARY IN TEXT.txt','w+') as f:
    data={1:{'ABEL','Maths'},2:{'NITHYA',"English"}}
    s=(data.items())
    print(s)
    for  key,value in data.items():
        f.write('%s:%s\n' % (key,value)) #or f.write("{}:{}".format(key,value))
    f.seek(0)
    print("File Dictionary in TEXT:\n",f.read())

#2)  USING DICTIONARY IN BINARY FILE

print("FILE DICTIONARY IN BINARY FILES:",'wb+')
with open ('FILE READ AND WRITE BINARY','wb+') as f:
    data={1:{'ABEL','Maths'},2:{'NITHYA',"English"}}
    pickle.dump(data,f)
    f.seek(0)
    print("File Dictionary in BINARY:\n {}".format(pickle.load(f)))
