# Calculates the number of non-happy numbers below 10,000,000

cache = {}

def chain(n):
	if n not in cache.keys():
		cache[n] = chain_uncached(n)
	return cache[n]

def chain_uncached(n):
	s = sum(int(i)**2 for i in str(n))
	if s == 89:
		return True
	elif s == 1:
		return False
	else:
		return chain(s)

print(sum(1 for i in range(1,10000000) if chain(i)))
