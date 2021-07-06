# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 21:30:41 2021

@author: Deepak Murugesan
"""

# Using map() and lambda
def listOfTuples(l1, l2):
    return list(map(lambda x, y:(x,y), l1, l2))
list1 = [2001, 2002, 2003]
list2 = ['ant', 'bug', 'cat']
print(listOfTuples(list1, list2))