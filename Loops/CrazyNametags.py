# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 22:08:12 2021

@author: dhruv
"""

#Desc: A code that experiemnts with using loops for various purposes

# main.py

name = input("Please enter your name: ")

for x in range(len(name)):
  print(name[x])

for i in range(0, len(name), 2):
  print("Every other letter in your name: " + name[i])
  
for j in range(len(name) - 1, -1, -1):
  print("Your name spelled backwards: " + name[j])
  
d = 0
r = 0
g = len(name) - 1

while(d < len(name)):
  print(name[d])
  d += 1

while(r < len(name)):
  print(name[r])
  r += 2

while(g >= 0):
  print(name[g])
  g -= 1

  


# for i in range(10, 21, 5):
#   print(i)

# for j in range(10, 0, -1):
#   print(j)