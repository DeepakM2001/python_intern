# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 22:11:07 2021

@author: Deepak Murugesan
"""

def covid(name,btemp):
    print("patient name is :",name,"\tbody temperature:",btemp)

name = input("enter patients name:\n")
btemp = input("enter temperature :")
if btemp.isalpha() == True:
    weight = 98
else:
    weight = btemp
covid(name,btemp)