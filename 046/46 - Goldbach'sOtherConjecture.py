# Calculates the smallest odd composite that cannot be written as the sum of a prime and twice a square

def isPrime(n):
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
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