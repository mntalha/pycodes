# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 22:50:04 2021

@author: talha
"""

import  os

#current file name
print(os.path.basename(__file__))

#get exact location
## os.getcwd()
print("Current directory ",os.getcwd())


#list theall files unders directories name
path = "C:/Users/talha/Desktop/"
print(os.listdir(path))
