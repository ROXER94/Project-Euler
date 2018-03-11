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

P = {}
for p in primes:
	if p > 100000:
		P[p] = True

for p in primes:
	if p > 100000:
		count = 0
		i = p
		r = collections.Counter(str(p)).most_common(1)[0][0]
		i = int(str(i).replace(r,"0"))
		try:
			if P[i]:
				count += 1
		except:
			pass
		i = p
		i = int(str(i).replace(r,"1"))
		try:
			if P[i]:
				count += 1
		except:
			pass
		i = p
		i = int(str(i).replace(r,"2"))
		try:
			if P[i]:
				count += 1
		except:
			pass
		i = p
		i = int(str(i).replace(r,"3"))
		try:
			if P[i]:
				count += 1
		except:
			pass
		i = p
		i = int(str(i).replace(r,"4"))
		try:
			if P[i]:
				count += 1
		except:
			pass
		i = p
		i = int(str(i).replace(r,"5"))
		try:
			if P[i]:
				count += 1
		except:
			pass
		i = p
		i = int(str(i).replace(r,"6"))
		try:
			if P[i]:
				count += 1
		except:
			pass
		i = p
		i = int(str(i).replace(r,"7"))
		try:
			if P[i]:
				count += 1
		except:
			pass
		i = p
		i = int(str(i).replace(r,"8"))
		try:
			if P[i]:
				count += 1
		except:
			pass
		i = p
		i = int(str(i).replace(r,"9"))
		try:
			if P[i]:
				count += 1
		except:
			pass
		if count == 8:
			print(p)
			break
