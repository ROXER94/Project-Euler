# Calculates the smallest prime in an eight prime value family

import collections

max = 1000000
primes = []
sieve = [True] * max
for i in range(2, max):
    if sieve[i]:
        primes.append(i)
        for j in range(i * i, max, i):
            sieve[j] = False

primes = primes[9592:]

array = []
for p in primes:
	count = 0
	i = p
	r = collections.Counter(str(p)).most_common(1)[0][0]
	i = int(str(i).replace(r,"0"))
	if i in primes:
		count += 1
	i = p
	i = int(str(i).replace(r,"1"))
	if i in primes:
		count += 1
	i = p
	i = int(str(i).replace(r,"2"))
	if i in primes:
		count += 1
	i = p
	i = int(str(i).replace(r,"3"))
	if i in primes:
		count += 1
	i = p
	i = int(str(i).replace(r,"4"))
	if i in primes:
		count += 1
	i = p
	i = int(str(i).replace(r,"5"))
	if i in primes:
		count += 1
	i = p
	i = int(str(i).replace(r,"6"))
	if i in primes:
		count += 1
	i = p
	i = int(str(i).replace(r,"7"))
	if i in primes:
		count += 1
	i = p
	i = int(str(i).replace(r,"8"))
	if i in primes:
		count += 1
	i = p
	i = int(str(i).replace(r,"9"))
	if i in primes:
		count += 1
	if count == 8:
		print(p)
		break