# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 22:09:08 2021

@author: dhruv
"""


#Desc: Program the game Double or Nothing! The user should start with $10 and be given the option to walk away or play double or nothing with all of their money.
#If they play, then simulate a coin flip, where heads doubles their money and tails means they lose it all. Keep playing until the player either walks away or loses!


# main.py 
import random
import sys

while True:
  money = 10
  userChoice = input("You currently have $10. Type q to walk away with the money you have or press Enter to continue: ")


    
  while(userChoice == ""):
    randNum = random.randint(0, 1)
    userChoice = input("You currently have " + str(money) + " dollars. Type q to walk away with the money you have or press Enter to continue: ")
    
    if(userChoice == "q"):
      sys.exit("You exited double or nothing with " + str(money) + " dollars")
    if(randNum == 0):
      money = money * 2
      print("Nice the coin was heads. You now have " + str(money) + " dollars")
    if(randNum == 1):
      sys.exit("Sorry the coin was tails and you lost - you exited with 0 dollars")