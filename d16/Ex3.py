# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:20:46 2021

@author: Deepak Murugesan
"""

def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,-8]))

