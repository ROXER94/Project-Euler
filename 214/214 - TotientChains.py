# Calculates the sum of all primes less than 40,000,000 which generate a totient chain of length 25

def totients(n):
	phi = [0]*(n+1)
	phi[1] = 1
	for i in range(1,n+1):
		if phi[i] == 0:
			phi[i] = i - 1
			for j in range(2,n//i+1):
				if phi[j] != 0:
					q = j
					f = i - 1
					while q % i == 0:
						f *= i
						q //= i
					phi[i*j] = f * phi[q]
		yield phi[i]

max = 40000000
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False

sum = 0
phi = list(totients(max))
for p in primes:
	current = p
	chain = 1
	while current != 1:
		current = phi[current]
		chain += 1
	if chain == 25:
		sum += p
print(sum)
