# Calculates a 12-digit number that is formed by concatenating the three terms in a unique sequence

max = 10000
primes = set()
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.add(i)
		for j in range(i * i, max, i):
			sieve[j] = False

for i in primes:
	if i > 1000:
		n = 4
		if i+3330 in primes and i+6660 in primes and i != 1487:
			array = [i,i+3330,i+6660]
			for j in str(array[0]):
				if j not in str(array[1]) or j not in str(array[2]):
					break
				else:
					n -= 1
		if n == 0:
			print(int(str(i)+str(i+3330)+str(i+6660)))
			break
