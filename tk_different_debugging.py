# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 22:13:39 2021

@author: talha
"""


#icecream module might be usefull for debugging issues 

# first dowloand the module 
    
# pip install icecream 

from icecream import ic

ic.configureOutput(prefix='Debug | ') # writes Debug before each printing

# if you dont want to print you can disable
#ic.disable() 
#ic.enable()

def square_of(num):
    return num*num

# it gives function and its input value
ic(square_of(2)) # ic| square_of(2): 4 ,normally print("square_of(2)",square_of(2))


my_dict = {'name': 'Chris','age': 33}

ic("Talha",my_dict) #ic| my_dict: {'age': 33, 'name': 'Chris'}
print(my_dict) #{'name': 'Chris', 'age': 33} no name

num =2
if ic(square_of(num)) == pow(num, 2):
    ic('Correct!')



