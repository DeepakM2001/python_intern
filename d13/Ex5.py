# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 22:24:09 2021

@author: Deepak Murugesan
"""
import re
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))