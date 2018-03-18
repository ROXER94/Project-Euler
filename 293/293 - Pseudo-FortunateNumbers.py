# Calculates the sum of all distinct pseudo-Fortunate numbers for admissible numbers less than 10^9

def isPrime(n):
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i * i <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True

admissible = []
def Admissable(index,product,N=1000000000):
	if (index == len(primes)):
		return
	while (product < N):
		product *= primes[index]
		if (product < N):
			admissible.append(product)
		Admissable(index+1,product)

max = 24
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False
S = set()
Admissable(0,1)
for i in admissible:
	j = 3
	while True:
		if isPrime(i+j):
			break
		j += 2
	S.add(j)
print(sum(S))
