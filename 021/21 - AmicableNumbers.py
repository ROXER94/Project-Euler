# Calculates the sum of all amicable numbers under 10,000

def properfactors(n):
	factors_array = []
	for x in range(1, n//2 + 1):
		if n % x == 0:
			factors_array.append(x)
	return factors_array

amicable = []
for i in range(1,10000):
	s = sum(properfactors(i))
	d = sum(properfactors(s))
	if i == d and s != d:
		amicable.append(i)
print(sum(amicable))