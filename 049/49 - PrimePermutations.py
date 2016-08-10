# Calculates a 12-digit number that is formed by concatenating the three terms in a unique sequence

Primes = []

def isPrime(n):
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

for i in range(1000,10000):
	if isPrime(i):
		Primes.append(i)

n = 4
for i in Primes:
	array = []
	if i + 3330 in Primes and i + 6660 in Primes and i != 1487:
		array.append(i)
		array.append(i + 3330)
		array.append(i + 6660)
	if array:
		for j in str(array[0]):
			if j not in str(array[1]) or j not in str(array[2]):
				break
			else:
				n -= 1
			if n == 0:
				print(int(str(i)+str(i+3330)+str(i+6660)))