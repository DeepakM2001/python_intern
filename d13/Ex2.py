# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 22:11:14 2021

@author: Deepak Murugesan
"""

import re
def check(string) :

    regex = re.compile("\w*a\w*")
 
    match_object = regex.findall(string)
 
    if len(match_object) != 0 :
        for word in match_object :
            print(word)
            print("String found")
             
    else :
        print(" nothing found ")
    
if __name__ == '__main__' :
    string = input("Enter your string: ")
 
    check(string)