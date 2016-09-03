# Calculates the number of primes below 1,000,000 where n^3 + p*n^2 is a perfect cube

max = 1000000
primes = []
sieve = [True] * max
for i in range(2, max):
    if sieve[i]:
        primes.append(i)
        for j in range(i * i, max, i):
            sieve[j] = False		

count = 0
for n in range(1000):
	if 3*n**2 + 3*n + 1 in primes:
		count += 1
print(count)