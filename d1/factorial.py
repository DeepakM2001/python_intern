# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 19:29:59 2021

@author: Deepak Murugesan
"""

import math  
def fact(n):  
    return(math.factorial(n))  
  
num = int(input("Enter the number:"))  
input = fact(num)  
print("Factorial of", num, "is: ",input)  