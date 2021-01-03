# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 22:09:42 2021

@author: dhruv
"""


#Desc: Write a program where the correct password is saved as a string in a variable in the code, 
#and the user has to continuously guess until they get the correct password. Once the user guesses correctly, 
#print the number of guesses it took!

# main.py
password = "seahawks"
counter = 1
guess = input("Enter the password: ")

while(password != guess):
  guess = input("Incorrect password, try again: ")
  counter += 1
print("You got the password and it took " + str(counter) + " tries")