# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 22:02:02 2021

@author: dhruv
"""

#Desc: Write a program that asks the user for a credit card number, and then uses the described process to determine if the inputted number is valid or not.

# main.py

card = input("Enter a credit card number: ")

c = 0
for x in card:
  c += int(x)
print("The sum of the digits is: " + str(c))

d = 0
for i in range(len(card)):
  if int(i) % 2 != 0:
    a = int(card[i])
    a = a * 2
    d += a
  
  if int(i) % 2 == 0:
    d += int(card[i])
print("The sum of the digits with every other digit multiplied by 2 is: " + str(d))

if d % 10 == 0:
  print("Valid Card!")
else:
  print("Invalid Card!")
    