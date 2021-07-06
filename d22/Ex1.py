# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 21:43:55 2021

@author: Deepak Murugesan
"""


from PIL import Image
img = Image.open("D:\\College Files\\Internship\\bootcamp\\python\\d22\\download.jpg")
print(img.format)
import matplotlib.pyplot as plt
plt.imshow(img)
