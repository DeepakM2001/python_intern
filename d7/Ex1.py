# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 22:05:48 2021

@author: Deepak Murugesan
"""

def matfun(a,b):
    value = a+b
    print("addition of two numbers is :",value,"\n")
    value = a-b
    print("substraction of two numbers is :", value,"\n")
    value = a*b
    print("multiplication of two numbers is :", value,"\n")
    value = a/b
    print("division  of two numbers is :", value,"\n")

a =int(input("enter input 1 here:\n"))
b = int(input("enter input 2 here:\n"))
matfun(a,b)