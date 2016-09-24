# Calculates the sum of S(p) for primes between 5 and 100,000,000

def S(p):
	q = p // 2
	return (p * (p - 1) - q * (q - 1)) // 2 % p

max = 100000000
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False
print(sum(S(p) for p in primes[2:]))