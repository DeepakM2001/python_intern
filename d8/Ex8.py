# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 21:29:08 2021

@author: Deepak Murugesan
"""


from collections import Counter
def MMM(n_num):
    n = len(n_num)
    get_sum = sum(n_num)
    mean = get_sum / n
    print("Mean / Average is: " + str(mean))
    n_num.sort()
    if n % 2 == 0:
        median1 = n_num[n//2]
        median2 = n_num[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = n_num[n//2]
    print("Median is: " + str(median))
    data = Counter(n_num)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    if len(mode) == n:
        get_mode = "No mode found"
    else:
        get_mode = "Mode is / are: " + ', '.join(map(str, mode))
    print(get_mode)