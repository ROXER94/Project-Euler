# Calculates the sum of a set of five primes for which any two primes concatenate to produce another prime

max = 90000000
primes = {}
p = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes[i] = True
		p.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False
	else:
		primes[i] = False

def primeCheck(array):
	if len(array) == 2:
		return primes[int(str(array[0])+str(array[1]))] and primes[int(str(array[1])+str(array[0]))]
	if len(array) == 3:
		return primes[int(str(array[0])+str(array[2]))] and primes[int(str(array[2])+str(array[0]))] and primes[int(str(array[1])+str(array[2]))] and primes[int(str(array[2])+str(array[1]))]
	if len(array) == 4:
		return primes[int(str(array[0])+str(array[3]))] and primes[int(str(array[3])+str(array[0]))] and primes[int(str(array[1])+str(array[3]))] and primes[int(str(array[3])+str(array[1]))] and primes[int(str(array[2])+str(array[3]))] and primes[int(str(array[3])+str(array[2]))]
	if len(array) == 5:
		return primes[int(str(array[0])+str(array[4]))] and primes[int(str(array[4])+str(array[0]))] and primes[int(str(array[1])+str(array[4]))] and primes[int(str(array[4])+str(array[1]))] and primes[int(str(array[2])+str(array[4]))] and primes[int(str(array[4])+str(array[2]))] and primes[int(str(array[3])+str(array[4]))] and primes[int(str(array[4])+str(array[3]))]

for a in range(10):
	for b in range(a+1,700):
		if primeCheck([p[a],p[b]]):
			for c in range(b+1,755):
				if primeCheck([p[a],p[b],p[c]]):
					for d in range(c+1,900):
						if primeCheck([p[a],p[b],p[c],p[d]]):
							for e in range(d+1,1100):
								if primeCheck([p[a],p[b],p[c],p[d],p[e]]):
									print(p[a] + p[b] + p[c] + p[d] + p[e])
									quit()