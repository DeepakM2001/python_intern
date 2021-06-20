# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 21:26:05 2021

@author: Deepak Murugesan
"""


from collections import Counter
 
list1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
d = Counter(list1)
print(d)
 
new_list = list([item for item in d if d[item]>1])
print(new_list)