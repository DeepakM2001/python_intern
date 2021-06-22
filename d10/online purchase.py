# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:57:10 2021

@author: Deepak Murugesan
"""

class Online_Shopping:
	def __init__(self):
		self.item=0
		print("Welcome to the Monkey Website")

	def checkin(self):
		product=str("Enter the product to be purchased: ")
		self.item == product
		print("\n  Product purchased is :",product)

	def checkout(self):
		product = str("Enter product to be discarded: ")
		if self.item==product:
			self.item-=product
			print("\n The product has been discarded")
		else:
			print("\n Error in purchasing the product ")

	def display(self):
		print("\n The item in the cart is =",self.item)

s = Online_Shopping()

s.checkin()
s.checkout()
s.display()
