#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:37:14 2020

@author: talhakilic
"""


import numpy
#Inside of the value might came from 0 to 4 5 element random array
randlist=numpy.random.randint(0,4,size=(2,5)) 

print(randlist.ndim) #dimension is 2 because (2,5) have two direction
print(randlist.shape) # 2x5 
print(randlist.size) # totalay 10 element  2*5
print(randlist.dtype)#it contain int64 format

##Reshaping ##
rangelist=numpy.arange(1,10,1)#from 1 to 10 except 10 with 1 iterative 

 #let say we want to build 3x3 matrix from rangelist 
 
newrangelist=rangelist.reshape((3,3))

##Concat ##

#axis=0 refer to row .It adds row to row
#axis=1 refer to column .It adds columns to columns.
a=numpy.array([1, 2, 3, 4])
b=numpy.array([5, 6, 7, 8])
lastlist=numpy.concatenate([a,b],axis = 0)  
                                        # 1
                                        # 2
                                        # 3
                                        # 4
                                        # 5
                                        # 6
                                        # 7
                                        # 8
#lastlist1=numpy.concatenate([a,b], axis = 1)  
                       #it gives me error .
                       
##Split ##

x=numpy.arange(0,100)
y,z,t=numpy.split(x,[20, 30]) #it divide 3 part  and build list
                            #y-->first from 0 to 20 except 20
                            #z-->second from 20 to 30 except 30
                            #t-->third from 30 to 100 except 100
