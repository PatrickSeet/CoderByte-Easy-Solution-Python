#!/usr/bin/python -tt
def VowelCount(strng):

	vowels = ['a','e','i','o','u']
	count = 0
	newStrng = strng.lower()

	for chars in newStrng:
		if chars in vowels:
			count += 1
			
	return  count

def main():

	result = VowelCount("All cows eat grass")
	print result

if __name__ == "__main__":
  main()