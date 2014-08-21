#!/usr/bin/python -tt
def CheckNums(n1,n2):

	return True if n2 > n1 else False if n2 < n1 else -1

def main():

	result = CheckNums(3,122)
	print result

if __name__ == "__main__":
  main()