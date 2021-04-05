# main.py

def insertionSort(list1):
  for x in range(len(list1)):
    temp = list1[x]
    index = x
    while True:
      if list1[index] < list1[index-1] and index != 0:
        list1[index] = list1[index-1]
        list1[index-1] = temp
        index -= 1
      else:  
        break
  return list1

print(insertionSort([5, 9, 2, 3, 7, 10, 4, 15, 12]))