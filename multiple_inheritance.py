# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 15:00:52 2021

@author: talha
"""

class Person:
    name = ""
    
class Nationalty:
    kind =""
    

class Turk(Person,Nationalty):
    pass

tt = Turk()

tt.name = "Turj"
tt.kind = "dasd"

