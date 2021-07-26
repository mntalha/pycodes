# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 22:04:24 2021

@author: talha
"""

import time
from threading import Timer 




def display (msg):
    print("Hello ",msg)
    

# interval timer
class Tk_timer(Timer):
    def run(self):
        print("Beginnig of the Timer")
        while not self.finished.wait(self.interval):
            self.function(*self.args,**self.kwargs)
        print("End of the Timer")


if __name__ == "__main__":
    # one time timer
    timer = Timer(2,display,args=["Richard"]) # after 2 seconds , run the display functions
    timer.start()
    
    #interval
    interval_timer = Tk_timer(1, display,args=["Jonathan"]) # once in 2 seconds
    interval_timer.start()
    time.sleep(10) # it blocks the main thread not timers 
    interval_timer.cancel()
    
    
    
    