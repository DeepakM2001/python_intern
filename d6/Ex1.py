# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:40:03 2021

@author: Deepak Murugesan
"""

def Merge(country,forest):
    return(country.update(forest))
country={"Neem":"country",
        "Rose":"country",
        "hibiscus":"country"}
forest={"sandal":"forest",
        "olive":"forest",
        "lime":"forest"}

sol=country.update(forest)
print(sol)
print(country)
print(forest)