# main.py

def merge(list1, list2):
  list3 = []
  while len(list1) != 0 and len(list2) != 0:
    if list1[0] < list2[0]:
      list3.append(list1[0])
      list1.remove(list1[0])
    else:
      list3.append(list2[0])
      list2.remove(list2[0])
      
  return list3 + list1 + list2

def mergeSort(listu):
  if len(listu) == 1 or len(listu) == 0:
    return listu
  else:
    firsthalf = mergeSort(listu[:len(listu)//2])
    secondhalf = mergeSort(listu[len(listu)//2:])
    return merge(firsthalf, secondhalf)

print(mergeSort([2, 5, 3, 7, 8, 1, 9, 100]))
