# Calculates the sum of c less than 120,000 for abc-hits 

from fractions import gcd
from functools import reduce
from operator import mul

def prime_factors(n):
	if n not in factors_cache:
		factors_cache[n] = prime_factors_uncached(n)
	return factors_cache[n]

def prime_factors_uncached(n):
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

rad_cache = {}
factors_cache = {}

def rad(n):
	if n not in rad_cache:
		rad_cache[n] = rad_uncached(n)
	return rad_cache[n]

def rad_uncached(n):
	return reduce(mul,prime_factors(n),1)

hits = 0
n = 120000
for a in range(1,n//2):
	if a%2==0:
		for b in range(a+1,n-a,2):
			c = a + b
			radc = rad(c)
			if radc < c//2:
				if rad(a)*rad(b)*radc < c:
					if gcd(a,b) == 1:
						hits += c
	else:
		for b in range(a+1,n-a):
			c = a + b
			radc = rad(c)
			if radc < c//2:
				if rad(a)*rad(b)*radc < c:
					if gcd(a,b) == 1:
						hits += c
print(hits)