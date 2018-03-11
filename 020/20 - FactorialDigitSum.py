# Calculates the sum of the digits in 100!

cache_fact = {}

def fact(n):
	if n not in cache_fact.keys():
		cache_fact[n] = factorial_uncached(n)
	return cache_fact[n]
	
def factorial_uncached(n):
    if n == 0: return 1
    else: return n*fact(n-1)

print(sum(int(i) for i in str(fact(100))))
