# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 21:02:59 2021

@author: Deepak Murugesan
"""

import re

if __name__ == '__main__':
    
    string = input("Enter your value: ")
    pattern = re.compile("[A-Za-z0-9]+")

    if pattern.fullmatch(string) is not None:
        print("The pattern has been found: " + string)
    else:
        print("No pattern found")