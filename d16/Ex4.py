# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:29:25 2021

@author: Deepak Murugesan
"""

num_list = [45, 55, 60, 37, 100, 105, 220]

result = list(filter(lambda x: (x % 9 == 0), num_list))
print("Numbers divisible by 9 are",result)