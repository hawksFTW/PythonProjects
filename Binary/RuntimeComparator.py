# main.py
import time

start = time.time()
print("Starting linear search...")


def linearSearch(list1, num):
  for x in list1:
    if num == x:
      return True

  return False
      
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(linearSearch(list1, 5))

end = time.time()
elapsed = end - start
print("Linear search ended.")

bstart = time.time()
print("Starting binary search...")

def binarySearch(list1, target):
  minIndex = 0
  maxIndex = len(list1) - 1
  while minIndex <= maxIndex:
    middle = int((minIndex + maxIndex)/2)
    if list1[middle] == target:
      return True
    elif target > list1[middle]:
      minIndex = middle + 1
    else:
      maxIndex= middle - 1
      
  return False
  
print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 1))

bend = time.time()
belapsed = bend - bstart
print("Binary search ended.")

print("Linear search took " + str(elapsed))
print("Binary search took " + str(belapsed))


#print(elapsed)

