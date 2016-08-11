# Calculates the product of the coefficients, a and b, for the quadratic expression n^2+a*n+b that produces the maximum number of primes for consecutive values of n, starting with n=0

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

primes = [2] + [p for p in range(3,1001,2) if isPrime(p)]
	
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