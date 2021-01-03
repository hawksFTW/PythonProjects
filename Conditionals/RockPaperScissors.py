# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 22:02:27 2021

@author: dhruv
"""


#Desc: Code a two-player Rock, Paper, Scissors game. First, set up the player1 and player2 variables to be rock, paper, or scissors. 
#Then, print out "Player 1 wins," "Player 2 wins," or "It's a tie."

# main.py

p1 = input("Player 1 - pick rock, paper, scissors: ")
p2 = input("Player 2 - pick rock, paper, scissors: ")


if(p2 == "scissors"):
  if(p1 == "paper"):
    print("Player 2 wins!")
  elif(p1 == "rock"):
    print("Player 1 wins")
  elif(p1 == "scissors"):
    print("It's a tie!")
    
if(p2 == "rock"):
  if(p1 == "paper"):
    print("Player 1 wins!")
  elif(p1 == "rock"):
    print("It's a tie!")
  elif(p1 == "scissors"):
    print("Player 2 wins")
    
if(p2 == "paper"):
  if(p1 == "paper"):
    print("It's a tie!")
  elif(p1 == "rock"):
    print("Player 2 wins")
  elif(p1 == "scissors"):
    print("Player 1 wins!")
  
if(p1 != "rock" and p1 != "paper" and p1 != "scissors"):
  print("Not a valid input")
  
if(p2 != "rock" and p2 != "paper" and p2 != "scissors"):
  print("Not a valid input")