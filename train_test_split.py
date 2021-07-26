# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 09:28:37 2021

@author: talha
"""

import os
import random
import numpy as np
import shutil

root_dir        = os.getcwd()
classes         = os.listdir('dataset')

test_ratio=0.1

shutil.rmtree(root_dir+'/train/', ignore_errors=True)
shutil.rmtree(root_dir+'/test/', ignore_errors=True)


for cls in classes:
    os.makedirs(root_dir+'/train/'+cls)
    os.makedirs(root_dir+'/test/'+cls)
    
for cls in classes:
    #ouputs the name of images inside the files.
    files_name=os.listdir(root_dir+"/dataset/"+cls)
    #shuffle names
    np.random.shuffle(files_name)
    
    #split the files
    train_FileNames=files_name[:int(len(files_name)*(1-test_ratio))]
    test_FileNames=files_name[int(len(files_name)*(1-test_ratio)):]
    
    #add path to image names
    train_FileNames=[root_dir+'/dataset/'+cls+"/"+name for name in train_FileNames]
    test_FileNames=[root_dir+'/dataset/'+cls+"/"+name for name in test_FileNames]
    print(cls," Splitting")
    print("Total Images:",len(files_name))
    print("Train",len(train_FileNames))
    print("Test",len(test_FileNames))
    
    #copy images
    for name in train_FileNames:
        shutil.copy(name,root_dir+"/train/"+cls)
        
    for name in test_FileNames:
        shutil.copy(name,root_dir+"/test/"+cls)

