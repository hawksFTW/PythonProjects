# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:36:26 2021

@author: dhruv
"""


biology = ["Sarah", "Ahmed", "Fred", "Gillian", "Shradah", "Max", "Max", "Sara", "Max", "Esther"]

computerScience = ["Sarah", "John", "Fred", "Gillian", "Jermaine", "Max", "Sara", "Juan", "Esther"]

english = ["Nico", "Sharjeel", "Isabella", "Taylor", "Ali", "Ali", "Jean-Baptiste", "Jean-Baptiste", "Jean-Baptiste", "William"]



duplicate = set()
single = []
c = 0
for x in biology:
    if x not in duplicate:
        single.append(x)
        duplicate.add(x)
        c += 1
print("Biology actually has " + str(c) + " students enroled")

duplicate1 = set()
single1 = []
d = 0
for x in computerScience:
    if x not in duplicate1:
        single1.append(x)
        duplicate1.add(x)
        d += 1
print("CS actually has " + str(d) + " students enroled")

duplicate2 = set()
single1 = []
a = 0
for x in english:
    if x not in duplicate2:
        single1.append(x)
        duplicate2.add(x)
        a += 1
print("English actually has " + str(a) + " students enroled")