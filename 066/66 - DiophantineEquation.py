# Calculates the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained

from math import sqrt
from fractions import Fraction

def isSquare(integer):
	root = sqrt(integer)
	if int(root + 0.5) ** 2 == integer: 
		return True
	else:
		return False

def continuedFraction(array):
	if len(array) != 2:
		return array[0] + Fraction(1,continuedFraction(array[1:]))
	else:
		return array[0] + Fraction(1,array[1])

def Diophantine(x,y,D):
	return x**2 - D * y**2 == 1

cache = {}
for i in range(1,1001):
	if not isSquare(i):
		n = i
		residue = int(n ** 0.5)
		r = residue
		array = []
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
		cache[i] = [r] + array * 2

max = 0
for i in cache:
	index = 2
	while True:
		fraction = continuedFraction(cache[i][:index])
		if Diophantine(fraction.numerator,fraction.denominator,i):
			break
		else:
			index += 1
	if fraction.numerator > max:
		max = fraction.numerator
		value = i
print(value)