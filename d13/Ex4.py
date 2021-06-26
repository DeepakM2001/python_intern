# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 22:23:46 2021

@author: Deepak Murugesan
"""

import re
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))