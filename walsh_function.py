#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 17:49:47 2021

@author: mntalha
"""

c = [[1,1],[1,-1]]

import numpy as np

c = np.array (c)

up_two = np.concatenate((c, c),axis=1)

down_two = np.concatenate((c, -1*c),axis=1)

four =np.concatenate((up_two, down_two),axis=0)
##

up_four =np.concatenate((four, four),axis=1)

down_four =np.concatenate((four, -1*four),axis=1)

eight= np.concatenate((up_four, down_four),axis=0)

##

up_eight=np.concatenate((eight, eight),axis=1)

down_eight=np.concatenate((eight, -1*eight),axis=1)

sixteen = np.concatenate((up_eight, down_eight),axis=0)

sixteen[sixteen == -1] = 0