# Calculates the product of a Pythagorean triplet that sums to 1000

from math import sqrt

for a in range(1,500):
	for b in range(a+1,500):
		c = sqrt(a**2 + b**2)
		if a + b + c == 1000:
			print(int(a*b*c))
			break