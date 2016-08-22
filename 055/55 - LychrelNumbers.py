# Calculates the number of Lychrel numbers below 10,000

def isPalindrome(string):
	if string == string[::-1]:
		return True
	else:
		return False

def Lychrel(string):
	return int(string) + int(string[::-1])

total = 0
Range = 10000
for i in range(Range):
	L = True
	count = 0
	value = str(i)
	while count < 50:
		value = Lychrel(str(value))
		if isPalindrome(str(value)):
			L = False
			break
		else:
			count += 1
	if L:
	    total += 1
print(total)