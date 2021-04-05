# main.py

def selectionSort(list1):
  s = []
  while len(list1) > 0:
    mNum = min(list1)
    s.append(mNum)
    list1.remove(mNum)
  return s
  
print(selectionSort([5, 6, 2, 8, 9, 3, 4, 7]))

list2 = [9, 3, 6, 2, 7, 5, 8, 11]
temp = list2[0]
list2[0] = list2[7]
list2[7] = temp
print(list2)

def inPlaceSelectionSort(list3):
  for x in range(len(list3)):
    minNum = list3[x]
    minIndex = x
    temp1 = list3[x]
    for i in range(x, len(list3)):
      if list3[i] < minNum:
        minNum = list3[i]
        minIndex = i
    list3[x] = list3[minIndex]
    list3[minIndex] = temp1
    
  return list3

print(inPlaceSelectionSort([5, 6, 2, 8, 9, 3, 4, 7]))

