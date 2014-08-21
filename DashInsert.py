#!/usr/bin/python -tt

def DashInsert(num):

	result = []
	strng = str(num)

	#loop through to check consecutive odd numbers, add '-' if consecutive
	for i in range(len(strng)-1):
		if int(strng[i]) % 2 != 0 and int(strng[i+1]) % 2 != 0:
			result.extend((strng[i],'-'))
		else:
			result.append(strng[i])

	result.append(strng[-1])
	
	return ''.join(result)

def main():

	result = DashInsert(56730)
	print result

if __name__ == "__main__":
  main()