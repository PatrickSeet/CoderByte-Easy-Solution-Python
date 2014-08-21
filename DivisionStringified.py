#!/usr/bin/python -tt

import math

def DivisionStringified(n1,n2):

	answer = float(n1) / float(n2)
	answer = int(math.ceil(answer))

	result = ''
	strng = str(answer)
	if len(strng) >= 4:
		hundredsR = strng[-3:]
		hundredsL = strng[:-3]
		result = hundredsL + ',' + hundredsR
	else:
		result = answer

	return result 

def main():

	result = DivisionStringified(123456789,10000)
	print result

if __name__ == "__main__":
  main()