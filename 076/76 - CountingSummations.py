# Calculates the number of different ways 100 can be written as a sum of at least two positive integers

def Factors(n):
	factors_array = []
	for x in range(1, n//2 + 1):
		if n % x == 0:
			factors_array.append(x)
	factors_array.append(n)
	return sum(factors_array)

cache = {0:1}
def P(n):
	if n not in cache:
		cache[n] = sum(Factors(n-k) * P(k) for k in range(n)) // n
	return cache[n]

print(P(100)-1)
