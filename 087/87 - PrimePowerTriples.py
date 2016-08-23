# Calculates the number of numbers below 50,000,000 that can be expressed as the sum of a prime square, prime cube, and prime fourth power

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

primes = [2] + [i for i in range(3,7070,2) if isPrime(i)]

Range = 50000000
array = []
for square in range(2,7072):
	if square in primes:
		for cube in range(2,369):
			if square**2 + cube**3 < Range:
				if cube in primes:
					for fourth in range(2,85):
						if fourth in primes:
							number = int(square**2 + cube**3 + fourth**4)
							if number < Range:
								array.append(number)
print(len(list(set(array))))