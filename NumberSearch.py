#!/usr/bin/python -tt
import re

def NumberSearch(strng):

	total = 0
	ary = []
	ary = re.findall(r'\d+',strng)

	for i in ary:
		total += int(i)
		
	return total
def main():

	result = NumberSearch("88Hello 3World!")
	print result

if __name__ == "__main__":
  main()