#!/usr/bin/python -tt
def LetterChanges(strng):
	
	vowels = 'aeiou'
	charList = 'abcdefghijklmnopqrstuvwxyz'
	newarray = []

	for letter in strng:

		#if letter is alphabetical
		if letter.isalpha():
			#find the index of the letter from charList
			cindex = charList.find(letter)
			#if the next char is a vowel, upper case it, else just append
			if vowels.find(charList[cindex+1]) != -1:
				newarray.append(charList[cindex+1].upper()) 
			else:
				newarray.append(charList[cindex+1])
		else:
			newarray.append(letter)
	
	return ''.join(newarray)

def main():

	result = LetterChanges("hello*3")
	print result

if __name__ == "__main__":
  main()