# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:29:57 2020

@author: Dhruv Darbha
"""


# main.py

r1 = float(input("Runner 1, enter your time in seconds: "))
r2 = float(input("Runner 2, enter your time in seconds: "))
r3 = float(input("Runner 3, enter your time in seconds: "))
r4 = float(input("Runner 4, enter your time in seconds: "))

print("Total tun time: " + str(r1 + r2 + r3 + r4))
print("Avg time for runners: " + str((r1 + r2 + r3 + r4)/4))