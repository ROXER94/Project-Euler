# Calculates the values of nCr, for 1 ≤ n ≤ 100, that are greater than 1,000,000

cache = {}

def fact(n):
	if n not in cache.keys():
		cache[n] = factorial_uncached(n)
	return cache[n]

def factorial_uncached(n):
    if n == 0: return 1
    else: return n*fact(n-1)

def nCr(n,r):
	return fact(n)//(fact(r)*fact(n-r))

print(sum(1 for r in range(1,101) for n in range(r,101) if nCr(n,r) > 1000000))
