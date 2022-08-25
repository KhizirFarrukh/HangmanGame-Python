import random
import time
from tqdm import tqdm

wordsFile = open("wordsList.txt","r")
words = wordsFile.readlines()
EnglishWordsList = []
for i in range(len(words)):
  EnglishWordsList.append(words[i][:-1])
print("\n\n")

def HangmanWordPrinter(InputLetterList):
  print("\t\t", end="")
  for i in InputLetterList:
    print(i, end="  ")
  print()
while True:
  print("1 - Easy")
  print("2 - Medium")
  print("3 - Hard")
  print("4 - Expert")

  diff = input("Select difficulty: ")
  wordLengthMin = 0
  wordLengthMax = 0
  if diff == "1":
    wordLengthMin = 3
    wordLengthMax = 5
    # between 3 and 5 
  elif diff == "2":
    wordLengthMin = 6
    wordLengthMax = 9
    # between 6 and 9
  elif diff == "3":
    wordLengthMin = 10
    wordLengthMax = 14
    # between 10 and 14
  elif diff == "4":
    wordLengthMin = 15
    wordLengthMax = 1000
    # greater than or equal to 15
  else:
    break

  filteredWordsList = [i.lower() for i in EnglishWordsList if len(i) >= wordLengthMin and len(i) <= wordLengthMax and i.isalpha()]
  random.seed(int(time.time()))

  SelectedWordIndex = random.randint(0,len(filteredWordsList)-1)
  HangmanWord = filteredWordsList[SelectedWordIndex]
  InputLetterList = ["_"] * len(HangmanWord)
  AvailableLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  incorrectTriesLimit = 5 
  incorrectCounter = 0
  gameOver = False

  while not gameOver:
    HangmanWordPrinter(InputLetterList)
    print("\n\n\t\tYou have " + str(incorrectTriesLimit - incorrectCounter) + " tries left")
    print("\n\nAvailable letters: " + str(AvailableLetters))
    charInput = input("\nEnter letter: ")
    charInput = charInput.lower()
    if charInput in AvailableLetters:
      AvailableLetters.remove(charInput)
      letterFound = False
      for i in range(len(HangmanWord)):
        if HangmanWord[i] == charInput:
          InputLetterList[i] = charInput
          letterFound = True
      if "_" not in InputLetterList:
        gameOver = True
        print("\n\n\t\tCongratulations!!! YOU WON!\n")
        HangmanWordPrinter(InputLetterList)
      if not letterFound:
        incorrectCounter += 1
        print("\n\n\t\tIncorrect Attempt!\n\n")
      if incorrectCounter == incorrectTriesLimit:
        print("\n\n\t\tYOU LOST!! GAME OVER!!!")
        print("\n\t\tHangman word : " + HangmanWord + "\n\n")
        gameOver = True
