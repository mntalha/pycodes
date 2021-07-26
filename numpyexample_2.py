#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 

@author: talhakilic
"""


import numpy

#numpy save all data in only one type .In here we can select array type

list1=numpy.array([1,2,3,4],dtype="float16")

#sometimes we need to create empty array to fill data.

zerolist=numpy.zeros(5) #create 5x1 zeros 

zerolist2=numpy.zeros((1,5)) #create 5x1 zeros vector

zerolist3=numpy.zeros((4,2)) #create 4x2 zeros matrix

#sometimes we need to create  array that have ones.

onelist=numpy.ones(5) #create 5x1 ones 

onelist2=numpy.ones((1,5)) #create 5x1 ones vector

onelist3=numpy.ones((4,2)) #create 4x2 ones matrix

#and sometimes we need to create  array that have the value that we spesify.

newlist1=numpy.full(5,6)  #create 5x1 array that contain 6.

newlist2=numpy.full((1,5),6) #create 5x1 array that contain 6

newlist2=numpy.full((2,4),6) #create 4x2 ones that contain 6


# or maybe you want to build arrayby  putting number with 
#increasing or decreasing
startnumber=1
stopnumber=20
inreasingnumber=2
increasinglist=numpy.arange(start=startnumber,stop=stopnumber,
                            step=inreasingnumber)
#in above the list is from 1 to 20 with increasing 2.
#1 is including 20 is not including 


#or with certain start ,stop and numberofdata 
startnumber1=1
stopnumber1=2
numberofdata=100
#from 1 to 2 . build 100 data and include 1 and 2
newincreasinglist=numpy.linspace(startnumber1,stopnumber1,numberofdata)


#or build random matrix with spesifying mean and stardart deviation 
#but the result will be float
mean=10
std=6
distributedlist=numpy.random.normal(mean,std,(4,4)) #4x4 matrix 

#or build random matrix without spesifying mean and stardart deviation 
# the result will be int
#values came from 0 to 10
randomlist=numpy.random.randint(0,10,(4,4)) #4x4 matrix 

print(randomlist.ndim)
print(randomlist.shape
print(randomlist.size)
