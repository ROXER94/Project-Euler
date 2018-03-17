# Calculates the number of semiprimes below 100,000,000

limit = 100000000
max = limit//2
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False
count = 0
sublimit = int(limit**.5)
for i in range(sublimit+1):
	if primes[i] < sublimit:
		for j in range(i,len(primes)):
			if primes[i] * primes[j] >= limit:
				break
			count += 1
	else:
		break
print(count)
