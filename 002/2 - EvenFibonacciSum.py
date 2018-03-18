# Calculates the sum of the even terms of the Fibonacci sequence under 4,000,000

cache_fib = {}

def fib(n):
	if n not in cache_fib.keys():
		cache_fib[n] = fibonacci_uncached(n)
	return cache_fib[n]

def fibonacci_uncached(n):
	if n < 2: return n
	else: return fib(n-1) + fib(n-2)

print(sum(fib(x) for x in range(1,10000) if fib(x) < 4000000 and fib(x) % 2 == 0))
