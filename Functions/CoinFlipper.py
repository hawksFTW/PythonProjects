# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 22:13:26 2021

@author: dhruv
"""

#Desc: Coin Flipping Code

# main.py

import random 


def flipCoin():
   randNum = random.randint(0, 1)
   if randNum == 0:
     return "heads"
   if randNum == 1:
     return "tails"

heads = 0
tails = 0


for x in range(1000):
  flip = flipCoin()
  if flip == "heads":
    heads += 1
  else:
    tails += 1

heads = (heads/1000) * 100    
tails = (tails/1000) * 100
print(str(heads) + "% of your flips was heads")
print(str(tails) + "% of your flips was tails")
