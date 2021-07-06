# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 21:33:24 2021

@author: Deepak Murugesan
"""


def merge(list1, list2):
      
    merged_list = list(zip(list1, list2)) 
    return merged_list


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(merge(list1, list2))