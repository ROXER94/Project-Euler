# Calculates the sum of all primes below 2,000,000

def isPrime(n):
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

print(sum([n for n in range(3,2000000,2) if isPrime(n)])+2)
