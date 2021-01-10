# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 11:09:41 2021

@author: dhruv
"""


import random
import sys

# read in states
f = open("states.txt")
data = f.readlines()
states = [line.strip() for line in data]
f.close()

# read in capitals
f = open("capitals.txt")
data = f.readlines()
capitals = [line.strip() for line in data]
f.close()

c = 0
while True:
  choice  = random.randint(0, 49)
  
  newState = states[choice]
  guess = input("What is the capital of " + str(newState) + ": ")
  
  if guess == capitals[choice]:
    c += 1
    print("Correct, your score was " + str(c))
  else:
    sys.exit("Incorrect, your final score was " + str(c))