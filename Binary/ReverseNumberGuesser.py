# main.py

print("Think of a whole number between 1 and 100, and I'll try to guess it in 7 guesses!")

guesses = []
minIndex = 0
maxIndex = 99
guess = 0
middle = int((minIndex + maxIndex)/2)

for x in range(1, 101):
  guesses.append(x)


while guess <= 7:
  print("Is your number " + str(guesses[middle]))
  print("If not is it above or below " + str(guesses[middle]))
  i = input("(Type 'yes', 'above', or 'below') ")
  guess += 1
  if i == "yes":
    print("Your number is " + str(guesses[middle]))
    break
  elif i == "above":
    minIndex = middle
    middle = int((minIndex + maxIndex)/2)
  elif i == "below":
    maxIndex = middle
    middle = int((minIndex + maxIndex)/2)
