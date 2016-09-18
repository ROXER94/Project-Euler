# Calculates the minimum size of cuboids, up to a maximum size of N x N x N, for which the shortest path has integer length and the number of solutions first exceeds 1,000,000

from math import sqrt

def isSquare(integer):
    root = sqrt(integer)
    return int(root + 0.5) ** 2 == integer

max = 2000
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False

squares = {}
for i in range(1,6000):
	squares[i] = i**2

cache = {}
count = 2
for n in range(1,2000):
	if n not in primes:
		current = 0
		for a in range(1,n+1):
			for b in range(a,n+1):
				x = squares[a+b] + squares[n]
				if x not in cache:
					cache[x] = isSquare(x)
				if cache[x]:
					current += 1
		count += current
	if count > 1000000:
		print(n)
		break
