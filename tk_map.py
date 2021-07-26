# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 22:42:23 2021

@author: talha
"""

#Map is special function that does operation without looping as in filter

#map(func,array or iterables )

# filter only returns true ones

# map does operation to each value in list or iterables

people = ["Matt","Bryan","Tommy","Markus"]


# old method
counts = []
for i in people:
    counts.append(len(i))
    
print(counts)

# new method

x = list(map(len,people)) # len(people[0]), len(people[1]) . . . 
print(x)