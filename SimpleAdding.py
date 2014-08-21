#!/usr/bin/python -tt
def SimpleAdding(num):

	total = 0
	for i in range(num+1):
		total += i

	return total

def main():

	result = SimpleAdding(140)
	print result

if __name__ == "__main__":
  main()