# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 18:43:50 2021

@author: talha
"""


# it has 2 way to profile the process. 

#cProfile.run(fnc) or # write function to see long range

import cProfile, pstats, io

from tk_logging import *

def profile(fnc ,*arg):
    
    tk = Tk_logging("profile","cprofile.txt","DEBUG")
    pr = cProfile.Profile()
    pr.enable()
    retval = fnc(*arg)
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    tk.logger.info(s.getvalue())
    
    return retval
 
#profile(test(args))