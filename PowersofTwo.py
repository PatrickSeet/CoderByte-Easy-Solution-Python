#!/usr/bin/python -tt
import math

def PowersofTwo(num):

	result = math.sqrt(num)

	return True if result % 2 == 0 else False

def main():

	result = PowersofTwo(16)
	print result

if __name__ == "__main__":
  main()