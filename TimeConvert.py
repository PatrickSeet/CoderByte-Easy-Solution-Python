#!/usr/bin/python -tt
def TimeConvert(num):

	hr = 0
	mins = 0.0
	hr = num / 60
	mins = num % 60
	hr = str(hr)
	mins = str(mins)
	
	return hr + ":" + mins

def main():

	result = TimeConvert(63)
	print result

if __name__ == "__main__":
  main()