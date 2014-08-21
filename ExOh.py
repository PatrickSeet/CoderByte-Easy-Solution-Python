#!/usr/bin/python -tt
def ExOh(strng):

	countX = 0
	countO = 0

	for i in strng:
		if i == 'o':
			countO += 1
		if i == 'x':
			countX += 1
			
	return True if countX == countO else False

def main():

	result = ExOh("xooxxo")
	print result

if __name__ == "__main__":
  main()