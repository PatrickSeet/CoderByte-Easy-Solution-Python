#!/usr/bin/python -tt
def AlphabetSoup(strng):

	ary = list(strng)
	ary.sort()
	return ''.join(ary)

def main():

	result = AlphabetSoup("hooplah")
	print result

if __name__ == "__main__":
  main()