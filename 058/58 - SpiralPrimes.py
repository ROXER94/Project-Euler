# Calculates the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%

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

ratio = 1
n = 3
sum = 1
primes = 0
while ratio > .10:
	corner1 = n**2-1*(n-1)
	corner2 = n**2-2*(n-1)
	corner3 = n**2-3*(n-1)
	if isPrime(corner1):
		primes += 1
	if isPrime(corner2):
		primes += 1
	if isPrime(corner3):
		primes += 1
	sum += 4
	ratio = primes/sum
	n += 2
print(n-2)