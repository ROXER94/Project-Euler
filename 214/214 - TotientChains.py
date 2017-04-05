# Calculates the sum of all primes less than 40,000,000 which generate a totient chain of length 25

max = 40000000
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False

def totient_gen(limit):
	phi = (limit+1)*[0]
	phi[1] = 1
	yield 1
	for n in range(2,limit):
		if phi[n] == 0:
			phi[n] = n - 1
			for j in range(2,int(limit/n)):
				if phi[j] != 0:
					q = j
					f = n - 1
					while q % n == 0:
						f *= n
						q //= n
					phi[n*j] = f * phi[q]
		yield phi[n]


totients = [""]+list(totient_gen(int(1.5*max)))[:max]

sum = 0
for p in primes:
	current = p
	chain = 1
	while current != 1:
		current = totients[current]
		chain += 1
	if chain == 25:
		sum += p
print(sum)