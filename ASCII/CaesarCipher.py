# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 22:05:36 2021

@author: dhruv
"""



#Desc: This time, our secret message will be encoded with letters. First, ask the user for a secret message and a key (a number). 
#The program should print out the message with each letter shifted forward in the alphabet by the key amount. 
#Keep in mind: what happens if the letter goes past the end of the alphabet? How can we make sure to start over at the beginning of the alphabet?

# main.py

i = input("Type in your message to encrypt: ")
key = int(input("Enter the key: "))

d = ""
for x in i:
  w = ord(x)
  d = chr(w + key)
  print(d, end = " ")
print("\n")


g = input("Type in your message to decrypt: ")
dkey = int(input("Type in the decryption key: "))

o = ""
for f in g:
  e = ord(f)
  o = chr(e - key)
  print(o, end = " ")
print("\n")


