# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 21:27:59 2021

@author: Deepak Murugesan
"""


a=int(input("Enter number :"))
b=int(input("Enter number :"))
c=int(input("Enter number :"))
sum1=a+b+c
print(sum1)
user=int(input("Enter the number to divide sum!"))
if sum1% user==0:
    print("The given input divide")
else :
    print("The given input does not divide sum1")