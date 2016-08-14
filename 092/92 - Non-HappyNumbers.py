# Calculates the number of non-happy numbers below 10,000,000

cache = {}

def chain(n):
	if n not in cache.keys():
		cache[n] = chain_uncached(n)
	return cache[n]


def chain_uncached(n):
	s = 0
	for i in str(n):
		s += int(i)**2
	if s == 89:
		return True
	elif s == 1:
		return False
	else:
		return chain(s)

count = 0
for i in range(1,10000000):
	if chain(i):
		count += 1
print(count)