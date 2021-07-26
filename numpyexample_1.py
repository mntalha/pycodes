#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:21:21 2020

@author: talhakilic
"""


"""
I am creating lists such as list1 and list2  that contains integer numbers
"""
list1=[1, 2, 3, 4]
list2=[5, 6, 7, 8]

"""
in order to multiply each element one by one and create another list
"""

list3=[] #empty list

for i in range(len(list1)):
    list3.append(list1[i]*list2[i])
    
print(list3)
print(type(list1))

#remove for loop  and make all list numpy array
import numpy 

list1numpy=numpy.array(list1)
list2numpy=numpy.array(list2)

list3numpy=list1numpy*list2numpy
    
print(list3numpy)
