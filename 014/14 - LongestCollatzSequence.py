# Calculates the number that produces the longest Collatz sequence under one million

cache = {}
n = 1000000

def Collatz(n):
	if n not in cache.keys():
		cache[n] = Collatz_uncached(n)
	return cache[n]

def Collatz_uncached(n):
	if n == 1:
		return 1
	elif n%2 != 0:
		return 2 + Collatz((3 * n + 1) / 2)
	else:
		return 1 + Collatz(n / 2)

chain = 0
for i in range(1,n):
	Collatz(i)
	if cache[i] > chain:
		chain = cache[i]
		value = i

print(value)