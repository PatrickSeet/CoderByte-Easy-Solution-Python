#!/usr/bin/python -tt
import re

def ABCheck(strng):

	matchre = re.search(r'a...b',strng)
	return True if matchre != 'None' else False

def main():

	result = ABCheck("after badly")
	print result

if __name__ == "__main__":
  main()