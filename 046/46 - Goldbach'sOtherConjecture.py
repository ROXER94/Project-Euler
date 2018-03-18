# Calculates the smallest odd composite that cannot be written as the sum of a prime and twice a square

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

primes = [2]
composites = []
for n in range(3,10001,2):
	if isPrime(n):
		primes.append(n)
	else:
		composites.append(n)
doublesquares = [2*n**2 for n in range(1,71)]

array = []
for p in primes:
	for ds in doublesquares:
		if p + ds not in array and (p + ds) % 2 != 0 and not isPrime(p + ds):
			array.append(p+ds)

print(list(set(composites).difference(array))[0])
