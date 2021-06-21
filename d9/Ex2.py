# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 21:50:42 2021

@author: Deepak Murugesan
"""

n = int(input("Enter your value: "))
for i in range(n):
    print(''.join(map(str,range(n-i,0,-1))))