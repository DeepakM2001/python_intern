# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 22:06:14 2021

@author: Deepak Murugesan
"""


print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

ch = int(input("enter choice(1-4):"))

if ch ==1:
    a =int(input("enter a:"))
    b = int(input("enter b:"))
    c = a+b
    print("sum is=",c)
elif ch == 2:
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    c = a - b
    print("difference is= ",c)
elif ch==3:
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    c = a * b
    print("product  is= ", c)
elif ch==4:
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    c = a / b
    print("quotient = is ", c)
else:
    print("Invalid")