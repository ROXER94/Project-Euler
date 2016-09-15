# Calculates the index of the first Fibonacci number for which the first and last nine digits are 1-9 pandigital

cache = {1:1,2:1}

def fibonacci(n):
	if n not in cache:
		cache[n] = fibonacci(n-1) + fibonacci(n-2)
	return cache[n]

def isPandigital(n):
	n = str(n)
	return "1" in n and "2" in n and "3" in n and "4" in n and "5" in n and "6" in n and "7" in n and "8" in n and "9" in n

n = 1
while not (isPandigital(fibonacci(n)%1000000000) and isPandigital(str(fibonacci(n))[:9])):
	n += 1
print(n)
