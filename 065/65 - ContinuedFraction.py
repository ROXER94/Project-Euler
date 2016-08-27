# Calculates the sum of the digits in the numerator of the 100th convergent of the continued fraction for e

from fractions import Fraction

array = [2,1]

k=2

convergent = 100

for i in range(convergent-2):
	if i%3==0:
		array.append(k)
		k += 2
	else:
		array.append(1)

def continuedFraction(array):
	if len(array) != 2:
		return array[0] + Fraction(1,continuedFraction(array[1:]))
	else:
		return array[0] + Fraction(1,array[1])

print(sum(int(i) for i in str(continuedFraction(array).numerator)))
