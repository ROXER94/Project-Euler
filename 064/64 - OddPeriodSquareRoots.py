# Calculates the number of continued fractions for N ≤ 10,000 that have an odd period

from math import sqrt

def isSquare(n):
	return int(sqrt(n)+.5)**2 == n

cache = {}
for i in range(1,10001):
	if not isSquare(i):
		array = []
		n = i
		residue = int(n**.5)
		denominator = residue
		numerator = n-denominator**2

		while True:
			sequence = (residue+denominator)//numerator
			array.append(sequence)    
			newDenominator = sequence*numerator-denominator    
			newNumerator = (n-newDenominator**2)/numerator			
			denominator = newDenominator
			numerator = newNumerator
			
			if newNumerator == 1:
				break

		array.append(2*residue)
		if len(array) == 2 and array[0] == array[1]:
			del array[0]
		cache[i] = array

print(sum(1 for i in cache.values() if len(i) % 2 != 0))
