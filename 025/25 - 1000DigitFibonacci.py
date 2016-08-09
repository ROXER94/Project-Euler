# Calculates the index of the first term in the Fibonacci sequence to contain 1000 digits

cache_fib = {}

def fib(n):
    if n not in cache_fib.keys():
        cache_fib[n] = fibonacci_uncached(n)
    return cache_fib[n]

def fibonacci_uncached(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

number = 0
while len(str(fib(number))) < 1000:
	number += 1
print(number)