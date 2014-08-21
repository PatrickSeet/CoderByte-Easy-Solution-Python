#!/usr/bin/python -tt
import re

def SimpleSymbols(strng):

	matchResult = re.match(r'(\+\w\+)',strng)

	return True if matchResult else False

def main():

	result =  SimpleSymbols("+d+=3=+s+")
	print result

if __name__ == "__main__":
  main()