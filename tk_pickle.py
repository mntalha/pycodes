# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 20:09:21 2021

@author: talha
"""


# store and load variable , models , lists  by using pickle

import pickle 

class Tk_Storage:

    def load_data (self , variable_path , variable):
        with open(variable_path,"wb") as f:
            pickle.dump(variable,f)
    def get_data(self, variable_path):
        with open(variable_path,"rb") as f:
            return pickle.load(f)
        
        
        
if __name__ == "__main__":
    
    import numpy as np
    
    a = np.random.random(size=[10,10])
    
    store = Tk_Storage()
    
    #should be pickle
    store.load_data("value.pickle", a)
    
    #get
    lo = store.get_data("value.pickle")
    
    if a.all() == lo.all():
        print("YESSS")
        