#!/usr/bin/python -tt

def FirstFactorial(num):

	if num <= 1:
		return 1
	else:
		return num * FirstFactorial(num - 1)

def main():

	result = FirstFactorial(8)
	print result

if __name__ == "__main__":
  main()