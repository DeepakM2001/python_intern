# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 21:53:13 2021

@author: Deepak Murugesan
"""

n = int(input("Enter your value: "))
a = 0
b = 1
sum = 0
count = 1
print("fibonacci series:",end = "")
while(count <= n):
    print(sum,end ="")
    count += 1
    a = b
    b = sum
    sum = a + b
