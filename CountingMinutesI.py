#!/usr/bin/python -tt

def isPM(strng):

	#function to check PM or AM, return True if PM
	if strng[-2] == 'p' or strng[-2] == 'P':
		return True
	else:
		return False

def convertTime(strng):

	#function to convert incoming time as strng and return minutes
	totalMinutes = 0

	#if the strng is in "12:00" format
	if len(strng) == 7:
		tmpHr = int(strng[0:2])
		tmpMin = int(strng[3:5])
		if isPM(strng):
			#12 PM is special case
			if tmpHr != 12:
				tmpHr = (tmpHr + 12) * 60
			else:
				tmpHr = tmpHr * 60
		else:
			if tmpHr == 12:
				tmpHr = 0
			else:
				tmpHr = tmpHr * 60
		totalMinutes = tmpHr + tmpMin

	#if the strng is in "1:00" format
	if len(strng) == 6:
		tmpHr = int(strng[0:1])
		tmpMin = int(strng[2:4])
		if isPM(strng):
			#12 PM is special case
			if tmpHr != 12:
				tmpHr = (tmpHr + 12) * 60
			else:
				tmpHr = tmpHr * 60
		else:
			if tmpHr == 12:
				tmpHr = 0
			else:
				tmpHr = tmpHr * 60
		totalMinutes = tmpHr + tmpMin
	
	return totalMinutes

def CountingMinutesI(strng):

	ary = strng.split('-')
	startStrng = ary[0]
	endStrng = ary[1]
	result = 0

	#calling convertTime to get start mins and end mins
	startTime = convertTime(startStrng)
	endTime = convertTime(endStrng)

	#finding the difference in minutes between the 2 times
	if endTime == 0:
		result = 24 * 60 - startTime
	elif endTime < startTime:
		result = (endTime + 24 * 60) - startTime
	else:
		result = endTime - startTime

	return result

def main():

	result = CountingMinutesI("12:30pm-12:00am")
	print result

if __name__ == "__main__":
  main()