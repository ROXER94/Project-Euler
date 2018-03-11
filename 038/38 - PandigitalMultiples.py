# Calculates the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2,...,n) where n > 1

def pandigital(n):
	total = ""
	i = 1
	while len(total) < 10:
		total += str(n * i)
		i += 1
	total = total[:9]
	if len("".join(set(total))) == 9 and "0" not in "".join(set(total)):
	    return int(total)
	return 0

Max = 0
for i in range(9999,9000,-1):
	Max = max(Max,pandigital(i))
print(Max)
