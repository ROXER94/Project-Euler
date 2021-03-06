# Calculates the 30th number for which the sum of its digits is some number raised to a power

def digitpowersum(n):
	s = sum(int(i) for i in str(n))
	if s == 1:
		return False
	while n / s % 1 == 0:
		n /= s
	return n == 1

set = set()
for base in range(3,70):
	for exponent in range(3,10):
		value = base**exponent
		if digitpowersum(value):
			set.add(value)

print(sorted(list(set))[29])
