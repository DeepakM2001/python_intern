# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:19:13 2021

@author: Deepak Murugesan
"""

#importing library
from tkinter import *
import tkinter as tk 
from tkinter import ttk
from tkinter.ttk import *


window = tk.Tk()

#Declaring Window Title
window.title("Registration Screen")
#Declaring Window size
window.geometry('500x320')
#Declaring Window Color
window.configure(background = "azure");
#below four fields are declared
Firstname = Label(window ,text = "First Name").grid(row = 0,column = 0)
LastName = Label(window ,text = "Last Name").grid(row = 1,column = 0)
Email = Label(window ,text = "Email Id").grid(row = 2,column = 0)
Mobile = Label(window ,text = "Contact Number").grid(row = 3,column = 0)
ttk.Label(window, text = "Select the Country :").grid(row = 4,column = 0) 
languages = [("Python", 101),
   	     ("Perl", 102),
    	     ("Java", 103),
             ("C++", 104),
             ("C", 105)]


Firstname1 = Entry(window).grid(row = 0,column = 1)
Lastname1 = Entry(window).grid(row = 1,column = 1)
Email1 = Entry(window).grid(row = 2,column = 1)
Mobile1 = Entry(window).grid(row = 3,column = 1)
n = tk.StringVar() 
country = ttk.Combobox(window, width = 22, textvariable = n) 
  
# Adding combobox drop down list 
country['values'] = (' India',  
                          ' China', 
                          ' Australia', 
                          ' Nigeria', 
                          ' Malaysia', 
                          ' Italy', 
                          ' Turkey', 
                          ' Canada') 
country.grid(column = 1, row = 4) 
country.current()
    
#fubction declaration
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=8,column=0)
window.mainloop()
