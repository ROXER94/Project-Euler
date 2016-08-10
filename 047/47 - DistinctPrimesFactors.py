# Calculates the first of four consecutive integers to have four distinct prime factors

def prime_factors(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	newfactors = []
	for i in factors:
		if factors.count(i) == 1:
			newfactors.append(i)
		else:
			number = factors.count(i)
			newfactors.append(i**number)
	return list(set(newfactors))

n = 1
while True:
	array = []
	pfactors1 = prime_factors(n)
	if len(pfactors1) == 4:
		pfactors2 = prime_factors(n+1)
		if len(pfactors2) == 4:
			pfactors3 = prime_factors(n+2)
			if len(pfactors3) == 4:
				pfactors4 = prime_factors(n+3)
				if len(pfactors4) == 4:
					for i in pfactors1:
						array.append(i)
					for i in pfactors2:
						if i in array:
							break
						else:
							array.append(i)
					if len(array) != 8:
						break
					for i in pfactors3:
						if i in array:
							break
						else:
							array.append(i)
					if len(array) != 12:
						break
					for i in pfactors4:
						if i in array:
							break
						else:
							array.append(i)
					if len(array) == 16:
						break
	n += 1
print(n)