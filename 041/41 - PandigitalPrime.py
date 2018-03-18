# Calculates the largest n-digit pandigital prime

from itertools import permutations

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

perms = [''.join(p) for p in permutations(str(7654321))]
for i in perms:
	if isPrime(int(i)):
		print(i)
		break
