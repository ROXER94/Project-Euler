# Calculates the sum of all the primes below 100,000 that will never be a factor of R(10^n)

from math import gcd

def MultiplicativeOrder(a,n):
	if gcd(a,n) != 1:
		return -1
	r = 1
	k = 1
	while k < n:
		r = r*a % n
		if r == 1:
			return k
		k += 1
	return -1
 
def form(n):
	if n == 0:
		return -1
	while n%2==0:
		n //= 2
	while n%5==0:
		n //= 5
	return n == 1

max = 100000
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False

print(sum(p for p in primes if not form(MultiplicativeOrder(10,p)))+3)