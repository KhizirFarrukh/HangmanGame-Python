import nltk
from nltk.corpus import brown

nltk.download('brown')
EnglishWordsList = brown.words()


print("1 - Easy")
print("2 - Medium")
print("3 - Hard")
print("4 - Expert")

diff = input("Select difficulty: ")
wordLengthMin = 0
wordLengthMax = 0
if diff == "1":
  wordLengthMin = 3
  wordLengthMax = 4
  # between 3 and 4 
elif diff == "2":
  wordLengthMin = 5
  wordLengthMax = 7
  # between 5 and 7
elif diff == "3":
  wordLengthMin = 8
  wordLengthMax = 11
  # between 8 and 11
elif diff == "4":
  wordLengthMin = 12
  wordLengthMax = 1000
  # greater than or equal to 12

filteredWordsList = [i.lower() for i in EnglishWordsList if len(i) >= wordLengthMin and len(i) <= wordLengthMax and i.isalpha()]
