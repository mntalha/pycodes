# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 12:56:24 2021

@author: talha
"""

def check_gpu_avaliable(tf_name = None):
    if tf_name == None:
        print("Enter tensorflow module")
        return False
    print(tf_name.config.list_physical_devices('GPU'))
    print('Default GPU Device: {}'.format(tf_name.test.gpu_device_name()))
    print(tf_name.test.is_built_with_cuda())
    return True
 
def cudnn_handle_error(tf_name = None):
#Could not create cudnn handle: CUDNN_STATUS_ALLOC_FAILED error
    if tf_name == None:
        print("Enter tensorflow module")
        return False
    physical_devices = tf_name.config.list_physical_devices('GPU')
    try:
        tf_name.config.experimental.set_memory_growth(physical_devices[0], True)
    except:
        # Invalid device or cannot modify virtual devices once initialized.
        pass