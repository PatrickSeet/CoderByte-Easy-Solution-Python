#!/usr/bin/python -tt

def FirstReverse(strng):

	return ''.join(strng[::-1])
	
def main():

	result = FirstReverse("I Love Code!")
	print result

if __name__ == "__main__":
  main()