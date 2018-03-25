# Calculates the sum of the numbers n not exceeding 10^16 for which g(n) = n

from functools import reduce
from operator import mul
from collections import Counter

cache = {}

def factorial(n):
	if n not in cache:
		cache[n] = factorial_uncached(n)
	return cache[n]

def factorial_uncached(n):
	if n == 0: return 1
	else: return n*factorial(n-1)

def nCr(n,r):
	return factorial(n) // (factorial(r) * factorial(n-r))

def Omega(n):
	i = 2
	factors = Counter()
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors[i] += 1
	if n > 1:
		factors[n] += 1
	return list(factors.values())

def H(n):
	if len(n) == 1: O = Omega(n[0])
	else: O = n
	return sum((-1)**i * nCr(j,i) * reduce(mul,[nCr(O[k]+j-i-1,O[k]) for k in range(len(O))],1) for j in range(1,sum(O)+1) for i in range(j))

S = set()
for a in range(1,45):
	for b in range(1,5):
		for c in range(2):
			for d in range(c,2):
				for e in range(d,2):
					for f in range(e,2):
						n = H([a,b,c,d,e,f])
						if n < 10**16 and H([n]) == n:
							S.add(n)
print(sum(S)+1)