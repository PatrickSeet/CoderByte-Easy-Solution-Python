#!/usr/bin/python -tt

def MeanMode(ary):

	ary.sort()
	mode =mean = modeCount = 0

	#calculate mean
	for numbers in ary:
		mean += numbers
	mean = mean / len(ary)

	#find mode
	for i in range(len(ary)-1):
		if ary[i] == ary[i+1]:
			modeCount += 1
			mode = ary[i]

	return 1 if mean == mode else 0

def main():

	result = MeanMode([5,3,3,3,1])
	print result

if __name__ == "__main__":
  main()