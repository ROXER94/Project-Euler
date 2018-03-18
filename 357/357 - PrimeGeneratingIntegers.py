# Calculates the sum of all positive integers n below 100,000,000 such that the sum of each pair of factors of n is prime

max = 100000000
P = {}
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		P[i] = True
		for j in range(i * i, max, i):
			sieve[j] = False
			P[j] = False

def isPrimeGeneratingInteger(n):
	for d in range(1, int(n**.5) + 1):
		if n % d == 0:
			if P[d + n//d]:
				continue
			else:
				return False
	return True

print(sum(n for n in range(2,max+1,4) if P[n+1] and isPrimeGeneratingInteger(n)) + 1)
