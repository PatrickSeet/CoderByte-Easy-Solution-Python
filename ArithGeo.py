#!/usr/bin/python -tt
def ArithGeo(ary):

	result = ''
	ary.sort()
	for i in range(len(ary) - 2):
		if ary[i+1] / ary[i] == ary[i+2] / ary[i+1]:
			result = 'Geometric'
		elif ary[i+1] - ary[i] == ary[i+2] - ary[i+1]:
			result = 'Arithmetic'
		else:
			result = '-1'
	return result

def main():

	result = ArithGeo([2,6,18,54])
	print result

if __name__ == "__main__":
  main()