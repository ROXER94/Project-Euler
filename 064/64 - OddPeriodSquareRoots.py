# Calculates the number of continued fractions for N ≤ 10,000 that have an odd period

from math import sqrt

def isSquare(integer):
	root = sqrt(integer)
	if int(root + 0.5) ** 2 == integer: 
		return True
	else:
		return False

cache = {}
for i in range(1,10001):
	if not isSquare(i):
		array = []
		n = i
		residue = int(n ** 0.5)
		denominator = residue
		numerator = n - denominator **2

		while True:
			newarray = int((residue+denominator)/numerator)
			array.append( newarray )    
			newDenominator = (newarray * numerator) - denominator    
			newNumerator = (n - newDenominator **2)/numerator

			if newNumerator == 1:
				break
			denominator = newDenominator
			numerator = newNumerator

		array.append(2*residue)
		if len(array) == 2 and array[0] == array[1]:
			del array[0]
		cache[i] = array

count = 0
for i in cache.values():
	if len(i) % 2 != 0:
		count += 1
print(count)