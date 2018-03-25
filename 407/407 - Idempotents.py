# Calculates the sum of the largest value of a < n such that a^2 ≡ a (mod n) for 1 ≤ n ≤ 10,000,000

from math import log

max = 10000000
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
seen = {1,2,4}
for p in primes:
	for e in range(1,int(log(max,3))+1):
		value = p**e
		if value <= max:
			seen.add(value)
			Sum += 1
		else:
			break
for n in range(1,max+1):
	if n not in seen:
		for a in range(n-array[n],-1,-array[n]):
			if (a+1)**2 % n == a+1:
				Sum += a+1
				break
			if a**2 % n == a:
				Sum += a
				break
print(Sum)