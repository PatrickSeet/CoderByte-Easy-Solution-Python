#!/usr/bin/python -tt
def LetterCapitalize(strng):

	inString = strng.split(" ")
	result = []
	for i in inString:
		s1 = i[0].upper()
		s2 = i[1:]
		result.append(s1+s2)

	return ' '.join(result)

def main():

	result = LetterCapitalize("i ran there")
	print result

if __name__ == "__main__":
  main()