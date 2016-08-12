# Calculates the largest n-digit pandigital prime

from itertools import permutations

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

perms = [''.join(p) for p in permutations(str(7654321))]
for i in perms:
	if isPrime(int(i)):
		print(i)
		break