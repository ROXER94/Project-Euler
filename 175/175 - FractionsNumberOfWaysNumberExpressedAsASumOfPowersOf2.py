# Calculates the Shortened Binary Expansion of the smallest n for which f(n)/f(n-1) = 123456789/987654321

from fractions import Fraction

def continuedFraction(r):
	i = r.numerator // r.denominator
	f = r - i
	array.append(i)
	if f == 0: return
	continuedFraction(Fraction(1,f))

array = []
continuedFraction(Fraction(123456789,987654321))
array = array[1:]
if len(array) % 2 == 0:
	array[-1] -= 1
	array.append(1)
print(array[::-1])
