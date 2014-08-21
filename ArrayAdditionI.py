#!/usr/bin/python -tt
def ArrayAdditionI(ary):

	#sort array, take the largest, then compare
	ary.sort()
	total = 0
	largest = ary[-1]

	for i in range(len(ary)-1):
		total += ary[i]

	return True if total == largest else False

def main():

	result = ArrayAdditionI([3,5,-1,8,12])
	print result

if __name__ == "__main__":
  main()