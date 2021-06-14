# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:46:26 2021

@author: Deepak Murugesan
"""

name = input("Enter your name")
print (name)

l_list = [2,0,0,1,0,4,2,1]
l_list.append(5)
del l_list[2]
print(l_list)
low=min(l_list)
high=max(l_list)
print(low,high)