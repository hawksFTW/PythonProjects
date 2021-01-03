# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 22:06:37 2021

@author: dhruv
"""


#Desc: Ask the user for a word in all uppercase. Convert this word using all lowercase, using the ord() and chr() functions. Do not use the lower() function!


# main.py

word = input("Enter a word in all uppercase: ")
lower = ''
 
for i in word:
    if ord(i) >= 65 and ord(i) <= 90:
        i = chr(ord(i)+32)
    lower = lower + i
 
print("Word in lowercase: " + lower)