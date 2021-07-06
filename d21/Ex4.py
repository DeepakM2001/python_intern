# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 21:37:12 2021

@author: Deepak Murugesan
"""

def filtereven(nums):
    if nums%2 !=0:
        return True
    else :
        return False
    

numbers =[2,2,3,5,7,96,22,65,98,65,22,65,67,85,98,95,65,42]
result=filter(filtereven,numbers)
for i in result:
    print(i)