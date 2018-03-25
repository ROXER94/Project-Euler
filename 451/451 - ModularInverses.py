# Calculates the sum of largest positive number m smaller than n-1 such that the modular inverse of m modulo n equals m itself for 3 ≤ n ≤ 20,000,000

from math import log

max = 20000000
primes = set()
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.add(i)
		for j in range(i * i, max, i):
			sieve[j] = False

Sum = 0
array = [0] * (max+1)
for i in range(2,max+1):
	if i in primes:
		for j in range(i,max+1,i):
			array[j] = i
primes.remove(2)
seen = {1,2,4}
for e in range(3,int(log(max,2))+1):
	value = 2**e
	seen.add(value)
	Sum += value//2 + 1
for p in primes:
	for e in range(1,int(log(max,3))+1):
		value = p**e
		if value <= max:
			seen.add(value)
			Sum += 1
		else:
			break
		if 2 * value <= max:
			seen.add(2*value)
			Sum += 1
for n in range(3,max+1):
	if n not in seen:
		for m in range(n-array[n],-1,-array[n]):
			if (m+1)**2 % n == 1:
				Sum += m+1
				break
			if (m-1)**2 % n == 1:
				Sum += m-1
				break
print(Sum+1)