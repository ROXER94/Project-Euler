# Calculates the number of fractions that lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000

from fractions import Fraction

def FareySequence(n):
	array = []
	a = 1
	b = 3
	c = n//3
	d = n-1
	array.append(Fraction(a,b))
	array.append(Fraction(c,d))
	while c < n/2:
		p = (n+b)//d*c-a
		q = (n+b)//d*d-b
		array.append(Fraction(p,q))
		a = c
		b = d
		c = p
		d = q
	return array

n = 12000
array = FareySequence(n)
print(array.index(Fraction(1,2))-array.index(Fraction(1,3))-1)
