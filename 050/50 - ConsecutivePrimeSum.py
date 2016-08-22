# Calculates the prime below 1000000 that can be written as the sum of the most consecutive primes

from itertools import accumulate

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

primes = [2]
i = 3
while sum(primes) < 1000000:
	if isPrime(i):
		primes.append(i)
	i += 2
primes = primes[:-1]

max = 0
start = 0
while start != len(primes):
	accumulated = list(accumulate(primes[start:]))
	newaccumulated = []
	for i in accumulated:
		if i%2!=0 and str(i)[-1] != "5":
			newaccumulated.append(i)
	newprimes = []
	for i in newaccumulated:
		if isPrime(i):
			newprimes.append(i)
	current = accumulated.index(newprimes[-1]) + 1
	if current > max:
		max = current
		prime = newprimes[-1]
	start += 1
print(prime)