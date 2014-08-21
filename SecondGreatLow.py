#!/usr/bin/python -tt

def SecondGreatLow(ary):

	answer = []
	ary = list(set(ary))
	ary.sort()

	if len(ary) == 2:
		return ary
	else:
		ary.remove(ary[0])
		ary.remove(ary[-1])
		largest = max(ary)
		smallest = min(ary)
		answer.extend((smallest,largest))

	return answer

def main():

	result = SecondGreatLow([7, 7, 12, 98, 106])
	print result

if __name__ == "__main__":
  main()