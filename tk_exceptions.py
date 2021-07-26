# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 20:05:51 2021

@author: talha
"""

# try :
#     # attemp
# except : 
#     # when error occurs
# finally :
#     # her ne olursa olsun try ve catch den sonra girer."
    
    
try : 
    x = (10/2)
    assert x >6 ,"err" # burası false olursa hata verir  ve hata error
except KeyboardInterrupt: # while loop broker
            print("Shutting down")
        
except :
    print("hata var")
finally :
    print("Definetely")
    
    
#assert de cok önemli

x = -1

if x < 0 :
    raise Exception("Sorry ")