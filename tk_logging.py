# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 17:32:15 2021

@author: talha
"""

# includes personalized log class and its own functions

# provide to log in different stages and level .

#LEVELS :

"""
DEBUG
INFO 
WARNING 
ERROR 
CRITICAL
"""

import logging

class Tk_logging():
    
    _file_name = None
    _log_level = None
    logger = None
    
    
    def __init__(self,loggername,filename,level="DEBUG"):
        
        self.logger = logging.getLogger(loggername)
        
        handler = logging.FileHandler(filename=filename,mode="w")
        
        formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - (%(levelname)s) --- %(message)s")

        handler.setFormatter(formatter)
        
        # console = logging.StreamHandler()
        # console.setLevel(logging.DEBUG)
        # self.logger.addHandler(console)


        self.logger.addHandler(handler)

        if level == "DEBUG":
            self.logger.setLevel(logging.DEBUG)
        if level == "INFO":
            self.logger.setLevel(logging.INFO)
        if level == "WARNING":
            self.logger.setLevel(logging.WARNING)
        if level == "ERROR":
            self.logger.setLevel(logging.ERROR)
        if level == "CRITICAL":
            self.logger.setLevel(logging.CRITICAL)
         
        self.logger.critical("LOGGING STARTED")
        
    def getlevel(self):
        
        return logging.getLevelName(self.logger.getEffectiveLevel())
    
    
    def setlevel(self,level):
        if level == "DEBUG":
            self.logger.setLevel(logging.DEBUG)
        if level == "INFO":
            self.logger.setLevel(logging.INFO)
        if level == "WARNING":
            self.logger.setLevel(logging.WARNING)
        if level == "ERROR":
            self.logger.setLevel(logging.ERROR)
        if level == "CRITICAL":
            self.logger.setLevel(logging.CRITICAL)
        

if __name__ == "__main__":
    tk = Tk_logging("main","deneme.txt","DEBUG")
    tk.logger.debug("TEST")
    tk.logger.debug("DENEME")
    value  = 0.88
    tk.logger.debug(f" ********** { {value} } EPOCH")


   
#If down option is chosen , it should be the top of the messages othewise , it will not be saved.
#logging.basicConfig(filename='log_file.log', filemode='w',format="%(asctime)s-%(threadName)s-(%(levelname)s)-->%(message)s",level=logging.DEBUG)
        

        
    
    
        
    
    