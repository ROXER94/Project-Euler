# Calculates the number under 1,000,000 for which the value of the number/phi(number) is maximized

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

def phi(n):
	pfactors = prime_factors(n)
	product = 1
	for i in pfactors:
		product *= (1-(1/i))
	return int(n * product)

max = 0
for i in range(1,10000000):
	current = i/phi(i)
	if current > max:
		max = current
		value = i
print(value)