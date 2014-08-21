#!/usr/bin/python -tt
import re

def LetterCountI(strng):

	ary = strng.split()
	maxLetterFreq = 0
	findLetterMatch = ''
	currentWord = ''
	currentLetter = ''
	resultWord = ''

	for words in ary:
		currentWord = words
		for i in range(1,len(words)):
			currentLetter = words[i]
			#findall returns the all the matching char in a list
			findLetterMatch = re.findall(currentLetter,words)
			#use the lenght of list to determine char's # of occurence
			if len(findLetterMatch) > maxLetterFreq:
				maxLetterFreq = len(findLetterMatch)
				resultWord = currentWord

	return '-1' if maxLetterFreq == 1 else resultWord

def main():

	result = LetterCountI("Today, is the greatest day ever!")
	print result

if __name__ == "__main__":
  main()