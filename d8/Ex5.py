# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 21:08:04 2021

@author: Deepak Murugesan
"""

def dpk_char(str1):
    char = str1[0]
    str1 = str1.replace(char, str1[0].upper())
    str1 = char + str1[1:]
    return str1

