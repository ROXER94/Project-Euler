# Calculates the sum of all primes below 2,000,000

max = 2000000
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False

print(sum(primes))
