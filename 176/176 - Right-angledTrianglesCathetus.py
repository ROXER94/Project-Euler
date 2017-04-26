# Calculates the smallest integer that can be the length of a cathetus of exactly 47,547 different integer sided right-angled triangles

from functools import reduce
import operator

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
	return factors

max = 50
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False

n = 47547
P = prime_factors(2*n+1)[::-1]
print(reduce(operator.mul,[primes[P.index(p)]**((p-1)//2) for p in P[1:]],2**((P[0]+1)//2)))