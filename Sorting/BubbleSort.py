# main.py

import random

def bubbleSort(list1):
  for j in range(0, len(list1)):
    for i in range(0, len(list1)-1):
      if list1[i] > list1[i+1]:
        temp = list1[i]
        list1[i] = list1[i+1]
        list1[i+1] = temp
  return list1
  
unsortedList = []
for i in range(10):
  unsortedList.append(random.randint(0, 100))

print(unsortedList)

print(bubbleSort(unsortedList))