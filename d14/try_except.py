# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:05:23 2021

@author: Deepak Murugesan
"""

try:
    a = 123
    if a==123:
        print(b)
        raise NameError("Name error")
    if a >0:
        raise ValueError("Value error")
except NameError as ne:
        print(ne)
except ValueError as ve:
    print(ve)