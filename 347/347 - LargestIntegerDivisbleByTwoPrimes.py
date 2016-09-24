# Calculates the sum of M(p,q,10,000,000) for all distinct primes p and q

from math import log

N = 100
maximum = N // 2
primes = []
sieve = [True] * maximum
for i in range(2, maximum):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, maximum, i):
			sieve[j] = False

def M(p,q):
	Range = int(log(N/q,p)) + 1
	array = [0]
	for i in range(1,Range):
		for j in range(1,Range):
			value = p**i*q**j
			if value <= N and value > array[0]:
				array[0] = value
	return array[0]

sum = 0
for p in primes:
	for q in primes[primes.index(p)+1:]:
		if p*q > N:
			break
		else:
			sum += M(p,q)
print(sum)