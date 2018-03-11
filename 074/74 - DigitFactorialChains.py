# Calculates the number of starting numbers below 1,000,000 that produce a digit factorial chain of exactly sixty non-repeating terms

cache = {}

def fact(n):
	if n not in cache.keys():
		cache[n] = factorial_uncached(n)
	return cache[n]

def factorial_uncached(n):
    if n == 0: return 1
    else: return n*fact(n-1)

count = 0
for i in range(1000000):
	s = set()
	match = False
	while not match:
		s.add(i)
		value = sum(fact(int(j)) for j in str(i))
		if value in s:
			match = True
		i = value
	if len(s) == 60:
		count += 1
print(count)
