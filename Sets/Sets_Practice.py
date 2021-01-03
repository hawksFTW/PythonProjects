# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:35:06 2021

@author: dhruv
"""


import random
# main.py
# fives = set()

# for i in range(5, 36, 5):
#   fives.add(i)

# print(fives)

# fives.remove(35)
# print(fives) 

# for number in fives:
#   print(number)

# if 10 in fives:
#   print("yes")
  
# evens = set()
# for i in range(2, 31, 2):
#   evens.add(i)

# print(evens)

# print(fives.intersection(evens))

# print(fives.union(evens))

set1 = set()
set2 = set()

for i in range(1, 6):
  num = random.randint(1, 15)
  set1.add(num)
print(set1)

for x in range(1, 6):
  num = random.randint(1, 15)
  set2.add(num)
print(set2)

print(set1.intersection(set2))

print(set1.union(set2))

if 1 in set2:
  print("Number is inside set")

words = set()  
word = input("Give me a word: ")
for x in word:
  words.add(x)

print(words)

words2 = set()
word2 = input("Give me another word: ")
for i in word2:
  words2.add(i)
  
print(words.intersection(words2))

def evenReturn(setIn):
  evens = set()
  for x in setIn:
    if x % 2 == 0:
      evens.add(x)
  return evens

def oddReturn(setIn):
  odd = set()
  for x in setIn:
    if x % 2 != 0:
      odd.add(x)
  return odd

def threeReturn(setIn):
  three = set()
  for x in setIn:
    if len(x) == 3:
      three.add(x)
  return three

print(evenReturn(set1))
print(oddReturn(set1))
print(threeReturn(set(["cat", "dog", "house", "horse"])))