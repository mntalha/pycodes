# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 21:48:36 2021

@author: talha
"""

#filter
# without making foor loop itererate all elements inside the list and (return only true ones)



def lower (value):
    if value > 1:
        return True
    else :
        return False

import numpy as np
v = np.random.randint(10, size=10)
f = filter(lower, v)  
print(list(f)) 
