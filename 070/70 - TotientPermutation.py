# Calculates the number under 10,000,000 for which the value of the number/phi(number) is minimized and phi(number) is a permutation of the number

import collections

def same_permutation(a,b):
    d = collections.defaultdict(int)
    for x in a:
        d[x] += 1
    for x in b:
        d[x] -= 1
    return not any(d.values())

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
	return int(round(n * product))

min = 1.5
for i in range(2,10000000):
	totient = phi(i)
	current = i/totient
	if len(str(i)) == len(str(totient)):
		if same_permutation(str(i),str(totient)):
			if current < min:
				min = current
				value = i
print(value)