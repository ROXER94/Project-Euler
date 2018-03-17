# Calculates the number of primes below 1,000,000 where n^3 + p*n^2 is a perfect cube

max = 1000000
P = {1:False}
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		P[i] = True
		for j in range(i * i, max, i):
			sieve[j] = False
			P[j] = False

print(sum(1 for i in range(1000) if 3*i**2 + 3*i + 1 < 1000000 and P[3*i**2 + 3*i + 1]))
