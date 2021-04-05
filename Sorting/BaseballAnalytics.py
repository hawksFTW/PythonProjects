# List of baseball players with random stats
p1 = ["B. Harper", .254, 27, 92]
p2 = ["J. Soler", .256, 36, 91]
p3 = ["C. Yelich", .329, 41, 89]
p4 = ["C. Bellinger", .312, 42, 100]
p5 = ["M. Trout", .299, 41, 99]
p6 = ["F. Lindor", .296, 23, 56]
p7 = ["M. Betts", .285, 21, 67]
p8 = ["A. Rendon", .328, 29, 104]
p9 = ["D. Lemahieu", .331, 22, 87]
p10 = ["R. Acuna", .290, 36, 89]

playerList = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]


#print(playerList[8][3])
import random

def bubbleSort(list1, index):
  for j in range(0, len(list1)):
    for i in range(0, len(list1)-1):
      if list1[i][index] < list1[i+1][index]:
        temp = list1[i]
        list1[i] = list1[i+1]
        list1[i+1] = temp
  return list1
  
sortlist1 = bubbleSort(playerList, 1)
sortlist2 = bubbleSort(playerList, 2)
sortlist3 = bubbleSort(playerList, 3)
#print(sortlist)

print("Average Leaderboard:")
for x in range(len(sortlist1)):
  print(sortlist1[x][0])
print("")

print("Home run Leaderboard:")
for x in range(len(sortlist2)):
  print(sortlist2[x][0])
print("")

print("RBI Leaderboard:")
for x in range(len(sortlist3)):
  print(sortlist3[x][0])


