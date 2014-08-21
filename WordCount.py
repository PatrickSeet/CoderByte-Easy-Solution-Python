#!/usr/bin/python -tt
import re

def WordCount(strng):

	matchre = re.findall(r'\s',strng)
	return len(matchre) + 1

def main():

	result = WordCount("Never eat shredded wheat")
	print result

if __name__ == "__main__":
  main()