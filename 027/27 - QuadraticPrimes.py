# Calculates the product of the coefficients, a and b, for the quadratic expression n^2+a*n+b that produces the maximum number of primes for consecutive values of n, starting with n=0

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

max = 1000
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False
	
max = 0
for a in range(1,1000,2):
	for b in primes:
		n = 0
		count = 0
		while isPrime(n**2+a*n+b):
			count += 1
			if count > max:
				max = count
				x = a
				y = b
			n += 1
		n = 0
		count = 0
		while isPrime(n**2-a*n+b):
			count += 1
			if count > max:
				max = count
				x = -a
				y = b
			n += 1
		n = 0
		count = 0
		while isPrime(n**2+a*n-b):
			count += 1
			if count > max:
				max = count
				x = a
				y = -b
			n += 1
		n = 0
		count = 0
		while isPrime(n**2-a*n-b):
			count += 1
			if count > max:
				max = count
				x = -a
				y = -b
			n += 1
print(x*y)
