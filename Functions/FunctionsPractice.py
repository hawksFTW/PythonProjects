# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 22:14:26 2021

@author: dhruv
"""


#Desc: Functions Practice

# main.py

def sumFunc(num1, num2):
  return num1 + num2
  
def diffFunc(num1, num2):
  return num1 - num2
  
def multiply(num1, num2, num3):
  return num1 * num2 * num3

def average(num1, num2):
  return (num1 + num2)/2

def factorial(num1):
  d = 1
  for num in range(2, num1 + 1):
    d *= num
  return d

def power(base, exp):
  return base ** exp

print("The sum of 2 and 3 is: " + str(sumFunc(2, 3)))

print("The difference of 2 and 3 is: " + str(diffFunc(2, 3)))

print("The product of 2, 3 and 4 is: " + str(multiply(2, 3, 4)))

print("The average of 2 and 3 is: " + str(average(2, 3)))

print("The factorial of 4 is: " + str(factorial(4)))

print("2 raised to the 3rd power: " + str(power(2, 3)))
