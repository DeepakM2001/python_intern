# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 22:17:02 2021

@author: Deepak Murugesan
"""
import re
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False

print(end_num('abcdef'))
print(end_num('abcdef6'))