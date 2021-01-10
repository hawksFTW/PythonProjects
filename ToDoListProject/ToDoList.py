# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 11:07:22 2021

@author: dhruv
"""


import sys

print("Welcome to your todo list!")

tasks = []
while True:
  print("What would you like to do with your todo list?\n")
  print("1. Add a task")
  print("2. Remove a task")
  print("3. Exit a task")
  i = input("Type in the number here: ")
  
  if i == "1":
    task = input("Please type in the task you would like to add: ")
    print("\nHere's your updated list:")
    tasks.append(task) 
    c = 0
    for x in tasks:
      c += 1
      print(str(c) + ". " + x)
    
  elif i == "2":
    print(tasks)
    taskr = input("Please type in the task you would like to remove: ")
    print("\nHere's your updated list:")
    tasks.remove(taskr)
    for i in tasks:
      print(i)
    
  elif i == "3":
    sys.exit("Bye")
    