# Calculates the number of numbers below 50,000,000 that can be expressed as the sum of a prime square, prime cube, and prime fourth power

max = 7070
primes = []
sieve = [True] * max
for i in range(2, max):
	if sieve[i]:
		primes.append(i)
		for j in range(i * i, max, i):
			sieve[j] = False

Range = 50000000
set = set()
for square in range(2,7072):
	if square in primes:
		for cube in range(2,369):
			if square**2 + cube**3 < Range:
				if cube in primes:
					for fourth in range(2,85):
						if fourth in primes:
							number = int(square**2 + cube**3 + fourth**4)
							if number < Range:
								set.add(number)
print(len(set))
