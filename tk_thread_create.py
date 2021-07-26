# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 22:54:28 2021

@author: talha
"""

from threading import Thread
import time        


def longtask(args):
    while True:
        time.sleep(2)
        print(args)
        
th1 = Thread(name="longtask_thread",target=longtask,args=["Executation1"])
# get name = th1.name
th1.start()
#th1.join() # wait untill th1 thread finish its jobs
th2 = Thread(target=longtask,args=["Executation2"])
th2.start()
#th2.join() # wait untill th2thread finish its jobs


