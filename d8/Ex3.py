# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 20:54:30 2021

@author: Deepak Murugesan
"""

dict_mgl={'Deepak':[12,13,31,16],'MGL':[12,77,54,43],'Adithys':[34,87,28,98],'Anuj':[33,66,55,44]}
result={k:sorted(dict_mgl[k]) for k in sorted(dict_mgl)}
print(result)

def function1(dict_mgl):
    res = dict()
    for key in sorted(dict_mgl):
        res[key] = sorted(dict_mgl[key])
    return res
function1(dict_mgl)
