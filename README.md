# Introduction

This is a Hangman game made in Python 3

This game has 4 difficulty levels;
*  1 - Easy (Word length is between 3 and 5)
*  2 - Medium (Word length is between 6 and 9)
*  3 - Hard (Word length is between 10 and 14)
*  4 - Expert (Word length is greater than 15)

# Libraries used in the program

This program uses nltk corpus "brown" to load english vocabulary words, nltk library to download corpus, 
random library to generate a random index to select a random word from library, time library to generate 
a unique seed for random library

# Release Notes

#### Version 1.2:
*  Removed loading print statements and progress bar since game loads instantly
*  Added loop to game, new game starts after previous one is over

#### Version 1.1:
*  Removed nltk library and corpus, English Words are now loaded from a txt file
*  Added progress bar on loading of english words

### Version 1.0:
*  Added print statements to make it loading easier to understand
*  Some touches added to print statements
*  Fixed a bug where game will not be over when all tries have been used
*  Fixed a bug that the game will print the Hangman input line instead of actual Hangman word

### Version 0:
*  A functioning game 