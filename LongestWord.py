#!/usr/bin/python -tt

def LongestWord(strng):

	strnArray = rawArray = []
	maxLength = 0
	longestWord = ''

	#loop through to strip punctuation
	for i in strng:
		if i.isalpha() or i.isspace():
			rawArray.append(i)

	#put char and space only array back
	strnArray = ''.join(rawArray)
	#split into word array
	strnArray = strnArray.split(' ')

	for j in strnArray:
		if len(j) > maxLength:
			longestWord = j
			maxLength = len(j)

	return longestWord

def main():

	result = LongestWord("fun&!! time")
	print result

if __name__ == "__main__":
  main()