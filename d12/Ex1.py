# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 16:09:13 2021

@author: Deepak Murugesan
"""

file1 = open("30days30hour.txt","w")
file1.write("Hello \n")
file1.write("I have completed 10 days successfully\n")
file1.close()
file1 = open("30days30hour.txt","a")
file1.write("Nothing can be done now \n")
file1.close()

