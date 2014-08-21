#!/usr/bin/python -tt

def SwapCase(strng):

	result = []

	for letters in strng:
		if letters.isalpha():
			if letters.isupper():
				result.append(letters.lower())
			else:
				result.append(letters.upper())
		else:
			result.append(letters)

	return ''.join(result)
	
def main():

	result = SwapCase("Sup DUDE!!?")
	print result

if __name__ == "__main__":
  main()