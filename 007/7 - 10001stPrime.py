# Calculates the 10,001st prime number

max = 150000
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False
print(primes[10000])
