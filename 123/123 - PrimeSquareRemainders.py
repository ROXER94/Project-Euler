# Calculates the smallest value of n for which the remainder first exceeds 10^10 in the equation (p(n)-1)^n + (p(n)+1)^n % p(n)^2

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

def PrimeSquareRemainder(n):
	return ((primes[n-1]-1)**(n) + (primes[n-1]+1)**(n)) % primes[n-1]**2

primes = [2] + [p for p in range(3,300000,2) if isPrime(p)]

n = 7037
while PrimeSquareRemainder(n) < 10000000000:
	n += 2
print(n)