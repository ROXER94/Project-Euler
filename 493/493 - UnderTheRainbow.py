# Calculates the expected number of distinct colors in 20 randomly picked balls

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

print(round(7*(1-nCr(60,20)/nCr(70,20)),10))