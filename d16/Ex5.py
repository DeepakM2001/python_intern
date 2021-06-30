# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:53:45 2021

@author: Deepak Murugesan
"""



list1 = [10, 21, 4, 45, 66, 93, 1]
  
even_count = 0

for num in list1:
      
    if num % 2 == 0:
        even_count += 1
  
          
print("Even numbers in the list: ", even_count)