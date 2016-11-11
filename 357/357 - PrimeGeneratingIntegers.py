# Calculates the sum of all positive integers n below 100,000,000 such that the sum of each pair of factors of n is prime

max = 100000000
primes = {}
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes[i] = True
		for j in range(i * i, max, i):
			sieve[j] = False
	else:
		primes[i] = False

def Factors(n):
	valid = True
	for d in range(1, int(n**.5) + 1):
		if n % d == 0:
			if primes[d + n//d]:
				continue
			else:
				valid = False
				break
	return valid

print(sum([n for n in range(2,max+1,4) if primes[n+1] and Factors(n)]) + 1)
