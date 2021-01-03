# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:36:59 2021

@author: dhruv
"""


# main.py

# prices = {"eggs":2, "bread":4, "milk":3}

# prices["toast"] = milk

# print(prices)

# print(prices["eggs"])

# print(prices)

# if "milk" in prices:
#   print(prices["milk"])

# if 3 in prices.values():
#   print("yes")

# for x in prices:
#   print(x)
#   print(prices[x])
# prices["eggs"] += 10
# print(prices)

words = {"cake":"A baked bread thing", "Chocolate":"Cocao seeds mushed in a pot", "Jello":"geletain", "Toast":"Toasted bread", "Ice cream":"Frozen ice"}

print(words)

squares = {"1":"1", "2":"4", "3":"9", "4":"16", "5":"25", "6":"36", "7":"49", "8":"64", "9":"81", "10":"100", "11":"121", "12":"144", "13":"169", "14":"196", "15":"225", "16":"256", "17":"289","18":"324", "19":"361", "20":"400", "21":"441", "22":"484", "23":"589", "24":"576", "25":"625"} 
print(squares)

def factorial(num1):
  d = 1
  for num in range(2, num1 + 1):
    d *= num
  return d
 
fac = {} 
#fac = {1:factorial(1), 2:factorial(2), 3:factorial(3), 4:factorial(4), 5:factorial(5), 6:factorial(6), 7:factorial(7), 8:factorial(8), 9:factorial(9), 10:factorial(10), 11:factorial(11), 12:factorial(12), 13:factorial(13), 14:factorial(14), 15:factorial(15), 16:factorial(16), 17:factorial(17), 18:factorial(18), 19:factorial(19), 20:factorial(20), 21:factorial(21), 22:factorial(22), 23:factorial(23), 24:factorial(24), 25:factorial(25)}


for x in range(1, 26):
  fac[x] = factorial(x)

print(fac)

words = {}
word = input("Enter a word: ")

for x in word:
  if x not in words:
    words[x] = 1
  elif x in words:
    words[x] += 1 

print(words)