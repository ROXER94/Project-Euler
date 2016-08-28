# Calculates the number of elements in the set of reduced proper fractions for d ≤ 1,000,000

def phi(n):
	pfactors = prime_factors(n)
	product = 1
	for i in pfactors:
		product *= (1-(1/i))
	return int(round(n * product))

def prime_factors(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return list(set(factors))

print(sum(phi(i) for i in range(1000001))-1)