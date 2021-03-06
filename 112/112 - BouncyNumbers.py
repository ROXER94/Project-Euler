# Calculates the least number for which the proportion of bouncy numbers is exactly 99%

def isIncreasing(number):
	number = str(number)
	for i in range(len(number)-1):
		if int(number[i]) <= int(number[i+1]):
			continue
		else:
			return False
	return True

def isDecreasing(number):
	number = str(number)
	for i in range(len(number)-1):
		if int(number[i]) >= int(number[i+1]):
			continue
		else:
			return False
	return True

def isBouncy(number):
    return not isIncreasing(number) and not isDecreasing(number)

count = 525
Range = 1000
while count/Range != .99:
	Range += 1
	if isBouncy(Range):
		count += 1
print(Range)
