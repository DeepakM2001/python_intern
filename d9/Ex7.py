# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 22:01:56 2021

@author: Deepak Murugesan
"""

def find(in_dpk):
    year = int(in_dpk/365)
    week = int((in_dpk%365)/day_check)
    days = int((in_dpk%365)%day_check)

    print(year ,": years,",week,": weeks ,",days , ":days")

in_dpk =int(input("Enter your value: "))
day_check = 7
find(in_dpk)