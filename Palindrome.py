#!/usr/bin/python -tt
import re

def Palindrome(strng):

	return strng == strng[::-1]

def main():

	result = Palindrome("never odd or even")
	print result

if __name__ == "__main__":
  main()