# Calculates the least number for which the proportion of bouncy numbers is exactly 99%

def isIncreasing(number):
	increasing = True
	number = str(number)
	for i in range(len(number)-1):
		if int(number[i]) <= int(number[i+1]):
			continue
		else:
			increasing = False
			break
	return increasing

def isDecreasing(number):
	decreasing = True
	number = str(number)
	for i in range(len(number)-1):
		if int(number[i]) >= int(number[i+1]):
			continue
		else:
			decreasing = False
			break
	return decreasing

def isBouncy(number):
    if number < 100:
        return False
    return not isIncreasing(number) and not isDecreasing(number)

count = 525
Range = 1000
while count/Range != .99:
	if isBouncy(Range+1):
		count += 1
	Range += 1
print(Range)