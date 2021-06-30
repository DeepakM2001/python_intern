# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:18:30 2021

@author: Deepak Murugesan
"""

from functools import reduce

fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
								range(n-2), [0, 1])

print(fib(5))
